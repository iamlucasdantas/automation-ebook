# AUDIT — Conferência contra a UI real do HighLevel

Documento vivo de auditoria contra as docs oficiais do HighLevel
(`help.gohighlevel.com`). Aqui ficam os achados acionáveis. A tabela
completa de status por entry está em [AUDIT-TABLE.md](./AUDIT-TABLE.md)
(gerada por `scripts/build-audit.py`).

## Fonte da verdade

- ✅ **Confirmado** — agente conseguiu `WebSearch site:help.gohighlevel.com`
  e extraiu campos do resumo oficial da página
- ⚠ **Inspeção interna** — agente não conseguiu acessar docs externos
  e comparou só o HTML contra ele mesmo (achados são pistas, não
  verdades absolutas)
- 🔍 **Pendente** — ainda não auditado

## Resumo da primeira rodada (2026-06-16)

| Lote | Status fonte | Itens | Notas |
|------|--------------|------:|-------|
| Gatilhos cat01 | ✅ Confirmado (WebSearch) | 12 | 2 fixes aplicados |
| Gatilhos cat02 | ⚠ Inspeção interna | 17 | Plausível, sem fonte autoritativa |
| Gatilhos cat03-06 | ⚠ Inspeção interna | 21 | Idem |
| Gatilhos cat07-09 | ⚠ Inspeção interna | 14 | URLs citadas, achados específicos plausíveis |
| Gatilhos cat10-12 | ⚠ Inspeção interna | 9 | Todos flagados "uncertain" — docs sparse |
| Ações cat01-14 | 🔍 Pendente | 109 | Próximo lote |

## ✅ Achados aplicados (cat01)

### G3 · Contact DND
- **Doc:** https://help.gohighlevel.com/support/solutions/articles/155000002673-workflow-trigger-contact-dnd
- ➕ Faltava **DND Direction (Inbound/Outbound/Both)** — adicionado como filtro dropdown
- ✅ Outros filtros (DND Status, Channel multi-select, Has Tag) já corretos

### G5 · Contact Engagement Score
- **Doc:** https://help.gohighlevel.com/support/solutions/articles/155000003496-workflow-trigger-contact-engagement-score
- ➕ Faltava **Business Niche** — adicionado como filtro dropdown
- ✅ Outros filtros (Score Threshold com 4 operadores, Has Tag) já corretos

## ⚠ Pendente revisão manual (inspeção interna)

Achados que vieram dos agentes sem acesso confirmado às docs oficiais.
**Não aplicar cegamente** — usar como worklist pra você abrir HL e
confirmar antes de eu mexer:

### Cat02 — Eventos
- **G7 Quiz Submitted**: Category Score (uma linha por categoria do quiz) — JÁ implementado ✓
- **G16 New Review Received**: ⚠ Contactless Workflow (sem merge fields `{{contact.*}}`) — adicionar nota se confirmado
- **G17 Prospect Generated**: Source = In-App / Widget / Prospect AI (3 opções)

### Cat07 — Pagamentos
- **G2 Payment Received**: Source = 8 opções (Calendar/External/Form/Funnel/Invoice/Manual/Memberships/Website) + Sub-Source conditional
- **G6 Subscription**: 8 estados (Active/Canceled/Expired/Incomplete Expired/Past Due/Paused/Trialing/Unpaid)
- **G7 Refund**: ⚠ Stripe direct refunds NÃO disparam — adicionar nota
- **G5 Documents and Contracts**: ⚠ Status avaliado só na entrada do workflow — mudanças subsequentes precisam workflow separado
- **G8 Coupon Applied**: incluir "Products in Order" multi-select

### Cat08 — E-commerce
- **G1 Cart Abandoned**: Source Shopify-specific (Store/External com Sub-Source)
- **G2 Order Placed**: Shopify-specific filtering

### Cat09 — IVR
- **G1 Start IVR**: ⚠ Cada LC Phone Number só pode estar em UM IVR ativo (auto-desativa outros) — regra crítica

### Cat10 — Comentários sociais
- **G1 Facebook Comment**: "Track First Level Comments Only" toggle + "Post Type (Published/Custom)"
- **G2 Instagram Comment**: "Exact Match Phrase" vs "Contains Phrase" — verificar nomenclatura
- **G3 TikTok**: Account dropdown + "Video Is" conditional

### Cat11 — Comunidades
- **G3 Private Channel**: pode precisar Group + Private Channel como 2 dropdowns separados

## Próximos passos

1. **Ações cat01-14 (109 entries)** — disparar nova rodada de agentes Explore com instruções mais estritas pra forçar WebSearch real
2. **Validação humana dos pendentes** — você abre HL e confirma os itens marcados ⚠ acima
3. **Re-rodada dos gatilhos cat02-cat12** — re-disparar com prompt menor por categoria pra forçar WebSearch (cat01 funcionou, os outros não)

## Como o usuário pode contribuir

Pra acelerar, abre o HL Workflow Builder e me cola/descreve os
campos dos triggers/actions específicos da lista ⚠ acima. Eu marco
✅ ou aplico fix conforme a info entrar.
