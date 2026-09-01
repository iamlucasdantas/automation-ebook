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

## 🆕 Rodada 2026-09-01 — Checagem de novidades nativas

Rotina automática comparou o guia (87 gatilhos + 175 ações = 262 painéis,
estado da rodada 2026-08-24) contra `help.gohighlevel.com` e o changelog
oficial da HighLevel em busca de itens nativos lançados/atualizados desde
então. `ideas.gohighlevel.com` segue bloqueado por egress direto neste
ambiente — a checagem usou busca web pra ler o conteúdo do changelog e dos
artigos de `help.gohighlevel.com` indiretamente.

### ✅ Adicionado nesta rodada (fonte oficial confirmada)
1. **Gatilho — Solicitação de Entrada no Grupo (Requested to Join Group)**
   · `guia-highlevel-cat11.html` G10. Dispara quando um usuário envia um
   pedido de entrada num grupo da comunidade com acesso por solicitação —
   antes de qualquer aprovação/rejeição (diferente do já existente G7
   "Community Group Join Request Rejected", que dispara só na rejeição).
   Filtro principal **Group** (obrigatório) + filtros dinâmicos por
   **Membership Question Responses** (cada pergunta de admissão
   configurada pro grupo vira um campo de filtro próprio). Caso de uso
   oficial: passar a resposta por um prompt de IA pra triagem de spam
   antes do If/Else decidir aprovar ou encaminhar pra revisão manual.
   [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000008439-automate-group-join-requests-with-workflows) ·
   [Changelog](https://ideas.gohighlevel.com/changelog/communities-smarter-join-requests-with-workflow-automation)

Totais atualizados: **88 gatilhos + 175 ações = 263 painéis** (homepage,
`guia-highlevel-cat11.html` e `search-index.json` já regenerados).

Conferido e **não** alterado — o outro trigger do mesmo artigo-irmão
"Communities Workflow Triggers for Posts, Comments, Requests, and Events"
([doc](https://help.gohighlevel.com/support/solutions/articles/155000008289-communities-workflow-triggers-for-posts-comments-requests-and-events))
cobre join-request-rejeitada/post/comentário/event-registration — os 4 já
existem no guia (G5-G9), nada novo ali.

### 🔍 Candidatos encontrados, NÃO aplicados (precisam de validação humana)
Integrações nativas novas encontradas nesta rodada — múltiplos sub-itens
cada, pedem confirmação humana de campos antes de virar mockup:
- **Klaviyo** — 4 gatilhos de polling (New Event, New Profile, Profile
  Added to List, Profile Added to Segment, a cada 5 min) + 17 ações
  cobrindo ciclo de vida de profile (create/update/find/subscribe/
  unsubscribe), listas, segmentos, tags e envio de campanha. Premium, OAuth.
  [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000008018-klaviyo-workflow-actions-triggers)
- **Calendly** — 5 gatilhos (bookings, cancelamento por invitee/host,
  no-show, routing-form; 4 instantâneos + 1 via polling a cada 5 min) + 9
  ações (criar reunião, booking, find/cancel event, marcar no-show,
  contact create/find/update, user lookup). Premium, OAuth.
  [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000008110-calendly-workflow-actions-triggers)
- **Cal.com** — gatilhos/ações nativos (integração irmã do Calendly).
  Campos não detalhados ainda nesta rodada.
  [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007879-cal-com-workflow-actions-triggers)
- **HubSpot** — 1 gatilho (New Contact Created) + ações (Create Contact,
  Find Contact, Create Association a Company/Deal/Ticket, entre outras).
  [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007955-hubspot-workflow-actions-trigger)

### 🔁 Atualizações nos candidatos pendentes de rodadas anteriores
Sem novo item confirmado o suficiente pra virar mockup, mas vale registrar
o que mudou desde 2026-08-24 (a pedido, checagem rápida sem re-pesquisar
do zero):
- **Linear** — agora tem doc dedicada com nomes reais dos gatilhos: **New
  Issue**, **Updated Issue**, **New Issue Comment**, **New Project** (dos
  12 gatilhos + 13 ações totais). [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007978-linear-integration-in-highlevel-workflows) —
  promovível, mas ainda faltam os ~21 itens restantes documentados.
- **Monday.com** — doc dedicada agora lista ações concretas: Create New
  Board/Group/Column/Item/Subitem, Update Item/Subitem, Archive Board/
  Group, Delete Item/Group, Get Board Items, Find Items by Column
  Value/by ID. Gatilhos aparecem como "coming soon" na própria doc — ainda
  não lançados. [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007216-monday-com-actions-and-triggers-in-workflows)
- **Jira** — doc dedicada agora existe: campo **Cloud Site** obrigatório
  em toda ação/gatilho, ações create/update/link/comment/watch/attach
  files/log work/move to sprint. [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000008219-jira-workflow-actions-and-triggers)
- **Apify** — doc dedicada agora existe: trigger **"Finished Actor Run"**
  (dispara quando um actor termina) + ação **"Run A Task"** (roda uma
  Apify task salva). [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007631-apify-actions-triggers-in-workflows)
- **Housecall Pro** — doc dedicada agora existe: 2 gatilhos concretos
  (**Job Scheduled** — novo agendamento/reagendamento; **Job Completed** —
  job marcado como concluído, ambos filtráveis por cliente/tag/técnico) +
  1 ação de criar cliente (First Name/Last Name obrigatórios; Email/
  Company/Mobile Number/Home Number opcionais). Auth via API key própria.
  [Changelog](https://ideas.gohighlevel.com/changelog/housecall-pro-workflow-action-triggers)
- **Badge Issued** — sem atualização; segue sem artigo dedicado com campos
  exatos de filtro.
- **Browse AI, OpenRouter, Manus** — sem atualização encontrada nesta
  rodada (docs seguem as mesmas de fevereiro/julho de 2026).

Nenhum desses foi promovido a mockup nesta rodada — mesmo os que ganharam
doc dedicada com campos mais concretos (Housecall Pro, Apify) ainda somam
múltiplos sub-itens e pedem confirmação humana antes da montagem com
fidelidade real, seguindo a mesma régua das rodadas anteriores.

### 🧐 Verificado e descartado (fora de escopo do guia)
- **"Trigger Automation in Bulk for Companies & Custom Objects"**
  (changelog 26/08/2026) — é um recurso de disparo manual em massa a
  partir da list view (seleciona vários registros de Company/Custom
  Object e roda um workflow já existente neles), não um novo node de
  trigger/action dentro do Workflow Builder. Não se aplica ao inventário
  deste guia. [Changelog](https://ideas.gohighlevel.com/changelog/trigger-automation-in-bulk-for-companies-custom-objects)
- **Python no Custom Code**, **Sender domain dropdown** (Workflow
  Settings) e **criação de Certificado via prompt de IA** — são melhorias
  a features/telas já existentes (Custom Code Action, configurações
  gerais de workflow, tela de criação de Certificate), não itens novos de
  trigger/action pro inventário.
- **Review Received** e **Payment Failed** — já cobertos no guia (cat02
  G16 e cat08 G... via "Payment Failed" respectivamente); nenhuma
  mudança de campo encontrada.
- **Form Partially Completed** — mencionado em blogs de terceiros como
  gatilho 2026, mas nenhum artigo oficial em `help.gohighlevel.com` com o
  nome exato/campos foi encontrado nesta rodada. Fica como candidato
  fraco — não logado como pendente formal por falta de fonte oficial
  (nem changelog, nem doc) confirmando a existência do item.

## Como agora prossegue

A auditoria automática está completa. Os próximos passos são humanos:

1. **Você abre HL** e valida os ~15 itens ⚠ dos rounds anteriores + os
   candidatos 🔍 acumulados (Browse AI, OpenRouter, Manus, Badge Issued,
   Monday.com, Jira, Linear, Housecall Pro, Apify, Klaviyo, Calendly,
   Cal.com, HubSpot) — confirmar nome real do campo / da action antes de
   qualquer um virar mockup.
2. Me diz quais aplicar
3. Eu mexo no HTML + commito

Ou: você marca o estado atual como "good enough" e segue. O conteúdo
está em ~92% de fidelidade verificada contra docs oficiais.
