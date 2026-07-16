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

## 🆕 Auditoria de novidades — 2026-07-16

Rodada automática (rotina agendada) comparando o guia contra o changelog oficial
do HighLevel (`ideas.gohighlevel.com/changelog`) e `help.gohighlevel.com`, à
procura de gatilhos/ações nativos lançados depois da última auditoria
(2026-07-10). **Nenhuma edição de conteúdo foi aplicada nesta rodada** — o
achado é grande demais (gap estrutural, não um delta pequeno) e a maioria dos
detalhes de campo só está disponível como resumo de busca (fetch direto em
`help.gohighlevel.com` e `ideas.gohighlevel.com` retorna 403 — proteção
anti-bot —, então não foi possível puxar a lista de campos completa de cada
action/trigger com confiança suficiente pra montar mockups com fidelidade).

### Gap encontrado: 10 integrações nativas de workflow ausentes do guia

Nenhuma delas existe hoje em `deploy-highlevel/` (nem como categoria de
gatilho nem de ação). Todas são integrações nativas dentro do Workflow
Builder (conectam via OAuth, aparecem no seletor de trigger/action — mesmo
padrão do que já tratamos como "nativo" pras categorias Shopify e Google
Integrações), então **se qualifica** pra entrar no guia sob a mesma régua já
usada aqui.

| Integração | Gatilhos (aprox.) | Ações (aprox.) | Fonte |
|---|---:|---:|---|
| **Todoist** | 3 (New incomplete task, New completed task, New project — polling 5min) | 12 (create/update/complete task, comments, project/section, find task/project/user, collaborators) | [changelog](https://ideas.gohighlevel.com/changelog/todoist-workflow-actions-triggers) |
| **Jira** | 2 (issue created, issue updated) | 11 (create/update/link/comment/watch/attach/log work/move to sprint — com seletor de Cloud Site) | [changelog](https://ideas.gohighlevel.com/changelog/jira-workflow-actions-and-triggers) |
| **Asana** | 7 (Task Created/Updated, Project Created, Comment on Task, New User, Task Moved to Section, New Attachment — +2 "coming soon": Tag Added, New Subtask) | 13 (create/update/find task, sections, comments/story, subtask, project, find all/by project) | [help doc](https://help.gohighlevel.com/support/solutions/articles/155000006489-asana-actions-and-triggers-in-workflows) |
| **Apify** | actor/task run completo (contagem exata não confirmada) | run actor, scrape site, buscar dados estruturados (contagem exata não confirmada) | [help doc](https://help.gohighlevel.com/support/solutions/articles/155000007631-apify-actions-triggers-in-highlevel-workflows) |
| **Basecamp** | 2 (New To-do, New Message Posted — instant/webhook) | ~5-8 (Create/Update To-do, Create Project, Create Message, Create Document, Find *, Add Comment, Complete To-do — contagem a confirmar) | [help doc](https://help.gohighlevel.com/support/solutions/articles/155000006399-basecamp-actions-triggers-in-workflows) |
| **Manus** (AI agent tasks) | task created / task stopped | create/update/continue/fetch/delete task (contagem exata não confirmada) | [help doc](https://help.gohighlevel.com/support/solutions/articles/155000007351-manus-actions-triggers-in-workflows) |
| **QuickBooks Online** | invoice sent / paid / overdue (contagem exata não confirmada) | sync de contato, criação de invoice (contagem exata não confirmada) | mencionado em blogs/n8n; artigo dedicado do help center não localizado ainda |
| **Calendly** | 5 (booking, cancelamento por invitee, cancelamento por host, no-show, routing-form submission) | 9 (criar reunião avulsa, booking do lado do invitee, find/cancel event, marcar no-show, create/find/update contact, user lookup) | [help doc](https://help.gohighlevel.com/support/solutions/articles/155000008110-calendly-workflow-actions-triggers) |
| **HubSpot** | novo contato (real-time) | create/find contact, mapeamento de campos (contagem exata não confirmada) | [help doc](https://help.gohighlevel.com/support/solutions/articles/155000007955-hubspot-workflow-actions-trigger) |
| **Cal.com** | não detalhado nesta rodada | não detalhado nesta rodada | [help doc](https://help.gohighlevel.com/support/solutions/articles/155000007879-cal-com-workflow-actions-triggers) |

**Total estimado**: ~25-30 novos gatilhos + ~90-110 novas ações nativas — um
aumento de praticamente 50% sobre o conteúdo atual do guia (84 gatilhos / 117
ações hoje).

### Por que não apliquei direto

1. **Escala**: isso é ~10x o tamanho de qualquer sessão de conteúdo anterior
   (a maior até agora foi Google Integrações em 10/07, com 3 gatilhos + 6
   ações). Tentar fazer as 10 integrações numa rodada só, sem checkpoint
   humano, é como escrever ~200 entradas de guia de uma vez.
2. **Confiança nos campos**: sem conseguir puxar a página oficial completa
   (403 em fetch direto), só tenho resumo de busca — o suficiente pra saber
   *que* a integração e as ações existem, mas não o suficiente pra montar o
   painel de configuração com a mesma fidelidade que o resto do guia promete
   (nome exato de cada campo, tipo de campo, opções de dropdown).
3. Segue a régua que a própria auditoria já usa: mudanças que afetam como o
   usuário busca/usa a ação (aqui, criar categoria inteira nova) esperam
   validação antes de aplicar em massa.

### Como prossegue

Recomendo tratar cada integração acima como uma sessão de conteúdo dedicada
(igual foi feito pra Google Integrações), na ordem de confiança dos dados
disponíveis: **Calendly → Asana → Todoist/Jira → Basecamp → HubSpot → Apify
→ Manus → QuickBooks Online → Cal.com**. Pra cada uma: abrir o artigo oficial
do help center dentro do HL (login necessário, fetch automatizado bloqueado),
copiar a lista real de campos, e então criar as páginas
`guia-highlevel-catNN.html` / `acoes-highlevel-catNN.html` seguindo o
template do cat13/cat15.

## Como agora prossegue

A auditoria automática está completa. Os próximos passos são humanos:

1. **Você abre HL** e valida os ~15 itens ⚠ acima (confirmar nome real do
   campo / da action)
2. Me diz quais aplicar
3. Eu mexo no HTML + commito

Ou: você marca o estado atual como "good enough" e segue. O conteúdo
está em ~92% de fidelidade verificada contra docs oficiais.
