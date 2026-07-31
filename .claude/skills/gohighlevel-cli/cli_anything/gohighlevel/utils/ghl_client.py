"""Cliente da API pública do GoHighLevel.

Camada HTTP única do CLI: autenticação por bearer token, roteamento de versão
por path, carregamento de .env, retry com backoff em 429/5xx e formatação de
saída.
"""
from __future__ import annotations

import json
import os
import random
import sys
import time
from pathlib import Path
from typing import Any

import requests

DEFAULT_BASE_URL = "https://services.leadconnectorhq.com"

# Roteamento de versão por prefixo de path — endpoints do GHL exigem versões
# diferentes no header "Version".
VERSION_MAP = {
    "/conversations/": "2021-04-15",
    "/calendars/": "2021-04-15",
    "/contacts/": "2021-07-28",
    "/opportunities/": "2021-07-28",
    "/workflows/": "2021-07-28",
    "/campaigns/": "2021-07-28",
    "/invoices/": "2021-07-28",
    "/payments/": "2021-07-28",
    "/emails/": "2021-07-28",
    "/forms/": "2021-07-28",
    "/locations/": "2021-07-28",
    "/social-media-posting/": "2021-07-28",
    "/proposals/": "2021-07-28",
    "/users/": "2021-07-28",
    "/businesses/": "2021-07-28",
}
DEFAULT_VERSION = "2021-07-28"

# Retry
MAX_RETRIES = int(os.environ.get("GHL_MAX_RETRIES", "4"))
TIMEOUT = int(os.environ.get("GHL_TIMEOUT", "30"))
RETRY_STATUS = {408, 429, 500, 502, 503, 504}

_ENV_LOADED = False


# ---------------------------------------------------------------------------
# Carregamento de .env (sem dependência externa)
# ---------------------------------------------------------------------------

def _candidate_env_paths() -> list[Path]:
    here = Path(__file__).resolve()
    # utils/ -> gohighlevel/ -> cli_anything/ -> raiz do projeto
    project_root = here.parents[3]
    return [
        Path.cwd() / ".env",
        project_root / ".env",
        Path.home() / ".ghl-cli" / ".env",
    ]


def load_env(override: bool = False) -> None:
    """Carrega o primeiro .env encontrado. Idempotente."""
    global _ENV_LOADED
    if _ENV_LOADED and not override:
        return
    for path in _candidate_env_paths():
        if not path.is_file():
            continue
        try:
            for raw in path.read_text(encoding="utf-8").splitlines():
                line = raw.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                key = key.strip()
                if key.startswith("export "):
                    key = key[len("export "):].strip()
                value = value.strip().strip('"').strip("'")
                # variável exportada vazia conta como não definida — senão um
                # `export GHL_API_KEY=` no shell silencia o .env inteiro
                if override or not os.environ.get(key, "").strip():
                    os.environ[key] = value
        except OSError:
            continue
        break
    _ENV_LOADED = True


def _die(message: str) -> None:
    print(f"Erro: {message}", file=sys.stderr)
    sys.exit(1)


# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------

def base_url() -> str:
    load_env()
    return os.environ.get("GHL_API_BASE", DEFAULT_BASE_URL).rstrip("/")


def app_domain() -> str:
    """Domínio do app (white label). Usado para montar links clicáveis."""
    load_env()
    return os.environ.get("GHL_APP_DOMAIN", "app.gohighlevel.com").strip().rstrip("/")


def _version_for_path(path: str) -> str:
    for prefix, version in VERSION_MAP.items():
        if path.startswith(prefix):
            return version
    return DEFAULT_VERSION


def _get_token() -> str:
    load_env()
    token = os.environ.get("GHL_API_KEY", "").strip()
    if not token:
        _die(
            "GHL_API_KEY não definida.\n"
            "  Crie um Private Integration Token em: Settings > Private Integrations\n"
            "  e coloque no .env:  GHL_API_KEY=pit-..."
        )
    return token


def _get_location_id() -> str:
    load_env()
    loc = os.environ.get("GHL_LOCATION_ID", "").strip()
    if not loc:
        _die(
            "GHL_LOCATION_ID não definida.\n"
            "  É o ID longo que aparece na URL da subconta:\n"
            "  https://app.../location/<GHL_LOCATION_ID>/dashboard\n"
            "  Defina no .env ou passe --location-id."
        )
    return loc


def _headers(version: str | None = None, path: str = "") -> dict[str, str]:
    return {
        "Authorization": f"Bearer {_get_token()}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Version": version or _version_for_path(path),
    }


# ---------------------------------------------------------------------------
# Núcleo HTTP
# ---------------------------------------------------------------------------

def _clean_params(params: dict[str, Any] | None) -> dict[str, Any] | None:
    """Remove chaves None — o GHL rejeita 'param=None' como string."""
    if not params:
        return None
    return {k: v for k, v in params.items() if v is not None}


