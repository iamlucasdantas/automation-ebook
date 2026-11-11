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

## 🆕 Rodada 2026-11-11 — Checagem de novidades nativas

Rotina automática comparou o guia (87 gatilhos + 175 ações = 262 painéis,
estado da rodada 2026-08-24) contra o changelog e a central de ajuda oficiais
da HighLevel em busca de itens **nativos** lançados desde então.
`ideas.gohighlevel.com`, `help.gohighlevel.com` e os agregadores de release
notes continuam bloqueados por egress direto neste ambiente — a checagem usou
busca web pra ler o conteúdo dessas páginas indiretamente, igual às rodadas
anteriores. Nenhum campo foi inventado: itens sem descrição de campo
confiável ficaram na lista 🔍.

### ✅ Gatilhos novos aplicados (+3 · 87 → 90)

| # | Gatilho | Página | Filtros documentados |
|---|---------|--------|----------------------|
| 1 | **Produto Visualizado** · Product Viewed | `guia-highlevel-cat08.html` G4 | Store, Product, Duration, Checkout Status |
| 2 | **Produto Adicionado ao Carrinho** · Add Products to Cart | `guia-highlevel-cat08.html` G5 | Store, Product, Cart Value, Duration, Checkout Status |
| 3 | **Registro em Evento** · Event Registration | `guia-highlevel-cat03.html` G3 | Event, Ticket Type, Registration State |

Os dois primeiros são da categoria **Ecommerce Stores** e valem tanto pra loja
nativa do HighLevel quanto pra Shopify conectada — nesse caso exigindo o Web
Pixel instalado. Visitante não logado é rastreado anonimamente no navegador até
se identificar. O terceiro é do módulo **Events**, ainda em beta/Labs: cada
registro entra no workflow de forma independente e o *wait* relativo à data do
evento calcula em cima do evento em que o contato entrou.

### ✅ Ações novas aplicadas (+7 · 175 → 182)

| # | Ação | Página | Observação |
|---|------|--------|------------|
| 1 | **Loop** | `acoes-highlevel-cat04.html` A23 | List ou Number Range; item da vez exposto como custom value de Loop Item; aba Test por iteração |
| 2 | **Router** | `acoes-highlevel-cat04.html` A24 | Executa **todas** as branches verdadeiras (If/Else para na primeira). Branch types: Custom Rules, Always Run, Fallback |
| 3 | **Comentário Interno** · Add Internal Comment | `acoes-highlevel-cat02.html` A38 | @menção de usuários; notificação segue as preferências de cada usuário |
| 4 | **Indicador de Digitação WhatsApp** · WhatsApp Typing Indicator | `acoes-highlevel-cat02.html` A39 | Expira em 25s ou na resposta; marca como lida (tiques azuis); WhatsApp Cloud API |
| 5 | **Registrar em Evento com Ingresso** · Register for Ticketed Event | `acoes-highlevel-cat06.html` A5 | Events (beta/Labs) |
| 6 | **Registrar em Evento RSVP** · Register for RSVP Event | `acoes-highlevel-cat06.html` A6 | Events (beta/Labs) |
| 7 | **Invocar Managed Agent** · Invoke Managed Agent | `acoes-highlevel-cat17.html` A13 | Só lista agentes publicados com o trigger *Invoked from a workflow* |

⚠ **Não confundir A13 com A12.** `Invoke Agent in Agent Studio` (A12) é pra
agentes baseados em flow e tem configuração de gatilho própria; `Invoke Managed
Agent` (A13) é pra Managed Agents publicados. A própria central de ajuda da HL
faz essa separação explícita.

⚠ **Events e Register for Ticketed/RSVP Event estão em beta (Labs).** Os nomes
das duas ações vêm de roundup de release notes (semana de 12–16/10/2026), não de
artigo dedicado da HL — o módulo Events tem artigo oficial, as duas ações não.
Marcadas com a tag `Beta · Labs` no guia. **Vale confirmar os campos na UI real**
antes de tratar esses dois painéis como definitivos.

### ✅ Enhancements em itens já existentes (não mudam o total)

