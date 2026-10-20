# Remaining state codes: find a way to download them
Type: task
Status: resolved
Blocked by: 19

## Question

Grant asked on 2026-10-20 to "find a way to download these remaining codes after the rest of everything is done." The states whose official code the six download agents couldn't fetch: AL, AK, AR, GA, IL, MS, NJ, OH, OK, PA, TN, and possibly CA. Find a route for each one that stays within the rules (official sources only, honor robots.txt and terms, never bypass a CAPTCHA or login, Grant accepts any terms himself). Candidate routes to try, per state:

- **Alternate official files:** IL `ftp.ilga.gov/ILCS/` (curl got 200); AK `akleg.gov` (curl got 200; only WebFetch was blocked); CA `downloads.leginfo.legislature.ca.gov` pubinfo (1.1 GB; check for a smaller per-code file); NJ "Download Data → Statutes"; TN `publications.tnsosfiles.com` session-law PDFs; PA palegis.us in a browser.
- **Session-law PDFs** of the specific acts, from the legislature's own bill site, where the code viewer is a JS or Lexis wall (AR, GA, MS, TN).
- **The Chrome MCP browser,** reading pages Grant has open on the official site. Only where robots.txt and the site terms allow it: check ALISON (AL) first. Never on OH or OK, where robots.txt disallows everything. On LexisNexis portals only after Grant himself accepts the terms.
- **Hand download** by Grant, with exact pages and buttons, as the fallback (`Sources/_reports/slice*.md` "Grant downloads by hand").

Done when every listed state is either in `Sources/MANIFEST.md` or has a written reason it can't be obtained within the rules.

## Answer

Resolved 2026-10-20. Four more states are on disk: AL, CA, NJ and PA, plus Tennessee's 2026 non-compete act. AK and IL were already fetched by the download agents and needed only MANIFEST rows. Six states are blocked within the rules, each with one step left for Grant. `Sources/MANIFEST.md` now has a row for every edition on disk: 49 rows across 45 states plus DC.

| State | Route used | Edition | Status |
|---|---|---|---|
| AL | ALISON's public GraphQL endpoint (`alison.legislature.state.al.us/graphql`), the API the code viewer itself calls. No robots.txt; the site sets `NEXT_PUBLIC_ROBOTS: all`; no login. 1 s between requests. | fetched-2026-10-20 | done: 123 sections, 10 groups (8-1 art. 9, 8-27, 13A-8 arts. 1 and 5A, 8-19, 8-38, 6-6 art. 1, 25-1-20 to -30, 36-26A) |
| AK | akleg.gov print view (download agents) | 2025 | done earlier: 9 chapters |
| AR | Act 232 of 2025 from arkleg (download agents). The code itself is only on LexisNexis. | 2025-session (Act only) | **blocked: Lexis terms** |
| CA | Legislative Counsel bulk file `downloads.leginfo.legislature.ca.gov/pubinfo_2025.zip` (1.2 GB, dated 2026-10-19). Read by HTTP byte range: the index table plus only the 346 needed section files, about 30 MB. No robots.txt on that host. leginfo itself stays behind a Cloudflare challenge. | 2025-26-session | done: 346 sections, 22 groups (B&P 16600–16608 and 17200–17210, Lab. 200–244, 432.3, 510, 925–926, 980, 1102.5, 1182.12, 1194, 1198.5, 2870–2872, 2922, Civ. 3426 et seq., 1670.11, 1798.80–.84, CCP 1001–1002 and 1280–1294.4, Pen. 496, 499c, 502, Gov. 12900–12996). Gov. 12901 and Lab. 226.7 each have two versions in force, both kept (`-v2`). |
| GA | none | none | **blocked: Lexis terms** |
| IL | ftp.ilga.gov/ILCS (download agents) | through-PA-104-433 | done earlier: 112 sections |
| MS | none | none | **blocked: Lexis terms** |
| NJ | `pub.njleg.gov/statutes/STATUTES-TEXT.zip`, the Legislature's own "Download Data → Statutes" file. robots.txt allows all. Only the 84 MB `STATUTES.TXT` member was read. | P.L.2026-c50 ("updated through P.L.2026, c.50, and J.R.1") | done: 10 chapters split into `text/` (56:15, 56:8, 2C:20, 2A:38A, 2A:23B, 10:5, 34:19, 34:11, 34:6B, 34:1B-265) |
| OH | none | none | **blocked: robots.txt** (`codes.ohio.gov`: `User-agent: * Disallow: /`) |
| OK | none | none | **blocked: robots.txt** (`oklegislature.gov`: `Disallow: /` for `*`; `oscn.net` is behind a Cloudflare Turnstile check) |
| PA | palegis.us statute views (`view-statute?iFrame=true&txtType=HTM…`), read in a browser. robots.txt has no `*` group and the Legal Notices page sets no use limits; curl gets 403. Saved as one bundle with Grant's OK. | fetched-2026-10-20 | done: 12 files (12 Pa.C.S. ch. 53; 18 Pa.C.S. chs. 39, 76; 42 Pa.C.S. ch. 73; Acts 222/1955 PHRA, 329/1961 WPCL, 5/1968 MWA, 387/1968 UTPCPL, 286/1978, 169/1986 Whistleblower, 94/2005 breach, 74/2024 health-care non-competes) |
| TN | Pub. Ch. 934 (2026, the non-compete law: 50-1-210 et seq.) PDF, saved from publications.tnsosfiles.com in a browser (curl gets a CloudFront 403). The code itself is only on LexisNexis. | 2026-PC934 (Act only) | Act done; **code blocked: Lexis terms** |

### Grant's next step for each blocked state

After saving, run `scripts/ingest-code.sh <ST> <edition> <folder>`. It writes `text/` and the MANIFEST row. Chapter lists are under "Grant downloads by hand" in `Sources/_reports/slice*.md` (AR, CA, GA: slice 1–2; MS: slice 3; OH, OK, PA: slice 5; TN: slice 6).

- **AR, GA, MS, TN (LexisNexis free public access).** Open the link, accept Lexis's terms yourself, then use each chapter's Print/Download button into `~/Downloads/<ST>-code/`. Each link is the state's official entry: LexisNexis's `hottopics` redirect, which the legislature's own "Code" link uses.
  - AR: https://www.lexisnexis.com/hottopics/arcode/
  - GA: https://www.lexisnexis.com/hottopics/gacode/
  - MS: https://www.lexisnexis.com/hottopics/mscode/
  - TN: https://www.lexisnexis.com/hottopics/tncode/
- **OH.** robots.txt bars all automated access, so only a person can save these. Open https://codes.ohio.gov/ohio-revised-code/chapter-1333 and save the page into `~/Downloads/OH-ORC/`; repeat for chapters 2913, 2307, 4113, 4111, 4112, 4101, 2711, 1345 and 1349.
- **OK.** Same robots bar. At https://www.oklegislature.gov, open "Oklahoma Statutes" and save Titles 15, 78, 40, 21, 25, 12, 24 and 85A into `~/Downloads/OK-statutes/`, then trim to the sections in slice 5.

Methods that did not work and should not be retried: the built-in browser pane cannot save files; the Lexis public portal sent an automated Chrome tab to a sign-in error page ("Unable to Complete Your Request") twice, so Grant opens those links himself; and the CA, OSCN and tnsosfiles bot checks were not bypassed.
