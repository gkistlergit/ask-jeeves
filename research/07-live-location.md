# 07: Live device location for ask-jeeves

Ticket: `.scratch/ask-jeeves/issues/07-live-location-tool.md`
Researched: 2026-10-20 (all URLs below accessed 2026-10-20). Nothing in this research requested a location or triggered a permission prompt.

## Answer

- **Primary: a one-time, hand-built macOS Shortcut run with `shortcuts run`.** It returns only `City|ZIP` to the skill. Shortcuts is built into macOS, needs no third-party install, and asks "Allow Once / Always Allow / Don't Allow" itself. The skill asks for consent first every time.
- **Fallback: IP geolocation through `curl` to ip-api.com**, limited to the `city` and `zip` fields. It's approximate (ISP or VPN exit), it sends the user's IP to a third party, and it uses plain HTTP on the free tier. Disclose all three every time.
- The current Claude Code and desktop docs describe no location tool. Absence can't be proven from docs, but there's nothing to build on. Don't build on one.

## 1. What Claude Code and the desktop app offer

| Option | Finding | Source |
|---|---|---|
| Built-in Claude Code tool | **None.** The tools reference lists every built-in tool (Agent, Artifact, AskUserQuestion, Bash, … WebFetch, WebSearch, Write). None reads location. | https://code.claude.com/docs/en/tools-reference.md |
| Docs index | No page has "location" or "geolocation" in its title or description. | https://code.claude.com/docs/llms.txt |
| Desktop app (Code tab) | Lists a browser pane, diff, terminal, file, iOS Simulator and computer use. It mentions no location tool or Location Services permission. Its only macOS permissions are Accessibility and Screen Recording, both for computer use. | https://code.claude.com/docs/en/desktop.md |
| Claude iOS app | Has a real location tool, granted through iOS Location Services with Allow once / Always allow / Don't allow. The article covers iOS only, and Team/Enterprise members can't use it. **Not available on macOS** (the article doesn't mention desktop). | https://support.claude.com/en/articles/11869619-using-claude-with-ios-apps |
| Anthropic's own location use | Claude may use the IP address to infer a coarse city/region for features like web search. You can turn this off in the privacy dashboard. A separate country/region inference can't be turned off. On surfaces like the mobile app and browser extension, location access is "managed at the device level". Last updated 2026-03-16. The article doesn't say whether the model can read this inferred location; the claim that it can't is an inference (UNVERIFIED). | https://privacy.claude.com/en/articles/11186740 |
| Artifact runtime capabilities | **No `location` capability for this account.** The artifact-capabilities skill (bundled with Claude Code 2.1.299, runtime contract 0.2.87; the installed CLI now reports 2.1.304) lists the complete set: `artifact, assets, comments, db, downloads, files, mcp, room, sample, self, user`, plus the built-in `permissions`. It says "Anything not listed is unavailable to this user", and the shipped `.d.ts` files contain no geolocation API. The skill's generic description mentions "the viewer's camera, microphone, location", so the capability may exist for other accounts or later (UNVERIFIED). Two further problems: the page's CSP lets fetch reach only the page's own origin, so it couldn't reverse-geocode, and the result would sit in a claude.ai browser tab, not in the session. | local skill text; https://code.claude.com/docs/en/artifacts.md ("Page constraints") |
| Computer use | Clicks, types and takes screenshots, and needs Accessibility and Screen Recording. It has no location feature. It could drive Maps or Shortcuts by screen, but that's slow, needs Pro/Max, and adds nothing over `shortcuts run`. | https://code.claude.com/docs/en/computer-use.md |
| Browser (Chrome extension or built-in pane) calling `navigator.geolocation` | Possible in principle, with a per-site browser prompt. Chrome resolving Wi-Fi location through Google's service is UNVERIFIED (no source cited). The result would be raw coordinates that still need geocoding. Not recommended. The desktop docs describe the browser pane's per-site prompts for Claude's actions but never mention geolocation, so whether the pane honors geolocation requests is UNVERIFIED. | none found (weak: this row is unsourced) |

## 2. Built-in macOS options (checked on this machine, nothing installed)

```
$ which swift shortcuts osascript   → /usr/bin/swift  /usr/bin/shortcuts  /usr/bin/osascript
$ sw_vers                           → macOS 27.0.1 (26A434)
$ swift --version                   → Apple Swift 6.4, arm64-apple-macosx27.0.0 (Xcode installed)
$ shortcuts list                    → Open Waze, Start Scrolling Screenshot, Proton Mail, Maxim, Proton (no location shortcut yet)
$ which CoreLocationCLI             → not found
```

### 2a. CoreLocation from a `swift` script: rejected

- `requestWhenInUseAuthorization` does nothing without an Info.plist. From the macOS 27 SDK header `CoreLocation.framework/Headers/CLLocationManager.h` (lines 484-486): "The NSLocationWhenInUseUsageDescription key must be specified in your Info.plist; otherwise, this method will do nothing". A script run with `swift loc.swift` has no Info.plist, so it gets no prompt and no location.
- A compiled binary with an embedded plist (`-Xlinker -sectcreate __TEXT __info_plist`) is how tools like CoreLocationCLI work (https://github.com/fulldecent/corelocationcli). Their README doesn't document the mechanism, so it's UNVERIFIED. It also isn't documented which process macOS attributes the grant to (the binary, Terminal, or Claude.app). Two Apple Developer Forums threads show non-app location clients misbehaving, though neither is a plain CLI stuck at `notDetermined`. Thread 840513 (2026-08) is a signed LaunchAgent app bundle stuck at `notDetermined` with no prompt; an Apple DTS engineer asks whether it's tied to a GUI app, with no resolution. Thread 124189 (2019-20) is a CLI tool that *was* granted authorization, but CoreWLAN still withheld BSSIDs; a user there guesses `locationd` keys bare binaries by executable path. No Apple reply in that one. Weak sources for this question: user reports, not Apple guidance (https://developer.apple.com/forums/thread/840513, https://developer.apple.com/forums/thread/124189).
- Reverse geocoding: `CLGeocoder` is deprecated as of macOS 26 ("Use MapKit" / "Use MKReverseGeocodingRequest", `CLGeocoder.h` lines 23 and 33 in the local SDK). A script would have to use MapKit's `MKReverseGeocodingRequest`, which also exists in the local SDK.
- Verdict: fragile, depends on Xcode, and builds an unsigned binary. Use Shortcuts instead.

### 2b. Shortcuts + `shortcuts run`: recommended

- `shortcuts run <name> [--output-path -]` writes the shortcut's output to stdout. From the local `man shortcuts` (dated 2021-09-08): `--output-path` "Can be omitted, or set to "-" for stdout". Apple's guide says a shortcut that ends with a text-producing action can return its result with `-o`, and that shortcuts which ask for input pause the command (https://support.apple.com/guide/shortcuts-mac/apd455c82f02/mac).
- Consent is per shortcut and handled by Shortcuts: "If a Privacy dialog appears requesting access to data, choose Allow Once, Always Allow, or Don't Allow". Always Allow stops future prompts. You revoke it in the shortcut's Details > Privacy (deselect Location) or with **Reset Privacy** (https://support.apple.com/guide/shortcuts-mac/apd961a4fc65/mac).
- Actions: **Get Current Location** (no input, outputs a Location) and **Get Details of Locations** (fields include City and ZIP Code). This comes from Matthew Cassinelli's action directory (https://matthewcassinelli.com/actions/get-current-location/, https://matthewcassinelli.com/actions/get-details-of-locations/), a third-party source. I didn't find an Apple page for these two actions (UNVERIFIED with Apple). The directory says Get Current Location uses "the GPS signal"; Macs have no GPS, so how it resolves on a Mac is UNVERIFIED. Field names should be confirmed in the editor when building the shortcut.
- The `shortcuts` CLI can't create a shortcut ("To create or edit a shortcut, use the Shortcuts application", man page). Grant builds it once by hand. `shortcuts sign` exists, but generating a `.shortcut` file to sign and import is UNVERIFIED and not worth it.
- UNVERIFIED, test on first run:
  - whether the Allow Once dialog appears when the shortcut is started from the CLI (rather than inside Shortcuts.app);
  - whether a Claude Code Bash sandbox, if enabled, blocks `shortcuts run`;
  - whether a Mac without GPS resolves from Wi-Fi (it needs Wi-Fi on and Location Services enabled for Shortcuts in System Settings > Privacy & Security > Location Services);
  - whether the geocode goes to Apple's servers (MapKit geocoding normally requires a network connection).

## 3. IP geolocation (fallback)

| Service | Free terms | Returns city + ZIP? | Privacy | Source |
|---|---|---|---|---|
| **ip-api.com** (recommended fallback) | Non-commercial use only. 45 req/min per IP. No key. **No HTTPS on the free endpoint** ("256-bit SSL encryption is not available for this free API"). | Yes (`city`, `zip`), and a `fields=` filter limits the response | Stores client IPs in RAM "for up to 1 minute". "We do not log requests". The no-cookies statement covers the website; the policy doesn't address cookies for the API. The policy has no effective date. | https://ip-api.com/docs/api:json, https://ip-api.com/docs/legal |
| ipapi.co | HTTPS. The free quota isn't stated on the API page (UNVERIFIED; the 429 `RateLimited` error exists). | Yes (`city`, `postal`) | Request logs kept "for a limited time". The FAQ says "We do not share or sell your IP address queries", but the policy lists Cloudflare Bot Management, iubenda and FastMail as processing IPs. Policy dated 2026-06-07. | https://ipapi.co/api/, https://ipapi.co/privacy/ |
| ipinfo.io Lite | Free, but **country-level only**. City starts at the paid Core plan. | No | n/a | https://ipinfo.io/pricing |
| Self-hosted Cloudflare Worker that echoes `request.cf.city` / `request.cf.postalCode` | Workers plans include these fields ("All plans have access to"). Fields can be `null`. The page was updated 2026-10-18. | Yes | HTTPS. Data goes only to Cloudflare, which Grant already uses for Sage. It needs a small deploy, so it's an option if Grant wants no new third party. | https://developers.cloudflare.com/workers/runtime-apis/request/ |

Run the lookup with `curl` from Bash, so the request comes from the user's own IP. Don't use WebFetch. The tools reference says "HTTP URLs are automatically upgraded to HTTPS", and ip-api's free endpoint has no HTTPS, so WebFetch can't reach it at all. Separately, the docs don't say whether WebFetch's request leaves from the user's machine, so it could geolocate the wrong IP (UNVERIFIED). A VPN or iCloud Private Relay changes the result.

## 4. Recommended flow

**One-time setup (Grant, in Shortcuts.app):** create a shortcut named `Jeeves Location` with:
1. Get Current Location
2. Get Details of Locations → City (save to a variable `City`)
3. Get Details of Locations → ZIP Code (from the same location; save to `ZIP`)
4. Text: `City|ZIP` (with the two variables), as the final output action

When the Shortcuts Privacy dialog appears on a run, choose **Allow Once** (never Always Allow). Allow Once is a choice in that run-time dialog; the shortcut's Details > Privacy tab only shows and revokes access. Apple says Always Allow stops future prompts; that Allow Once brings the dialog back on every run is implied, not stated (UNVERIFIED). If Always Allow is ever chosen, undo it with Details > Privacy > Reset Privacy.

**Each run (skill):**
1. **Ask first** with `AskUserQuestion`: "To find the law and attorneys that apply to you, may I check your location? I'll keep only city and ZIP." Options:
   - Use this Mac's location (Shortcuts; macOS will also ask)
   - Use approximate location from my IP (sends your IP to ip-api.com over unencrypted HTTP; may be wrong on VPN)
   - I'll type my city or ZIP
   - Skip
2. **Device:** check that the shortcut exists, then run it:
   ```bash
   shortcuts list | grep -qx 'Jeeves Location' || echo "MISSING"
   shortcuts run 'Jeeves Location' --output-path - --output-type public.plain-text
   ```
   Expect `Austin|78701`. If it's missing, empty, denied or times out, offer the fallback or typed entry. Don't retry in a loop.
3. **IP fallback**, only if the user chose it in step 1:
   ```bash
   curl -sS --max-time 5 'http://ip-api.com/json/?fields=status,message,city,zip'
   ```
   Use the result only if `status` is `"success"`. Label it "approximate (from your internet connection)".
4. **Confirm back:** "I have Austin, 78701. Use it?" Let the user correct it.
5. **Keep only city + ZIP.** Coordinates never leave the shortcut, and the IP request asks only for `city,zip`. Don't write the location to files or memory. Say that it enters this conversation, which goes to Anthropic.

**Privacy notes to state in the skill:**
- Device path: Apple handles positioning and reverse geocoding (network geocoding is likely, UNVERIFIED for Shortcuts), and only city and ZIP reach Claude.
- IP path: the user's IP goes to ip-api.com in plaintext. Their terms limit the free tier to non-commercial use, which fits a personal skill (assumption).
- Typed entry is always an option and sends nothing anywhere.

## UNVERIFIED items

- Whether an Artifact `location` capability exists for other accounts or later runtime contracts.
- That a Shortcuts privacy dialog appears when the shortcut is launched from `shortcuts run` in the Claude Code CLI or desktop Bash, and how the Bash sandbox interacts with it.
- Apple-sourced names for the "Get Current Location" / "Get Details of Locations" actions and their City / ZIP Code fields (third-party source only).
- How Mac location is resolved and whether the geocode goes to Apple's servers.
- That a Swift binary with an embedded Info.plist gets a Location prompt, and which app the grant is attributed to.
- ipapi.co's free quota. Whether WebFetch requests come from the user's machine.
- That choosing Allow Once makes Shortcuts prompt again on every run.
- Whether Anthropic's IP-inferred location is visible to the model.
- Chrome's Wi-Fi geolocation provider, and whether the desktop browser pane honors `navigator.geolocation`.

## Independent verification (2026-10-20)

Re-checked by a second agent. No location shortcut was run, ip-api was not called, and no location prompt was triggered.

**Re-opened:** every cited URL (code.claude.com tools-reference, llms.txt, desktop, computer-use, artifacts, and data-usage; support.claude.com 11869619; privacy.claude.com 11186740; the CoreLocationCLI GitHub page; Apple forum threads 840513 and 124189; Apple Shortcuts guide pages apd455c82f02 and apd961a4fc65; both Cassinelli action pages; ip-api docs/api:json and docs/legal; ipapi.co /api/ and /privacy/; ipinfo.io/pricing; Cloudflare Workers Request API). The full desktop, computer-use and artifacts pages were downloaded and grepped for "location" and "geoloc". Local re-runs: `which`, `sw_vers`, `swift --version`, `xcode-select -p`, `shortcuts list`, `man shortcuts`, the macOS 27 SDK headers `CLLocationManager.h`, `CLGeocoder.h` and MapKit's `MKReverseGeocodingRequest.h`, and the bundled artifact-capabilities skill text and its `.d.ts` files.

**Confirmed (22):**
1. The tools reference lists no tool that reads location.
2. llms.txt has no page titled or described with "location" or "geolocation".
3. The desktop doc's panes and its two computer-use permissions (Accessibility, Screen Recording) match. The only "location" hits are worktree and repo paths.
4. iOS article: location tool, Allow once / Always allow / Don't allow, Team/Enterprise excluded, no macOS mention.
5. Privacy article: optional IP city/region inference, dashboard toggle, "device level" wording, updated 2026-03-16.
6. The capability list matches, as does "Anything not listed is unavailable to this user". No `.d.ts` file has a geolocation API (the only "location" hits in `comments.d.ts` mean a comment thread's anchor).
7. Artifacts "Page constraints": the CSP limits fetch/XHR/WebSocket to the page's own origin.
8. Computer use needs Accessibility and Screen Recording, plus Pro or Max. It's not on Team/Enterprise.
9. The local commands match: swift, shortcuts and osascript are in /usr/bin; macOS 27.0.1 (26A434); Swift 6.4; Xcode at /Applications/Xcode.app; same five shortcuts; no CoreLocationCLI.
10. `CLLocationManager.h` lines 484-486 contain the quoted Info.plist sentence.
11. `CLGeocoder.h` line 23 reads "Use MapKit", line 33 reads "Use MKReverseGeocodingRequest", and `MKReverseGeocodingRequest.h` exists.
12. The CoreLocationCLI README doesn't document a permission mechanism. It installs as a notarized Homebrew cask.
13. `man shortcuts` (2021-09-08): "-" means stdout, create/edit needs the app, `sign` exists.
14. The Apple CLI guide covers `-o` / `--output-path` and the pause when a shortcut asks for input.
15. The Apple privacy guide covers the three dialog choices, Always Allow ending future prompts, and Details > Privacy / Reset Privacy.
16. The Cassinelli pages: Get Current Location takes no input and outputs a Location. Get Details of Locations includes City and ZIP Code.
17. ip-api json docs: no commercial use, 45/min, no key, no SSL on free, `city`/`zip`, `fields=`, `status`/`message`.
18. ip-api legal: IP held in RAM up to 1 minute, "We do not log requests", no date.
19. ipapi.co API: HTTPS, no free quota stated, 429 `RateLimited`, `city`/`postal`.
20. ipapi.co privacy: "limited time" logs, the FAQ no-share quote, all three processors, dated 2026-06-07.
21. ipinfo Lite is country-level only. City data starts at Core ($26/mo).
22. Cloudflare `request.cf.city`/`postalCode`: "All plans have access to", `string | null`, updated 2026-10-18.

**Corrected (6):**
1. Forum threads: neither shows a CLI stuck at `notDetermined`. One is a LaunchAgent app bundle, the other a CLI that was granted access. Both are now described accurately and flagged as weak.
2. Recommended flow: Allow Once is chosen in the run-time dialog, not set in Details > Privacy.
3. ip-api "No cookies" covers the website only.
4. Privacy article: "non-web surfaces" narrowed to the mobile app and browser extension, the mandatory country inference added, and "the model can't read any of this" marked as an inference.
5. WebFetch: added the documented reason it can't work, since it upgrades HTTP to HTTPS and ip-api's free tier has no HTTPS.
6. Version: 2.1.299 is the bundled skill's version. The installed CLI reports 2.1.304.

**Unverified (11):** Artifact `location` for other accounts or later contracts; Chrome's location provider and the browser pane's geolocation handling (unsourced row); the embedded-plist mechanism and which app gets the grant; the Shortcuts dialog under `shortcuts run` from Claude, and sandbox effects; how a Mac without GPS resolves "Get Current Location" and where the geocode goes; Apple-sourced action and field names; Allow Once re-prompting every run; ipapi.co's quota; where WebFetch's request comes from; whether the model sees the IP-inferred location; that "non-commercial" covers a personal skill (assumption).

**Negative claims:** "No location tool in Claude Code or the desktop app" and "no Artifact location capability" hold against the current docs and this account's capability roster. This desktop session's own tool list has none either. A web search turned up no official Mac location feature. Absence from docs is not proof: a feature could be undocumented, gated per account, or shipped after 2026-10-20. The skill's generic description does mention location, so the Artifact claim holds for this account only.

**Not checked:** Behavior on real hardware (by design: no shortcut run, no ip-api call, no prompt). The Apple forum pages showed month and year only.

**Recommendation:** Unchanged. Use the Shortcuts primary path with consent first, the ip-api fallback with disclosure, and typed entry as an option.
