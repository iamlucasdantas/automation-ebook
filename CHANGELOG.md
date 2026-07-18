# Changelog

All notable changes to the HighLevel PT-BR Guide are logged here.

Format: each entry has a date, type (Deploy / Content / Automation / Hotfix),
and a short summary of what changed. The weekly auto-refine workflow appends
an entry whenever it detects drift and opens a PR.

For full diffs, follow the commit hash link or browse the PR.

---

## 2026-07-18 — Content
**Add 2 new native GHL triggers (Inbound Email, Client Portal Upload) + fix widespread count/SEO drift**

- **cat02 · Comunicação — G20 Email Recebido (Inbound)**: new trigger, confirmed
  against official doc (cold/warm/customer-reply email types, mailbox/sender/
  subject/attachment filters, "new conversation only" advanced setting).
  Counter: 19 → 20 gatilhos.
  Ref: help.gohighlevel.com/.../workflow-trigger-inbound-email
- **cat07 · Contratos e Assinaturas — G11 Upload no Client Portal**: new trigger,
  confirmed against official changelog (fires on file upload via Client Portal
  Shared Documents). Counter: 10 → 11 gatilhos.
  Ref: ideas.gohighlevel.com/changelog/workflow-trigger-for-file-uploads-via-client-portal
- **Bug fix — search index silently dropped 6 actions**: `acoes-highlevel-cat15.html`
  (Google Integrações) was hand-built with English class names (`action-block`
  etc.) instead of the `acao-block` convention every other action page uses,
  so `build-search-index.py`'s regex never matched it. Fixed the indexer to
  accept both class prefixes. Site search now actually finds all 6 Google
  actions it was silently missing.
- **Bug fix — auto-refine.py wasn't protecting the 2 newest hand-crafted pages**:
  `guia-highlevel-cat13.html` and `acoes-highlevel-cat15.html` were missing
  from `HAND_CRAFTED`, so a mechanical refine pass would gut their rich,
  hand-written `configData` panels down to one-field skeletons. Added both
  to the protected set (caught and reverted before commit — see git history
  for the near-miss).
- **Category-count drift across ~27 files**: breadcrumbs/footers on
  guia-cat01–11 still said "X/12" and "de 12" (stale since cat13 was added
  on 2026-07-10 — should've been "/13"); acoes-cat01–04/06–13 still said
  "X/14" and "de 14" (stale since cat15 was added — should've been "/15").
  All fixed to the real current totals (13 trigger categories, 15 action
  categories).
- **Stale per-page trigger/action/mockup counts**: several category pages'
  own hero-stat blocks and prose sentences had drifted from their real
  content (e.g. acoes-cat07 said "9 ações" in three places when Add Follower
  to Opportunity had already bumped it to 10; acoes-cat03/cat05 similarly
  off by one; guia-cat06 hero text said "10 gatilhos" for a 12-trigger page;
  guia-cat08 said "1 Mockup interativo" on a page that has always had 3).
  Recomputed every page's real trigger/action-block count and real
  interactive-mockup (`ghl-mockup`) count and corrected all mismatches.
- **SEO — acoes-cat01 through cat14 had identical, wrong meta tags**: every
  one of those 14 pages shared the exact same `<title>`, meta description,
  and keywords — copy-pasted from a *gatilhos* (triggers) template, saying
  "Contatos" and "Parte 01/12" regardless of which actions category the page
  actually covered. Gave each page a real, distinct title/description/
  keywords matching its own category.
- **index.html**: stats updated — 84→86 gatilhos, 117 ações (unchanged),
  201→203 painéis. "Mockups interativos" corrected 37→196 (the real count of
  pages with a full interactive canvas, not a stale figure left over from
  before the 2026-07-10 batch). "Última atualização" → 18 de julho de 2026.
  cat02/cat07 category cards updated to the new per-category counts.
- **AUDIT.md**: logged 5 pending discoveries from this round's research that
  need a dedicated session before being added — an entire new "Company-Based
  Workflows" trigger/action family, a Service Booking (Services v2) trigger,
  Conversation AI Trigger, Custom Trigger, and a possible Documents & Contracts
  action. Explicitly out of scope: third-party marketplace-app triggers/actions
  (HubSpot, Jira, Basecamp, Vapi) — this guide only documents native HighLevel,
  same rule that already excludes Slack.

Worklist grows to 86 triggers + 117 actions = 203 entries.

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
