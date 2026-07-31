# GoHighLevel CLI

Interface de linha de comando para o GoHighLevel — contatos, oportunidades, calendários, conversas, workflows, custom fields, formulários, faturas, documentos e usuários. Feita para ser dirigida por humano no terminal ou por um agente (Claude Code) via skill.

Versão 2.1.0.

---

## Instalação

Requisitos: **Python 3.10+** e uma subconta GHL.

```bash
cd gohighlevel-cli-skill
./install.sh
```

O instalador cria `.venv/`, instala o pacote em modo editável e copia `.env.example` → `.env` com permissão 600.

Preencha o `.env`:

```env
GHL_API_KEY=pit-xxxxxxxx-...      # Settings > Private Integrations
GHL_LOCATION_ID=SUA_LOCATION_ID   # ID longo da URL /location/<ID>/dashboard
GHL_TIMEZONE=America/Sao_Paulo
GHL_CURRENCY=BRL
```

Valide antes de confiar no CLI:

```bash
./ghl doctor
```

O `doctor` testa credenciais, conectividade e **o escopo real de cada grupo de endpoint**. Escopo faltando no Private Integration Token é a causa nº 1 de erro 403 no meio de uma operação — melhor descobrir aqui.

---

## Uso rápido

```bash
# Contatos
./ghl --json contacts list --limit 50
./ghl --json contacts list --all --max-records 500
./ghl contacts search "joao@empresa.com"
./ghl contacts create --email lead@empresa.com --first-name Ana --tag lead-quente
./ghl contacts add-tag <contact_id> lead-quente
./ghl contacts remove-tag <contact_id> lead-frio

# Pipeline
./ghl --json opportunities pipelines
./ghl --json opportunities list --pipeline-id <id> --status open
./ghl opportunities update <opp_id> --stage-id <stage_id> --status won

# Agenda (aceita YYYY-MM-DD, ISO 8601 ou epoch ms)
./ghl calendars slots <calendar_id> --start 2026-08-01 --end 2026-08-07
./ghl calendars book --calendar-id <id> --contact-id <id> --start 2026-08-03T14:00:00-03:00

# Conversas (o envio é por contato, não por conversa)
./ghl --json conversations list --type WhatsApp
./ghl conversations send --contact-id <id> --type WhatsApp --message "Confirmando a call."

# Configuração da subconta
./ghl locations create-custom-field --name CF_DRIVE_LINK --data-type TEXT
./ghl locations create-custom-value --name "WhatsApp Suporte" --value "+5511999999999"
./ghl locations bootstrap-fields --from-file presets/custom-fields.json --dry-run

# REPL interativo
./ghl
```

`--json` funciona na maioria dos comandos de leitura e sai limpo para `jq`.

---

## Bootstrap de subconta nova

`presets/custom-fields.json` já traz os campos de tracking (UTMs, GCLID, FBCLID) e os de orquestração (`CF_DRIVE_LINK`, `CF_CLICKUP_LINK`, `CF_NOTION_LINK`, `CF_NPS_ULTIMO`, `CF_DATA_RENOVACAO`).

```bash
./ghl locations bootstrap-fields --from-file presets/custom-fields.json --dry-run   # confere
./ghl locations bootstrap-fields --from-file presets/custom-fields.json             # cria
```

Idempotente: campo existente é pulado, não duplicado. Edite o JSON para adaptar ao nicho.

---

## Criação de workflow (experimental)

A API pública do GHL é **somente leitura** para workflows. Criar ou editar exige a API interna — a mesma que a interface web usa — autenticada por um token do Firebase.

### 1. Capturar o token

1. `chrome://extensions/` → ative o Modo desenvolvedor
2. **Carregar sem empacotamento** → selecione a pasta `chrome-extension/`
3. Abra qualquer página do GHL logada
4. Clique no ícone da extensão → **Capturar token** → **Copiar bloco .env**
5. Cole as duas linhas no seu `.env` (`GHL_FIREBASE_REFRESH_TOKEN` e `GHL_FIREBASE_API_KEY`)

Confirme com `./ghl doctor`.

### 2. Criar

