# Reference-file spec (build ticket 18)

A reference file is a dated, built-in summary of verified law for one legal area, with a section for each covered jurisdiction (see `CONTEXT.md`). Jeeves reads it at every depth. Quick mode cites **only** what is in these files, so every line must be trustworthy.

## Source rules
- Draw content **only** from the named research file(s) in `research/`. Each research file ends with "Independent verification" sections; apply their corrections. Drop anything marked removed. Carry anything still UNVERIFIED forward only with an inline `[UNVERIFIED: reason]`, and only when the point matters for issue-spotting.
- **Indiana Code:** check every IC citation against the official 2026 Indiana Code text in `~/Developer/ask-jeeves/sources/indiana-code/IC-title-NN.txt`. That text is the official iga.in.gov download; sections start at a line reading `IC <title>-<art>-<ch>-<sec>`, and `grep -n "^IC 24-2-3-2$"` finds one. Where the text confirms the claim, cite it as `IC 24-2-3-2 (2026 Ind. Code, official IGA edition)` with the URL `https://iga.in.gov/laws/2026/ic/titles/24`. Where the text contradicts the research, follow the code and note the correction. A title not in that folder may be converted from `~/Downloads/2026-Indiana-Code/2026_Indiana_Code_HTML/<NN>.html` with `textutil -convert txt -output <scratchpad file> <that file>`. Don't put code text into the repo; quote under 15 words only.
- Don't do new web research except a WebFetch to confirm a URL you cite, under the limits in `references/research-resilience.md`. No browser, computer-use or clipboard, and don't spawn subagents.

## Format
```
---
area: <slug>
as_of: 2026-10-20
verified: 2026-10-20
sources: research/<file>.md (+ verification passes); 2026 Indiana Code (official IGA edition)
---
# <Area>: reference

> For issue-spotting only. Not legal advice. Every claim cites its source; [UNVERIFIED] marks claims that could not be confirmed.

## Federal
### <claim or rule group>
- <rule in one or two lines> [cite: <short citation>, <URL>]
- **CHANGED 2025–26:** <change> [cite]
## Indiana
...
## South Carolina
...
## Facts that decide outcomes
- Employer side: …
- Employee side: …
## Common offer-letter / situation risks and typical recommendations
- <risk>: likely <Low/Med/High> when <condition>; typical fix: … [cite]
## Creative angles (non-obvious, lawful)
- <idea>. Risk: … Enforceability: … [cite]
## Open questions / known gaps
```

- Scannable and dense: aim for 200–450 lines. Bullets, not essays.
- Quotes stay under 15 words. Write page references as "pg. N".
- Every bullet that states law has a `[cite: …]` with a URL.
- Never invent a citation. If a needed point lacks a verified source, leave it out.
- The repo is public: no personal names beyond case names and parties in published opinions, and no street addresses.
