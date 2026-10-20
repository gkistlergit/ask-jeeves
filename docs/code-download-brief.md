# Brief: download state employment statutes into the local library

Grant authorized this on 2026-10-20: download the available official state codes into `~/Developer/ask-jeeves/Sources/`, optimized for Jeeves. Read `Sources/README.md` first.

## What to get, per state (expanded 2026-10-20 by Grant: "covered in depth")

Only **employment-related chapters** from the **official** code site (legislature or official publisher). Fetch at chapter level, never whole codes. Cover all of these groups in depth. Where a state has no statute for an item, record "none: common law" (or "none found"), with the page you checked.

**A. IP theft and trade secrets**
1. the trade secrets act (usually a UTSA enactment);
2. the criminal theft-of-trade-secrets statute, plus any statute on theft of computer data or intellectual property;
3. the computer crime or computer trespass act;
4. civil-theft or conversion statutes with multiple damages (Indiana's Crime Victims Relief Act, IC 34-24-3, is the model).

**B. NDAs and confidentiality**
5. statutes that limit NDAs or confidentiality terms: harassment, discrimination or assault NDA bans, "Silenced No More"-style laws, settlement-confidentiality limits;
6. state whistleblower protections that override confidentiality.

**C. Restrictive covenants**
7. the non-compete or restrictive-covenant statute (including non-solicit, no-hire and garden-leave rules), or "none: common law";
8. occupation-specific bans (physicians, healthcare, broadcasters, low-wage) and wage thresholds;
9. choice-of-law or forum anti-waiver statutes for employees;
10. employee invention-assignment limit statutes (like Cal. Lab. Code § 2870), or "none".

**D. Employment law**
11. the wage payment act: timing, final pay, deductions, penalties;
12. state minimum wage and overtime;
13. the state fair-employment and civil rights act (discrimination, retaliation);
14. general labor provisions;
15. employee-privacy statutes: social-media password laws, electronic-monitoring notice laws, personnel-file access;
16. at-will exceptions in statute (for example Montana's Wrongful Discharge from Employment Act).

**E. Commercial and procedure (the South Carolina set)**
17. the state arbitration act;
18. the unfair or deceptive trade practices act;
19. the data-breach notification statute.

Also get any other section that the state's row in `research/04-choice-of-law.md` Part B cites. Prefer HTML or XML over PDF. Use an official per-title bulk file only when it's no bigger than about 20 MB and contains these chapters. Cap: about 120 files per state.

## Where to find the URLs

1. `research/04-choice-of-law.md` Part B, plus its verification and follow-up sections: verified statute URLs per state.
2. If they exist, `state-codes-part1.md` or `state-codes-part2.md` in `/private/tmp/claude-501/-Users-grantkistler-Developer-sage-troubleshooting-app--claude-worktrees-eager-elion-57a9f8/43c02ece-8b9e-492c-86cc-2441cfc8691a/scratchpad/aj-skill/skills/ask-jeeves/references/`. Another agent may still be writing them, so read them but never edit them.
3. Otherwise: WebFetch the state legislature's statutes page. **At most 5 WebSearch calls per agent in total**, because the search budget is shared and runs out.

## How to download

- Use `curl -sSL --max-time 30 -o <file> <url>` with curl's default user agent. Don't spoof a browser user agent.
- Before the first download from a host, fetch its `robots.txt`. If the code path is disallowed for `*`, download nothing from that host; list the state under "Grant downloads by hand", with the exact page and button.
- Never bypass a CAPTCHA, login, paywall or JS-only wall. A page that comes back as a JS shell, a 403 or a CAPTCHA goes to Grant's manual list too.
- Keep at least 1 second between requests to the same host, and stay within the 120-file cap per state.
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
- **Coverage grid:** one row per state, one column per item 1–19, each cell `✓ <chapter-id>`, `none: common law`, `none found`, or `manual`.

Reply to the coordinator in at most 3 lines: done / partial / manual counts, and the total MB downloaded.
