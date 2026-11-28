#!/usr/bin/env bash
# Bangun diagram, DOCX, dan PDF dari sumber. Perlu: pandoc, python-docx, LibreOffice, mmdc.
set -euo pipefail
python3 "$(dirname "$0")/build.py"
