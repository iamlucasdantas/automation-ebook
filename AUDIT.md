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

## 🆕 Rodada 2026-08-23 — Checagem de novidades nativas

Rotina automática comparou o guia contra `help.gohighlevel.com` e
`ideas.gohighlevel.com/changelog` em busca de itens nativos lançados desde a
rodada de 2026-08-10. `WebFetch` ficou bloqueado pela política de rede desta
sessão (egress proxy recusou até domínios não relacionados) — a confirmação
abaixo veio só de `WebSearch` (múltiplas queries independentes por item,
convergindo pro mesmo conteúdo), no mesmo padrão "✅ Confirmado por
WebSearch" já usado nas rodadas anteriores.

### ✅ Adicionados nesta rodada (fonte oficial confirmada)
1. **Gatilho — Solicitação de Entrada no Grupo (Requested to Join Group)**
   · `guia-highlevel-cat11.html` G10. Dispara na submissão do pedido de
   entrada — antes de aprovar/rejeitar (diferente do já existente G07
   "Solicitação de Entrada Rejeitada"). Filtro Group + Membership Question
   Responses dinâmico por pergunta de admissão do grupo. [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000008439-automate-group-join-requests-with-workflows)
2. **Gatilho — Badge Emitido (Badge Issued)** · `guia-highlevel-cat11.html`
   G11. Dispara quando um badge é emitido pra um membro. Uma ação dedicada
   "Issue Badge" ainda não existe (changelog oficial diz "coming soon") —
   só o gatilho foi adicionado, badges continuam emitidos manualmente ou
   via Issue Certificate. [Changelog oficial](https://ideas.gohighlevel.com/changelog/badge-automation-is-now-available-in-workflows)
3. **Gatilho — Browse AI: Tarefa Concluída (New Completed Task)** ·
   `guia-highlevel-cat02.html` G23. Webhook-backed, dispara quando um robot
   do Browse AI termina uma tarefa. Filtros Robot (obrigatório) + Select
   Operator (condicional). Premium, requer API key própria do Browse AI.
   [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000008028-browse-ai-workflow-actions-and-trigger)
4. **Ação — OpenRouter: Gerar Resposta (Generate Response)** ·
   `acoes-highlevel-cat05.html` A11. Gateway unificado pra 300+ modelos
   (Claude, GPT, Gemini, Perplexity...) — troca de modelo sem trocar de
   ação, diferente do Mistral AI (A08) que só fala com a Mistral. Requer
   API key própria do OpenRouter. [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007330-workflow-action-openrouter-generate-response)
5. **Ações — Browse AI (4 ações)** · `acoes-highlevel-cat05.html` A12-A15:
   Executar Tarefa (Run Task), Executar Tarefas em Lote (Bulk Run Tasks),
   Buscar Tarefa (Get Task), Buscar Execução em Lote (Get Bulk Run). Item
   já estava na lista de candidatos pendentes desde 2026-07-29 — confirmado
   nesta rodada com detalhe de campos o suficiente pra montar com
   fidelidade. Todas Premium, API key própria do Browse AI. [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000008028-browse-ai-workflow-actions-and-trigger)

Totais atualizados: **90 gatilhos + 180 ações = 270 entries** (`index.html`,
`search-index.json` e `AUDIT-TABLE.md` já regenerados via
`scripts/build-search-index.py` e `scripts/build-audit.py`).

### 🐛 Drift corrigido nesta rodada (não era novidade do HL, era bug nosso)
- `acoes-highlevel-cat05.html`: hero-stat-num da própria página dizia "8
  ações" enquanto o arquivo já tinha 10 blocos reais (A1-A10) antes desta
  rodada — corrigido pro número real antes de somar as 5 novas.
- `guia-highlevel-cat02.html` G22 e `guia-highlevel-cat11.html`: mesma
  classe de bug (hero-stat-num desatualizado na própria página, mesmo com
  `index.html` e o total geral corretos) não encontrada nesses dois, mas
  vale checar as demais 15 páginas de ação na próxima rodada — o padrão se
  repetiu em pelo menos uma página por rodada nas últimas 3 auditorias.
- `python3 scripts/auto-refine.py --check` sinalizou drift mecânico
  pré-existente (não relacionado a esta rodada) em
  `acoes-highlevel-cat15.html` e `guia-highlevel-cat13.html` — corrigido
  rodando `auto-refine.py` (idempotente).
- `index.html`: conferi cada card de categoria contra a contagem real de
  blocos (`id="aN"`/`id="gN"`) em cada página e achei **8 categorias de
  ações desatualizadas havia pelo menos uma rodada** — provavelmente
  esquecidas na correção de contadores do fechamento de gap de 2026-08-10:
  Contatos 16→18, Comunicação 29→37 (a maior — tinha 8 ações a mais no
  arquivo do que o card mostrava), Ferramentas Internas 21→22,
  Agendamentos 3→4, Oportunidades 11→13, Pagamentos 5→9, Marketing 5→8,
  Comunidades 6→8. Todos os 13 cards de gatilhos já batiam. Corrigido —
  a soma dos cards agora bate exatamente com o total geral (90/180).

### 🔍 Candidatos encontrados, NÃO aplicados (precisam de outra rodada)
- **Manus** — forma confirmada (2 vias: ~5 ações de workflow pra
  Create/Update/Continue/Fetch/Delete de uma task Manus + triggers no lado
  do Manus quando a task é criada via ação de workflow — não dispara pra
  tasks criadas direto no app Manus), mas o texto exato dos botões/nome dos
  5 campos de ação ainda diverge entre fontes. Precisa de uma passada com
  acesso direto à doc antes de montar mockup com fidelidade real.
  [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007351-manus-actions-triggers-in-workflows)

### ⚠ Drift de conteúdo encontrado, NÃO corrigido (precisa validação humana)
- `acoes-highlevel-cat05.html` A3 e A5: CHANGELOG de 2026-08-10 registra os
  renames "Summarize Conversation → AI Summarize" e "AI Classify → AI
  Intent Detection" como aplicados, mas o HTML real da categoria ainda usa
  os nomes antigos (H2 "Summarize Conversation" / "Classify"). Ou o
  CHANGELOG documentou algo que não foi commitado, ou uma reversão
  aconteceu depois. Não mexi nos nomes nesta rodada — fica pra confirmação
  humana antes de tocar (rename muda como o usuário busca a ação no guia).

## Como agora prossegue

A auditoria automática está completa. Os próximos passos são humanos:

1. **Você abre HL** e valida os ~15 itens ⚠ do round anterior + os 6
   candidatos 🔍 da rodada 2026-07-10 acima (confirmar nome real do
   campo / da action)
2. Me diz quais aplicar
3. Eu mexo no HTML + commito

Ou: você marca o estado atual como "good enough" e segue. O conteúdo
está em ~92% de fidelidade verificada contra docs oficiais.
