#!/bin/zsh
# Prints "City|ZIP" (or DENIED / FAILED / GEOCODE_FAILED / TIMEOUT). Builds the app first if needed.
set -euo pipefail
here=${0:A:h}
app="$here/build/Jeeves Location.app"
[[ -d "$app" ]] || "$here/build.sh" >/dev/null
out=$(mktemp -t jeeves-location)
open -W -n --stdout "$out" --stderr /dev/null "$app"
cat "$out"
rm -f "$out"
