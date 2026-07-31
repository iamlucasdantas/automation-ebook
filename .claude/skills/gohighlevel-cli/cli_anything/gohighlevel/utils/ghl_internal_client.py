"""Cliente da API interna do GoHighLevel (backend.leadconnectorhq.com).

A API pública é somente-leitura para workflows. Para CRIAR ou ATUALIZAR
workflow, gatilho e pasta, é preciso falar com o mesmo backend que a interface
web usa — autenticado por um ID token do Firebase, derivado do refresh token
da sessão do navegador.

AVISO: esta é uma API não documentada e não suportada pela HighLevel. Pode
mudar sem aviso. Todo comando que depende dela é gated por --experimental.

Variáveis de ambiente:
    GHL_FIREBASE_REFRESH_TOKEN  (obrigatória)  capturada pela extensão Chrome
    GHL_FIREBASE_API_KEY        (obrigatória)  capturada pela extensão Chrome
    GHL_INTERNAL_API_BASE       (opcional)     default backend.leadconnectorhq.com
"""
from __future__ import annotations

import json
import os
import random
import threading
import time
from pathlib import Path
from typing import Any

import requests

from cli_anything.gohighlevel.utils import ghl_client

DEFAULT_INTERNAL_BASE = "https://backend.leadconnectorhq.com"
SECURETOKEN_URL = "https://securetoken.googleapis.com/v1/token"
CACHE_PATH = Path.home() / ".ghl-cli" / "firebase_token.json"

TIMEOUT = int(os.environ.get("GHL_TIMEOUT", "30"))
MAX_RETRIES = int(os.environ.get("GHL_MAX_RETRIES", "4"))
RETRY_STATUS = {408, 429, 500, 502, 503, 504}

_SETUP_HINT = (
    "Configure o acesso à API interna:\n"
    "  1. Carregue chrome-extension/ como extensão sem empacotamento no Chrome\n"
    "  2. Abra sua conta GHL logada e clique no ícone da extensão\n"
    "  3. Clique em 'Capturar token' e depois em 'Copiar'\n"
    "  4. Cole no .env:  GHL_FIREBASE_REFRESH_TOKEN=...  e  GHL_FIREBASE_API_KEY=..."
)


class InternalAuthError(RuntimeError):
    """Falha de autenticação na API interna."""


class TokenManager:
    """Troca o refresh token do Firebase por um ID token de vida curta.

    O ID token dura ~1h. É cacheado em disco (0600) e renovado sob demanda,
    de forma thread-safe — o CampaignBuilder cria workflows em paralelo.
    """

    def __init__(self, refresh_token: str | None = None, api_key: str | None = None):
        ghl_client.load_env()
        self.refresh_token = (
            refresh_token or os.environ.get("GHL_FIREBASE_REFRESH_TOKEN", "")
        ).strip()
        self.api_key = (
            api_key or os.environ.get("GHL_FIREBASE_API_KEY", "")
        ).strip()

        missing = []
        if not self.refresh_token:
            missing.append("GHL_FIREBASE_REFRESH_TOKEN")
        if not self.api_key:
            missing.append("GHL_FIREBASE_API_KEY")
        if missing:
            raise InternalAuthError(f"Faltando: {', '.join(missing)}.\n{_SETUP_HINT}")

        self._lock = threading.Lock()
        self._id_token: str | None = None
        self._expires_at: float = 0.0
        self._load_cache()

    # -- cache -------------------------------------------------------------

    def _cache_key(self) -> str:
        return self.refresh_token[-24:]

    def _load_cache(self) -> None:
        try:
            payload = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return
        if payload.get("key") != self._cache_key():
            return
        self._id_token = payload.get("id_token")
        try:
            self._expires_at = float(payload.get("expires_at", 0))
        except (TypeError, ValueError):
            self._expires_at = 0.0

    def _save_cache(self) -> None:
        try:
            CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
            CACHE_PATH.write_text(
                json.dumps({
                    "key": self._cache_key(),
                    "id_token": self._id_token,
                    "expires_at": self._expires_at,
                }),
                encoding="utf-8",
            )
            os.chmod(CACHE_PATH, 0o600)
        except OSError:
            pass

    # -- token -------------------------------------------------------------

    def get_token(self, force_refresh: bool = False) -> str:
        with self._lock:
            # margem de 5 min para não usar token quase expirado
            if not force_refresh and self._id_token and time.time() < self._expires_at - 300:
                return self._id_token
            return self._refresh()

    def _refresh(self) -> str:
        resp = requests.post(
            SECURETOKEN_URL,
            params={"key": self.api_key},
            data={"grant_type": "refresh_token", "refresh_token": self.refresh_token},
            timeout=TIMEOUT,
        )
        if resp.status_code != 200:
            try:
                detail = resp.json().get("error", {}).get("message", "")
            except Exception:  # noqa: BLE001
                detail = resp.text[:200]
            raise InternalAuthError(
                f"Falha ao renovar o token do Firebase ({resp.status_code}): {detail}\n"
                "O refresh token expira quando você desloga do GHL. "
                f"Capture um novo.\n{_SETUP_HINT}"
            )
        payload = resp.json()
        self._id_token = payload.get("id_token") or payload.get("access_token")
        if not self._id_token:
            raise InternalAuthError("Resposta do Firebase sem id_token.")
        try:
            expires_in = int(payload.get("expires_in", 3600))
        except (TypeError, ValueError):
            expires_in = 3600
        self._expires_at = time.time() + expires_in
        self._save_cache()
        return self._id_token


