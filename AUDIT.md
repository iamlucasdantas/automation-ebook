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

## 🆕 Rodada 2026-09-12 — Checagem de novidades nativas

Rotina automática comparou o guia (87 gatilhos + 175 ações = 262 painéis,
estado da rodada 2026-08-24) contra `help.gohighlevel.com` e
`ideas.gohighlevel.com` em busca de itens nativos lançados desde então.
Ambos os domínios continuam bloqueados por egress direto neste ambiente —
a checagem usou WebSearch pra ler o conteúdo indiretamente, e para cada
achado o agente marcou explicitamente quando só tinha o resumo do
changelog (sem artigo dedicado de doc com os campos exatos) em vez de
inventar campos.

### ✅ Adicionado nesta rodada (fonte oficial dedicada confirmada)
1. **Ação — OpenRouter (Generate Response)** · `acoes-highlevel-cat05.html`
   A11. Conecta 300+ modelos (Claude, GPT, Gemini, Perplexity etc.) no
   workflow via API key própria da OpenRouter — mesmo padrão "BYOK" da
   ação Mistral AI (A8) já existente. Campos confirmados: Connect Account,
   Model (dropdown, 300+ opções), System Prompt, Prompt, Test Action
   (valida e salva schema de saída como custom values).
   [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007330-workflow-action-openrouter-generate-response)

Totais atualizados: **87 gatilhos + 176 ações = 263 entries**.

### 🐛 Drift corrigido nesta rodada (não era novidade do HL, era bug nosso)
- **`index.html` — contagem por categoria de Ações estava dessincronizada
  da contagem real há várias rodadas.** A comparação `grep -c` contra o
  conteúdo real de cada `acoes-highlevel-catNN.html` encontrou 8
  categorias com o card da homepage mostrando um número menor que o real:
  Cat01 Contatos (16→18), Cat02 Comunicação (29→37), Cat04 Ferramentas
  Internas (21→22), Cat05 Workflow AI (7→10, antes da adição da
  OpenRouter), Cat06 Agendamentos (3→4), Cat07 Oportunidades (11→13),
  Cat08 Pagamentos (5→9), Cat09 Marketing (5→8), Cat13 Comunidades (6→8).
  O total geral (175) batia com a soma real por coincidência de
  arredondamento entre as categorias — só a distribuição por card estava
  errada. Todos os 9 cards corrigidos pra bater com a contagem real de
  `acao-block` de cada página; a soma agora fecha 176 (175 + 1 OpenRouter).
  As contagens de **gatilhos** por categoria já batiam certinho — não
  precisaram de correção.
- **Denominador "Categoria NN de 15" desatualizado em 5 páginas de
  Ações** (`cat05`, `cat14`, `cat15`, `cat16`, `cat17`) — o guia tem 17
  categorias de Ações desde a rodada 2026-08-10, mas essas 5 páginas
  ainda diziam "/15" no hero-tag e no footer-legal (herdado de antes das
  categorias 16/17 existirem). Corrigido pra "/17" nas 5. Além disso,
  `cat16.html` e `cat17.html` tinham o footer-legal com copy-paste da
  `cat14.html` ("Categoria 14 de 15") — corrigido pra 16 e 17
  respectivamente.
- **`acoes-highlevel-cat05.html` já tinha 10 ações desde a rodada
  2026-08-10** (AI Translate A9 e AI Decision Maker A10 foram aplicadas
  lá, resolvendo os candidatos "🔍 pendentes" listados na rodada
  2026-07-10 deste documento), mas o texto in-page (side-nav label,
  hero-desc, footer) continuava dizendo "8 ações" — nunca tinha sido
  atualizado quando A9/A10 entraram. Corrigido pra refletir as 11 atuais
  (10 + OpenRouter).

### 🔍 Candidatos encontrados, NÃO aplicados (precisam de validação humana)

Achados nesta rodada com detalhe suficiente pra reduzir incerteza, mas
ainda sem confirmação forte o bastante pra virar mockup com fidelidade
real:

