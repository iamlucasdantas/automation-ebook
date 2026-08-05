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
- **Communities: Rejected Join Request / New Post / New Comment** (3
  gatilhos novos de Communities, além dos que já temos)
- **AI Translate** (ação — traduz texto dentro do workflow)
- **Update Conversation AI Bot and Status** (ação — troca o bot/status da
  conversa a partir do workflow)

### ⚠ Rename já sinalizado (não é novo, é nome desatualizado — mantido como está até confirmação)
- Nosso "AI Extract Info" → doc oficial atual é **"AI Extract Data"**
  (mesma função, possível rename).

## Como agora prossegue

A auditoria automática está completa. Os próximos passos são humanos:

1. **Você abre HL** e valida os ~15 itens ⚠ do round anterior + os 6
   candidatos 🔍 da rodada 2026-07-10 acima (confirmar nome real do
   campo / da action)
2. Me diz quais aplicar
3. Eu mexo no HTML + commito

Ou: você marca o estado atual como "good enough" e segue. O conteúdo
está em ~92% de fidelidade verificada contra docs oficiais.

## 🆕 Rodada 2026-08-05 — Checagem automática de novidades nativas

Rotina agendada comparou os 209 itens do guia (87 gatilhos + 122 ações,
já contando as adições abaixo) contra `help.gohighlevel.com` e o
changelog oficial via WebSearch (WebFetch direto pro domínio da HL
retornou 403 no ambiente — WebSearch foi usado como alternativa, mesmo
método já usado nas rodadas anteriores para os itens ✅).

### ✅ Adicionados nesta rodada (fonte oficial confirmada)
Dos 5 candidatos pendentes da rodada 2026-07-10, 2 já tinham sido
aplicados em commits avulsos (Communities: Rejected Join Request/New
Post/New Comment em `693a60a`; Update Conversation AI Bot and Status em
`86099b3`). Os 3 restantes foram confirmados e aplicados agora:

1. **Gatilho — Upload de Arquivo no Portal (Client Portal File Uploaded)**
   · cat06 G13. Dispara quando o contato sobe um arquivo pela experiência
   de Documentos Compartilhados do Client Portal. Sem filtros nativos.
   Vídeo (.mp4/.mov/.avi/.mkv/.wmv) não é suportado no upload.
   [Changelog oficial](https://ideas.gohighlevel.com/changelog/workflow-trigger-for-file-uploads-via-client-portal) ·
   [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000008172-upload-documents-through-the-client-portal)
2. **Ação — AI Decision Maker** · cat05 A8. Ação Premium: roteia o
   contato entre caminhos do workflow a partir de uma instrução em
   linguagem natural, alternativa ao If/Else manual com múltiplas
   condições. Cobrança por execução.
   [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000005649-workflow-action-ai-decision-maker)
3. **Ação — AI Translate** · cat05 A9. Traduz texto (Static Value ou
   Custom Variable) de um idioma pra outro; resultado fica disponível
   como variável customizada pras próximas ações do workflow.
   [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000005892-workflow-action-ai-translate)

Totais atualizados: **87 gatilhos + 122 ações = 209 entries** — homepage,
`search-index.json` e `AUDIT-TABLE.md` regenerados.

### 🐛 Drift corrigido nesta rodada (não era novidade do HL, era bug nosso)
- `index.html`: tab-counts e section-labels ainda diziam 84/117 enquanto
  os hero-stats já diziam 86/120 (drift de commits anteriores que só
  atualizaram um dos dois lugares).
- `guia-highlevel-cat06.html`: hero-desc/hero-stat diziam "10 gatilhos"
  quando já existiam 12 blocos reais (g1-g12) na página.
- `acoes-highlevel-cat05.html`: side-section-label dizia "5 ações" e o
  hero-stat dizia "6" quando já existiam 7 blocos reais (a1-a7).

### 🔎 Verificado e já coberto (não é novidade)
Itens que apareceram em buscas por "novos gatilhos/ações HighLevel 2026"
mas já existem no guia — confirmado antes de considerar adicionar:
- **Review Received** → já é o nosso "Nova Avaliação Recebida" (cat02 G16).
- **Community Group Member Leaderboard Level Changed** → já é "Mudança de
  Nível na Classificação" (cat11 G5) + ação "Atribuir Nível na
  Classificação" (cat13 A5).
- **Payment Failed** → não existe como gatilho nativo dedicado; é uma
  opção de filtro (Event Type) dentro do gatilho **Subscription**, que já
  cobrimos. Não foi adicionado como item novo pra evitar duplicidade.
- **Form Partially Completed** → não encontrada nenhuma doc oficial da HL
  confirmando esse gatilho; provavelmente confusão com "Opt-In" do Order
  Form Submission (que já cobrimos). Não aplicado — sem fonte oficial.

### ⚠ Ainda pendente (sem mudança nesta rodada)
- Nosso "AI Extract Info" → doc oficial atual é **"AI Extract Data"**
  (mesma função, possível rename) — segue precisando de confirmação
  humana antes de renomear, como já sinalizado na rodada anterior.
- Os ~15 itens ⚠ de discrepância cat02/cat05/cat07/cat12 do primeiro
  round de auditoria seguem sem validação humana contra a UI real.

### Nota de acesso
`WebFetch` para `help.gohighlevel.com` e outros domínios retornou 403 em
todas as tentativas nesta rodada (incl. um teste de controle contra
`en.wikipedia.org`, também 403) — parece ser uma limitação do proxy do
ambiente, não do domínio da HL especificamente. `WebSearch` funcionou
normalmente e foi a única fonte usada pra confirmar os itens acima.
