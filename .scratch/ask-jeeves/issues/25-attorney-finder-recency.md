# Attorney-finder recency rule
Type: grilling
Status: resolved
Blocked by:

## Question

In testing (2026-10-20), 0 attorneys qualified at each of 3 Indiana and SC locations. Review dates are rarely visible to Jeeves's tools: aggregators and search snippets show a rating and a count but no date. So the "review in the last 24 months" rule and the 2-source rule reject employee-side firms with strong ratings, such as a 4.8 average from 144 reviews.

Should Jeeves:
- keep the rule;
- accept an undated source when another source shows a recent date;
- list such firms in a separate "rating strong, recency unconfirmed" tier for Grant to check himself?

Grant decides; this doesn't block deploy.

## Answer

Grant took the recommendations (2026-10-20). Shipped in gkistlergit/ask-jeeves#2 (merge `933fc5a`), pinned by claude-global-settings#62, and installed.
- **Recency** is met when any one source shows a review dated within 24 months.
- **Second source:** an aggregator that republishes a platform (TrustAnalytica, LeadStal, Expertise.com) counts as that platform. Facebook counts as its own platform. The 4.3 average is weighted by review count, and firm and attorney reviews may pool.
- **Fee:** an explicit "free consultation" or "free case evaluation" counts as published. A bare "consultation" stays unknown.
- **New tier, "Strong, not fully confirmed":**
  - shown only when fewer than 3 qualify, at most 3 entries, lettered A–C;
  - still requires the right side, 4.3 stars or better, at least 10 reviews and no strong fake-review signal;
  - may lack recency, a second platform (then 50+ reviews on one) or a published fee, and must say which.
- **Re-test, Home (Noblesville):** before, 0 qualified and nothing to show. Now 0 qualified, plus 2 employee-side firms in the tier, each missing only recency.
- **Rule gaps the re-test found, folded in:**
  - directory profile text can show side when a firm site is blocked;
  - on a budget tie, a firm-site fee ranks above a directory flag;
  - when nothing is local, widen to the nearest metro and say so.
