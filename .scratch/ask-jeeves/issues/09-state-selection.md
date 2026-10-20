# State-selection questions and recommendation
Type: grilling
Status: resolved
Blocked by: 04, 08

## Question

What exact short questions does the skill ask to pick a state? How does it weigh the answers into a primary state or a primary and backup, what wording flags conflicting states and an uncertain choice-of-law clause, and how does it get Grant's confirmation before research starts?

## Answer

Resolved 2026-10-20. Grant accepted the recommendations ("go for recs on tickets 09, 11 and 13"). The state round is built on the verified 10-step procedure in `research/04-choice-of-law.md` §A9.

**1. Pre-fill from the input.** Read the pasted document or file first. Pull out any choice-of-law clause, forum clause, signing date, work location, occupation and pay it states, and show them as pre-filled answers for Grant to correct. Ask only what's missing.

**2. Questions: at most two AskUserQuestion rounds, with short options and "Other" to type a state.**
- *Round 1:*
  - **Where does the employee work?** IN / SC / Remote from another state / Other. Multi-select, with a share of time if split.
  - **Where do they live?** Same as work / IN / SC / Other.
  - **Where is the employer based, and where does it operate?** IN / SC / Multi-state / Other.
  - **Where did the key events happen** (resignation, data access, competing work)? Multi-select, or "Not yet".
- *Round 2 (only if still unknown):*
  - **Does the contract name a governing-law state or a court?** Yes, which? / No / No contract.
  - **Occupation and pay band.** Healthcare? Broadcast? This catches occupation bans and wage floors.
  - **Signing date.** This catches whether a 2025–26 law applies.

Mode only changes the framing (whose contacts are "ours"). The questions stay the same.

**3. The recommendation shown to Grant:**
```
Candidate state: Indiana (primary). Why: <one line>
Backup: South Carolina. Why: <one line>          (only when the procedure yields one)
Where they differ: <2–4 rows: issue | primary | backup>, e.g. non-compete enforceability, blue pencil vs strict voiding, wage-deduction rules
Confidence: Clear | Uncertain: <the signal, in plain words, e.g. "courts may not honor the contract's choice of Indiana law because you work in a state that voids it">
Confirm the applied state with a licensed attorney before relying on this.
```
It always says **Uncertain** when any §A8 signal is present: an override statute, a clause that conflicts with the default state's fundamental policy, a forum that applies its own conflicts rules, split work, or a new law whose reach depends on the signing date.

**4. Confirmation.** One AskUserQuestion: *Confirm <primary>* / *Use <backup> instead* / *Primary with backup notes* / *Other state*. **No research starts until Grant answers.** This applies even when the state was passed as an argument (ticket 08).

**5. Primary with backup.** The memo applies the primary state throughout. Where the backup would change a risk's outcome, it adds a short "Under <backup>: …" note in that risk's Law cell and in State applied.

**6. Any state.** A state without a built-in reference file uses Part B of the survey only to flag likely issues. It's then researched at the chosen depth; quick refuses it (ticket 10). Trade-secret claims also get a line naming where the misappropriation happened, plus the DTSA (§A9 step 8).
