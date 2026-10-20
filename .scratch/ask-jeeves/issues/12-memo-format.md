# Memo format
Type: prototype
Status: resolved
Blocked by: 01, 02, 03, 08

## Question

What does the issue-spotting memo look like? Prototype one from a sample offer letter with a non-compete, an IP assignment and a device policy. Settle the sections, the likelihood scale, the wording of what could go wrong later, recommendations, questions for a licensed attorney, the state-applied note and length.

Carried from [Skill structure and request flow](08-skill-structure.md): a humanizer plain-language pass runs before the memo is shown. Prototype the "in plain terms" line that follows a hard-to-read quoted clause, and confirm quotes, citations and glossary terms survive the pass untouched.

## Answer

Resolved 2026-10-20. Grant accepted the recommendations ("go for recs on tickets 10, 12 and 15"). Prototype: [`prototypes/memo-intermediate.md`](../../../prototypes/memo-intermediate.md), built from [`fixtures/sample-offer-letter.md`](../../../fixtures/sample-offer-letter.md) in employee mode, Indiana, intermediate depth. It has 7 risks; 11 sources were confirmed and 3 Indiana Code cites are UNVERIFIED. The prototype's own critique is in [`prototypes/memo-notes.md`](../../../prototypes/memo-notes.md).

The format is locked to the prototype's sections, with these changes taken from the notes:

1. **Header.** The disclaimer line, then: Mode · Applied state (with a one-line reason) · Depth and verification label · Reference files as-of date · Date prepared.
2. **Sections, in order:** Bottom line (at most 3 bullets) · State applied and why · Risks · Recommendations · Creative option (format set in ticket 13) · Questions for a licensed attorney (3–6) · Adjacent issues flagged · Sources · Verification. Every depth has all of them.
3. **Bottom line** may also carry deal-logistics flags, such as a sign-by date that has passed or a release window.
4. **Risks table** has 5 columns: `# | Issue (clause) | Likelihood | What could go wrong later | Law [n]`. Each cell stays under about 25 words, and the law sits in its own column. There are at most 6 rows; extra risks move to Adjacent issues as "also noted".
5. **Likelihood** is Low / Medium / High plus a few words of reason. No percentages.
6. **"In plain terms"** follows any hard-to-read quoted clause, tagged with the risk number: `> #4 "quote under 15 words"`, then `*In plain terms:* …`.
7. **Recommendations** are grouped by timing (**Before signing / On the job / When leaving**), and each item names its risk number. A hire-an-attorney trigger (ticket 15) adds "Talk to a licensed attorney before you act" to that item.
8. **Citations.** Every legal claim carries [n]. A practical risk with no law behind it is allowed, tagged *(practical)*. General statements already in the glossary don't need a cite. An unverified cite is written inline as `[12, UNVERIFIED]`.
9. **Sources** prefer official or court copies, with mirrors such as FindLaw labeled "(mirror)". Fallback order is in `references/research-resilience.md`.
10. **Verification.** Quick and intermediate end with one line giving the counts and the main failure cause, for example "iga.in.gov did not load through WebFetch". Deep ends with the full note (ticket 11).
11. **Length.** 600–900 words of prose, not counting the header, tables, quotes and sources. Depth changes how much backs the memo, not its length or its sections.
12. **Plain-language pass:** the humanizer skill runs on prose only, as in ticket 08. The prototype shows quotes, citations and case names surviving it unchanged.
