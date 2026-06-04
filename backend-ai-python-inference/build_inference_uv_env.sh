#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="$SCRIPT_DIR/../backend-ai-python"

cp "$BASE_DIR/pyproject.toml" "$SCRIPT_DIR/pyproject.toml"

cd "$SCRIPT_DIR"

# Generate uv.lock for inference-only image (core + inference group), using the existing pyproject.
uv sync --no-default-groups --group inference
