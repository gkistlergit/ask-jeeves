# Memo template

Fill every section at every depth. Depth changes how much research and verification backs the memo, never which sections it has. Prose runs 600–900 words, not counting the header, tables, quotes and sources.

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
- (#1) <action>. <"Talk to a licensed attorney before you act." when a hire trigger applies>
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
[1] <citation>. <URL> (confirmed <date> | from reference file, verified <date> | (mirror) | [UNVERIFIED: reason] | [NOT FOUND: possibly fabricated])

<Verification line or note, by depth (see below)>
```

## Labels and verification endings

- **Quick.** Label: `Unverified against current sources`. End: `Verification: none this request. Unverified against current sources. Reference files current as of <date>. Citations in your document were not checked (quick mode).`
- **Intermediate.** Label: `quick-verified`. End: `Verification: quick-verified. N sources opened and confirmed; M marked unverified; K not found. Main failure cause: <e.g. site down / search limit hit / none>.`
- **Deep.** Label: `deep-verified`. End with the full note:
```
Verification note
Checked: N sources (x primary official, y primary mirror, z secondary). Opened <date> via <tools>.
Results: confirmed a · corrected b · removed c · unverified d · not found e
Corrections: <one line each>
Conflicts between sources: <or "none seen">
Not checked: <what, and why: site down, CAPTCHA, search limit hit>
```

## Citation forms
- In-line: `[n]`. When unverified: `[n, UNVERIFIED]`. When it doesn't exist: `[n, NOT FOUND]`, which is never used as support.
- Indiana Code: `IC 24-2-3-2 (2026 Ind. Code, official IGA edition)`.
- Quotes stay under 15 words.
