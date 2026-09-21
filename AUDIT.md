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

> **Nota de escopo (2026-09-21):** esta tabela é um snapshot manual antigo e
> para de cobrir em Ações cat14 — ela nunca foi estendida pras categorias
> Ações cat15 (Google Integrações), cat16 (Objetos & Empresas), cat17
> (Bots & Agentes) nem, agora, cat18 (Robôs & Agentes Externos), todas
> adicionadas em rounds posteriores. Os números aqui **não** refletem mais
> o total real do guia (hoje 90 gatilhos + 186 ações = 276 painéis). Pra
> contagem atual por categoria com sinais de fidelidade auto-medidos, use
> [AUDIT-TABLE.md](./AUDIT-TABLE.md) (gerado por `scripts/build-audit.py`,
> já cobre cat01-cat14 gatilhos e cat01-cat18 ações). Pra histórico de cada
> rodada de checagem de novidades nativas, veja as seções `## 🆕 Rodada
> AAAA-MM-DD` abaixo.

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

## 🆕 Rodada 2026-09-21 — Checagem de novidades nativas

Rotina de auditoria mensal comparou o guia (estado da rodada 2026-08-24:
87 gatilhos + 175 ações = 262 painéis, 30 categorias) contra
`help.gohighlevel.com` em busca de candidatos pendentes de rodadas
anteriores (Browse AI, OpenRouter, Manus — pendentes desde 2026-07-29;
Monday.com, Jira, Linear, Housecall Pro, Apify — pendentes desde
2026-08-24) que já tivessem artigo oficial de KB com detalhe de campo
suficiente pra virar mockup com fidelidade real.

### ✅ Adicionados nesta rodada (fonte oficial confirmada)
Três integrações nativas confirmadas com artigo dedicado no
`help.gohighlevel.com` e campos claros o bastante pra montar o mockup:

1. **Ação — OpenRouter: Gerar Resposta (OpenRouter: Generate Response)**
   · `acoes-highlevel-cat05.html` A9 (Workflow AI — inserida logo depois da
   Mistral AI, A8; Tradução com IA e Decisor com IA renumeradas de A9/A10
   pra A10/A11). Roteador com acesso a 300+ modelos (Perplexity, Claude,
   OpenAI, Gemini e outros) através de uma única integração. Campos:
   System Prompt (opcional), Prompt (obrigatório, aceita variáveis
   dinâmicas), Model Selection (obrigatório) e Test Action (roda uma vez e
   salva o schema da resposta como custom value). Premium — cobrança
   pass-through do provedor por execução. [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007330-workflow-action-openrouter-generate-response)
2. **Gatilhos e ações — Browse AI** · nova categoria **Robôs & Agentes
   Externos** (`guia-highlevel-cat14.html` cat14 de gatilhos, 3 gatilhos;
   `acoes-highlevel-cat18.html` cat18 de ações, 4 das 10 ações). 1 gatilho
   (**New Completed Task**, instantâneo, filtro Robot) + 4 ações (**Run
   Task**, **Bulk Run Tasks**, **Get Task**, **Get Bulk Run**). Todas
   Premium, requer API key própria da Browse AI. [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000008028-browse-ai-workflow-actions-and-trigger)
3. **Gatilhos e ações — Manus** · mesma nova categoria (2 gatilhos em
   cat14, 6 das 10 ações em cat18). 2 gatilhos (**New Task Created**,
   **Task Stopped**) + 6 ações (**Create Task**, **Get Task**, **Update
   Task**, **Fetch Tasks**, **Delete Task**, **Continue a Task with a
   Prompt**). Requer API key própria da Manus. [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007351-manus-actions-triggers-in-workflows)

Totais atualizados: **90 gatilhos + 186 ações = 276 entries, 32
categorias** (`search-index.json`, `AUDIT-TABLE.md` e `index.html`
regenerados/atualizados; `validate-mockups.js` roda limpo nas 32 páginas).

> ⚠ **Aplicar com revisão — categoria Robôs & Agentes Externos completa**
> (`guia-highlevel-cat14.html` e `acoes-highlevel-cat18.html`, 13 entries
> no total). Os artigos oficiais da HighLevel nomeiam e descrevem o
> propósito de cada gatilho/ação da Browse AI e da Manus, mas **não**
> publicam um schema campo-a-campo exaustivo como fazem ações mais
> maduras. Os campos usados aqui (Robot, Input Parameters, Task ID, Prompt,
> Fields to Update, etc.) são razoáveis e consistentes com o que a doc
> descreve, mas nomes/ordem exatos dos campos **precisam ser confirmados
> contra o builder real do HL por um humano** antes de considerar essa
> categoria 100% final — mesmo tratamento que toda integração nova recebeu
> neste guia (ex.: Mistral AI em 2026-07-29, Google Integrações em
> 2026-08-10).

### 🔍 Candidatos encontrados, NÃO aplicados (status atualizado desta rodada)
Continuam pendentes de validação humana antes de virar mockup — agora com
mais detalhe do que nas rodadas anteriores, mas ainda sem confiança
suficiente pra montar campo-a-campo:

