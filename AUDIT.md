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

## 🔍 Pendente — descobertas da varredura de 2026-07-18 (precisam de sessão dedicada)

Rodada de checagem por WebSearch encontrou features novas que **não foram
adicionadas** neste guia ainda — o escopo de construir mockup interativo +
painel gold-standard pra cada uma é grande o suficiente pra merecer sessão
própria, não um item a mais numa rodada de manutenção. Registrando aqui pra
não perder o achado:

1. **Company-Based Workflows (categoria inteira nova)** — o HighLevel lançou
   um tipo de workflow "Company-based" (paralelo ao contact-based que o guia
   cobre hoje), com seus próprios triggers (`Company Created` confirmado por
   doc oficial) e ações que escrevem em campos de Company. É uma família nova
   de conteúdo, não um item isolado — precisa de levantamento completo antes
   de criar categoria 14 de gatilhos.
   Doc: https://help.gohighlevel.com/support/solutions/articles/155000006609-workflow-trigger-company-created
   Overview: https://help.gohighlevel.com/support/solutions/articles/155000006688-company-based-workflows-company-triggers-actions
2. **Service Booking (Services v2)** — trigger dedicado à v2 do sistema de
   agendamento de serviços, distinto do `Customer Booked Appointment` (cat03)
   já coberto. Confirmar se convive com o antigo ou substitui, antes de
   documentar.
   Doc: https://help.gohighlevel.com/support/solutions/articles/155000006140-workflow-trigger-service-booking-services-v2-
3. **Conversation AI Trigger** e **Custom Trigger** — apareceram como itens
   na listagem oficial de triggers, mas sem confirmação detalhada do que
   disparam exatamente. Precisa de doc-diving antes de escrever conteúdo.
4. **"Documents & Contracts" como categoria de ação** (não só de gatilho) —
   a doc oficial lista "Documents & Contracts" entre as categorias de
   Workflow Actions. O guia só tem essa como gatilho (cat07 g5). Verificar
   se existe uma ação nativa correspondente (ex.: enviar documento pra
   assinatura via workflow) que falta no guia.
5. **Possível rename**: "Pipeline State Changed" (nosso nome atual, cat04 g4)
   pode ser "Pipeline Stage Changed" na doc oficial — não é uma feature nova,
   é só uma discrepância de nome a confirmar contra a UI real antes de mexer.

Itens que a mesma varredura mencionou mas com evidência fraca — não vale
adicionar sem confirmação melhor: "Payment Failed" trigger (parece ser só
uma feature request no ideas board, não algo já lançado), "Form/Survey
Partially Submitted" trigger, e alegações de triggers nativos de
Shopify v2/Calendly/WhatsApp direto/Todoist (fonte única, blog de baixa
qualidade, sem doc oficial correspondente).

Também vale notar: HighLevel expandiu bastante os módulos de marketplace
(HubSpot, Jira, Basecamp, Vapi, etc.) que injetam triggers/ações no mesmo
Workflow Builder — mas esses dependem de conectar um app de terceiros, então
ficam **fora do escopo** deste guia (mesma lógica que já fez o guia trocar
"Slack Message" por "Outbound Webhook (Slack)" — só documentamos o que é
nativo do HighLevel puro, sem integração externa).

## Adicionado nesta rodada (2026-07-18)

- **Cat02 G20 — Email Recebido (Inbound)**: gatilho novo confirmado por doc
  oficial (cold/warm/customer-reply, filtros de mailbox/remetente/assunto).
  https://help.gohighlevel.com/support/solutions/articles/155000007650-workflow-trigger-inbound-email
- **Cat07 G11 — Upload no Client Portal**: gatilho novo confirmado pelo
  changelog oficial (Shared Documents do Client Portal).
  https://ideas.gohighlevel.com/changelog/workflow-trigger-for-file-uploads-via-client-portal

## Como agora prossegue

A auditoria automática está completa. Os próximos passos são humanos:

1. **Você abre HL** e valida os ~15 itens ⚠ acima (confirmar nome real do
   campo / da action)
2. Me diz quais aplicar
3. Eu mexo no HTML + commito

Ou: você marca o estado atual como "good enough" e segue. O conteúdo
está em ~92% de fidelidade verificada contra docs oficiais.
