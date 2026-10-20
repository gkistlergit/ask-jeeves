# Live device location: what tool exists
Type: research
Status: resolved
Blocked by:
Findings: research/07-live-location.md

## Question

In Claude Code (CLI and desktop app), what tool, if any, can get the user's live device location with their consent? Options might include a desktop-app tool, an Artifact location capability, macOS CoreLocation through a CLI helper, or IP geolocation (approximate and network-based, which needs a disclosure). Which is free, needs no install from an untrusted source, and returns only a city or ZIP?

## Answer

See `research/07-live-location.md` (research plus an independent verification pass, 2026-10-20: 22 claims confirmed, 6 corrected, 11 UNVERIFIED).

- **Primary:** a "Jeeves Location" Shortcut that Grant builds once (Get Current Location, then City and ZIP), run with `shortcuts run 'Jeeves Location' --output-path -`. Consent comes twice: AskUserQuestion first, then the Shortcuts Allow Once dialog at run time. Untested: whether that dialog appears when the shortcut runs from the CLI.
- **Fallback:** ip-api's free tier, disclosed as approximate. It's plain HTTP only and non-commercial, and WebFetch can't reach it, so it has to be called with `curl`.
- **Always offer typed entry.** A CoreLocation `swift` script won't work: it gets no prompt without an Info.plist.
- Claude Code and the desktop app have no location tool, and this account's Artifact runtime has no location capability. That's per the current docs; an absence can't be proven.
