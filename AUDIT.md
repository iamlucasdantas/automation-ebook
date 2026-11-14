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

## 🆕 Rodada 2026-11-12 — Checagem de novidades nativas

Comparação do guia (87 gatilhos + 175 ações = 262, estado da `main` em
14/09) contra o changelog oficial (`ideas.gohighlevel.com/changelog`), a
central de ajuda (`help.gohighlevel.com`) e o post oficial do LevelUp Day
2026. Esses hosts continuam bloqueados pra acesso direto neste ambiente —
a verificação foi feita via WebSearch, que devolve resumos dessas páginas.
Só entrou o que tem fonte oficial com nome exato; os campos dos painéis
usam apenas o que as fontes descrevem.

### ✅ Aplicados — 11 gatilhos

| Gatilho | Página | Fonte oficial |
|---|---|---|
| Association Created (Labs) | `guia-highlevel-cat01.html` G13 | changelog "Association Created Trigger: Start Workflows When CRM Records Are Linked" |
| Company Created | `guia-highlevel-cat01.html` G14 | help "Company Based Workflows - Company Triggers & Actions" (155000006688) |
| Company Changed | `guia-highlevel-cat01.html` G15 | help "Workflow Trigger - Company Changed" (155000006494) |
| Event Registration (Labs) | `guia-highlevel-cat03.html` G3 | help "Events and Workflows Integration" (155000008431) |
| Client Portal File Uploaded | `guia-highlevel-cat06.html` G13 | changelog "Workflow Trigger for file uploads via Client Portal" |
| Estimates | `guia-highlevel-cat07.html` G11 | help "Trigger - Estimates" (155000003704) |
| Viewed Product | `guia-highlevel-cat08.html` G4 | post LevelUp Day 2026 (categoria Ecommerce Stores) |
| Add to Cart | `guia-highlevel-cat08.html` G5 | post LevelUp Day 2026 (categoria Ecommerce Stores) |
| Product Review Submitted | `guia-highlevel-cat08.html` G6 | help 155000007386 |
| Social Planner Posts | `guia-highlevel-cat10.html` G4 | changelog "Create Workflows with Social Planner Posts" |
| Requested to Join Group | `guia-highlevel-cat11.html` G10 | help "Automate Group Join Requests with Workflows" (155000008439) |

### ✅ Aplicados — 9 ações

| Ação | Página | Fonte oficial |
|---|---|---|
| WhatsApp Typing Indicator | `acoes-highlevel-cat02.html` A38 | changelog "WhatsApp typing indicator action for workflows" (10/11) |
| Add Internal Comment | `acoes-highlevel-cat02.html` A39 | changelog "Conversations: Add Internal Comments Using Workflows" |
| Router | `acoes-highlevel-cat04.html` A23 | changelog "Router: New Workflow Action" |
| Loop | `acoes-highlevel-cat04.html` A24 | changelog "Loop: New Workflow Action" |
| AI Image Generation | `acoes-highlevel-cat05.html` A11 | help 155000008497 + changelog (incl. reference images) |
| AI Video Generation | `acoes-highlevel-cat05.html` A12 | changelog "AI Video Generation: New Workflow Action" |
| Find Object Record | `acoes-highlevel-cat16.html` A10 | help 155000006483 |
| Find Company | `acoes-highlevel-cat16.html` A11 | help 155000006483 |
| Invoke Managed Agent | `acoes-highlevel-cat17.html` A13 | help 155000008858 |

### ⚠ Pontos pra conferir na UI real (aplicados com o que a fonte dá)

- **Viewed Product / Add to Cart** — o post oficial cita filtros "produto,
  valor do carrinho ou duração" sem dizer qual pertence a qual gatilho; um
  blog de terceiros lista outros (store, order source, checkout status).
  Documentei só os do post oficial.
- **Client Portal File Uploaded** — nenhuma fonte lista filtros; painel
  mostra o gatilho sem filtro obrigatório.
- **Router** — as fontes não dizem se existe branch de fallback/"None";
  não documentei nenhuma.
- **Loop** — as fontes não confirmam limite de iterações; não documentei.
- **Invoke Managed Agent** — rótulos exatos dos campos (Agent /
  Instructions) inferidos da descrição do release, não de screenshot.
- **Company Created / Company Changed / Association Created** foram pra
  cat01 (Contatos) por falta de categoria própria de gatilhos de
  Empresas/Objetos — vale decidir se merecem uma categoria nova.

