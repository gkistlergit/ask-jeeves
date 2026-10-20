# Trace: ask-jeeves, intermediate run on offer-letter-with-citation.md

Run date: 2026-10-20. Skill: `aj-skill/skills/ask-jeeves/SKILL.md`. Input: `fixtures/offer-letter-with-citation.md`. No other fixture file was opened. No git, browser, computer-use or clipboard was used.

## Files loaded (in order)
1. `SKILL.md`
2. Input document `fixtures/offer-letter-with-citation.md` (read in full)
3. `../../CONTEXT.md` (glossary the skill points to)
4. `references/choice-of-law.md` (step 3)
5. `templates/memo.md` (step 5; read early to plan)
6. `references/research-resilience.md` (read before the first web call and before any subagent dispatch)
7. `references/employee-contracts.md` (pages 1–224 and 225–265)
8. `references/restrictive-covenants.md`
9. `references/insider-theft.md`
10. `references/adjacent-fields.md`
11. Skill `humanizer` (loaded through the Skill tool for the plain-language pass)

`references/attorney-finder.md` was not loaded: Grant answered No at step 6, and step 7 runs only on a yes.

## Step 0: opening disclaimer
Shown once at the start of the request: "Not legal advice. Jeeves spots issues to raise with a licensed attorney; it is not a lawyer."

## Step 1: intake and live-matter screen
- Input read in full: a fictional offer letter dated October 1, 2026 (Senior Data Engineer, $128,000, start November 2, 2026, sign by October 9, 2026).
- Screen results:
  - Lawsuit or arbitration filed or threatened in writing: no.
  - Cease-and-desist or demand letter: no.
  - Government charge, subpoena or investigation: no.
  - Employer accusation of data taking: no.
  - Legal deadline within 30 days: no. The October 9 sign-by date has passed and is an offer deadline, not a legal deadline. The start date (Nov 2) is 13 days out. Both were carried into the memo as deal-logistics flags, and the start date was used as a hire trigger.
- Result: screen clear. Proceeded to step 2.

## Step 2: end goal, mode and depth
Question 1 (plain chat, verbatim):
> What's your end goal? For example: 'I must keep sole ownership of the 3 apps I built on my own time and money.' Or say 'no specific goal'.

Pre-supplied answer: "I must keep sole ownership of the 3 apps I created on my own time and with my own money."

Restatement shown (verbatim):
> So your goal is: keep sole ownership of the 3 apps you created on your own time and with your own money. Is that right?

Answer: confirmed.

Goal checks: the goal is lawful and not on the won't-do list. Re-ran the live-matter screen against it: still clear (no dispute exists over the apps).

Question 2 (one AskUserQuestion round, verbatim):
- **Mode:** Employer / Employee.
- **Depth:** Quick, about 1–2 minutes: built-in files only, unverified. / Intermediate (recommended), about 5–10 minutes: web-checked, quick-verified. / Deep, about 20–45 minutes: multi-source research plus a separate verifier.

Answers: Employee; Intermediate.

## Step 3: state selection
Pre-filled from the input:
- Choice-of-law clause: Indiana (§8).
- Forum clause: exclusive, state or federal courts in Marion County, Indiana (§8).
- Signing date: not stated (letter dated Oct 1, 2026; sign by Oct 9, 2026).
- Work location: Indianapolis office 3 days a week, remote otherwise (§ opening paragraph).
- Occupation and pay: Senior Data Engineer, $128,000 base.

