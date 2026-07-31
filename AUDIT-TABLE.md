# AUDIT — Conferência contra a UI real do HighLevel
Status auto-gerado por `scripts/build-audit.py` baseado em sinais mensuráveis do HTML/JS (presença e qualidade do painel HL, profundidade das entries configData, número de params no node).
**Como ler a confiança:**
- 🟢 **Alta** — painel HL com 3+ widgets reais + click-panel com 3+ campos + ações detalhadas
- 🟡 **Média** — falta um dos sinais (geralmente HL panel raso ou click-panel curto)
- 🔴 **Baixa** — sem painel HL ou click-panel com 1-2 campos

_Use a coluna `Verificar` pra marcar `[x]` conforme você confere contra o HL real (UI ou docs)._

## Resumo
| Tipo | 🟢 Alta | 🟡 Média | 🔴 Baixa | **Total** |
|------|--------:|--------:|--------:|----------:|
| Gatilhos | 31 | 53 | 3 | **87** |
| Ações | 38 | 77 | 8 | **123** |


## Gatilhos · 12 categorias

### CAT01 · Eventos de Existência
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| g1 | [Criação de Contato](guia-highlevel-cat01.html#g1) | Contact Created | 5 | 4/6 | 🟢 | [ ] | |
| g2 | [Alterações no Contato](guia-highlevel-cat01.html#g2) | Contact Changed | 5 | 3/6 | 🟢 | [ ] | |
| g3 | [Contato Ativou DND](guia-highlevel-cat01.html#g3) | Contact DND | 3 | 5/6 | 🟡 | [ ] | |
| g4 | [Tag Adicionada ou Removida](guia-highlevel-cat01.html#g4) | Contact Tag | 3 | 5/6 | 🟢 | [ ] | |
| g5 | [Pontuação de Engajamento](guia-highlevel-cat01.html#g5) | Contact Engagement Score | 3 | 3/6 | 🟢 | [ ] | |
| g6 | [Lembrete de Aniversário](guia-highlevel-cat01.html#g6) | Birthday Reminder | 5 | 5/6 | 🟢 | [ ] | |
| g7 | [Lembrete de Data Personalizada](guia-highlevel-cat01.html#g7) | Custom Date Reminder | 5 | 3/6 | 🟢 | [ ] | |
| g8 | [Nota Adicionada](guia-highlevel-cat01.html#g8) | Note Added | 4 | 4/6 | 🟢 | [ ] | |
| g9 | [Nota Alterada](guia-highlevel-cat01.html#g9) | Note Changed | 3 | 2/6 | 🟡 | [ ] | |
| g10 | [Tarefa Adicionada](guia-highlevel-cat01.html#g10) | Task Added | 4 | 2/6 | 🟡 | [ ] | |
| g11 | [Lembrete de Tarefa](guia-highlevel-cat01.html#g11) | Task Reminder | 4 | 3/6 | 🟢 | [ ] | |
| g12 | [Tarefa Completada](guia-highlevel-cat01.html#g12) | Task Completed | 3 | 2/6 | 🟡 | [ ] | |

### CAT02 · Integrações & Webhooks
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| g1 | [Webhook de Entrada](guia-highlevel-cat02.html#g1) | Inbound Webhook | 5 | 3/6 | 🟢 | [ ] | |
| g2 | [Status de Ligação](guia-highlevel-cat02.html#g2) | Call Status | 4 | 4/6 | 🟢 | [ ] | |
| g3 | [Eventos de Email](guia-highlevel-cat02.html#g3) | Email Events | 4 | 4/6 | 🟢 | [ ] | |
| g4 | [Contato Respondeu](guia-highlevel-cat02.html#g4) | Customer Replied | 3 | 3/6 | 🟢 | [ ] | |
| g5 | [Formulário Preenchido](guia-highlevel-cat02.html#g5) | Form Submitted | 3 | 3/6 | 🟢 | [ ] | |
| g6 | [Survey Respondido](guia-highlevel-cat02.html#g6) | Survey Submitted | 2 | 2/6 | 🟡 | [ ] | |
| g7 | [Quiz Respondido](guia-highlevel-cat02.html#g7) | Quiz Submitted | 4 | 2/6 | 🟡 | [ ] | |
| g8 | [Formulário de Lead do Facebook](guia-highlevel-cat02.html#g8) | Facebook Lead Form Submitted | 3 | 2/6 | 🟡 | [ ] | |
| g9 | [Formulário de Lead do TikTok](guia-highlevel-cat02.html#g9) | TikTok Lead Form Submitted | 3 | 2/6 | 🟡 | [ ] | |
| g10 | [Formulário de Lead do LinkedIn](guia-highlevel-cat02.html#g10) | LinkedIn Lead Form Submitted | 3 | 2/6 | 🟡 | [ ] | |
| g11 | [Link de Gatilho](guia-highlevel-cat02.html#g11) | Trigger Link | 2 | 2/6 | 🟡 | [ ] | |
| g12 | [Vídeo Assistido em Funil](guia-highlevel-cat02.html#g12) | Video Tracking | 4 | 3/6 | 🟢 | [ ] | |
| g13 | [Visualização de Página](guia-highlevel-cat02.html#g13) | Funnel/Website Page View | 4 | 3/6 | 🟢 | [ ] | |
| g14 | [Validação de Número](guia-highlevel-cat02.html#g14) | Number Validation | 2 | 3/6 | 🟡 | [ ] | |
| g15 | [Erro de Mensagem SMS](guia-highlevel-cat02.html#g15) | Messaging Error - SMS | 2 | 3/6 | 🟡 | [ ] | |
| g16 | [Nova Avaliação Recebida](guia-highlevel-cat02.html#g16) | New Review Received | 3 | 3/6 | 🟢 | [ ] | |
| g17 | [Novo Prospecto](guia-highlevel-cat02.html#g17) | Prospect Generated | 3 | 3/6 | 🟢 | [ ] | |
| g18 | [Transcript Gerado](guia-highlevel-cat02.html#g18) | Transcript Generated | 4 | 2/6 | 🟡 | [ ] | |
| g19 | [Agendador (Scheduler)](guia-highlevel-cat02.html#g19) | Scheduler | 6 | 3/6 | 🟢 | [ ] | |
| g20 | [Email Recebido](guia-highlevel-cat02.html#g20) | Inbound Email | 3 | 2/6 | 🟡 | [ ] | |
| g21 | [Usuário Respondeu](guia-highlevel-cat02.html#g21) | User Replied | 3 | 3/6 | 🟡 | [ ] | |
| g22 | [AI Studio — Formulário Enviado](guia-highlevel-cat02.html#g22) | AI Studio Form Submitted | 3 | 2/6 | 🟡 | [ ] | |

### CAT03 · Agendamentos
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| g1 | [Status de Compromisso](guia-highlevel-cat03.html#g1) | Appointment Status | 4 | 4/6 | 🟢 | [ ] | |
| g2 | [Contato Marcou Agendamento](guia-highlevel-cat03.html#g2) | Customer Booked Appointment | 4 | 4/6 | 🟢 | [ ] | |

### CAT04 · Ciclo de Vida
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| g1 | [Oportunidade Criada](guia-highlevel-cat04.html#g1) | Opportunity Created | 4 | 3/6 | 🟢 | [ ] | |
| g2 | [Oportunidade Alterada](guia-highlevel-cat04.html#g2) | Opportunity Changed | 4 | 2/6 | 🟡 | [ ] | |
| g3 | [Mudança de Status em Oportunidade](guia-highlevel-cat04.html#g3) | Opportunity Status Changed | 4 | 2/6 | 🟡 | [ ] | |
| g4 | [Mudança de Estágio no Pipeline](guia-highlevel-cat04.html#g4) | Pipeline State Changed | 4 | 2/6 | 🟡 | [ ] | |
| g5 | [Oportunidade Ociosa](guia-highlevel-cat04.html#g5) | Stale Opportunities | 4 | 2/6 | 🟡 | [ ] | |

### CAT05 · Ciclo de Vida do Afiliado
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| g1 | [Afiliado Criado](guia-highlevel-cat05.html#g1) | Affiliate Created | 2 | 1/6 | 🟡 | [ ] | |
| g2 | [Afiliado Inscrito em Campanha](guia-highlevel-cat05.html#g2) | Affiliate Enrolled in Campaign | 3 | 3/6 | 🟢 | [ ] | |
| g3 | [Nova Venda de Afiliado](guia-highlevel-cat05.html#g3) | New Affiliate Sales | 4 | 2/6 | 🟡 | [ ] | |
| g4 | [Lead Criado por Afiliado](guia-highlevel-cat05.html#g4) | Lead Created (by Affiliate) | 3 | 2/6 | 🟡 | [ ] | |

### CAT06 · Progresso em Curso
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| g1 | [Categoria Iniciada](guia-highlevel-cat06.html#g1) | Category Started | 3 | 2/6 | 🟡 | [ ] | |
| g2 | [Categoria Completada](guia-highlevel-cat06.html#g2) | Category Completed | 3 | 2/6 | 🟡 | [ ] | |
| g3 | [Aula Iniciada](guia-highlevel-cat06.html#g3) | Lesson Started | 3 | 2/6 | 🟡 | [ ] | |
| g4 | [Aula Completada](guia-highlevel-cat06.html#g4) | Lesson Completed | 3 | 2/6 | 🟡 | [ ] | |
| g5 | [Nova Inscrição](guia-highlevel-cat06.html#g5) | New Signup | 2 | 2/6 | 🟡 | [ ] | |
| g6 | [Dar Acesso a Oferta](guia-highlevel-cat06.html#g6) | Offer Access Granted | 2 | 2/6 | 🟡 | [ ] | |
| g7 | [Remover Acesso a Oferta](guia-highlevel-cat06.html#g7) | Offer Access Removed | 2 | 2/6 | 🟡 | [ ] | |
| g8 | [Dar Acesso a Produto](guia-highlevel-cat06.html#g8) | Product Access Granted | 2 | 2/6 | 🟡 | [ ] | |
| g9 | [Remover Acesso a Produto](guia-highlevel-cat06.html#g9) | Product Access Removed | 2 | 2/6 | 🟡 | [ ] | |
| g10 | [Produto Iniciado](guia-highlevel-cat06.html#g10) | Product Started | 2 | 2/6 | 🟡 | [ ] | |
| g11 | [Produto Completado](guia-highlevel-cat06.html#g11) | Product Completed | 2 | 3/6 | 🟢 | [ ] | |
| g12 | [Login de Usuário](guia-highlevel-cat06.html#g12) | User Login | 2 | 2/6 | 🟡 | [ ] | |

### CAT07 · Recebimento
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| g1 | [Cobrança (Invoice)](guia-highlevel-cat07.html#g1) | Invoice | 3 | 4/6 | 🟢 | [ ] | |
| g2 | [Pagamento Recebido](guia-highlevel-cat07.html#g2) | Payment Received | 3 | 3/6 | 🟢 | [ ] | |
| g3 | [Ordem em Formulário](guia-highlevel-cat07.html#g3) | Order Form Submission | 2 | 3/6 | 🟡 | [ ] | |
| g4 | [Ordem Submetida](guia-highlevel-cat07.html#g4) | Order Submitted | 3 | 3/6 | 🟢 | [ ] | |
| g5 | [Documentos e Contratos](guia-highlevel-cat07.html#g5) | Documents & Contracts | 2 | 3/6 | 🟢 | [ ] | |
| g6 | [Assinatura (Subscription)](guia-highlevel-cat07.html#g6) | Subscription | 3 | 3/6 | 🟢 | [ ] | |
| g7 | [Reembolso](guia-highlevel-cat07.html#g7) | Refund | 2 | 3/6 | 🟡 | [ ] | |
| g8 | [Cupom Aplicado](guia-highlevel-cat07.html#g8) | Coupon Code Applied | 2 | 4/6 | 🟡 | [ ] | |
| g9 | [Limite de Cupom Atingido](guia-highlevel-cat07.html#g9) | Coupon Redemption Limit Reached | 2 | 1/6 | 🟡 | [ ] | |
| g10 | [Cupom Expirado](guia-highlevel-cat07.html#g10) | Coupon Code Expired | 2 | 2/6 | 🟡 | [ ] | |

### CAT08 · Pré-compra
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| g1 | [Carrinho Abandonado](guia-highlevel-cat08.html#g1) | Abandoned Cart | 4 | 4/6 | 🟢 | [ ] | |
| g2 | [Compra Feita](guia-highlevel-cat08.html#g2) | Order Placed | 3 | 2/6 | 🟡 | [ ] | |
| g3 | [Pedido Concluído](guia-highlevel-cat08.html#g3) | Order Fulfilled | 3 | 2/6 | 🟡 | [ ] | |

### CAT09 · Atendimento Automatizado
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| g1 | [Iniciar Gatilho IVR](guia-highlevel-cat09.html#g1) | Start IVR Trigger | 4 | 2/6 | 🟡 | [ ] | |

### CAT10 · Engajamento Social
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| g1 | [Comentários do Facebook](guia-highlevel-cat10.html#g1) | Facebook Comment on a Post | 4 | 4/6 | 🟢 | [ ] | |
| g2 | [Comentários do Instagram](guia-highlevel-cat10.html#g2) | Instagram Comment on a Post | 4 | 3/6 | 🟢 | [ ] | |
| g3 | [Comentários do TikTok](guia-highlevel-cat10.html#g3) | TikTok – Comment(s) On A Video | 4 | 2/6 | 🟡 | [ ] | |

### CAT11 · Grupos
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| g1 | [Acesso a Grupo](guia-highlevel-cat11.html#g1) | Group Access Granted | 3 | 2/6 | 🟡 | [ ] | |
| g2 | [Remoção de Grupo](guia-highlevel-cat11.html#g2) | Group Access Revoked | 3 | 2/6 | 🟡 | [ ] | |
| g3 | [Acesso Concedido a Canal Privado](guia-highlevel-cat11.html#g3) | Private Channel Access Granted | 3 | 2/6 | 🟡 | [ ] | |
| g4 | [Remoção de Acesso a Canal Privado](guia-highlevel-cat11.html#g4) | Private Channel Access Revoked | 3 | 2/6 | 🟡 | [ ] | |
| g5 | [Mudança de Nível na Classificação](guia-highlevel-cat11.html#g5) | Community Group Member Leaderboard Level Changed | 4 | 2/6 | 🟡 | [ ] | |
| g6 | [Registrado em Evento do Grupo](guia-highlevel-cat11.html#g6) | Community Group Event Registration | 3 | 2/6 | 🟡 | [ ] | |
| g7 | [Solicitação de Entrada Rejeitada](guia-highlevel-cat11.html#g7) | Community Group Join Request Rejected | 0 | 2/6 | 🔴 | [ ] | |
| g8 | [Nova Publicação no Grupo](guia-highlevel-cat11.html#g8) | Community Group New Post | 0 | 2/6 | 🔴 | [ ] | |
| g9 | [Novo Comentário no Grupo](guia-highlevel-cat11.html#g9) | Community Group New Comment | 0 | 2/6 | 🔴 | [ ] | |

### CAT12 · Conclusão
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| g1 | [Certificado Enviado](guia-highlevel-cat12.html#g1) | Certificate Issued | 3 | 2/6 | 🟡 | [ ] | |

### CAT13 · Contatos Google
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| g1 | [Contato Google Criado](guia-highlevel-cat13.html#g1) | Google Contact Created | 2 | 2/6 | 🟡 | [ ] | |
| g2 | [Novo Grupo de Contatos Google](guia-highlevel-cat13.html#g2) | New Google Contact Group | 3 | 2/6 | 🟡 | [ ] | |
| g3 | [Resposta de Formulário Google](guia-highlevel-cat13.html#g3) | Google Form Response | 3 | 2/6 | 🟡 | [ ] | |

## Ações · 14 categorias

### CAT01 · Ação
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| a1 | [Criar Contato](acoes-highlevel-cat01.html#a1) | Create Contact | 4 | 2/6 | 🟡 | [ ] | |
| a2 | [Encontrar Contato](acoes-highlevel-cat01.html#a2) | Find Contact | 3 | 2/6 | 🟡 | [ ] | |
| a3 | [Atualizar Campos do Contato](acoes-highlevel-cat01.html#a3) | Update Contact Field | 2 | 3/6 | 🟡 | [ ] | |
| a4 | [Adicionar Tag ao Contato](acoes-highlevel-cat01.html#a4) | Add Contact Tag | 3 | 3/6 | 🟡 | [ ] | |
| a5 | [Remover Tag do Contato](acoes-highlevel-cat01.html#a5) | Remove Contact Tag | 3 | 4/6 | 🟡 | [ ] | |
| a6 | [Atribuir a Usuário](acoes-highlevel-cat01.html#a6) | Assign to User | 2 | 5/6 | 🟢 | [ ] | |
| a7 | [Remover Usuário Atribuído](acoes-highlevel-cat01.html#a7) | Remove Assigned User | 3 | 1/6 | 🟡 | [ ] | |
| a8 | [Editar Conversação](acoes-highlevel-cat01.html#a8) | Edit Conversation | 3 | 3/6 | 🟢 | [ ] | |
| a9 | [Ativar/Desativar DND](acoes-highlevel-cat01.html#a9) | Enable/Disable DND | 2 | 4/6 | 🟡 | [ ] | |
| a10 | [Adicionar às Notas](acoes-highlevel-cat01.html#a10) | Add to Notes | 3 | 1/6 | 🟡 | [ ] | |
| a11 | [Adicionar Tarefa](acoes-highlevel-cat01.html#a11) | Add Task | 3 | 2/6 | 🟡 | [ ] | |
| a12 | [Copiar Contato](acoes-highlevel-cat01.html#a12) | Copy Contact | 3 | 4/6 | 🟢 | [ ] | |
| a13 | [Deletar Contato](acoes-highlevel-cat01.html#a13) | Delete Contact | 2 | 1/6 | 🟡 | [ ] | |
| a14 | [Modificar Pontuação de Engajamento](acoes-highlevel-cat01.html#a14) | Modify Contact Engagement Score | 2 | 3/6 | 🟡 | [ ] | |
| a15 | [Adicionar Seguidores](acoes-highlevel-cat01.html#a15) | Add Contact Followers | 3 | 2/6 | 🟡 | [ ] | |
| a16 | [Remover Seguidores](acoes-highlevel-cat01.html#a16) | Remove Contact Followers | 3 | 2/6 | 🟡 | [ ] | |

### CAT02 · Ação
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| a1 | [Enviar Email](acoes-highlevel-cat02.html#a1) | Send Email | 2 | 4/6 | 🟢 | [ ] | |
| a2 | [Enviar SMS](acoes-highlevel-cat02.html#a2) | Send SMS | 2 | 2/6 | 🟡 | [ ] | |
| a3 | [Mensagem no Slack](acoes-highlevel-cat02.html#a3) | Outbound Webhook (Slack) | 3 | 2/6 | 🟡 | [ ] | |
| a4 | [Chamada Telefônica](acoes-highlevel-cat02.html#a4) | Call | 2 | 3/6 | 🟢 | [ ] | |
| a5 | [Correio de Voz](acoes-highlevel-cat02.html#a5) | Voicemail | 3 | 2/6 | 🟡 | [ ] | |
| a6 | [Facebook Messenger](acoes-highlevel-cat02.html#a6) | Facebook Messenger | 3 | 2/6 | 🟡 | [ ] | |
| a7 | [Instagram DM](acoes-highlevel-cat02.html#a7) | Instagram DM | 3 | 2/6 | 🟡 | [ ] | |
| a8 | [Ação Manual para SMS](acoes-highlevel-cat02.html#a8) | Manual Action to SMS | 3 | 2/6 | 🟡 | [ ] | |
| a9 | [Ação Manual para Chamada](acoes-highlevel-cat02.html#a9) | Manual Action to Call | 3 | 2/6 | 🟡 | [ ] | |
| a10 | [Notificação Interna](acoes-highlevel-cat02.html#a10) | Internal Notification | 2 | 4/6 | 🟢 | [ ] | |
| a11 | [Pedido de Avaliação](acoes-highlevel-cat02.html#a11) | Review Request | 3 | 4/6 | 🟢 | [ ] | |
| a12 | [WhatsApp Oficial](acoes-highlevel-cat02.html#a12) | WhatsApp Official | 3 | 3/6 | 🟢 | [ ] | |
| a13 | [Email do Conversas IA](acoes-highlevel-cat02.html#a13) | Conversation AI Email | 2 | 2/6 | 🟡 | [ ] | |
| a14 | [SMS do Conversas IA](acoes-highlevel-cat02.html#a14) | Conversation AI SMS | 2 | 2/6 | 🟡 | [ ] | |
| a15 | [Enviar Formulário por SMS](acoes-highlevel-cat02.html#a15) | Send Form via SMS | 3 | 2/6 | 🟡 | [ ] | |
| a16 | [Enviar Survey por SMS](acoes-highlevel-cat02.html#a16) | Send Survey via SMS | 3 | 2/6 | 🟡 | [ ] | |
| a17 | [Ligação com IA](acoes-highlevel-cat02.html#a17) | Voice AI Call | 3 | 3/6 | 🟢 | [ ] | |
| a18 | [Responder Comentário FB](acoes-highlevel-cat02.html#a18) | Reply to FB Comment | 3 | 3/6 | 🟢 | [ ] | |
| a19 | [Responder Comentário IG](acoes-highlevel-cat02.html#a19) | Reply to IG Comment | 3 | 2/6 | 🟡 | [ ] | |
| a20 | [Gerar Conteúdo com IA](acoes-highlevel-cat02.html#a20) | AI Content Generation | 3 | 3/6 | 🟢 | [ ] | |
| a21 | [Mensagem via Número Específico](acoes-highlevel-cat02.html#a21) | Send From Specific Number | 3 | 2/6 | 🟡 | [ ] | |
| a22 | [Mensagem com Número Pool](acoes-highlevel-cat02.html#a22) | Send From Number Pool | 2 | 2/6 | 🟡 | [ ] | |
| a23 | [Confirmação GMB](acoes-highlevel-cat02.html#a23) | GMB Confirmation | 2 | 2/6 | 🔴 | [ ] | |
| a24 | [SMS via Shortcode](acoes-highlevel-cat02.html#a24) | Shortcode SMS | 2 | 2/6 | 🟡 | [ ] | |
| a25 | [Anexar Arquivo](acoes-highlevel-cat02.html#a25) | Attach File | 2 | 3/6 | 🟢 | [ ] | |

### CAT03 · Ação
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| a1 | [Webhook de Saída](acoes-highlevel-cat03.html#a1) | Outbound Webhook | 4 | 4/6 | 🟢 | [ ] | |
| a2 | [Google Sheets](acoes-highlevel-cat03.html#a2) | Google Sheets | 3 | 3/6 | 🟢 | [ ] | |
| a3 | [Enviar Dados pra API Custom](acoes-highlevel-cat03.html#a3) | Custom API Call | 2 | 2/6 | 🟡 | [ ] | |
| a4 | [Enviar Conversão para Meta e Google](acoes-highlevel-cat03.html#a4) | Send Conversion Event (Meta CAPI · Google Ads) | 4 | 4/6 | 🟢 | [ ] | |
| a5 | [Código Customizado](acoes-highlevel-cat03.html#a5) | Custom Code | 2 | 2/6 | 🟡 | [ ] | |

### CAT04 · Ação
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| a1 | [If/Else](acoes-highlevel-cat04.html#a1) | If/Else Condition | 2 | 3/6 | 🟢 | [ ] | |
| a2 | [Wait (Esperar)](acoes-highlevel-cat04.html#a2) | Wait | 2 | 5/6 | 🟡 | [ ] | |
| a3 | [Wait Until Event](acoes-highlevel-cat04.html#a3) | Wait Until Event Date | 2 | 3/6 | 🟡 | [ ] | |
| a4 | [Set Event Date](acoes-highlevel-cat04.html#a4) | Set Event Date | 2 | 2/6 | 🟡 | [ ] | |
| a5 | [Goal Event](acoes-highlevel-cat04.html#a5) | Goal Event | 3 | 4/6 | 🟢 | [ ] | |
| a6 | [Math Operation](acoes-highlevel-cat04.html#a6) | Math Operation | 2 | 3/6 | 🟢 | [ ] | |
| a7 | [Custom Value Update](acoes-highlevel-cat04.html#a7) | Update Custom Value | 2 | 2/6 | 🟡 | [ ] | |
| a8 | [Create Calendar Event](acoes-highlevel-cat04.html#a8) | Create Calendar Event | 3 | 2/6 | 🟡 | [ ] | |
| a9 | [Cancel All Events](acoes-highlevel-cat04.html#a9) | Cancel All Events | 2 | 1/6 | 🟡 | [ ] | |
| a10 | [Call Workflow (Chamar outro fluxo)](acoes-highlevel-cat04.html#a10) | Call Another Workflow | 3 | 3/6 | 🟡 | [ ] | |
| a11 | [Adicionar a Workflow](acoes-highlevel-cat04.html#a11) | Add to Workflow | 2 | 2/6 | 🔴 | [ ] | |
| a12 | [Remover de Workflow](acoes-highlevel-cat04.html#a12) | Remove from Workflow | 2 | 2/6 | 🔴 | [ ] | |
| a13 | [Remove from Current Workflow](acoes-highlevel-cat04.html#a13) | Remove from Current Workflow | 3 | 1/6 | 🟡 | [ ] | |
| a14 | [Jump to Action](acoes-highlevel-cat04.html#a14) | Jump to Action | 2 | 2/6 | 🟡 | [ ] | |
| a15 | [Stop Workflow](acoes-highlevel-cat04.html#a15) | Stop Workflow | 3 | 1/6 | 🟡 | [ ] | |
| a16 | [Restart Workflow](acoes-highlevel-cat04.html#a16) | Restart Workflow | 3 | 1/6 | 🟡 | [ ] | |
| a17 | [Split (Teste A/B)](acoes-highlevel-cat04.html#a17) | Split | 3 | 1/6 | 🟡 | [ ] | |

### CAT05 · Ação
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| a1 | [Generate Text (Texto)](acoes-highlevel-cat05.html#a1) | AI Generate Text | 3 | 3/6 | 🟢 | [ ] | |
| a2 | [Parse Image (Analisar Imagem)](acoes-highlevel-cat05.html#a2) | AI Parse Image | 3 | 2/6 | 🟡 | [ ] | |
| a3 | [Summarize Conversation](acoes-highlevel-cat05.html#a3) | Summarize Conversation | 3 | 3/6 | 🟢 | [ ] | |
| a4 | [Extract Info](acoes-highlevel-cat05.html#a4) | AI Extract Data | 2 | 1/6 | 🟡 | [ ] | |
| a5 | [Classify](acoes-highlevel-cat05.html#a5) | AI Classify | 2 | 2/6 | 🟡 | [ ] | |
| a6 | [Agente de IA](acoes-highlevel-cat05.html#a6) | AI Agent | 2 | 3/6 | 🟢 | [ ] | |
| a7 | [Atualizar Bot de IA e Status](acoes-highlevel-cat05.html#a7) | Update Conversation AI Bot and Status | 3 | 3/6 | 🟢 | [ ] | |
| a8 | [Mistral AI](acoes-highlevel-cat05.html#a8) | Mistral AI: Create Chat Completion / Create Embeddings / Analyze Image | 2 | 3/6 | 🟢 | [ ] | |
| a9 | [OpenRouter](acoes-highlevel-cat05.html#a9) | OpenRouter: Generate Response | 2 | 3/6 | 🟢 | [ ] | |

### CAT06 · Ação
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| a1 | [Atualizar Status do Agendamento](acoes-highlevel-cat06.html#a1) | Update Appointment Status | 2 | 3/6 | 🟡 | [ ] | |
| a2 | [Marcar Agendamento](acoes-highlevel-cat06.html#a2) | Book Appointment | 3 | 4/6 | 🟢 | [ ] | |
| a3 | [Criar Nota no Agendamento](acoes-highlevel-cat06.html#a3) | Create Appointment Note | 3 | 1/6 | 🟡 | [ ] | |

### CAT07 · Ação
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| a1 | [Criar Oportunidade](acoes-highlevel-cat07.html#a1) | Create Opportunity | 2 | 2/6 | 🟡 | [ ] | |
| a2 | [Atualizar Oportunidade](acoes-highlevel-cat07.html#a2) | Update Opportunity | 3 | 2/6 | 🟡 | [ ] | |
| a3 | [Mover Estágio no Pipeline](acoes-highlevel-cat07.html#a3) | Move Pipeline Stage | 3 | 2/6 | 🟡 | [ ] | |
| a4 | [Mover Entre Pipelines](acoes-highlevel-cat07.html#a4) | Move Between Pipelines | 3 | 2/6 | 🟡 | [ ] | |
| a5 | [Atualizar Status](acoes-highlevel-cat07.html#a5) | Update Opportunity Status | 3 | 3/6 | 🟢 | [ ] | |
| a6 | [Deletar Oportunidade](acoes-highlevel-cat07.html#a6) | Delete Opportunity | 3 | 2/6 | 🟡 | [ ] | |
| a7 | [Adicionar Dono à Oportunidade](acoes-highlevel-cat07.html#a7) | Add Owner to Opportunity | 3 | 2/6 | 🟡 | [ ] | |
| a8 | [Adicionar Tag à Opp](acoes-highlevel-cat07.html#a8) | Add Opportunity Tag | 3 | 3/6 | 🟢 | [ ] | |
| a9 | [Remover Tag da Opp](acoes-highlevel-cat07.html#a9) | Remove Opportunity Tag | 2 | 2/6 | 🟡 | [ ] | |
| a10 | [Adicionar Seguidores à Oportunidade](acoes-highlevel-cat07.html#a10) | Add Follower(s) to Opportunity | 4 | 3/6 | 🟢 | [ ] | |
| a11 | [Remover Seguidores da Oportunidade](acoes-highlevel-cat07.html#a11) | Remove Followers from Opportunity | 3 | 4/6 | 🟢 | [ ] | |

### CAT08 · Ação
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| a1 | [Criar Invoice](acoes-highlevel-cat08.html#a1) | Create Invoice | 4 | 3/6 | 🟢 | [ ] | |
| a2 | [Enviar Payment Link](acoes-highlevel-cat08.html#a2) | Send Payment Link | 3 | 2/6 | 🟡 | [ ] | |
| a3 | [Atualizar Status de Pagamento](acoes-highlevel-cat08.html#a3) | Update Payment Status | 3 | 3/6 | 🟢 | [ ] | |
| a4 | [Processar Reembolso](acoes-highlevel-cat08.html#a4) | Process Refund | 4 | 2/6 | 🟡 | [ ] | |
| a5 | [Cancelar Subscription](acoes-highlevel-cat08.html#a5) | Cancel Subscription | 3 | 3/6 | 🟢 | [ ] | |

### CAT09 · Ação
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| a1 | [Adicionar a Campanha](acoes-highlevel-cat09.html#a1) | Add to Campaign | 3 | 2/6 | 🟡 | [ ] | |
| a2 | [Remover de Campanha](acoes-highlevel-cat09.html#a2) | Remove from Campaign | 3 | 3/6 | 🟢 | [ ] | |
| a3 | [Adicionar à Audiência Facebook](acoes-highlevel-cat09.html#a3) | Add to FB Audience | 3 | 2/6 | 🟡 | [ ] | |
| a4 | [Remover de Audiência FB](acoes-highlevel-cat09.html#a4) | Remove from FB Audience | 3 | 2/6 | 🟡 | [ ] | |
| a5 | [Adicionar ao Smart List](acoes-highlevel-cat09.html#a5) | Add to Smart List | 2 | 2/6 | 🟡 | [ ] | |

### CAT10 · Ação
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| a1 | [Adicionar ao Gerenciador de Afiliados](acoes-highlevel-cat10.html#a1) | Add to Affiliate Manager | 2 | 3/6 | 🟢 | [ ] | |
| a2 | [Adicionar Afiliado a Campanha](acoes-highlevel-cat10.html#a2) | Add Affiliate to Campaign | 3 | 2/6 | 🟡 | [ ] | |
| a3 | [Remover Afiliado de Campanha](acoes-highlevel-cat10.html#a3) | Remove Affiliate from Campaign | 2 | 2/6 | 🟡 | [ ] | |
| a4 | [Aprovar Comissão](acoes-highlevel-cat10.html#a4) | Approve Commission | 3 | 2/6 | 🟡 | [ ] | |
| a5 | [Pagar Comissão](acoes-highlevel-cat10.html#a5) | Pay Commission | 2 | 2/6 | 🟡 | [ ] | |
| a6 | [Atualizar Custom Field do Afiliado](acoes-highlevel-cat10.html#a6) | Update Affiliate Custom Field | 4 | 2/6 | 🟡 | [ ] | |

### CAT11 · Ação
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| a1 | [Conceder Acesso à Oferta](acoes-highlevel-cat11.html#a1) | Grant Offer Access | 3 | 2/6 | 🟡 | [ ] | |
| a2 | [Remover Acesso à Oferta](acoes-highlevel-cat11.html#a2) | Remove Offer Access | 3 | 2/6 | 🟡 | [ ] | |

### CAT12 · Ação
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| a1 | [Tocar Mensagem (Say/Play)](acoes-highlevel-cat12.html#a1) | Say or Play Message | 3 | 3/6 | 🟢 | [ ] | |
| a2 | [Menu IVR](acoes-highlevel-cat12.html#a2) | IVR Menu | 2 | 1/6 | 🟡 | [ ] | |
| a3 | [Coletar Input](acoes-highlevel-cat12.html#a3) | Gather Input | 2 | 3/6 | 🟢 | [ ] | |
| a4 | [Transferir Ligação](acoes-highlevel-cat12.html#a4) | Transfer Call | 2 | 3/6 | 🟢 | [ ] | |
| a5 | [Encerrar Chamada](acoes-highlevel-cat12.html#a5) | Hangup Call | 2 | 1/6 | 🟡 | [ ] | |

### CAT13 · Ação
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| a1 | [Conceder Acesso a Grupo](acoes-highlevel-cat13.html#a1) | Grant Group Access | 3 | 2/6 | 🟡 | [ ] | |
| a2 | [Remover Acesso a Grupo](acoes-highlevel-cat13.html#a2) | Revoke Group Access | 3 | 2/6 | 🟡 | [ ] | |
| a3 | [Conceder Acesso a Canal Privado](acoes-highlevel-cat13.html#a3) | Grant Private Channel Access | 3 | 2/6 | 🟡 | [ ] | |
| a4 | [Remover Acesso a Canal Privado](acoes-highlevel-cat13.html#a4) | Revoke Private Channel Access | 4 | 2/6 | 🟡 | [ ] | |
| a5 | [Atribuir Nível na Classificação](acoes-highlevel-cat13.html#a5) | Assign Leaderboard Level | 4 | 2/6 | 🟡 | [ ] | |
| a6 | [Publicar na Comunidade](acoes-highlevel-cat13.html#a6) | Post to Community | 3 | 2/6 | 🟡 | [ ] | |
| a7 | [Conceder Pontos na Classificação](acoes-highlevel-cat13.html#a7) | Grant Community Group Leaderboard Points | 3 | 2/6 | 🟡 | [ ] | |

### CAT14 · Ação
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| a1 | [Emitir Certificado](acoes-highlevel-cat14.html#a1) | Issue Certificate | 4 | 3/6 | 🟢 | [ ] | |

### CAT15 · Contatos Google
| # | Nome (PT) | Nome (EN) | Click panel | HL panel | Conf. | Verificar | Notas |
|---|-----------|-----------|------------:|---------:|:-----:|:---------:|-------|
| a1 | [Criar Contato Google](acoes-highlevel-cat15.html#a1) | Create Google Contact | 0 | — | 🔴 | [ ] | |
| a2 | [Atualizar Contato Google](acoes-highlevel-cat15.html#a2) | Update Google Contact | 0 | — | 🔴 | [ ] | |
| a3 | [Buscar Contato Google](acoes-highlevel-cat15.html#a3) | Find Google Contact | 0 | — | 🔴 | [ ] | |
| a4 | [Buscar ou Criar Contato Google](acoes-highlevel-cat15.html#a4) | Find or Create Google Contact | 2 | — | 🟡 | [ ] | |
| a5 | [Criar Grupo Google](acoes-highlevel-cat15.html#a5) | Create Google Contact Group | 0 | — | 🔴 | [ ] | |
| a6 | [Adicionar a Grupos Google](acoes-highlevel-cat15.html#a6) | Add to Google Groups | 2 | — | 🔴 | [ ] | |
