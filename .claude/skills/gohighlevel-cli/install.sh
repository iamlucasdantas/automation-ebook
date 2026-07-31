#!/usr/bin/env bash
# Instalador do GoHighLevel CLI: cria .venv, instala o pacote e valida o setup.
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")"

PY=${PYTHON:-python3}

echo "→ verificando python..."
"$PY" -c "import sys; assert sys.version_info >= (3, 10), 'requer python 3.10+'" || {
  echo "  Python 3.10+ é obrigatório. Instale e rode de novo (ou use PYTHON=/caminho/python3.11 ./install.sh)." >&2
  exit 1
}

if [ ! -d .venv ]; then
  echo "→ criando .venv ..."
  "$PY" -m venv .venv
fi

echo "→ instalando pacote ..."
# shellcheck disable=SC1091
source .venv/bin/activate
pip install --upgrade pip >/dev/null
pip install -e . >/dev/null

chmod +x ghl

if [ ! -f .env ]; then
  echo "→ criando .env a partir de .env.example ..."
  cp .env.example .env
  chmod 600 .env
  echo
  echo "  ⚠  Edite o .env agora: GHL_API_KEY e GHL_LOCATION_ID são obrigatórios."
fi

echo
echo "✓ instalado."
echo
echo "Próximos passos:"
echo "  1. Edite .env  (GHL_API_KEY, GHL_LOCATION_ID)"
echo "  2. Valide:     ./ghl doctor"
echo "  3. Teste:      ./ghl contacts list --limit 5"
echo "  4. Opcional:   carregue chrome-extension/ no Chrome para capturar o"
echo "                 token Firebase e liberar a criação de workflows."
