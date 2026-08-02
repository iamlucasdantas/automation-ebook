# Changelog

All notable changes to the HighLevel PT-BR Guide are logged here.

Format: each entry has a date, type (Deploy / Content / Automation / Hotfix),
and a short summary of what changed. The weekly auto-refine workflow appends
an entry whenever it detects drift and opens a PR.

For full diffs, follow the commit hash link or browse the PR.

---

## 2026-08-02 — Content
**Scheduled audit: 5 new native GHL triggers/actions + stale count drift fix**

- **Conversation SLA** trigger added (`guia-highlevel-cat02.html` G22) —
  fires on the Conversations SLA timer events (Due Soon/Overdue/SLA
  Dismissed), with channel/tags/owner/custom-field filters and an
  "Avoid Repeated Triggers" toggle. [Official changelog](https://ideas.gohighlevel.com/changelog/conversations-sla-workflow-trigger-permissions)
- **Estimates** trigger added (`guia-highlevel-cat07.html` G11) — fires on
  Estimate Sent/Accepted/Declined, distinct from the generic "Documents &
  Contracts" e-signature trigger. [Official doc](https://help.gohighlevel.com/support/solutions/articles/155000003704-workflow-trigger-estimates)
- **Send Estimate** action added (`acoes-highlevel-cat08.html` A6) —
  companion to the Estimates trigger. [Official doc](https://help.gohighlevel.com/support/solutions/articles/155000003705-workflow-action-send-estimate)
- **Client Portal File Uploaded** trigger added (`guia-highlevel-cat07.html`
  G12) — candidate flagged in the 2026-07-10 round, now confirmed and
  applied. No documented dedicated filters. [Official changelog](https://ideas.gohighlevel.com/changelog/workflow-trigger-for-file-uploads-via-client-portal)
- **Grant Community Group Leaderboard Points** action added
  (`acoes-highlevel-cat13.html` A7) — companion to the existing "Assign
  Leaderboard Level"; grants points to an existing group member, level
  auto-updates. [Official changelog](https://ideas.gohighlevel.com/changelog/community-leaderboard-workflow-trigger-action)
- Researched but **not applied**: "Form Partially Completed" trigger —
  only found in third-party blogs, no primary source confirmed yet.
- Fixed count drift found while auditing: `index.html` tab-counts and
  section-labels still said 84/117 while hero-stats already said 86/120;
  `guia-highlevel-cat02.html` hero "Mockups interativos" stat said 8
  instead of the real 21 (pre-existing, unrelated to this round's
  addition). CHANGELOG hadn't been updated since 2026-07-10 despite two
  real content commits landing on 2026-07-20/21 (Update Conversation AI
  Bot and Status as cat05 A7, Remove Followers from Opportunity as cat07
  A11) — both already correctly reflected in the guide's counts, just
  never logged here.
- Totals now: **89 gatilhos, 122 ações, 211 entries** —
  `search-index.json` and `AUDIT-TABLE.md` regenerated via
  `scripts/build-search-index.py` / `scripts/build-audit.py`, all pages
  pass `validate-mockups.js`. `index.html` footer date updated.

## 2026-07-21 — Content
**Add Remove Followers from Opportunity as cat07 A11**

Companion to A10 (Add Followers): removes specific users — or all at once
via the Remove All Followers toggle — from the opportunity's follower
list. Requires an opportunity in context; skipped otherwise. Totals:
120 ações / 206 painéis.
[Official doc](https://help.gohighlevel.com/support/solutions/articles/155000004757-workflow-action-remove-followers-from-opportunity)

## 2026-07-20 — Content
**Add Update Conversation AI Bot and Status as cat05 A7 + reconcile parallel sessions**

The per-contact Conversation AI bot control action was missing from the
ebook. Added to cat05 (AI actions) as A7 "Atualizar Bot de IA e Status"
(Conversation AI Bot dropdown, Bot Status Active/Inactive, conditional
Sleep Timer). Landed alongside a parallel session's work (AI Agent as
cat05 A6, Google Integrações cat13/cat15 pages) — merged and reconciled,
with `acoes-highlevel-cat15.html` class names normalized (`action-*` →
`acao-*`) so the Google actions show up in search/audit.

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


## 2026-07-10 — Content
**Add 14 new native GHL triggers/actions: Communities, Google Integrations, AI Agent**

- **cat11 · Comunidades** — 4 new triggers added (g6–g9):
  Registrado em Evento do Grupo, Solicitação de Entrada Rejeitada,
  Nova Publicação no Grupo, Novo Comentário no Grupo.
  Counter: 5 → 9 gatilhos. New sidebar section "Engajamento".
- **cat05 · Workflow AI** — 1 new action added (a6):
  Agente de IA (AI Agent) with full interactive mockup.
  Counter: 5 → 6 ações.
- **cat12 · Certificados (Gatilhos)** — breadcrumb/nav updated: 12/12 → 12/13.
  Next nav now points to new cat13.
- **cat14 · Certificados (Ações)** — breadcrumb/nav updated: 14/14 → 14/15.
  Next nav now points to new cat15.
- **NEW: guia-highlevel-cat13.html** — Google Integrações (Gatilhos):
  3 new LC Premium triggers (g1–g3): Contato Google Criado,
  Novo Grupo de Contatos Google, Resposta em Formulário Google.
  Each with interactive mockup + static HL config panel.
- **NEW: acoes-highlevel-cat15.html** — Google Integrações (Ações):
  6 new LC Premium actions (a1–a6): Criar, Atualizar, Buscar,
  Buscar ou Criar Contato Google, Criar Grupo Google,
  Adicionar a Grupos Google. Interactive mockups for a4 and a6.
- **index.html** — stats updated: 76→83 gatilhos, 109→116 ações,
  185→199 painéis, 31→37 mockups. Tabs updated to 13 cat / 15 cat.
  New cards for cat13 and cat15. "Última atualização: 10 de julho de 2026."
- **search-index.json** — 14 new entries added. Total: 185 → 199.

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
