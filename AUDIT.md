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

## 🆕 Rodada 2026-08-07 — Checagem de novidades nativas

Rotina automática comparou os 209 (86 gatilhos + 120 ações, estado antes desta
rodada) itens do guia contra o changelog oficial do HighLevel
(`ideas.gohighlevel.com/changelog`) e `help.gohighlevel.com` em busca de
gatilhos/ações nativos lançados recentemente e não cobertos ainda. Acesso
direto (WebFetch) a `ideas.gohighlevel.com` e `help.gohighlevel.com` está
bloqueado pelo proxy de rede deste ambiente — a checagem usou WebSearch
(resultados indexados) como fonte.

### ✅ Adicionados nesta rodada (fonte oficial confirmada via WebSearch)
1. **Gatilho — Upload de Arquivo no Client Portal (Client Portal File
   Uploaded)** · cat07 G11. Dispara quando um contato sobe um documento pela
   experiência de Shared Documents do Client Portal. Nenhum filtro
   documentado oficialmente — dispara em qualquer upload.
   [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000008172-upload-documents-through-the-client-portal) ·
   [Changelog oficial](https://ideas.gohighlevel.com/changelog/workflow-trigger-for-file-uploads-via-client-portal)
2. **Ação — AI Decision Maker** · cat05 (Workflow AI) A8. Roteamento de
   contatos por ramificações do workflow usando instruções em linguagem
   natural em vez de If/Else manual. Default Branch obrigatório e travado.
   Ação Premium (cobrança por execução).
   [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000005649-workflow-action-ai-decision-maker)
3. **Ação — AI Translate** · cat05 (Workflow AI) A9. Traduz texto de um
   idioma pra outro dentro do workflow — Source Language, Target Language,
   Input Text (Static Value ou Custom Variable), saída como variável
   customizada.
   [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000005892-workflow-action-ai-translate)

Estes 3 itens já estavam listados como "candidatos pendentes" nas rodadas
2026-07-10/2026-07-20 (junto com AI Decision Maker/AI Translate/Client
Portal File Uploaded). Confirmado que **Communities: Rejected Join
Request/New Post/New Comment** e **Update Conversation AI Bot and Status**
— os outros candidatos da mesma lista — já tinham sido aplicados nas rodadas
seguintes (commits `693a60a` e `86099b3`). "Form Partially Completed" foi
pesquisado (apareceu numa busca de terceiros sobre triggers 2026) mas não
foi possível confirmar via fonte oficial HighLevel — **não aplicado**, fica
como candidato de baixa confiança.

Totais atualizados: **87 gatilhos + 122 ações = 209 entries** (homepage,
search-index.json e AUDIT-TABLE.md regenerados). Contagem por categoria
auditada linha a linha contra o HTML real (soma bate 87 e 122).

### 🐛 Drift corrigido nesta rodada (não era novidade do HL, era bug nosso)
- Rodapés de todas as páginas de gatilhos diziam "Categoria XX de 12"
  (deveria ser de 13, já que cat13 Google Integrações existe desde
  2026-07-10) — corrigido nas 13 páginas.
- Rodapés de todas as páginas de ações diziam "Categoria XX de 14" (deveria
  ser de 15, já que cat15 Google Integrações existe desde 2026-07-10) —
  corrigido nas 15 páginas.
- `acoes-highlevel-cat05.html`: hero-desc/hero-stat diziam "7 ações" /
  contador "6" — nenhum dos dois batia com as 7 ações reais que já existiam
  (A1-A7) antes desta rodada. Corrigido pra refletir as 9 ações atuais.
- `index.html`: tab-counts diziam "13 cat · 84" / "15 cat · 117" enquanto os
  hero-stats já diziam 86/120 — mais um caso de drift entre dois contadores
  da mesma página. Corrigido.

### ⚠ Bug encontrado em `scripts/auto-refine.py` (NÃO aplicado — reportado aqui)
Rodar `auto-refine.py` nesta sessão para regenerar `search-index.json`
também tentou "regenerar" o configData de páginas fora do `HAND_CRAFTED` set
(`guia-highlevel-cat13.html`, `acoes-highlevel-cat15.html`) — mas o
resultado **removeu entradas inteiras de configData** (`g1-3`, `a4-1`,
`a6-1`) cujos nós ainda existem no DOM do mockup, e enxugou drasticamente o
conteúdo dos campos restantes. Isso quebra o click-to-expand desses nós
(painel fica vazio) e reduz a fidelidade que essas páginas já tinham.
Revertido antes de commitar — **as duas páginas não foram alteradas por
esta rodada**. Recomendo não rodar `auto-refine.py` sem revisão manual do
diff até esse bug ser corrigido, ou adicionar cat13/cat15 ao `HAND_CRAFTED`
set do script.

### 🔍 Candidatos encontrados, NÃO aplicados (precisam de mais confirmação)
- **Form Partially Completed** (gatilho) — mencionado em busca de terceiros
  sobre lançamentos 2026, sem confirmação numa fonte oficial HighLevel
  (help.gohighlevel.com ou ideas.gohighlevel.com/changelog) nesta rodada.

## Como agora prossegue

A auditoria automática está completa. Os próximos passos são humanos:

1. **Você abre HL** e valida os ~15 itens ⚠ do round anterior + os 6
   candidatos 🔍 da rodada 2026-07-10 acima (confirmar nome real do
   campo / da action)
2. Me diz quais aplicar
3. Eu mexo no HTML + commito

Ou: você marca o estado atual como "good enough" e segue. O conteúdo
está em ~92% de fidelidade verificada contra docs oficiais.
