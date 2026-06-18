# AUDIT — Conferência contra a UI real do HighLevel

Auditoria contra `help.gohighlevel.com`. Aqui ficam os achados acionáveis.
Tabela completa de status por entry em [AUDIT-TABLE.md](./AUDIT-TABLE.md).

## Como cada item foi verificado

- ✅ **Confirmado por WebSearch** — agente puxou resumo da página oficial e comparou
- ⚠ **Aplicar com revisão** — discrepância encontrada mas precisa olho humano antes de mexer
- 🔍 **Pendente** — ainda não auditado

## Status geral (2026-06-16)

| Lote | Status | Itens | Fontes oficiais consultadas |
|------|--------|------:|-----------------------------|
| Gatilhos cat01 | ✅ Confirmado | 12 | 12 docs (todos com URL) |
| Gatilhos cat02 | ✅ Confirmado | 17 | 17 docs |
| Gatilhos cat03 | ✅ Confirmado | 2 | 2 docs |
| Gatilhos cat04 | ✅ Confirmado | 5 | 5 docs |
| Gatilhos cat05 | ✅ Confirmado | 4 | 4 docs |
| Gatilhos cat06 | ✅ Confirmado | 12 | ~10 docs |
| Gatilhos cat07 | ✅ Confirmado | 10 | 10 docs |
| Gatilhos cat08 | ✅ Confirmado | 3 | 3 docs |
| Gatilhos cat09 | ✅ Confirmado | 1 | 1 doc |
| Gatilhos cat10 | ✅ Confirmado | 3 | 3 docs |
| Gatilhos cat11 | ✅ Confirmado | 5 | 5 docs |
| Gatilhos cat12 | ✅ Confirmado | 1 | 1 doc |
| **Total gatilhos** | **✅ 76/76** | | ~73 fontes |
| Ações cat01-14 | 🔍 Pendente | 109 | — |

## ✅ Fixes aplicados

### Cat01 G3 · Contact DND
- **Doc:** https://help.gohighlevel.com/support/solutions/articles/155000002673-workflow-trigger-contact-dnd
- ➕ Adicionado filtro **DND Direction (Inbound/Outbound/Both)** que faltava

### Cat01 G5 · Contact Engagement Score
- **Doc:** https://help.gohighlevel.com/support/solutions/articles/155000003496-workflow-trigger-contact-engagement-score
- ➕ Adicionado filtro **Business Niche** que faltava

### Cat11 G2 · Group Access Revoked (nomenclatura)
- **Doc:** https://help.gohighlevel.com/support/solutions/articles/155000001239-workflow-triggers-for-communities-granting-and-revoking-group-access
- ⚠ Renomeado de "Group Removal" → **"Group Access Revoked"** (configData kind + title)

### Cat11 G4 · Private Channel Access Revoked (nomenclatura)
- **Doc:** https://help.gohighlevel.com/support/solutions/articles/155000003681-workflow-trigger-action-grant-revoke-private-channel-access
- ⚠ Renomeado de "Private Channel Access Removed" → **"Private Channel Access Revoked"** (trigger-en + configData)

## 📋 Discrepâncias menores observadas mas NÃO aplicadas

Pontos que os agentes flagaram mas que decidi não mexer agora (low impact ou requerem confirmação adicional):

### Cat02 G2 · Call Status
- HTML tem "In Phone Number" como filtro. Doc oficial não cita explicitamente mas existe na UI. **Manter como está.**

### Cat02 G13 · Funnel/Website Page View
- Doc oficial menciona **UTM Medium** além de UTM Campaign/Source. Nosso HTML não tem. **Worklist:** considerar adicionar.

### Cat05 — Afiliados
- Agente flagou vários "Falta", mas confundiu **merge fields** (referral_link, magic login link, commission earned) com **filter fields**. Os merge fields são valores expostos pelo gatilho, não filtros do config panel. **Achados descartados.**

### Cat07 G2 · Payment Received
- Confirmado: 8 sources (Calendar/External/Form/Funnel/Invoice/Manual/Memberships/Website) + Sub-Source conditional + Payment Status (Success/Failed) + Customer Type + Product + Product Price filters. ✅ Tudo já está no nosso painel.

### Cat07 G5 · Documents and Contracts
- ⚠ Doc menciona "Status avaliado só na entrada" — adicionar nota didática se ainda não temos.

### Cat07 G6 · Subscription Event
- 8 estados confirmados (Active/Cancelled/Expired/Failed/Incomplete/Overdue/Trial/Unpaid). ✅

### Cat07 G7 · Refund
- ⚠ Stripe direct refunds NÃO disparam — adicionar nota didática.

### Cat09 G1 · IVR
- ⚠ Cada LC Phone Number só pode estar em UM IVR ativo (auto-desativa outros) — regra crítica, adicionar destaque.

### Cat10 G3 · TikTok Comments
- Doc usa **"Account"** (não "Page"). HTML usa "Conta TikTok" (PT) — semanticamente correto. **Manter.**

### Cat11 — Todos os 5
- Doc oficial não documenta explicitamente filtros de "Custom Fields" pra Communities, mas eles existem na UI. Nosso HTML mostra. **Manter.**

## Próximo passo

**Auditoria das 109 ações** — disparar nova rodada de agentes Explore com o mesmo protocolo (WebSearch primeiro, escopo pequeno por agente).

Categorias de ação:
- cat01 Eventos de Existência (10 ações)
- cat02 Eventos (12)
- cat03 Agendamentos (5)
- cat04 Oportunidades (4)
- cat05 Afiliados (4)
- cat06 Memberships (6)
- cat07 Pagamentos (7)
- cat08 E-commerce (3)
- cat09 IVR (8)
- cat10 Comentários sociais (4)
- cat11 Comunidades (5)
- cat12 Certificados (2)
- cat13 Comunicação multi-canal (24)
- cat14 Lógica de workflow (15)

Total: 109 ações distribuídas em 14 categorias.
