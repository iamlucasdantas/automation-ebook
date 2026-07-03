# AUDIT — Conferência contra a UI real do HighLevel

Auditoria contra `help.gohighlevel.com`. Aqui ficam os achados acionáveis.
Tabela completa de status por entry em [AUDIT-TABLE.md](./AUDIT-TABLE.md).

## 🆕 Gap check 2026-07-03 — triggers/ações nativos que o guia AINDA NÃO cobre

Rodada de pesquisa (WebSearch, sem acesso de página completa a
`help.gohighlevel.com` neste ambiente — só snippets) pra achar o que o HL
lançou de nativo desde a última auditoria (jun/2026) e que os 76
gatilhos + 110 ações atuais não cobrem. **Nada foi adicionado ao guia
ainda** — os itens abaixo precisam de alguém abrindo o HL real (ou pelo
menos a página completa do artigo) pra confirmar nome exato e campos do
painel antes de virar mockup, porque o guia inteiro é vendido em cima de
"fidelidade total à interface real" e eu não consigo validar isso sem
acesso à página.

### Confiança alta (nome + artigo oficial datado de 2026, claramente novo)

**Ações**
- **AI Agent** — ação autônoma multi-step: você descreve o objetivo em
  linguagem natural, dá até 10 tools, ela planeja/decide/executa.
  Premium, cobrada por execução. Diferente das AI actions que já
  temos (Summarize/Intent Detection/Content Generation).
  https://help.gohighlevel.com/support/solutions/articles/155000007600-workflow-action-ai-agent
- **Invoke Agent Studio Agent** — chama um agente conversacional do
  Agent Studio de dentro do workflow, usa a resposta dele nos passos
  seguintes.
  https://help.gohighlevel.com/support/solutions/articles/155000007402-workflow-action-invoke-agent-studio-agent
- **AI Extract Data** — extrai variáveis tipadas (texto/email/telefone/
  número/data) de texto não-estruturado via schema definido.
  https://help.gohighlevel.com/support/solutions/articles/155000007992-workflow-action-ai-extract-data
- **Custom Object actions** (família nova inteira) — Create/Update/
  Clear Custom Object Record, Find Object Record/Find Company, e ações
  cross-object (add/remove/find Contact/Company/Custom Object
  relacionado por Association Label). Lançado como parte de "Custom
  Objects are Live in Workflows", 27/mai/2026.
  https://help.gohighlevel.com/support/solutions/articles/155000004389-using-custom-objects-in-workflow-actions-and-triggers
  https://help.gohighlevel.com/support/solutions/articles/155000006701-custom-object-and-company-based-workflow-actions-triggers
  https://help.gohighlevel.com/support/solutions/articles/155000006483-workflow-action-find-object-record-find-company

**Gatilhos**
- **Inbound Email** — dispara em qualquer email recebido, inclusive de
  remetente que ainda não é contato no CRM (diferente de "Customer
  Replied", que só pega resposta a algo que você mandou).
  https://help.gohighlevel.com/support/solutions/articles/155000007650-workflow-trigger-inbound-email
- **Custom Object Created / Updated / Deleted** — mesmo lançamento de
  27/mai/2026 acima.
- **Product Review Submitted** (E-commerce Stores) — dispara quando
  cliente avalia produto na loja HL; carrega rating/título/comentário/
  produto com filtros.
  https://help.gohighlevel.com/support/solutions/articles/155000007386-workflow-trigger-product-review-submitted-for-e-commerce-stores-
- **Proposals and Estimates** — ciclo de vida de documento (Sent/
  Viewed/Signed/Completed) com filtros de Template/Recipient Type/Value.
  https://help.gohighlevel.com/support/solutions/articles/155000001491-proposals-and-estimates-trigger-inside-workflows

### Confiança média — pode já estar coberto de forma implícita, ou data incerta

- **Workflow Scheduler Trigger** (cron/intervalo — hourly/daily/weekly/
  monthly/one-off/advanced cron, sem contato associado). Artigo mostra
  "last updated November 5, 2025" — pode já ser anterior à nossa
  auditoria de jun/2026 e simplesmente não ter entrado na lista.
  https://help.gohighlevel.com/support/solutions/articles/155000006653-workflow-trigger-scheduler
- **Review Received** (Google/Facebook, contactless) e **New Affiliate
  Sale(s)** — artigos reais existem, mas provavelmente já caem dentro
  dos nossos buckets genéricos de "Campaign events"/"Affiliate events".
- **Send Live Chat Message** / filtro Live Chat em Customer Replied —
  real, mas talvez já coberto pela família genérica de "enviar
  mensagem".

### Checado e NÃO confirmado — não adicionar

- **"Payment Failed" trigger** e **"Form Partially Completed" trigger**
  só aparecem em blogs terceiros (rsla.io, softomatesolutions.com), não
  em help.gohighlevel.com nem ideas.gohighlevel.com. Achamos inclusive
  um *feature request* aberto ("Partial Survey Submission Workflow
  Trigger") sugerindo que isso **ainda não existe** — contradiz o blog.
- **"Membership access expiry" trigger** — não achamos como trigger
  dedicado; provavelmente já coberto pelo filtro "Expired" do trigger
  de Subscription que já temos.

### Fora de escopo (não é nativo)

Slack, Google Sheets, Asana, Basecamp, Airtable, Apify, Browse AI,
Mistral AI, Fathom, Cal.com, Housecall Pro apareceram nos changelogs
como integrações de Marketplace/Premium App — não contam como "nativo"
pro critério deste guia.

### Próximo passo

Alguém confirma direto no HL (ou abre a página completa do artigo, já
que este ambiente não tem acesso de fetch a `help.gohighlevel.com`) os
campos reais do painel de cada item de confiança alta acima. Aí dá pra
escrever os mockups no padrão gold-standard do guia (ver commit
`2aa70e2` como referência de como um "ação nova" é adicionada). Sem
isso, adicionar agora seria inventar campos — o oposto do que este
guia se propõe a ser.

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
| **Ações cat06** (Appointments) | ✅ | 3 | 2 (A2 sem doc) |
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
- **Cat06 A2 Reassign Appointment** — sem doc dedicada
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
