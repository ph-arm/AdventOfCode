#!/usr/bin/env bash
# Decrypt every year's puzzle input back to plaintext with age.
#
# Operates across ALL years: AdventOfCode20*/day_*/input.txt.age -> input.txt.
# Private key is taken from $AGE_SECRET_KEY (as used in CI) or the local
# age-key.txt (gitignored).
set -euo pipefail

cd "$(dirname "$0")"

KEY_FILE="age-key.txt"

command -v age >/dev/null 2>&1 || { echo "error: 'age' not found — install with: brew install age"; exit 1; }

identity=()
tmpkey=""
if [[ -n "${AGE_SECRET_KEY:-}" ]]; then
    tmpkey="$(mktemp)"
    printf '%s\n' "$AGE_SECRET_KEY" > "$tmpkey"
    identity=(-i "$tmpkey")
elif [[ -f "$KEY_FILE" ]]; then
    identity=(-i "$KEY_FILE")
else
    echo "error: no private key — set \$AGE_SECRET_KEY or provide $KEY_FILE"
    exit 1
fi
trap '[[ -n "$tmpkey" ]] && rm -f "$tmpkey"' EXIT

shopt -s nullglob
count=0
for enc in AdventOfCode20*/day_*/input.txt.age; do
    age -d "${identity[@]}" -o "${enc%.age}" "$enc"
    echo "  decrypted $enc"
    count=$((count + 1))
done
echo "Done. Decrypted $count file(s) across all years."