1. **Pedido Concluído (Order Fulfilled)** · `guia-highlevel-cat08.html` G3 —
   a versão unificada de Ecommerce Stores ganhou filtros de **Fulfilled
   Products**, **Order Source** (Store/External) e **Tracking Details**
   (transportadora + código). O gatilho legado passou a aparecer como
   **Shopify Order Fulfilled (Deprecating Soon)**; workflows que já usam o
   legado continuam funcionando, mas automação nova deve usar o unificado.
   Filtros e nota de deprecação adicionados ao painel.
2. **Oportunidade Alterada (Opportunity Changed)** · `guia-highlevel-cat04.html`
   G2 — operadores **Has Changed** e **Has Changed To** adicionados ao guia num
   bloco próprio. Eles resolvem exatamente o problema de volume que o próprio
   bloco de alerta da página já descrevia: antes, filtrar por valor atual (*is*)
   redisparava em toda edição subsequente enquanto o campo continuasse igual.

### 🔍 Candidatos encontrados, NÃO aplicados

**Fora do escopo "só nativo"** — são integrações de terceiros, mesma régua que
já tinha excluído Slack (substituído por Outbound Webhook no guia) e deixado
Monday/Jira/Linear/Apify de fora nas rodadas anteriores:

- **Jotform** — gatilhos New Submission e New Signed Document + ação Create
  Submission. Conexão por API key do Jotform. É integração nativa de um produto
  de terceiro, não trigger/action nativo do HighLevel.
- **Browse AI** — 1 gatilho instantâneo (New Completed Task) + 4 ações (Run
  Task, Bulk Run Tasks, Get Task, Get Bulk Run). Pendente desde 2026-07-29 pelo
  mesmo motivo.
- **Slack** — 5 gatilhos premium anunciados no LevelUp Day 2026.
- **Google Sheets** — gatilhos de nova linha e linha atualizada. (A **ação**
  Google Sheets já está no guia em `acoes-highlevel-cat03.html` A2 desde antes;
  os gatilhos novos ficam de fora pela mesma régua.)

**Nativo, mas precisa de validação humana antes de virar painel:**

- **Association Created** (gatilho) — nativo, dispara quando uma associação é
  criada entre registros; funciona com Contacts, Opportunities, Custom Objects e
  Companies, em workflows standard, de Custom Object e de Company. Tem filtro de
  **Association label**. Está atrás de toggle no **Labs** e foi anunciado junto
  com os Company-based workflows. O guia hoje não tem categoria de **gatilhos**
  de Objetos & Empresas (só a de *ações*, `acoes-highlevel-cat16.html`) — entrar
  com ele significa abrir uma 14ª categoria de gatilhos, com cascata de
  renumeração "Parte NN/14", sitemap e canonicals. Decisão de escopo humana,
  não de rotina automática.

**Já cobertos, nenhuma ação necessária:** os 4 gatilhos novos de Communities
(Join Request Rejected, New Post, New Comment, Group Event Registration) já
tinham entrado como `guia-highlevel-cat11.html` G6–G9 na rodada de 2026-08-10.

### 🐛 Bug de manutenção corrigido nesta rodada

`scripts/build-search-index.py` extraía a descrição de cada entry com um regex
que só casava `O que esse` e `O que essa`. As páginas de **ações** usam
`O que esta ação faz` — ou seja, **169 das 175 ações estavam indexadas com
descrição vazia** desde que o índice de busca foi criado. Na prática a busca do
site achava ação por nome, EN, categoria, tag e keyword, mas **nunca pelo texto
da descrição**, enquanto gatilho era encontrável por texto normalmente. Regex
corrigido pra aceitar as três variantes; agora 272/272 entradas têm descrição.

Efeito colateral esperado no diff: `search-index.json` cresce bastante nesta
rodada, porque 169 descrições que antes eram `""` passaram a ter conteúdo.

### 📊 Totais depois desta rodada

| | Antes (2026-08-24) | Depois (2026-11-11) |
|---|---:|---:|
| Gatilhos | 87 | **90** |
| Ações | 175 | **182** |
| Painéis | 262 | **272** |
| Páginas | 30 | 30 |

`auto-refine.py --check` → 0 drift · `validate-mockups.js` → ALL 30 PAGES OK.

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
