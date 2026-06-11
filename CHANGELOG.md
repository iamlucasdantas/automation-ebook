# Changelog

All notable changes to the HighLevel PT-BR Guide are logged here.

Format: each entry has a date, type (Deploy / Content / Automation / Hotfix),
and a short summary of what changed. The weekly auto-refine workflow appends
an entry whenever it detects drift and opens a PR.

For full diffs, follow the commit hash link or browse the PR.

---

## 2026-06-11 — Content
**Add 9 new native triggers and 15 new actions — Cal.com, Custom Objects, Google Contacts, Workflow AI**

- **Gatilhos · Cat03 (Compromissos):** +4 Cal.com triggers — Booking Created, Booking Rescheduled, Booking Cancelled, Meeting Ended. Category grows from 2 → 6 triggers.
- **Ações · Cat05 (Workflow AI):** +2 actions — AI Agent (autonomous multi-step execution) and AI Decision Maker (AI-powered branch routing). Category grows from 5 → 7 actions.
- **Ações · Cat06 (Agendamentos):** +4 Cal.com actions — Create Booking, Cancel Booking, Reschedule Booking, Find Booking. Category grows from 3 → 7 actions.
- **Nova Cat13 (Gatilhos · Objetos Personalizados):** 3 new triggers — Object Created, Object Updated, Object Deleted. Full interactive mockups.
- **Nova Cat14 (Gatilhos · Google Contatos):** 2 new triggers — New Google Contact, New Google Group. Full interactive mockups.
- **Nova Cat15 (Ações · Objetos Personalizados):** 3 new actions — Create Object Record, Update Object Record, Find Object Record.
- **Nova Cat16 (Ações · Google Contatos):** 6 new actions — Create Contact, Update Contact, Find Contact, Find or Create Contact, Create Group, Add Contact to Group.
- **index.html:** Updated hero stats (76→85 gatilhos, 108→123 ações, 184→208 painéis, 31→43 mockups), tab counts (12→14 cats / 14→16 cats), added new category cards for cat13–cat16, updated last-update date to 11/06/2026.
- Total: 85 gatilhos · 123 ações · 30 categorias

## 2026-06-08 — Content
**Replace generic 'Configurar conforme necessidade' fallback with realistic params**
([8fd206c](../../commit/8fd206c))

- 89 nodes carrying the generic fallback got specific HighLevel field sets:
  Voicemail (Slydial drop), FB/IG Messenger (PSID + Public Reply),
  Webhook da Hotmart, "Tag Added · X" with extracted tag, "48h antes da
  consulta" → Custom Date Field + Timing, Opportunity Won/Status Changed,
  GMB Message Received, Campaign Blast, and ~20 others.
- 47 nodes got specific params; 42 had the lone bad param removed.
- 21 files updated, configData click panels regenerated.

## 2026-06-05 — Automation
**Add weekly auto-refine routine for mockups**
([f6e2da7](../../commit/f6e2da7))

- `scripts/auto-refine.py`: idempotent script that consolidates the
  mechanical refinements (label standardization, filter header
  normalization, Slack → Webhook, trigger-type specification, placeholder
  cleanup, configData regen). Run with `--check` for CI.
- `.github/workflows/weekly-refine.yml`: cron every Monday 09:00 BRT,
  opens a PR if drift is detected.
- `scripts/README.md`: documents the routine.
- Cleaned a non-idempotent "Template padrão da subconta da subconta…"
  suffix that was growing across 14 files.

## 2026-06-05 — Content
**Specify trigger node types (Trigger · X) across all category mockups**
([ac46b36](../../commit/ac46b36))

- 148 trigger nodes now show their specific trigger name in the type label
  (e.g., `Trigger · Inbound Webhook`, `Trigger · Form Submitted`) instead
  of the generic `Trigger`.
- 492 configData click-panel entries regenerated so the popup header
  reflects the specific trigger.

## 2026-06-05 — Content
**Replace generic placeholder values with realistic merge-field content**
([f477f70](../../commit/f477f70))

- 610 placeholders swapped for realistic content using `{{contact.first_name}}`
  and friends. Examples:
  - "Conteúdo da notificação" → "Lead {{contact.first_name}} pronto pra atendimento"
  - "Detalhes da tarefa" → "Confirmar próximos passos com {{contact.first_name}}"
  - "sender@empresa.com.br" → "lucas@magneticflows.com.br"

## 2026-06-05 — Content
**Standardize node icons to match action type across all category pages**
([89ad953](../../commit/89ad953))

- 69 mockup-node icons re-mapped: Send Email → @, Wait → ⏱, Set Event
  Date → 📅, Webhook → ↗, AI → 🤖, Task → ✓, Slack-as-Webhook → ↗,
  Remove from Workflows → ⊘, etc. Each icon class now matches the action
  being illustrated.