### 🔍 Candidatos NÃO aplicados

- **Register for Ticketed Event / Register for RSVP Event** (ações do
  módulo Events) — nomes só aparecem num resumo de terceiros
  (netpartners.marketing, semana 12–16/10); o artigo oficial confirma só o
  gatilho. Sem campos.
- **AI Analyze Video** e **AI Analyze Image** — existem no changelog
  oficial, mas sem lista de campos. Analyze Image pode ser rename da nossa
  "AI Parse Image" (cat05 A2).
- **Google Sheets — 4 gatilhos premium** (planilha criada, aba criada,
  linha adicionada, linha atualizada) e **Slack — 5 gatilhos premium**:
  anunciados no LevelUp Day 2026, nomes exatos não obtidos.
- **Payment Failed** e **Form Partially Completed** (gatilhos) — só em
  resumo de terceiros (rsla.io).
- Integrações de terceiros vistas no changelog (Todoist, Linear, Browse
  AI, Jotform, Vapi, Mistral AI) — **fora do escopo** ("só nativos");
  Mistral foi removida a pedido em 14/09 e não foi recolocada.

### 🧹 Drift de contagem corrigido

Hero-stat, meta tags, hero-desc e rodapé de 18 páginas agora batem com o
número real de blocos no HTML (ex.: Ações cat02 dizia 29 e tinha 37;
cat08 dizia 5 e tinha 9; cat16/cat17 mostravam "1"). Os cards da home
também. O total do site (`search-index.json`) nunca esteve errado.

Totais: **98 gatilhos + 184 ações = 282 painéis** · 210 mockups
interativos (os 20 itens novos têm painel de configuração, sem mockup
animado).

## 🆕 Rodada 2026-11-13 — Checagem de novidades nativas

Comparação do guia (98 gatilhos + 184 ações = 282, estado da rodada
2026-11-12) contra o changelog oficial e a central de ajuda da HighLevel.
`ideas.gohighlevel.com` e `help.gohighlevel.com` continuam bloqueados pra
acesso direto neste ambiente — a verificação foi feita via WebSearch, que
devolve resumos dessas páginas. Nenhum gatilho/ação novo foi publicado
pela HighLevel entre 12/11 e 13/11; o que entrou nesta rodada são
pendências de rodadas anteriores que agora têm nome e campos em fonte
oficial.

### ✅ Aplicados — 4 gatilhos

| Gatilho | Página | Fonte oficial |
|---|---|---|
| Event Checked In (Labs) | `guia-highlevel-cat03.html` G4 | help "Events and Workflows Integration" (155000008431) |
| Google Sheets · New Spreadsheet (Premium) | `guia-highlevel-cat13.html` G4 | changelog "Google Sheets: Trigger Workflows from New Spreadsheets, Rows, and Worksheets" |
| Google Sheets · New Spreadsheet Row (Premium) | `guia-highlevel-cat13.html` G5 | idem |
| Google Sheets · New Worksheet (Premium) | `guia-highlevel-cat13.html` G6 | idem |

### ✅ Aplicado — 1 correção de ação (sem mudar o total)

- **AI Parse Image → AI Analyze Image** (`acoes-highlevel-cat05.html` A2).
  O artigo oficial "How to Use AI Analyze Image Action in HighLevel
  Workflows" (155000008506) e o changelog "AI Analyze Image: New Workflow
  Action" confirmam o nome e os campos reais: **Image URL** (link público
  e direto pro arquivo), **Prompt** (aceita custom values), **Detail**
  (Auto / High / Low) e **Model**. É ação Premium, processa uma imagem
  por ação, e a resposta sai pelo seletor de custom values — não existe
  campo "Save Output to", que foi removido do painel. Resolve o rename
  pendente de cat05 A2.

### ⚠ Pontos pra conferir na UI real

- **Event Checked In** — a fonte só confirma o filtro por evento
  (nome/tipo); documentei só esse.
- **Google Sheets** — a forma exata do painel (um gatilho "Google Sheets"
  com seletor de evento, ou três gatilhos separados na lista) não está
  clara nas fontes; o guia trata como três itens com campo **Event**. Um
  quarto gatilho ("linha atualizada"), citado no LevelUp Day, não aparece
  no changelog — não foi documentado.
- **AI Analyze Image** — o changelog cita nomes de modelos que não
  consegui confirmar em segunda fonte; o painel mostra o dropdown
  **Model** sem valor.

