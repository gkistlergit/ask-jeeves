---
area: attorney-finder
as_of: 2026-10-20
verified: 2026-10-20
sources: research/06-attorney-finder-sources.md (+ independent and follow-up verification); research/07-live-location.md (+ independent verification); decisions in .scratch/ask-jeeves/issues/14-attorney-finder-criteria.md and 15-safeguards.md
---
# Attorney finder: procedure

> For issue-spotting only. Not legal advice. Every claim cites its source; [UNVERIFIED] marks claims that could not be confirmed. Jeeves never contacts, hires or messages an attorney.

This is an operational procedure, not a summary of law. The *attorney finder* returns a short ranked list of license-confirmed, customer-reviewed, budget-friendly attorneys for one *location option* (see `CONTEXT.md`). Follow the steps in order.

## 0. When it runs
- Only when Grant opts in after the memo. For a *live matter* (ticket 15 intake screen), Jeeves writes no memo and offers only the attorney finder. [cite: ticket 14; ticket 15]
- It runs as a subagent at every depth, under `references/research-resilience.md`: WebSearch and WebFetch only, no browser, computer-use or clipboard, and no nested subagents. [cite: ticket 14; research-resilience §3–4]
- Inputs it needs from the memo: the *mode* (employer or employee) and the *applied state*. Nothing else from the request goes to the subagent. [cite: ticket 14; ticket 15]

## 1. Opt-in and the location picker
Ask one AskUserQuestion, **multi-select**. Search each chosen location separately and give each its own list. [cite: ticket 14]

| Option | What Jeeves does |
|---|---|
| **My live location** | Consent first, then the Jeeves Location app, then the IP fallback, then typed entry (below) |
| **Type a ZIP** | Ask for the ZIP. Sends nothing anywhere until the search |
| **Home: Noblesville, IN 46060** | Use exactly this city and ZIP. Never any street address |
| **Aiken, SC** | Use the city and state |

**Home.** The skill stores the home location as "Home: Noblesville, IN 46060" only. A street address never goes into skill files, URLs, queries or saved files. [cite: ticket 15]

**Live location, in order:**
1. **Consent.** Ask: may I check your location? Say Jeeves keeps only city and ZIP, and that the result enters this conversation, which goes to Anthropic. Ask every time; never assume a past yes. [cite: research 07 §4; ticket 15]
2. **Device (Jeeves Location app).** Run the bundled helper:
   ```bash
   <skill folder>/scripts/jeeves-location/run.sh
   ```
   - It builds and ad-hoc signs `Jeeves Location.app` on first use (`build.sh`, output in its gitignored `build/`), opens it, and prints `City|ZIP`. Coordinates are never printed or saved. Apple's geocoder turns the fix into a city and ZIP, so tell Grant his location goes to Apple for that step.
   - macOS shows its own prompt for "Jeeves Location" the first time. Grant's answer stays in System Settings → Privacy & Security → Location Services, where he can remove it to be asked again. Jeeves still asks for consent in chat every run (step 1).
   - On `DENIED`, `FAILED`, `GEOCODE_FAILED` or `TIMEOUT` (90 s): don't retry in a loop. Go to step 3.
   - Why an app: a bare script or `swift` run gets no prompt and an immediate denial, since locationd only prompts a bundled app with a location usage string. Checked on this Mac on 2026-10-20 (macOS 27), where it returned the correct city and ZIP.
   - The Shortcuts route (`shortcuts run 'Jeeves Location' --output-path -`, from research 07) is an untested alternative if Grant builds that shortcut by hand. The CLI can't create shortcuts. [cite: research 07 §2b, §4; https://support.apple.com/guide/shortcuts-mac/apd455c82f02/mac]
