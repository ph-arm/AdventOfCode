#!/usr/bin/env bash
# Encrypt every year's puzzle input with age.
#
# Operates across ALL years: AdventOfCode20*/day_*/input.txt -> input.txt.age.
# Recipient (public key) is read from .github/age-public-key.txt (committed).
# Raw input.txt stays gitignored; only the *.age files are committed.
#
# Usage:
#   ./encrypt_inputs.sh            # (re)encrypt every input with the current key
#   ./encrypt_inputs.sh --new-key  # rotate: generate a fresh key pair, update
#                                  # .github/age-public-key.txt, re-encrypt all,
#                                  # then print the new private key to store as
#                                  # the GitHub Actions secret AGE_SECRET_KEY.
set -euo pipefail

cd "$(dirname "$0")"

PUB_FILE=".github/age-public-key.txt"
KEY_FILE="age-key.txt"

command -v age >/dev/null 2>&1 || { echo "error: 'age' not found — install with: brew install age"; exit 1; }

if [[ "${1:-}" == "--new-key" ]]; then
    command -v age-keygen >/dev/null 2>&1 || { echo "error: 'age-keygen' not found — install with: brew install age"; exit 1; }
    echo "Generating a new age key pair -> $KEY_FILE"
    age-keygen -o "$KEY_FILE" 2>/dev/null
    chmod 600 "$KEY_FILE"
    age-keygen -y "$KEY_FILE" > "$PUB_FILE"
    echo "Updated public recipient in $PUB_FILE"
fi

[[ -f "$PUB_FILE" ]] || { echo "error: $PUB_FILE missing — run with --new-key to create one"; exit 1; }
recipient="$(tr -d '[:space:]' < "$PUB_FILE")"
echo "Recipient: $recipient"

shopt -s nullglob
count=0
for input in AdventOfCode20*/day_*/input.txt; do
    age -e -r "$recipient" -o "${input}.age" "$input"
    echo "  encrypted $input"
    count=$((count + 1))
done
echo "Done. Encrypted $count input(s) across all years."

if [[ "${1:-}" == "--new-key" ]]; then
    echo
    echo "New PRIVATE key — keep it safe and set it as the GitHub secret AGE_SECRET_KEY:"
    grep '^AGE-SECRET-KEY-' "$KEY_FILE"
fi