### 🔍 Candidatos NÃO aplicados

- **Slack — 5 gatilhos premium**: os nomes agora estão confirmados no
  artigo oficial "Slack Workflow Triggers: Setup, Filters & Examples"
  (155000009492) — New Reaction Added, New Direct Message, User Invited
  to Channel, New Mention, New Message Posted to Channel. Não entraram
  porque (a) não existe categoria de gatilhos onde eles caibam — precisa
  de decisão: categoria 14 nova ou outro lugar; (b) os filtros de New
  Reaction Added e New Message Posted to Channel não foram obtidos (os
  outros: canal obrigatório; DM com filtros opcionais de texto e
  remetente).
- **Register for Ticketed Event / Register for RSVP Event** — continuam
  só em resumo de terceiros.
- **AI Analyze Video**, **Payment Failed**, **Form Partially Completed**
  — sem fonte oficial com campos.

Totais: **102 gatilhos + 184 ações = 286 painéis** · 210 mockups
interativos (os 4 gatilhos novos têm painel de configuração, sem mockup
animado).

### ⚠ Processo — nada chegou à `main` desde 14/09

Esta rodada foi construída em cima da branch da rodada de 12/11
(`claude/friendly-meitner-wond0r`), que por sua vez parte da `main`. As
duas continuam **sem merge** — o site publicado segue no estado de 14/09
(87 gatilhos + 175 ações). Pra publicar, basta mergear
`claude/friendly-meitner-gwh4wb` na `main` (contém 12/11 + 13/11).

## 🆕 Rodada 2026-11-14 — Checagem de novidades nativas

Comparação do guia (102 gatilhos + 184 ações = 286, estado da rodada
2026-11-13) contra o changelog oficial e a central de ajuda da HighLevel.
`ideas.gohighlevel.com` e `help.gohighlevel.com` continuam bloqueados pra
acesso direto neste ambiente — a verificação foi feita via WebSearch, que
devolve resumos dessas páginas. Nenhum gatilho/ação novo foi publicado
pela HighLevel entre 13/11 e 14/11.

### ✅ Aplicado — 1 ação

- **AI Analyze Video** (`acoes-highlevel-cat05.html` A13). Fonte:
  changelog oficial "AI Analyze Video: New Workflow Action"
  (`ideas.gohighlevel.com/changelog/ai-analyze-video-new-workflow-action`).
  Fica em AI Actions; campos **Video URL** (link público pra MP4, MOV,
  WebM, MPEG, FLV, WMV ou 3GP, fixo ou dinâmico) e **Prompt** (aceita
  custom values). Ação Premium, cobrada por execução conforme tokens;
  uma URL de vídeo por ação; dá pra testar no builder antes de publicar.

### 🐛 Fix de navegação

- Side-nav do `acoes-highlevel-cat05.html`: o rótulo dizia "10 ações" e
  os itens 09 (Decisor com IA) e 10 (OpenRouter) apontavam pra `#a8` e
  `#a9`. Corrigido pra 13 ações, `#a9` e `#a10`.

### ⚠ Pontos pra conferir na UI real

- **AI Analyze Video** — o changelog não lista todos os rótulos do
  painel; documentei só Video URL e Prompt. Um resumo cita o Google
  Gemini como modelo, outro não confirma — o guia não cita modelo.

### 🔍 Candidatos NÃO aplicados

- **Slack — 5 gatilhos premium** — segue igual a 13/11: nomes
  confirmados, mas falta decidir a categoria e faltam os filtros de New
  Reaction Added e New Message Posted to Channel (o artigo oficial só
  mostra esses dois em captura de tela).
- **Register for Ticketed Event / Register for RSVP Event** — só em
  resumo de terceiros; o artigo oficial "Events and Workflows
  Integration" não cita essas ações.
- **Payment Failed**, **Form Partially Completed** — só em guia de
  terceiros.

Totais: **102 gatilhos + 185 ações = 287 painéis** · 210 mockups
interativos (a ação nova tem painel de configuração, sem mockup animado).

### ⚠ Processo

O PR #23 (`claude/friendly-meitner-gwh4wb`, rodadas de 12/11 e 13/11)
segue aberto. Esta rodada foi feita em cima dele, na branch
`claude/friendly-meitner-kedekw`, que contém as três rodadas. O site
publicado continua no estado de 14/09 (87 gatilhos + 175 ações).

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
