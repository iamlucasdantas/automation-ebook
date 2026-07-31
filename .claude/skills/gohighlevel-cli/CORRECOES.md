# Correções aplicadas — v2.1.0

Auditoria e correção do pacote original (v1.1.0). Registro do que mudou e por quê.

## Bloqueador

**`utils/ghl_internal_client.py` era um stub.** `TokenManager.__init__` e
`InternalGHLClient.__init__` levantavam `RuntimeError` na primeira linha — logo,
`workflows create`, `create-step`, `create-n8n` e os 7 builders estavam 100%
inoperantes. A criação de workflow, principal diferencial do pacote, não existia.

Reimplementado: renovação do ID token via `securetoken.googleapis.com`, cache em
disco com permissão 600 e margem de 5 min, thread-safe (o `CampaignBuilder` roda
10 workflows em paralelo), retry com backoff e reautenticação automática em
401/403.

## Erros de contrato da API

| Comando | Antes | Depois |
|---|---|---|
| `contacts remove-tag` | DELETE sem body — as tags nunca eram enviadas | DELETE com body (`api.delete` passou a suportar) |
| `opportunities list` | `locationId` em `/opportunities/search`, que exige `location_id` (snake_case) → 422 | corrigido + filtros de estágio, contato e responsável |
| `conversations send` | Enviava `conversationId`; a API envia por `contactId` | resolve o contato pela conversa automaticamente |
| `calendars slots` | Passava `YYYY-MM-DD`; o endpoint só aceita epoch ms | conversor aceita os três formatos |
| `calendars book` | Campo `selectedSlot`, inexistente na API | campos reais + `appointmentStatus` |
| `payments create-invoice` | Sem `items`, `currency`, `contactDetails`, `issueDate` → 422 | payload completo; busca dados do contato sozinho |
| `contacts list --offset` | Inteiro em `startAfterId`, que espera ID de contato | cursor correto + `--all` com paginação por `searchAfter` |
| `contacts search` | Filtrava só `firstNameLowerCase` | busca ampla (nome/email/telefone); `--field` restringe |
| `workflows create-n8n` | Tag adicionada como ação — o workflow nunca disparava | tag vira gatilho de verdade |

## Segurança e isolamento

- Removido o **fallback hardcoded para a location ID do autor original**
  (`YB8rMdFShcHGcZGW87mA`) em `ghl_client.py` e nos 6 builders. Sem
  `GHL_LOCATION_ID`, o CLI escreveria silenciosamente na subconta de terceiro.
  Agora falha com erro explícito.
- Links de workflow deixaram de apontar para o domínio white label do autor;
  passam a usar `GHL_APP_DOMAIN`.
- Extensão Chrome: removida permissão no domínio do autor.
- `.env` criado com permissão 600 pelo instalador.
- Caminhos pessoais nos builders (`~/Documents/Tech & Dev/...`) → variável
  `GHL_SEQUENCES_DIR`.

## Robustez

- **Carregamento de `.env` em Python** (`ghl_client.load_env`): antes só o
  wrapper bash exportava, então o CLI morria quando chamado por agente, cron ou
  `python -m`. Busca em cwd → raiz do projeto → `~/.ghl-cli/.env`. Variável
  exportada vazia deixou de silenciar o `.env` inteiro.
- **Rate limit:** retry com backoff exponencial + jitter em 429/5xx,
  respeitando `Retry-After`. O GHL corta em 100 req/10s e o builder é paralelo.
- `_handle_error` não quebra mais quando `e.response is None`; traduz
  401/403/422/429 em instrução acionável.
- `ctx.obj["json"]` acessado direto em 4 pontos causava `KeyError` no REPL →
  helper `_is_json`.
- `validate_campaign` era decorativa: coletava erros e criava o workflow
  quebrado assim mesmo. Agora aborta antes de tocar no GHL (`--force` ignora).
- Versão unificada (setup 1.1.0 / CLI 2.0.0 / REPL 1.0.0 → 2.1.0).
- `setup.py`: pacote raiz `cli_anything` não entrava em `find_namespace_packages`.
- `install.sh` e wrapper `ghl`: mensagens claras quando falta venv, pacote ou
  Python 3.10+.
- `import os` faltando em `email-sequences-doc-builder.py`.

## Adições

- **`ghl doctor`** — valida credenciais, conectividade e o escopo real de cada
  grupo de endpoint antes de você depender do CLI.
- **`locations create-tag` / `create-custom-field` / `create-custom-value`** —
  faltava toda a camada de configuração da subconta.
- **`locations bootstrap-fields --from-file`** — criação de custom fields em
  lote, idempotente, com `--dry-run`. Acompanha `presets/custom-fields.json`
  com UTMs, GCLID, FBCLID e os campos de orquestração.
- `users list` — para atribuição de responsável.
- Novos builders de step: `internal_notification`, `update_contact_field`,
  `add_notes`, `add_to_workflow` (workflow chaining).
- Extensão Chrome captura também a `GHL_FIREBASE_API_KEY` (extraída da chave do
  IndexedDB) e entrega o bloco `.env` pronto para colar.
- `tests/smoke_test.py` — 26 verificações offline da camada de código.
- `SKILL.md` reescrita no formato correto (a original usava a chave `triggers:`,
  fora do padrão) com regras operacionais.

## Não validado

As correções de endpoint seguem o contrato da API do GoHighLevel, mas **não
foram testadas contra uma conta real** — o ambiente de auditoria não tinha
acesso de rede a `services.leadconnectorhq.com`. Rode `./ghl doctor` como
primeiro comando.

A API interna é reverse-engineered e não suportada pela HighLevel: pode quebrar
sem aviso.
