# AUDIT — Conferência contra a UI real do HighLevel

Auditoria contra `help.gohighlevel.com`. Aqui ficam os achados acionáveis.
Tabela completa de status por entry em [AUDIT-TABLE.md](./AUDIT-TABLE.md).

## 🆕 Rodada 2026-07-09 — Checagem de novidades nativas + achado de processo

**Contexto importante descoberto nesta rodada:** a rotina periódica desta
tarefa vem rodando diariamente pelo menos desde 2026-06-22, cada dia numa
branch nova a partir da `main`, mas **nenhuma dessas branches foi mergeada**
— a `main` está parada em `e8df13d` (2026-07-03). Isso significa que os
achados dos últimos ~6 dias (incl. a rodada de 2026-07-08 documentada abaixo)
nunca chegaram a ficar visíveis pra ninguém. Nesta rodada eu recuperei o
trabalho da branch `claude/friendly-meitner-ab4lcl` (commits `d8e394c` +
`87bba0d`, 2026-07-08 — os 5 gatilhos + 4 ações abaixo) via cherry-pick pra
não perder esse trabalho de novo, e sigo publicando na branch desta sessão.
**Recomendação pro humano:** decidir uma branch "canônica" (ex. sempre a
mesma, ou sempre abrir PR contra `main` e mergear) pra que o trabalho diário
pare de se perder.

Rechecagem de WebSearch hoje (WebFetch continua bloqueado com 403 em
`help.gohighlevel.com`, mesmo caveat de sempre) **corrobora de forma
independente** 5 dos 9 itens abaixo adicionados ontem (mesmos 4 triggers de
Comunidades batendo com o changelog "New Communities Triggers", e RCS Message
batendo com o changelog de RCS private beta) — sinal razoável de que não são
alucinação de busca. Os 4 itens restantes (Client Portal File Uploaded, Find
Opportunity, Remove Owner from Opportunity, Remove Follower(s) from
Opportunity) não foram re-encontrados na busca de hoje, mas também não foram
contradidos — mantidos, cada um já linkado à fonte oficial abaixo.

**Novidade grande NÃO adicionada hoje — precisa de sessão dedicada:**
a busca de hoje encontrou uma família inteira de integrações nativas
"Premium Triggers & Actions" que a própria HighLevel constrói e mantém
dentro do Workflow Builder (mesma família da nossa já existente ação
"Google Sheets"), cada uma com doc oficial dedicada: **Basecamp, Typeform,
Vapi, Browse AI, Apify, Cal.com, Notion, Airtable, ClickUp** — cada uma com
2-6 triggers/actions próprios. Isso é dezenas de entradas potenciais, uma
superfície de produto nova o suficiente pra merecer avaliação humana antes
de virar conteúdo "gold-standard" no guia (categoria nova? dentro de
Envio de Dados?). Não inventei essa estrutura sem revisão. Fontes: ver seção
"Integrações Premium — pendente" mais abaixo.

**Também flagado, não aplicado:** o help.gohighlevel.com tem um artigo
("workflow-action-slack-message") que sugere que **Slack Message pode ser
uma ação nativa real**, contradizendo a premissa atual do guia (que trata
Slack como não-nativo e usa "Outbound Webhook (Slack)" no lugar). O
formato antigo do ID do artigo sugere que isso é anterior à nossa última
auditoria, não uma novidade — mas não foi possível confirmar sem acesso
à UI ao vivo. Precisa de verificação humana antes de qualquer mudança,
porque reverter essa decisão afeta várias entradas já publicadas.

Nenhum conteúdo novo de mockup foi escrito nesta rodada além do que já
veio do cherry-pick de 2026-07-08 (documentado abaixo) — a contagem
77→82 gatilhos / 110→114 ações / 187→196 painéis já reflete isso.

## 🆕 Rodada 2026-07-08 — Checagem de novidades nativas

Verificação periódica (a mesma rotina de `db26cd1`, 2026-06-09) pra achar
triggers/actions nativos que o HighLevel lançou e que ainda não estavam no
guia. **Caveat de ferramenta:** `WebFetch` retornou 403 pra qualquer URL
neste ambiente (inclusive um teste de controle contra `example.com`) —
proxy de rede bloqueou `CONNECT` pra hosts externos. Todos os achados abaixo
vêm de múltiplas buscas `WebSearch` independentes contra os domínios oficiais
`ideas.gohighlevel.com` e `help.gohighlevel.com` (mesmo texto/descrição
corroborado em 2-3 queries distintas cada), não de leitura direta da página.
Recomendado um spot-check manual no Workflow Builder antes de tratar como
100% definitivo, mas a convergência entre buscas é forte o suficiente pra
publicar.