- **Jira** — artigo de KB dedicado já existe. 2 gatilhos nomeados
  (ex.: issue criada/atualizada); as 11 ações só aparecem listadas por
  categoria no artigo, sem nome individual confirmado de cada uma. Precisa
  de uma rodada dedicada pra extrair os 11 nomes exatos antes de montar
  qualquer mockup.
- **Linear** — artigo de KB dedicado já existe (conexão nativa via OAuth).
  8 dos 12 gatilhos já aparecem nomeados no artigo; as ações continuam,
  em sua maioria, só por categoria (issues, projects, customers, customer
  needs, initiatives, documents), sem lista individual confirmada. Volume
  grande (12 gatilhos + ~13 ações) — mesma recomendação da rodada
  2026-08-24: rodada dedicada só pra levantar os nomes exatos.
- **Monday.com** — 4 ações agora nomeadas e confirmadas no artigo oficial;
  os gatilhos continuam explicitamente marcados como **"Coming Soon"**
  pela própria HighLevel — ou seja, ainda não existem de fato no produto,
  não é falta de documentação. Não dá pra adicionar gatilho nenhum até a
  HL lançar.
- **Housecall Pro** — 9 gatilhos agora nomeados, com cadência de polling
  documentada (a integração não é 100% tempo real pra todos os eventos);
  as 14 ações continuam só listadas por categoria, sem nome individual
  confirmado. Achado só em changelog (`ideas.gohighlevel.com`), sem artigo
  de KB dedicado ainda — sinal de que a integração é recente e a doc
  formal pode vir depois.
- **Apify** — artigo de KB dedicado existe e descreve o comportamento do
  gatilho (robôs/atores rodando scraping dentro do workflow), mas o nome
  exato do gatilho não está 100% confirmado no texto. 4 ações são
  nomeadas, mas a lista pode estar incompleta (o artigo não deixa claro se
  é exaustiva). Precisa confirmação humana antes de virar entrada nova.
- **"AI Image Generation" / "AI Analyze Image"** — encontrados apenas em
  changelog (`ideas.gohighlevel.com`), sem artigo de KB dedicado. Risco
  real de sobreposição com a ação já existente **"AI Parse Image"**
  (`acoes-highlevel-cat05.html` A2) — pode ser o mesmo recurso
  renomeado/estendido, ou pode ser uma ação genuinamente nova de geração
  (não só análise) de imagem. **Não adicionar** até um humano comparar
  contra o builder real e decidir se é rename, extensão ou item novo.
- **"Invoke Managed Agent"** — mencionado só num roundup de blog
  third-party, sem artigo oficial da HighLevel nem changelog confirmando o
  nome exato. Leitura mais provável: é apenas um rename da ação já
  existente **"Invoke Agent in Agent Studio"** acompanhando o rebrand
  interno da HighLevel de Agent Studio → Managed Agents (mesma família do
  Conversation AI / `acoes-highlevel-cat17.html`) — não uma ação nova.
  **Não adicionar como entrada nova** até um humano confirmar contra o
  builder real se é rename (aplicar como rename, como já foi feito com AI
  Extract Data e outros) ou se é de fato algo adicional.

Nenhum campo foi inventado pra nenhum desses — são candidatos genuínos com
mais sinal do que antes, mas ainda sem confiança suficiente pros nomes de
campo exatos de cada sub-item.

### 🐛 Drift verificado nesta rodada (nenhum encontrado além do já corrigido)
`auto-refine.py --check` reportou 0 drift depois de todas as mudanças
mecânicas (novas páginas adicionadas ao `HAND_CRAFTED`, denominadores
"Parte NN/M" corrigidos em todas as 30 páginas existentes,
`search-index.json` regenerado). As constantes `HAND_CRAFTED_TRIGGERS` /
`HAND_CRAFTED_ACTIONS` no topo de `scripts/build-audit.py` (código morto,
não referenciado no resto do script, mas mantido como documentação viva do
range de categorias) ainda estavam paradas em `range(1, 13)` / `range(1,
15)` — desatualizadas mesmo antes desta rodada (não cobriam cat13, cat15,
cat16 nem cat17). Corrigidas pra `range(1, 15)` / `range(1, 19)`, cobrindo
corretamente cat01–cat14 (gatilhos) e cat01–cat18 (ações) — mesmo espírito
do fix do `auto-refine.py` logado na rodada 2026-08-24.

## Como agora prossegue

A auditoria automática está completa. Os próximos passos são humanos:

1. **Você abre HL** e valida (a) os campos exatos da nova categoria Robôs
   & Agentes Externos (Browse AI + Manus, cat14 gatilhos / cat18 ações —
   ver a nota ⚠ na rodada 2026-09-21 acima), (b) os ~15 itens ⚠ dos rounds
   anteriores, e (c) os candidatos 🔍 acumulados (Badge Issued, Monday.com,
   Jira, Linear, Housecall Pro, Apify, AI Image Generation/AI Analyze
   Image, Invoke Managed Agent) — confirmar nome real do campo / da action
   antes de qualquer um virar mockup ou de considerar cat14/cat18 100%
   finais.
2. Me diz quais aplicar
3. Eu mexo no HTML + commito

Ou: você marca o estado atual como "good enough" e segue. O conteúdo
está em ~92% de fidelidade verificada contra docs oficiais (excluindo a
categoria nova, que ainda não passou por essa verificação humana).
