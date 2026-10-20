# Verification levels and fake-citation handling
Type: grilling
Status: resolved
Blocked by: 10

## Question

For each depth, what verification steps run and what labels appear (Unverified, quick-verified, the deep verification note)? How is an unconfirmed citation handled (removed or marked), how does the skill catch a planted fake citation, and what does the verification note contain?

## Answer

Resolved 2026-10-20. Grant accepted the recommendations ("go for recs on tickets 09, 11 and 13"). The fetch order and limits are in `references/research-resilience.md`.

**What gets checked:** every authority Jeeves cites, **and** every authority the input itself relies on, such as a case quoted in a contract, a demand letter or an earlier memo. This is how a planted fake citation gets caught.

| | Quick | Intermediate | Deep |
|---|---|---|---|
| Web checks | None | Each cited source opened once, following the fallback chain | A separate verifier subagent re-opens **every** source |
| Existence | Only reference-file sources are cited. Input citations are marked `[NOT CHECKED: quick mode]`. | Name, number, court and date match the opened record | Same, plus later history: amended, repealed or overruled, where free sources show it |
| Claim | Trusts the reference file (deep-verified at build; its `verified` date is printed) | The key claim is spot-checked against the opened text | Each claim is checked against the opened text |
| Source quality | n/a | Mirrors labeled | Tiered: **primary official / primary mirror / secondary authoritative** (agency, bar, court guidance) / **secondary weak** (blogs, unsourced). A weak source can't stand alone for a legal rule. |
| Conflicts | n/a | Noted if seen | Always noted |
| Label | "Unverified against current sources. Reference files current as of <date>." | "Quick-verified": one line with counts and the main failure cause | Full verification note (below) |

**When a check fails:**
- *Exists but doesn't support the claim:* fix the claim, or drop it.
- *Couldn't open it:* the fallback chain ran out, so mark it `[n, UNVERIFIED]` with the reason.
- *No record anywhere* (the cite doesn't resolve, and the official site, case.law and Google Scholar all come up empty): mark it **`[NOT FOUND: possibly fabricated]`**, drop it from the reasoning, and list it in Bottom line if the input relied on it. Never silently swap in a similar real case.

**Deep verification note** (ends every deep memo):
```
Verification note
Checked: N sources (x primary official, y primary mirror, z secondary). Opened <date> via <tools>.
Results: confirmed a · corrected b · removed c · unverified d · not found e
Corrections: <one line each>
Conflicts between sources: <or "none seen">
Not checked: <what, and why: site down, CAPTCHA, search limit hit>
```