3. **IP fallback (approximate).** Offer it; use it only if Grant agrees. Disclose all three every time: it is **approximate** (ISP or VPN exit; iCloud Private Relay changes it), it **sends Grant's IP to ip-api.com**, and it uses **plain HTTP**. [cite: research 07 §3; https://ip-api.com/docs/api:json]
   ```bash
   curl -sS --max-time 5 'http://ip-api.com/json/?fields=status,message,city,zip'
   ```
   - Use it only when `status` is `"success"`. Label it "approximate (from your internet connection)". [cite: research 07 §4]
   - Run it with `curl` from Bash, never WebFetch: WebFetch upgrades HTTP to HTTPS, and the free endpoint has no HTTPS. [cite: research 07 §3; https://ip-api.com/docs/api:json]
   - Free tier: non-commercial use, 45 requests/min, no key; IPs held in RAM "for up to 1 minute". [cite: https://ip-api.com/docs/api:json; https://ip-api.com/docs/legal]
4. **Typed entry.** Always available as the last resort or by choice. It sends nothing anywhere. [cite: research 07 §4]
5. **Confirm back.** "I have <city>, <ZIP>. Use it?" Let Grant correct it. Keep only city and ZIP; coordinates never leave the location helper. Don't write the location to files or memory. [cite: research 07 §4; ticket 15]

## 2. Mismatch check
- For each location, compare its state with the applied state. If they differ, that is a *mismatch*. [cite: ticket 14; CONTEXT.md]
- Say so, then ask before searching that location, with exactly these options: [cite: ticket 14]
  - *Licensed in <applied state>*
  - *Licensed in <location state>*
  - *Both*
- The answer sets the license state(s) for that location's list and its header line.

## 3. Search
### Query rules (privacy)
- **Discovery queries** contain only the city or ZIP plus generic terms, for example "employment lawyer Noblesville IN 46060" or "employee-side employment attorney 29801". [cite: ticket 14; ticket 15]
- **Review queries** for a shortlisted candidate may name the attorney or firm plus the city, for example "<attorney name> <city> reviews". An attorney's name is public professional information. Nothing about Grant or his matter goes in. [cite: research 06; clarification of ticket 14, 2026-10-20]
- Never put party names, contract text, personal facts or any street address in a query or URL. [cite: ticket 15]
- Side terms are generic too: "employee" or "plaintiff" for employee mode; "management-side" or "employer defense" for employer mode. [cite: ticket 14 practice match]

### Budget
- At most **8 WebSearch calls per location**. WebFetch of a firm's own site or an official URL is preferred over another search. [cite: ticket 14; research-resilience §1]
- On a rate-limit or quota error: stop searching, finish with WebFetch, mark what's unchecked [UNVERIFIED], and say the search limit was hit. [cite: research-resilience §1]
- Never bypass a CAPTCHA, login, bot check or "Just a moment" challenge. Try each source once, then move on. [cite: research-resilience §2]

### What tools can and can't read
Review evidence comes from **WebSearch snippets** plus **firm websites via WebFetch**, and links Grant opens himself. Label snippet ratings "snippet-derived (secondary)". [cite: research 06 summary, review-quality method]

| Source | Tool access | Use it as |
|---|---|---|
| Firm websites | WebFetch works (4 of 4 in dry run) | Practice area, side, consult wording, fees if stated |
| Avvo | 403, Cloudflare challenge; Internet Brands property | Snippets only; give Grant the profile link |
| Justia | 403, Cloudflare challenge | Snippets only |
| Cornell LII directory | 403 / WAF | Snippets only |
| Yelp | 403; robots.txt disallows Claude-User; ToS bans robots | Snippets only |
| Google Maps reviews | JS app; terms bar automated access against robots instructions | Snippets (sometimes carry the rating) |
| Martindale, Lawyers.com | Load to WebFetch, but Internet Brands terms ban robots and scrapers (search engines excepted) | Snippets only. Martindale's "x/5.0 (n)" is a **peer** rating; never mix it with client reviews |
| FindLaw, Super Lawyers | Homepages loaded on re-check; directory pages not re-tested; Internet Brands terms | Snippets only |
| BBB | Loads; robots.txt disallows query URLs and `/business-reviews/*` for Claude-User; terms bar aggregation | Snippets only |

[cite: research 06 source-capability table and verification corrections 1–4; https://www.internetbrands.com/ibterms/ ; https://www.yelp.com/robots.txt ; https://www.bbb.org/robots.txt ; https://policies.google.com/terms]

## 4. Who qualifies (thresholds, from ticket 14)
A candidate must meet **all** of these. [cite: ticket 14]
- **Practice match.** Employment law, on the right side for the mode: employee-side for employee mode, management-side for employer mode.
  - Prefer the firm's own site as evidence of side. If it can't be opened, the attorney's own directory profile text may stand in; say so on the entry. [cite: ticket 25 test]
- **Reviews.** At least a **4.3-star** average, from at least **10 reviews** across at least **2 independent sources**, with at least one review in the **last 24 months**.
  - **Recency** is met when any one source shows a review dated within 24 months. Undated sources still count toward the rating, the review count and the 2-source rule. [cite: ticket 25]
  - **Independent** means a distinct review platform (Google, Avvo, Yelp, BBB, Lawyers.com, a firm-independent directory). An aggregator that republishes another platform's reviews, such as TrustAnalytica or LeadStal mirroring Google, counts as that platform, never as a second source. [cite: ticket 25]
  - **The 4.3 average** is weighted by review count across the counted sources. Facebook counts as a platform. A firm's reviews and its named attorneys' reviews may be pooled into one candidate that names those attorneys. [cite: ticket 25 test]
  - Record the rating, the count and the latest review date for each source **as seen**. Never estimate them.
  - Watch for FTC fake-review signals (16 CFR 465; §5 below). Flag a candidate with those signals; drop it when the signals are strong.
- **Budget: free or close to free.** At least one of these must be **published**:
  - a **free consultation**;
  - a consultation of **$50 or less**;
  - the **bar lawyer-referral service** route (SC Bar LRS: ≤$50 for 30 min);
  - **legal aid** eligibility (125% FPL);
  - **limited-scope** help (RPC 1.2(c)).
- A fee appears only when a source states it; otherwise it reads "unknown". An explicit "free consultation" or "free case evaluation" counts as a published free consult. "Initial consultation" or "book a consultation" with no fee stays "unknown", never "free". [cite: ticket 14; ticket 25; research 06 budget method 4]
- **Fewer than 3 qualify:** say so, and list the bar referral service and legal aid as the budget route (§6). Don't lower the bar quietly. Fill the gap with the **strong, not fully confirmed** tier below, never by relaxing a threshold. [cite: ticket 14; ticket 25]
- **License.** Nobody is listed as confirmed until Grant confirms an active license (§7).

### Strong, not fully confirmed (second tier)
Shown only when fewer than 3 qualify, with at most 3 entries, ranked like the qualified list. [cite: ticket 25]
- **Still required:** practice match on the right side; at least 4.3 stars from at least 10 reviews in total; no strong fake-review signal (§5). The license reads "pending your check", as for everyone.
- **May be missing,** in any combination:
  - **recency:** no review dated within 24 months on any source (undated, or only older dates seen);
  - **second source:** one platform only, which must then show at least **50** reviews;
  - **published fee:** fee "unknown".
- Each entry names exactly which of these it is missing, so Grant knows what to check himself. For a missing fee, the line reads "ask about the consult fee".
- These are never ranked with, or described as, qualified attorneys.

## 5. Fake-review signals (FTC)
16 CFR Part 465 has been in force since 2024-10-21 and was unamended as of the 2026-10-15 eCFR text. [cite: 16 CFR 465, https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465 ; 89 FR 68034 (Aug. 22, 2024), https://www.federalregister.gov/documents/2024/08/22/2024-18519/trade-regulation-rule-on-the-use-of-consumer-reviews-and-testimonials]

**Check for these (ticket 14's list first):**
- A **burst** of 5-star reviews over a short period. [cite: FTC, How To Evaluate Online Reviews (Oct 2022), https://consumer.ftc.gov/articles/how-evaluate-online-reviews]
- **Generic** text, and slightly-under-perfect fakes. [cite: same]
- Reviewers with **no history** (accounts with a single review). [cite: same]
- **Review gating**: selective solicitation, sentiment-conditioned incentives, suppressing negatives, uneven moderation, closed vs. open collection. [cite: FTC, Featuring Online Customer Reviews: A Guide for Platforms (Jan 2022), https://www.ftc.gov/business-guidance/resources/featuring-online-customer-reviews-guide-platforms]
- Incentive badges; fake negatives against competitors. Cross-check several sources. [cite: FTC consumer guide, above]

**Practices the rule makes illegal (signals of a bad listing):**
- Fake reviewers or experiences. [cite: 16 CFR 465.2, eCFR URL above]
- Buying reviews conditioned on sentiment. [cite: 16 CFR 465.4]
- Undisclosed insider reviews by officers, managers, employees or relatives. [cite: 16 CFR 465.5]
- Company-controlled "independent" review sites. [cite: 16 CFR 465.6]
- Suppressing reviews by unfounded threats or intimidation (§465.7(a)), or implying the shown reviews are all or most of them while negatives are suppressed by rating or sentiment (§465.7(b)). Showing only favourable reviews is not itself banned; neutral exclusions such as likely-fake reviews are allowed. [cite: 16 CFR 465.7]
- Fake social-media indicators. [cite: 16 CFR 465.8]

**Lawyer-specific red flags:**
- SC: a testimonial must say it is one, disclose payment, say whether a non-client wrote it, and state that one result doesn't promise others. A firm-site testimonial missing these is a red flag. [cite: SC RPC 7.1(d), https://www.sccourts.org/resources/court-rules/appellate/rule-407/rule-7-1/]
- Lawyers may not pay for recommendations: SC RPC 7.2(c) "shall not give anything of value to a person for recommending"; IN RPC 7.2(b) reads "recommending or advertising". Both have listed exceptions. [cite: https://www.sccourts.org/resources/court-rules/appellate/rule-407/rule-7-2/ ; https://rules.incourts.gov/Content/prof-conduct/rule7-2/current.htm]

**Reading counts.** Under about 10 reviews is weak evidence either way, which is why the threshold is 10. [cite: research 06 review-quality method]

**Enforcement context.** Courts may impose civil penalties for knowing violations; the FTC sent its first warning letters under the rule on 2025-12-22 (letters are not findings of violation). [cite: FTC Q&A (Nov 2024), https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers ; https://www.ftc.gov/news-events/news/press-releases/2025/12/ftc-warns-10-companies-about-possible-violations-agencys-new-consumer-review-rule] [UNVERIFIED: whether any Part 465 enforcement order exists beyond the letters; search incomplete]

## 6. Budget routes
### Free or ≤$50 consult
- Accept only a fee a source states: the firm's own site, or a directory "Free Consultation" flag (Lawyers.com has one; treat it as self-reported). [cite: research 06 budget method 3–4; ticket 14]

### South Carolina Bar Lawyer Referral Service
- Each lawyer agrees to charge "no more than $50 for a 30-minute consultation"; normal fees apply after. LRS lawyers don't take pro bono cases. Phone (803) 799-7100 and 24/7 online referral. [cite: https://www.scbar.org/for-the-public/quicklinks/get-legal-help/]
- SC Free Legal Answers is reached through the same SC Bar page. [cite: same]

### IndyBar Indy Lawyer Finder (fee unknown)
- Lists Employment as a case type and uses AI to match referrals. It publishes attorney subscription fees but **no client consult fee**: report "fee unknown". [UNVERIFIED: client fee not published; Hamilton County coverage not confirmed] [cite: https://www.indybar.org/?pg=lawyer-referral ; https://www.indybar.org/?pg=LawyerReferralService-HomePage]

### Legal aid (125% FPL)
- **Indiana Legal Services:** free civil aid within 125% of FPL (200% in some cases), under $10,000 countable assets. It generally takes fee-generating cases only when no private attorney will, and many employment claims are fee-generating. Its WRAPP project serves workers, focused on farmworkers and trafficking survivors. [cite: https://www.indianalegalservices.org/eligibility-guidelines/ ; https://www.indianalegalservices.org/wrapp/]
- **Indiana Legal Help:** routes by ZIP or county; links Free Legal Answers and clinics. [cite: https://www.indianalegalhelp.org/] [UNVERIFIED: indiana.freelegalanswers.org linked, not opened]
- **South Carolina Legal Services:** 125% of FPL ($19,950 for one person, 2026), some exceptions up to 200%. [cite: https://sclegal.org/income-guidelines/] [UNVERIFIED: which office serves Aiken County; the locations page lists no Aiken office, https://sclegal.org/locations/]

### Limited scope (unbundling)
- **Indiana:** RPC 1.2(c) allows limiting scope "if the limitation is reasonable under the circumstances" with informed consent. [cite: IN RPC 1.2(c), https://rules.incourts.gov/Content/prof-conduct/rule1-2/current.htm]
- **Indiana court work:** Trial Rule 3.1(I) requires a "notice of temporary or limited representation" (version effective Jan 1, 2025). [cite: IN TR 3.1(I), https://rules.incourts.gov/Content/trial/rule3-1/current.htm]
- **South Carolina:** RPC 1.2(c) has the same core text; Comment [7] allows a brief consult only if it can "yield advice upon which the client could rely". [cite: SC RPC 1.2, https://www.sccourts.org/resources/court-rules/appellate/rule-407/rule-1-2/] [UNVERIFIED: no SC court rule for limited-scope appearances found]

## 7. License and discipline: Grant checks
- **Jeeves never fetches, scrapes or browser-drives a license lookup in IN or SC.** It gives the official site and the exact search terms; Grant checks in his own browser and reports back. [cite: ticket 14; research 06 verification "design conclusion holds"]
- Each candidate reads "License: pending your check" until Grant reports back. Drop anyone he can't confirm as active. Record "confirmed by Grant on <date>". [cite: ticket 14; research 06 open question 1]
- Give **last name plus city** as the search. Firm sites use nicknames and middle names, which broke a first-plus-last search in the dry run. [cite: research 06 summary; https://www.in.gov/courts/help/attorney-search]
- The dry-run lookups, where Claude drove a browser, were a feasibility test only. Don't repeat them. [cite: research 06 conduct disclosure]

### Indiana
- **Site:** name it as "Indiana Roll of Attorneys on in.gov/courts" and give the help page, https://www.in.gov/courts/help/attorney-search. Don't hand out the app URL or a results deep link. [cite: ticket 14; research 06 verification fallback]
- **Why:** the Roll terms bar "spiders, robots, avatars, intelligent agents" other than a normal browser, and list "frame or link to" among prohibited acts. The Online Services terms bar "using any software other than a web browser" and linking to an Application. [cite: https://www.in.gov/courts/policies/tou-roll-of-attorneys ; https://www.in.gov/courts/policies/tou] [UNVERIFIED: whether a plain link in chat counts as "link to"; this is the conservative reading]
- **Search tips:** last name is required; city filters; last-name search matches partial strings. [cite: https://www.in.gov/courts/help/attorney-search]
- **Record shows** license status (e.g. *Active In Good Standing*), status date, admit date, firm and "Disciplinary information", with history from July 1, 1986 and pending vs. concluded cases. [cite: research 06 Indiana steps 3, seen in the dry run; not re-checked by the verifier because the app is off-limits]
- **False negative:** the app briefly shows "0 of 0" while loading. Tell Grant to wait for it. [cite: research 06 summary]
- **Discipline:** on the Roll record itself. [cite: ticket 14]

### South Carolina
- **Site:** SC Judicial Branch Attorney Search, https://www.sccourts.org/attorneys/. The SC Bar's own directory needs a login and sends the public here to verify status. [cite: https://www.scbar.org/lawyers/directory/]
- **Why not fetch:** sccourts.org robots.txt is `User-agent: *` / `Disallow: /` and names no Claude agent. The detail page also needs a form POST with an anti-forgery token. [cite: https://www.sccourts.org/robots.txt ; research 06 SC steps]
- **Detail shows** bar number, county, firm, SC Admission Date, Membership Class and Membership Status (e.g. *Good Standing*). **No discipline section.** [cite: research 06 SC step 2]
- **Discipline:** Grant checks the Supreme Court's Judicial/Legal Conduct orders, filtered by year (dropdown back to 1978, with gaps such as 1990–91 and 1995–98): https://www.sccourts.org/opinions-orders/court-orders/judiciallegal-conduct/. The Court Order Search has no name field; a name only goes in as a full-text keyword. [cite: research 06 SC step 3, verification corrections 7–8] [UNVERIFIED: whether full-text search covers conduct orders]
- **Limits of a clean record:** formal charges go public "30 days after the filing of the answer"; earlier complaints stay confidential, so a clean record doesn't prove no complaint. [cite: SC RLDE Rule 12(a)–(b), https://www.sccourts.org/resources/court-rules/appellate/rule-413/rule-12/]

### Any other state
- Prefer the licensing authority (state supreme court, registration office, or a mandatory bar acting for the court). Use a voluntary bar's referral page only as a last resort; status must come from the authority. [cite: research 06 general method]
- Match bar number, admission date and city against the attorney's own site. Get discipline from the authority's public-discipline records. [cite: same]
- Grant opens the lookup by default. Jeeves may WebFetch it only after reading that state's robots.txt and terms and finding they allow it, and never past a CAPTCHA, login or bot check. Status still reads "pending your check" until Grant confirms. [cite: ticket 14; research-resilience §2]

### Official lookup per state
"Loads" = the page returned on 2026-10-20 with the stated title, or was linked from the authority's own site. **Loads does not mean a search was run;** only IN and SC were exercised end-to-end. "Re-checked" = reopened by a verifier. [cite: research 06 per-state table, independent and follow-up verification]

| State | Official lookup | Status |
|---|---|---|
| AL | https://members.alabar.org/Member_Portal/Member_Portal/Member-Search.aspx | Loads, re-checked; no login. Shows status? UNVERIFIED |
| AK | https://alaskabar.org/for-lawyers/member-directories/ | Corrected URL. Shows status? UNVERIFIED. Discipline: https://justiceweb.alaskabar.org/justiceweb (linked, not opened) |
| AZ | https://www.azbar.org/for-legal-professionals/practice-tools-management/member-directory/ | Loads, re-checked |
| AR | https://attorneyinfo.aoc.arkansas.gov/info/attorney/attorneysearch.aspx | Loads, re-checked; no login. Shows status? UNVERIFIED |
| CA | https://apps.calbar.ca.gov/attorney/LicenseeSearch/QuickSearch | Loads, re-checked |
| CO | https://www.coloradolegalregulation.com/attorney-search/ | Loads, re-checked (includes disciplinary history); challenge marker |
| CT | https://lookup.jud.ct.gov/AttorneyFirm | Loads, re-checked |
| DE | none found | UNVERIFIED. ODC Digest of Lawyer Discipline only (https://courts.delaware.gov/odc/); good-standing certificates via DSCLMS login |
| DC | https://my.dcbar.org/memberdirectory | Loads, re-checked; robot check on the page |
| FL | https://www.floridabar.org/directories/find-mbr/ | Loads, re-checked; "Eligible lawyers only" filter |
| GA | https://www.gabar.org/member-directory/ | Loads, re-checked |
| HI | https://hsba.org/member-directory | Corrected URL; says it shows whether the attorney can actively practice; needs JS |
| ID | https://isb.idaho.gov/licensing-mcle/attorney-roster-search/ | Loads, re-checked |
| IL | https://www.iardc.org/Lawyer/Search | Loads, re-checked (ARDC) |
| IN | "Indiana Roll of Attorneys on in.gov/courts"; help page https://www.in.gov/courts/help/attorney-search | **Verified end-to-end** (browser only). Name the site; don't link the app (terms) |
| IA | https://www.iacourtcommissions.org/ ("Search the Lawyer Database"; also discipline orders) | Links found, re-checked; session-based URLs |
| KS | https://directory-kard.kscourts.gov/ | UNVERIFIED. URL from secondary source; host blocked to tools |
| KY | https://kybar.org/For-Public/Find-a-Lawyer | Loads, re-checked. Shows status? UNVERIFIED. Suspended/disbarred list: https://kybar.org/For-Public/KBA-Currently-Suspended-and-Disbarred-Lawyers |
| LA | https://www.lsba.org/MD321654/MembershipDirectory.aspx | Loads, re-checked; CAPTCHA gates it (Grant opens) |
| ME | https://apps.web.maine.gov/cgi-bin/online/maine_bar/attorney_directory.pl | Loads, re-checked |
| MD | https://www.mdcourts.gov/attysearch | Corrected URL; shows active or inactive/retired status |
| MA | https://www.massbbo.org/s/attorney-lookup | UNVERIFIED. JS shell names no operator |
| MI | https://dir.michbar.org/ | Loads, re-checked; lets you check status |
| MN | https://mars.courts.state.mn.us/ | Loads, re-checked |
| MS | https://msbar.reliaguide.com/home | Loads, re-checked; needs JS; the Bar's named status source |
| MO | https://mobar.org/public/LawyerDirectory.aspx | Corrected URL; lists every lawyer in good standing |
| MT | https://www.montanabar.org/For-Attorneys/Attorney-Directory | UNVERIFIED. No search fields seen; may need login |
| NE | https://attorneys.nejudicial.gov/member-search | Loads, re-checked |
| NV | none found | UNVERIFIED. Bar Status page (https://nvbar.org/for-lawyers/membership/bar-status/) defines categories but links no lookup |
| NH | https://www.nhbar.org/attorney-verification-good-standing-request | UNVERIFIED as a lookup: request form only; directory needs login |
| NJ | https://drblookupportal.judiciary.state.nj.us/ (links "NJ Attorney Index") | UNVERIFIED. Index hit a bot check |
| NM | https://www.sbnm.org/For-Public/I-Need-a-Lawyer/Online-Bar-Directory | Loads, re-checked. Shows status? UNVERIFIED |
| NY | https://iapps.courts.state.ny.us/attorneyservices/search | UNVERIFIED content; Cloudflare challenge |
| NC | https://portal.ncbar.gov/verification/search.aspx | Loads, re-checked |
| ND | https://www.ndcourts.gov/lawyers | Loads, re-checked; "By Status" filter |
| OH | https://www.supremecourt.ohio.gov/AttorneySearch/ | Loads, re-checked |
| OK | none found | UNVERIFIED. OBA listing is opt-in; member directory needs login |
| OR | https://www.osbar.org/members/membersearch_start.asp | Loads, re-checked. Shows status? UNVERIFIED |
| PA | https://www.padisciplinaryboard.org/for-the-public/find-attorney | Loads, re-checked ("Look Up an Attorney") |
| RI | https://rijrs.courts.ri.gov/rijrs/attorney.do | UNVERIFIED. Linked by courts.ri.gov; tools get a connection reset |
| SC | https://www.sccourts.org/attorneys/ | **Verified end-to-end** (detail needs a browser) |
| SD | none found | UNVERIFIED. DOJ EOIR says call the State Bar (https://www.justice.gov/eoir/attorney-licensing-verification) |
| TN | https://www.tbpr.org/attorneys | UNVERIFIED. Loaded to curl; 403 to WebFetch on re-check |
| TX | https://www.texasbar.com/AM/Template.cfm?Section=Find_A_Lawyer&Template=/CustomSource/MemberDirectory/Search_Form_Client_Main.cfm | Loads, re-checked |
| UT | https://services.utahbar.org/Licensee-Directory | Loads, re-checked. Shows status? UNVERIFIED |
| VT | https://www.vtcourts.gov/attorneys/attorney-licensing | Corrected URL; links a static good-standing list, not a search (list not opened) |
| VA | https://vsb.org/Shared_Content/Directory/va-lawyer-directory.aspx | Loads, re-checked; shows good-standing status; no login |
| WA | https://www.mywsba.org/PersonifyEbusiness/LegalDirectory.aspx | Loads, re-checked; shows license status and public discipline |
| WV | https://www.mywvbar.org/membership-search-members | UNVERIFIED. 403 to WebFetch |
| WI | https://lawyerhistory.wicourts.gov/ | Loads, re-checked ("Lawyer Status and History") |
| WY | https://www.wyomingbar.org/for-the-public/hire-a-lawyer/lawyer-search/ | Loads, re-checked; covers all WY-licensed lawyers. Shows status? UNVERIFIED |

12 rows are UNVERIFIED (DE, KS, MA, MT, NV, NH, NJ, OK, RI, SD, TN, WV). For those, tell Grant the lookup is unconfirmed and that a call to the state bar may be needed. [cite: research 06 open question 6]

## 8. Output (per location, exactly as ticket 14)
- Return **3–5** candidates, ranked by **budget fit, then rating, then review volume**. [cite: ticket 14]
- On a budget-fit tie, a fee stated on the firm's own site ranks above a self-reported directory flag. When no candidate with usable reviews sits in the location itself, widen to the nearest metro and say so in the header. [cite: ticket 25 test]
- One block per location, in this format: [cite: ticket 14]
```
Attorney finder: <city, ZIP> · licensed in <state> · checked <date>
1. <Name>, <Firm> (<city>). Why: <one line>
   License: pending your check at <official site> (search "<Last name>", city <city>) · Discipline: <check there>
   Reviews: Google 4.8 (37, latest 2026-09) · Avvo 4.6 (12, latest 2026-05)
   Fees: free 30-min consult (source) | unknown
   Sources checked: <list with dates>
Not an endorsement. Jeeves does not contact or hire attorneys; you choose and contact them yourself.
```
- `<official site>`: for Indiana, "Indiana Roll of Attorneys on in.gov/courts" (help page in.gov/courts/help/attorney-search); for SC, the SC Judicial Branch attorney search; otherwise the §7 table entry. SC discipline reads "check the Supreme Court's lawyer-conduct orders". [cite: ticket 14]
- Mark snippet-derived ratings "(snippet)". Add any fake-review flag on its own line under Reviews. [cite: research 06 review-quality method; ticket 14]
- Fewer than 3 qualify: say so, list who did, then the second tier (§4) under its own heading, then the budget route (bar referral service and legal aid for that state, §6). [cite: ticket 14; ticket 25]
```
Strong, not fully confirmed (fewer than 3 qualified; check these yourself)
A. <Name>, <Firm> (<city>). Missing: <no review dated within 24 months | one platform only | fee unknown, ask about the consult fee>
   License: pending your check at <official site> (search "<Last name>", city <city>) · Discipline: <check there>
   Reviews: Google 4.8 (144, latest unknown) (snippet)
   Fees: unknown
   Sources checked: <list with dates>
```
- Letter second-tier entries (A, B, C) so they can't be mistaken for the numbered qualified list. [cite: ticket 25]
- The not-an-endorsement line closes every block, verbatim. [cite: ticket 14]

## 9. Rules
- **Never invent** a rating, review count, review date or fee. Record only what a source shows; otherwise "unknown". [cite: ticket 14]
- **Never contact** anyone: no calls, emails, forms, referral requests or messages to attorneys, firms, bars or legal-aid offices. Grant chooses and contacts them himself. [cite: ticket 15 refusals]
- **Never save** results, locations or lists to disk or memory unless Grant asks, and then only where he says. [cite: ticket 14; ticket 15]
- **Drop anyone not confirmed:** wrong side, below a threshold, strong fake-review signals, or a license Grant can't confirm as active. [cite: ticket 14]
- Never put a street address, party name or contract text in a query, URL or file. [cite: ticket 15]
- Never drive a browser or computer-use, and never bypass a CAPTCHA, login or bot check. [cite: research-resilience §2, §4]

## Open questions / known gaps
- Settled 2026-10-20: the privacy rule protects Grant and the parties to his matter, not public attorneys. Per-candidate review queries ("<name> <city> reviews") are allowed, and they count toward the per-location search budget.
- Settled 2026-10-20: device location comes from the bundled Jeeves Location app (§1 step 2), verified on this Mac. The hand-built Shortcut route is untested. [UNVERIFIED: research 07]
- IndyBar's client fee and Hamilton County coverage; the SCLS office for Aiken County; an SC limited-scope appearance rule. [UNVERIFIED: research 06 open questions 4–5]
- Whether handing over any Indiana lookup URL breaches "link to". The help page is the conservative choice. [UNVERIFIED: research 06 open question 2]