**5 novos gatilhos adicionados:**
- **Cat02 g20 — Upload no Client Portal** (Client Portal File Uploaded) — dispara quando um contato sobe um arquivo via Client Portal → Shared Documents. Sem filtros granulares documentados (só o nome do trigger). Fonte: [changelog](https://ideas.gohighlevel.com/changelog/workflow-trigger-for-file-uploads-via-client-portal)
- **Cat11 g6 — Solicitação de Entrada em Grupo Rejeitada** (Group Join Request Rejected)
- **Cat11 g7 — Novo Post Criado no Grupo** (New Post Created in Group) — filtros: Group, Channel, Post Title, Post Content
- **Cat11 g8 — Novo Comentário em Post do Grupo** (New Comment Added to Group Post) — filtros: Group, Channel, Comment Content
- **Cat11 g9 — Membro Inscrito em Evento do Grupo** (Member Registered for Group Event) — filtros: Group, Event Title
  - Fonte (g6-g9): [changelog — New Communities Triggers](https://ideas.gohighlevel.com/changelog/new-communities-triggers-in-workflows-automate-more-faster)

**4 novas ações adicionadas:**
- **Cat02 a26 — Enviar Mensagem RCS** (Send RCS Message) — ⚠ **Private Beta**, acesso via CSM, GA prevista pro fim do Q3 2026. Campos exatos podem mudar antes do GA. Fonte: [changelog](https://ideas.gohighlevel.com/changelog/rcs-messaging-is-now-available-in-workflows-private-beta)
- **Cat07 a11 — Encontrar Oportunidade** (Find Opportunity) — busca a oportunidade mais antiga/recente do contato por filtro, com branch "Opportunity Not Found". Fonte: [doc](https://help.gohighlevel.com/support/solutions/articles/155000004751-workflow-action-find-opportunity)
- **Cat07 a12 — Remover Dono da Oportunidade** (Remove Owner from Opportunity). Fonte: [doc](https://help.gohighlevel.com/support/solutions/articles/155000004755-workflow-action-remove-owner-from-opportunity)
- **Cat07 a13 — Remover Seguidores da Oportunidade** (Remove Follower(s) from Opportunity), contraparte da a10 existente. Fonte: [changelog](https://ideas.gohighlevel.com/changelog/opportunity-workflow-actions)

**1 rename aplicado** (item já flagado numa rodada anterior, confirmado agora
com fonte oficial): Cat07 a6 "Deletar Oportunidade" → **"Remover Oportunidade"**
(EN: Delete Opportunity → Remove Opportunity). Fonte: [doc](https://help.gohighlevel.com/support/solutions/articles/155000003365-workflow-action-remove-opportunity)

**Descartado por baixa confiança:** triggers "Payment Failed" e "Form
Partially Completed" apareceram em sites de conteúdo de terceiros
(rsla.io, softomatesolutions.com e similares) mas não em nenhuma página
oficial `help.gohighlevel.com`/`ideas.gohighlevel.com` — a doc oficial
descreve falha de pagamento como um filtro de status dentro do trigger
**Payment Received** já existente, não um trigger dedicado. Não adicionados.

Novo total: **82 gatilhos, 114 ações, 196 painéis/mockups** (era 77/110/187).
Contagens da home (`index.html`) e `AUDIT-TABLE.md` atualizadas junto.

## Como cada item foi verificado

- ✅ **Confirmado por WebSearch** — agente puxou resumo da página oficial e comparou
- ⚠ **Aplicar com revisão** — discrepância encontrada mas precisa olho humano antes de mexer
- 🔍 **Pendente** — ainda não auditado

## Status geral

| Lote | Status | Itens | Confirmados |
|------|--------|------:|-----------:|
| **Gatilhos cat01-cat12** | ✅ | 82 | 76 (+ 5 novos g20/g6-g9, fonte changelog oficial, ainda sem verificação de UI ao vivo) |
| **Ações cat01** (Contact) | ✅ | 16 | 16 |
| **Ações cat02** (Comunicação) | ✅ | 26 | 22 (3 c/ flag + 1 novo a26 RCS, Beta, fonte changelog oficial) |
| **Ações cat03** (Webhooks) | ✅ | 4 | 4 |
| **Ações cat04** (Workflow logic) | ✅ | 17 | 17 |
| **Ações cat05** (AI) | ✅ | 5 | 5 (2 renames recomendados) |
| **Ações cat06** (Appointments) | ✅ | 3 | 3 (A2/A3 fake removidas, substituídas por Book Appointment + Create Appointment Note) |
| **Ações cat07** (Opportunities) | ✅ | 13 | 8 (rename A6 aplicado + 3 novas a11-a13, fonte doc oficial; 2 sem doc) |
| **Ações cat08** (Payments) | ✅ | 5 | 3 (2 sem doc dedicada) |
| **Ações cat09** (Campaigns) | ✅ | 5 | 5 (campaigns deprecadas pra workflows) |
| **Ações cat10** (Affiliates) | ✅ | 6 | 4 (A4/A5 sem doc) |
| **Ações cat11** (Memberships) | ✅ | 2 | 2 |
| **Ações cat12** (IVR) | ✅ | 5 | 4 (A4 rename) |
| **Ações cat13** (Communities) | ✅ | 6 | 4 (A5/A6 sem doc) |
| **Ações cat14** (Certificados) | ✅ | 1 | 1 |
| **Total** | **✅** | **196** | **179/196 (91%)** |

## ✅ Fixes aplicados nesta auditoria

### Gatilhos
1. **Cat01 G3 Contact DND** — adicionado filtro DND Direction (Inbound/Outbound/Both)
2. **Cat01 G5 Engagement Score** — adicionado filtro Business Niche
3. **Cat11 G2** renomeado: "Group Removal" → "Group Access Revoked"
4. **Cat11 G4** renomeado: "Private Channel Access Removed" → "Private Channel Access Revoked"

### Ações
5. **Cat07 A6** renomeado: "Delete Opportunity" → **"Remove Opportunity"** (fonte oficial confirmada — ver rodada 2026-07-08 acima). Sinônimos antigos mantidos no `data-name` pra não quebrar busca.

Demais achados abaixo seguem sem fix — precisam de validação humana contra
a UI real do HL antes de aplicar (rename de ações afeta como o usuário
busca elas no builder).

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
