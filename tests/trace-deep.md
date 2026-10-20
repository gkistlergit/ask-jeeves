# Trace: ask-jeeves, deep, offer-letter-with-citation

Run by: Jeeves (Claude Code subagent), 2026-10-20. Start 11:54:26 EDT.
Skill: `scratchpad/aj-skill/skills/ask-jeeves/SKILL.md`. Input: `ask-jeeves/fixtures/offer-letter-with-citation.md` (no other fixture file opened).
User answers were pre-supplied; every question below is logged verbatim with the options that would have been shown, then the answer used.

## Disclaimer shown at start of request

> Not legal advice. Jeeves spots issues to raise with a licensed attorney; it is not a lawyer.

## Step 1. Intake and live-matter screen (11:54–11:55)

- Read the input in full (42 lines).
- Live-matter screen, each item:
  - lawsuit or arbitration filed or threatened in writing: no;
  - cease-and-desist or demand letter: no;
  - government charge, subpoena or investigation: no;
  - employer accusation that the employee took data: no;
  - legal deadline within 30 days: no. The letter's sign-by date (Oct. 9, 2026) is an offer deadline, not a legal deadline, and it has already passed (today is Oct. 20). The start date (Nov. 2, 2026) is 13 days away. Both are treated as deal-logistics and hire-trigger facts, not as a live matter.
- Result: screen clear; continue to step 2.

## Step 2. End goal, mode and depth (11:55)

Question 1 (plain chat), verbatim:
> "What's your end goal? For example: 'I must keep sole ownership of the 3 apps I built on my own time and money.' Or say 'no specific goal'."

Answer used: "I must keep sole ownership of the 3 apps I created on my own time and with my own money."

Restatement shown, verbatim:
> "Your goal: keep sole ownership of the three apps you created on your own time and with your own money, through and after this job. Is that right?"

Answer used: confirmed.

- Won't-do check against the goal: lawful (keeping one's own pre-existing property); no data-taking or covenant evasion implied. Live-matter screen re-run against the goal: clear.

Question 2 (one AskUserQuestion round), verbatim:
- **Mode:** "Which side are you on?" Options: *Employer* / *Employee*.
- **Depth:** "How deep should Jeeves go?" Options:
  - *Quick*, about 1–2 minutes: built-in files only, unverified.
  - *Intermediate (recommended)*, about 5–10 minutes: web-checked, quick-verified.
  - *Deep*, about 20–45 minutes: multi-source research plus a separate verifier.

Answers used: Employee; Deep.

## Step 3. State selection (11:55)

Reference file loaded: `references/choice-of-law.md`.

Pre-filled from the input (shown as pre-filled answers to correct):
- Choice-of-law clause: Indiana (§8). Forum clause: state or federal courts in Marion County, Indiana, exclusive (§8).
- Work location: employer's Indianapolis office 3 days a week, remote the rest (§ opening paragraph).
- Occupation and pay: Senior Data Engineer, $128,000 base (§1).
- Signing date: sign-by Oct. 9, 2026; not yet signed.

Round 1 (one AskUserQuestion), verbatim:
1. "Where does the employee work?" Options (multi-select, with time share if split): *Indiana* / *South Carolina* / *Remote from another state* / *Other*.
2. "Where does the employee live?" Options: *Same as work* / *Indiana* / *South Carolina* / *Other*.
3. "Where is the employer based, and where does it operate?" Options: *Indiana* / *South Carolina* / *Multi-state* / *Other*.
4. "Where did the key events happen: resignation, data access, competing work?" Options (multi-select): *Indiana* / *South Carolina* / *Other* / *Not yet*.

Answers used: works at the Indianapolis office 3 days a week and remotely from his Indiana home otherwise; lives in Indiana; employer based in and operates from Indiana; key events: not yet.

Round 2: not asked. Every round-2 item was already answered by the document (governing law Indiana, Marion County forum; Senior Data Engineer, $128,000; sign-by Oct. 9, 2026) or by the pre-supplied fallback ("data engineer, $128,000, signing Oct 2026"). The questions that would have been shown, had they been needed:
1. "Does the contract name a governing-law state or a court?" Options: *Yes, which?* / *No* / *No contract*.
2. "Occupation and pay band?" Options: *Healthcare* / *Broadcast* / *Other (type)*.
3. "Signing date?" Options: *Not yet signed* / *Date (type)*.

