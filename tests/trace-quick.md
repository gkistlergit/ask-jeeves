# Trace: ask-jeeves, quick mode, offer-letter-with-citation.md

Run date 2026-10-20. Skill: `scratchpad/aj-skill/skills/ask-jeeves/SKILL.md`. Input: `/Users/grantkistler/Developer/ask-jeeves/fixtures/offer-letter-with-citation.md`. No other file in either fixtures folder was opened (README.md in neither). No git run.

## Files loaded
| When | File | Why |
|---|---|---|
| Start | `skills/ask-jeeves/SKILL.md` | the skill |
| Start | `CONTEXT.md` (repo root) | SKILL.md says terms follow this glossary |
| Step 1 | input fixture (read in full) | intake |
| Step 3 | `references/choice-of-law.md` | step 3 says read it |
| Step 4 | `references/restrictive-covenants.md` | §3 non-compete, §4 non-solicit, §5 confidentiality |
| Step 4 | `references/employee-contracts.md` | at-will, §6 IP assignment, §7 devices/BYOD, §1 and §7(a) deductions and clawbacks |
| Step 4 | `references/insider-theft.md` | §7(c) data copying, return of devices, trade-secret exposure for the apps |
| Step 4 | `references/adjacent-fields.md` | step 4 says load it for adjacent issues |
| Step 5 | `templates/memo.md` | step 5 says fill it exactly |
| Step 5 | `humanizer` skill (via Skill tool) | plain-language pass |

Not loaded: `references/research-resilience.md` (standing rule says read it before the first web call or subagent dispatch; quick made neither). `references/attorney-finder.md` (step 7 not run; Grant said No).

One grep over `skills/ask-jeeves/` for "Hartwell|Kessler|258 N.E.3d" (no hits) and one for `as_of` dates (all 2026-10-20). Local Python (`-I`) scripts to count and trim memo prose words. None of these are web calls.

## Web calls
None. No WebSearch, no WebFetch, no subagents, no browser.

## Step 0: disclaimer
Said in chat at the start of the request: "Not legal advice. Jeeves spots issues to raise with a licensed attorney; it is not a lawyer." Also at the top of the memo.

## Step 1: intake and live-matter screen
Read the full letter. Screen:
- lawsuit or arbitration filed or threatened in writing: no (§9 arbitration omitted).
- cease-and-desist or demand letter: no.
- government charge, subpoena, investigation: no.
- employer accusation of data taking: no.
- legal deadline within 30 days: no. The letter's "sign and return by October 9, 2026" is an offer-acceptance date, not a legal deadline, and it has already passed (today 2026-10-20). Treated as a deal-logistics flag for the Bottom line, as the template allows. Start date November 2, 2026 is 13 days out.
Result: clear, continue.

Noted: the letter is addressed to a fictional "Jordan Avery"; I treated Grant as the employee receiving it, per the test setup. No party names went anywhere outside the memo.

## Step 2: end goal, mode, depth
Question asked (plain chat, verbatim from the skill):
> What's your end goal? For example: 'I must keep sole ownership of the 3 apps I built on my own time and money.' Or say 'no specific goal'.

Answer: "I must keep sole ownership of the 3 apps I created on my own time and with my own money."

Restatement shown:
> Your goal: keep sole ownership of the 3 apps you created on your own time and with your own money, after you sign this offer. Is that right?

Answer: confirmed.

Goal checks: lawful, nothing on the won't-do list. Live-matter screen re-run against the goal: still clear.

AskUserQuestion round (one round, two questions):
- "Which side are you on?" Options: Employer / Employee. Answer: Employee.
- "How deep should Jeeves go?" Options: Quick (about 1–2 minutes: built-in files only, unverified) / Intermediate (recommended) (about 5–10 minutes: web-checked, quick-verified) / Deep (about 20–45 minutes: multi-source research plus a separate verifier). Answer: Quick.

## Step 3: state selection
Pre-filled from the letter (shown to Grant as answers to correct):
- Choice of law: Indiana (§8). Forum: state or federal courts in Marion County, Indiana, exclusive (§8).
- Signing date: not yet signed; letter dated October 1, 2026, sign-by October 9, 2026.
- Work location: Indianapolis office 3 days a week, remote the rest (remote location not stated).
- Occupation and pay: Senior Data Engineer, $128,000 base, up to 10% discretionary bonus, $10,000 signing bonus.
- Employer: Brightline Analytics, Inc., Indianapolis, Indiana (where it operates not stated).

Round 1 AskUserQuestion (only the missing facts):
1. "Where will you work? The letter says the Indianapolis office 3 days a week and remote the rest. Where is the remote work?" Options: IN / SC / Remote from another state / Other. Answer: remote from his home in Indiana; office 3 days, home the rest (both Indiana).
2. "Where do you live?" Options: Same as work / IN / SC / Other. Answer: Indiana.
3. "Where is the employer based, and where does it operate?" Options: IN / SC / Multi-state / Other. Answer: based in and operates from Indiana.
4. "Where did the key events happen (resignation, data access, competing work)?" Options (multi-select): IN / SC / Other / Not yet. Answer: Not yet.

Round 2: not asked. Governing law, forum, occupation, pay and signing timing were all in the document or the pre-supplied answer ("data engineer, $128,000, signing Oct 2026").

