#!/usr/bin/env python3
"""Append a CHANGELOG entry summarizing the current uncommitted changes.

Called by .github/workflows/weekly-refine.yml after auto-refine.py runs.
If `deploy-highlevel/` has no uncommitted changes, exits silently — nothing
to log.
"""

import datetime
import os
import re
import subprocess
import sys

ROOT = os.path.join(os.path.dirname(__file__), '..')
CHANGELOG = os.path.join(ROOT, 'CHANGELOG.md')


def changed_files_in(path_prefix):
    """Return a sorted list of changed files under the given path."""
    out = subprocess.check_output(['git', 'status', '--porcelain', path_prefix], cwd=ROOT).decode()
    files = []
    for line in out.splitlines():
        # Format: ' M deploy-highlevel/foo.html' or '?? deploy-highlevel/bar.html'
        parts = line.strip().split(None, 1)
        if len(parts) == 2:
            files.append(parts[1].replace(path_prefix.rstrip('/') + '/', ''))
    return sorted(set(files))


def main():
    files = changed_files_in('deploy-highlevel/')
    if not files:
        print('No drift in deploy-highlevel/ — skipping CHANGELOG.')
        return

    date = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
    # Group files into a single comma list, wrapped tight
    files_str = ', '.join(f'`{f}`' for f in files)

    entry = (
        f'## {date} — Automation\n'
        f'**Weekly auto-refine**\n'
        f'([pending](../../actions))\n\n'
        f'- `scripts/auto-refine.py` detected drift and reapplied the mechanical '
        f'refinements (label standardization, filter headers, Slack → Webhook, '
        f'trigger-type, placeholder cleanup, configData regen).\n'
        f'- Files touched ({len(files)}): {files_str}\n\n'
    )

    with open(CHANGELOG) as f:
        content = f.read()

    # Insert the new entry right after the first '---\n\n' separator (end of intro)
    sep = '---\n\n'
    idx = content.find(sep)
    if idx == -1:
        print('CHANGELOG.md is missing the expected --- separator. Aborting.', file=sys.stderr)
        sys.exit(1)
    insert_at = idx + len(sep)
    new_content = content[:insert_at] + entry + content[insert_at:]

    with open(CHANGELOG, 'w') as f:
        f.write(new_content)

    print(f'Appended CHANGELOG entry for {date} ({len(files)} files).')


if __name__ == '__main__':
    main()
