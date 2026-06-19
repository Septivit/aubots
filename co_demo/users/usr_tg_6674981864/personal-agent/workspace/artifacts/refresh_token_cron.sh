#!/bin/bash
set -e
WORKSPACE="/var/lib/private/teamon-clean/co_demo/users/usr_tg_6674981864/personal-agent/workspace"
SA_FILE="$WORKSPACE/inbox/sheetsms-470810-d89dad35a23c.json"
SCRIPT="$WORKSPACE/artifacts/gsheets_token_refresh.py"
export GOOGLE_SHEETS_SA=$(base64 -w0 "$SA_FILE")
python3 "$SCRIPT" | grep '^STATUS:'