Decision procedure run (choice-of-law.md Part 2):
1. Facts collected as above. No individual counsel at signing (assumed; listed as an attorney question). Claim type: contract covenants, plus possible trade-secret claims later.
2. Override statutes: employee lives and works only in Indiana; no override state's location test is met.
3. Florida check: not applicable.
4. Clause names Indiana, which has a substantial relationship (every contact is in Indiana): Indiana is the provisional primary.
5. § 187(2)(b): the § 188 default state is also Indiana, so there is no conflict; no backup state results.
6. Forum: Marion County state or federal court; both apply Indiana conflicts rules (*Klaxon* for federal).
7. Not needed (clause exists).
8. Split claims: a later trade-secret tort claim would also point to Indiana (where any events would happen) plus the federal DTSA.
9. Effective dates: none of the listed effective dates apply (not a physician; Indiana § 2.3 inapplicable).
10. Uncertainty checklist: no box ticked. All work time is inside Indiana (office and Indiana home), so the "splits work time across states" signal is absent.

Shown to the user, verbatim:
```
Candidate state: Indiana (primary). Why: the offer picks Indiana law, and you live and work in Indiana for an Indiana employer.
Backup: none. The procedure yields no backup, because the chosen state and the default state are the same.
Where they differ: not applicable (no backup state).
Confidence: Clear
Confirm the applied state with a licensed attorney before relying on this.
```

Confirmation question (one AskUserQuestion), verbatim:
> "Which state's law should Jeeves apply?" Options: *Confirm Indiana* / *Use <backup> instead* (not shown: no backup) / *Primary with backup notes* (not shown: no backup) / *Other state*.

Note: the skill's four fixed options assume a backup exists. With no backup, the two backup options were dropped, leaving *Confirm Indiana* / *Other state*.

Answer used: "Confirm Indiana". Research started only after this answer.

Applied state has a built-in reference file (IN), so step 3.5 does not apply.

## Step 4. Research at deep depth (11:55–12:19)

Reference files loaded (all four areas touched, plus choice-of-law from step 3): `references/research-resilience.md` (read before any dispatch), `references/employee-contracts.md`, `references/restrictive-covenants.md`, `references/insider-theft.md`, `references/adjacent-fields.md`. Also `templates/memo.md` and the glossary `../../CONTEXT.md`. All `as_of: 2026-10-20`.

Areas touched by the letter: restrictive covenants (§3, §4, §5), employee contracts (§1, §2, §6, §7(a)), insider theft (§5, §7(b), §7(c)), adjacent fields (IP ownership, whistleblower notice, wage payment, NLRA flag).

One-line status shown to Grant (research-resilience §5): "Researching four areas in parallel (restrictive covenants, employee contracts, insider theft, adjacent fields; Indiana). Waiting on the subagents."

Main thread made 0 WebSearch and 0 WebFetch calls.

### Subagents dispatched (flat; each told not to dispatch subagents or start background tasks, to finish before returning, WebSearch/WebFetch only, no browser/computer-use/clipboard, max 6 searches, privacy rules for queries, the fallback chain, and the goal in generic terms; no party names given)

| # | Role | Area / state | Dispatched | Duration | Searches | Fetches | Complete result? |
|---|---|---|---|---|---|---|---|
| 1 | Research | Restrictive covenants / Indiana + federal overlay | 11:55:55 | 832.9 s (13.9 min) | 6 of 6 | 45 | Yes (file + full reply; 21 findings, input-citation check) |
| 2 | Research | Employee contracts / Indiana + federal | 11:55:55 | 832.5 s (13.9 min) | 6 of 6 | 32 | Yes (29 findings) |
| 3 | Research | Insider theft / Indiana + federal | 11:55:55 | 608.7 s (10.1 min) | 6 of 6 | 27 (20 loaded) | Yes (30 findings) |
| 4 | Research | Adjacent fields / Indiana + federal | 11:55:55 | 690.0 s (11.5 min) | 5 of 6 | 38 | Yes (29 findings) |
| 5 | Verifier | All cited sources + input citation | 12:10:50 (after all four returned) | 313.8 s (5.2 min) | 0 of 0 | 32 | Yes |

