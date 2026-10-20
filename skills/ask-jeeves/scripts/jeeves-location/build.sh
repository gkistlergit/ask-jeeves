#!/bin/zsh
# Builds and ad-hoc signs "Jeeves Location.app" next to this script, in build/ (gitignored).
# Run once per machine, and again after editing main.swift. A rebuild may make macOS ask again.
set -euo pipefail
here=${0:A:h}
app="$here/build/Jeeves Location.app"
rm -rf "$app"
mkdir -p "$app/Contents/MacOS"
cp "$here/Info.plist" "$app/Contents/Info.plist"
swiftc -O -suppress-warnings -o "$app/Contents/MacOS/JeevesLocation" "$here/main.swift"
codesign --sign - --force "$app" >/dev/null 2>&1
echo "$app"
