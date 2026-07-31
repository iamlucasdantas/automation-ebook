"""Teste de fumaça offline — valida a camada de código sem tocar a API do GHL.

Uso:
    .venv/bin/python tests/smoke_test.py

Cobre: parsing de datas, builders de step, linker, validação de campanha,
carregamento de .env e registro de todos os comandos do CLI.
"""
from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

falhas: list[str] = []


def check(nome: str, condicao: bool, detalhe: str = "") -> None:
    if condicao:
        print(f"  ✓ {nome}")
    else:
        print(f"  ✗ {nome} {detalhe}")
        falhas.append(nome)


print("\n1. Conversão de datas")
from datetime import datetime, timezone

from cli_anything.gohighlevel.gohighlevel_cli import _to_epoch_ms

ESPERADO = int(datetime(2026, 8, 1, tzinfo=timezone.utc).timestamp() * 1000)

check("YYYY-MM-DD vira epoch ms", _to_epoch_ms("2026-08-01") == ESPERADO,
      f"-> {_to_epoch_ms('2026-08-01')} != {ESPERADO}")
check("ISO com timezone", _to_epoch_ms("2026-08-01T00:00:00+00:00") == ESPERADO)
check("ISO com offset -03:00 respeita o fuso",
      _to_epoch_ms("2026-08-01T00:00:00-03:00") == ESPERADO + 3 * 3600 * 1000)
check("epoch ms passa direto", _to_epoch_ms(str(ESPERADO)) == ESPERADO)
check("epoch em segundos vira ms", _to_epoch_ms(str(ESPERADO // 1000)) == ESPERADO)

print("\n2. Builders de step")
from cli_anything.gohighlevel.utils import workflow_builder as wb

email = wb.email_step("teste", "Assunto", "Linha um\nLinha dois")
sms = wb.sms_step("teste", "Oi")
wait = wb.wait_step("espera", 2, "days")
tag = wb.tag_step("tag", ["lead-quente"])
hook = wb.webhook_step("n8n", "https://exemplo/webhook")
notif = wb.internal_notification_step("aviso", "Novo lead", "corpo")
campo = wb.update_field_step("grava", "CF_DRIVE_LINK", "https://drive")

check("email gera HTML", "<p style=" in email["attributes"]["body"])
check("email tem id único", email["id"] != wb.email_step("x", "y", "z")["id"])
check("wait usa unidade da API", wait["attributes"]["startAfter"]["type"] == "days")
check("tag é add_contact_tag", tag["type"] == "add_contact_tag")
check("remove tag é remove_contact_tag",
      wb.tag_step("t", ["x"], remove=True)["type"] == "remove_contact_tag")
check("webhook tem url", hook["attributes"]["url"] == "https://exemplo/webhook")
check("notificação interna é tipo verificado",
      notif["type"] in wb.VERIFIED_ACTIONS)
check("update_contact_field é tipo verificado",
      campo["type"] in wb.VERIFIED_ACTIONS)

print("\n3. Linker de steps")
linked = wb.link_steps([email, wait, sms])
check("ordem sequencial", [s["order"] for s in linked] == [0, 1, 2])
check("primeiro sem pai", linked[0]["parentKey"] is None)
check("encadeamento correto", linked[1]["parentKey"] == linked[0]["id"])
check("next aponta para o seguinte", linked[0]["next"] == linked[1]["id"])
check("último sem next", "next" not in linked[2])

print("\n4. Validação de campanha")
valida = wb.validate_campaign({"a": {"name": "X", "templates": linked}})
check("campanha válida não gera erro", valida == [], f"-> {valida}")

invalida = wb.validate_campaign({"a": {"templates": [{"type": "inexistente"}]}})
check("campanha inválida é pega", len(invalida) >= 2, f"-> {invalida}")

print("\n5. Carregamento de .env")
from cli_anything.gohighlevel.utils import ghl_client

with tempfile.TemporaryDirectory() as tmp:
    env = Path(tmp) / ".env"
    env.write_text('GHL_TESTE_SMOKE="valor-do-env"\n# comentário\nexport GHL_TESTE_2=abc\n')
    cwd = os.getcwd()
    os.chdir(tmp)
    os.environ.pop("GHL_TESTE_SMOKE", None)
    os.environ["GHL_TESTE_2"] = ""  # exportada vazia deve ser sobrescrita
    ghl_client._ENV_LOADED = False
    ghl_client.load_env()
    os.chdir(cwd)

check("lê valor com aspas", os.environ.get("GHL_TESTE_SMOKE") == "valor-do-env")
check("variável exportada vazia não bloqueia o .env",
      os.environ.get("GHL_TESTE_2") == "abc")

print("\n6. Limpeza de parâmetros")
check("None é removido dos params",
      ghl_client._clean_params({"a": 1, "b": None}) == {"a": 1})

print("\n7. Registro de comandos")
from cli_anything.gohighlevel.gohighlevel_cli import cli

grupos = set(cli.commands)
esperados = {
    "contacts", "opportunities", "calendars", "conversations", "workflows",
    "documents", "payments", "forms", "social", "locations", "users",
    "emails", "doctor",
}
check("todos os grupos registrados", esperados <= grupos,
      f"faltando: {esperados - grupos}")

sub_locations = set(cli.commands["locations"].commands)
check("comandos de configuração presentes",
      {"create-tag", "create-custom-field", "create-custom-value",
       "bootstrap-fields"} <= sub_locations)

print("\n8. Preset de custom fields")
import json
preset = Path(__file__).resolve().parents[1] / "presets" / "custom-fields.json"
dados = json.loads(preset.read_text(encoding="utf-8"))
check("preset é uma lista", isinstance(dados, list))
check("todo campo tem name e dataType",
      all(d.get("name") and d.get("dataType") for d in dados))
check("dataTypes são válidos",
      all(d["dataType"] in {
          "TEXT", "LARGE_TEXT", "NUMERICAL", "PHONE", "MONETORY", "CHECKBOX",
          "SINGLE_OPTIONS", "MULTIPLE_OPTIONS", "DATE", "TEXTBOX_LIST",
          "FILE_UPLOAD", "RADIO", "EMAIL"} for d in dados))

print()
if falhas:
    print(f"FALHOU: {len(falhas)} verificação(ões) -> {falhas}")
    sys.exit(1)
print("Todos os testes de fumaça passaram.")
