#!/usr/bin/env python3
"""
Weekly auto-refine for HighLevel guide mockups.

Idempotent — running multiple times produces the same result. Applies the
mechanical transformations that keep mockups visually and structurally
aligned with the HighLevel Workflow Builder UI:

- Standardize action category labels (PT → real HL action names)
- Standardize filter section headers (Filters · X → Filters)
- Convert non-native Slack Message nodes → Outbound Webhook
- Specify trigger node-type (Trigger · X) per the trigger's title
- Replace generic placeholder values with realistic merge-field content
- Regenerate the configData click-panel JS so it mirrors the visible
  mockup node parameters

Hand-rewritten files are skipped (see HAND_CRAFTED).

Usage: python3 scripts/auto-refine.py [--check]
  --check  exit 1 if any file would change (useful for CI)
"""

import argparse
import glob
import html as html_lib
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(__file__), '..', 'deploy-highlevel')

# Files that are hand-rewritten to a higher fidelity. Their visible node
# bodies + configData are preserved as-is.
HAND_CRAFTED = {
    os.path.join(ROOT, 'guia-highlevel-cat01.html'),
    os.path.join(ROOT, 'guia-highlevel-cat02.html'),
    os.path.join(ROOT, 'guia-highlevel-cat03.html'),
    os.path.join(ROOT, 'guia-highlevel-cat04.html'),
    os.path.join(ROOT, 'guia-highlevel-cat05.html'),
    os.path.join(ROOT, 'guia-highlevel-cat06.html'),
    os.path.join(ROOT, 'guia-highlevel-cat07.html'),
    os.path.join(ROOT, 'guia-highlevel-cat08.html'),
    os.path.join(ROOT, 'guia-highlevel-cat09.html'),
    os.path.join(ROOT, 'guia-highlevel-cat10.html'),
    os.path.join(ROOT, 'guia-highlevel-cat11.html'),
    os.path.join(ROOT, 'guia-highlevel-cat12.html'),
    os.path.join(ROOT, 'acoes-highlevel-cat01.html'),
}

# ---------- 1. Label standardization ----------
PT_TO_EN_LABELS = {
    'Action · Comunicação':       'Action · Communication',
    'Action · Ferramenta Interna': 'Action · Workflow',
    'Action · Lógica':            'Action · If/Else',
    'Action · Temporização':      'Action · Wait',
    'Action · Contato':           'Action · Contact',
    'Action · Oportunidade':      'Action · Opportunity',
    'Action · Envio de Dados':    'Action · Webhook',
}

# ---------- 2. Filter header standardization ----------
FILTER_HEADERS = [
    'Filters · AND logic between rows',
    'Filters · AND logic',
    'Filters · opcionais',
    'Filters · opcional',
]

# ---------- 3. Slack replacement ----------
SLACK_REPLACEMENTS = [
    ('>Slack Message</div>',          '>Outbound Webhook (Slack)</div>'),
    ('<span>Slack Message</span>',    '<span>Outbound Webhook (Slack)</span>'),
    ('Action · Slack Message',        'Action · Webhook'),
]

# ---------- 4. Placeholder content replacement ----------
PLACEHOLDER_REPLACEMENTS = {
    'Conteúdo da notificação':                              'Lead {{contact.first_name}} pronto pra atendimento',
    'Detalhes da tarefa':                                   'Confirmar próximos passos com {{contact.first_name}}',
    'Mensagem dinâmica usando merge fields':                'Oi {{contact.first_name}}, tudo bem?',
    'Conteúdo da nota':                                     'Nota automática gerada pelo workflow',
    'Campo a comparar':                                     'Custom Value · Status',
    'Valor esperado':                                       'Qualificado',
    'Valor a atualizar':                                    'Status: Atualizado',
    'Novo valor':                                           'Atualizado via workflow',
    'Campo a atualizar':                                    'Custom Field · Status',
    'Pipeline atual':                                       'Pipeline ativa do contato',
    'Novo estágio':                                         'Próximo estágio',
    'Usuário responsável':                                  'Round-robin SDR',
    'Tag a remover':                                        'Lead Frio',
    'Action ID destino':                                    'Branch · Continue Fluxo',
    'Ver documentação HighLevel pra detalhes específicos':  'Configurar conforme necessidade',
    'sender@empresa.com.br':                                'lucas@magneticflows.com.br',
}

