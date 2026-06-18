#!/usr/bin/env python3
"""Build the verification audit checklist (AUDIT.md).

Walks every category page, lists each trigger / action with the current
fidelity signals we can measure from the file:

- Hand-crafted vs auto-generated (was this page in HAND_CRAFTED?)
- How many configData fields the click panel shows
- Whether the HL Config Panel above the mockup uses real HL field types
  (hl-input, hl-dropdown, hl-toggle, hl-tag-picker)
- Whether the visible workflow node bodies have at least 3 params
- Whether the action title looks like a real HL action name

Outputs AUDIT.md ordered Gatilhos → Ações, with a per-item confidence
rating (Alta / Média / Baixa) and a 'verify' column for human review.
"""

import glob
import json
import os
import re

ROOT = os.path.join(os.path.dirname(__file__), '..', 'deploy-highlevel')
OUTPUT = os.path.join(os.path.dirname(__file__), '..', 'AUDIT.md')

HAND_CRAFTED_TRIGGERS = {f'cat{n:02d}' for n in range(1, 13)}  # all 12 trigger pages
HAND_CRAFTED_ACTIONS = {f'cat{n:02d}' for n in range(1, 15)}   # all 14 action pages


def count_config_fields(panel_html):
    """How many config-section blocks are in the JS body for this entry?"""
    return panel_html.count('<div class="config-section">')


def parse_page(fp, kind):
    """Return list of dicts per entry on this page."""
    with open(fp) as f:
        html = f.read()
    fname = os.path.basename(fp)
    catnum = re.search(r'cat(\d+)', fname).group(0)

    name_class = f'{kind}-name'
    block_class = f'{kind}-block'
    en_class = f'{kind}-en'
    cat_class = f'{kind}-cat'

    blocks = re.findall(
        rf'<div class="{block_class}" id="([^"]+)"[^>]*>(.*?)'
        rf'(?=<div class="{block_class}"|<!-- GATILHO|<!-- AÇÃO|<!-- ═══════════════════════════════════════════════════════════════════════\s*\n\s*GATILHO|<!-- ═══════════════════════════════════════════════════════════════════════\s*\n\s*AÇÃO|<nav class="cat-nav"|<div class="guide-footer)',
        html, re.DOTALL,
    )

    # Parse configData entries to count fields per node
    cd_field_count = {}
    for m in re.finditer(
        r"'([ga]\d+-\d+)':\s*\{\s*kind:\s*'([^']*)',\s*title:\s*'([^']*)',\s*body:\s*`([^`]*)`",
        html,
    ):
        node_id, _, _, body = m.group(1), m.group(2), m.group(3), m.group(4)
        cd_field_count[node_id] = body.count('<div class="config-section">')

    # HL Config Panel detection per trigger/action
    out = []
    for anchor, body in blocks:
        if not anchor.startswith(('g', 'a')):
            continue
        name_m = re.search(rf'<h2 class="{name_class}">([^<]+)</h2>', body)
        en_m = re.search(rf'<div class="{en_class}">([^<]+)</div>', body)
        cat_m = re.search(rf'<div class="{cat_class}">([^<]+)</div>', body)
        name = name_m.group(1).strip() if name_m else anchor
        en = en_m.group(1).strip() if en_m else ''
        category = cat_m.group(1).strip() if cat_m else ''

        # Field signal from the trigger's first node (gN-1 or aN-1)
        trigger_node = f'{anchor}-1'
        click_panel_fields = cd_field_count.get(trigger_node, 0)
        action_fields = [cd_field_count.get(f'{anchor}-{i}', 0) for i in range(2, 9) if f'{anchor}-{i}' in cd_field_count]

        # HL Config Panel above the mockup
        has_hl_panel = '<div class="hl-panel">' in body
        # Real HL field types?
        hl_panel_quality = 0
        if has_hl_panel:
            if 'hl-input' in body: hl_panel_quality += 1
            if 'hl-dropdown' in body: hl_panel_quality += 1
            if 'hl-tag-picker' in body: hl_panel_quality += 1
            if 'hl-toggle' in body: hl_panel_quality += 1
            if 'hl-multiselect' in body: hl_panel_quality += 1
            if 'opt-chip' in body: hl_panel_quality += 1

        # Confidence: simple heuristic
        # Alta: has HL panel with ≥3 widgets + click panel ≥3 fields + at least 1 action node
        # Média: has HL panel but limited widgets, OR no HL panel but click panel ≥3 fields
        # Baixa: thin click panel + no HL panel
        avg_action = sum(action_fields) / len(action_fields) if action_fields else 0
        score = (3 if has_hl_panel and hl_panel_quality >= 3 else (1 if has_hl_panel else 0))
        score += (2 if click_panel_fields >= 3 else (1 if click_panel_fields >= 2 else 0))
        score += (2 if avg_action >= 4 else (1 if avg_action >= 3 else 0))

        if score >= 6:
            confidence = 'Alta'
        elif score >= 3:
            confidence = 'Média'
        else:
            confidence = 'Baixa'

        out.append({
            'anchor': anchor,
            'name': name,
            'en': en,
            'category': category,
            'href': f'{fname}#{anchor}',
            'click_panel_fields': click_panel_fields,
            'avg_action_fields': round(avg_action, 1),
            'has_hl_panel': has_hl_panel,
            'hl_panel_quality': hl_panel_quality,
            'confidence': confidence,
            'cat_id': catnum,
        })
    return out


