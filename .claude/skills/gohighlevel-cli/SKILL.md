---
name: gohighlevel-cli
description: Opera o GoHighLevel pela linha de comando via CLI `ghl` — contatos, oportunidades/pipeline, calendários e agendamentos, conversas (SMS/WhatsApp/e-mail), workflows, custom fields, custom values, tags, formulários, faturas, documentos e usuários. Use sempre que a tarefa envolver ler ou alterar dados no GHL, configurar uma subconta, criar campos/tags, montar automações, ou auditar pipeline e conversas. Também cria workflows via API interna quando o token Firebase está configurado.
---

# GoHighLevel CLI

CLI para o GoHighLevel. Toda operação é um comando `ghl`. Use `--json` sempre que for consumir a saída programaticamente.

## Antes de qualquer coisa

```bash
ghl doctor          # valida token, location, escopos e API interna
```

Se `doctor` acusar falha de escopo, o Private Integration Token não tem a permissão do endpoint — o usuário precisa marcar o escopo em Settings > Private Integrations. Não tente contornar.

Requisitos: Python 3.10+, `GHL_API_KEY` e `GHL_LOCATION_ID` no `.env` da raiz do projeto.

## Duas camadas de API

| Camada | Cobre | Autenticação |
|---|---|---|
| Pública (`services.leadconnectorhq.com`) | Tudo, exceto criar/editar workflow (workflow é GET-only) | `GHL_API_KEY` |
| Interna (`backend.leadconnectorhq.com`) | Criação e edição de workflow, gatilho e pasta | Token Firebase, atrás da flag `--experimental` |

A camada interna é **não documentada e não suportada** pela HighLevel. Pode quebrar sem aviso. Nunca use em produção sem revisar o resultado na interface.

## Opções globais

- `--json` — saída JSON (use por padrão em automação)
- `--location-id <ID>` — sobrescreve a subconta da chamada
- `--experimental` — libera comandos que usam a API interna
- `--version`, `--help`

## Grupos de comandos

| Grupo | Comandos |
|---|---|
| `contacts` | list, get, create, update, delete, search, add-tag, remove-tag |
| `opportunities` | list, get, create, update, delete, pipelines |
| `calendars` | list, get, slots, appointments, book, groups |
| `conversations` | list, get, messages, get-email, send |
| `workflows` | list, enroll, remove, create*, create-step*, create-n8n* |
| `locations` | get, search, tags, custom-fields, custom-values, create-tag, create-custom-field, create-custom-value, bootstrap-fields |
| `documents` | list, templates, send, send-template |
| `payments` | transactions, orders, invoices, create-invoice |
| `forms` | list, submissions |
| `social` | accounts, posts, create-post |
| `users` | list |
| `doctor` | diagnóstico de setup |

`*` exige `--experimental`.

## Receitas

```bash
# Contatos
ghl --json contacts list --limit 50
ghl --json contacts list --all --max-records 500          # pagina sozinho
ghl contacts search "joao@empresa.com"                     # nome, email ou telefone
ghl contacts create --email lead@empresa.com --first-name Ana --tag lead-quente
ghl contacts add-tag <contact_id> tag-um tag-dois
ghl contacts remove-tag <contact_id> tag-um

# Pipeline
ghl --json opportunities pipelines                          # pegue pipelineId/stageId aqui primeiro
ghl --json opportunities list --pipeline-id <id> --status open
ghl opportunities update <opp_id> --stage-id <stage_id> --status won

# Agenda (datas aceitam YYYY-MM-DD, ISO 8601 ou epoch ms)
ghl --json calendars list
ghl calendars slots <calendar_id> --start 2026-08-01 --end 2026-08-07
ghl calendars book --calendar-id <id> --contact-id <id> --start 2026-08-03T14:00:00-03:00

# Conversas — o envio é por contato, não por conversa
ghl --json conversations list --type WhatsApp --limit 20
ghl conversations send --contact-id <id> --type WhatsApp --message "Confirmando nossa call."
ghl conversations send --conversation-id <id> --type SMS --message "..."   # resolve o contato

# Configuração da subconta
ghl locations create-custom-field --name CF_DRIVE_LINK --data-type TEXT
ghl locations create-custom-value --name "WhatsApp Suporte" --value "+5511999999999"
ghl locations bootstrap-fields --from-file presets/custom-fields.json --dry-run
ghl --json locations custom-fields

# Workflows
ghl --json workflows list
ghl workflows enroll --contact-id <id> --workflow-id <id>
ghl --experimental workflows create-n8n --name "Ponte n8n" --webhook-url https://... --tag cliente-fechado
```

## Regras de operação

1. **IDs primeiro.** Nunca invente `pipelineId`, `stageId`, `calendarId` ou `workflowId`. Liste antes (`opportunities pipelines`, `calendars list`, `workflows list`) e use o ID retornado.
2. **Workflows nascem como rascunho.** O builder nunca publica. Depois de criar, mande o usuário revisar e publicar na interface.
3. **`bootstrap-fields` é idempotente** — campos já existentes são pulados. Rode com `--dry-run` antes.
4. **Rate limit:** 100 requisições por 10s por subconta. Em lote, prefira `--all` (que já pagina com controle) a laços de chamadas.
5. **Destrutivos** (`contacts delete`, `opportunities delete`) exigem confirmação explícita do usuário antes de executar.
6. **Nunca imprima o conteúdo do `.env`** nem os tokens em log ou resposta.
7. Erro 401 = token inválido; 403 = falta escopo; 422 = payload incorreto; 429 = rate limit. O CLI já faz retry com backoff em 429 e 5xx.

## REPL

`ghl` sem argumentos abre o shell interativo com autocomplete. Em automação, prefira comandos diretos — o REPL é para uso humano.
