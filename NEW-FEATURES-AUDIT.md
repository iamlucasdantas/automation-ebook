# Novos gatilhos/ações nativos — auditoria de 2026-07-01

Varredura contra `help.gohighlevel.com` e `ideas.gohighlevel.com` (changelog
oficial) pra achar gatilhos/ações **nativos** do HighLevel que existem hoje
mas não estão no nosso catálogo de 76 gatilhos + 110 ações.

**Acesso:** `help.gohighlevel.com` bloqueia WebFetch direto (403 no proxy) —
todo achado abaixo vem de snippets do WebSearch citando o artigo oficial
(título + trecho), não da página renderizada inteira. Confiança marcada por
item. **Antes de construir as páginas/mockups com fidelidade total (padrão
do guia), confirme cada item contra a UI real do HL** — é o mesmo processo
que o `AUDIT.md` já usa pros itens existentes.

## Gatilhos candidatos (não estão nos 76 atuais)

| Nome (EN) | Categoria sugerida | Confiança | Fonte |
|---|---|:-:|---|
| **Scheduler** — dispara por horário (diário/semanal/mensal), sem contato associado; mutuamente exclusivo com outros gatilhos no mesmo workflow | Nova seção em Integrações (cat02) ou categoria própria | 🟢 Alta | [artigo](https://help.gohighlevel.com/support/solutions/articles/155000006653-workflow-trigger-scheduler) |
| **Company Created** | Nova categoria "Empresas" (B2B) | 🟢 Alta | [artigo](https://help.gohighlevel.com/support/solutions/articles/155000006609-workflow-trigger-company-created) |
| **Company Changed** — dispara quando campos selecionados da Company mudam (não dispara na criação) | Nova categoria "Empresas" | 🟢 Alta | [artigo](https://help.gohighlevel.com/support/solutions/articles/155000006494-workflow-trigger-company-changed) |
| **Company Deleted** | Nova categoria "Empresas" | 🟡 Média (citado, sem artigo dedicado capturado) | via busca "Company Workflow Triggers" |
| **Object Created / Object Changed / Object Deleted** (Custom Objects) — dispara quando um registro de objeto personalizado é criado/atualizado/removido | Nova categoria "Objetos Personalizados" | 🟡 Média-Alta | [artigo](https://help.gohighlevel.com/support/solutions/articles/155000004389-using-custom-objects-in-workflow-actions-and-triggers) |
| **Product Review Submitted** (e-commerce) — avaliação de produto enviada, com filtro de nota (1-5) | CAT08 Shopify (e-commerce) | 🟢 Alta | [artigo](https://help.gohighlevel.com/support/solutions/articles/155000007386-workflow-trigger-product-review-submitted-for-e-commerce-stores-) |
| **Call Details** — possível segundo gatilho de chamada além de "Call Status"; checar se substitui/complementa o existente | CAT02 Integrações | 🟡 Média — verificar se não é o mesmo item renomeado | [artigo](https://help.gohighlevel.com/support/solutions/articles/48001212511-workflow-trigger-call-details) |
| **Fathom – New Recording** — nova gravação de reunião processada no Fathom (integração nativa) | CAT02 Integrações | 🟡 Média | [artigo](https://help.gohighlevel.com/support/solutions/articles/155000007578-fathom-actions-triggers-in-workflows) |

## Ações candidatas (não estão nas 110 atuais)

| Nome (EN) | Categoria sugerida | Confiança | Fonte |
|---|---|:-:|---|
| **Book Appointment** — cria um compromisso direto num calendário a partir do workflow (diferente de status/reassign/cancel que já temos) | CAT06 Agendamentos | 🟢 Alta — provável lacuna antiga, não só novidade | [artigo](https://help.gohighlevel.com/support/solutions/articles/155000004209-workflow-action-book-appointment) |
| **AI Agent** — ação autônoma multi-step: recebe objetivo em linguagem natural + até 10 ferramentas, planeja passos, puxa contexto do CRM, retorna texto ou JSON estruturado | CAT05 Workflow AI | 🟢 Alta | [artigo](https://help.gohighlevel.com/support/solutions/articles/155000007600-workflow-action-ai-agent) |
| **Invoke Agent Studio Agent** — roda um agente construído no Agent Studio a partir de um step do workflow | CAT05 Workflow AI | 🟢 Alta | [artigo](https://help.gohighlevel.com/support/solutions/articles/155000007402-workflow-action-invoke-agent-studio-agent) |
| **AI Data Extract** — extrai variáveis estruturadas e tipadas de texto livre (~mai/2026) | CAT05 Workflow AI — checar se não duplica "AI Extract Info" (a4) já catalogada | 🟡 Média | [changelog](https://ideas.gohighlevel.com/changelog/ai-data-extract-action-in-workflows) |
| **Mistral AI actions** (Create Chat Completion, Create Embeddings, Analyze Image) — ações de outro provider de IA dentro da categoria Workflow AI, beta | CAT05 Workflow AI | 🟡 Média | [changelog](https://ideas.gohighlevel.com/changelog/mistral-ai-workflow-actions) |
| **Custom Code (AI) / Custom Code** — gera/roda JavaScript custom a partir de descrição em linguagem natural; checar se "Custom Code" já existe como ação separada de "Custom API Call" | CAT04 Ferramentas Internas | 🟡 Média | [artigo](https://help.gohighlevel.com/support/solutions/articles/155000004709-workflow-action-custom-code-ai) |
| **Create Company or Associated Contact** / **Update Company or Associated Contact** / **Clear Associated Company Fields** | Nova categoria "Empresas" | 🟢 Alta | [artigo](https://help.gohighlevel.com/support/solutions/articles/155000006688-company-based-workflows-company-triggers-actions) |
| **Find Object Record / Find Company** — busca registro de Company ou Custom Object via dados de webhook | Nova categoria "Empresas"/"Objetos Personalizados" | 🟢 Alta | [artigo](https://help.gohighlevel.com/support/solutions/articles/155000006483-workflow-action-find-object-record-find-company) |
| **Add Associated Records to Workflow** / **Remove Associated Records from Workflow** — inscreve/remove registros associados (Contact/Company/Custom Object) em outro workflow, filtrando por Association Label | CAT04 Ferramentas Internas | 🟢 Alta | [changelog](https://ideas.gohighlevel.com/changelog/new-workflow-actions-add-remove-associated-records-from-workflows) |
| **Log External Call** — registra uma chamada externa (feita fora da plataforma) na conversa do contato | CAT02 Comunicação ou CAT12 IVR | 🟡 Média-Alta | [changelog](https://ideas.gohighlevel.com/changelog/new-workflow-action-log-external-call-to-crm) |
| **Community leaderboard points action** | CAT13 Comunidades — checar se já é coberta por "Assign Leaderboard Level" (a5) | 🟡 Média — possível duplicata | [changelog](https://ideas.gohighlevel.com/changelog/community-leaderboard-workflow-trigger-action) |

## Confirmado que NÃO são novidade (ruído descartado)

- "Payment Failed", "Membership access expiry", "Survey/Form Partial
  Completion" — são apenas pedidos no board de ideias (`ideas.gohighlevel.com`),
  não features lançadas. Não adicionar.
- Certificados (Certificate Issued / Issue Certificate), IVR (Start IVR
  Trigger, Call Status, IVR Connect/Gather/End Call), Reviews (New Review
  Received, Send Review Request) — todos já estão corretos no catálogo
  atual, só reconfirmados.
- "Transfer Call" (nosso a4 do CAT12) — nome oficial real é **"IVR Connect
  Call"**, isso já estava anotado como pendente em `AUDIT.md`.

## Como proceder

O guia se vende com "fidelidade total à interface real" — cada campo com o
tipo certo, todas as opções listadas. Construir ~19 novas entradas (2
categorias novas de gatilho, 1-2 novas de ação) direto de snippet de busca,
sem ver a UI real, quebraria esse padrão. Meu recomendo:

1. Abrir o Workflow Builder do HL e confirmar os itens 🟢/🟡 acima (nome
   exato, campos, opções) — mesmo processo que os itens `⚠` do `AUDIT.md`.
2. Depois de confirmado, construir as páginas novas (`guia-highlevel-cat13.html`
   "Empresas", `guia-highlevel-cat14.html` "Objetos Personalizados",
   ações correspondentes) seguindo o template das categorias existentes.
3. Atualizar `index.html`, `search-index.json`, `AUDIT-TABLE.md` e sidebar
   nav de todas as páginas com as novas categorias.

Até lá, este arquivo é o backlog priorizado do que falta.

## Addendum — mais candidatas (Pagamentos, Afiliados)

Uma segunda leva de sub-agentes (varredura por categoria: Pagamentos,
Afiliados, Comunidades, Cursos) trouxe mais candidatas depois do corte
inicial acima. Mesmo aviso de confiança (snippet de busca, não
verificado contra a UI real):

| Nome (EN) | Categoria sugerida | Confiança | Nota |
|---|---|:-:|---|
| **Send Invoice** | CAT08 Pagamentos | 🟡 Média | Checar se não é o mesmo fluxo da nossa "Create Invoice" (a1) já catalogada |
| **Send Recurring Invoice** | CAT08 Pagamentos | 🟡 Média | Cobrança recorrente automatizada |
| **Stripe One Time Charge** | CAT08 Pagamentos | 🟡 Média | Cobrança avulsa direto via Stripe |
| **Update Affiliate** (Active/Inactive) | CAT10 Afiliados | 🟡 Média | Ativar/desativar afiliado |
| **Add Leads Under an Affiliate** | CAT10 Afiliados | 🟡 Média | Atribui leads a um afiliado específico |
| **Add Manual Sales For An Affiliate** | CAT10 Afiliados | 🟡 Média | Lança venda manual pro afiliado |

**Discrepância pra verificar:** essa varredura reportou "nenhuma ação
nativa de Cancel/Pause Subscription existe — só pedido de feature em
aberto", o que contradiz nossa "Cancelar Subscription" (CAT08 a5) já
catalogada. Pode ser que a a5 esteja com nome/comportamento errado desde
sempre (o `AUDIT.md` já marcava os itens de pagamento como parcialmente
"sem doc dedicada") — **confirmar contra a UI real antes de mexer**.

Certificados, IVR e Reviews foram reconfirmados como já corretos por essa
segunda leva também — nada novo lá além do que já está listado acima.
