# Memo template

Fill every section at every depth. Depth changes how much research and verification backs the memo, never which sections it has. Prose runs 600–900 words. **Counts:** the sentences in Bottom line, Path to your goal, State applied, Recommendations, Creative option, Questions and Adjacent issues. **Doesn't count:** the header, headings and bold labels, the Risks table, quoted clauses and their *In plain terms* lines, Sources, and the verification ending.

```
# Jeeves memo: <short title>
> Not legal advice. Jeeves spots issues to raise with a licensed attorney; it is not a lawyer.
Goal: <Grant's end goal, one line | none stated>
Mode: <Employer|Employee> · Applied state: <State> (why: <one line>)[; backup: <State>] · Depth: <Quick|Intermediate|Deep>, <label> · Reference files current as of <oldest as_of> · Prepared <date>

## Bottom line
- **Goal:** <Likely | Uncertain | Unlikely> to be reachable: <why, one line> [n]
- (then at most 3 more bullets: the biggest risks, plus any deal-logistics flag such as a passed sign-by date or a release window, plus any input citation marked NOT FOUND)

## Path to your goal
1. <ordered steps that reach the goal, each tied to a risk # and timing: before signing / on the job / when leaving> [n]
(3–6 steps. If the goal can't be reached lawfully, say so and give the closest lawful alternative. With no goal stated: "No end goal given. Recommendations below cover the general risks.")

## State applied and why
<2–4 lines: the contacts that point to this state; Clear or Uncertain, with the reason in plain words; "Under <backup>: …" where the backup changes things>
Confirm the applied state with a licensed attorney before relying on this.

## Risks
| # | Issue (clause) | Likelihood | What could go wrong later | Law [n] |
|---|---|---|---|---|
| 1 | <issue> (§x) | High: <few words> | <short scenario> | [1][2] |
(at most 6 rows, goal-threatening risks first and tagged *(goal)*, each cell under about 25 words; a practical risk with no law behind it is tagged *(practical)*; extra risks go to Adjacent issues as "also noted")

> #<risk> "<hard-to-read clause, under 15 words>"
*In plain terms:* <one line>

## Recommendations
**Before signing**
- (#1) <action>. <"Talk to a licensed attorney before you act." when a hire trigger applies; put it once under the group heading when every item in the group has one>
**On the job**
- (#n) <action>
**When leaving**
- (#n) <action>

## Creative option
**Creative, not standard practice.** <idea in 2–3 sentences, aimed at the end goal>
Why it might work: <one line> [n]
**Risk:** <Low|Medium|High>: <what could backfire>
**Enforceability:** <Likely|Uncertain|Unlikely>: <why> [n]
Run it past a licensed attorney before using it.
(1–2 of these)

## Questions for a licensed attorney
1. (3–6 questions)

## Adjacent issues flagged
- <field>: <one line> [n]

## Sources
[1] <citation>. <URL> (confirmed <date> | from reference file, verified <date> | local official code, <edition> | (mirror) | [UNVERIFIED: reason] | [NOT CHECKED: quick mode] | [NOT FOUND: possibly fabricated])

<Verification line or note, by depth (see below)>
```

## Labels and verification endings

- **Quick.** Label: `Unverified against current sources`. End: `Verification: none this request. Unverified against current sources. Reference files current as of <date>. Citations in your document were not checked (quick mode).` When a reference file is stale (more than 12 months old, `references/research-resilience.md` §7), the label becomes `Unverified against current sources; reference may be out of date`, and the end adds `Reference may be out of date: references/<file>.md, as of <date>.`, one entry per stale file, separated by semicolons.
- **Quick on a state card.** When a state's law comes from `references/state-cards/<ST>.md`, the label adds `; slim state card`, and the end adds `State law from a slim state card: references/state-cards/<ST>.md, as of <date>. Not on the card: <the card's "Not on this card" list, plus any gap this request hit>.` A stale card also takes the out-of-date wording above, for example `Unverified against current sources; slim state card; reference may be out of date`.
- **Intermediate.** Label: `quick-verified`. End: `Verification: quick-verified. N sources opened and confirmed; M marked unverified; K not found. Main failure cause: <e.g. site down / search limit hit / none>.` When the input changed mid-run, add: `Earlier input: <areas researched against an earlier input, and which were re-run>.`
- **Intermediate and deep, newer law found:** add `Reference out of date: <file>, <change>; queued for refresh.` to the ending or note.
- **Deep.** Label: `deep-verified`. End with the full note:
```
Verification note
Checked: N sources (x primary official, y primary mirror, z secondary). Opened <date> via <tools>.
Results: confirmed a · corrected b · removed c · unverified d · not found e
Corrections: <one line each>
Conflicts between sources: <or "none seen">
Not checked: <what, and why: site down, CAPTCHA, search limit hit>
Earlier input: <areas researched against an earlier input, and which were re-run> (only when the input changed mid-run)
```

## Citation forms
- In-line: `[n]`. When unverified: `[n, UNVERIFIED]`. When it doesn't exist: `[n, NOT FOUND]`, which is never used as support. An input citation quick mode didn't check: `[n, NOT CHECKED]`.
- Every in-line use of a NOT FOUND or NOT CHECKED source carries its label, in the Risks table too. Never put it in a run of support cites such as `[8][9][12]`: cite the rule from other sources, and mention the input's case separately.
- Indiana Code: `IC 24-2-3-2 (2026 Ind. Code, official IGA edition)`.
- Quotes stay under 15 words.
