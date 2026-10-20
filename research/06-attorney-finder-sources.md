# 06 — Attorney-finder sources and feasibility

Ticket: `.scratch/ask-jeeves/issues/06-attorney-finder-sources.md`. All sources accessed 2026-10-20 unless a row says otherwise. Glossary terms (*attorney finder*, *location option*, *mismatch*) follow `CONTEXT.md`.

## Summary

- **Licence checks work, but you have to open them in a real browser.** The Indiana Roll of Attorneys is an Angular single-page app. A WebFetch of it returns an empty shell. Its terms bar "spiders, robots, avatars, intelligent agents" and anything other than "a normal browser". The South Carolina Judicial Branch name search does return results to WebFetch, but only names. Status, admission date and county sit on a detail page that needs a POST with an anti-forgery token. sccourts.org's robots.txt also disallows every agent it doesn't name. So for both test states, the skill should hand Grant the official search page plus the exact name to type (or confirm in his own browser). It should not fetch the record itself.
- **Discipline:** Indiana shows it on the Roll record (history from July 1, 1986, with pending matters labelled). South Carolina shows it nowhere on the attorney record. Public discipline lives in the Supreme Court's "Judicial/Legal Conduct" orders, and complaints stay confidential until formal charges become public under RLDE Rule 12(b).
- **Review sites are mostly blocked or barred.** Avvo, Justia and Cornell LII return 403 or a bot challenge to both WebFetch and curl. FindLaw and Super Lawyers homepages loaded to WebFetch on re-check (their directory pages were not re-tested), but both are Internet Brands sites, so its robot ban applies. Yelp returns 403, and its robots.txt disallows Claude-User. Google Maps is a JS app. Its robots.txt disallows `/maps/` but explicitly allows `/maps/place/` and `/maps/search/`, and its terms forbid automated access that ignores robots.txt. Martindale and Lawyers.com do load, but Internet Brands' terms ban robots and scrapers (search engines excepted). BBB loads, but its robots.txt disallows query-string URLs for Claude agents. In practice, review evidence has to come from WebSearch result snippets plus links Grant opens himself.
- **Fake-review signals are well sourced.** The FTC rule (16 CFR Part 465) has been in force since 2024-10-21 and is unamended per eCFR. The FTC sent its first warning letters under it on 2025-12-22. Its consumer and platform guidance lists checkable signals.
- **Budget signals:**
  - The SC Bar Lawyer Referral Service caps the consult at $50 for 30 minutes.
  - The IndyBar referral service doesn't publish a client fee (UNVERIFIED).
  - Both states' legal aid uses a 125% FPL cutoff.
  - Both states allow limited-scope work under RPC 1.2(c), and Indiana adds a court notice under Trial Rule 3.1(I).
- **Dry run: 4 of 4 licences were confirmed in official lookups,** all active or in good standing, with no Indiana discipline shown. Two lessons came out of it:
  - Search by last name plus city. Firm sites use nicknames or middle names.
  - The Indiana app briefly shows "0 of 0" while loading. That is a false negative.

## Source-capability table

Key: **WF** = WebFetch; **WS** = WebSearch; **curl** = plain HTTP GET from Bash, which is a proxy for any non-browser client. "Reach" means the tool got real content.

