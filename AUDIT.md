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

## 🆕 Rodada 2026-09-07 — Checagem de novidades nativas

Rotina automática comparou o guia (87 gatilhos + 175 ações = 262 painéis,
estado da rodada 2026-08-24) contra `help.gohighlevel.com` e
`ideas.gohighlevel.com` em busca de itens nativos lançados desde então.
Ambos os domínios estão bloqueados por egress direto neste ambiente
(`WebFetch` retornou `EGRESS_BLOCKED` em todas as tentativas, incluindo
mirrors) — a checagem usou WebSearch pra ler o conteúdo indiretamente,
cruzando múltiplas queries e blogs terceiros que acompanham o changelog
semanal do HL antes de reportar qualquer achado.

### ✅ Nenhum gatilho/ação nativo genuinamente novo confirmado nesta janela
Buscas direcionadas por releases de 24/08 a 07/09/2026 não encontraram
nenhum trigger/action novo com fonte oficial datada dentro da janela. Os
itens relevantes que apareceram (Dynamic Value Chips, "Explain This
Workflow", outbound setup movido pro builder) são UX do builder/IA
assistente, não novos tipos de nó. O já aplicado "Claude e Gemini no AI
Agent" (rodada 2026-08-24) continua sendo o único item real dessa
janela — não é novidade.

### 🔓 Candidatos pendentes que GANHARAM doc oficial com campos (ainda NÃO aplicados — pedem rodada dedicada)
Confirmação por WebSearch de artigo oficial dedicado com nomes de campo
reais pra cada um — mas são integrações multi-item (2 a 25 sub-itens),
que pela própria regra deste arquivo ("Volume grande — precisa de rodada
dedicada") pedem confirmação humana dos nomes exatos antes de montar
mockup com fidelidade real. Nenhum campo foi inventado — o que segue é
o que a busca confirmou, com fonte:

- **Jira** — 2 gatilhos (Issue Created, Issue Updated — ambos filtram por
  Project, com seletor de Cloud Site) + 11 ações (create/update/link/
  comment/watch/attach/log-work/move-to-sprint/find issue). Create Issue
  exige Project, Issue Type, Assignee, Summary. Auth OAuth via Atlassian.
  [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000008219-jira-workflow-actions-and-triggers)
- **Monday.com** — 4 gatilhos (New Item in a Board, New Board, Any Column
  Value Changed — filtra por tipo de coluna, Any Item Moved to a Group) +
  ações de create/update board/group/column/item/subitem + find items.
  [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007216-monday-com-actions-and-triggers-in-workflows)
- **Linear** — 12 gatilhos + 13 ações (issues/projects/customers/customer
  needs/initiatives/documents). Auth OAuth nativo. Volume grande — precisa
  de rodada própria só pra listar os 25 itens com confirmação humana.
  [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007978-linear-integration-in-highlevel-workflows)
- **Apify** — 1 gatilho (Actor Run finalizado) + 4 ações (Run a Task,
  Scrape Single URL, Find Last Actor/Task Run, Fetch Dataset Items).
  [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007631-apify-actions-triggers-in-workflows)
- **OpenRouter** — 1 ação apenas (Generate Response: System Prompt,
  Prompt, Model Selection entre 300+ modelos). Sem gatilho, ao contrário
  do que rodadas anteriores supunham. Menor risco por ser item único, mas
  ainda pendente de confirmação humana antes de virar mockup.
  [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007330-workflow-action-openrouter-generate-response)
- **Housecall Pro** — 2 gatilhos (Job Scheduled, Job Completed) + 1 ação
  (Create New Customer). Conteúdo encontrado via snippet de busca parece
  ser texto real do artigo, mas a URL exata do artigo (fora o changelog)
  não foi capturada — confirmar antes de aplicar.
  [Changelog](https://ideas.gohighlevel.com/changelog/housecall-pro-workflow-action-triggers)

**Browse AI** e **Manus** continuam com doc oficial já confirmado desde
2026-07-29, sem mudança nesta rodada.

### 🔴 Badge Issued / Issue Badge — continua sem doc dedicada
Mesmo changelog da rodada 2026-08-24, nenhum artigo novo com campos de
filtro exatos. Um resultado de busca sugeria a ação "Issue Badge" já ter
saído do "em desenvolvimento", mas sem fonte citável — tratando como
ainda pendente, não aplicar.

### 🆕 Achado lateral — integrações nativas com doc completa, nunca sinalizadas em nenhuma rodada anterior
Não são novidade desta janela (docs parecem ser de meses atrás), mas
nunca apareceram em nenhum "Rodada" anterior do AUDIT.md e não existem
em nenhum HTML do guia (confirmado por grep — zero ocorrências em
`deploy-highlevel/`). Ficam registradas aqui como backlog pra próxima
rodada de decisão humana:

- **Cal.com** — 6 gatilhos (Booking Created/Rescheduled/Cancelled, Meeting
  Ended, Out-of-Office Updated, New Recording) + 4 ações (Create/Cancel/
  Reschedule/Find Booking). Hoje o guia só cita Cal.com como exemplo de
  caso de uso, não como painel real.
  [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007879-cal-com-workflow-actions-triggers)
- **HubSpot** — 1 gatilho (New Contact Created) + 5 ações (Create/Find/Get
  by ID/Search by Email Contact, Associate Contact with Company/Deal).
  [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007955-hubspot-workflow-actions-trigger)
- **Klaviyo** — 4 gatilhos por polling de 5min (New Event, New Profile,
  Profile Added to List/Segment) + 17 ações.
  [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000008018-klaviyo-workflow-actions-triggers)
- **Basecamp** — 2 gatilhos (New To-do, New Message Posted) + ações de
  create project/to-do/message/document + find. Premium, cobrança por
  execução, via de mão única.
  [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000006399-basecamp-actions-triggers-in-workflows)
- **Google Forms — lado das ações** (o gatilho já existe no guia em
  `guia-highlevel-cat13.html`, mas faltam as 4 ações: Find Form by ID/
  Name, Find Response by ID, Find Responses by Form Name).
  [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007217-google-forms-actions-and-triggers-in-workflows)

### ✅ Conferido e já coberto corretamente (nada a fazer)
- Operadores "Has Changed / Has Changed To" do gatilho Opportunity Changed
  (`guia-highlevel-cat04.html` G2) — já batem com o changelog oficial.
- WhatsApp × Workflow (Customer Replied + ações de WhatsApp) — já
  cobertos em `guia-highlevel-cat02.html` G4 e `acoes-highlevel-cat02.html`.
- Leaderboard de Community (gatilho + ação) — já cobertos desde 2026-07-29.
- 4 gatilhos de Communities (Post/Comment/Join Request/Event) — já em
  `guia-highlevel-cat11.html`.
- New Affiliate Sales — já em `guia-highlevel-cat05.html` G3.

### 🔍 Checado, não confirmável (não aplicar)
- "Payment Failed" como gatilho próprio e "Form Partially Completed" —
  só apareceram num blog terceiro, sem fonte oficial. Payment Failed já
  existe corretamente como Event Type dentro do gatilho Subscription.
- Client Portal + gatilho "User Login" — changelog sugere que o gatilho
  já existente (`guia-highlevel-cat06.html` G12) agora também dispara do
  novo Client Portal, não só do membership legado. Sem campos novos
  confirmados — checar manualmente no HL antes de qualquer nota.

Totais não mudaram: **87 gatilhos + 175 ações = 262 entries** (nenhum
item novo tinha confiança suficiente pra virar mockup nesta rodada).

## Como agora prossegue

A auditoria automática está completa. Os próximos passos são humanos:

1. **Você abre HL** e valida os ~15 itens ⚠ dos rounds anteriores + os
   candidatos 🔍 acumulados — 5 já com doc oficial detalhada (Jira,
   Monday.com, Linear, Apify, OpenRouter), Housecall Pro perto disso,
   Browse AI/Manus/Badge Issued ainda sem confirmação de campo — mais o
   backlog novo achado em 2026-09-07 (Cal.com, HubSpot, Klaviyo, Basecamp,
   ações do Google Forms) — confirmar nome real do campo / da action
   antes de qualquer um virar mockup.
2. Me diz quais aplicar
3. Eu mexo no HTML + commito

Ou: você marca o estado atual como "good enough" e segue. O conteúdo
está em ~92% de fidelidade verificada contra docs oficiais.
