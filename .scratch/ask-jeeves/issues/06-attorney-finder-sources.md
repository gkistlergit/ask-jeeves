# Attorney-finder sources and feasibility
Type: research
Status: resolved
Blocked by:
Findings: research/06-attorney-finder-sources.md

## Question

What sources can the skill use, for free and through web search or fetch, to (a) confirm a lawyer's active license and public discipline in Indiana (Roll of Attorneys), South Carolina (SC Bar and SC Judicial Branch) and any other state (a general method or a list of bar lookups); (b) judge customer reviews (Google, Avvo, Martindale-Hubbell, Justia, Lawyers.com, Yelp, BBB), including how to read counts and dates and how to spot fake or purchased reviews; and (c) judge budget (flat fees, limited-scope rules such as Indiana Rule 1.2(c), free or low-cost consultations, bar lawyer-referral services, legal aid in IN and SC)? Test that each source can actually be fetched by the tools: note blocks, CAPTCHAs and logins. Never bypass a CAPTCHA.

## Answer

See `research/06-attorney-finder-sources.md`. It went through research, an independent verification (62 confirmed, 10 corrected, 1 removed, 7 UNVERIFIED) and a follow-up check of the 35 remaining state rows (19 confirmed, 5 corrected, 11 UNVERIFIED). The privacy scrub was run, and the dry run is anonymized as Attorney A–D.

- **License checks need Grant's own browser.** The Indiana Roll is a JS app, and its terms bar intelligent agents and possibly even linking to it. sccourts.org's robots.txt disallows every unnamed agent, and SC status sits behind a POST detail page. The skill should give the official site and the exact name to search, not fetch the record itself.
- **Discipline:** Indiana shows it on the Roll record. SC shows it only in the Supreme Court's conduct orders.
- **Review sites** (Avvo, Justia, Yelp, Google Maps, Internet Brands sites, BBB) are blocked or barred to bots. Review evidence comes from search snippets plus pages Grant opens.
- **Fake reviews:** the FTC rule, 16 CFR Part 465 (in force since 2024-10-21), plus its first warning letters (2025-12-22) and its guidance signals.
- **Budget:** the SC Bar LRS charges at most $50 for 30 minutes. The IndyBar LRS fee is UNVERIFIED. Legal aid in both states uses a 125% FPL cutoff. Limited scope is allowed under RPC 1.2(c), and Indiana also has TR 3.1(I).
- **Process note:** the original research agent drove 4 live lookups in a browser before reading Indiana's terms. Treat that as a one-off and never automate it. Open questions 1–3 and 6 in the file go to ticket 14.
