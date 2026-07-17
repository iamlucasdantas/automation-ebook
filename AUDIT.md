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

## 🔍 Checagem de novidades — 2026-07-17

Rotina periódica de checagem contra o catálogo nativo do HighLevel
Workflow Builder. `WebFetch` direto em `help.gohighlevel.com` e
`ideas.gohighlevel.com` continua bloqueado (HTTP 403) neste ambiente —
mesma limitação já registrada em rodadas anteriores. Achados vêm de
`WebSearch` cruzado contra múltiplas queries independentes.

**Nenhum item novo foi adicionado ao guia nesta rodada.** Motivo: os
dois candidatos com fonte mais forte (abaixo) já tinham sido levantados
por uma sessão anterior (ver Google Drive, relatório de 2026-07-11) mas
nunca chegaram a ser mesclados na branch usada por esta sessão — e a
prática mais recente deste projeto (ver achados de 2026-07-13 no
histórico do Drive) foi propositalmente conservadora com candidatos que
não têm confirmação por captura direta da UI, depois do episódio de
ações inventadas no cat06. Mantive essa régua.

### Candidatos com fonte oficial razoável (pendente confirmação humana na UI real)
- **Gatilho "User Replied"** (cat02 Eventos) — dispara quando um
  USUÁRIO HighLevel (não o contato) responde numa conversa. Contraparte
  de "Customer Replied" (g4). Fonte:
  https://ideas.gohighlevel.com/changelog/workflow-trigger-user-replied
- **Ação "Find Opportunity"** (cat07 Oportunidades) — busca a
  oportunidade mais antiga/recente vinculada ao contato. Fonte:
  https://help.gohighlevel.com/support/solutions/articles/155000004751-workflow-action-find-opportunity
- **Ação "Remove Owner from Opportunity"** (cat07 Oportunidades) —
  limpa o Owner de uma oportunidade em contexto. Fonte:
  https://help.gohighlevel.com/support/solutions/articles/155000004755-workflow-action-remove-owner-from-opportunity

### Descartado (não é nativo ou não confirmado)
- Jira, Todoist, HubSpot, Asana, Basecamp, Apify, Manus, Calendly,
  Cal.com, QuickBooks Online — integrações via App Marketplace/OAuth,
  não nativas do builder (mesmo critério já usado pra excluir Slack).
- "Payment Failed" e "Form Partially Completed" como gatilhos dedicados —
  não existem como nós nativos; só aparecem em blogs de terceiros. O
  oficial trata falha de pagamento como filtro de status dentro do
  trigger "Payment Received" já existente.
- "Review Received" / "Reviews Received" — já coberto pelo gatilho
  existente `g16` (Nova Avaliação Recebida) em cat02.

### ⚠️ Achado operacional (mais importante que qualquer item de conteúdo hoje)

O histórico de relatórios no Google Drive mostra rodadas quase diárias
desde 2026-07-05 (05, 08, 09, 10, 11, 12, 13, 16/07) descrevendo
pesquisa e, em vários casos, commits reais de novos gatilhos/ações. Mas
tanto a branch padrão do repositório (`claude/loving-faraday-UK9eK`)
quanto este `CHANGELOG.md`/`AUDIT.md` estão parados no commit de
**2026-07-10** (`693a60a`). Ou seja: nenhuma dessas rodadas depois de
10/07 foi mesclada — cada dia a rotina parte do mesmo ponto desatualizado,
redescobre (ou não) as mesmas novidades, e o trabalho fica órfão numa
branch `claude/friendly-meitner-*` nova. Um exemplo concreto do custo
disso: a rodada de 12/07 chegou a adicionar Jira e Todoist como
"nativos"; a rodada de 13/07, pesquisando do zero por não ter visto o
commit anterior, corrigiu esse engano e os excluiu — mas como nada
tinha sido mesclado, o guia publicado nunca chegou a ficar errado (sorte,
não processo). Recomendação: decidir um fluxo pra essas branches diárias
não ficarem órfãs (sempre abrir PR e mesclar, ou consolidar numa branch
de trabalho fixa) antes de continuar rodando checagens automáticas todo
dia — do jeito atual, o trabalho não se acumula.