| Source | URL | Run by | Shows | WF | WS | JS / login / CAPTCHA | Terms on automated access |
|---|---|---|---|---|---|---|---|
| Indiana Roll of Attorneys | https://courtapps.in.gov/rollofattorneys/ | IN Office of Judicial Administration (Supreme Court) | Name, attorney no., admit date, licence status + date, firm, contact, other names, disciplinary history | **No.** Empty SPA shell (curl: 2.5 KB of HTML that loads `main.*.js`) | Finds the help page only | **JS required.** No login, no CAPTCHA seen | Roll ToU forbids "spiders, robots, avatars, intelligent agents" except a normal browser, and also forbids "frame or link to" its materials. robots.txt holds content-signal comments only, no rules. Footer: "Data mining from this website is prohibited by Supreme Court rule" (UNVERIFIED: the footer is inside the app, which the verifier did not fetch; the phrase is not in either ToU page and WebSearch found no copy) |
| IN Roll help page | https://www.in.gov/courts/help/attorney-search | IN courts | How the search works (last name required; city filter; partial match) | Yes | Yes | None | in.gov general |
| SC Judicial Branch Attorney Search | https://www.sccourts.org/attorneys/ (name search is a GET: `?first=&last=`) | SC Judicial Branch | Results list = names only. Detail = bar no., county, firm, contact, law school, SC admission date, membership class, membership status | **Partial.** WF returned the name list. Detail needs a POST to `/attorneys/detail/` with an anti-forgery token | Indirect | **Detail needs a browser** (form POST plus token). No login, no CAPTCHA | robots.txt: `User-agent: *` / `Disallow: /` ("# No one else"), with `Crawl-delay: 120000`. Only Googlebot variants and Bingbot get partial access; GPTBot is also `Disallow: /`. No Claude agent is named, so Claude-User falls under `*`. No terms-of-use page found (`/terms-of-use/` and `/disclaimer/` are 404). Privacy policy only |
| SC Bar Member Directory | https://www.scbar.org/lawyers/directory/ | SC Bar | Member directory | Page loads | Yes | **"Login required"** | Points the public to the SCJB Attorney Search instead |
| SC public discipline orders | https://www.sccourts.org/opinions-orders/court-orders/judiciallegal-conduct/ | SC Supreme Court | Lawyer- and judicial-conduct orders as PDFs, by year (dropdown back to 1978, with gaps such as 1990–91 and 1995–98) | Yes | n/a | Year filter; no name search on this page | Same robots.txt as above |
| SC RLDE Rule 12 | https://www.sccourts.org/resources/court-rules/appellate/rule-413/rule-12/ | SC Supreme Court | When discipline becomes public | Yes | n/a | None | — |
| Avvo | https://www.avvo.com/ | Internet Brands (acquired 2018, rebranded Martindale-Avvo, per ABA Journal; IB's legal-sites supplemental terms also name Avvo) | Ratings, reviews, licence claims | **No (403)** | Snippets only | Cloudflare challenge ("Just a moment") | robots.txt allows most paths for `*` (no Claude group). Terms page itself is 403; the IB terms likely apply, but that avvo.com links them is UNVERIFIED |
| Justia lawyer directory | https://www.justia.com/lawyers/ | Justia | Profiles, reviews | **No (403)** | Snippets | Cloudflare challenge | robots.txt allows all. Terms page 403 (UNVERIFIED) |
| Martindale-Hubbell | https://www.martindale.com/all-lawyers/noblesville/indiana/ | Internet Brands (footer links to internetbrands.com terms; the verifier's WebFetch text did not include the footer, so the link itself is UNVERIFIED on re-check, though IB's legal-sites terms name Martindale) | Peer rating "x/5.0 (n)", AV badge, client-review filter | **Yes** (browse pages) | Snippets | No CAPTCHA seen | robots.txt disallows `/search/` and `*?term=*`. IB terms ban "spiders, robots, crawlers, scrapers, framing, iframes or RSS feeds", with search engines excepted |
| Lawyers.com | https://www.lawyers.com/labor-and-employment/noblesville/indiana/law-firms/ | Internet Brands (same terms) | Firm rating + review count (in JSON-LD), "Free Consultation" flag | **Yes** | Snippets | CAPTCHA marker present in HTML (curl finding; WebFetch's text view showed no CAPTCHA, and raw HTML could not be re-checked) | robots.txt disallows `/attorney/`, `?free_consultation=`, and `?review=` after a path segment (`/*/?review=`). IB terms as above |
| Yelp | https://www.yelp.com/ | Yelp | Star ratings, counts | **No (403)** | Snippets | CAPTCHA page | robots.txt: Claude-User and Claude-SearchBot `Disallow: /`. ToS bans "any robot, spider, Service search/retrieval application" |
| BBB | https://www.bbb.org/ | BBB / IABBB | Letter rating, accreditation, complaints | **Yes** (search page loaded; no review counts on it) | Snippets | Cookie banner; CAPTCHA marker in HTML | robots.txt for Claude-User: `Disallow: /*?` (query URLs) and `/business-reviews/*`, but profile URLs (`/us/*/*/profile/*/*?`) allowed. Terms: "not for sale, republication, or aggregation"; they have no explicit robot clause but bar compiling data for a competing service |
| Google Maps / Business reviews | https://www.google.com/maps/ | Google | Star rating, counts, dated reviews | Not tried. curl got a 211 KB JS app | Snippets sometimes carry the rating | JS app | robots.txt disallows `/maps/` and `/search` for `*`, **but allows `/maps/place/`, `/maps/search/` and other listed `/maps/` paths** (corrected: place pages are not robots-disallowed). Terms bar automated access "in violation of the machine-readable instructions on our web pages" |
| Cornell LII Lawyer Directory | https://lawyers.law.cornell.edu/ | LII (directory powered by Justia, UNVERIFIED) | Listings | **No (403)**; curl gets 202 empty (WAF) | Snippets | Bot wall | — |
| FindLaw, Super Lawyers | findlaw.com, superlawyers.com | **Internet Brands** (corrected from Thomson Reuters: FindLaw's own page says IB acquired it in 2024; Super Lawyers' structured data names IB as parent) | Listings | Original run: 403. Verifier re-check: **both homepages loaded** to WebFetch; directory pages not re-tested | Snippets | Original run saw a Cloudflare challenge | IB terms (below) presumably apply; their footers were not checked |
| Firm websites | various | the firms | Practice areas, consult wording, fees (rarely) | **Yes** (all 4 tried) | Yes | None seen | Varies |
| SC Bar Lawyer Referral Service | https://www.scbar.org/for-the-public/quicklinks/get-legal-help/ | SC Bar | Phone (803) 799-7100 + online referral; "no more than $50 for a 30-minute consultation" | Yes (curl; WF timed out once in the original run, loaded on re-check) | Yes | Online referral form not tested | — |
| IndyBar Indy Lawyer Finder | https://www.indybar.org/?pg=lawyer-referral | Indianapolis Bar Association | Hire-a-lawyer, legal questions, legal-aid paths | Yes | Yes | Not tested past landing | — |
| Indiana Legal Services | https://www.indianalegalservices.org/eligibility-guidelines/ | Indiana Legal Services, Inc. | Free civil aid; 125% FPL (200% in some cases); $10,000 asset cap | Yes | Yes | Online application exists, not used | — |
| Indiana Legal Help | https://www.indianalegalhelp.org/ | Funding partners shown: Indiana Bar Foundation, Indiana Supreme Court | Help by ZIP/county, Free Legal Answers link, clinics | Yes | Yes | Get-help page wants ZIP/county (not tested) | — |
| SC Legal Services | https://sclegal.org/income-guidelines/ | South Carolina Legal Services | Free civil aid; 125% FPL ($19,950 for 1 person, 2026), with some exceptions up to 200% | Yes | Yes | Intake not used | — |
| FTC / eCFR (fake reviews) | https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465 | FTC / OFR | Rule text and version history | ftc.gov: **WF yes, curl 404** (blocks non-browser UA). eCFR: curl + API yes | Budget ran out mid-task | None | — |

## Licensing method by state

### Indiana (verified end-to-end)