class InternalGHLClient:
    """Chamadas à API interna do GHL. Thread-safe."""

    def __init__(self, token_manager: TokenManager, location_id: str,
                 base_url: str | None = None):
        self.tokens = token_manager
        self.location_id = location_id
        self.base_url = (
            base_url or os.environ.get("GHL_INTERNAL_API_BASE", DEFAULT_INTERNAL_BASE)
        ).rstrip("/")
        self.call_count = 0
        self._count_lock = threading.Lock()

    def _headers(self, token: str) -> dict[str, str]:
        return {
            "token-id": token,
            "channel": "APP",
            "source": "WEB_USER",
            "version": "2021-07-28",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Origin": f"https://{ghl_client.app_domain()}",
            "Referer": f"https://{ghl_client.app_domain()}/",
        }

    def request(self, method: str, path: str, body: dict[str, Any] | None = None,
                params: dict[str, Any] | None = None) -> dict:
        """Executa a chamada. Retorna dict; em erro retorna {"_error": ...}.

        O CampaignBuilder inspeciona `_error`, então não levantamos exceção
        aqui — uma falha isolada não deve derrubar a campanha inteira.
        """
        url = f"{self.base_url}{path}"
        with self._count_lock:
            self.call_count += 1

        attempt = 0
        forced_refresh = False
        while True:
            attempt += 1
            try:
                token = self.tokens.get_token(force_refresh=forced_refresh)
            except InternalAuthError as exc:
                return {"_error": str(exc)}
            forced_refresh = False

            try:
                resp = requests.request(
                    method.upper(), url, headers=self._headers(token),
                    json=body if body is not None else None,
                    params=params, timeout=TIMEOUT,
                )
            except requests.exceptions.RequestException as exc:
                if attempt > MAX_RETRIES:
                    return {"_error": f"rede: {exc}"}
                time.sleep(min(2 ** attempt, 20) + random.random())
                continue

            # token expirado no meio da execução: renova e tenta de novo
            if resp.status_code in (401, 403) and attempt <= 2:
                forced_refresh = True
                continue

            if resp.status_code in RETRY_STATUS and attempt <= MAX_RETRIES:
                time.sleep(min(2 ** attempt, 20) + random.random())
                continue

            if resp.status_code >= 400:
                return {
                    "_error": f"HTTP {resp.status_code}",
                    "_status": resp.status_code,
                    "_body": resp.text[:500],
                }

            if not resp.content:
                return {"status": "ok", "statusCode": resp.status_code}
            try:
                return resp.json()
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                return {"status": "ok", "raw": resp.text}

    # -- helpers -----------------------------------------------------------

    def create_location_tag(self, tag: str) -> dict:
        """Garante que a tag existe na subconta.

        Usa a API pública (documentada e estável). Tag já existente devolve
        400/409 — tratado como sucesso.
        """
        try:
            return ghl_client.post(
                f"/locations/{self.location_id}/tags", data={"name": tag}
            )
        except requests.exceptions.HTTPError as exc:
            status = exc.response.status_code if exc.response is not None else 0
            if status in (400, 409, 422):
                return {"status": "exists", "name": tag}
            return {"_error": f"HTTP {status}", "name": tag}
        except Exception as exc:  # noqa: BLE001 — nunca derrubar o build por tag
            return {"_error": str(exc), "name": tag}

    def ping(self) -> dict:
        """Valida credenciais listando workflows pela API interna."""
        return self.request("GET", f"/workflow/{self.location_id}")