def main():
    triggers = []
    for fp in sorted(glob.glob(os.path.join(ROOT, 'guia-highlevel-cat*.html'))):
        triggers.extend(parse_page(fp, 'trigger'))
    actions = []
    for fp in sorted(glob.glob(os.path.join(ROOT, 'acoes-highlevel-cat*.html'))):
        actions.extend(parse_page(fp, 'acao'))

    md = []
    md.append('# AUDIT — Conferência contra a UI real do HighLevel\n')
    md.append('Status auto-gerado por `scripts/build-audit.py` baseado em sinais '
              'mensuráveis do HTML/JS (presença e qualidade do painel HL, '
              'profundidade das entries configData, número de params no node).\n')
    md.append('**Como ler a confiança:**\n')
    md.append('- 🟢 **Alta** — painel HL com 3+ widgets reais + click-panel com 3+ campos + ações detalhadas\n')
    md.append('- 🟡 **Média** — falta um dos sinais (geralmente HL panel raso ou click-panel curto)\n')
    md.append('- 🔴 **Baixa** — sem painel HL ou click-panel com 1-2 campos\n')
    md.append('\n_Use a coluna `Verificar` pra marcar `[x]` conforme você confere contra o HL real (UI ou docs)._\n\n')

    # Summary
    def count_by(items, key):
        return {k: sum(1 for i in items if i['confidence'] == k) for k in ['Alta', 'Média', 'Baixa']}
    t_summary = count_by(triggers, 'confidence')
    a_summary = count_by(actions, 'confidence')
    md.append('## Resumo\n')
    md.append(f'| Tipo | 🟢 Alta | 🟡 Média | 🔴 Baixa | **Total** |\n')
    md.append(f'|------|--------:|--------:|--------:|----------:|\n')
    md.append(f'| Gatilhos | {t_summary["Alta"]} | {t_summary["Média"]} | {t_summary["Baixa"]} | **{len(triggers)}** |\n')
    md.append(f'| Ações | {a_summary["Alta"]} | {a_summary["Média"]} | {a_summary["Baixa"]} | **{len(actions)}** |\n\n')

    # Per-category sections
    def emit(title, items, prefix):
        md.append(f'\n## {title}\n')
        cur_cat = None
        for it in items:
            if it['cat_id'] != cur_cat:
                cur_cat = it['cat_id']
                md.append(f'\n### {cur_cat.upper()} · {it["category"] or "(sem categoria)"}\n')
                md.append('| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |\n')
                md.append('|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|\n')
            symbol = {'Alta': '🟢', 'Média': '🟡', 'Baixa': '🔴'}[it['confidence']]
            hlp = f"{it['hl_panel_quality']}/6" if it['has_hl_panel'] else '—'
            md.append(f"| {it['anchor']} | [{it['name']}]({it['href']}) | {it['en']} | "
                      f"{it['click_panel_fields']} | {hlp} | {symbol} | [ ] | |\n")

    emit('Gatilhos · 12 categorias', triggers, 'g')
    emit('Ações · 14 categorias', actions, 'a')

    with open(OUTPUT, 'w') as f:
        f.write(''.join(md))
    print(f'Wrote {OUTPUT} — {len(triggers)} gatilhos + {len(actions)} ações = {len(triggers)+len(actions)} entries')
    print(f'Triggers: Alta={t_summary["Alta"]} Média={t_summary["Média"]} Baixa={t_summary["Baixa"]}')
    print(f'Actions:  Alta={a_summary["Alta"]} Média={a_summary["Média"]} Baixa={a_summary["Baixa"]}')


if __name__ == '__main__':
    main()