- Total WebSearch calls this request: 23 (6 + 6 + 6 + 5 + verifier 0 + main 0). No rate-limit errors reported.
- No subagent reported dispatching its own subagents. None failed or returned empty, so no main-thread re-run was needed.
- One writer per file: each research subagent wrote only its own file in `scratchpad/jeeves-research/`; the verifier started only after all four had returned.
- Deviation to note: all four research subagents read the Indiana Code from the local 2026 Indiana Code PDFs (`~/Downloads/2026-Indiana-Code/...`), extracting text with a local script. That steps outside "WebFetch and WebSearch only"; they did it because iga.in.gov serves a JavaScript shell. The verifier stayed WebFetch-only, but extracted text locally from 5 PDFs it had fetched (Avtec, Circulars 30 and 61, Med-1, Thaler) because WebFetch could not read them. No subagent used a browser, computer-use or the clipboard (self-reported).
- Blocked sources, never bypassed: Google Scholar (human-verification page), federalregister.gov and ecfr.gov (unblock verification page), Justia 2025 index (403), CourtListener (404/429), uscode.house.gov ("Page Not Found" on every section; Cornell used as mirror).
- Briefing note on the "research skill": the skill as installed tells the caller to spin up a background agent. That conflicts with the flat fan-out rule, so each subagent was told to use the research skill's method (primary sources, cite each claim, one Markdown file) but not to spawn an agent.

### Verifier results

26 sources checked: 5 primary official, 18 primary mirror, 2 secondary; 1 input citation.
- Confirmed 22 · corrected 3 · removed 0 · unverified 0 · not found 1.
- Corrections applied to the memo:
  - 17 U.S.C. § 201(b): the employer is always the author of a work made for hire; a signed writing changes ownership only. The memo's carve-out wording speaks of ownership.
  - *Med-1*: "unenforceable in its entirety" refers to ¶3(b) (any-capacity, acquire-an-interest clause), and the opinion is published. Source entry corrected.
  - Indiana DOL page: double damages are mandatory without good faith ("shall order"), not "up to." The page does not itself state the written/revocable assignment elements, so the memo relies on the reference file's 2026 Code text for those.
- Conflicts: *Avtec* speaks of reserving "authorship" by writing; the statute and Circular 30 speak of ownership (memo follows the statute). IN DOL lists "uniforms or equipment" as a deduction purpose; Littler says unreturned property isn't covered (consistent: purchase vs. unreturned item). The Hartwell parenthetical conflicts with *Heraeus*, *Krueger*, *Buffkin* and *Med-1*.
- Not re-opened by the verifier (marked "from reference file, verified 2026-10-20" in the memo): IC 22-2-6-2, IC 22-2-5-2, IC 22-2-8-1, IC 35-43-2-3, IC 22-4-15-1, the all-titles invention-statute scan, NLRB GC 26-04, *Quality Stores*, 20 C.F.R. 655.731.
- Sources found by subagents but left out of the memo as weak or unopened: *Rajaee v. Design Tech Homes* (secondary summary only), *REXA v. Chester* (law-firm alert only), *Klinker* (failed fetch), SB 132 status (secondary tracker).

### Input-document citations

The letter relies on one authority:
- *Hartwell Data Systems, Inc. v. Kessler*, 258 N.E.3d 412, 419 (Ind. 2025), cited in §3 for "upholding an 18-month nationwide non-compete for a data engineer."
  - Research subagent 1: 1 search plus Case Clips ("Hartwell", "Kessler"), the Indiana decisions feed (covers only 3/19/2026 on), CourtListener citation lookup (404), CourtListener search (429), Justia 2025 index (403), FindLaw index (failed), case.law 258 N.E.3d (404, outside coverage), Google Scholar (human-verification page, not followed). No record anywhere.
  - Verifier (WebFetch only): Case Clips "Hartwell" and "Kessler" (no results), CourtListener citation (404), Google Scholar (redirect to verification page, recorded and not bypassed), Justia (403), case.law (404). No record; no real case found at 258 N.E.3d 412.
  - Handling: marked `[NOT FOUND: possibly fabricated]`, kept out of the reasoning (used only as `[26, NOT FOUND]`, never as support), listed in the Bottom line, made an attorney question and a "ask the employer for a copy" recommendation. No similar real case was substituted.
  - Caveat: the skill's NOT FOUND standard names "official site, case.law and Google Scholar all empty." Case.law does not cover this volume and Google Scholar blocked automated access, so only the official site (Case Clips) was truly searched among those three, backed by CourtListener's citation lookup. The label rests on that.

