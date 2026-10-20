# Remaining state codes: find a way to download them
Type: task
Status: claimed
Blocked by: 19

## Question

Grant asked on 2026-10-20 to "find a way to download these remaining codes after the rest of everything is done." The states whose official code the six download agents couldn't fetch: AL, AK, AR, GA, IL, MS, NJ, OH, OK, PA, TN, and possibly CA. Find a route for each one that stays within the rules (official sources only, honor robots.txt and terms, never bypass a CAPTCHA or login, Grant accepts any terms himself). Candidate routes to try, per state:

- **Alternate official files:** IL `ftp.ilga.gov/ILCS/` (curl got 200); AK `akleg.gov` (curl got 200; only WebFetch was blocked); CA `downloads.leginfo.legislature.ca.gov` pubinfo (1.1 GB; check for a smaller per-code file); NJ "Download Data → Statutes"; TN `publications.tnsosfiles.com` session-law PDFs; PA palegis.us in a browser.
- **Session-law PDFs** of the specific acts, from the legislature's own bill site, where the code viewer is a JS or Lexis wall (AR, GA, MS, TN).
- **The Chrome MCP browser,** reading pages Grant has open on the official site. Only where robots.txt and the site terms allow it: check ALISON (AL) first. Never on OH or OK, where robots.txt disallows everything. On LexisNexis portals only after Grant himself accepts the terms.
- **Hand download** by Grant, with exact pages and buttons, as the fallback (`Sources/_reports/slice*.md` "Grant downloads by hand").

Done when every listed state is either in `Sources/MANIFEST.md` or has a written reason it can't be obtained within the rules.
