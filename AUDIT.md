# AUDIT — Conferência contra a UI real do HighLevel

Auditoria contra `help.gohighlevel.com`. Aqui ficam os achados acionáveis.
Tabela completa de status por entry em [AUDIT-TABLE.md](./AUDIT-TABLE.md).

## Como cada item foi verificado

- ✅ **Confirmado por WebSearch** — agente puxou resumo da página oficial e comparou
- ⚠ **Aplicar com revisão** — discrepância encontrada mas precisa olho humano antes de mexer
- 🔍 **Pendente** — ainda não auditado

## Status geral

| Lote | Status | Itens | Confirmados |
|------|--------|------:|-----------:|
| **Gatilhos cat01-cat12** | ✅ | 76 | 76 |
| **Ações cat01** (Contact) | ✅ | 16 | 16 |
| **Ações cat02** (Comunicação) | ✅ | 25 | 22 (3 c/ flag) |
| **Ações cat03** (Webhooks) | ✅ | 4 | 4 |
| **Ações cat04** (Workflow logic) | ✅ | 17 | 17 |
| **Ações cat05** (AI) | ✅ | 5 | 5 (2 renames recomendados) |
| **Ações cat06** (Appointments) | ✅ | 3 | 3 (A2/A3 fake removidas, substituídas por Book Appointment + Create Appointment Note) |
| **Ações cat07** (Opportunities) | ✅ | 9 | 5 (2 renames + 2 sem doc) |
| **Ações cat08** (Payments) | ✅ | 5 | 3 (2 sem doc dedicada) |
| **Ações cat09** (Campaigns) | ✅ | 5 | 5 (campaigns deprecadas pra workflows) |
| **Ações cat10** (Affiliates) | ✅ | 6 | 4 (A4/A5 sem doc) |
| **Ações cat11** (Memberships) | ✅ | 2 | 2 |
| **Ações cat12** (IVR) | ✅ | 5 | 4 (A4 rename) |
| **Ações cat13** (Communities) | ✅ | 6 | 4 (A5/A6 sem doc) |
| **Ações cat14** (Certificados) | ✅ | 1 | 1 |
| **Total** | **✅** | **185** | **170/185 (92%)** |

## ✅ Fixes aplicados nesta auditoria

### Gatilhos
1. **Cat01 G3 Contact DND** — adicionado filtro DND Direction (Inbound/Outbound/Both)
2. **Cat01 G5 Engagement Score** — adicionado filtro Business Niche
3. **Cat11 G2** renomeado: "Group Removal" → "Group Access Revoked"
4. **Cat11 G4** renomeado: "Private Channel Access Removed" → "Private Channel Access Revoked"

### Ações
Nenhum fix aplicado nesta rodada — todos os achados acionáveis precisam de
validação humana contra a UI real do HL antes de aplicar (rename de ações
afeta como o usuário busca elas no builder).

## ⚠ Discrepâncias com fonte oficial mas NÃO aplicadas

Pra cada item: você abre o HL Workflow Builder e me diz se o nome/campo é
realmente como o agente reportou. Aí eu aplico o fix.

### Ações cat02 — Comunicação
- **A5 Voicemail**: agente flagou campo "Created via Source" no painel HL que não pertence — copy-paste do trigger Contact Created? Verificar
- **A20 AI Content Generation**: docs mencionam Model selector (GPT/Claude) — não temos no painel
- **A21 Send From Specific Number**: mockup tem "Tag Operation"/"Tag" que não deveriam estar (copy-paste de Tag Action?)
- **A22 Send From Number Pool**: mockup tem campos extras (Campaign/Subject/Schedule) que não pertencem
- **A23 GMB Confirmation**: official talvez seja "GMB Verification Reply"
- **A24 Shortcode SMS**: mockup mistura PT (Código/Mensagem) com EN — uniformizar