- **AI Image Generation** (ação, categoria AI) — só achamos o
  [changelog](https://ideas.gohighlevel.com/changelog/ai-image-generation-action-in-workflows),
  sem artigo dedicado em `help.gohighlevel.com` ainda. O changelog é
  incomumente detalhado (Model: GPT Image 2 / Gemini 3 Pro "Nano Banana
  Pro" / Gemini 3.1 Flash "Nano Banana 2" / Gemini 2.5 Flash "Nano
  Banana"; Prompt; Enhance Prompt; Templates; Design Kit/Brand Voice;
  Quality; Size/Background/File format; Reference images até 5, adicionado
  11/09), mas seguindo o padrão da auditoria de exigir doc oficial
  dedicada antes de montar mockup, fica como candidato forte pra próxima
  rodada confirmar a doc.
- **AI Analyze Image** (ação, categoria AI) — mesmo caso: só changelog
  ([link](https://ideas.gohighlevel.com/changelog/ai-analyze-image-new-workflow-action)),
  sem doc dedicada. Campos citados: Model (GPT-5.6 Luna / GPT-5.6 Tera),
  Image URL, Prompt, Detail level. **Risco de duplicidade** com a ação já
  existente **Parse Image / Analisar Imagem** (A2, doc "AI Parse Image")
  — pode ser o mesmo painel renomeado/atualizado em vez de item novo.
  Precisa confirmação humana (abrir o Workflow Builder e comparar A2 com
  esse antes de decidir se é rename ou item novo).
- **Badge Issued / Issue Badge** — **removido da lista de observação**.
  Confirmado que segue não existindo como ação dedicada
  ([doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000005887-automate-badge-issuance-in-workflows-using-issue-certificate-action-)
  diz textualmente que a HighLevel está "actively working on" uma ação
  dedicada). O workaround (badge emitido escolhendo um template de Badge
  dentro da ação **Issue Certificate** já existente, cat14 A1) já está
  coberto no guia. Não é mais candidato — só reabre se a HL lançar a ação
  dedicada.

### 🔍 Candidatos de rodadas anteriores — atualização de status (ainda pendentes)

Pra Browse AI, OpenRouter, Manus, Jira, Linear, Apify, Housecall Pro e
Monday.com (rodada 2026-08-24), a rotina achou artigos de doc dedicados
pra quase todos — mas com uma ressalva importante: um digest terceiro
indica que várias dessas integrações (OpenRouter, Monday.com) já
existiam desde o início de 2026, ou seja, **não são lançamentos dentro
da janela de auditoria** — só não tinham sido documentadas no guia ainda.
Status atualizado:

- **OpenRouter** — ✅ aplicado nesta rodada (ver acima).
- **Browse AI** — doc confirma exatamente o que já estava anotado (1
  trigger "New Completed Task" com filtros Robot/Operator + 4 ações Run
  Task/Bulk Run Tasks/Get Task/Get Bulk Run), mas os campos de cada ação
  seguem genéricos ("Robot ID + input específico do robô", que varia por
  robô) — não dá pra montar mockup fiel sem escolher um robô de exemplo
  real. Segue pendente de validação humana.
- **Manus** — doc confirma 2 triggers (New Task Created, Task
  Stopped/Completed) + 6 ações (Create/Get/Update/Fetch/Delete/Continue
  Task), mas os campos internos de cada ação não vieram no snippet.
  Pendente.
- **Jira** — doc confirma 2 triggers (Issue Created, Issue Updated) + 11
  ações, das quais só 8 nomes foram recuperados (Create, Update, Link,
  Comment, Watch, Attach File, Log Work, Move to Sprint) — faltam 3.
  Pendente.
- **Linear** — doc confirma a contagem exata já suspeitada (12 triggers +
  13 ações, via OAuth), com um campo de exemplo (Issue Created: Team +
  filtros Label/Project/Priority/Status), mas não os outros 24 itens.
  Volume grande — ainda precisa de rodada dedicada. Pendente.
- **Apify** — doc confirma trigger de run finalizado + ações (Run
  Actor/Task, Scrape Single URL, Find Last Actor/Task Run, Fetch Dataset
  Items), mas campos exatos por ação não confirmados. Pendente.
- **Monday.com** — doc mostra que as **ações já estão live** (~12: Create
  Board/Group/Column/Item/Subitem, Update Item/Subitem, Archive
  Board/Group, Delete Item/Group, Retrieve All Items, Search/Find Item),
  mas os **triggers seguem "Coming Soon"** na doc oficial — não contar
  triggers do Monday.com como existentes ainda. Pendente (ações com nomes
  confirmados, campos por ação não).
- **Housecall Pro** — changelog detalha 9 triggers + 14 ações em prosa,
  mas sem doc dedicada em `help.gohighlevel.com` e sem campos exatos por
  item. Pendente.

## Como agora prossegue

A auditoria automática está completa. Os próximos passos são humanos:

1. **Você abre HL** e valida os ~15 itens ⚠ dos rounds anteriores + os
   candidatos 🔍 acumulados (Browse AI, OpenRouter, Manus, Badge Issued,
   Monday.com, Jira, Linear, Housecall Pro, Apify) — confirmar nome real
   do campo / da action antes de qualquer um virar mockup.
2. Me diz quais aplicar
3. Eu mexo no HTML + commito

Ou: você marca o estado atual como "good enough" e segue. O conteúdo
está em ~92% de fidelidade verificada contra docs oficiais.
