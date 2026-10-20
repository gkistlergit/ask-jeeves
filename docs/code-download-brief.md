# Brief: download state employment statutes into the local library

Grant authorized this on 2026-10-20: download the available official state codes into `~/Developer/ask-jeeves/Sources/`, optimized for Jeeves. Read `Sources/README.md` first.

## What to get, per state

Only the **employment titles and chapters** Jeeves uses, from the **official** code site (legislature or official publisher):
1. the non-compete or restrictive-covenant statute. If the state has none (common law only), record that;
2. the trade secrets act (usually a UTSA enactment);
3. the wage payment act, covering wage payment, deductions and penalties;
4. the computer crime or computer trespass statute;
5. any other section that the state's row in `research/04-choice-of-law.md` Part B cites, such as anti-waiver, choice-of-law or occupation bans.

Fetch at chapter level, not whole codes. Prefer HTML or XML over PDF. Use an official per-title bulk file only if it's no bigger than about 20 MB and contains these chapters.

## Where to find the URLs

1. `research/04-choice-of-law.md` Part B, plus its verification and follow-up sections: verified statute URLs per state.
2. If they exist, `state-codes-part1.md` or `state-codes-part2.md` in `/private/tmp/claude-501/-Users-grantkistler-Developer-sage-troubleshooting-app--claude-worktrees-eager-elion-57a9f8/43c02ece-8b9e-492c-86cc-2441cfc8691a/scratchpad/aj-skill/skills/ask-jeeves/references/`. Another agent may still be writing them, so read them but never edit them.
3. Otherwise: WebFetch the state legislature's statutes page. **At most 5 WebSearch calls per agent in total**, because the search budget is shared and runs out.

## How to download

- Use `curl -sSL --max-time 30 -o <file> <url>` with curl's default user agent. Don't spoof a browser user agent.
- Before the first download from a host, fetch its `robots.txt`. If the code path is disallowed for `*`, download nothing from that host; list the state under "Grant downloads by hand", with the exact page and button.
- Never bypass a CAPTCHA, login, paywall or JS-only wall. A page that comes back as a JS shell, a 403 or a CAPTCHA goes to Grant's manual list too.
- Keep at least 1 second between requests to the same host, and fetch at most 40 files per state.
- Official sources only. A mirror (Justia, FindLaw, Casetext, etc.) is never downloaded.

## Where to put it

```
Sources/<ST>/<edition>/html/<chapter-id>.html    (or .xml / .pdf) the downloaded file
Sources/<ST>/<edition>/text/<chapter-id>.txt     plain text: textutil -convert txt -output <txt> <html>
                                                 or for PDF: swift ~/Developer/ask-jeeves/scripts/pdf2txt.swift <pdf> <txt>
```

- `<ST>` is the two-letter code.
- `<edition>` is the session or year the site says the code is current through (for example `2025-session`), or `fetched-2026-10-20` if the site doesn't say.
- `<chapter-id>` is the state's own numbering, for example `t39c008` or `ORS-653`.
- After converting, check that each text file contains the statute's section headings. A file that is mostly navigation or empty doesn't count as downloaded.

## What not to touch

- Don't edit `Sources/MANIFEST.md`. The coordinator writes it.
- Don't touch other agents' states.
- Don't run git, use a browser, computer-use or the clipboard, or spawn subagents.

## Report

Write `Sources/_reports/<your slice name>.md` (gitignored) with:
- **one row per state:** ST | edition | site | chapters downloaded (id → statute) | text files verified | robots/terms note | status (`done` / `partial` / `manual`);
- **"Grant downloads by hand":** for each state that needs it, the exact URL, the button or link to click, and the titles to grab;
- **"Not found":** any of the 4 statutes you couldn't locate officially.

Reply to the coordinator in at most 3 lines: done / partial / manual counts, and the total MB downloaded.