# ---------- 5. configData dropdown/chip/toggle heuristics ----------
DROPDOWN_FIELDS = {
    'From Email', 'User', 'Wait Type', 'Event Date Field', 'When', 'Operator',
    'Status', 'Pipeline', 'Stage', 'Assigned To', 'Method', 'Notification Type',
    'User Type', 'Field', 'Target Action', 'Model', 'Split Traffic',
    'Country', 'Source',
}
CHIPS_FIELDS = {'Users', 'Has Tag', "Doesn't Have Tag", 'Filters'}
REQUIRED_FIELDS = {
    'Action Name', 'Workflow Trigger Name', 'Title', 'Tag', 'URL', 'User',
    'Users', 'Pipeline', 'Stage', 'Subject', 'Message', 'Field', 'Operator',
    'Value', 'From Email', 'When', 'Number of Days', 'Notification Type',
    'User Type', 'Event Date Field', 'Wait Type', 'Duration', 'Email', 'To',
    'Prompt', 'Workflows',
}


def standardize_labels(s):
    for pt, en in PT_TO_EN_LABELS.items():
        s = s.replace(pt, en)
    return s


def standardize_filter_headers(s):
    for old in FILTER_HEADERS:
        old_tag = f'<div class="hl-section-head">{old}</div>'
        s = s.replace(old_tag, '<div class="hl-section-head">Filters</div>')
    return s


def fix_slack(s):
    for old, new in SLACK_REPLACEMENTS:
        s = s.replace(old, new)
    # Update configData kind for any Slack outbound webhook
    s = re.sub(
        r"kind: 'Action · Communication', title: 'Outbound Webhook \(Slack\)'",
        "kind: 'Action · Webhook', title: 'Outbound Webhook (Slack)'",
        s,
    )
    return s


def fix_placeholders(s):
    for old, new in PLACEHOLDER_REPLACEMENTS.items():
        s = s.replace(old, new)
    return s


def specify_trigger_types(s):
    """Set each gX-1 / aX-1 trigger node type to 'Trigger · {title}'."""
    pattern = re.compile(
        r'(<div class="ghl-node" data-node-id="[a-z]+\d+-1">'
        r'.*?<div class="ghl-node-icon trigger">[^<]+</div>\s*<div>\s*'
        r'<div class="ghl-node-type">)([^<]+)(</div>\s*'
        r'<div class="ghl-node-title">([^<]+)</div>)',
        re.DOTALL,
    )

    def repl(m):
        title = m.group(4).strip()
        new_type = f'Trigger · {title}'
        if m.group(2).strip() == new_type:
            return m.group(0)
        return m.group(1) + new_type + m.group(3)

    return pattern.sub(repl, s)


