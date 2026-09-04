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

## 🆕 Rodada 2026-09-04 — Checagem de novidades nativas

Rotina automática comparou o guia (87 gatilhos + 175 ações = 262 painéis,
estado da rodada 2026-08-24) contra o changelog oficial da HighLevel em
busca de itens nativos lançados desde então, e reconferiu o status dos
candidatos pendentes acumulados (Badge Issued/Issue Badge, Monday.com,
Jira, Linear, Housecall Pro, Apify, Browse AI, OpenRouter, Manus).
`ideas.gohighlevel.com` e `help.gohighlevel.com` estão bloqueados por
egress direto neste ambiente (WebFetch retornou `EGRESS_BLOCKED` nos
dois domínios) — a checagem usou WebSearch pra ler o conteúdo indireto.

### ✅ Adicionado nesta rodada (1 ação nova, fonte oficial confirmada)
1. **Ação — OpenRouter (Generate Response)** · `acoes-highlevel-cat05.html`
   A11. Desde a atualização de fevereiro/2026, o OpenRouter ficou
   disponível como ação nativa de Workflow AI — gateway único pra 300+
   modelos (OpenAI, Anthropic/Claude, Google/Gemini, Perplexity e outros)
   usando a própria API key do OpenRouter, com campos claros o bastante
   pra montar um mockup honesto: **Model** (obrigatório), **Prompt**
   (obrigatório, aceita variáveis do workflow), **System Prompt**
   (opcional) e **Output Variable**. Mesmo padrão já usado no mockup da
   Mistral AI (A8). [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007330-workflow-action-openrouter-generate-response)

   Esse candidato já estava pendente desde a rodada 2026-07-29 — o que
   mudou foi a publicação do artigo dedicado com os campos exatos.

Totais atualizados: **87 gatilhos + 176 ações = 263 painéis**
(homepage, `search-index.json` e `AUDIT-TABLE.md` já regenerados).

### 🐛 Drift de contagem corrigido nesta rodada (não era novidade do HL, era bug nosso)
Ao editar `acoes-highlevel-cat05.html` pra adicionar a A11, encontramos
que essa página já tinha 10 ações reais no HTML (A9 Tradução com IA e
A10 Decisor com IA — ambos eram candidatos 🔍 da rodada 2026-07-10 que
foram aplicados em algum commit posterior sem que o meta/side-nav/hero
da própria página fossem atualizados). O `<meta>`, side-nav, hero-stat e
footer da página ainda diziam "8 ações", e o side-nav tinha uma tag
`<a>` mal fechada (`#a8` nunca fechava antes do `#a9` abrir). Corrigido
junto com a adição da A11 — agora a página diz corretamente "11 ações"
em todo lugar e o HTML do side-nav está bem formado.

Também corrigimos o `cat-stat` da Categoria 05 na home (`index.html`),
que dizia "7 ações" — desatualizado desde antes da própria rodada
2026-07-10. Contagem por categoria de Ações na home foi conferida
integralmente contra o HTML real de cada `acoes-highlevel-catNN.html`
nesta rodada (ver seção seguinte pra o que ainda ficou pendente).

### 🔍 Candidatos reconferidos nesta rodada — ainda NÃO aplicados
Pra cada um: já existe artigo oficial dedicado (progresso desde a
rodada 2026-08-24, que só tinha links de changelog), mas os detalhes de
campo encontrados via WebSearch ainda não são suficientes pra montar
mockups fiéis de cada sub-item sem inventar rótulo de campo — volume
grande, precisa de rodada dedicada com confirmação humana ou acesso
direto ao doc (bloqueado neste sandbox):