Decision procedure run (choice-of-law.md Part 2):
1. Facts: lives IN, works IN (office + home), employer IN, clause IN, forum Marion County IN, not yet signed, no counsel noted, no suit, claim type none yet.
2. Override statutes: none met (IN is not an override state).
3. Florida check: no.
4. Clause: Indiana, substantial relationship: yes, so Indiana is provisional primary.
5. §187(2)(b): the §188 default state is also Indiana, so no conflict. Indiana primary; the "default state backup" is the same state, so no backup.
6. Forum: Marion County, state or federal; a federal court applies Indiana conflicts rules (Klaxon). No change.
7. Not applicable (clause exists).
8. Split claims: any trade-secret tort would also arise in Indiana, plus DTSA.
9. Effective dates: IN 2025-07-01 change is physician-only; not relevant.
10. Uncertainty checklist: no box ticked. Confidence Clear.

Shown:
```
Candidate state: Indiana (primary). Why: the letter picks Indiana law, and you live and work in Indiana for an Indiana employer.
Where they differ: n/a (no backup state)
Confidence: Clear
Confirm the applied state with a licensed attorney before relying on this.
```

Confirmation AskUserQuestion:
> Which state's law should Jeeves apply?
Options shown: Confirm Indiana / Other state. ("Use <backup> instead" and "Primary with backup notes" dropped because the procedure yielded no backup.)
Answer: Confirm Indiana.

Step 3.5: Indiana has built-in reference coverage, so Quick is allowed. Research started only after this answer.

## Step 4: research (Quick)
Reference files only, no web calls. Cited only what the files contain. Research aimed at the goal: what transfers the apps (§6 prior-invention and all-hours assignment), what could destroy or taint them (§7(b) wipe, §5/§7(c) mixing Company material), what restricts owning or selling them later (§3, §4), and levers (Exhibit A schedule, carve-out, countersigned side letter, LLC holding).

Citation statuses: every memo citation [1]–[5], [7]–[30] is "from reference file, verified 2026-10-20" (Indiana Code cites from the official 2026 IGA edition as the files record). Items the files mark UNVERIFIED keep that mark ([14] publication status; the Creative A enforceability line, which rests on the file's own UNVERIFIED "no Indiana appellate decision" finding).

### Input-document citations
| Citation in the input | Where | How handled |
|---|---|---|
| *Hartwell Data Systems, Inc. v. Kessler*, 258 N.E.3d 412, 419 (Ind. 2025), said to uphold an 18-month nationwide non-compete for a data engineer | §3 | Marked `[NOT CHECKED: quick mode]` (source [6]). Not opened, not searched (no web in quick). Grep confirmed it is in no reference file. Kept out of the reasoning and never used as support. Bottom line notes that the reference files' Indiana cases (*Heraeus*, *Buffkin*) point the other way. Listed as attorney question 3. Not labeled NOT FOUND, since that label requires an official-site, case.law and Google Scholar check that quick does not run. |

No other authority is cited in the input. §8's reference to "the laws of the State of Indiana" is a choice-of-law clause, not a citation.

## Step 5: memo
Filled `templates/memo.md` with every section. Hire triggers applied: High risks #1 and #2, and a signing within 14 days (start November 2), so every before-signing item ends with "Talk to a licensed attorney before you act." No criminal-exposure, agency or uncertain-state triggers.

Plain-language pass: invoked `humanizer` with the Skill tool (embedded mode). Applied: no em or en dashes in prose, plain verbs, no staged contrasts or closers. Template-required bold labels, every quote, citation, statute and case name and glossary term kept verbatim. Two `*In plain terms:*` lines follow the quoted §6 clauses.

Word count (prose only; excludes header, table, quotes, Sources and the verification line): first draft 1,226, trimmed to **895** (inside 600–900). Whole file 1,825 words.

Verification ending: the template's Quick text, verbatim.

## Step 6: deliver
Memo shown in chat (and written to `tests/memo-quick.md` because the test asked for that path). Question asked:
> Want Jeeves to find a budget-friendly, well-reviewed attorney licensed in Indiana?
Options: Yes / No. Answer: No.

## Step 7: attorney finder
Not run (Grant said No).

## Unclear or contradictory in the skill
1. Step 3.3/3.4 and the template assume a backup state. When the clause state equals the §188 default, the procedure yields none, yet "Where they differ" isn't marked optional and the confirmation has four fixed options, two of which then make no sense. I showed "n/a" and two options.
2. Step 1's "legal deadline within 30 days" is undefined. A sign-by date (here, already passed) could be read as one, which would stop the memo. I treated it as deal logistics, as the template's Bottom line suggests.
3. Quick input-citation status `[NOT CHECKED: quick mode]` isn't among the template's Sources status values or in-line citation forms. I used `[6, NOT CHECKED: quick mode]`.
4. The 600–900 word count doesn't say whether citation brackets, the bold template labels or the fixed lines ("Run it past...", "Confirm the applied state...") count. I counted all of them, which made the cap tight.
5. "Deferred fields ... get one-line flags" doesn't say whether all four are always flagged or only relevant ones. I flagged all four.
6. Recommendations: "Talk to a licensed attorney" on "any item with a hire trigger" puts it on every before-signing item whenever signing is within 14 days. That's repetitive, so I merged before-signing items into three bullets.
7. Creative option must not restate a recommendation, but the skill's own example (dated prior-inventions schedule) is the obvious Path/Recommendation step for this goal. I made the schedule a Path step and used an LLC holding and a countersigned side letter as the creative options.
8. Standing rule says memos are saved to disk only when Grant asks; the test harness asked, so I saved.
