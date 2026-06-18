#!/usr/bin/env python3
"""Build a JSON search index for every trigger and action across the guide.

Walks deploy-highlevel/guia-highlevel-cat*.html (triggers) and
acoes-highlevel-cat*.html (actions), pulls structured metadata from each
.trigger-block / .acao-block, and writes deploy-highlevel/search-index.json
ready for the client-side search.

Idempotent — re-running with no content change leaves the file untouched.
"""

import glob
import json
import os
import re
from html import unescape

ROOT = os.path.join(os.path.dirname(__file__), '..', 'deploy-highlevel')
OUTPUT = os.path.join(ROOT, 'search-index.json')

CATEGORY_LABEL = {'guia': 'Gatilho', 'acoes': 'Ação'}


def strip_tags(s):
    return re.sub(r'<[^>]+>', '', s).strip()


def first_paragraph(s):
    m = re.search(r'<p[^>]*>(.*?)</p>', s, re.DOTALL)
    return strip_tags(unescape(m.group(1))) if m else ''


def parse_blocks(path, kind):
    """kind is 'trigger' or 'acao' — picks the right class names."""
    block_class = f'{kind}-block'
    name_class = f'{kind}-name'
    en_class = f'{kind}-en'
    cat_class = f'{kind}-cat'
    tags_class = f'{kind}-tags'

    with open(path) as f:
        html = f.read()

    fname = os.path.basename(path)
    pattern = re.compile(
        rf'<div class="{block_class}" id="([^"]+)" data-name="([^"]*)">(.*?)'
        rf'(?=<div class="{block_class}"|<!-- ═|<!-- GATILHO|<!-- AÇÃO|<nav class="cat-nav"|<div class="guide-footer)',
        re.DOTALL,
    )
    out = []
    for m in pattern.finditer(html):
        anchor, data_name, body = m.group(1), m.group(2), m.group(3)
        if not anchor[0] in ('g', 'a'):
            continue
        name_m = re.search(rf'<h2 class="{name_class}">([^<]+)</h2>', body)
        en_m = re.search(rf'<div class="{en_class}">([^<]+)</div>', body)
        cat_m = re.search(rf'<div class="{cat_class}">([^<]+)</div>', body)
        tags_m = re.search(rf'<div class="{tags_class}">(.*?)</div>', body, re.DOTALL)
        # Description = first paragraph of "O que esse gatilho/ação faz" block
        desc_m = re.search(
            r'<div class="tblock-label">[^<]*(?:O que esse|O que essa)[^<]*</div>\s*<div class="tblock-content">(.*?)</div>',
            body, re.DOTALL,
        )

        tags = []
        if tags_m:
            for t in re.finditer(r'<span class="info-tag[^"]*">([^<]+)</span>', tags_m.group(1)):
                tags.append(strip_tags(t.group(1)))

        out.append({
            'id': anchor,
            'type': CATEGORY_LABEL['guia' if kind == 'trigger' else 'acoes'],
            'name': strip_tags(name_m.group(1)) if name_m else anchor,
            'en': strip_tags(en_m.group(1)) if en_m else '',
            'category': strip_tags(cat_m.group(1)) if cat_m else '',
            'tags': tags,
            'description': first_paragraph(desc_m.group(1)) if desc_m else '',
            'keywords': data_name,
            'href': f'{fname}#{anchor}',
        })
    return out


def main():
    entries = []
    for path in sorted(glob.glob(os.path.join(ROOT, 'guia-highlevel-cat*.html'))):
        entries.extend(parse_blocks(path, 'trigger'))
    for path in sorted(glob.glob(os.path.join(ROOT, 'acoes-highlevel-cat*.html'))):
        entries.extend(parse_blocks(path, 'acao'))

    payload = {
        'generated_at': None,  # left null so the file is bit-stable
        'total': len(entries),
        'items': entries,
    }
    new_content = json.dumps(payload, ensure_ascii=False, indent=2) + '\n'

    if os.path.exists(OUTPUT):
        with open(OUTPUT) as f:
            if f.read() == new_content:
                print(f'Search index up to date ({len(entries)} entries)')
                return

    with open(OUTPUT, 'w') as f:
        f.write(new_content)
    triggers = sum(1 for e in entries if e['type'] == 'Gatilho')
    actions = sum(1 for e in entries if e['type'] == 'Ação')
    print(f'Wrote {OUTPUT} — {triggers} gatilhos + {actions} ações = {len(entries)} entries')


if __name__ == '__main__':
    main()