- **Badge Issued (gatilho) / Issue Badge (ação)** — **sem mudança de
  status**. A HighLevel continua descrevendo a ação "Issue Badge" como
  em desenvolvimento; o workaround oficial recomendado continua sendo a
  ação **Issue Certificate** já existente
  (`acoes-highlevel-cat14.html` A1) selecionando um template de Badge.
  [Doc oficial — workaround](https://help.gohighlevel.com/support/solutions/articles/155000005887-automate-badge-issuance-in-workflows-using-issue-certificate-action-)
- **Monday.com** — agora tem artigo oficial dedicado
  ([doc](https://help.gohighlevel.com/support/solutions/articles/155000007216-monday-com-actions-and-triggers-in-workflows)).
  Ações nativas confirmadas (create board/group/column/item/subitem,
  update item/subitem, archive board/group, delete item/group, get
  board items, find items by column value, find items by ID) — mas os
  **gatilhos ainda estão "Coming Soon"** (não lançados), e os campos
  exatos de cada uma das ~12 ações (ex.: quais colunas/valores um
  "Create Item" espera) não vieram detalhados o bastante pra evitar
  inventar rótulo.
- **Jira** — agora tem artigo oficial dedicado
  ([doc](https://help.gohighlevel.com/support/solutions/articles/155000008219-jira-workflow-actions-and-triggers)).
  Confirmado: **2 gatilhos** (issue criada / issue atualizada) + **11
  ações** (create, update, link, comment, watch, attach, log work, move
  to sprint, entre outras) via OAuth com Atlassian + filtro "Cloud Site".
  Contagem exata agora conhecida, mas os campos específicos de cada uma
  das 13 entradas não.
- **Linear** — artigo oficial confirmado
  ([doc](https://help.gohighlevel.com/support/solutions/articles/155000007978-linear-integration-in-highlevel-workflows)),
  mesmo volume grande já registrado em 2026-08-24 (12 gatilhos + 13
  ações instantâneos via webhook nativo do Linear, cobrindo issues,
  projects, customers, customer needs, initiatives e documents). Ainda
  sem os 25 nomes exatos + campos de cada item.
- **Housecall Pro** — a integração ganhou mais detalhe desde 2026-08-24:
  agora são **9 gatilhos** (Job/Estimate/Lead/Customer Created, Job
  Scheduled, Job Completed/Finished/Canceled, Estimate Scheduled/
  Finished) + **14 ações**, com filtro por customer/tag/employee/campo
  capturado nos gatilhos, e ao menos um campo detalhado (Create Customer
  exige First Name + Last Name, opcionais Email/Company/Mobile/Home
  Number). Ainda falta o detalhe de campo das outras ~22 entradas — não
  o suficiente pra cobrir a integração inteira sem inventar.
- **Apify** — artigo oficial confirmado
  ([doc](https://help.gohighlevel.com/support/solutions/articles/155000007631-apify-actions-triggers-in-workflows)),
  mas o WebSearch não trouxe os campos (ex.: nome exato do parâmetro do
  Actor/input JSON) — mesmo status de 2026-08-24.
- **Manus** — mesmo artigo já linkado desde 2026-07-29
  ([doc](https://help.gohighlevel.com/support/solutions/articles/155000007351-manus-actions-triggers-in-workflows)).
  Confirmado o padrão geral (task-based: create/update/continue/fetch/
  delete task, cada task começa com um prompt) mas sem os rótulos
  exatos de campo de cada uma das ações — sem mudança suficiente pra
  aplicar.
- **Browse AI** — mesmo status de 2026-07-29 (1 gatilho + 4 ações,
  campos ainda não detalhados o bastante).

### 📋 Achados que já existiam no guia (não são gaps)
Durante a checagem, o changelog geral mencionou "Review Received",
"Payment Failed" e "Form Partially Completed" como triggers relevantes
de 2026 — conferimos e **"New Review Received"** já existe como
`guia-highlevel-cat02.html` G16 e **"Payment Failed"** já existe como
gatilho em `acoes-highlevel-cat08.html` (referenciado também em mockup
de `acoes-highlevel-cat02.html`). "Form Partially Completed" não foi
encontrado com artigo oficial dedicado nesta busca — fica de olho pra
próxima rodada, sem virar candidato ainda por falta de fonte oficial
clara.

### ℹ️ Observado mas NÃO corrigido (fora do escopo desta rodada)
Ao investigar o bug de contagem da cat05, notamos que o `cat-stat`
("N ações") de **outras 15 das 17 categorias de Ações** na home
(`index.html`) também está desatualizado em relação à contagem real do
HTML de cada página — soma real 175→176, soma exibida antes desta
rodada era 149. Só corrigimos a Categoria 05 (a que editamos). Também
notamos que o badge visível "Categoria NN/YY" no topo de cada página de
Ações (`hero-tag`) ainda usa denominador antigo (`/14` em cat01-13,
`/15` em cat14-17) enquanto o `<meta>` da mesma página já foi corrigido
pra `/17` numa rodada de SEO anterior (2026-08-24 "Deploy"). Nenhum dos
dois afeta os totais gerais do guia (87/176/263) — são bugs de exibição
por categoria, isolados, que pedem uma rodada de manutenção dedicada
pra recontar e corrigir as 17 páginas de Ações de uma vez, sem risco de
mexer em conteúdo por engano.

## Como agora prossegue

A auditoria automática está completa. Os próximos passos são humanos:

1. **Você abre HL** e valida os ~15 itens ⚠ dos rounds anteriores + os
   candidatos 🔍 acumulados (Browse AI, Manus, Badge Issued, Monday.com,
   Jira, Linear, Housecall Pro, Apify) — confirmar nome real do campo /
   da action antes de qualquer um virar mockup. (OpenRouter já saiu
   dessa lista — aplicado na rodada 2026-09-04.)
2. Me diz quais aplicar
3. Eu mexo no HTML + commito

Ou: você marca o estado atual como "good enough" e segue. O conteúdo
está em ~92% de fidelidade verificada contra docs oficiais.