Round 1 (AskUserQuestion, verbatim; asked even though the letter covers part of it, because the letter doesn't say where the remote work happens or where the employee lives):
1. Where does the employee work? Options: IN / SC / Remote from another state / Other (multi-select, with time share if split). Pre-filled: "Indianapolis office 3 days a week, remote the rest (from the letter)".
2. Where does the employee live? Options: Same as work / IN / SC / Other.
3. Where is the employer based, and where does it operate? Options: IN / SC / Multi-state / Other.
4. Where did the key events happen (resignation, data access, competing work)? Options: multi-select of states / Not yet.

Answers: works at the Indianapolis office 3 days a week and remotely from home in Indiana otherwise; lives in Indiana; employer based in and operates from Indiana; key events: not yet.

Round 2 (AskUserQuestion, verbatim; only the still-unknown item):
1. What date will you sign (or did you sign) the offer letter? Options: Not yet signed / Signed on <date> / Other.

Governing-law state and court, occupation and pay were answered from the document and not re-asked. Answer: "data engineer, $128,000, signing Oct 2026".

Decision procedure (choice-of-law.md Part 2):
1. Facts collected as above. No individual counsel indicated. No suit.
2. Override statutes: none met (Indiana is not an override state; the employee neither lives nor works in CA, CO, LA, MA, MN, WA, NM, UT, VT).
3. Florida CHOICE Act: not applicable (no Florida work or headquarters).
4. Clause names Indiana, which has a substantial relationship: provisional primary Indiana.
5. § 187(2)(b): the § 188 default state is also Indiana (work and residence both Indiana), so there is no conflict. Chosen and default state are the same, so no backup state results.
6. Forum: Marion County, Indiana, state or federal. Indiana or S.D. Ind. (under *Klaxon*) applies Indiana conflicts rules.
7. N/A (clause exists).
8. Split claims: a trade-secret tort claim would follow where misappropriation happened (Indiana) plus the DTSA. Noted; no claim exists.
9. Effective dates: signing Oct 2026; the only nearby Indiana change (IC 25-22.5-5.5-2.3, 2025-07-01) covers physicians and doesn't apply.
10. Uncertainty checklist: none of the 12 signals present.

Recommendation shown (verbatim):
```
Candidate state: Indiana (primary). Why: you live and work in Indiana, the employer is based there, and the letter picks Indiana law and Marion County courts.
Where they differ: n/a (no backup state)
Confidence: Clear
Confirm the applied state with a licensed attorney before relying on this.
```

Confirmation question (one AskUserQuestion, verbatim): "Which state's law should Jeeves apply?" Options: Confirm Indiana / Other state. The skill's "Use <backup> instead" and "Primary with backup notes" options were left out because the procedure yielded no backup state (see unclear items).

Answer: "Confirm Indiana". Research started only after this answer.

## Step 4: research at intermediate depth
Progress line shown to Grant: "Jeeves is checking sources for four areas in parallel (covenants, inventions and pay, trade secrets, adjacent issues); this takes a few minutes."

### Areas touched and reference files
- Restrictive covenants (§3, §4, §5): `restrictive-covenants.md`.
- Employee contracts (§2, §6, §7(a), §7(b), signing bonus): `employee-contracts.md`.
- Insider theft (§5, §7(c)): `insider-theft.md`.
- Adjacent fields (IP ownership, wage deductions, whistleblower carve-outs, NLRA flag): `adjacent-fields.md`.
- Applied state Indiana has a reference file in each, so no subagent was needed on that ground.

### Subagent decision
Dispatched 4 subagents (one per legal area), all `general-purpose`, all flat. Why: the intermediate rule dispatches "one subagent per legal area only when the request touches 2 or more areas and needs more than 8 sources opened". This request touched 4 areas, and the memo needed about 20 sources opened (17 ended up opened and cited, plus the input-citation checks). Each subagent got one area and its search budget from research-resilience §1 and §3, was told to use WebFetch and WebSearch only, to dispatch nothing, to write no files, and to return its complete result. All four ran in parallel and returned complete results. The main thread made no WebSearch or WebFetch calls itself.

Search budget split (intermediate cap 8 in total): restrictive covenants 3, employee contracts 2, insider theft 0, adjacent fields 0, main-thread reserve 3 (unused). No rate-limit or quota error occurred.

Search targets: each reference file's `as_of` is 2026-10-20 (today), so a "changes since as_of" check has no window. Searches went to the input citation (2), one Indiana 2025–26 non-compete change check (1), and the goal question, Indiana invention-assignment case law (2).

### Every WebSearch call (5 of 8)
| # | Agent | Query | Result |
|---|---|---|---|
| 1 | Restrictive covenants | `"258 N.E.3d 412"` | No case found at that citation; only volume-index pages for other volumes |
| 2 | Restrictive covenants | `"Hartwell Data Systems" v. Kessler Indiana Supreme Court` | No such case; only unrelated *Kessler v. Eldred* (U.S. 1907) and noise |
| 3 | Restrictive covenants | `Indiana Supreme Court 2025 non-compete covenant reasonableness blue pencil decision` | No 2025–26 decision; results centered on *Heraeus* (2019) and *Product Action Int'l v. Mero* (2003) commentary |
| 4 | Employee contracts | `Indiana Court of Appeals employee invention assignment agreement enforceability prior inventions own time` | No Indiana decision; other-state and secondary results |
| 5 | Employee contracts | `"Indiana law" employee invention assignment clause enforceable "Southern District of Indiana" OR "Seventh Circuit" OR "Northern District of Indiana" inventions unrelated to employer business` | Only *REXA, Inc. v. Chester* (7th Cir. 2022), which applied Massachusetts law; no Indiana-law case |

Search count: 5 of 8 used (3 + 2 + 0 + 0; main thread 0).

Privacy note: no query contained the employer's or employee's names, contract text or personal facts. Queries 1–2 used the reporter cite and case name of the authority the letter cites. I judged that a published legal citation, not a party name. The skill doesn't say so expressly (see unclear items).

### Every WebFetch call
Restrictive covenants subagent:
| URL | Result |
|---|---|
| https://caselaw.findlaw.com/court/in-supreme-court/2034943.html | *Heraeus* (Ind. Dec. 3, 2019, No. 19S-PL-471). Eraser rule confirmed; "any individual employed" non-solicit overbroad and void (the unfair-advantage limit is the court's contrast, not an express rule) |
| https://caselaw.findlaw.com/court/in-supreme-court/1134633.html | *Krueger* (Ind. Mar. 11, 2008). Protectable interest plus time/activity/geography confirmed; geography tied to where he practiced. Reporter cite not shown on the page |
| https://caselaw.findlaw.com/court/in-court-of-appeals/1646418.html | *Buffkin* (Ind. Ct. App. Oct. 7, 2013). Continental-U.S. scope unreasonable; training and know-how not protectable. Confirmed |
| https://caselaw.findlaw.com/court/in-court-of-appeals/1658360.html | *Clark's Sales* (Ind. Ct. App. Feb. 20, 2014). All competitive services overbroad; not divisible, unenforceable. Confirmed |
| https://caselaw.findlaw.com/court/in-court-of-appeals/116719877.html | *Med-1* (Ind. Ct. App. Nov. 25, 2024). "Any capacity" clause unenforceable; continued at-will employment is consideration. Confirmed; published/memorandum status not shown |
| https://caselaw.findlaw.com/court/in-supreme-court/1153073.html | *Allen* (Ind. Apr. 2, 2002). "favors contractual stipulations as to governing law." Confirmed |
| https://public.courts.in.gov/Decisions/ | Loaded with no listings (JavaScript-driven); inconclusive |
| https://public.courts.in.gov/decisions?c=9510 | Same; inconclusive |
| https://www.in.gov/courts/supreme/opinions/ | HTTP 404 |
| https://www.in.gov/courts/supreme/ | Loaded; no Hartwell or Kessler; links only to the search tool |
| https://www.in.gov/courts/public-records/appellate-decisions | Loaded; no Hartwell or Kessler |
| https://static.case.law/ne3d/ | Covers N.E.3d vols. 1–130 only; vol. 258 not available (not a negative) |
| Google Scholar case search for the case name | Redirected to google.com/sorry (CAPTCHA). Not bypassed; could not check |
| https://www.leagle.com/decisions/browse/series/volume/258%20N.E.3d | Vol. 258 pg. 412 holds three Supreme Court of Ohio entries; no Hartwell or Kessler anywhere in the volume |

Employee contracts subagent:
| URL | Result |
|---|---|
| https://www.law.cornell.edu/uscode/text/17/101 | Work-for-hire definition confirmed (scope of employment; nine categories by signed writing) |
| https://www.law.cornell.edu/uscode/text/17/201 | § 201(b) confirmed; the overriding writing must be signed by both parties |
| https://www.law.cornell.edu/uscode/text/17/204 | § 204(a) signed-writing rule confirmed |
| https://www.law.cornell.edu/uscode/text/17/410 | § 410(c) prima facie evidence within five years of publication confirmed |
| https://www.law.cornell.edu/uscode/text/35/261 | Written assignment; void against a later purchaser unless recorded within three months. Confirmed |
| https://www.law.cornell.edu/supremecourt/text/09-1159 | Syllabus only |
| https://www.law.cornell.edu/supct/html/09-1159.ZO.html | Majority: "rights in an invention belong to the inventor." "Agree to assign" vs "hereby assign" is Federal Circuit background; n.2 declines to rule. Confirmed with that caveat |
| https://www.law.cornell.edu/cfr/text/29/541.602 | Permitted deductions listed; none for lost or unreturned equipment. Confirmed |
| https://www.law.cornell.edu/cfr/text/29/541.603 | Improper-deduction practice; exemption lost for the class; safe harbor. Confirmed |
| https://foleyhoag.com/.../seventh-circuit-emphasizes-the-necessity-of-a-written-invention-assignment-agreement/ | Confirms *REXA v. Chester* applied Massachusetts law. Not cited |

Insider theft subagent:
| URL | Result |
|---|---|
| https://www.govinfo.gov/content/pkg/USCODE-2024-title18/html/USCODE-2024-title18-partI-chap90-sec1833.htm | § 1833(b) immunity, notice duty, sanction and post-May 11, 2016 scope confirmed; (b)(3)(B) policy cross-reference |
| https://static.case.law/ne2d/874/cases/1065-01.json | *Kopka* (Ind. Ct. App. Oct. 18, 2007). Duty of loyalty; may prepare to compete; no active competition; no use of confidential information (quoting *Potts*). Confirmed |
| https://www.govinfo.gov/content/pkg/USCODE-2024-title18/html/USCODE-2024-title18-partI-chap90-sec1839.htm | § 1839(3) confirmed, including "programs, or codes" |

Adjacent fields subagent:
| URL | Result |
|---|---|
| https://www.law.cornell.edu/cfr/text/17/240.21F-17 | Rule 21F-17(a) confirmed |
| https://www.law.cornell.edu/uscode/text/42/19403 | Speak Out Act confirmed; trade-secret savings in (d) |
| https://apps.nlrb.gov/link/document.aspx/09031d4584351740 | Binary PDF streams only; unreadable |
| https://www.nlrb.gov/guidance/memos-research/general-counsel-memos | GC 26-04 exists, dated 08/26/2026, "Further Guidance Regarding General Counsel Priorities"; no summary of content |

### How each citation was verified
Input document citation:
- *Hartwell Data Systems, Inc. v. Kessler*, 258 N.E.3d 412, 419 (Ind. 2025): **NOT FOUND: possibly fabricated.** Exists check failed at every source. The Indiana official search was inconclusive (JavaScript), the in.gov court pages had no mention, case.law doesn't cover the volume, Google Scholar returned a CAPTCHA (not bypassed), and two web searches found no such case. The Leagle index of 258 N.E.3d shows Ohio Supreme Court entries at pg. 412. Its claimed holding also conflicts with *Buffkin* and *Heraeus*. Handling: kept out of the reasoning, never replaced with a similar case, listed in the Bottom line and Sources as [12, NOT FOUND], shown in Risk #3's Law cell only as NOT FOUND.
- The letter cites no other authority.

Memo citations:
| [n] | Source | Exists | Supports claim (key claim spot-checked) | Status |
|---|---|---|---|---|
| 1 | 2026 Ind. Code, all titles (no invention-assignment statute) | Reference file (scan of the official 2026 download) | Negative finding per the file; subagent searches found no Indiana case either | From reference file, verified 2026-10-20 (iga.in.gov is JS-only per research-resilience) |
| 2 | 17 U.S.C. § 204(a) | Yes | Yes | Confirmed |
| 3 | 17 U.S.C. §§ 101, 201(b) | Yes | Yes | Confirmed |
| 4 | *Stanford v. Roche* | Yes | Yes (inventor owns first; wording point cited only as background) | Confirmed |
| 5 | 35 U.S.C. § 261 | Yes | Yes | Confirmed |
| 6 | 17 U.S.C. § 410(c) | Yes | Yes | Confirmed |
| 7 | *Heraeus* | Yes | Yes | Confirmed (mirror) |
| 8 | *Krueger* | Yes | Yes | Confirmed (mirror) |
| 9 | *Buffkin* | Yes | Yes | Confirmed (mirror) |
| 10 | *Clark's Sales* | Yes | Yes | Confirmed (mirror) |
| 11 | *Med-1* | Yes | Yes | Confirmed (mirror); publication status UNVERIFIED |
| 12 | *Hartwell* (input) | No | n/a | NOT FOUND |
| 13 | *Allen* | Yes | Yes | Confirmed (mirror) |
| 14 | *Kopka* | Yes | Yes | Confirmed (mirror) |
| 15 | 18 U.S.C. § 1833(b) | Yes | Yes | Confirmed |
| 16 | 18 U.S.C. § 1839(3) | Yes | Yes | Confirmed |
| 17 | IC 22-2-6-2(a)–(b) | Reference file | Per the file (checked against the official 2026 text) | From reference file, verified 2026-10-20 |
| 18 | IC 22-2-8-1 | Reference file | Per the file | From reference file, verified 2026-10-20 |
| 19 | 29 C.F.R. §§ 541.602–.603 | Yes | Yes | Confirmed |
| 20 | 17 C.F.R. § 240.21F-17(a) | Yes | Yes | Confirmed |
| 21 | 42 U.S.C. § 19403 | Yes | Yes | Confirmed |
| 22 | NLRB GC 26-04 | Number and date yes | Could not read the content | UNVERIFIED |

Totals: 17 opened and confirmed; 3 from reference files; 1 unverified; 1 not found.

## Step 5: memo
- Filled every section of `templates/memo.md`.
- Prose length: about 880 words, excluding header, table, block quotes, the quoted draft clause and sources. The first draft ran 1,391 words and was cut to fit 600–900.
- Goal in the header. Bottom line opens with "Uncertain to be reachable" and the reason. Path to your goal has 6 ordered steps, each tied to a risk number and a timing. Goal risks (#1–#4) rank first and carry the *(goal)* tag. #4 is also tagged *(practical)*.
- Hire triggers applied: High risks (#1, #2, #5); signing within 14 days (signing "Oct 2026", start Nov 2) on every Before-signing item. No criminal exposure, Uncertain state, backup state or agency was involved.
- Two creative options, each labeled, with Risk, Enforceability and a citation per legal premise: (A) copyright registration referenced in Exhibit A; (B) pre-signing assignment of the apps to an LLC Grant owns, with disclosure. Neither restates a recommendation; filling Exhibit A, the skill's own example, stayed a recommendation.
- Suggested clause wording is labeled "draft for your attorney to review."
- Adjacent fields: included fields (IP ownership, wage deductions, whistleblower) got analysis; deferred fields (NLRA, unemployment, tax, immigration) got one-line flags.
- Plain-language pass: loaded `humanizer` with the Skill tool. Applied it to the prose (no dashes in prose, no not-X-but-Y, no closers, straight quotes). Kept quotes, citations, statute and case names and glossary terms verbatim, and kept the template's required bold labels. The one remaining en dash sits inside the citation "IC 22-2-6-2(a)–(b)" and was left as is. Added an *In plain terms:* line after each quoted clause.
- Verification ending: intermediate form.

## Step 6: deliver
- Memo shown (here, written to `tests/memo-intermediate.md` because the test asked for it on disk).
- Question asked (verbatim): "Want Jeeves to find a budget-friendly, well-reviewed attorney licensed in Indiana?" Options: Yes / No.
- Answer: No.

## Step 7: attorney finder
Not run (answer No). `references/attorney-finder.md` not loaded.

## Unclear or contradictory points in the skill
1. Step 3.4's confirmation options assume a backup state ("Use <backup> instead", "Primary with backup notes"). When the procedure yields none, the skill doesn't say what to show. I showed "Confirm Indiana / Other state".
2. The intermediate rule says to "WebFetch every source you will cite", but research-resilience says iga.in.gov can't be fetched and that the reference files come first for Indiana Code. I followed research-resilience, so 3 IC cites rest on the reference files.
3. The intermediate searches are for "changes since each file's as_of". Every as_of is 2026-10-20, today, so that check has no window. The skill doesn't say what to spend the budget on otherwise. I used it on the input citation and the goal.
4. The subagent trigger ("needs more than 8 sources opened") is met by almost any multi-area intermediate request, because every cited source must be fetched. In practice intermediate always fans out, which may not be intended.
5. The privacy rule keeps "party names" and "contract text" out of queries, but step 4 requires checking authorities the input cites, which means searching a case name taken from the contract. I treated a published case citation as allowed.
6. The live-matter screen's "legal deadline within 30 days" doesn't say whether an offer's sign-by date or start date counts. The template's "passed sign-by date" flag implies it doesn't, which is how I read it.
7. The hire trigger "a signing or resignation within 14 days" needs a signing date, but round 2 got only "Oct 2026". I applied it because the start date is 13 days away.
8. 600–900 words of prose is tight for every section plus 6 risks and 2 creative options. The first full draft ran 1,391 words.
9. The humanizer removes bold labels (§19), while the template requires several. I kept the template's bold.
10. The Privacy rule says memos are saved to disk only when Grant asks. The test harness asked, so I saved.
