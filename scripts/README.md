# scripts/

## auto-refine.py

Mechanical refinements to keep the HighLevel guide mockups visually and
structurally aligned with the real HighLevel Workflow Builder UI.

Run locally:

```bash
python3 scripts/auto-refine.py          # apply
python3 scripts/auto-refine.py --check  # exit 1 if drift detected
```

Idempotent — running multiple times produces the same result.

Transformations applied (in order):

1. Standardize Portuguese category labels to real HL action names
   (`Action · Comunicação` → `Action · Communication`, etc.)
2. Standardize filter section headers (`Filters · X` → `Filters`)
3. Replace `Slack Message` nodes with `Outbound Webhook (Slack)`
   (Slack is not a native HL action)
4. Specify the trigger node-type per its title
   (`Trigger` → `Trigger · Inbound Webhook`)
5. Replace generic placeholder values with realistic merge-field
   content (e.g., `Conteúdo da notificação` → `Lead {{contact.first_name}} pronto pra atendimento`)
6. Regenerate the configData JS object so the click-to-expand detail
   panel mirrors each node's visible parameters

Files in `HAND_CRAFTED` are skipped — they are maintained at higher
fidelity by hand.

## append-changelog.py

After `auto-refine.py` runs in the weekly workflow, this script appends
a new entry at the top of `CHANGELOG.md` listing the files that drifted
and what the refine pass did. Skipped if no drift was detected.

```bash
python3 scripts/append-changelog.py
```

## Weekly automation

`.github/workflows/weekly-refine.yml` runs every Monday at 09:00 BRT:

1. `auto-refine.py` applies the mechanical refinements.
2. `append-changelog.py` records the changes in `CHANGELOG.md`.
3. If any drift was detected, a PR is opened against `main` carrying
   both the file diffs and the new CHANGELOG entry.

Open the [Changelog](../CHANGELOG.md) anytime to see what's changed
session-by-session.

For deeper improvements that need judgment (e.g., per-action HL field
research, copy editing), open a Claude Code session from the GitHub
PR or web app and ask Claude to refine specific categories.