def request(
    method: str,
    path: str,
    params: dict[str, Any] | None = None,
    data: dict[str, Any] | None = None,
    version: str | None = None,
) -> dict:
    """Executa a request com retry/backoff. Levanta HTTPError em erro final."""
    url = f"{base_url()}{path}"
    headers = _headers(version, path)
    params = _clean_params(params)
    attempt = 0
    while True:
        attempt += 1
        try:
            resp = requests.request(
                method.upper(), url, headers=headers, params=params,
                json=data if data is not None else None, timeout=TIMEOUT,
            )
        except requests.exceptions.RequestException:
            if attempt > MAX_RETRIES:
                raise
            time.sleep(min(2 ** attempt, 20) + random.random())
            continue

        if resp.status_code in RETRY_STATUS and attempt <= MAX_RETRIES:
            retry_after = resp.headers.get("Retry-After")
            try:
                delay = float(retry_after) if retry_after else min(2 ** attempt, 20)
            except ValueError:
                delay = min(2 ** attempt, 20)
            time.sleep(delay + random.random())
            continue

        resp.raise_for_status()
        if not resp.content:
            return {"status": "ok", "statusCode": resp.status_code}
        try:
            return resp.json()
        except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
            return {"status": "ok", "statusCode": resp.status_code, "raw": resp.text}


def get(path: str, params: dict[str, Any] | None = None, version: str | None = None) -> dict:
    return request("GET", path, params=params, version=version)


def post(path: str, data: dict[str, Any] | None = None,
         params: dict[str, Any] | None = None, version: str | None = None) -> dict:
    return request("POST", path, params=params, data=data or {}, version=version)


def put(path: str, data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None, version: str | None = None) -> dict:
    return request("PUT", path, params=params, data=data or {}, version=version)


def delete(path: str, data: dict[str, Any] | None = None,
           params: dict[str, Any] | None = None, version: str | None = None) -> dict:
    """DELETE com suporte a body — exigido por /contacts/{id}/tags."""
    return request("DELETE", path, params=params, data=data, version=version)


# ---------------------------------------------------------------------------
# Paginação
# ---------------------------------------------------------------------------

def search_contacts_page(body: dict[str, Any]) -> dict:
    return post("/contacts/search", data=body)


def search_contacts_all(location_id: str, filters: list[dict] | None = None,
                        page_size: int = 100, max_records: int = 1000) -> list[dict]:
    """Pagina /contacts/search usando searchAfter até max_records."""
    collected: list[dict] = []
    search_after: list = []
    while len(collected) < max_records:
        body: dict[str, Any] = {
            "locationId": location_id,
            "pageLimit": min(page_size, max_records - len(collected)),
            "filters": filters or [],
        }
        if search_after:
            body["searchAfter"] = search_after
        data = search_contacts_page(body)
        batch = data.get("contacts", [])
        if not batch:
            break
        collected.extend(batch)
        search_after = batch[-1].get("searchAfter") or []
        if not search_after:
            break
    return collected


# ---------------------------------------------------------------------------
# Formatação de saída
# ---------------------------------------------------------------------------

def format_output(data: Any, as_json: bool = False) -> str:
    if as_json:
        return json.dumps(data, indent=2, default=str, ensure_ascii=False)
    if isinstance(data, dict):
        return _format_dict(data)
    if isinstance(data, list):
        return _format_list(data)
    return str(data)


def _format_dict(d: dict, indent: int = 0) -> str:
    lines = []
    prefix = "  " * indent
    for k, v in d.items():
        if isinstance(v, dict):
            lines.append(f"{prefix}{k}:")
            lines.append(_format_dict(v, indent + 1))
        elif isinstance(v, list):
            lines.append(f"{prefix}{k}: [{len(v)} itens]")
            for i, item in enumerate(v[:5]):
                if isinstance(item, dict):
                    name = item.get("name") or item.get("title") or item.get("id", f"item {i}")
                    lines.append(f"{prefix}  - {name}")
                else:
                    lines.append(f"{prefix}  - {item}")
            if len(v) > 5:
                lines.append(f"{prefix}  ... e mais {len(v) - 5}")
        else:
            lines.append(f"{prefix}{k}: {v}")
    return "\n".join(lines)


def _format_list(items: list, indent: int = 0) -> str:
    lines = []
    prefix = "  " * indent
    for i, item in enumerate(items):
        if isinstance(item, dict):
            name = item.get("name") or item.get("title") or item.get("id", f"item {i}")
            lines.append(f"{prefix}{i + 1}. {name}")
            for k, v in item.items():
                if k not in ("name", "title") and not isinstance(v, (dict, list)):
                    lines.append(f"{prefix}   {k}: {v}")
        else:
            lines.append(f"{prefix}{i + 1}. {item}")
    return "\n".join(lines)