```bash
# Ponte para n8n: gatilho por tag → webhook
./ghl --experimental workflows create-n8n \
  --name "Provisionamento de cliente" \
  --webhook-url https://seu-n8n/webhook/xyz \
  --tag cliente-fechado

# Montar passo a passo e depois publicar
./ghl --experimental workflows create-step --type email --name "D0 boas-vindas" \
  --subject "Bem-vindo" --body "Texto..." --output-file /tmp/wf.json
./ghl --experimental workflows create-step --type wait --name "espera" \
  --value 2 --unit days --output-file /tmp/wf.json
./ghl --experimental workflows create --name "Onboarding" --from-json /tmp/wf.json
```

Todo workflow é criado como **rascunho**. Revise e publique na interface.

> **Aviso:** `backend.leadconnectorhq.com` é uma API não documentada e não suportada pela HighLevel. Pode mudar sem aviso. Use para acelerar montagem, não como dependência de processo crítico. O refresh token expira quando você desloga do GHL — recapture quando o `doctor` acusar falha.

---

## Duas camadas de API

| API | O que faz | Autenticação |
|---|---|---|
| Pública (`services.leadconnectorhq.com`) | Tudo, menos criar/editar workflow | `GHL_API_KEY` (Private Integration Token) |
| Interna (`backend.leadconnectorhq.com`) | Criar/editar workflow, gatilho e pasta | Token Firebase, atrás de `--experimental` |

O CLI trata rate limit (100 req/10s por subconta) com retry e backoff exponencial, respeitando `Retry-After`.

---

## Uso com Claude Code

```bash
mkdir -p ~/.claude/skills/gohighlevel-cli
cp cli_anything/gohighlevel/skills/SKILL.md ~/.claude/skills/gohighlevel-cli/
ln -s "$(pwd)/ghl" ~/.local/bin/ghl    # ou adicione a pasta ao PATH
```

Em qualquer sessão, peça o que quer em português — a skill mapeia para os comandos.

---

## Estrutura

```
gohighlevel-cli-skill/
├── ghl                          # wrapper executável
├── install.sh                   # instalador
├── .env.example                 # template de configuração
├── presets/custom-fields.json   # bootstrap de subconta
│
├── cli_anything/
│   ├── gohighlevel/
│   │   ├── gohighlevel_cli.py           # comandos
│   │   ├── skills/SKILL.md              # manifesto da skill
│   │   └── utils/
│   │       ├── ghl_client.py            # API pública: .env, retry, paginação
│   │       ├── ghl_internal_client.py   # API interna: Firebase + workflows
│   │       ├── workflow_builder.py      # steps, linker, CampaignBuilder
│   │       └── repl_skin.py             # REPL
│   ├── nextcloud/               # bônus
│   └── blotato/                 # bônus
│
├── chrome-extension/            # captura do token Firebase
├── builders/                    # exemplos de sequências de e-mail
├── tests/smoke_test.py          # teste offline da camada de código
└── docs/
```

---

## Segurança

- `.env` está no `.gitignore`. **Nunca** versione.
- O refresh token do Firebase equivale à sua sessão completa do GHL. Trate como senha.
- O ID token é cacheado em `~/.ghl-cli/firebase_token.json` com permissão 600.
- A extensão só lê o IndexedDB dos domínios do GHL — não faz chamada de rede.
- Comandos destrutivos (`delete`) não pedem confirmação: use com cuidado em script.

---

## Solução de problemas

| Sintoma | Causa provável | O que fazer |
|---|---|---|
| `GHL_API_KEY não definida` | `.env` ausente ou variável exportada vazia no shell | `./ghl doctor` |
| 401 | Token inválido ou revogado | gerar novo Private Integration Token |
| 403 | Escopo faltando no token | marcar o escopo em Settings > Private Integrations |
| 422 | Payload incorreto para o endpoint | conferir campos obrigatórios; rodar com `--json` |
| 429 | Rate limit | o CLI já faz retry; reduza concorrência |
| Falha ao renovar token do Firebase | Refresh token expirado (logout no GHL) | recapturar pela extensão |
| Workflow criado mas vazio | Validação ignorada com `--force` | rodar sem `--force` e corrigir os erros apontados |
