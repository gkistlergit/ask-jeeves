# Input document changes mid-run
Type: task
Status: resolved
Blocked by:

## Question

In the deep test (2026-10-20), the real input document arrived after step 4 research had started on a stand-in. SKILL.md has no step for this. Add one: when the input changes after step 3, Jeeves re-reads it in full and re-runs the live-matter screen. It also re-checks the state pre-fill against the new document. It then decides per legal area whether the research still applies or that slice must re-run, and lists any area left unchecked against the new document in the verification note.

Done when SKILL.md steps 1–4 carry the re-scope rule, and the verification template has a "researched against an earlier input" line.

## Answer

Done 2026-10-20 on `skill/v1` (39ebf1a, draft PR gkistlergit/ask-jeeves#1).
- SKILL.md step 1 has a new subsection, "When the input changes mid-run". It covers four steps:
  1. Read the new document in full, re-run the live-matter screen and re-check the goal against it.
  2. Redo the step 3 pre-fill, asking Grant only what changed. A changed state goes back through confirmation.
  3. Per legal area, keep research whose law still applies to the new clauses. Re-run a slice with a new clause type, a changed state or a materially different term, or list it as a gap. Every cited authority still goes to the verifier.
  4. Tell Grant which areas were kept and which re-ran.
- Step 4 points to the subsection if a document arrives during research.
- `templates/memo.md` adds an "Earlier input" line to the deep verification note and to the intermediate ending.
