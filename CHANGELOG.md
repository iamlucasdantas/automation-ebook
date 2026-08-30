# Changelog

All notable changes to the HighLevel PT-BR Guide are logged here.

Format: each entry has a date, type (Deploy / Content / Automation / Hotfix),
and a short summary of what changed. The weekly auto-refine workflow appends
an entry whenever it detects drift and opens a PR.

For full diffs, follow the commit hash link or browse the PR.

---

## 2026-08-30 — Automation
**Checagem de novidades nativas — nenhuma nova encontrada**

Rodada de auditoria comparou o guia (87 gatilhos + 175 ações = 262
painéis) contra `help.gohighlevel.com` e o changelog oficial desde a
rodada de 2026-08-24. Detalhe completo em [AUDIT.md](./AUDIT.md#-rodada-2026-08-30--checagem-de-novidades-nativas).

- Nenhum gatilho/ação nativo novo lançado nos últimos ~6 dias cruzou a
  barra de confirmação. Dois itens do changelog da semana (disparo em
  massa pra Companies/Custom Objects via list view, dropdown de Sender
  Domain em Workflow Settings) são features de produto reais mas não são
  nós de Trigger/Action do Workflow Builder — fora do escopo do guia.
- `help.gohighlevel.com` e `ideas.gohighlevel.com` estavam bloqueados por
  egress direto neste ambiente (diferente de rodadas anteriores) — a
  checagem rodou só com resumos do WebSearch, o que manteve os
  candidatos pendentes (Badge Issued/Issue Badge, Monday.com, Jira,
  Linear, Housecall Pro, Apify, Browse AI, OpenRouter, Manus) como
  candidatos — nenhum tinha nomes de campo confirmados via fonte
  primária direta.
- Totais e "Última atualização" do `index.html` **não mudaram** — nada
  de conteúdo foi tocado nesta rodada.
- `auto-refine.py --check`, `build-search-index.py` e `build-audit.py`
  confirmam 0 drift (262 entries, já sincronizado).

## 2026-08-24 — Deploy
**SEO audit + fix: duplicate titles/descriptions, missing canonicals, stale sitemap**

Requested SEO pass on the live site (`guia.magneticflows.com`). Found and fixed:

- **Duplicate title + meta description on 16 of 17 Ações pages.** Every
  category page from `acoes-highlevel-cat01.html` through `cat14.html`
  (plus `cat16`/`cat17`) shared the exact same `<title>` ("Ações do
  HighLevel — Guia Magnetic Funnels") and the exact same description —
  which described **Contact triggers**, not the actions on that page. Google
  treats near-duplicate title/description across 16 URLs as duplicate
  content and tends to index only one of them. Wrote a unique, accurate
  title + description + keywords + OG/Twitter tags for each of the 16
  pages, based on that page's real category and action count.
  `acoes-highlevel-cat15.html` already had unique content; only its stale
  "Parte 15/15" was corrected to "Parte 15/17" (17 Ações categories exist
  now).
- **No `<link rel="canonical">` anywhere.** Added one to all 31 pages
  (30 category pages + `index.html`), pointing at
  `https://guia.magneticflows.com/<page>`. This also backstops the
  duplicate-content issue above going forward.
- **Sitemap missing 4 pages.** `sitemap.xml` had 27 `<loc>` entries; the
  4 pages added in the 2026-08-10 round (`guia-highlevel-cat13.html`,
  `acoes-highlevel-cat15/16/17.html`) were never added. Fixed — now 31/31.
- **Stale "Parte NN/12" denominator on all 12 original Gatilhos pages.**
  `guia-highlevel-cat13.html` (added 2026-07-29) correctly says "13/13",
  but cat01–cat12 still said "/12" in their description/OG/Twitter tags.
  Corrected to "/13" across all 12.

Not done yet (needs a decision, not code): `og:image` — no page has one,
so link previews on social/WhatsApp show no image. Needs a real image
asset before it can be added. Also skipped: JSON-LD structured data —
lower priority, no blocker, can follow in a later round.

No trigger/action content changed — this is metadata/deploy-surface only.
`build-search-index.py` confirms 262 entries unchanged; `auto-refine.py
--check` reports 0 drift.
## 2026-08-24 — Content
**Add tutorial video to Appointment Status trigger (requested)**

- Vídeo tutorial incorporado logo abaixo da descrição do gatilho
  **Status de Compromisso (Appointment Status)** ·
  `guia-highlevel-cat03.html` G1, a pedido do usuário.

## 2026-08-24 — Content
**Add tutorial videos to 2 Pipeline/Opportunity triggers (requested)**

- Vídeo tutorial incorporado logo abaixo da descrição do gatilho
  **Mudança de Estágio no Pipeline (Pipeline Stage Changed)** ·
  `guia-highlevel-cat04.html` G4, a pedido do usuário.
- Vídeo tutorial incorporado logo abaixo da descrição do gatilho
  **Mudança de Status em Oportunidade (Opportunity Status Changed)** ·
  `guia-highlevel-cat04.html` G3, a pedido do usuário.

## 2026-08-24 — Content + Automation
**Checagem de novidades nativas + fix de bug no auto-refine**

Rotina automática comparou o guia (87 gatilhos + 175 ações = 262 painéis)
contra o changelog oficial da HighLevel em busca de itens nativos lançados
desde a rodada de 2026-08-10. Detalhe completo em [AUDIT.md](./AUDIT.md#-rodada-2026-08-24--checagem-de-novidades-nativas).

- **AI Agent** (`acoes-highlevel-cat05.html` A6): seletor de modelo agora
  também traz Anthropic e Google, além de OpenAI — campos **Model
  Provider** e **Reasoning Effort** adicionados ao painel e ao mockup.
- **Eventos de Email** (`guia-highlevel-cat02.html` G3): nota sobre o novo
  **Message ID** disponível como custom value no Send Webhook.
- Nenhuma das duas muda a contagem total (são enhancements a itens já
  existentes, não itens novos).
- 6 candidatos novos encontrados mas **não aplicados** — precisam de
  validação humana de campos antes de virar mockup: Badge Issued
  (gatilho), Monday.com, Jira, Linear (25 itens), Housecall Pro, Apify.
- 🐛 **Fix**: `scripts/auto-refine.py` tinha a lista `HAND_CRAFTED`
  desatualizada — não protegia `guia-highlevel-cat13.html` nem
  `acoes-highlevel-cat15/16/17.html`. Rodar o refine nelas destruía o
  `configData` de vários nós (colapsava painéis ricos pra 1 campo
  genérico). Corrigido antes que a rotina semanal abrisse um PR
  corrompendo essas 4 páginas.
- `index.html`: data de "Última atualização" recontada para hoje.

## 2026-08-10 — Content
**Fechamento do gap contra o painel real de Actions: +45 ações, 2 categorias novas**

Auditoria da lista completa do painel de Actions da UI real contra o ebook
encontrou 45 ações faltantes. Todas adicionadas:

- **cat01 Contatos** +2: Mesclar Contato, Verificação de Email
- **cat02 Comunicação** +8: Messenger/IG/TikTok Interativos, Live Chat,
  RCS (interativa + simples), Registrar Ligação Externa, Bot de Agendamento
  Conversation AI. Rename: GMB Confirmation → GMB Messaging
- **cat04 Interno** +1: Drip (liberação em lotes)
- **cat05 IA** +2 e renames: AI Translate, AI Decision Maker;
  Summarize Conversation → AI Summarize; AI Classify → AI Intent Detection
- **cat06 Agendamentos** +1: Gerar Link de Agendamento Único
- **cat07 Oportunidades** +2: Buscar Oportunidade, Remover Dono
- **cat08 Pagamentos** +4: Cobrança Única Stripe, Enviar Estimate,
  Docs & Contratos, Invoice Recorrente
- **cat09 Marketing** +3: Add ao Google Analytics, Add ao Google Ads,
  Relatório de Auditoria de Marketing
- **cat10 Afiliados**: a4/a5 substituídas (Approve/Pay Commission não
  existem no painel) por Adicionar Leads a um Afiliado e Venda Manual
- **cat13 Comunidades** +1: Notificação Push Inteligente
- **NOVA acoes-highlevel-cat16.html** · Objetos & Empresas (9): Custom
  Objects (3), Companies (3), Associations (3, uma em beta)
- **NOVA acoes-highlevel-cat17.html** · Bots & Agentes (12): fluxo interno
  do Conversation AI Bot (9), Eliza (2), Agent Studio (1)

Totais: 87 gatilhos + 175 ações = 262 painéis · 30 páginas · validador OK.

## 2026-08-03 — Content
**Add tutorial video to Contact DND trigger (requested)**

- Vídeo tutorial incorporado logo abaixo da descrição do gatilho
  **Contato Ativou DND (Contact DND)** · `guia-highlevel-cat01.html` G3,
  a pedido do usuário.

## 2026-08-03 — Content
**Add 3 native WhatsApp actions found missing (requested)**

User cross-checked the real HighLevel action list (screenshot of the
"Communication" category) against the guide and flagged 3 native WhatsApp
actions we didn't have yet:

- **Ação — WhatsApp: Verificar Janela de Atendimento (WhatsApp Customer
  Service Window Check)** · `acoes-highlevel-cat02.html` A27. Checks if the
  24h customer-service window is open for a number; branches the workflow
  into Open (free-form messages, no extra cost) / Closed (only approved
  templates). [Official doc](https://help.gohighlevel.com/support/solutions/articles/155000003533-workflow-action-whatsapp-customer-service-window-check)
- **Ação — WhatsApp: Enviar Flow (WhatsApp: Send Flows)** · A28. Sends a
  Meta WhatsApp Flow (in-app guided form/booking) — only works inside the
  Open branch of A27, not supported on COEX integrations. [Official doc](https://help.gohighlevel.com/support/solutions/articles/155000003720-whatsapp-flows-in-app-appointment-booking)
- **Ação — WhatsApp: Mídia (WhatsApp Media)** · A29. Sends image/video/
  audio/document with optional caption (not for audio); only within the
  24h window; documented Meta size/type limits per media type. [Official doc](https://help.gohighlevel.com/support/solutions/articles/155000005235-how-to-send-whatsapp-media-images-videos-audio-document-via-workflow)
- Totais reais agora: **87 gatilhos + 126 ações = 213 entries**
  (`search-index.json` e `AUDIT-TABLE.md` regenerados); `index.html`
  atualizado (cat02: 26→29 ações; hero-stats, tab-count, section-label e
  "Mockups interativos" — 203→206 — recontados).

## 2026-08-03 — Content
**Add tutorial video to Contact Changed trigger (requested)**

- Vídeo tutorial incorporado logo abaixo da descrição do gatilho
  **Alterações no Contato (Contact Changed)** · `guia-highlevel-cat01.html`
  G2, a pedido do usuário.

## 2026-08-03 — Deploy
**Update trial CTA link across the whole guide (requested)**

- Replaced `https://magneticflows.com/30-dias` with the correct affiliate
  link `https://www.gohighlevel.com/highlevel-bootcamp?fp_ref=dantasghl`
  in all 117 occurrences across every page (sidebar CTA, footer CTA, hero
  CTA) — 28 category pages + `index.html`.

## 2026-08-03 — Content
**Add tutorial video to Contact Created trigger (requested)**

- Vídeo tutorial incorporado logo abaixo da descrição do gatilho
  **Criação de Contato (Contact Created)** · `guia-highlevel-cat01.html` G1,
  a pedido do usuário.

## 2026-08-03 — Content
**Add WhatsApp Interactive Messages action (requested) + tutorial video**

- **Ação — Mensagens Interativas do WhatsApp (WhatsApp Interactive Messages)**
  · `acoes-highlevel-cat02.html` A26. Nova ação nativa que envia mensagens
  interativas via API oficial do WhatsApp (Meta) — diferente da já
  existente "WhatsApp Oficial" (A12), que só manda templates estáticos.
  Suporta 4 tipos: Interactive Reply Buttons (até 3 botões), List Message,
  Location Message e Contact Message.
  [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000006082-interactive-whatsapp-messages)
- Vídeo tutorial incorporado logo abaixo da descrição da ação (a pedido do
  usuário).
- 🐛 Fix de drift: "Mockups interativos" no `index.html` estava parado em
  42 há várias rodadas de crescimento de conteúdo; recontado
  programaticamente (`.ghl-mockup` por arquivo) e corrigido pra **203**.
- Totais reais agora: **87 gatilhos + 123 ações = 210 entries**
  (`search-index.json` e `AUDIT-TABLE.md` regenerados); `index.html`
  atualizado (cat02: 25→26 ações; hero-stats, tab-count e section-label
  batendo com o conteúdo real).

## 2026-07-29 — Content
**Add AI Studio Form Submitted as its own trigger (requested)**

The earlier round today treated "AI Studio Form Submitted" as a filter
note on the existing Form Submitted trigger (G5) instead of a separate
entry. On request, added it as a full standalone trigger instead:

- **Gatilho — AI Studio — Formulário Enviado (AI Studio Form Submitted)**
  · `guia-highlevel-cat02.html` G22, new "AI Studio" sidebar section.
  Same underlying Form Submitted engine, applied to forms embedded in an
  AI Studio site, with its own `Domain` / `External Form` filters (both
  required — a site can have more than one AI Studio domain/form). The
  filter note added earlier on G5 stays as a cross-reference. [Official doc](https://help.gohighlevel.com/support/solutions/articles/155000007599-connect-forms-and-calendars-in-ai-studio)
- Sidebar, hero-stats, footer, `index.html` (Eventos card + aggregate
  totals), `search-index.json` and `AUDIT-TABLE.md` updated.
- Totals now: **87 gatilhos, 122 ações, 209 entries**.

## 2026-07-29 — Content
**Check for new native GHL triggers/actions + fix count drift across 4 files**

Routine check against `help.gohighlevel.com` and `ideas.gohighlevel.com` for
native workflow items released since the 2026-07-10 round.

- **Ação — Conceder Pontos na Classificação (Grant Community Group Leaderboard
  Points)** · cat13 A7. Soma pontos ao leaderboard de um grupo da comunidade —
  diferente da A5 (Assign Leaderboard Level), que seta o nível direto. Não
  concede pontos se o contato não for membro do grupo. [Official doc](https://help.gohighlevel.com/support/solutions/articles/155000004080-gamification-leaderboard-triggers-and-actions-for-community-groups)
- **Ação — Mistral AI (Create Chat Completion / Create Embeddings / Analyze
  Image)** · cat05 A8. Native Beta integration — connects Mistral language,
  embedding and vision models to workflows using the user's own Mistral API
  key. [Official doc](https://help.gohighlevel.com/support/solutions/articles/155000007779-mistral-ai-workflow-actions)
- **Gatilho — Form Submitted**: documented the `Domain` / `External Form`
  filters used when the connected form lives on an AI Studio site (the "AI
  Studio Form Submitted" changelog item is the same native trigger, not a
  separate one — added as a filter note on `guia-highlevel-cat02.html` G5
  instead of a duplicate entry).
- **Rename** — our "AI Extract Info" → official doc now says **"AI Extract
  Data"** (same action, confirmed rename, flagged since the 2026-07-10
  audit). Tagged Premium per official doc (per-execution charge).
- **Count drift fixed** (found while auditing, not new HL features):
  - `index.html` tab-counts / section-labels still said 84 gatilhos / 117
    ações while hero-stats already said 86 / 120 (drift from the
    2026-07-20/21 commits that updated hero-stats but not these).
  - `acoes-highlevel-cat05.html` had three different action counts on one
    page (side-nav said 5, hero-desc said 7, hero-stat-num said 6) — the
    Update Conversation AI Bot and Status action (07-20) never got the
    counter bumped everywhere.
  - `acoes-highlevel-cat07.html` side-nav/hero said 9 ações while the page
    actually has 11 blocks — the Remove Followers action (07-21) had the
    same partial-update bug.
  - `CHANGELOG.md` was missing entries for both of those commits — backfilled
    below.
- Totals now: **86 gatilhos, 122 ações, 208 entries** — `search-index.json`
  and `AUDIT-TABLE.md` regenerated, `validate-mockups.js` run against all 28
  pages.
- **Found, not applied** (need a human to confirm exact fields before adding
  full mockups): **Browse AI** (1 trigger "New Completed Task" + 4 actions:
  Run Task, Bulk Run Tasks, Get Task, Get Bulk Run — all premium, own API
  key), **OpenRouter** actions/triggers, **Manus** actions/triggers. See
  `AUDIT.md` for links.

## 2026-07-21 — Content
**Add Remove Followers from Opportunity as cat07 A11**

*(Backfilled — this shipped in commit `2140ed4` without a changelog entry.)*

Companion to A10 (Add Followers): removes specific users — or all at once
via the Remove All Followers toggle — from the opportunity's follower list.
The specific-users picker is shown disabled while the toggle is ON, matching
the real panel behavior. Requires an opportunity in context; skipped
otherwise. [Official doc](https://help.gohighlevel.com/support/solutions/articles/155000004757-workflow-action-remove-followers-from-opportunity)

Sidebar, configData, index (120 ações / 206 painéis / cat07 card 11), meta
descriptions, search-index.json (206 entries) and AUDIT-TABLE updated at the
time. (The page's own hero/side-nav counters were left stale at 9 — fixed in
the 2026-07-29 round above.)

## 2026-07-20 — Content
**Add Update Conversation AI Bot and Status as cat05 A6/A7**

*(Backfilled — this shipped in commit `86099b3` without a changelog entry.)*

The per-contact Conversation AI bot control action was missing from the
ebook. Added to cat05 (AI actions) as an A6 (renumbered to A7 after a rebase
folded in a parallel session's AI Agent addition), "Atualizar Bot de IA e
Status" / "Update Conversation AI Bot and Status", verified against the
official doc. Covers the Conversation AI Bot dropdown, Bot Status
(Active/Inactive, per contact not global) and the conditional Sleep Timer.
[Official doc](https://help.gohighlevel.com/support/solutions/articles/155000003821-workflow-action-update-conversation-ai-bot-and-status)

Sidebar, hero description, index card, hero totals, meta descriptions and
AUDIT-TABLE were updated at the time. (The page's own hero/side-nav counters
were left stale at 5/6 — fixed in the 2026-07-29 round above.)

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