1. Use the official search at https://courtapps.in.gov/rollofattorneys/ (OJA). Search by last name plus city. Firm sites often use a nickname or a middle name, which tripped one dry-run search. The help page says last-name-only searches are "designed to be as inclusive as possible" and match partial strings (https://www.in.gov/courts/help/attorney-search).
2. A results URL takes the form `/rollofattorneys/results?LastName=…&FirstName=…&City=…&OrderBy=0&Page=1` (observed in the browser). It still needs JS to render.
3. The record shows "License status" (e.g. *Active In Good Standing*, *Retired*), status date, admit date, firm, contact, and "Disciplinary information". Its own caveat reads "Most disciplinary history available here dates back to July 1, 1986". The UI strings also distinguish *pending* from *concluded* cases.
4. **Constraint:** both the Roll ToU (https://www.in.gov/courts/policies/tou-roll-of-attorneys) and the Online Services ToU (https://www.in.gov/courts/policies/tou) forbid automated agents and non-browser retrieval. The Online Services ToU says users may not "automate the collection of any content from an Application", and also bars "using any software other than a web browser to search and view data". Both ToUs list "(5) frame or link to" among the prohibited acts (the Online Services ToU adds "an Application" itself). **Recommendation:** the skill gives Grant the search page URL and the exact last name and city to type, and records his confirmation. It does not fetch, scrape or deep-link. (Whether a plain link in a chat counts as "link to" is UNVERIFIED; this is the conservative reading.)

### South Carolina (verified end-to-end)

1. Use the official search at https://www.sccourts.org/attorneys/ (SC Judicial Branch). The SC Bar directory page sends the public there "to verify contact information and member status" (https://www.scbar.org/lawyers/directory/). The Bar's own directory requires a login.
2. The name search is a GET (`?first=&last=`). Its results list holds names only, and each name is a POST form button. The detail page shows bar number, county, firm and contact, law school, "SC Admission Date", "SC Bar Membership Class" and "SC Bar Membership Status" (e.g. *Good Standing*). **It has no discipline section.**
3. For discipline, check the Supreme Court's Judicial/Legal Conduct orders (https://www.sccourts.org/opinions-orders/court-orders/judiciallegal-conduct/), filtered by year. A "Court Order Search" also exists at `/opinions-orders/court-orders/court-order-search/`. Corrected on re-check: it has no name field. It searches by order type, by affected court, or by full-text keyword, so a name can only go in as a keyword. Its order-type list doesn't name conduct orders, and whether full-text search covers them is UNVERIFIED. Under RLDE Rule 12(b), formal-charge filings go public "30 days after the filing of the answer". Earlier complaints stay confidential (Rule 12(a)), so a clean record doesn't prove there was never a complaint.
4. **Constraint:** sccourts.org's robots.txt disallows all user agents it doesn't name (`User-agent: *` / `Disallow: /`). **Recommendation:** treat it like Indiana and have Grant open the search himself.

### Any other state (general method)

1. Prefer the licensing authority: the state supreme court, its attorney-registration office, or a mandatory bar acting for the court. Use a voluntary bar's "find a lawyer" referral page only as a last resort. The status must come from the authority.
2. Search by last name plus city or county. Then match the bar number, admission date and city against the attorney's own site.
3. Get discipline from the authority's public-discipline records. Coverage varies (some states put it on the record, others in orders).
4. Read the site's robots.txt and terms before any fetch. Indiana and South Carolina both bar automated access, so assume a manual check unless a state says otherwise.

**Per-state starting URLs.** "Loads" means curl returned HTTP 200 on 2026-10-20 with the stated title or heading, or the link was found on the authority's own homepage. Text marked "Follow-up" or "Corrected" comes from the WebFetch re-check described under "Follow-up verification" below. **Loads does not mean a search was run.** Only IN and SC were exercised end-to-end. A "CAPTCHA/challenge marker" is a string found in the HTML. It suggests a wall but doesn't prove one.

| State | URL | Status |
|---|---|---|
| AL | https://members.alabar.org/Member_Portal/Member_Portal/Member-Search.aspx | Loads (linked as "find-a-member" from alabar.org public page). Follow-up: WebFetch shows an Alabama State Bar "Member Search" form with no login wall; whether results show status is UNVERIFIED |
| AK | https://alaskabar.org/for-lawyers/member-directories/ | **Corrected.** The old `member.alaskabar.org/cv5/…publicDirectory.htm` URL now returns a profile page with a template error. alaskabar.org links this Alaska Bar Association page ("Alaska Lawyer Directory") as its Lawyer Directory. Whether results show status is UNVERIFIED. Public discipline search: https://justiceweb.alaskabar.org/justiceweb (linked, not opened) |
| AZ | https://www.azbar.org/for-legal-professionals/practice-tools-management/member-directory/ | Loads ("Arizona State Bar Member Directory") |
| AR | https://attorneyinfo.aoc.arkansas.gov/info/attorney/attorneysearch.aspx | Linked as "Attorney Search" from arcourts.gov; loads. Follow-up: an Arkansas Judiciary search form (name, city, ZIP, bar no.) with no login wall; whether results show status is UNVERIFIED |
| CA | https://apps.calbar.ca.gov/attorney/LicenseeSearch/QuickSearch | Loads ("Attorney Search - The State Bar of California") |
| CO | https://www.coloradolegalregulation.com/attorney-search/ | Loads ("Attorney / LLP Search & Disciplinary History - Colorado Supreme Court"); challenge marker |
| CT | https://lookup.jud.ct.gov/AttorneyFirm | Loads ("Attorney Firm Look-up - Connecticut Judicial Branch") |
| DE | — | UNVERIFIED. The ODC page (https://courts.delaware.gov/odc/) links only the Digest of Lawyer Discipline (`/odc/digest/`). Follow-up: the courts' Information for Attorneys page lists no public lookup either; good-standing certificates go through the DSCLMS login (https://www.desclms.org/) |
| DC | https://my.dcbar.org/memberdirectory | Loads ("D.C. Bar - MemberDirectory", "Search for a Member of the D.C. Bar"). Follow-up: the page asks the user to "verify that you are not a robot" |
| FL | https://www.floridabar.org/directories/find-mbr/ | Loads ("Find a Florida Bar Lawyer", The Florida Bar). Follow-up: it has an "Eligible lawyers only" filter; WebFetch saw no challenge (the curl marker was not re-tested) |
| GA | https://www.gabar.org/member-directory/ | Loads (h1 "Member Directory") |
| HI | https://hsba.org/member-directory | **Corrected** from the HSBA "Find a Lawyer" landing page (https://hsba.org/find-a-lawyer), which links here as "Search Member Directory" and says the directory will "indicate whether the attorney can actively practice law in Hawaii". The directory page loads ("Member Directory \| HSBA"); results need JS |
| ID | https://isb.idaho.gov/licensing-mcle/attorney-roster-search/ | Loads ("Attorney Roster Search - Idaho State Bar") |
| IL | https://www.iardc.org/Lawyer/Search | Loads ("Lawyer Search", ARDC) |
| IN | https://courtapps.in.gov/rollofattorneys/ | **Verified end-to-end** (browser only). Follow-up: the in.gov help page links this URL; the app itself was not fetched (ToU) |
| IA | https://www.iacourtcommissions.org/ (links "Search the Lawyer Database" and "Search the Lawyer Disability and Discipline Orders") | Links found; session-based Oracle APEX URLs. Follow-up: the root redirects to the APEX home page of the Office of Professional Regulation, which shows both links |
| KS | https://directory-kard.kscourts.gov/ | UNVERIFIED. **URL corrected** from `.org` to `.gov`, per WebSearch (secondary), which reports that kscourts.gov's registration page says the directory lists all attorneys and their current status. The `.org` host resets the connection to WebFetch, and the `.gov` host and kscourts.gov both return 403, so none could be opened |
| KY | https://kybar.org/For-Public/Find-a-Lawyer | Loads ("Find a Lawyer", Kentucky Bar Association; linked as "Directory of Kentucky Attorneys"). Follow-up: WebFetch saw no CAPTCHA (the curl marker was not re-tested); whether results show status is UNVERIFIED. KBA also publishes a list of currently suspended and disbarred lawyers (https://kybar.org/For-Public/KBA-Currently-Suspended-and-Disbarred-Lawyers) |
| LA | https://www.lsba.org/MD321654/MembershipDirectory.aspx | Loads ("LSBA Membership Directory", Louisiana State Bar Association). Follow-up: a word-verification CAPTCHA gates the directory |
| ME | https://apps.web.maine.gov/cgi-bin/online/maine_bar/attorney_directory.pl | Loads ("Attorney Search \| Maine Board of Overseers of the Bar") |
| MD | https://www.mdcourts.gov/attysearch | **Corrected** from the AIS page (`/lawyers/ais`), which links here as "Search for a Maryland Attorney". Loads ("Maryland Attorney Listing", Maryland Judiciary); shows status such as active or inactive/retired; no login or CAPTCHA seen |
| MA | https://www.massbbo.org/s/attorney-lookup | UNVERIFIED. To WebFetch the page is a JS shell (heading "Registration", "Sorry to interrupt") that names no operator, and the massbbo.org home page returns the same shell. Only WebSearch (secondary) describes it as the Board of Bar Overseers lookup |
| MI | https://dir.michbar.org/ (redirect from michbar.org/memberdirectory) | Loads ("Member Directory", State Bar of Michigan). Follow-up: it lets you "check an attorney's status"; WebFetch saw no challenge (the curl Incapsula marker was not re-tested) |
| MN | https://mars.courts.state.mn.us/ | Loads (page text includes "Lawyer Search") |
| MS | https://msbar.reliaguide.com/home (redirect from msbar.org find-a-lawyer) | Loads; JS required (WebFetch got only a loader). Follow-up: msbar.org's Membership Status page sends readers to this "online Member Directory" for "up-to-date membership information", so it is the Bar's own status source |
| MO | https://mobar.org/public/LawyerDirectory.aspx | **Corrected.** The old `/site/content/Find-a-Lawyer` URL is a 404. "The Official Missouri Directory of Lawyers" (The Missouri Bar) says every lawyer "in good standing with the Supreme Court of Missouri is included"; no login seen. The opt-in LawyerSearch (`/public/LawyerSearch.aspx`) is a hiring tool, not a status check |
| MT | https://www.montanabar.org/For-Attorneys/Attorney-Directory | UNVERIFIED. **URL corrected:** the old `/For-Attorneys/Find-a-Lawyer` URL loads a generic "For Attorneys" page. This State Bar of Montana "Attorney Directory" page loads but showed no search fields or status, and its login link returns to it, so it may need a login. The public "Find a Lawyer" goes to licensedlawyer.org, a participation list |
| NE | https://attorneys.nejudicial.gov/member-search | Linked as "Search Nebraska Licensed Attorneys" from nebraskajudicial.gov; loads |
| NV | — | UNVERIFIED. **Wrong URL removed:** nvbar.org/for-the-public/find-a-lawyer/ is a Lawyer Referral Service page with no search. The "Bar Status" page (https://nvbar.org/for-lawyers/membership/bar-status/) defines status categories but links no public lookup, and "Find a Colleague" points back to the referral page |
| NH | https://www.nhbar.org/attorney-verification-good-standing-request | UNVERIFIED as a lookup. NHBA offers an online verification-request form, not a search. Its Member Directory (https://member.nhbar.org/directory) is behind a member login |
| NJ | https://drblookupportal.judiciary.state.nj.us/ (links "NJ Attorney Index") | UNVERIFIED. The Supreme Court's Disciplinary Review Board portal links the NJ Attorney Index, a Pega app on portalattysearch-cloud.njcourts.gov. The app returned a bot-check page ("Pardon Our Interruption") to WebFetch, which was not bypassed. A 2012 Judiciary notice (secondary, via WebSearch) says the index shows admission date and status to practice |
| NM | https://www.sbnm.org/For-Public/I-Need-a-Lawyer/Online-Bar-Directory | Loads ("Online Bar Directory", State Bar of New Mexico); whether it shows status is UNVERIFIED |
| NY | https://iapps.courts.state.ny.us/attorneyservices/search | Cloudflare challenge to curl; content UNVERIFIED |
| NC | https://portal.ncbar.gov/verification/search.aspx | Linked as "Search the Lawyer Directory" from ncbar.gov; loads |
| ND | https://www.ndcourts.gov/lawyers | Loads ("Lawyers", North Dakota Court System). Follow-up: the search has a "By Status" filter; WebFetch saw no challenge (the curl marker was not re-tested) |
| OH | https://www.supremecourt.ohio.gov/AttorneySearch/ | Loads ("Attorney Search") |
| OK | — | UNVERIFIED. **Wrong URL removed:** okbar.org/findalawyer/ is the OBA's opt-in "voluntary listing", which says it is not a complete list and shows no status. The OBA member directory now needs a MyOKBar login. No public status lookup was found |
| OR | https://www.osbar.org/members/membersearch_start.asp | Loads ("OSB Licensee Directory", Oregon State Bar); search by name, bar no. or city; whether it shows status is UNVERIFIED |
| PA | https://www.padisciplinaryboard.org/for-the-public/find-attorney | Loads (heading "Look Up an Attorney") |
| RI | https://rijrs.courts.ri.gov/rijrs/attorney.do | UNVERIFIED. Follow-up: courts.ri.gov's Attorney Resources page links this URL as "Attorney Search", so it is the Judiciary's own, but the tool reset the connection to WebFetch as it did to curl |
| SC | https://www.sccourts.org/attorneys/ | **Verified end-to-end** (detail needs a browser); landing page re-opened by the first verifier |
| SD | — | UNVERIFIED. Follow-up: statebarofsouthdakota.com links no directory or verification page. DOJ EOIR's licensing-verification page (https://www.justice.gov/eoir/attorney-licensing-verification, updated 2023-01-25) says to call the State Bar |
| TN | https://www.tbpr.org/attorneys | Loads to curl (Board of Professional Responsibility); 403 to WebFetch on re-check |
| TX | https://www.texasbar.com/AM/Template.cfm?Section=Find_A_Lawyer&Template=/CustomSource/MemberDirectory/Search_Form_Client_Main.cfm | Loads ("State Bar of Texas \| Find A Lawyer"). Follow-up: it covers "Attorneys licensed to practice in Texas"; DOJ EOIR's verification page lists the same URL |
| UT | https://services.utahbar.org/Licensee-Directory | Loads ("Utah State Bar Member Directory"); whether it shows status is UNVERIFIED |
| VT | https://www.vtcourts.gov/attorneys/attorney-licensing | **Corrected** from `/attorneys`. This Vermont Judiciary page links a static report, "Attorneys in Good Standing (as of 10/1/26)" (`/media/759`). It is a list, not a search, and the report was not opened |
| VA | https://vsb.org/Shared_Content/Directory/va-lawyer-directory.aspx | Linked from vsb.org; loads ("Virginia Lawyer Directory", Virginia State Bar). Follow-up: shows status such as In Good Standing or Not in Good Standing; no login |
| WA | https://www.mywsba.org/PersonifyEbusiness/LegalDirectory.aspx | Linked from wsba.org. **Resolved in follow-up:** the https URL loads to WebFetch ("Legal Directory", WSBA) with no SSO redirect, and says it shows license status and public discipline |
| WV | https://www.mywvbar.org/membership-search-members | UNVERIFIED. wvbar.org links it as "Membership Directory Search", but it returns 403 to WebFetch (a Cloudflare challenge to curl), so its content was not seen |
| WI | https://lawyerhistory.wicourts.gov/ | Loads ("Lawyer Status and History"); wicourts.gov also links public-discipline pages |
| WY | https://www.wyomingbar.org/for-the-public/hire-a-lawyer/lawyer-search/ | Loads ("Lawyer Search and Referral", Wyoming State Bar). Follow-up: its Lawyer Directory Search covers all Wyoming-licensed lawyers; whether results show status is UNVERIFIED; WebFetch saw no CAPTCHA (the curl marker was not re-tested) |

The ABA's "Bar Directories and Lawyer Finders" page (https://www.americanbar.org/groups/legal_services/flh-home/flh-bar-directories-and-lawyer-finders/) loads in a browser but gives 403 to WebFetch and curl. It lists additional lawyer-*finding* resources by state, not licence lookups, and marks SC "No known additional bar-sponsored lawyer-finding resources". The ABA disciplinary-agency directory URL I tried is a 404.

## Review-quality method

**Getting the evidence.** Directory pages can't be fetched, or their terms bar it. So:

1. Run WebSearch for "<name> <city> reviews" and "<firm> Avvo", and read the rating and count from the snippets. Label them as snippet-derived (secondary).
2. Read the attorney's and firm's own sites with WebFetch.
3. For anything decisive, give Grant the profile link to open himself.

One dry-run attorney's rating came only from a search snippet; it is UNVERIFIED.

**Reading counts and dates.**
- Count: a small count, under about 10 reviews, is weak evidence either way. Snippets from Avvo's area pages advertise filters such as "10+ reviews" (secondary, unverified).
- Recency: the FTC tells consumers to check how recent reviews are and to watch for "a burst of reviews over a short period of time" (https://consumer.ftc.gov/articles/how-evaluate-online-reviews, Oct 2022).
- Kind of rating: Martindale shows *peer* ratings ("x/5.0 (n)") apart from client reviews. Lawyers.com puts its client rating and count in JSON-LD while the visible listing may say "Reviews not shown" (WebFetch of both pages). Don't mix peer and client scores.

**Fake or purchased review signals (verified).**

| Signal | Source |
|---|---|
| A review burst over a short period; reviewer accounts with a single review; slightly-under-perfect fakes; fake negatives against competitors; incentive badges; cross-checking several sources | FTC, *How To Evaluate Online Reviews* (Oct 2022), https://consumer.ftc.gov/articles/how-evaluate-online-reviews |
| Open vs. closed (verified-customer) collection; selective solicitation; sentiment-conditioned incentives; suppressing negatives; uneven moderation | FTC, *Featuring Online Customer Reviews: A Guide for Platforms* (Jan 2022), https://www.ftc.gov/business-guidance/resources/featuring-online-customer-reviews-guide-platforms |
| Illegal practices to watch for: fake reviewers or experiences (§465.2); buying reviews conditioned on sentiment (§465.4); undisclosed insider reviews by officers, managers, employees or relatives (§465.5); company-controlled "independent" review sites (§465.6); review suppression by unfounded threats or intimidation (§465.7(a)), or implying the displayed reviews are all or most of them while negatives are suppressed by rating or sentiment (§465.7(b); corrected: the rule doesn't ban showing only favourable reviews as such, and neutral exclusions such as likely-fake reviews are allowed); fake social-media indicators (§465.8) | 16 CFR Part 465, https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465 (WebFetch now gets a federalregister.gov "unblock" redirect; read via the eCFR API); eCFR source note 89 FR 68077 (Aug. 22, 2024), which is the regulatory-text page; the FR document starts at 89 FR 68034 |
| Lawyer-specific: in SC, a testimonial must say it's a testimonial, disclose payment, say whether a non-client wrote it, and state that one client's result doesn't mean others will get the same (RPC 7.1(d)). A firm-site testimonial missing these is a red flag | SC RPC 7.1, https://www.sccourts.org/resources/court-rules/appellate/rule-407/rule-7-1/ |
| Lawyers may not pay for recommendations: "shall not give anything of value to a person for recommending" (SC RPC 7.2(c); IN RPC 7.2(b) reads "recommending or advertising", with listed exceptions in both). Paid-for reviews would breach that as well as the FTC rule | https://rules.incourts.gov/Content/prof-conduct/rule7-2/current.htm ; https://www.sccourts.org/resources/court-rules/appellate/rule-407/rule-7-2/ |

**FTC rule status, 2024–26 (verified).**
- 2024-08-14: the Commission announced the final rule, approved 5-0, to take effect 60 days after publication (FTC press release).
- Published 2024-08-22 (document at 89 FR 68034; the rule text and eCFR source note at 89 FR 68077). In effect 2024-10-21. eCFR lists one version, with the latest amendment on 2024-10-21. So it was unamended as of the 2026-10-15 text I pulled.
- Nov 2024: the FTC Q&A says the rule "authorizes courts to impose civil penalties for knowing violations". Its content rules reach businesses, not ordinary reviewers.
- 2025-12-22: "FTC Warns 10 Companies About Possible Violations of the Agency's New Consumer Review Rule". It cites civil penalties up to $53,088 per violation and says the letters are not findings of violation.
- 2026-04-16: a Federal Register consent-order notice (Publishing.com) charges fake-testimonial conduct under **FTC Act §5, not Part 465**. Searching the Federal Register API turned up no Part 465 enforcement order. Whether one exists elsewhere is UNVERIFIED, because the WebSearch budget ran out.

## Budget method

Signals, best first:

1. **Bar referral consult caps.**
   - SC Bar LRS: each lawyer "agrees to charge no more than $50 for a 30-minute consultation". Normal fees apply after that. LRS lawyers "do not take pro bono cases". Phone and 24/7 online referral are available (https://www.scbar.org/for-the-public/quicklinks/get-legal-help/).
   - IndyBar's Indy Lawyer Finder publishes attorney subscription fees ($300/yr members, $600/yr non-members, plus 10% on referred fees over $100) and lists Employment as a case type. It publishes **no client consult fee**, and its page doesn't confirm it covers Hamilton County (both UNVERIFIED). The program says it uses AI to match referrals.
2. **Free or low-cost help.**
   - Legal aid: ILS takes clients within 125% of FPL (200% in some cases) with under $10,000 in countable assets. It generally takes fee-generating cases only when no private attorney will, which matters because many employment claims are fee-generating. Its WRAPP project covers workers, focused on farmworkers and trafficking survivors.
   - SCLS: 125% of FPL ($19,950 for one person, 2026). Its locations page lists no Aiken office, and which office serves Aiken County is UNVERIFIED.
   - Free Legal Answers: SC via the SC Bar page; Indiana via indiana.freelegalanswers.org (linked from Indiana Legal Help; not opened).
   - Indiana Legal Help routes users by ZIP or county.
3. **Directory flags.** Lawyers.com shows a "Free Consultation" flag and filter (seen on one Noblesville firm). Treat it as self-reported.
4. **Firm-site wording.** In the dry run, the firm sites said "schedule a consultation" or "initial consultation" with no fee stated. "Free" was never claimed. The skill should report "consult fee not stated" rather than guess.
5. **Limited scope (unbundling) as a cost lever.**
   - Indiana: RPC 1.2(c) allows limiting scope "if the limitation is reasonable under the circumstances" and the client gives informed consent (current text effective Jan 1, 2005). Trial Rule 3.1(I) requires a "notice of temporary or limited representation" in court (current version effective Jan 1, 2025, per the rules site).
   - South Carolina: RPC 1.2(c) has the same core text. Comment [7] allows a brief consult only if the time is enough to "yield advice upon which the client could rely" (wording checked against the page). An SC court rule for limited-scope *appearances* was not found and is UNVERIFIED.

## Dry-run results

Two attorneys per test state. Nobody was contacted. Licences were checked in the official lookups in Claude's built-in browser pane (see the verification note on Indiana's terms). Identifying details were scrubbed from this table on 2026-10-20.

| Attorney | State | Lookup method that worked |
|---|---|---|
| Attorney A | IN | IN Roll of Attorneys, in a browser |
| Attorney B | IN | IN Roll of Attorneys, last name only, in a browser (first plus last name found nothing) |
| Attorney C | SC | SCJB Attorney Search, name search plus detail page, in a browser |
| Attorney D | SC | SCJB Attorney Search, name search plus detail page, in a browser |

What worked:
- Discovery: WebSearch snippets, and WebFetch on firm websites.
- Licence: the official lookups, in a browser.
- Directory pages: Lawyers.com, Martindale and BBB loaded, but their terms bar automated use.

What didn't:
- Avvo, Justia, LII, Yelp, FindLaw and Super Lawyers: blocked.
- Indiana Roll via WebFetch: an empty SPA shell.
- SC detail via WebFetch: needs a POST.

## Open questions

1. Should the skill drive a browser for licence checks at all? Indiana's terms bar "intelligent agents", and SC's robots.txt bars unnamed agents. The conservative design is: the skill prepares the name, city and lookup URL, Grant confirms in his own browser, and the skill records "confirmed by Grant on <date>". (Ticket 14 or 15.)
2. Does a plain link to the Indiana search page breach the "frame or link to" clause? Not resolved. The proposed design gives the search page, not a results deep link.
3. Review evidence rests on search-engine snippets. Is "snippet-derived, unverified" good enough for the *well-reviewed* criterion, or must Grant open each profile? (Ticket 14.)
4. Which SCLS office serves Aiken County? Does IndyBar's referral service cover Hamilton County, and what is its client fee? Is there an Indiana or Hamilton County bar referral service with a published fee cap?
5. Is there an SC court rule for limited-scope appearances?
6. After the follow-up verification, the per-state table has 12 UNVERIFIED rows (DE, KS, MA, MT, NV, NH, NJ, OK, RI, SD, TN and WV), and no state other than IN or SC was exercised end-to-end. Several confirmed rows also leave open whether results show status. These need Grant's own browser or a phone call to the bar.
7. Has the FTC enforced Part 465 itself (beyond the warning letters)? I found no Part 465 consent order in the Federal Register, but the search was incomplete.

## Verification note

- **Method:** each claim above was checked against the page named in its row or sentence, on 2026-10-20. I used WebFetch, which summarises pages through a small model, for most pages. I used curl text extraction for rule texts, robots.txt and terms pages, the eCFR versioner API and the Federal Register API. I used the built-in browser pane only for the four licence records and the ABA page. Quotes are under 15 words and come from page text I extracted, except where a WebFetch summary was the only view (FTC pages, ILS and SCLS guidelines). Those are faithful to the summary but weren't re-read from raw HTML.
- **Secondary sources (marked as such):** WebSearch result summaries, Avvo/Lawyers.com snippets, and firm marketing pages. They were used only to find candidates, never for licence status.
- **Limits:**
  - The shared WebSearch budget ran out partway through, so the per-state list, the "Avvo = Internet Brands" question and the Part 465 enforcement search are incomplete and marked UNVERIFIED.
  - ftc.gov returns 404 to curl, so its pages rest on WebFetch alone.
  - The browser pane was shared with another session that navigated my first tab away mid-task. Results were re-read in a fresh tab.
- **Conduct disclosure:**
  - To learn how the Indiana Roll renders, I fetched its public HTML and JS bundle with curl and read the API path from it. I didn't use that API.
  - I ran the four lookups by driving the in-app browser. Indiana's ToU (which I read afterwards) forbids non-browser software and "intelligent agents" and lists decompiling or reverse-engineering. Grant should treat those dry-run lookups as a feasibility test only, and the skill should not repeat them automatically. See open question 1.
  - No CAPTCHA was bypassed, no login was used and no account was created. No attorney names, street addresses or bar numbers are in this file.

## Sources

All accessed 2026-10-20.

| # | Source | URL | Type |
|---|---|---|---|
| 1 | Indiana Roll of Attorneys (app + record pages) | https://courtapps.in.gov/rollofattorneys/ | Primary (official) |
| 2 | IN Roll of Attorneys help | https://www.in.gov/courts/help/attorney-search | Primary |
| 3 | IN Roll of Attorneys Search Tool ToU | https://www.in.gov/courts/policies/tou-roll-of-attorneys | Primary |
| 4 | IN Online Services ToU | https://www.in.gov/courts/policies/tou | Primary |
| 5 | courtapps.in.gov robots.txt (content-signal comments only, no rules) | https://courtapps.in.gov/robots.txt | Primary |
| 6 | SC Judicial Branch Attorney Search (search + detail) | https://www.sccourts.org/attorneys/ | Primary |
| 7 | sccourts.org robots.txt | https://www.sccourts.org/robots.txt | Primary |
| 8 | SC Judicial/Legal Conduct orders | https://www.sccourts.org/opinions-orders/court-orders/judiciallegal-conduct/ | Primary |
| 9 | SC Lawyer & Judicial Discipline overview | https://www.sccourts.org/about/lawyer-judicial-discipline/ | Primary, **weak**: on re-check it is a link page (confidential-discipline summaries, annual reports) and doesn't itself explain how discipline is published |
| 10 | SC RLDE Rule 12 | https://www.sccourts.org/resources/court-rules/appellate/rule-413/rule-12/ | Primary |
| 11 | SC RPC 1.2, 7.1, 7.2 | https://www.sccourts.org/resources/court-rules/appellate/rule-407/rule-1-2/ (and `/rule-7-1/`, `/rule-7-2/`) | Primary |
| 12 | SC Bar directory page | https://www.scbar.org/lawyers/directory/ | Primary (bar) |
| 13 | SC Bar Get Legal Help (LRS) | https://www.scbar.org/for-the-public/quicklinks/get-legal-help/ | Primary (bar) |
| 14 | IN RPC 1.2 | https://rules.incourts.gov/Content/prof-conduct/rule1-2/current.htm | Primary |
| 15 | IN RPC 7.2 | https://rules.incourts.gov/Content/prof-conduct/rule7-2/current.htm | Primary |
| 16 | IN Trial Rule 3.1 | https://rules.incourts.gov/Content/trial/rule3-1/current.htm | Primary |
| 17 | IndyBar referral pages | https://www.indybar.org/?pg=lawyer-referral ; https://www.indybar.org/?pg=LawyerReferralService-HomePage | Primary (bar) |
| 18 | Indiana Legal Services eligibility; WRAPP | https://www.indianalegalservices.org/eligibility-guidelines/ ; https://www.indianalegalservices.org/wrapp/ | Primary (provider) |
| 19 | Indiana Legal Help | https://www.indianalegalhelp.org/ | Primary (provider) |
| 20 | SC Legal Services income guidelines; locations | https://sclegal.org/income-guidelines/ ; https://sclegal.org/locations/ | Primary (provider) |
| 21 | 16 CFR Part 465 (text + versions API) | https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465 | Primary |
| 22 | Federal Register, Part 465 final rule | https://www.federalregister.gov/documents/2024/08/22/2024-18519/trade-regulation-rule-on-the-use-of-consumer-reviews-and-testimonials | Primary (listed via FR API) |
| 23 | FTC press release, final rule (2024-08-14) | https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials | Primary |
| 24 | FTC Q&A on the rule (Nov 2024) | https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers | Primary |
| 25 | FTC warning letters (2025-12-22) | https://www.ftc.gov/news-events/news/press-releases/2025/12/ftc-warns-10-companies-about-possible-violations-agencys-new-consumer-review-rule | Primary |
| 26 | FTC platform guide (Jan 2022) | https://www.ftc.gov/business-guidance/resources/featuring-online-customer-reviews-guide-platforms | Primary |
| 27 | FTC consumer guide (Oct 2022) | https://consumer.ftc.gov/articles/how-evaluate-online-reviews | Primary |
| 28 | Federal Register, Publishing.com consent notice (2026-04-16) | https://www.federalregister.gov/documents/2026/04/16/2026-07420/ | Primary |
| 29 | Yelp ToS; robots.txt | https://terms.yelp.com/tos/en_us/20260101_en_us/ ; https://www.yelp.com/robots.txt | Primary (site terms) |
| 30 | BBB terms; robots.txt | https://www.bbb.org/terms-of-use ; https://www.bbb.org/robots.txt | Primary (site terms) |
| 31 | Internet Brands ToU (Martindale, Lawyers.com footer link; last updated Aug 30, 2023, a date the verifier did not re-read); Supplemental Terms for Legal Sites (updated Feb 23, 2026; names Avvo, FindLaw, LawInfo, Lawyers.com, Martindale, Nolo in its product list) | https://www.internetbrands.com/ibterms/ ; https://www.internetbrands.com/ibterms/supplementallegalterms/ | Primary (site terms) |
| 31a | Avvo ownership: ABA Journal, "Internet Brands renames legal offerings as Martindale-Avvo" (2018) | https://abajournal.com/news/article/internet_brands_renames_legal_offerings_as_martindale_avvo | Secondary (seen as WebSearch result; not opened) |
| 31b | FindLaw corporate background ("acquired by parent company Internet Brands" in 2024); Super Lawyers homepage structured data | https://www.findlaw.com/company/company-history/findlaw-corporate-information-press-company-background.html ; https://www.superlawyers.com/ | Primary (company's own pages) |
| 32 | Martindale and Lawyers.com robots.txt + browse pages | https://www.martindale.com/robots.txt ; https://www.lawyers.com/robots.txt | Primary (site) |
| 33 | Google Terms; robots.txt | https://policies.google.com/terms ; https://www.google.com/robots.txt | Primary (site terms) |
| 34 | Avvo, Justia robots.txt (sites themselves 403) | https://www.avvo.com/robots.txt ; https://www.justia.com/robots.txt | Primary (site) |
| 35 | ABA Bar Directories and Lawyer Finders | https://www.americanbar.org/groups/legal_services/flh-home/flh-bar-directories-and-lawyer-finders/ | Primary (ABA), browser only |
| 36 | Per-state lookup pages | see the per-state table | Primary (each state); "loads" check only |
| 37 | WebSearch summaries, directory snippets, firm websites | (not cited for facts beyond candidate discovery) | **Secondary** |

## Independent verification (2026-10-20)

An independent verifier re-checked this file using WebFetch and WebSearch only. They didn't drive a browser, look up any attorney, fetch the Indiana Roll app, or bypass any CAPTCHA.

**Re-opened:**
- Indiana: both Indiana ToU pages, courtapps.in.gov robots.txt, and the IN Roll help page.
- South Carolina:
  - sccourts.org robots.txt.
  - The SCJB Attorney Search landing page (no search was run).
  - The SC Bar directory page and the Judicial/Legal Conduct orders page.
  - The Court Order Search page and the discipline overview page.
  - RLDE Rule 12 and SC RPC 1.2, 7.1 and 7.2.
- Indiana rules: IN RPC 1.2 and 7.2, and Trial Rule 3.1.
- Referral and legal aid: the SC Bar LRS page, both IndyBar pages, the ILS eligibility and WRAPP pages, Indiana Legal Help, and the SCLS income and locations pages.
- FTC rule:
  - The eCFR versions, structure and full-text APIs for Part 465.
  - The FR API entries for 2024-18519 and 2026-07420, plus the 2026-07420 full text.
  - The FTC final-rule press release, Q&A, warning-letter release, platform guide and consumer guide.
- Review sites:
  - robots.txt for Yelp, BBB, Martindale, Lawyers.com, Google, Avvo and Justia.
  - Terms for Yelp, BBB, Google and Internet Brands, plus IB's legal-sites supplemental terms.
  - The Martindale and Lawyers.com browse pages.
  - Fetch tests of Avvo, Justia, Yelp, LII, FindLaw, Super Lawyers, BBB and the ABA page.
- Per-state lookups (16 rows): CA, IL, CT, OH, WI, PA, ID, ME, NE, NC, AZ, TN, GA, MN, CO and NY.

**Counts:** 62 confirmed, 10 corrected, 1 removed, 7 newly marked UNVERIFIED. The UNVERIFIED items the original author had already flagged stay as they were.

**Corrections:**
1. FindLaw and Super Lawyers are owned by Internet Brands, not Thomson Reuters. FindLaw's own page says IB acquired it in 2024, and Super Lawyers' structured data names IB as its parent.
2. The FindLaw and Super Lawyers homepages loaded to WebFetch. They did not return 403. Their directory pages were not re-tested.
3. Avvo is an Internet Brands property, so it is no longer UNVERIFIED. ABA Journal reported the 2018 acquisition and the Martindale-Avvo rebrand, and IB's legal-sites terms name Avvo.
4. Google robots.txt disallows `/maps/`, but it explicitly allows `/maps/place/` and `/maps/search/`. "Robots-disallowed" was wrong for place pages. The review design doesn't change, because the page is a JS app and the Google terms still apply.
5. §465.7(b) does not ban showing only favourable reviews as such. It bars implying that the displayed reviews are all or most of them while negatives are suppressed by rating or sentiment.
6. The FR document 2024-18519 starts at 89 FR 68034. 89 FR 68077 is the eCFR source note, which points at the regulatory text. Both citations are now given.
7. The SC Court Order Search has no name field. It searches by order type, affected court, or full-text keyword.
8. The SC conduct-orders year dropdown has gaps, such as 1990–91 and 1995–98.
9. The IN RPC 7.2(b) wording is "recommending or advertising". The quoted fragment matches SC RPC 7.2(c) exactly.
10. The PA heading is "Look Up an Attorney".

**Additions (confirmed, not corrections):**
- The Indiana Online Services ToU also bars "using any software other than a web browser", and its "frame or link to" clause covers the Application itself.
- sccourts.org robots.txt also disallows GPTBot and sets `Crawl-delay: 120000`. It names no Claude agent, so Claude-User falls under `User-agent: *` / `Disallow: /`.
- BBB robots.txt also disallows `/business-reviews/*`. BBB's terms have no explicit robot clause.
- SCLS allows some exceptions up to 200% FPL.
- The Lawyers.com `?review=` disallow applies only after a path segment.
- Source 9 is flagged as weak.

**Removed (privacy scrub):** a profile ZIP code, from one Indiana dry-run row. The scrub found no attorney names, bar numbers, firm names, attorney phone numbers or street addresses. The one phone number in the file is the SC Bar LRS public line, which belongs to the organisation and was kept.
- The dry-run rows still carried admission years and an out-of-state office city. These were removed in the follow-up below.

**Newly UNVERIFIED:**
1. The Roll footer phrase "Data mining… prohibited by Supreme Court rule". It is in neither ToU page, and the app itself was not fetched.
2. The Martindale footer link to the IB terms. The footer was not in the WebFetch text.
3. Whether avvo.com links to the IB terms. avvo.com returns 403.
4. The Lawyers.com CAPTCHA marker. This was a curl-only finding, and WebFetch showed none.
5. Whether the SC full-text order search covers conduct orders.
6. The IB ToU "last updated" date. The verifier did not re-read it.
7. TN. It returns 403 to WebFetch, so the curl "loads" finding could not be re-checked.

**Not checked:**
- **By rule:** the four dry-run licence results, Indiana Roll record fields, the "July 1, 1986" caveat and the "0 of 0" loading behaviour (all inside the app). Also the SC search's GET results and its POST/anti-forgery detail mechanics, since no search was run.
- **No curl access:** the curl-only observations (byte sizes, challenge or CAPTCHA markers, ftc.gov returning 404 to curl).
- **Not re-opened:** 34 per-state rows, the Yelp and Google pages themselves, and the Lawyers.com JSON-LD ratings.

**Design conclusion holds:** the skill gives Grant the official search page plus the last name and city, and Grant confirms the result in his own browser. Three findings support it:
- The Roll ToU bars "intelligent agents" except a normal browser.
- The Online Services ToU bars non-browser software and automated collection.
- sccourts.org robots.txt disallows all unnamed agents.

The dry run, in which Claude drove a browser, plausibly falls under "intelligent agents" itself. The skill must not repeat it. The "link to" clause remains open: the Online Services ToU says "link to an Application", so even handing over the search-page URL may arguably fall under it. Fallback: name the site, "Indiana Roll of Attorneys on in.gov/courts", and let Grant navigate to it.

### Follow-up verification

A second pass on 2026-10-20 covered the 34 states the first verifier didn't re-open, plus DC, so 35 rows. It used WebFetch on each listed URL and on the authority's own linking pages, with WebSearch only to find official URLs. It didn't drive a browser, run any search for an attorney, or bypass any CAPTCHA or bot check. The Indiana Roll app wasn't fetched, because its ToU bars it; the in.gov help page confirms the link. The per-state rows make no robots.txt claims, so no robots.txt was fetched.

**Counts (35 rows):** 19 confirmed, 5 corrected, 11 UNVERIFIED.
- **Confirmed (19):** AL, AR, DC, FL, IA, IN, KY, LA, MI, MS, ND, NM, OR, SC, TX, UT, VA, WA and WY. For MS and WA this resolves an earlier doubt. MS: the Bar names its ReliaGuide directory as its status source. WA: the https URL loads with no SSO redirect. For AL, AR, KY, NM, OR, UT and WY, the page is the official one, but whether results show status is still UNVERIFIED.
- **Corrected (5):**
  - AK: the old profile URL now shows a template error; replaced with alaskabar.org's Member Directories page.
  - HI: the referral landing page was replaced with `/member-directory`.
  - MD: the AIS page was replaced with `/attysearch`, the Maryland Attorney Listing, which shows status.
  - MO: the old URL is a 404; replaced with the Official Missouri Directory of Lawyers.
  - VT: `/attorneys` was replaced with the Attorney Licensing page, which links a static good-standing list rather than a search.
- **UNVERIFIED (11):**
  - Newly marked (5):
    - MA: a JS shell with no operator shown.
    - MT: the URL was corrected, but the directory showed no search fields and may need a login.
    - NV: the old URL is a referral page; removed.
    - OK: the old URL is an opt-in listing; removed. The member directory needs a login.
    - WV: 403.
  - Still UNVERIFIED with new detail (6):
    - DE: no public lookup; certificates go through the DSCLMS login.
    - KS: the URL was corrected from `.org` to `.gov` per WebSearch, but both hosts are blocked.
    - NH: only a verification-request form exists; the directory needs a login.
    - NJ: the NJ Attorney Index was found via the DRB portal but hit a bot check.
    - RI: the URL is confirmed as linked from courts.ri.gov, but the tool resets the connection.
    - SD: no online lookup found; DOJ EOIR says to call the State Bar.
- **Markers:** WebFetch confirmed a robot check on DC and a CAPTCHA on LA. For AK, FL, KY, MI, ND, NV and WY it saw no challenge. The curl markers stay as recorded but were not re-tested.

**Privacy scrub:** the dry-run table now holds only Attorney A–D, the state and the lookup method that worked. These were removed: the admission years, the out-of-state office city, the test-location cities, status wording, practice and firm notes, and the middle-name detail. Two references elsewhere were reworded to match: Indiana step 1 and the review-snippet note.
