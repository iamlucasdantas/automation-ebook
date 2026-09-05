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

## 🆕 Rodada 2026-09-05 — Checagem de novidades nativas

Rotina automática comparou o guia (87 gatilhos + 176 ações = 263 painéis,
estado da rodada 2026-08-31) contra o changelog oficial da HighLevel em
busca de itens nativos lançados desde então. `ideas.gohighlevel.com` e
`help.gohighlevel.com` seguem bloqueados por egress direto neste
ambiente — a checagem usou busca web pra ler o conteúdo indiretamente
(mesma limitação das rodadas anteriores).

### ✅ Aplicado nesta rodada

1. **NOVO gatilho — Avaliação de Produto Enviada (Product Review
   Submitted)** · `guia-highlevel-cat08.html` G4 (categoria Shopify/
   E-commerce Stores). Dispara no instante em que o cliente clica
   "Submit review" num produto da loja HighLevel. Campos confirmados via
   doc oficial: Global Product (seleção única), Store Name, Review Rating
   (1-5★), Review Headline (contains phrase / is not empty), Review
   Comment (contains phrase), User Email, User Name. Mockup + painel de
   config + entrada na sidebar + configData adicionados.
   [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007386-workflow-trigger-product-review-submitted-for-e-commerce-stores-)
2. **Nova Avaliação Recebida** (`guia-highlevel-cat02.html` G16) —
   enhancement: o filtro Fonte da Avaliação (Review Source) era só
   Google/Facebook; a atualização oficial "New Review Received Trigger
   Now Supports All Integrated Review Platforms" expande pra qualquer
   plataforma de reputação conectada (Trustpilot, Yelp, TripAdvisor,
   BBB, etc.), preservando compatibilidade com workflows existentes.
   Texto do gatilho, filtro e `data-name` atualizados. Não muda a
   contagem — enhancement a item já existente.

Totais atualizados: **88 gatilhos + 176 ações = 264 entries**
(`search-index.json` e `AUDIT-TABLE.md` regenerados via script;
`auto-refine.py --check` confirma 0 drift; sintaxe do `configData` de
`guia-highlevel-cat08.html` validada com `node --check`).

### 🔍 Candidatos revisados — sem mudança desde 2026-08-31

Cross-check via busca web desta rodada confirma os mesmos volumes já
registrados na rodada anterior, ainda sem campo-a-campo suficiente pra
montar mockup sem inventar rótulo: **Jira** (2 triggers + 11 actions),
**Housecall Pro** (9 triggers + 14 actions, só Create Customer com campo
confirmado), **Monday.com** (ações no ar, gatilhos ainda "Coming Soon"),
**Linear** (12 triggers + 13 actions, OAuth nativo), **Browse AI**, **Manus**,
**Apify**, **Badge Issued** (gatilho — ação companion Issue Badge segue
"em desenvolvimento"). Nenhum campo foi inventado pra nenhum desses.

### 🟢 Já coberto, não precisou de mudança

- **WhatsApp x WorkFlow Integration** (changelog oficial) — descreve
  capacidades (Customer Replied filtrado por WhatsApp, ação Send
  WhatsApp) que já existem no guia desde rodadas anteriores. Sem gap.
- **Payment Failed** e **Form Partially Completed** — já cobertos em
  `guia-highlevel-cat07.html`.
- **Google Forms** — já coberto em `guia-highlevel-cat13.html`.
- **Airtable** — sem doc oficial dedicada encontrada nesta rodada;
  fontes indiretas mencionam a integração mas sem confirmação suficiente
  pra virar candidato formal.

## Como agora prossegue

A auditoria automática está completa. Os próximos passos são humanos:

1. **Você abre HL** e valida os ~15 itens ⚠ dos rounds anteriores + os
   candidatos 🔍 acumulados (Calendly, HubSpot, Basecamp, Browse AI, Manus,
   Badge Issued, Monday.com, Jira, Linear, Housecall Pro, Apify) — confirmar
   nome real do campo / da action antes de qualquer um virar mockup.
2. Me diz quais aplicar
3. Eu mexo no HTML + commito

Ou: você marca o estado atual como "good enough" e segue. O conteúdo
está em ~92% de fidelidade verificada contra docs oficiais.
