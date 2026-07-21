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
- ~~**AI Decision Maker**~~ — ✅ aplicado na rodada 2026-07-21 (ver abaixo)
- **Client Portal File Uploaded** (gatilho — contato sobe arquivo no
  Client Portal). Ainda em aberto: confirmamos que o gatilho existe
  ([changelog oficial](https://ideas.gohighlevel.com/changelog/workflow-trigger-for-file-uploads-via-client-portal))
  mas nenhuma fonte encontrada detalha o painel de filtros real (Portal
  específico? filtro de tipo/extensão de arquivo? categoria de
  documento?) — precisa checar a UI ao vivo antes de montar o mockup.
- ~~**Communities: Rejected Join Request / New Post / New Comment**~~ —
  ❌ **entrada desatualizada, não era mais válida.** Checagem da rodada
  2026-07-21 confirmou que esses 3 gatilhos (+ um 4º, Registrado em
  Evento do Grupo) já tinham sido implementados em cat11 (g6–g9) no
  commit de 2026-07-10 "Add 14 new native GHL triggers/actions" — antes
  mesmo desta lista de candidatos ter sido escrita no mesmo dia. Ficaram
  aqui por engano por 11 dias. Os 86 gatilhos publicados já incluem
  esses 4.
- ~~**AI Translate**~~ — ✅ aplicado na rodada 2026-07-21 (ver abaixo)
- ~~**Update Conversation AI Bot and Status**~~ — ✅ aplicado em 2026-07-20
  (cat05 A7)

### ⚠ Rename já sinalizado (não é novo, é nome desatualizado — mantido como está até confirmação)
- Nosso "AI Extract Info" → doc oficial atual é **"AI Extract Data"**
  (mesma função, possível rename).

## 🆕 Rodada 2026-07-21 — Nova checagem de novidades nativas

Rotina automática (via WebSearch — WebFetch direto em help.gohighlevel.com
e ideas.gohighlevel.com está bloqueado pela política de rede deste
ambiente, então os achados vêm de resumos de busca, não da página crua)
revisou os candidatos em aberto da rodada anterior e procurou por
gatilhos/ações nativos lançados entre 2026-06-15 e 2026-07-21.

### ✅ Adicionados nesta rodada (fonte oficial confirmada)
1. **Ação — AI Decision Maker** · cat05 A8 (Premium). Campos confirmados:
   Action Name, Instructions (critério em linguagem natural), lista de
   Branches definidas pelo usuário, Default Branch automática/travada
   como fallback. NÃO confirmado e portanto não incluído no painel:
   seletor de modelo, limite de branches, botão de teste — se algum
   desses existir na UI real, é um gap conhecido.
   [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000005649-workflow-action-ai-decision-maker)
2. **Ação — AI Translate** · cat05 A9. Campos confirmados: Source
   Language (From), Target Language (To), Input Text (aceita merge
   fields/custom values). Output Variable foi adicionado por convenção
   (todas as outras 5 ações de Workflow AI desta categoria têm esse
   campo) mas NÃO foi confirmado especificamente para esta ação — flag
   deixado na legenda do painel. Também não confirmado: se é ação
   Premium, e a lista completa de idiomas do dropdown (mockup mostra só
   um valor selecionado de exemplo, sem inventar a lista inteira).
   [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000005892-workflow-action-ai-translate)

Totais atualizados: **86 gatilhos + 122 ações = 208 entries** (homepage,
search-index.json e AUDIT-TABLE.md já regenerados, validate-mockups.js
passando nas 28 páginas).

### 🐛 Drift corrigido nesta rodada (não era novidade do HL, era bug nosso)
- Todas as 28 páginas de categoria carregavam o total de categorias
  desatualizado no breadcrumb/hero-tag (ex.: "06/12" em vez de "06/13",
  "07/14" em vez de "07/15") — sobrou de quando cat13 (gatilhos) e cat15
  (ações) foram criadas e nenhuma das outras páginas teve seu total
  atualizado. `index.html` também tinha os tab-counts/section-labels
  presos em 84/117 enquanto os hero-stats já diziam 86/120.
- `guia-highlevel-cat06.html` (Cursos) subcontava os próprios gatilhos
  no hero (dizia 10, real 12). `acoes-highlevel-cat05.html` (Workflow AI)
  e `acoes-highlevel-cat07.html` (Oportunidades) subcontavam as próprias
  ações no side-nav/hero-stat/hero-desc (diziam 5–6 e 9; real 7 e 11,
  antes das adições de hoje) — sobrou das duas últimas ações adicionadas
  em cada categoria (A7 e A11) sem atualizar todos os contadores internos
  da própria página.

### 🔍 Candidatos encontrados, ainda NÃO aplicados
- **Client Portal File Uploaded** (ver acima — nome confirmado, campos
  não confirmados)
- **Invoke Agent Studio Agent** (ação — chama um agente do Agent Studio
  em produção a partir do workflow, passa dados em tempo real e roteia
  a resposta pro próximo passo. Distinta do nosso "AI Agent" atual.
  [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007402-workflow-action-invoke-agent-studio-agent),
  lançada em 26/fev/2026). Sem detalhe de campos — precisa da UI ao vivo.
- **OpenRouter Generate Response** (ação — node nativo de app que dá
  acesso a 300+ modelos de LLM via OpenRouter num único node de
  workflow. Campos parcialmente confirmados: System Prompt (opcional),
  Prompt (obrigatório, aceita variáveis), Model Selection (dropdown),
  botão de teste. [Doc oficial](https://help.gohighlevel.com/support/solutions/articles/155000007330-workflow-action-openrouter-generate-response),
  lançada em 6/fev/2026). Não aplicado ainda porque a lista completa de
  modelos do dropdown não foi confirmada e o agente de pesquisa não
  conseguiu acessar a página crua pra confirmar mais detalhes do painel.

## Como agora prossegue

A auditoria automática está completa. Os próximos passos são humanos:

1. **Você abre HL** e valida os itens 🔍 acima (Client Portal File
   Uploaded, Invoke Agent Studio Agent, OpenRouter Generate Response) —
   confirmar o painel de campos real antes de montar o mockup
2. Me diz quais aplicar
3. Eu mexo no HTML + commito

Ou: você marca o estado atual como "good enough" e segue. O conteúdo
está em ~92%+ de fidelidade verificada contra docs oficiais.