## 2026-06-05 — Content
**Enrich empty mockup nodes + regenerate form-style click panels everywhere**
([350f19b](../../commit/350f19b))

- 384 workflow nodes that had empty or sparse bodies received realistic
  HighLevel field sets per action type (Send Email gets From/Subject/
  Template; Internal Notification gets User/Type/Message; Wait gets
  Wait Type/Duration; etc.).
- 492 configData entries regenerated so the click panel mirrors the
  enriched visible nodes.

## 2026-06-04 — Content
**Generate form-style click panels from visible node params for all categories**
([46d15cc](../../commit/46d15cc))

- Auto-extracted every workflow node's visible parameters and rebuilt
  every file's configData JS object so the click-to-expand panel mirrors
  the real HighLevel action form (labels + filled values, dropdowns ▾,
  opt-chips for multi-select, 🟢/⚪ toggles).
- 134 entries generated across 19 files; 6 files preserved.

## 2026-06-04 — Content
**Apply HighLevel UI fidelity improvements to all 25 remaining category pages**
([44eaee3](../../commit/44eaee3))

- CSS: trigger purple stripe + gradient header, gear/menu hover
  controls, "+"-on-connector button.
- ~480 `<div class="ghl-node-controls">` injections so every node shows
  Settings (⚙) and More (⋮) on hover.
- ~50 filter headers standardized to "Filters".
- ~440 Portuguese category labels translated to real HL action names.
- ~37 `<div class="config-desc">` documentation paragraphs removed.
- 9 `Slack Message` instances converted to `Outbound Webhook (Slack)`.

## 2026-06-04 — Content
**Replace descriptive text with real form values across all 43 click panels (cat01)**
([8c579dd](../../commit/8c579dd))

- Rewrote every node's click-to-expand panel in cat01 (the gold
  standard) so each section shows the actual filled value
  ("lucas@empresa.com.br" with ▾ dropdown indicator, tag chips for
  multi-select, 🟢 ON / ⚪ OFF for toggles) instead of help text.
- Removed duplicate g12-1..g12-4 entries.

## 2026-06-03 — Content
**Show real values (not help text) in click-to-expand panel for G1 nodes**
([a846d0e](../../commit/a846d0e))

- Initial pilot of the click-panel refactor on G1's four nodes (trigger
  + Send Email + Assign to User + Internal Notification). Set the
  pattern used across all later refactors.

## 2026-06-03 — Content
**Audit and align mockup actions to real HighLevel UI**
([a03a053](../../commit/a03a053))

- Cross-checked every action node in cat01's 12 mockups against the
  real HighLevel action panels: Slack Message → Outbound Webhook,
  added missing required fields (Subject, From Email, Message), fixed
  Update Opportunity / Wait / Set Event Date / If/Else / Outbound
  Webhook / Remove from Workflows / Add Contact Tag structures, plus
  standardized action type labels from PT category names to the real
  HL action names.

## 2026-06-03 — Content
**Improve workflow mockup visual fidelity to HighLevel Advanced Builder**
([023afe8](../../commit/023afe8))

- Added the "+" connector button, hover controls on each node (gear +
  three-dot menu), purple left stripe on triggers with a subtle
  gradient header. Applied to all 43 nodes in cat01.

## 2026-06-03 — Content
**Standardize trigger panel headers and add missing G11 fields**
([2a950ff](../../commit/2a950ff))

- Normalized all 12 trigger-panel section headers ("Filters · AND
  logic" → "Filters") to match the real HL UI.
- Added the missing `When` (Before/After) dropdown and `Number of Days`
  input to the Task Reminder (G11) panel.

## 2026-06-03 — Hotfix
**Clean orphan mockup content + refine G1 trigger panel**
([c0b7bee](../../commit/c0b7bee))

- Removed two blocks of stale duplicate mockup HTML that earlier edits
  had left behind inside G1 and inside the footer (the G12 leftover
  was breaking the footer layout).
- Added the `Created via Source` filter row to the Contact Created
  (G1) panel.

## 2026-06-02 — Automation
**Auto-enable Pages in workflow**
([9bf41b8](../../commit/9bf41b8))

- `actions/configure-pages@v5` now uses `enablement: true` so the
  workflow can create the Pages site on demand. First run had failed
  because Pages wasn't enabled at trigger time.

## 2026-06-01 — Deploy
**Add GitHub Pages workflow and CNAME for guia.magneticflows.com**
([485b968](../../commit/485b968))

- `.github/workflows/pages.yml`: publishes `deploy-highlevel/` to
  GitHub Pages on push to `main`.
- `deploy-highlevel/CNAME` → `guia.magneticflows.com`.

## 2026-05-27 — Initial
**Add deploy-highlevel v3: HighLevel PT-BR guide static site**
([263fe1b](../../commit/263fe1b))

- Index + 12 trigger category pages (74 gatilhos) + 14 action category
  pages (107 ações) + 181 HighLevel panels + 28 interactive mockups.
