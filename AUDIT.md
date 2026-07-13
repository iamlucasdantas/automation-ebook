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

## Como agora prossegue

A auditoria automática está completa. Os próximos passos são humanos:

1. **Você abre HL** e valida os ~15 itens ⚠ acima (confirmar nome real do
   campo / da action)
2. Me diz quais aplicar
3. Eu mexo no HTML + commito

Ou: você marca o estado atual como "good enough" e segue. O conteúdo
está em ~92% de fidelidade verificada contra docs oficiais.

## 🔎 2026-07-13 — Varredura por novos gatilhos/ações nativos (pendente de verificação)

Rodada de pesquisa (4 agentes em paralelo, WebSearch apenas — **todo fetch
direto às páginas retornou 403**, inclusive help.gohighlevel.com,
ideas.gohighlevel.com e até web.archive.org como fallback. Os achados
abaixo vêm de snippets indexados pelo Google, não do corpo real da
página. Títulos de artigo são confiáveis; a descrição é paráfrase).

Nenhum item abaixo foi adicionado ao guia ainda — build de mockup fiel à
UI real exige confirmar campo-a-campo, e este projeto já levou correções
por causa de action "inventada" (ver histórico do Cat06). Precisa de
alguém abrir o HL real e confirmar antes de eu montar o painel.

### Candidatos com confiança média/alta (prováveis novos nativos)

- **Gatilho "Conversation AI Trigger"** — distinto das ações Conversation AI
  Email/SMS que já temos. Dispara a partir de um evento configurado dentro
  da Conversation AI.
- **Gatilho "Custom Trigger"** — gatilho de evento customizado/genérico,
  pra casos que não se encaixam nos triggers padrão.
- **Gatilho "Company Created"** — help.gohighlevel.com/.../155000006609-workflow-trigger-company-created.
  Parte da leva de "Company-based workflows".
- **Gatilho "Company Changed"** (par do Company Created, confiança menor —
  não achei artigo dedicado, só menção agregada).
- **Gatilho "Object Changed" / Custom Object Updated** — help.gohighlevel.com
  article 155000006701 (Custom Object and Company-based Workflow Actions
  & Triggers). Confirma via 2 agentes independentes.
- **Gatilho "Custom Object Created"** — confiança média, sem artigo com
  título exato confirmado.
- ⚠ **"Custom Object Deleted"** — 1 fonte mencionou, buscas de acompanhamento
  não confirmaram. Provável alucinação de resumo de busca — **não usar**
  sem confirmação humana.
- **Ação "Text Formatter"** — Trim / Replace Text / Find / Length / Split.
- **Ação "Custom Code"** (+ variante com IA) — execução de JavaScript
  (`inputData.<key>` → retorna JSON).
- **Ação "Drip"** — envio em lote com rate-limit configurável (tamanho de
  lote + intervalo), distinto do "Wait" que já temos.
- **Ação "Array Functions" (Premium)** — Find / Filter / Find by Index /
  Line Items / Math sobre arrays.
- **Ações de Objetos Customizados** (todas com artigo dedicado, confiança
  alta segundo os agentes — mas nenhuma verificada por fetch direto):
  - Create an Associated Record for Contact (155000004586)
  - Update an Associated Record for Contact (155000004588)
  - Clear Fields of Associated Record for Contact (155000004589)
  - Find Object Record & Find Company (155000006483)
  - Add Associated Records to Workflow (155000006486)
  - Remove Associated Records from Workflow (155000006485)
  - Não existe "Delete Custom Object Record" nativa — só limpar campos.
- **Ação "Grant Community Group Leaderboard Points"** — distinta da nossa
  já existente "Assign Leaderboard Level" (cat13 A?). Uma parece setar o
  nível diretamente, a outra concede pontos que acumulam pro nível. Achado
  via help.gohighlevel.com article 155000004080 (Gamification/Leaderboard
  triggers and actions for Community groups).

### Descartado — não é nativo ou não está em produção (NÃO adicionar)

- **Jira, Todoist, HubSpot, Mistral AI, Asana, Monday.com, Basecamp** —
  são apps do App Marketplace instalados via OAuth. Aparecem no painel
  "All Actions" do builder "como se fossem nativos" depois de instalados,
  mas não são — mesmo motivo pelo qual excluímos Slack (ver
  scripts/auto-refine.py). Fora de escopo pra este guia.
- **RCS Messaging in Workflows** — private beta, GA só previsto pro fim do
  Q3 2026. Não documentar até virar GA.
- **Advanced Builder** (canvas visual redesenhado) — mudança de UI do
  builder, não é um trigger/action novo.
- Upgrades da action "Workflow AI" existente (structured output, variável
  em runtime, test-mode) — é evolução de uma action que já documentamos,
  não uma nova.
- 4 "novos" triggers de Comunidades relatados por um agente batem com os
  que JÁ adicionamos em 2026-07-10 (cat11 G6-G9) — falso positivo, os
  agentes não sabiam que já tínhamos coberto.

### Próximo passo

Alguém confirma no HL real (ou builder sandbox) os itens da primeira
lista — nome exato do campo, categoria certa, se realmente é "nativo"
(não precisa instalar nenhum app externo). Confirmado isso, dá pra criar
categorias novas (provavelmente "Objetos Customizados/Empresas" nos
gatilhos e ações, e um item novo em "Lógica/Workflow" pra Text
Formatter/Custom Code/Drip/Array Functions) com mockup completo.