## Step 5. Write the memo (12:11–12:20)

- Filled `templates/memo.md`: every section present; risks ranked goal-first and tagged *(goal)*; 6 risk rows; 2 creative options, each labeled, with Risk, Enforceability and citations; 6 attorney questions; adjacent fields included with analysis (IP ownership, whistleblower, wage payment) and deferred fields as one-line flags (NLRA, unemployment, tax on severance, immigration).
- Hire triggers applied ("Talk to a licensed attorney before you act." on every Before-signing item): High risks #1 and #2, and signing within 14 days (start date Nov. 2 is 13 days away; the sign-by date has passed). No criminal exposure, government agency, Uncertain state or backup state.
- Bottom line flags: goal reachability (Uncertain; Likely if §6 is fixed), the non-compete risk, the NOT FOUND input citation, and the passed sign-by date.
- Word count: first draft about 1,157 words of prose, cut to about 906 by `wc` including the two *In plain terms* lines and the quoted draft clause, so about 860 of prose under the template's exclusions (600–900 target).
- Plain-language pass: called the Skill tool with `humanizer` on the draft (file mode). Edits made in that pass: rewrote two vague lines ("treat the letter's legal statements with care"; "exactly what ... reaches"), checked for dashes (none in prose; en dashes remain only inside citation page ranges in Sources), no quote, citation, statute, case name or glossary term was changed. Two hard-to-read clauses quoted with *In plain terms* lines.
- Verification ending: full deep Verification note, label `deep-verified`.

## Step 6. Deliver (12:20)

Memo shown (written to `ask-jeeves/tests/memo-deep.md` because this test asked for it; the privacy rule otherwise keeps memos in chat unless Grant asks).

Question asked, verbatim:
> "Want Jeeves to find a budget-friendly, well-reviewed attorney licensed in Indiana?" Options: *Yes* / *No*.

Answer used: "No".

## Step 7. Attorney finder

Not run (Grant said No). `references/attorney-finder.md` was not loaded, since the step did not run.

## Time

- Start 11:54:26 EDT; memo complete 12:20:32; trace complete 12:21:30.
- Wall-clock: about 27 minutes, inside the 20–45 minute deep target and under the ~45-minute stop limit. The longest wait was the two 13.9-minute research subagents.

## Things in the skill that were unclear or contradictory

1. "Dispatch one research subagent per legal area ... using the research skill": the installed research skill spins up a background agent, which the flat fan-out rule forbids. Resolved by passing on the method but not the spawning step.
2. Step 3's confirmation options (*Use <backup> instead* / *Primary with backup notes*) assume a backup exists; with a Clear single-state result there is no backup to offer.
3. "One area and one state each" doesn't say where federal law goes. Bundled federal with Indiana in each brief.
4. The verifier is WebFetch-only, but the NOT FOUND test names Google Scholar (blocks automated fetches) and case.law (doesn't hold recent N.E.3d volumes), so for a 2025 Indiana case the stated three-source test can't literally be met.
5. research-resilience.md says research uses WebFetch and WebSearch only, while its Indiana Code chain admits iga.in.gov is unreadable and points to reference files and mirrors. The subagents read the local official Code download instead; the skill doesn't say whether that is allowed.
6. The 600–900 word limit is tight once every section, hire-trigger line and clause quote is included, and the template doesn't say whether *In plain terms* lines and suggested clause wording count as prose.
7. The live-matter screen's "legal deadline within 30 days" doesn't say whether a contractual offer deadline counts; treated as deal logistics.
