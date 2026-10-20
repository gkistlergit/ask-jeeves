#!/bin/bash
# Usage: scripts/ingest-code.sh <ST> <edition> <download folder or file>
# Converts an official state-code download (left where it is) to text in Sources/<ST>/<edition>/text and records it in Sources/MANIFEST.md.
set -euo pipefail
[ $# -eq 3 ] || { echo "usage: $0 <ST> <edition> <path>" >&2; exit 2; }
st=$(printf '%s' "$1" | tr '[:lower:]' '[:upper:]'); ed=$2; src=$3
[[ "$st" =~ ^[A-Z]{2}$ ]] || { echo "state must be two letters" >&2; exit 2; }
[[ "$ed" =~ ^[A-Za-z0-9._-]+$ ]] || { echo "edition must be letters, digits, . _ -" >&2; exit 2; }
root=$(cd "$(dirname "$0")/.." && pwd)
lib="$root/Sources"; dest="$lib/$st/$ed"; txt="$dest/text"
mkdir -p "$txt"
raw=$(cd "$(dirname "$src")" && pwd)/$(basename "$src")
# expand any zip archives into a scratch folder next to the text
if [ -f "$raw" ] && [[ "$raw" == *.zip ]]; then unzip -oq "$raw" -d "$dest/unzipped"; raw="$dest/unzipped"; fi
pdf2txt="$root/scripts/pdf2txt.swift"
n=0
while IFS= read -r -d '' f; do
  base=$(basename "${f%.*}"); out="$txt/$base.txt"
  case "${f##*.}" in
    html|htm|doc|docx|rtf) textutil -convert txt -output "$out" "$f" >/dev/null 2>&1 && n=$((n+1)) ;;
    pdf) [ -e "$out" ] || { swift "$pdf2txt" "$f" "$out" >/dev/null 2>&1 && n=$((n+1)); } ;;
    xml|txt) cp "$f" "$out"; n=$((n+1)) ;;
  esac
done < <(find "$raw" -type f \( -iname '*.html' -o -iname '*.htm' -o -iname '*.doc' -o -iname '*.docx' -o -iname '*.rtf' -o -iname '*.pdf' -o -iname '*.xml' -o -iname '*.txt' \) -print0)
fmt=$(find "$raw" -type f | sed 's/.*\.//' | tr '[:upper:]' '[:lower:]' | sort -u | paste -sd, -)
printf '| %s | %s | %s | %s | %s | %s |\n' "$st" "$ed" "$raw" "$(date +%F)" "$fmt" "$n" >> "$lib/MANIFEST.md"
echo "$st $ed: $n text files in $txt"