def regenerate_config_data(s):
    """Auto-build configData JS object from visible node params."""
    cd_match = re.search(r'(  const configData = \{)(.*?)(\n  \};)', s, re.DOTALL)
    if not cd_match:
        return s

    seen = {}
    for m in re.finditer(r'<div class="ghl-node" data-node-id="([^"]+)">', s):
        node_id = m.group(1)
        chunk = s[m.start():m.start() + 8000]

        tm = re.search(r'<div class="ghl-node-type">([^<]+)</div>', chunk)
        tl = re.search(r'<div class="ghl-node-title">([^<]+)</div>', chunk)
        body_m = re.search(
            r'<div class="ghl-node-body">(.*?)</div>\s*</div>\s*'
            r'(?:<div class="ghl-connector"|<div class="config-panel"|</div>|<div class="ghl-node")',
            chunk, re.DOTALL,
        )
        if not body_m:
            continue
        params = []
        for pm in re.finditer(
            r'<div class="ghl-node-param"><span class="pk">([^<]+)</span>'
            r'<span class="pv([^"]*)">([^<]+)</span></div>',
            body_m.group(1),
        ):
            params.append((pm.group(1).strip(), pm.group(3).strip(), 'highlight' in pm.group(2)))
        if not params:
            continue
        seen[node_id] = {
            'type': tm.group(1).strip() if tm else 'Unknown',
            'title': tl.group(1).strip() if tl else 'Untitled',
            'params': params,
        }

    def build_panel(params):
        sections = []
        for key, value, is_highlight in params:
            is_req = key in REQUIRED_FIELDS
            is_action_name = key == 'Action Name'
            label_html = key + (' *' if is_req else '')

            if key in CHIPS_FIELDS or (key in ('Notification Type', 'Tag') and ('+' in value or ', ' in value)):
                tokens = re.split(r'[,+]', value)
                tokens = [re.sub(r'\s*\([^)]*\)\s*', '', t).strip() for t in tokens]
                tokens = [t for t in tokens if t]
                chip_html = ' '.join(
                    f'<span class="opt-chip">{html_lib.escape(t)}</span>' for t in tokens
                )
                sections.append(
                    f'<div class="config-section"><div class="config-label">{label_html}'
                    f'</div><div class="config-field">{chip_html}</div></div>'
                )
                continue

            if value.upper() in ('ON', 'OFF') or value.upper().startswith('ON ') or value.upper().startswith('OFF '):
                symbol = '🟢' if value.upper().startswith('ON') else '⚪'
                sections.append(
                    f'<div class="config-section"><div class="config-label">{label_html}'
                    f'</div><div class="config-field">{symbol} {html_lib.escape(value)}</div></div>'
                )
                continue

            classes = ['config-field']
            if is_action_name or is_highlight:
                classes.append('highlight')
            if key in DROPDOWN_FIELDS or value.startswith('Is — ') or value.startswith('Has Changed'):
                classes.append('dropdown')
            cls = ' '.join(classes)
            sections.append(
                f'<div class="config-section"><div class="config-label">{label_html}'
                f'</div><div class="{cls}">{html_lib.escape(value)}</div></div>'
            )
        return ''.join(sections)

    def js_escape(x):
        return x.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')

    lines = []
    for node_id, node in seen.items():
        body = js_escape(build_panel(node['params']))
        lines.append(
            f"    '{node_id}': {{ kind: '{node['type']}', title: '{node['title']}', body: `{body}` }},"
        )
    if lines:
        lines[-1] = lines[-1].rstrip(',')

    new_cd = cd_match.group(1) + '\n' + '\n'.join(lines) + cd_match.group(3)
    return s[:cd_match.start()] + new_cd + s[cd_match.end():]


TRANSFORMS = [
    ('labels',            standardize_labels),
    ('filter-headers',    standardize_filter_headers),
    ('slack',             fix_slack),
    ('placeholders',      fix_placeholders),
    ('trigger-types',     specify_trigger_types),
    ('config-data',       regenerate_config_data),
]


def process_file(fp):
    with open(fp) as f:
        orig = f.read()
    s = orig
    for _, fn in TRANSFORMS:
        s = fn(s)
    if s == orig:
        return False
    with open(fp, 'w') as f:
        f.write(s)
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true',
                        help='exit 1 if any file would change')
    args = parser.parse_args()

    files = sorted(glob.glob(os.path.join(ROOT, '*-cat*.html')))
    files = [f for f in files if os.path.realpath(f) not in {os.path.realpath(h) for h in HAND_CRAFTED}]

    if args.check:
        for fp in files:
            with open(fp) as f:
                orig = f.read()
            s = orig
            for _, fn in TRANSFORMS:
                s = fn(s)
            if s != orig:
                print(f'would change: {os.path.basename(fp)}')
                sys.exit(1)
        print('all files clean')
        return

    changed = []
    for fp in files:
        if process_file(fp):
            changed.append(os.path.basename(fp))

    if changed:
        print(f'updated {len(changed)} files:')
        for name in changed:
            print(f'  {name}')
    else:
        print('no changes')


if __name__ == '__main__':
    main()
