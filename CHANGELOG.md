# Changelog

All notable changes to the HighLevel PT-BR Guide are logged here.

Format: each entry has a date, type (Deploy / Content / Automation / Hotfix),
and a short summary of what changed. The weekly auto-refine workflow appends
an entry whenever it detects drift and opens a PR.

For full diffs, follow the commit hash link or browse the PR.

---

## 2026-07-14 — Automation
**Reconcile two diverged branches from 2026-07-10 + fix count drift + weekly native-item check**

- Two sessions on 2026-07-10 branched from the same commit and each added
  different native items without merging into each other: one branch (merged
  as `main`) added **Inbound Email** (G20), **User Replied** (G21), **Custom
  Code** (cat03 A5), and an **AI Agent** action (cat05 A6); a second branch
  (merged into `claude/loving-faraday-UK9eK` via PR #3) added 4 **Communities**
  triggers (cat11 g6–g9), a whole new **Google Integrações** category pair
  (`guia-highlevel-cat13.html` + `acoes-highlevel-cat15.html`), and its own
  independent **AI Agent** action (also cat05 A6).
- Rebased the Google/Communities branch onto `main` to combine both. Where
  both sides had independently authored the same **AI Agent** action, kept
  main's version (it cites the official doc: [workflow-action-ai-agent](https://help.gohighlevel.com/support/solutions/articles/155000007600-workflow-action-ai-agent))
  and dropped the duplicate rather than shipping two conflicting a6 blocks.
- Found `acoes-highlevel-cat15.html` used an `action-*` class-naming
  convention (`action-block`, `action-name`, …) instead of the `acao-*`
  convention every other action page uses — `scripts/build-search-index.py`
  only recognizes `acao-*`, so those 6 actions were silently missing from
  search. Renamed the classes in that one file to match the convention
  (its own internal CSS/JS updated together, so nothing broke).
- Found a real bug in `scripts/auto-refine.py`'s `regenerate_config_data`:
  its node-body regex could swallow a node's own closing `</div>` when
  matching against the following sibling, truncating the *last* visible
  parameter out of the click-panel — for a node with only one parameter,
  this silently dropped the whole entry (empty click-panel). It only ever
  bit `guia-highlevel-cat13.html` and `acoes-highlevel-cat15.html` in
  practice, since every other page is already in the `HAND_CRAFTED`
  skip-list and never runs through this regenerator. Fixed the regex
  (verified safe across all 603 nodes in the site — every affected node's
  old output was an exact prefix of the fixed output, i.e. purely
  additive, never reordered/removed), restored the two files' lost
  parameters, and added both new files to `HAND_CRAFTED` now that they're
  hand-tuned to the same fidelity bar as the rest of the guide (matching
  how every other category was promoted into that list once finished).
- Re-ran the periodic check against `help.gohighlevel.com` /
  `ideas.gohighlevel.com/changelog` for native triggers/actions released
  since 2026-07-10. Everything surfaced by the search (Call Transcript
  Generated, Community Leaderboard, Subscription/Refund, Google Forms
  response trigger) was already documented in the guide from earlier
  rounds. Two items reported by third-party recap blogs — "Payment Failed"
  and "Form Partially Completed" as standalone triggers — do not exist per
  official HighLevel docs (Payment Failed is a status filter on the
  existing Payment/Subscription trigger; Form Partially Completed is still
  an open feature request on the ideas board) and were **not** added.
  Todoist/Jira/Basecamp/Apify/Fathom-style app integrations that also
  surfaced in the search were excluded as non-native, per this guide's
  existing rule (see the Slack exclusion in `scripts/auto-refine.py`).
- Flags for a future session (not fixed now, out of scope for a count/drift
  pass): open PR #4 on this repo adds Todoist and Jira as new category
  pages — both are third-party marketplace integrations, not native HL
  triggers/actions, so it shouldn't be merged as-is. Also, cat15's actions
  (Google Integrações) are missing the dedicated "Painel de configuração —
  fidelidade HighLevel" block that every other action has; they only have
  the inline mockup click-panel.
- Totals now: **86 gatilhos, 118 ações, 204 entries** (198 painéis HL, 197
  mockups interativos) across 13 gatilho categories + 15 ação categories.
  `search-index.json` regenerated (204 entries), `AUDIT-TABLE.md`
  regenerated, all 28 pages pass `validate-mockups.js`, `index.html`
  updated with the corrected counts and "Última atualização: 14 de julho
  de 2026".

## 2026-07-10 — Content
**Add 14 new native GHL triggers/actions: Communities, Google Integrations, AI Agent**

- **cat11 · Comunidades** — 4 new triggers added (g6–g9):
  Registrado em Evento do Grupo, Solicitação de Entrada Rejeitada,
  Nova Publicação no Grupo, Novo Comentário no Grupo.
  Counter: 5 → 9 gatilhos. New sidebar section "Engajamento".
- **NEW: guia-highlevel-cat13.html** — Google Integrações (Gatilhos):
  3 new LC Premium triggers (g1–g3): Contato Google Criado,
  Novo Grupo de Contatos Google, Resposta em Formulário Google.
  Each with interactive mockup + static HL config panel.
- **NEW: acoes-highlevel-cat15.html** — Google Integrações (Ações):
  6 new LC Premium actions (a1–a6): Criar, Atualizar, Buscar,
  Buscar ou Criar Contato Google, Criar Grupo Google,
  Adicionar a Grupos Google. Interactive mockups for a4 and a6.
- **cat12 · Certificados (Gatilhos)** — breadcrumb/nav updated: 12/12 → 12/13.
  Next nav now points to new cat13.
- **cat14 · Certificados (Ações)** — breadcrumb/nav updated: 14/14 → 14/15.
  Next nav now points to new cat15.
- This branch (merged via PR #3 into `claude/loving-faraday-UK9eK`) also
  added its own AI Agent action (cat05 a6), authored independently of the
  same-day `main` branch below. The two were reconciled on 2026-07-14 (see
  entry above) — main's version of that action is the one that shipped.

## 2026-07-10 — Content
**Document all 8 Wait action parameters + fix orphaned duplicate markup (requested)**

- `acoes-highlevel-cat04.html` A2 (Wait): the HL config panel only documented
  3 of the 8 real `Wait Type` modes (Time Delay, Wait Until Event, Wait
  Until Date). Rewrote it to cover all 8: Wait For (Time Delay), Wait
  Until (Date/Time), Recurring Schedule, Wait for Appointment/Booking/
  Invoice, Wait for Contact Reply (incl. User Replied + Live Chat
  channels), Wait for Event, Wait for Opportunity, Wait for Review
  Request — plus the general Resume On / Overall Timeout / Advance
  Window settings that apply regardless of mode.
  [Official doc](https://help.gohighlevel.com/support/solutions/articles/155000002470-workflow-action-wait)
- Found and removed ~90 lines of orphaned duplicate mockup markup that
  had been left inside this same block from an earlier edit — unmatched
  closing `</div>` tags meant the DOM balanced to -4 at one point (browsers
  silently tolerate this, so `validate-mockups.js` never caught it, but it
  was dead/duplicate content sitting in the page).

## 2026-07-10 — Content
**Add User Replied trigger (requested)**

- Added **User Replied** trigger (`guia-highlevel-cat02.html` G21) — native
  trigger that fires when a team member/user (not the customer) replies
  to a contact, the opposite of Customer Replied. Filters: Reply Channel,
  Specific User, Assigned User. Confirmed via HighLevel's official
  changelog: [Workflow Trigger: User Replied](https://ideas.gohighlevel.com/changelog/workflow-trigger-user-replied).
  This was flagged as a pending candidate in the previous entry below and
  applied now on user request.
- Totals now: **79 gatilhos, 112 ações, 191 entries** — `search-index.json`
  and `AUDIT-TABLE.md` regenerated, all 26 pages pass validate-mockups.js.

## 2026-07-10 — Content
**Add 3 new native HighLevel workflow items + fix stale counts across the guide**

- **Inbound Email** trigger added (`guia-highlevel-cat02.html` G20) — native
  trigger for cold/warm inbound emails to a connected mailbox, distinct from
  Customer Replied and Email Events. [Official doc](https://help.gohighlevel.com/support/solutions/articles/155000007650-workflow-trigger-inbound-email)
- **Custom Code** action added (`acoes-highlevel-cat03.html` A5) — native
  JavaScript action (Input Data, Test your Code, AI-Powered Code
  Generation), distinct from Custom API Call. [Official doc](https://help.gohighlevel.com/support/solutions/articles/155000002253-workflow-action-custom-code)
- **AI Agent** action added (`acoes-highlevel-cat05.html` A6) — new
  autonomous multi-step Workflow AI action (Premium). [Official doc](https://help.gohighlevel.com/support/solutions/articles/155000007600-workflow-action-ai-agent)
- Fixed count drift found while auditing: `search-index.json` hadn't been
  regenerated since the previous round's Scheduler + Add Followers
  additions (was reporting 185 instead of 187); `index.html` tab-counts
  and section-labels still said 76/109 while hero-stats said 77/110;
  `acoes-highlevel-cat03.html`'s side-nav/hero-stats were missing A4 (Send
  Conversion Event) entirely.
- All totals now match the real HTML content: **78 gatilhos, 112 ações,
  190 entries** — `search-index.json` and `AUDIT-TABLE.md` regenerated,
  homepage last-updated date added to the footer.
- See `AUDIT.md` for 6 additional candidate native items (AI Decision
  Maker, User Replied, Client Portal File Uploaded, 3 new Communities
  triggers, AI Translate, Update Conversation AI Bot and Status) found
  but not yet applied — pending human confirmation of exact fields.


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
