# Attorney-finder criteria
Type: grilling
Status: resolved
Blocked by: 06, 07, 09

## Question

What thresholds define best customer-reviewed (minimum review count, rating, recency, number of sources) and budget-friendly? How does the location picker work (live location consent, ZIP, the saved home location by city and ZIP only, Aiken SC), how does it handle a location and state mismatch, how many results does it return (default 3–5), what does the ranked list show, and what wording does the not-an-endorsement note use?

## Answer

Resolved 2026-10-20 with Grant: **minimum 4.3 stars; budget means free or close to free**. He accepted the recommendations for everything else. The basis is `research/06-attorney-finder-sources.md` and `research/07-live-location.md`.

**When it runs.** Only when Grant opts in after the memo (ticket 08). It runs as a subagent at every depth, under the limits in `references/research-resilience.md`: at most 8 searches per location, and no browser.

**Location picker** (one AskUserQuestion, multi-select; each location is searched separately):
- *My live location*: ask consent first, then run the "Jeeves Location" Shortcut, which returns city and ZIP only. The fallback is ip-api, disclosed as approximate.
- *Type a ZIP*.
- *Home: Noblesville, IN 46060*. The street address is never stored or used.
- *Aiken, SC*.

**Mismatch.** If a location's state differs from the applied state, Jeeves says so and asks before searching: *Licensed in <applied state>* / *Licensed in <location state>* / *Both*.

**Who qualifies:**
- **Practice match.** Employment law, on the right side for the mode: employee-side for employee mode, management-side for employer mode.
- **Reviews.** At least a **4.3-star** average, from at least **10 reviews** across at least **2 independent sources**, with at least one review in the last 24 months. Jeeves records the rating, the count and the latest review date for each source as seen, and never estimates them. It watches for FTC fake-review signals (16 CFR 465): bursts of 5-star reviews, generic text, reviewers with no history, review gating. A candidate with those signals is flagged, or dropped when the signals are strong.
- **Budget: free or close to free.** At least one of these must be published: a **free consultation**, a consultation of **$50 or less**, the **bar lawyer-referral service** route (SC Bar LRS: ≤$50 for 30 min), **legal aid** eligibility (125% FPL), or limited-scope help (RPC 1.2(c)). A fee appears only when a source states it; otherwise it reads "unknown". If fewer than 3 attorneys qualify, Jeeves says so and lists the bar referral service and legal aid as the budget route. It doesn't lower the bar quietly.

**License and discipline (Grant checks).**
- Indiana's and South Carolina's official lookups can't be automated: Indiana's terms forbid it, and SC's robots.txt blocks it.
- For each candidate, Jeeves gives the official lookup site and the exact name to search: the Indiana Roll of Attorneys (help page in.gov/courts/help/attorney-search) and the SC Judicial Branch attorney search.
- Each candidate stays "License: pending your check" until Grant reports back. Anyone he can't confirm as active is dropped.
- Discipline: Indiana shows it on the Roll record. For SC, Grant checks the Supreme Court's lawyer-conduct orders.
- For other states, Jeeves uses the official lookup from the research 06 table, fetching it only where that state's terms and robots.txt allow, and otherwise Grant opens it.

**Output per location (3–5, ranked by budget fit, then rating, then review volume):**
```
Attorney finder: <city, ZIP> · licensed in <state> · checked <date>
1. <Name>, <Firm> (<city>). Why: <one line>
   License: pending your check at <official site> (search "<Last name>", city <city>) · Discipline: <check there>
   Reviews: Google 4.8 (37, latest 2026-09) · Avvo 4.6 (12, latest 2026-05)
   Fees: free 30-min consult (source) | unknown
   Sources checked: <list with dates>
Not an endorsement. Jeeves does not contact or hire attorneys; you choose and contact them yourself.
```

**Privacy.** Search queries contain only the city or ZIP plus terms like "employment lawyer". They never contain party names, contract text or the street address. Results aren't saved unless Grant asks.