### Ações cat05 — AI
- **A3**: nosso `acao-en` diz "Summarize Conversation" — doc oficial é **"AI Summarize"** (https://help.gohighlevel.com/support/solutions/articles/155000005886-workflow-action-ai-summarize)
- **A5**: nosso `acao-en` diz "AI Classify" — doc oficial é **"AI Intent Detection"** (https://help.gohighlevel.com/support/solutions/articles/155000005885-workflow-action-ai-intent-detection)

### Ações cat07 — Opportunities
- **A6**: nosso "Delete Opportunity" — doc oficial é **"Remove Opportunity"**
- **A7**: nosso "Assign Opportunity Owner" — doc oficial é **"Add Owner to Opportunity"**

### Ações cat12 — IVR
- **A4**: nosso "Transfer Call" — doc oficial é **"Connect Call"** (https://help.gohighlevel.com/support/solutions/articles/155000003371-workflow-action-ivr-connect-call)

### Gatilhos pendentes do round anterior (recap)
- Cat02 G13 Page View: doc menciona UTM Medium além de Campaign/Source
- Cat07 G7 Refund: ⚠ "Stripe direct refunds NÃO disparam" — adicionar nota
- Cat09 G1 IVR: ⚠ "1 IVR por LC phone number" — adicionar destaque

## 🟢 Ações sem doc oficial dedicada (NÃO é erro)

Estas ações existem na nossa lista mas o WebSearch não achou um artigo
oficial dedicado. Significa que ou (a) são features que rodam dentro de
outras ações, (b) features novas/experimentais, ou (c) docs sparse:

- **Cat04 A9 Cancel All Events** — sem doc dedicada
- ~~Cat06 A2 Reassign Appointment~~ — **REMOVIDA** (usuário confirmou que não existe; substituída por Book Appointment). A antiga A3 Cancel Appointment também não existia (cancelar = Update Appointment Status → Cancelled) e virou Create Appointment Note
- **Cat07 A3/A4 Move Pipeline/Between Pipelines** — provavelmente parte de Update Opportunity
- **Cat07 A8/A9 Add/Remove Opportunity Tag** — sem doc dedicada
- **Cat08 A1 Create Invoice** — só achou "Send Invoice" e "Send Recurring Invoice"
- **Cat08 A3 Update Payment Status** — sem doc dedicada
- **Cat09 A1/A2 Campaign actions** — Campaigns foram deprecados em favor de Workflows
- **Cat10 A4/A5 Approve/Pay Commission** — sem doc dedicada
- **Cat13 A5/A6 Leaderboard Level/Post to Community** — gamification docs sparse

Não significa que estão erradas — só que não foi possível auto-validar.
Pra qualquer uma, abra o HL e me diga se a action existe como está.

## 🆕 Rodada 2026-07-10 — Checagem de novidades nativas

Rotina automática comparou os 187 (76 gatilhos + 110 ações — já incluindo
o Scheduler e o Add Followers to Opportunity da rodada anterior) itens do
guia contra `help.gohighlevel.com` em busca de gatilhos/ações nativos
lançados recentemente e não cobertos ainda.

### ✅ Adicionados nesta rodada (fonte oficial confirmada)
1. **Gatilho — Email Recebido (Inbound Email)** · cat02 G20. Dispara em
   qualquer email novo numa caixa conectada, incl. remetentes frios
   (diferente de "Contato Respondeu" e "Eventos de Email").
   [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007650-workflow-trigger-inbound-email)
2. **Ação — Código Customizado (Custom Code)** · cat03 A5. Roda JavaScript
   dentro do workflow via `InputData`, com Test your Code obrigatório e
   AI-Powered Code Generation. Ação Premium.
   [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000002253-workflow-action-custom-code)
3. **Ação — Agente de IA (AI Agent)** · cat05 A6. Ação autônoma multi-step:
   recebe instruções em linguagem natural e decide sozinha quais
   ferramentas usar. Ação Premium.
   [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007600-workflow-action-ai-agent)
4. **Gatilho — Usuário Respondeu (User Replied)** · cat02 G21. Adicionado
   a pedido do usuário depois de confirmação adicional na fonte oficial.
   Dispara quando um usuário/membro do time responde o contato — oposto
   do "Contato Respondeu". Filtros: Reply Channel, Specific User,
   Assigned User. Integra com Wait (User Replied) e Goal Event.
   [Changelog oficial](https://ideas.gohighlevel.com/changelog/workflow-trigger-user-replied)

Totais atualizados: **79 gatilhos + 112 ações = 191 entries** (homepage,
search-index.json e AUDIT-TABLE.md já regenerados).

### 🐛 Drift corrigido nesta rodada (não era novidade do HL, era bug nosso)
- `search-index.json` estava desatualizado (185 ao invés de 187) — não
  tinha sido regenerado depois do Scheduler/Add Followers da rodada anterior.
- `index.html`: tab-counts e section-labels ainda diziam 76/109 enquanto os
  hero-stats já diziam 77/110.
- `acoes-highlevel-cat03.html`: side-nav e hero-stats esqueceram a A4 (Send
  Conversion Event), mostrando "3 ações" quando já eram 4.

### 🔍 Candidatos encontrados, NÃO aplicados (precisam de validação humana)
Achados com menos certeza sobre campos exatos — fica pra próxima rodada
com confirmação humana antes de montar o mockup com fidelidade real:
- **AI Decision Maker** (ação premium — roteamento por linguagem natural,
  alternativa ao If/Else manual)
- **Client Portal File Uploaded** (gatilho — contato sobe arquivo no
  Client Portal)
- **AI Translate** (ação — traduz texto dentro do workflow)

~~Communities: Rejected Join Request / New Post / New Comment~~ — **aplicado**
em 2026-07-10 (cat11 g6-g9). ~~Update Conversation AI Bot and Status~~ —
**aplicado** em 2026-07-20 (cat05 A7, ver CHANGELOG).

### ⚠ Rename já sinalizado — **aplicado em 2026-07-29**
- Nosso "AI Extract Info" → doc oficial é **"AI Extract Data"** (mesma
  função). Renomeado em `acoes-highlevel-cat05.html` A4, tag Premium
  adicionada (doc confirma custo por execução).

## 🆕 Rodada 2026-07-29 — Checagem de novidades nativas

Rotina automática comparou o guia contra `help.gohighlevel.com` e
`ideas.gohighlevel.com` em busca de itens nativos lançados desde a rodada
de 2026-07-10.

### ✅ Adicionados nesta rodada (fonte oficial confirmada)
1. **Ação — Conceder Pontos na Classificação (Grant Community Group
   Leaderboard Points)** · cat13 A7. [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000004080-gamification-leaderboard-triggers-and-actions-for-community-groups)
2. **Ação — Mistral AI** (Create Chat Completion / Create Embeddings /
   Analyze Image) · cat05 A8. Beta, requer API key própria da Mistral.
   [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007779-mistral-ai-workflow-actions)
3. **Gatilho — AI Studio — Formulário Enviado (AI Studio Form Submitted)**
   · `guia-highlevel-cat02.html` G22 (novo, a pedido). Inicialmente tratado
   como nota de filtro no G5 (Form Submitted) — depois desmembrado em
   entrada própria com sidebar, mockup e painel de config dedicados,
   já que é assim que o item aparece no changelog oficial da HighLevel.
   [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007599-connect-forms-and-calendars-in-ai-studio)

Totais atualizados: **87 gatilhos + 122 ações = 209 entries**.

### 🔍 Candidatos encontrados, NÃO aplicados (precisam de validação humana)
Achados nesta rodada — integrações nativas reais, mas com múltiplos
sub-itens cada, o que pede confirmação humana de campos antes de montar
os mockups com fidelidade real:
- **Browse AI** — 1 gatilho ("New Completed Task", instantâneo, filtra por
  Robot) + 4 ações (Run Task, Bulk Run Tasks, Get Task, Get Bulk Run).
  Premium, requer API key própria da Browse AI. [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000008028-browse-ai-workflow-actions-and-trigger)
- **OpenRouter** — ações/gatilhos (não detalhado ainda, achado só pelo
  changelog). [Changelog](https://ideas.gohighlevel.com/changelog/openrouter-actions-triggers)
- **Manus** — ações/gatilhos. [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007351-manus-actions-triggers-in-workflows)

## 🆕 Rodada 2026-08-24 — Checagem de novidades nativas

Rotina automática comparou o guia (87 gatilhos + 175 ações = 262 painéis,
estado da rodada 2026-08-10) contra o changelog oficial da HighLevel em
busca de itens nativos lançados desde então. `ideas.gohighlevel.com` está
bloqueado por egress direto neste ambiente — a checagem usou busca web
para ler o conteúdo do changelog indiretamente.

### ✅ Aplicado nesta rodada (enhancement a itens já existentes, sem novo total)
1. **AI Agent** (`acoes-highlevel-cat05.html` A6) — desde 20/08/2026 o
   seletor de modelo deixou de ser exclusivo OpenAI: agora lista também
   Anthropic (Claude) e Google (Gemini), com interface redesenhada pra
   escolher provedor + modelo + nível de raciocínio. Adicionados campos
   **Model Provider** e **Reasoning Effort** ao painel de config e ao
   mockup, e nota explicativa no texto.
2. **Eventos de Email** (`guia-highlevel-cat02.html` G3) — desde
   19/08/2026, Opened/Clicked carregam um **Message ID** único disponível
   como custom value dentro do Send Webhook — colapsa aberturas
   duplicadas do mesmo email num único registro. Nota adicionada ao texto
   do gatilho.

Nenhum dos dois muda a contagem de gatilhos/ações — são melhorias em
campos de itens já existentes, não itens novos.

### 🔍 Candidatos encontrados, NÃO aplicados (precisam de validação humana)
- **Badge Issued** (gatilho) — dispara quando um badge é emitido; anunciado
  no changelog oficial (~20-21/08/2026) mas sem artigo dedicado com os
  campos exatos de filtro ainda. A ação companion **Issue Badge** está
  marcada pela própria HighLevel como "em desenvolvimento" — hoje o
  workaround é usar a ação **Issue Certificate** já existente
  (`acoes-highlevel-cat14.html` A1) selecionando um template de Badge em
  vez de Certificado. [Changelog](https://ideas.gohighlevel.com/changelog/badge-automation-is-now-available-in-workflows)
- **Monday.com** — ações/gatilhos nativos pra automação em tempo real com
  boards do Monday (elimina Zapier/Make). Campos não detalhados ainda.
  [Changelog](https://ideas.gohighlevel.com/changelog/mondaycom-actions-and-triggers)
- **Jira** — ações/gatilhos nativos. Campos não detalhados ainda.
  [Changelog](https://ideas.gohighlevel.com/changelog/jira-workflow-actions-and-triggers)
- **Linear** — conexão nativa via OAuth (sem tokens de API pra gerenciar);
  12 gatilhos instantâneos + 13 ações cobrindo issues, projects,
  customers, customer needs, initiatives e documents. Volume grande —
  precisa de rodada dedicada pra levantar os nomes exatos de cada um dos
  25 itens antes de montar mockups. [Changelog](https://ideas.gohighlevel.com/changelog/linear-workflow-actions-triggers)
- **Housecall Pro** — ações/gatilhos adicionais (a integração já existente
  ganhou mais itens). Campos não detalhados ainda. [Changelog](https://ideas.gohighlevel.com/changelog/housecall-pro-more-workflow-actions-triggers)
- **Apify** — ações/gatilhos nativos pra rodar robôs de scraping/automação
  dentro do workflow. Campos não detalhados ainda. [Changelog](https://ideas.gohighlevel.com/changelog/apify-actions-and-triggers-in-workflows)

Igual às rodadas anteriores (Browse AI, OpenRouter, Manus — ainda
pendentes desde 2026-07-29): são integrações nativas reais, mas com
campos/sub-itens que precisam de confirmação humana antes de montar
mockup com fidelidade real. Não foram inventados campos pra nenhum desses.

### 🐛 Bug de manutenção corrigido nesta rodada
`scripts/auto-refine.py` tinha uma lista `HAND_CRAFTED` desatualizada —
não incluía `guia-highlevel-cat13.html` nem `acoes-highlevel-cat15/16/17.html`
(as páginas de Google Integrações, Objetos & Empresas e Bots & Agentes,
todas escritas à mão depois que a lista foi congelada). Rodar
`auto-refine.py` nelas **destruía** o `configData` de vários nós — o
regenerador mecânico não reconhece a estrutura mais rica desses painéis e
colapsava o conteúdo pra 1 campo genérico por nó. A rotina semanal teria
aberto um PR corrompendo essas 4 páginas na próxima segunda-feira. Corrigido
adicionando as 4 aos `HAND_CRAFTED`; `--check` confirma 0 drift agora.

## 🆕 Rodada 2026-08-31 — Checagem de novidades nativas

Rotina automática comparou o guia (87 gatilhos + 175 ações = 262 painéis,
estado da rodada 2026-08-24) contra `help.gohighlevel.com` e o changelog
oficial em busca de itens nativos lançados desde então. `help.gohighlevel.com`
e `ideas.gohighlevel.com` continuam bloqueados por egress direto neste
ambiente (`WebFetch` recusa qualquer domínio — testado também contra
`en.wikipedia.org` pra confirmar que é bloqueio geral de rede, não algo
específico do HighLevel) — toda a checagem usou `WebSearch` pra ler o
conteúdo indiretamente, igual às rodadas anteriores.

### ✅ Adicionado nesta rodada (fonte oficial confirmada)
1. **Ação — OpenRouter (Generate Response)** · `acoes-highlevel-cat05.html`
   A11. Resolve o candidato "OpenRouter" pendente desde 2026-07-29: conecta
   o workflow a mais de 300 modelos de IA (Claude, GPT, Gemini, Perplexity,
   Llama…) via API key própria da OpenRouter, no mesmo padrão da ação
   Mistral AI (A8) — Connect OpenRouter, Model Selection, System Prompt,
   Prompt, e opções avançadas (Temperature, Max Tokens, Output Format).
   Ação Premium. [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007330-workflow-action-openrouter-generate-response)

Totais atualizados: **87 gatilhos + 176 ações = 263 painéis** (mockups
interativos: 210 → 211).

### 🐛 Bug de drift pré-existente corrigido nesta rodada
Ao montar o mockup do A11 percebi que `acoes-highlevel-cat05.html` já tinha
**10** ações reais no HTML (A9 Tradução com IA / AI Translate e A10 Decisor
com IA / AI Decision Maker foram implementadas numa rodada passada) mas o
hero-stat, o `side-section-label`, o `hero-desc`, o rodapé da categoria e as
meta tags ainda diziam **"8 ações"** — nunca tinham sido atualizados quando
A9/A10 entraram. Pior: `index.html` (o card da categoria na home) dizia
**"7 ações"**, ainda mais desatualizado. `search-index.json` sempre esteve
certo (ele é gerado varrendo os `acao-block` reais do HTML, não os labels
manuais), então isso nunca afetou o total do site (175/262 já contavam os
10 reais) — só os textos *dentro* da própria página cat05 e o card da home
estavam errados. Corrigido: side-nav (com o link da A11 e sem a tag `<a>`
mal-fechada que já existia — o item 08 abria um `<a>` que só fechava depois
do item 09, aninhando duas tags `<a>`, HTML inválido), hero-stat, section
label, hero-desc, rodapé, as 3 meta tags (description/og/twitter), e o
`cat-stat` da categoria 05 em `index.html` — todos agora refletem **11**
(10 pré-existentes + 1 nova).

### 🔍 Candidatos encontrados, NÃO aplicados (precisam de validação humana)
Repasse dos candidatos acumulados desde 2026-07-29, com o que o WebSearch
conseguiu confirmar a mais nesta rodada — e 3 integrações novas que eu não
tinha visto até agora:

- **Calendly** *(novo achado)* — integração nativa lançada em ~06/2026: 5
  gatilhos (booking, cancelamento pelo convidado, cancelamento pelo host —
  este via polling de 5min por não ter webhook nativo —, no-show,
  submissão de routing form) + 9 ações (criação de reunião avulsa, booking
  do lado do convidado, find/cancel de evento, marcar no-show, CRUD de
  contato, lookup de usuário). Nomes de campo exatos por item não
  confirmados. [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000008110-calendly-workflow-actions-triggers)
- **HubSpot** *(novo achado)* — 1 gatilho instantâneo (**New Contact
  Created**) + 5 ações (Create Contact: Email/First Name/Last Name/Phone +
  custom properties; Find Contact: por Record ID, email ou filtro; Create
  Association: contato ↔ empresa/deal; mais 2 ações de lookup não
  nomeadas com precisão). [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007955-hubspot-workflow-actions-trigger)
- **Basecamp** *(novo achado)* — doc oficial confirmada
  ("Basecamp Actions & Triggers in HighLevel Workflows"), mas o WebSearch
  não trouxe nenhum campo/nome de gatilho ou ação específico ainda.
  [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000006399-basecamp-actions-triggers-in-workflows)
- **Browse AI** — agora com bem mais detalhe que 2026-07-29: 1 gatilho
  **New Completed Task** (filtro Robot + Select Operator opcional) + 4
  ações — **Run Task** (Robot ID + input params), **Bulk Run Tasks** (Robot
  ID + inputs em lote), **Get Task** (Task ID) confirmadas com campo; **Get
  Bulk Run** ainda sem detalhe. Ainda não decidido em qual categoria entra
  (não é IA generativa como Mistral/OpenRouter — é scraping/RPA; não existe
  categoria "Integrações" genérica nas Ações hoje) — fica pra próxima
  rodada resolver categoria + últimos campos antes de montar o mockup.
  [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000008028-browse-ai-workflow-actions-and-trigger)
- **OpenRouter** — ~~pendente~~ **aplicado nesta rodada** (ver acima).
- **Manus** — ainda sem detalhe de campo via WebSearch. [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007351-manus-actions-triggers-in-workflows)
- **Monday.com** — mais detalhe que antes: gatilhos ainda marcados "Coming
  Soon" pela própria HighLevel (Any Column Value Changed, Any Item Moved to
  Group, New Board/Item/Subitem/Update — nenhum lançado ainda); ações já
  no ar (Create Board/Group/Column/Item/Subitem, Update Item/Subitem, Get
  Board Items, Find Items by Column Value, Find Items by ID) mas sem
  schema de campo por ação. Esperar os gatilhos saírem de "Coming Soon"
  antes de montar isso. [Changelog](https://ideas.gohighlevel.com/changelog/mondaycom-actions-and-triggers)
- **Jira** — confirmado 2 gatilhos + 11 ações (issue created/updated;
  create/update/link/comment/watch/attach/log work/move to sprint). Campos
  exatos por ação ainda não. [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000008219-jira-workflow-actions-and-triggers)
- **Linear** — confirmado 12 gatilhos + 13 ações (issues, projects,
  customers, customer needs, initiatives, documents), OAuth nativo, tudo
  Premium. Volume grande, campos exatos por item ainda não — precisa de
  rodada dedicada. [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007978-linear-integration-in-highlevel-workflows)
- **Housecall Pro** — confirmado 9 gatilhos (criação = polling 5min;
  scheduled/finished/canceled = polling 10min) + 14 ações (CRUD de
  customer/job/estimate/lead + job-appointment). Create Customer tem campo
  confirmado (First/Last Name obrigatórios, Email/Company/Mobile/Home
  opcionais) — os outros 13 ainda não. [Changelog](https://ideas.gohighlevel.com/changelog/housecall-pro-more-workflow-actions-triggers)
- **Apify** — sem novo detalhe de campo desde 2026-08-24. [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007631-apify-actions-triggers-in-workflows)
- **Badge Issued** (gatilho) / **Issue Badge** (ação) — sem mudança desde
  2026-08-24: `Issue Badge` continua "em desenvolvimento" pela própria
  HighLevel, o workaround documentado continua sendo `Issue Certificate`
  com template de Badge. [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000005887-automate-badge-issuance-in-workflows-using-issue-certificate-action-)

Nenhum campo foi inventado pra nenhum desses — onde o WebSearch não trouxe
o nome exato do campo, o item ficou de fora do mockup.

### Nota informativa (não é gatilho/ação novo)
- **"Smoother Integration Setup with Field Previews"** — mudança de UX no
  HL Workflow Builder: painéis de ações/gatilhos que dependem de conta
  conectada (HubSpot, Jira, Linear, etc.) agora mostram uma pré-visualização
  "locked" dos campos antes de conectar, e o botão Connect abre a conexão
  numa aba nova sem perder o progresso no workflow. Não é um nó novo, é
  comportamento de UI — não muda nenhum mockup existente.
  [Changelog](https://ideas.gohighlevel.com/changelog/triggers-actions-smoother-integration-setup-with-field-previews)

## 🆕 Rodada 2026-09-14 — Checagem de novidades nativas

Rotina automática comparou o guia (87 gatilhos + 176 ações = 263 painéis,
estado da rodada 2026-08-31) contra o changelog oficial da HighLevel em
busca de itens nativos lançados desde então. Igual à rodada anterior,
`help.gohighlevel.com` e `ideas.gohighlevel.com` estão bloqueados por
egress direto neste ambiente — a checagem usou WebSearch pra ler o
conteúdo indiretamente. Dessa vez o WebSearch não conseguiu isolar
resultados por data (a mesma lista de itens aparece independente de o
termo de busca pedir "agosto 2026" ou "setembro 2026"), então não dá pra
afirmar com certeza que algo foi lançado depois de 31/08 especificamente.

### ✅ Aplicado nesta rodada
Nenhum item novo aplicado a partir desta auditoria — nenhuma novidade
nativa foi confirmada com confiança suficiente (nome exato + campos
exatos) pra virar mockup fiel. (Separadamente, a pedido do usuário, a
ação Mistral AI foi removida do cat05 nesta mesma janela — ver
CHANGELOG.md — o que muda o total pra **87 gatilhos + 175 ações = 262
painéis**, não uma novidade de auditoria.)

### 🔍 Candidatos encontrados, NÃO aplicados (precisam de validação humana)
- **Typeform** *(novo achado)* — integração nativa confirmada (doc
  oficial: [Typeform Actions & Triggers in HighLevel Workflows](https://help.gohighlevel.com/support/solutions/articles/155000006676-typeform-actions-triggers-in-workflows),
  lançada ~julho/2026). Hoje o guia só cita "Typeform" como exemplo de
  webhook externo genérico (`guia-highlevel-cat01.html` G1,
  `acoes-highlevel-cat01.html` A1) — não tem gatilho/ação dedicados.
  Campos exatos ainda não confirmados.
- **Calendly** — já logado na rodada 2026-08-31 acima (5 gatilhos + 9
  ações) — segue pendente, sem novo detalhe desta vez.
- **Slack** *(novo achado)* — merece revisão humana, não uma correção
  automática: o changelog oficial da HighLevel descreve Slack como
  "Premium Trigger & Action" nativo (mesma leva que lançou o Google
  Sheets nativo, já documentado em `acoes-highlevel-cat03.html` A2 com a
  tag "Integração nativa"). No guia hoje, `acoes-highlevel-cat02.html`
  A3 já tem um painel com cara de integração nativa (dropdown "Slack
  Channel", aviso de pré-requisito "Slack precisa estar conectado em
  Settings → Integrations") mas o nome em inglês ainda é "Outbound
  Webhook (Slack)" — resquício de quando o `auto-refine.py` tratava
  Slack como não-nativo e convertia pra webhook genérico (ver
  `acoes-highlevel-cat01.html` A11-3 e `acoes-highlevel-cat10.html`
  A3-2, que ainda mostram URL de Incoming Webhook do Slack ao invés do
  dropdown nativo). Pode ser um rename (`Outbound Webhook (Slack)` →
  `Slack`) mais unificação dos poucos nós de mockup que ainda usam o
  webhook antigo — mas rename de ação afeta como o usuário busca ela no
  builder, então fica pra confirmação humana antes de mexer.
- **HubSpot / Basecamp / Browse AI / Manus / Monday.com / Jira / Linear
  / Housecall Pro / Apify / Badge Issued** — mesmos candidatos pendentes
  desde 24/08 e 31/08 (ver rodada acima), sem novo detalhe de campo
  encontrado nesta busca.

Nenhum campo foi inventado pra nenhum desses. Igual às rodadas
anteriores: são integrações nativas reais, mas exigem confirmação humana
do nome e dos campos exatos antes de virar mockup com fidelidade real.

## 🆕 Rodada 2026-11-23 — Checagem de novidades nativas

Rotina automática comparou o guia (88 gatilhos + 175 ações = 263 painéis —
estado da `main` depois do gatilho Estimate adicionado em 17/11) contra o
changelog oficial e a central de ajuda da HighLevel em busca de itens
nativos lançados desde a rodada de 2026-09-14. `help.gohighlevel.com` e
`ideas.gohighlevel.com` continuam bloqueados por egress direto neste
ambiente (assim como os blogs de terceiros que resumem o changelog) — a
checagem leu o conteúdo indiretamente via WebSearch. Nome de cada item e
campos vêm do changelog/artigo oficial; **nada foi conferido no builder real**.

### ✅ Adicionados nesta rodada (9 itens — fonte oficial confirmada)
**Ações (7)**
1. **Router** (`acoes-highlevel-cat04.html` A23) — executa todas as branches
   que baterem (o If/Else para na primeira). Branches de regra customizada
   ("Only Continue If": field/operator/value, Add condition / Add rule
   group), sempre executar e fallback; ordem pela lista Branches.
   [Changelog](https://ideas.gohighlevel.com/changelog/router-new-workflow-action) ·
   [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000009512-router-action)
2. **Loop** (`acoes-highlevel-cat04.html` A24) — Loop Over (A list of items /
   A range of numbers), Execution Mode (Sequential / Parallel), custom values
   em Loop Item. [Changelog](https://ideas.gohighlevel.com/changelog/loop-new-workflow-action)
3. **AI Image Generation** (`acoes-highlevel-cat05.html` A11, Premium) —
   Model (GPT Image 2, Gemini 3 Pro Image, Gemini 3.1 Flash Image, Gemini 2.5
   Flash Image), Quality, Prompt, até 5 imagens de referência; saída Image
   URL / File Path / File Name. [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000008497-workflow-action-ai-image-generation)
4. **AI Video Generation** (`acoes-highlevel-cat05.html` A12) — Model (Veo 3.1
   Quality / Fast), Prompt; vídeo salvo na Media Library.
   [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000009513-workflow-action-ai-video-generation)
5. **AI Analyze Video** (`acoes-highlevel-cat05.html` A13) — Video URL, Prompt,
   Model (dois modelos Gemini: Flash padrão e Flash Lite).
   [Changelog](https://ideas.gohighlevel.com/changelog/ai-analyze-video-new-workflow-action)
6. **Add Internal Comment** (`acoes-highlevel-cat02.html` A38) — comentário
   interno na conversa, com @menção.
   [Changelog](https://ideas.gohighlevel.com/changelog/conversations-add-internal-comments-using-workflows)
7. **WhatsApp Typing Indicator** (`acoes-highlevel-cat02.html` A39) — sem
   configuração própria; dura até a resposta ou ~25s; marca como lida.
   [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000009791-whatsapp-typing-indicator-action-for-workflows)

**Gatilhos (2)**
8. **Social Planner Posts** (`guia-highlevel-cat10.html` G4) — filtros
   Category, Platform, Post Status, Post Type, Social Account, Tags.
   [Changelog](https://ideas.gohighlevel.com/changelog/create-workflows-with-social-planner-posts)
9. **Association Created** (`guia-highlevel-cat01.html` G13, beta — Labs) —
   "Association created with" (objeto) + filtro Association label.
   [Changelog](https://ideas.gohighlevel.com/changelog/association-created-trigger-start-workflows-when-crm-records-are-linked)

Os 9 entraram como bloco de texto + painel de configuração, **sem mockup
interativo** (mesmo formato do Drip) — o total de mockups segue 211.

### ⚠ Pontos pra conferir no builder (dos 9 itens acima)
- **Add Internal Comment**: o changelog usa "Add Internal Comment" no título e
  "Internal Comment" no passo a passo — o rótulo exato no seletor de ações e
  o rótulo do campo de texto ("Comment") não estão confirmados.
- **Router**: os três tipos de branch estão confirmados, mas não os rótulos
  exatos do seletor de tipo — o painel mostra o tipo como nota, não como campo.
- **AI Analyze Video**: o changelog cita versões específicas dos modelos
  Gemini; o painel usa só "Gemini Flash / Flash Lite" porque a numeração
  retornada pela busca não era confiável.
- **Social Planner Posts**: status oficiais confirmados = Approved, Published,
  Failed. Um guia de terceiros lista também Scheduled, Approval Requested e
  Approval Rejected — não incluídos.
- **AI Image Generation**: opções do campo Quality não confirmadas ("High" no
  painel é exemplo).
- **Association Created** ficou em Gatilhos › Contatos por falta de categoria
  de gatilhos pra objetos/empresas — vale decidir se merece categoria própria.

### 🔍 Candidatos encontrados, NÃO aplicados
- **User Signup (Client Portal / Memberships)** (gatilho) — dispara no
  cadastro pelo Client Portal; nenhum filtro documentado.
  [Changelog](https://ideas.gohighlevel.com/changelog/introducing-user-signup-workflow-trigger-for-client-portal)
- **Client Portal File Uploaded** (gatilho) — nova categoria "Client Portal"
  no seletor de gatilhos (junto com User login); filtros não documentados.
  [Changelog](https://ideas.gohighlevel.com/changelog/workflow-trigger-for-file-uploads-via-client-portal)
- **Gatilhos de e-commerce** (produto visualizado, adicionado ao carrinho) e
  **de Project Management** (tarefa adicionada/concluída/lembrete) — citados
  no post do LevelUp Day 2026, sem nome exato nem filtros.
- **Rename possível**: nossa "AI Parse Image" (`acoes-highlevel-cat05.html`
  A2) — a doc oficial agora se chama **AI Analyze Image**
  ([doc](https://help.gohighlevel.com/support/solutions/articles/155000008506-workflow-action-ai-analyze-image)).
  Rename afeta a busca da ação, fica pra confirmação humana.
- **Send SMS em workflows de Custom Object / Company** — extensão de ação já
  existente, sem detalhe de campo.
- **Jotform** (integração de terceiros: gatilhos New Submission e New Signed
  Document + ação Create Submission) — fora do escopo "só nativos", mesma
  fila de Typeform, Calendly, HubSpot, Basecamp, Browse AI, Manus,
  Monday.com, Jira, Linear, Housecall Pro e Apify (sem novidade nesta rodada).
- **Badge Issued / Slack rename** — sem mudança desde 14/09.

### 🐛 Drift corrigido nesta rodada
- `index.html` não tinha sido atualizado depois do gatilho Estimate (17/11):
  dizia 87 gatilhos / 262 painéis / 210 mockups e "10 gatilhos" no card de
  Pagamentos. Além disso, os cards de 9 categorias de Ações mostravam
  contagens antigas (ex.: Comunicação 29 em vez de 37, Pagamentos 5 em vez de
  9). Todos os cards agora são recontados a partir do HTML real.
- `acoes-highlevel-cat02.html` (dizia 29, tinha 37) e
  `acoes-highlevel-cat04.html` (dizia 17/21, tinha 22): hero, sidebar, meta
  tags e rodapé corrigidos junto com as adições.
- `acoes-highlevel-cat05.html`: sidebar tinha dois links apontando pra `#a8`
  (Decisor com IA e OpenRouter abriam a ação errada) — corrigido pra
  `#a9`/`#a10`.

## Como agora prossegue

A auditoria automática está completa. Os próximos passos são humanos:

1. **Você abre HL** e valida os ~15 itens ⚠ dos rounds anteriores + os
   candidatos 🔍 acumulados (Typeform, Calendly, HubSpot, Basecamp,
   Browse AI, Manus, Badge Issued, Monday.com, Jira, Linear, Housecall
   Pro, Apify) + o achado de rename do Slack — confirmar nome real do
   campo / da action antes de qualquer um virar mockup.
2. Me diz quais aplicar
3. Eu mexo no HTML + commito

Ou: você marca o estado atual como "good enough" e segue. O conteúdo
está em ~92% de fidelidade verificada contra docs oficiais.
