# HighLevel PT-BR Guide

Static site in `deploy-highlevel/`, published to GitHub Pages on every push to `main`.

## Scheduled update runs ("Daily Review for Updates")

Work only reaches the live site through `main`. Between 2026-09-14 and 2026-11-13 every
daily run pushed to its own branch and none was merged, so the site went stale. To avoid that:

1. Start from the latest `origin/main`. If the session branch is behind it, fast-forward
   to `origin/main` before changing anything.
2. If an earlier run's pull request is still open, build on that PR's branch instead and
   push to it (or note in the new PR that it supersedes the old one). Never start from an
   older snapshot.
3. When the run changes any file, open a pull request against `main`. The repository owner
   asks for this PR on every run that has changes; they review and merge it.
4. If nothing changed, do not commit a date-only bump and do not open a PR.

## Checks before committing

```bash
python3 scripts/auto-refine.py --check     # rebuilds search-index.json; must end clean
python3 scripts/build-audit.py             # regenerates AUDIT-TABLE.md
node scripts/validate-mockups.js           # all 30 pages must pass
```

Counts on `index.html` (hero stats, meta tags, tab labels, category cards) must match the
totals printed by `auto-refine.py`. Log each round in `CHANGELOG.md` and `AUDIT.md`.

## Scope

Only native HighLevel triggers and actions, confirmed by an official source
(`help.gohighlevel.com` or `ideas.gohighlevel.com/changelog`) with the exact name. Do not
invent fields; third-party marketplace integrations are out of scope.
