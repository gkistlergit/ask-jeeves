# Employee contracts: current law (Federal, Indiana, South Carolina)

Ticket: `.scratch/ask-jeeves/issues/03-employee-contracts-law.md`. Law as of 2026-10-20. Every source below was accessed on 2026-10-20. This is research for an issue-spotting skill. It is not legal advice.

Non-competes, non-solicits and NDAs are covered in depth by ticket 02 (`research/02-restrictive-covenants.md`). This file touches them only where an offer letter does.

## Summary

1. **At-will is the default in both states, and offer-letter wording can undo it.** Indiana presumes at-will "strong[ly]" (*Orr*). In South Carolina an offer e-mail guaranteeing two years' pay created a term contract (*Mathis*). SC handbooks need a signed, underlined, all-caps disclaimer on page 1 (§41-1-110).
2. **IP assignment.** Neither state has a statute protecting employee-owned inventions. Federal law decides form: signed writings (17 U.S.C. §204(a), 35 U.S.C. §261) and "hereby assign" wording.
3. **Device charges and clawbacks are the highest-risk clauses.**
   - Indiana allows a payroll deduction only under a written, signed, *revocable* wage assignment for a listed purpose. No listed purpose covers lost or unreturned property.
   - South Carolina allows deductions only if they were disclosed in writing. Bad-faith withholding risks treble damages.
   - Federally, no deduction may cut into the FLSA minimum wage or overtime.
4. **Arbitration.**
   - Class waivers are enforceable (*Epic*), except under the EFAA. In 2025–26 the 2d, 6th and 9th Circuits held that one plausible sexual-harassment claim takes the entire case out of arbitration. No 4th or 7th Circuit ruling was found.
   - SC refused to find an arbitration agreement in opt-out-by-silence (*Lampo*, 2025).
5. **Releases.**
   - OWBPA's checklist for workers 40 and over is unchanged.
   - FLSA claims can't be released privately (7th and 11th Circuits).
   - NLRB *McLaren Macomb* is still Board law, but the General Counsel is now asking the Board to overrule it (CHANGED 2025–26).
6. **Other 2025–26 changes.** The FTC non-compete rule was removed from the CFR (Feb. 12, 2026). *Flowers Foods* (May 2026) widened the FAA §1 transportation-worker exemption: there is no requirement to cross state lines. Indiana added an unauthorized-worker hiring statute (IC 22-5-9, July 1, 2026) and banned new physician–hospital non-competes (July 1, 2025). No South Carolina statutory change was found.

---

## Findings: Federal

### F-A. At-will and discharge limits

- **F1.** No federal statute makes employment at-will. State law sets the default, and federal statutes bar discharge for specific reasons. Title VII makes it unlawful "to discharge any individual" because of race, color, religion, sex or national origin.
  - Citation: 42 U.S.C. §2000e-2(a)(1) — https://www.law.cornell.edu/uscode/text/42/2000e-2 (acc. 2026-10-20).
  - Type: statute (LII mirror). Verified: Y for the statute.
  - The "no federal at-will statute" point is an inference from the absence of one, not a quoted rule.
- **F2.** Title VII also bars retaliation against anyone who "has opposed any practice" it makes unlawful, or who filed a charge or took part in a proceeding.
  - Citation: 42 U.S.C. §2000e-3(a) — https://www.law.cornell.edu/uscode/text/42/2000e-3 (acc. 2026-10-20).
  - Verified: Y.

### F-B. IP and invention assignment

- **F3.** A "work made for hire" is either:
  - a work an employee prepares within the scope of employment; or
  - a specially commissioned work in one of nine listed categories, and only "if the parties expressly agree in a written instrument signed by them."
  - Software from a contractor usually falls outside the nine categories.
  - Citation: 17 U.S.C. §101 — https://www.law.cornell.edu/uscode/text/17/101 (acc. 2026-10-20).
  - Verified: Y.
- **F4.** For a work made for hire, the employer is "considered the author," unless a signed writing says otherwise.
  - Citation: 17 U.S.C. §201(b) — https://www.law.cornell.edu/uscode/text/17/201 (acc. 2026-10-20).
  - Verified: Y.
- **F5.** Any copyright transfer other than by operation of law is valid only if it "is in writing and signed by the owner of the rights conveyed."
  - Citation: 17 U.S.C. §204(a) — https://www.law.cornell.edu/uscode/text/17/204 (acc. 2026-10-20).
  - Verified: Y.
- **F6.** Patents are assignable "by an instrument in writing." An unrecorded assignment is void against a later bona fide purchaser unless it is recorded at the USPTO within three months, or before that later purchase.
  - Citation: 35 U.S.C. §261 — https://www.law.cornell.edu/uscode/text/35/261 (acc. 2026-10-20).
  - Verified: Y.
- **F7.** *Stanford v. Roche* (June 6, 2011) holds that the Bayh-Dole Act doesn't vest title in federal contractors automatically: rights "belong to the inventor."
  - The Federal Circuit had read "agree to assign" as a mere promise to assign in the future, and "do hereby assign" as a present transfer. The Court recited that contrast in its background (and Justice Breyer's dissent discussed it). Footnote 2 (563 U.S. at 784 n.2) says only that the Court had "no occasion to pass on" the lower court's construction. *(Corrected 2026-10-20: the contrast is not in fn. 2 itself.)*
  - The FilmTec "hereby assign" rule therefore still governs in the Federal Circuit.
  - Citation: *Bd. of Trustees of Leland Stanford Jr. Univ. v. Roche Molecular Sys.*, 563 U.S. 776 (2011), No. 09-1159 — majority https://www.law.cornell.edu/supct/html/09-1159.ZO.html; concurrence https://www.law.cornell.edu/supct/html/09-1159.ZC.html; bound volume https://www.govinfo.gov/content/pkg/USREPORTS-563/pdf/USREPORTS-563-776.pdf (acc. 2026-10-20).
  - Verified: Y for the holding and fn. 2. Reporter cite 563 U.S. 776 verified 2026-10-20 (govinfo U.S. Reports PDF).
- **F8.** Who counts as an "employee" under §101 turns on the common law of agency, chiefly the hiring party's right to control the manner and means of the work. Other factors include skill, tools, location, duration, benefits and tax treatment. No single factor decides it.
  - Citation: *Community for Creative Non-Violence v. Reid*, 490 U.S. 730 (1989) — https://www.law.cornell.edu/supremecourt/text/490/730 (acc. 2026-10-20).
  - Verified: Y. Pin pages not checked.

### F-C. Limits on confidentiality and non-disparagement clauses

- **F9.** The Defend Trade Secrets Act gives immunity for confidential disclosures to a government official or an attorney, made solely to report a suspected violation of law, and for disclosures in a sealed court filing.
  - Citation: 18 U.S.C. §1833(b)(1)–(2) — https://www.law.cornell.edu/uscode/text/18/1833 (acc. 2026-10-20).
  - Verified: Y.
- **F10.** Any agreement with an employee that governs trade secrets or confidential information must notice this immunity: the employer "shall provide notice of the immunity set forth in this subsection."
  - A cross-reference to a policy that states it is enough.
  - The rule applies to contracts entered into or updated after May 11, 2016.
  - Citation: 18 U.S.C. §1833(b)(3)(A), (B), (D) — https://www.law.cornell.edu/uscode/text/18/1833 (acc. 2026-10-20).
  - Verified: Y.
- **F11.** Without the notice, the employer can't recover exemplary damages or attorney fees from that employee. Other remedies remain.
  - Citation: 18 U.S.C. §1833(b)(3)(C) — same URL (acc. 2026-10-20).
  - Verified: Y.
- **F12.** "Employee" here includes contractors and consultants, so their agreements need the notice too.
  - Citation: 18 U.S.C. §1833(b)(4) — same URL (acc. 2026-10-20).
  - Verified: Y.
- **F13.** Speak Out Act: a nondisclosure or nondisparagement clause agreed to before a sexual-assault or sexual-harassment dispute arises is not judicially enforceable for that dispute (§19403(a); §19402 holds only definitions).
  - Trade-secret protection survives (§19403(d)).
  - The Act applies to claims filed on or after Dec. 7, 2022 (§19404).
  - Citation: 42 U.S.C. §§19402–19404 (operative rule at §19403(a); corrected 2026-10-20) — https://www.law.cornell.edu/uscode/text/42/19403 and https://www.law.cornell.edu/uscode/text/42/19404 (acc. 2026-10-20).
  - Verified: Y.
- **F14.** SEC Rule 21F-17(a): "No person may take any action to impede an individual from communicating" with the SEC. That includes enforcing a confidentiality agreement.
  - Citation: 17 C.F.R. §240.21F-17(a) — https://www.law.cornell.edu/cfr/text/17/240.21F-17 (acc. 2026-10-20).
  - Verified: Y for the text. SEC enforcement in 2025–26 was not checked.
- **F15.** Under *McLaren Macomb* (Feb. 21, 2023), merely offering a severance agreement with broad confidentiality or non-disparagement terms that waive NLRA §7 rights violates §8(a)(1).
  - Citation: *McLaren Macomb*, 372 NLRB No. 58 — https://www.nlrb.gov/news-outreach/news-story/board-rules-that-employers-may-not-offer-severance-agreements-requiring (acc. 2026-10-20).
  - Type: agency (Board release). Verified: Y.
  - Conflict: the NLRB's April 6–10, 2026 weekly summary prints "No. 48." The decisions index and GC 26-04 say No. 58.
- **F16.** Under *Stericycle* (Aug. 2, 2023), a work rule is presumptively unlawful if it has "a reasonable tendency to chill employees' exercise" of §7 rights.
  - Citation: *Stericycle, Inc.*, 372 NLRB No. 113 — https://www.nlrb.gov/cases-decisions/weekly-summaries-decisions/summary-of-nlrb-decisions-for-week-of-july-31-august-4-0 (acc. 2026-10-20).
  - Verified: Y.
- **F17. CHANGED 2025–26.** GC 25-05 (Feb. 14, 2025) rescinded several General Counsel memos, including:
  - GC 23-05 (McLaren guidance);
  - GC 23-08 and GC 25-01 (non-competes and stay-or-pay);
  - GC 23-02 (electronic monitoring).
  - Memos are guidance only. Rescinding them doesn't overrule Board decisions.
  - Citation: https://www.nlrb.gov/news-outreach/news-story/gc-25-05-rescission-of-certain-general-counsel-memoranda (acc. 2026-10-20).
  - Verified: Y.
- **F18. CHANGED 2025–26.** The Board regained a quorum on Jan. 7, 2026, when Murphy and Mayer were sworn in.
  - Citation: https://www.nlrb.gov/news-outreach/news-story/james-murphy-and-scott-mayer-sworn-in-as-board-members-0 and https://www.nlrb.gov/about-nlrb/who-we-are/the-board (acc. 2026-10-20).
  - Verified: Y for the swearing-in and the current four-member roster.
  - Member Macy was sworn in Aug. 17, 2026 (term to Aug. 27, 2030), giving a 3–1 Republican-appointed majority: https://www.nlrb.gov/news-outreach/news-story/james-r-macy-sworn-in-as-board-member (verified 2026-10-20).
  - UNVERIFIED: the date Murphy became Chairman (no opened page states it).
- **F19. CHANGED 2025–26.** In *Prime Communications, LP* (Apr. 7, 2026), the Board unanimously held that overbroad severance confidentiality and non-disparagement terms are unlawful.
  - Two members (Chairman Murphy and Member Mayer) applied *McLaren* as extant precedent but "would be open to reconsideration of that precedent." Member Prouty, the third panelist, did not join that statement.
  - Citation: 374 NLRB No. 88 — https://www.nlrb.gov/cases-decisions/weekly-summaries-decisions/summary-of-nlrb-decisions-for-week-of-april-6-10-2026 (acc. 2026-10-20).
  - Verified: Y.
- **F20. CHANGED 2025–26.** GC 26-04 (Aug. 26, 2026, GC Crystal Carey) says she is "Arguing to overrule McLaren Macomb" (in *Valley Radiology*) and "Arguing to overturn Stericycle" (in *Honeywell*). Regional offices keep applying "extant Board law" in the meantime.
  - Citation: https://apps.nlrb.gov/link/document.aspx/09031d4584351740 (acc. 2026-10-20).
  - Verified: Y (full text read).
- **F21. CHANGED 2025–26.** I checked the Board's weekly summaries through Oct. 9, 2026. None overrules *McLaren* or *Stericycle*.
  - In *Beatrice Loving Heart* (375 NLRB No. 56, Sept. 30, 2026), the Board found overbroad exit-letter terms unlawful.
  - In the same case, the majority severed a handbook confidentiality-rule allegation "for further consideration." That is a sign *Stericycle* may be revisited.
  - Citation: https://www.nlrb.gov/cases-decisions/weekly-summaries-decisions/summary-of-nlrb-decisions-for-week-of-september-28-1 (acc. 2026-10-20).
  - Verified: Y. Decisions from Oct. 12–16 were not yet summarized. Re-checked 2026-10-20: the Oct. 5–9 summary (posted Oct. 16) overrules neither case.
  - Related, added by the verifier: in *Ralphs Grocery Co.*, 375 NLRB No. 25 (Aug. 10, 2026), the Board unanimously held an arbitration-policy ban on disclosing an arbitration's *existence* unlawful. A Murphy–Mayer majority upheld confidentiality of its content and outcome, and found the savings clause adequate; Prouty dissented on both. Source: https://www.nlrb.gov/cases-decisions/weekly-summaries-decisions/summary-of-nlrb-decisions-for-week-of-august-10-14-2026 (acc. 2026-10-20). Verified: Y (Board summary only; decision text not opened).

### F-D. Wages, deductions, device charges, clawbacks

- **F22.** FLSA wages must be paid "finally and unconditionally or 'free and clear'." A kick-back to the employer fails that test.
  - Making employees supply tools of the trade violates the Act in any week where the cost cuts into minimum wage or overtime.
  - Citation: 29 C.F.R. §531.35 — https://www.law.cornell.edu/cfr/text/29/531.35 (acc. 2026-10-20).
  - Verified: Y.
- **F23.** In weeks without overtime, a deduction is allowed only if the employee still nets the minimum wage in cash.
  - Citation: 29 C.F.R. §531.36 — https://www.law.cornell.edu/cfr/text/29/531.36 (acc. 2026-10-20).
  - Verified: Y.
- **F24.** Items "primarily for the benefit or convenience of the employer," such as tools of the trade, can't be credited as wages.
  - Citation: 29 C.F.R. §531.3(d) — https://www.law.cornell.edu/cfr/text/29/531.3 (acc. 2026-10-20).
  - Verified: Y.
- **F25.** DOL Fact Sheet #16 treats deductions for shortages, damage to employer property and theft as being for the employer's benefit. Such a deduction "may not reduce the employee's wage below the minimum wage" or required overtime.
  - This holds even if the employee was negligent.
  - Requiring a separate cash repayment doesn't avoid the rule.
  - Citation: https://www.dol.gov/agencies/whd/fact-sheets/16-flsa-wage-deductions (acc. 2026-10-20).
  - Type: agency guidance. Verified: Y.
- **F26.** An exempt employee's salary is "not subject to reduction because of variations in the quality or quantity" of work.
  - §541.602(b) lists the only permitted deductions. None covers lost, damaged or unreturned equipment.
  - Citation: 29 C.F.R. §541.602 — https://www.law.cornell.edu/cfr/text/29/541.602 (acc. 2026-10-20).
  - Verified: Y.
- **F27.** A practice of improper deductions can cost the exemption for everyone in that job classification under the same managers. A safe harbor applies if the employer has a communicated policy, a complaint process and reimburses.
  - Citation: 29 C.F.R. §541.603 — https://www.law.cornell.edu/cfr/text/29/541.603 (acc. 2026-10-20).
  - Verified: Y.
- **F28.** Training-cost repayment has been upheld as repayment of a voluntary loan, not a kick-back, where final-week pay stayed at or above minimum wage. *Gordon* followed the 7th Circuit's *Heder v. City of Two Rivers*, 295 F.3d 777 (7th Cir. 2002).
  - Citation: *Gordon v. City of Oakland*, 627 F.3d 1092 (9th Cir. Nov. 19, 2010), No. 09-16167 — https://caselaw.findlaw.com/us-9th-circuit/1545305.html (acc. 2026-10-20).
  - Verified: Y for *Gordon*, including the reporter cite (upgraded 2026-10-20). *Heder*, 295 F.3d 777 (7th Cir. July 10, 2002), verified 2026-10-20 at https://static.case.law/f3d/295/cases/0777-01.json.
  - UNVERIFIED: any DOL opinion letter on training repayment (none located on dol.gov).
- **F29.** SEC Rule 10D-1's mandatory clawback reaches only exchange-listed issuers. It gives a private employer no clawback right.
  - Citation: 17 C.F.R. §240.10D-1 — https://www.law.cornell.edu/cfr/text/17/240.10D-1 (acc. 2026-10-20).
  - Verified: Y.

### F-E. Devices, BYOD, return of property

- **F30.** CFAA "exceeds authorized access" means obtaining information "that the accesser is not entitled so to obtain."
  - A civil suit requires a listed harm, usually loss of $5,000 or more in a year.
  - The limitations period is 2 years.
  - Citation: 18 U.S.C. §1030(e)(6), (g) — https://www.law.cornell.edu/uscode/text/18/1030 (acc. 2026-10-20).
  - Verified: Y.
- **F31.** *Van Buren*: CFAA liability is a "gates-up-or-down inquiry." Misusing data you are allowed to reach, for example in breach of a "business purposes only" policy, isn't a violation. Footnote 8 leaves open whether contract or policy limits can count as "gates."
  - Citation: *Van Buren v. United States*, No. 19-783 (June 3, 2021) — https://www.supremecourt.gov/opinions/20pdf/19-783_k53l.pdf (slip op. pg. 13 fn. 8) (acc. 2026-10-20).
  - Verified: Y. Reporter cite 593 U.S. 374 verified 2026-10-20 (preliminary print https://www.supremecourt.gov/opinions/20pdf/593us2r42_n7ip.pdf).
- **F32.** The Stored Communications Act bars intentional unauthorized access to a communications facility that obtains stored communications.
  - It excepts conduct authorized by the service provider (for example, the employer's own e-mail system) or by the user.
  - Civil remedies include $1,000 minimum damages, punitive damages if willful, and attorney fees.
  - Citation: 18 U.S.C. §§2701, 2707 — https://www.law.cornell.edu/uscode/text/18/2701 and https://www.law.cornell.edu/uscode/text/18/2707 (acc. 2026-10-20).
  - Verified: Y.
  - My inference, not a verified case: the provider exception doesn't reach an employee's personal Gmail or iCloud on a BYOD phone.

### F-F. Arbitration and class waivers

- **F33.** FAA §2 makes arbitration clauses "valid, irrevocable, and enforceable." The savings clause keeps general contract defenses. The 2022 amendment adds "or as otherwise provided in chapter 4" (the EFAA).
  - Citation: 9 U.S.C. §2 — https://www.law.cornell.edu/uscode/text/9/2 (acc. 2026-10-20).
  - Verified: Y.
- **F34.** FAA §1 exempts "contracts of employment" of seamen, railroad employees and "any other class of workers engaged in foreign or interstate commerce."
  - Citation: 9 U.S.C. §1 — https://www.law.cornell.edu/uscode/text/9/1 (acc. 2026-10-20).
  - Verified: Y.
- **F35.** Class and collective waivers in employment arbitration agreements are enforceable, and the NLRA doesn't override them: "The policy may be debatable but the law is clear."
  - Citation: *Epic Systems Corp. v. Lewis*, 584 U.S. 497 (2018) — https://www.law.cornell.edu/supremecourt/text/16-285 (acc. 2026-10-20).
  - Verified: Y.
- **F36.** Three other Supreme Court rulings on the FAA:
  - A ramp supervisor who loads airline cargo is a §1-exempt worker (*Southwest Airlines Co. v. Saxon*, 596 U.S. 450 (2022)).
  - "A transportation worker need not work in the transportation industry" (*Bissonnette v. LePage Bakeries*, 601 U.S. 246 (2024)).
  - A court must stay, not dismiss, when a party asks for a §3 stay (*Smith v. Spizzirri*, 601 U.S. 472 (2024)).
  - Citations: https://www.law.cornell.edu/supremecourt/text/21-309; https://www.law.cornell.edu/supremecourt/text/23-51; https://www.law.cornell.edu/supremecourt/text/22-1218 (acc. 2026-10-20).
  - Verified: Y.
- **F37.** Waiving the right to arbitrate requires no showing of prejudice. A court "may not devise novel rules to favor arbitration over litigation."
  - Citation: *Morgan v. Sundance, Inc.*, 596 U.S. 411 (2022) — https://www.law.cornell.edu/supremecourt/text/21-328 (acc. 2026-10-20).
  - Verified: Y.
- **F38. CHANGED 2025–26.** A worker who carries goods on an intrastate leg of an interstate journey can qualify for the §1 exemption without crossing state lines or interacting with vehicles that do. Unanimous (Gorsuch, J.). Affirmed 121 F.4th 753 (10th Cir.).
  - The worker was a Denver-area franchisee who distributes Flowers's baked goods within Colorado.
  - Limit (added 2026-10-20): the Court rejected only the bright-line cross-state rule. It expressly did not decide whether his independent company, or his taking title to the goods, defeats the exemption.
  - Citation: *Flowers Foods, Inc. v. Brock*, No. 24-935, 608 U.S. 380 (May 28, 2026) — https://www.supremecourt.gov/opinions/25pdf/608us2r37_i425.pdf (syllabus pg. 380–81) (acc. 2026-10-20).
  - Verified: Y (I read the preliminary print myself).
- **F39. CHANGED 2025–26.** A federal court that stayed claims under §3 has jurisdiction to confirm or vacate the resulting award, even with no independent basis for jurisdiction. Unanimous. The underlying suit was an employment-discrimination case.
  - Citation: *Jules v. Andre Balazs Properties*, No. 25-83, 608 U.S. 200 (May 14, 2026) — https://www.supremecourt.gov/opinions/25pdf/608us1r31_8759.pdf (syllabus pg. 200–01) (acc. 2026-10-20).
  - Verified: Y (read myself).
- **F40.** EFAA: at the election of "the person alleging" a sexual-harassment or sexual-assault dispute, no predispute arbitration agreement or joint-action waiver is enforceable for a case that "relates to" that dispute.
  - A court, not an arbitrator, decides whether the EFAA applies, under federal law, even if the contract delegates arbitrability.
  - Citation: 9 U.S.C. §402(a)–(b) — https://www.law.cornell.edu/uscode/text/9/402 (acc. 2026-10-20).
  - Verified: Y.
- **F41.** The EFAA applies to any dispute or claim that "arises or accrues on or after" Mar. 3, 2022. A joint-action waiver is covered whether or not it sits inside an arbitration clause (§401(2)).
  - Citations: Pub. L. 117-90 §3, noted at https://www.law.cornell.edu/uscode/text/9/402; 9 U.S.C. §401 at https://www.law.cornell.edu/uscode/text/9/401 (acc. 2026-10-20).
  - Verified: Y.
- **F42.** "Accrue" in EFAA §3 carries its statute-of-limitations meaning. A hostile-environment claim reaccrues with each act, so a hostile-environment course of conduct that continues past Mar. 3, 2022 accrues after the Act. The test is when the claim accrued, not when the agreement was signed. *(Reworded 2026-10-20.)*
  - Citation: *Olivieri v. Stifel, Nicolaus & Co.*, No. 23-658 (2d Cir. Aug. 12, 2024) — https://govinfo.gov/content/pkg/USCOURTS-ca2-23-00658/pdf/USCOURTS-ca2-23-00658-0.pdf (pg. 2, 5, 25) (acc. 2026-10-20).
  - Verified: Y.
- **F43. CHANGED 2025–26.** "Dispute arises" and "claim accrues" are separate inquiries. A dispute arises when there is adversity, meaning "some aspect of opposition or disagreement." Here the dispute predated Mar. 3, 2022, so the EFAA didn't apply.
  - Citation: *Cornelius v. CVS Pharmacy Inc.*, No. 23-2961 (3d Cir. Apr. 2, 2025) (precedential) — https://www.govinfo.gov/content/pkg/USCOURTS-ca3-23-02961/pdf/USCOURTS-ca3-23-02961-0.pdf (pg. 10–12) (acc. 2026-10-20).
  - Verified: Y. The plaintiff conceded her claim accrued before the Act, so only the "dispute arises" prong was live. The court also vacated in part on arbitration-agreement formation (discovery needed).
- **F44. CHANGED 2025–26.** The 6th Circuit adopted the adversity test: a dispute arises when the employee voices disagreement and the employer opposes it, expressly or constructively.
  - Citation: *Memmer v. United Wholesale Mortgage, LLC*, No. 24-1144 (6th Cir. Apr. 18, 2025) — https://www.govinfo.gov/content/pkg/USCOURTS-ca6-24-01144/pdf/USCOURTS-ca6-24-01144-0.pdf (pg. 10, 15) (acc. 2026-10-20).
  - Verified: Y. Reversed and remanded for the district court to apply the test. Thapar, J., dissented.
- **F45. CHANGED 2025–26.** One plausibly pleaded sexual-harassment claim means "the EFAA bars arbitration of Bruce's entire case," including her ADA claims. The court left open whether the pleading test is plausibility or "nonfrivolous."
  - Citation: *Bruce v. Adams & Reese, LLP*, 168 F.4th 367 (6th Cir. Feb. 25, 2026), No. 25-5210 — https://www.opn.ca6.uscourts.gov/opinions.pdf/26a0054p-06.pdf (pg. 2, 8, 15–17) (acc. 2026-10-20).
  - Verified: Y (read myself). Moore, J., with Ritz, J. Thapar, J., dissented on whether the harassment claim was plausibly pleaded. The F.4th cite is taken from *Ding*'s citation of it; the reporter itself was not opened.
- **F46. CHANGED 2025–26.** A plaintiff who discovers an EFAA-covered claim during arbitration may leave arbitration and take her entire case to court. Starting arbitration on other claims was neither an election nor a waiver.
  - Citation: *Ding v. Structure Therapeutics, Inc.*, No. 25-1532 (9th Cir. Aug. 19, 2026) — https://cdn.ca9.uscourts.gov/datastore/opinions/2026/08/19/25-1532.pdf (pg. 16, 20–21) (acc. 2026-10-20).
  - Verified: Y. Published; Sanchez, J., with Miller, J.; Rawlinson, J., dissented on the election point. The no-waiver holding rests on the district court's finding that she didn't know of a plausible sex-harassment claim when she filed for arbitration.
- **F47. CHANGED 2025–26.** *Diaz-Roa v. Hermes Law, P.C.*, No. 24-3223-cv (2d Cir. Sept. 30, 2026) (Bianco, J., for Walker, Bianco and Pérez, JJ.) holds that a properly invoked EFAA election invalidates the arbitration agreement "as to the entire lawsuit," including non-harassment claims. Affirmed.
  - Citation: slip opinion (Justia copy) https://cases.justia.com/federal/appellate-courts/ca2/24-3223/24-3223-2026-09-30.pdf (pg. 2) (acc. 2026-10-20). Lead: https://www.sullcrom.com/insights/blogs/2026/October/Second-Circuit-Holds-EFAA-Takes-Entire-Case-Out-of-Arbitration (secondary).
  - Verified: Y (upgraded 2026-10-20 from the slip-opinion text; not opened on the 2d Circuit's own site).
- **F48.** The 4th Circuit (South Carolina) has only an unpublished ruling that the EFAA "does not apply retroactively" to pre-Mar. 3, 2022 claims. No published 4th Circuit decision on EFAA scope was found.
  - Citation: *Bopda v. Comcast of the District, LLC*, No. 23-2148 (4th Cir. Feb. 2, 2024) (unpublished) — https://www.govinfo.gov/content/pkg/USCOURTS-ca4-23-02148/pdf/USCOURTS-ca4-23-02148-0.pdf (acc. 2026-10-20).
  - Verified: Y. Not binding precedent.
- **F49.** No 7th Circuit (Indiana) EFAA opinion was found. A govinfo full-text search returned none.
  - District courts in Indiana and South Carolina: UNVERIFIED, not searched because of rate limits.

### F-G. Severance and releases

- **F50.** OWBPA: a waiver of ADEA claims is knowing and voluntary only if, at a minimum:
  - it is written to be understood;
  - it refers to the ADEA by name;
  - it doesn't waive claims arising after signing;
  - it gives consideration beyond what is already owed;
  - it advises the employee in writing to consult a lawyer;
  - it allows 21 days to consider (45 days for a group or exit program);
  - it allows 7 days to revoke;
  - for a group program, it discloses the decisional unit, eligibility factors, and "the job titles and ages" of those selected and not selected.
  - Citation: 29 U.S.C. §626(f)(1)(A)–(H) — https://www.law.cornell.edu/uscode/text/29/626 (acc. 2026-10-20).
  - Verified: Y.
- **F51.** "No waiver agreement may affect the Commission's rights and responsibilities." A waiver can't be used to stop anyone from filing an EEOC charge or taking part in an investigation.
  - Citation: 29 U.S.C. §626(f)(4) — same URL (acc. 2026-10-20).
  - Verified: Y.
- **F52.** Under the EEOC regulations:
  - the 7-day revocation period "cannot be shortened";
  - a material change to the offer restarts the 21- or 45-day period;
  - no provision may bar or penalize filing a charge, including a charge that challenges the waiver.
  - Citation: 29 C.F.R. §1625.22(e), (i) — https://www.ecfr.gov/api/versioner/v1/full/2026-10-16/title-29.xml?part=1625&section=1625.22 (acc. 2026-10-20).
  - Type: regulation (eCFR, current to 2026-10-16). Verified: Y.
- **F53.** No tender-back of severance is required before an ADEA suit. A covenant not to sue may not carry penalties, such as tender-back or fee-shifting for an ADEA suit. Any setoff is capped.
  - Citation: 29 C.F.R. §1625.23 — https://www.ecfr.gov/api/versioner/v1/full/2026-10-16/title-29.xml?part=1625&section=1625.23 (acc. 2026-10-20).
  - Verified: Y.
- **F54.** A release that fails OWBPA "cannot bar the ADEA claim," and keeping the severance pay doesn't ratify it.
  - Citation: *Oubre v. Entergy Operations, Inc.*, 522 U.S. 422 (1998) — https://www.law.cornell.edu/supremecourt/text/522/422 (acc. 2026-10-20).
  - Verified: Y.
- **F55.** The EEOC's 2009 Q&A on severance waivers is still posted with no rescission notice. It says employees can still file a charge after signing a waiver, and that courts are split on tender-back for non-ADEA claims.
  - Citation: https://www.eeoc.gov/laws/guidance/qa-understanding-waivers-discrimination-claims-employee-severance-agreements (acc. 2026-10-20).
  - Type: agency guidance. Verified: Y.
- **F56.** FLSA rights can't be waived by private agreement where there is no bona fide dispute; allowing it "would nullify the purposes of the Act."
  - Citation: *Brooklyn Savings Bank v. O'Neil*, 324 U.S. 697 (1945) — https://www.law.cornell.edu/supremecourt/text/324/697 (acc. 2026-10-20).
  - Verified: Y.
- **F57.** Courts "have refused to enforce wholly private settlements" of FLSA claims (*Walton*, 786 F.2d at 306, citing *Lynn's* at 1352; the quoted phrase is Walton's, not Lynn's). The two routes are a DOL-supervised settlement under §216(c) or court approval.
  - Citations:
    - *Walton v. United Consumers Club, Inc.*, 786 F.2d 303 (7th Cir. 1986) — https://static.case.law/f2d/786/cases/0303-01.json (acc. 2026-10-20).
    - *Lynn's Food Stores, Inc. v. United States*, 679 F.2d 1350 (11th Cir. 1982) — https://static.case.law/f2d/679/cases/1350-01.json (acc. 2026-10-20).
  - Verified: Y.
  - The 4th Circuit (SC) has only dicta: *Taylor v. Progress Energy*, 493 F.3d 454, 460 (4th Cir. 2007), an FMLA case reasoning by analogy to the FLSA, at https://static.case.law/f3d/493/cases/0454-01.json. A square 4th Circuit holding is UNVERIFIED (none found). A 2024 D. Md. approval order says the 4th Circuit "has not established a definitive rubric" and district courts follow *Lynn's* (https://www2.mdd.uscourts.gov/Opinions/Opinions/2024-03-22%20Conrad%20granting%20mot%20to%20approve%20settlement%20(21-2951-JMC).pdf).
- **F58. CHANGED 2025–26.** The EEOC regained a quorum (Chair Lucas plus two commissioners). It voted 2–1 on Jan. 22, 2026 to rescind its 2024 harassment guidance. No 2025–26 vote touched releases, severance or arbitration.
  - Citations: https://www.eeoc.gov/commission and https://www.eeoc.gov/commission-votes-january-2026 (acc. 2026-10-20).
  - Verified: Y. That the EEOC lacked a quorum for most of 2025 is inferred from gaps in its vote pages; the site doesn't say so.

### F-H. Non-competes (status only; detail in ticket 02)

- **F59. CHANGED 2025–26.** The FTC voted 3–1 on Sept. 5, 2025 to dismiss its appeals and accept vacatur of the Non-Compete Clause Rule. The FTC's rule page says the rule "is not in effect and it is not enforceable."
  - Citations: https://www.ftc.gov/news-events/news/press-releases/2025/09/federal-trade-commission-files-accede-vacatur-non-compete-clause-rule and https://www.ftc.gov/legal-library/browse/rules/noncompete-rule (acc. 2026-10-20).
  - Verified: Y.
- **F60. CHANGED 2025–26.** A final rule, published and effective Feb. 12, 2026, removed 16 C.F.R. Part 910 from the CFR.
  - Citation: 91 FR 6507, FR Doc. 2026-02866 — https://www.federalregister.gov/api/v1/documents/2026-02866.json (acc. 2026-10-20).
  - Verified: Y (metadata and abstract; the HTML page was bot-blocked).
- **F61. CHANGED 2025–26.** The FTC now acts case by case. Two proposed consent orders:
  - *Gateway Services* (pet cremation, published Sept. 10, 2025): bans noncompetes.
  - *Rollins/Orkin* (published Apr. 22, 2026): bans noncompetes for covered employees and also bars "fees or penalties" tied to a noncompete.
  - Citations: 90 FR 43606 — https://www.federalregister.gov/documents/full_text/html/2025/09/10/2025-17416.html; 91 FR 21497 — https://www.federalregister.gov/documents/full_text/html/2026/04/22/2026-07844.html (acc. 2026-10-20).
  - Verified: Y. Final-order dates and FTC warning letters are UNVERIFIED (URLs returned 404; search budget exhausted).

---

## Findings: Indiana

Indiana Code text is from the official 2026 Code files on iga.in.gov (`https://iga.in.gov/ic/2026/Title_NN.html`).

### IN-A. At-will and how contracts alter it

- **IN1.** Indiana has two kinds of employment: for a definite or ascertainable term, or at-will.
  - The at-will presumption is "strong."
  - A definite-term contract can be ended early only for cause or by mutual agreement, unless the employer reserved an early-termination right.
  - *Orr* declined to decide whether a handbook can ever be a unilateral contract. It held only that this handbook, with "suggestive rather than mandatory" discipline language plus a signed disclaimer, created no contract as a matter of law. *(Corrected 2026-10-20: the original said handbooks are never unilateral contracts.)*
  - Citation: *Orr v. Westminster Village North, Inc.*, 689 N.E.2d 712 (Ind. 1997) — https://caselaw.findlaw.com/court/in-supreme-court/1089282.html (acc. 2026-10-20).
  - Verified: Y.
- **IN2.** *Orr* recognizes only three exceptions to at-will: adequate independent consideration, public policy, and promissory estoppel. Quitting another job or moving, standing alone, is not adequate independent consideration.
  - Citation: same as IN1. Verified: Y.
- **IN3.** Public-policy exceptions:
  - an employee "discharged solely for exercising a statutorily conferred right" (filing a workers' compensation claim) has a claim;
  - so does an employee fired for "refusing to commit an illegal act for which he would be personally liable." *(Quote corrected 2026-10-20.)*
  - Citations:
    - *Frampton v. Central Indiana Gas Co.*, 297 N.E.2d 425 (Ind. 1973) — https://www.courtlistener.com/opinion/2031331/frampton-v-central-indiana-gas-company/ (acc. 2026-10-20).
    - *McClanahan v. Remington Freight Lines*, 517 N.E.2d 390 (Ind. 1988) — https://www.courtlistener.com/opinion/2097690/mcclanahan-v-remington-freight-lines-inc/ (acc. 2026-10-20).
  - Verified: Y.
- **IN4.** Leaving a "permanent" state-police job on the employer's assurance of permanent employment can be adequate independent consideration, enough to defeat summary judgment.
  - Procedure (added 2026-10-20): the Supreme Court (Aug. 20, 1987) adopted Judge Conover's Court of Appeals dissent (499 N.E.2d 768 (1986)) by reference and reversed summary judgment on the contract claim. It made no final finding that a contract existed.
  - Citation: *Romack v. Public Service Co.*, 511 N.E.2d 1024 (Ind. 1987) — https://www.courtlistener.com/opinion/2062078/romack-v-public-service-co-of-indiana/ (acc. 2026-10-20).
  - Verified: Y.
- **IN5.** Promissory estoppel on a promise of employment allows reliance damages only. Lost post-discharge wages are "not recoverable."
  - Citation: *Jarboe v. Landmark Community Newspapers*, 644 N.E.2d 118 (Ind. 1994) — https://www.courtlistener.com/opinion/2150024/jarboe-v-landmark-community-newspapers-of-indiana-inc/ (acc. 2026-10-20).
  - Verified: Y.
  - Conflict: *Orr* cites it as "(Ind. 1995)." It was decided Dec. 15, 1994; rehearing was denied in 1995.
- **IN6.** Continued at-will employment can be consideration for a restrictive covenant: "This is sufficient independent consideration to support the 2014 Agreement."
  - The court also held a covenant barring work in any capacity unreasonable and, with nothing to strike, unenforceable.
  - Citation: *Med-1 Solutions, LLC v. Taylor*, No. 24A-PL-450 (Ind. Ct. App. Nov. 25, 2024) — https://caselaw.findlaw.com/court/in-court-of-appeals/116719877.html (acc. 2026-10-20).
  - Verified: Y (read myself). UNVERIFIED: whether it is a published opinion or a memorandum decision, which affects its precedential weight in Indiana.

### IN-B. IP and invention assignment

- **IN7.** Indiana has no statute limiting assignment of employee-owned inventions, nothing like Cal. Lab. Code §2870.
  - Method: a keyword scan of all 37 titles of the 2026 Code for "invention" near "employ." The only hit was a tax provision (IC 6-3-2-21.7).
  - Citation: https://iga.in.gov/ic/2026/Title_1.html through Title_37.html (acc. 2026-10-20).
  - Verified: Y (negative finding). No 2025–26 change.
- **IN8.** The Indiana Uniform Trade Secrets Act:
  - defines a trade secret by independent economic value plus reasonable secrecy efforts (IC 24-2-3-2);
  - displaces all *conflicting* state law "except contract law and criminal law" (24-2-3-1(c));
  - allows exemplary damages up to twice the subsection (a) award (not the royalty award) for willful and malicious misappropriation (24-2-3-4). *(Both points tightened 2026-10-20.)*
  - Citation: https://iga.in.gov/ic/2026/Title_24.html (acc. 2026-10-20).
  - Verified: Y. No 2025–26 change.
- **IN9.** No Indiana appellate decision on the reach of an invention-assignment clause was found. UNVERIFIED either way: the search budget ran out, and the prior research also found none.

### IN-C. Wage payment, deductions, clawbacks

- **IN10.** Wages must be paid at least semimonthly, or biweekly if requested, for work done up to "not more than ten (10) business days prior to the date of payment." "Any contract in violation of this subsection is void." *(Wording corrected 2026-10-20.)*
  - An employee who quits is paid on the next regular payday.
  - Citation: IC 22-2-5-1 — https://iga.in.gov/ic/2026/Title_22.html (acc. 2026-10-20).
  - Verified: Y. No 2025–26 change.
- **IN11.** Attorney fees and costs are mandatory in a wage case. Liquidated damages of "two (2) times the amount of wages due" apply only if the employer "was not acting in good faith."
  - Citation: IC 22-2-5-2 (as amended by P.L.193-2015) — same URL (acc. 2026-10-20).
  - Verified: Y.
  - Conflict: *St. Vincent v. Steele* (2002) quotes the older 10%-per-day formula with no good-faith limit. That text is superseded.
- **IN12.** When the employer separates an employee, final wages are due on the regular payday for the pay period in which separation occurred.
  - In a dispute, the conceded amount must be paid "without condition," and accepting it "shall not constitute a release" of the balance.
  - Citation: IC 22-2-9-2, -3 — same URL (acc. 2026-10-20).
  - Verified: Y.
- **IN13.** Which statute applies depends on how employment ended:
  - employees the employer separated proceed under the Wage Claims Statute, IC 22-2-9, through the Department of Labor;
  - current employees and those who quit proceed under the Wage Payment Statute, IC 22-2-5.
  - Citation: *St. Vincent Hosp. & Health Care Ctr. v. Steele*, 766 N.E.2d 699 (Ind. 2002) — https://www.courtlistener.com/opinion/853188/st-vincent-hospital-health-care-center-inc-v-steele/ (acc. 2026-10-20).
  - Verified: Y.
- **IN14.** A bonus tied to production "and also the expenses of the overall business is not a 'wage.'" A bonus for time worked can be.
  - Citation: *Highhouse v. Midwest Orthopedic Inst.*, 807 N.E.2d 737 (Ind. 2004) — https://www.courtlistener.com/opinion/852921/highhouse-v-midwest-orthopedic-institute-pc/ (acc. 2026-10-20).
  - Verified: Y.
- **IN15.** A payroll deduction is a wage assignment. It is valid only if it is:
  - in writing and signed by the employee personally;
  - "by its terms revocable at any time" on written notice;
  - agreed to in writing by the employer;
  - delivered to the employer within 10 days;
  - for a purpose listed in IC 22-2-6-2(b).
  - New (f), added by P.L.104-2026, lets (b)(19) retirement assignments skip these conditions. It doesn't affect private employers.
  - Citation: IC 22-2-6-1, -2(a) — https://iga.in.gov/ic/2026/Title_22.html (acc. 2026-10-20).
  - Verified: Y.
- **IN16.** The listed purposes that matter for offer letters:
  - (b)(14): uniforms and job clothing, at no more than vendor cost;
  - (b)(15): equipment or tools "necessary to fulfill the duties of employment," at no more than vendor cost;
  - (b)(16): reimbursement of education or skills training, but not training funded by an economic-development incentive;
  - (b)(17): pay advances.
  - (d) caps (b)(14) and (b)(15) together at the lesser of $2,500 a year or 5% of weekly disposable earnings.
  - (e) bars charging for OSHA-required protective equipment.
  - **No listed purpose covers damage to, loss of, or failure to return employer property.**
  - Citation: IC 22-2-6-2(b), (d), (e) — same URL (acc. 2026-10-20).
  - Verified: Y.
- **IN17. CHANGED 2025–26 (technical; no effect on private employers' deduction rules).** Two 2026 acts amended IC 22-2-6-2, both effective July 1, 2026:
  - P.L.104-2026 (SB 14) added (b)(19) for political-subdivision retirement contributions;
  - P.L.115-2026 (SB 169) updated consumer-credit cross-references.
  - Citations: https://iga.in.gov/pdf-documents/124/2026/senate/bills/SB0014/SB0014.05.ENRH.pdf and https://iga.in.gov/pdf-documents/124/2026/senate/bills/SB0169/SB0169.04.ENRH.pdf (acc. 2026-10-20).
  - Verified: Y.
- **IN18.** An overpayment deduction is neither a fine nor a wage assignment. It requires 2 weeks' notice, can't take a disputed amount, and is capped (the lesser of 25% of weekly disposable earnings or the amount above 30 times the federal minimum wage).
  - Citation: IC 22-2-6-4 — same URL (acc. 2026-10-20).
  - Verified: Y.
- **IN19.** An employer may not "assess a fine on any pretext" and withhold it from wages. A violation is a Class C infraction.
  - Citation: IC 22-2-8-1 — same URL (acc. 2026-10-20).
  - Verified: Y.
- **IN20.** No Indiana statute addresses waiving or releasing wage-statute rights generally. A scan of IC 22-2, 22-5 and 22-6 for waive, waiver and release found only 22-2-9-3 and unrelated sections.
  - No Indiana case on releasing Wage Payment Statute claims, or on clawing back training costs from final pay, was found: UNVERIFIED, search budget exhausted.
  - Citation: https://iga.in.gov/ic/2026/Title_22.html (acc. 2026-10-20).
  - Verified: Y (for the scan only).

### IN-D. Arbitration

- **IN21.** Indiana's Uniform Arbitration Act makes written agreements to arbitrate existing or future disputes enforceable. It "also applies to arbitration agreement between employers and employees" unless the agreement says otherwise. A court must compel arbitration and stay the case.
  - Citation: IC 34-57-2-1, -3 — https://iga.in.gov/ic/2026/Title_34.html (acc. 2026-10-20).
  - Verified: Y.
  - CHANGED 2025–26 (technical only): P.L.115-2026 SEC. 82 updated a cross-reference, effective July 1, 2026.
- **IN22.** UNVERIFIED: Indiana appellate law on employment arbitration, class waivers and unconscionability. No primary source was opened because the search budget ran out.
  - Upgrade attempt 2026-10-20: still no employment-specific Indiana appellate decision found. Closest is a nursing-home case, *Sanford v. Castleton Health Care Ctr.*, 813 N.E.2d 411 (Ind. Ct. App. 2004), which states the general unconscionability test (verified at static.case.law). It doesn't answer the employment question.

### IN-E. Releases, references, service letters

- **IN23.** When an employee quits or is discharged, the employer must, on the employee's written request, give a signed letter "setting forth whether the employee quit or was involuntarily discharged." The duty doesn't apply to employers that don't require written applications or recommendations.
  - Citation: IC 22-6-3-1 — https://iga.in.gov/ic/2026/Title_22.html (acc. 2026-10-20).
  - Verified: Y.
  - Conflict: *Orr* fn. 1 quotes an older version that required stating the cause of leaving.
- **IN24.** Blacklisting a discharged employee is a Class C infraction with "penal damages" (IC 22-5-3-1(a)). A company that lets its agents blacklist must fully compensate the employee, and exemplary damages may be added (IC 22-5-3-2; no infraction). Employers are immune for disclosures about current or former employees unless the information was known to be false (IC 22-5-3-1(b), not -2). *(Corrected 2026-10-20: the original merged the two sections.)*
  - Citation: IC 22-5-3-1, -2 — same URL (acc. 2026-10-20).
  - Verified: Y.

### IN-F. Devices, BYOD, return of property

- **IN25.** Accessing a computer system or network without the owner's consent is computer trespass, a Class A misdemeanor. "Computer network" includes cellular devices. IC 35-43-1-4, the older section, was repealed in 2013.
  - Citation: IC 35-43-2-3 — https://iga.in.gov/ic/2026/Title_35.html (acc. 2026-10-20).
  - Verified: Y. The cellular-device language is in 35-43-2-3(a) itself. UNVERIFIED: what P.L.111-2026 SEC.6 changed in this section (its history shows the amendment).
- **IN26.** A person who suffers a pecuniary loss from an IC 35-43 property offense, such as criminal conversion (IC 35-43-4-3), may recover up to 3 times actual damages plus costs and attorney fees.
  - This is the employer's lever for an unreturned device, not a wage deduction.
  - Citations: IC 34-24-3-1 and IC 35-43-4-3 — https://iga.in.gov/ic/2026/Title_34.html and Title_35.html (acc. 2026-10-20).
  - Verified: Y. UNVERIFIED: what P.L.142-2026 SEC.5 changed in IC 34-24-3-1 (its history shows the amendment).
- **IN27.** Indiana has no statute on employee social-media or password privacy, and no general statute requiring employers to reimburse business or remote-work expenses. Method: a keyword scan of all titles and of Title 22.
  - Citation: https://iga.in.gov/ic/2026/ (acc. 2026-10-20).
  - Verified: Y (negative finding). No 2025–26 change.

### IN-G. 2025–26 legislation

- **IN28. CHANGED 2025–26.** A physician and a hospital, hospital parent, affiliated manager or hospital system "may not enter into a noncompete agreement on or after July 1, 2025." Violating agreements are void.
  - It reaches agreements "originally entered into" on or after that date. Amendments and renewals of older agreements don't count.
  - For physicians employed 3 or more years, "noncompete" includes bonus or training repayment based "solely or primarily" on practicing with a new employer.
  - Still allowed: NDAs; non-solicits of *current employees* lasting 1 year or less, which may not restrict patient interactions or referrals; and noncompetes in the sale of a practice more than 50% physician-owned. *(Scope tightened 2026-10-20.)*
  - Citation: SEA 475 (2025), P.L.207-2025, IC 25-22.5-5.5-1.1 to -2.3 — https://iga.in.gov/legislative/2025/bills/senate/475/details (acc. 2026-10-20).
  - Verified: Y.
  - Conflict: the lead attributing this change to HEA 1004 is wrong. HEA 1004 is P.L.216-2025.
- **IN29.** SB 132 (2026), which would have barred noncompetes for employees paid under $150,000, was referred to committee on Jan. 5, 2026, got no further action, and is marked dead. Not enacted.
  - Citation: https://iga.in.gov/legislative/2026/bills/senate/132/details (acc. 2026-10-20); introduced text https://iga.in.gov/pdf-documents/124/2026/senate/bills/SB0132/SB0132.01.INTR.pdf.
  - Verified: Y for the bill, its content and its Jan. 5 referral. Re-check 2026-10-20: the status page (a JavaScript app) couldn't be read, so "marked dead" rests on the first pass. Only the introduced printing exists, which is consistent with no further action.
- **IN30. CHANGED 2025–26.** New IC 22-5-9 (SEA 76, P.L.106-2026 SEC.16, effective July 1, 2026) makes it unlawful to knowingly recruit, hire or continue to employ an unauthorized alien. It is not limited to new hires: it excludes only conduct before July 1, 2026, so continuing to employ after that date is covered. *(Corrected 2026-10-20 from "for hires from July 1, 2026".)*
  - E-Verify or "industry standard best practices" is a defense.
  - The Attorney General enforces it. A first-time employer gets notice and a 15-business-day window to cure and file an affidavit. License suspensions escalate (5 days, 10 days, 180 days) up to permanent revocation, with 6–24 months' probation.
  - Citation: https://iga.in.gov/ic/2026/Title_22.html; enrolled act https://iga.in.gov/pdf-documents/124/2026/senate/bills/SB0076/SB0076.08.ENRH.pdf (acc. 2026-10-20).
  - Verified: Y.
- **IN31. CHANGED 2025–26.** New IC 22-2-20 (P.L.109-2025): no adverse action against an employee for attending, per calendar year, one school attendance conference and one case-conference meeting for their child, with 5 days' notice. *(Corrected 2026-10-20: the original said one meeting a year in total.)* It covers employers with 1 or more employees. The time may be unpaid. The chapter expires July 1, 2029.
  - Citation: same URL (acc. 2026-10-20).
  - Verified: Y.
- **IN32. CHANGED 2025–26.** Two other 2025–26 acts amended the minimum-wage chapter:
  - tip pooling, new IC 22-2-2-14.1 (P.L.15-2026);
  - minimum-wage definitions in IC 22-2-2-3 (P.L.67-2025). The substance of the P.L.67-2025 change was not examined.
  - The Indiana minimum wage still tracks the federal one (IC 22-2-2-4(c), unamended).
  - Citation: same URL (acc. 2026-10-20).
  - Verified: Y for the fact of amendment.
- **IN33.** No 2025 or 2026 public law appears in the section histories of IC 22-2-5, 22-2-9, 22-6-3, 22-5-3 or 24-2-3.
  - Citation: https://iga.in.gov/ic/2026/Title_22.html and Title_24.html (acc. 2026-10-20).
  - Verified: Y.

---

## Findings: South Carolina

Statute text is from scstatehouse.gov code pages. *(Corrected 2026-10-20: the original said the pages are marked current through the 2025 session. The pages opened on re-check show no "current through" date.)* 2026 acts were checked against the 2025–26 ratification log. Opinions are from sccourts.org.

### SC-A. At-will and how contracts alter it

- **SC1.** A handbook, policy or other employer document issued after June 30, 2004 creates no contract if it is conspicuously disclaimed.
  - For a handbook, the disclaimer "must be in underlined capital letters on the first page" and be signed by the employee.
  - For other documents, it must be in underlined capitals on page 1; no signature is needed.
  - Whether a disclaimer is conspicuous is a question of law.
  - Citation: S.C. Code §41-1-110 — https://www.scstatehouse.gov/code/t41c001.php (acc. 2026-10-20).
  - Verified: Y.
- **SC2.** Handbooks issued before July 2004 follow the older rule: a disclaimer is "merely one factor," and whether a contract exists is a jury question. (*Conner* (2005) quotes "merely one factor" from *Conner I*, 348 S.C. 454 (2002).) §41-1-110 applies only to documents issued after June 30, 2004.
  - The *Small v. Springs Industries* (1987) rule, that mandatory handbook procedures can bind the employer, comes through these later opinions.
  - Citation: *Conner v. City of Forest Acres*, Op. No. 25961 (S.C. Apr. 4, 2005) — https://www.sccourts.org/media/opinions/HTMLFiles/SC/25961.htm (acc. 2026-10-20).
  - Verified: Y for *Conner*. *Small* is verified only as *Conner* and *Prescott* describe it.
- **SC3.** A public-policy exception: a discharge that violates "a clear mandate of public policy" gives an at-will employee a tort claim.
  - It applies to an at-will contract with a notice provision.
  - An employee hired for a definite term can't be discharged before it ends without just cause.
  - Citation: *Stiles v. American General Life Ins. Co.*, Op. No. 24945 (S.C. 1999), quoting *Ludwick v. This Minute of Carolina*, 337 S.E.2d 213 (S.C. 1985) — https://www.sccourts.org/media/opinions/HTMLFiles/SC/24945.htm (acc. 2026-10-20).
  - Verified: Y (*Ludwick* only through *Stiles*).
- **SC4.** The exception isn't limited to illegal-act cases. It does not apply "where the employee has an existing statutory remedy for wrongful termination."
  - The Payment of Wages Act contains no such remedy.
  - Citation: *Barron v. Labor Finders of S.C.*, 713 S.E.2d 634, Op. No. 27018 (S.C. Aug. 1, 2011) — https://www.sccourts.org/media/opinions/HTMLFiles/SC/27018.htm (acc. 2026-10-20).
  - Verified: Y for the holding. The S.E.2d cite is UNVERIFIED (not on the slip opinion). Context: summary judgment for the employer was affirmed, and the court didn't decide whether retaliation for a wage complaint is protected.
- **SC5.** At-will status "may be altered by an oral contract of definite employment." Vague assurances such as "keep your nose clean" are puffery, not an offer.
  - Citation: *Prescott v. Farmers Telephone Coop.*, 516 S.E.2d 923, Op. No. 24948 (S.C. 1999) — https://www.sccourts.org/media/opinions/HTMLFiles/SC/24948.htm (acc. 2026-10-20).
  - Verified: Y.
- **SC6.** An offer e-mail guaranteeing first-year salary and second-year earnings created a two-year term contract, which defeated the employer's at-will defense.
  - Citation: *Mathis v. Brown & Brown of S.C., Inc.*, 698 S.E.2d 773, Op. No. 26851 (S.C. 2010) — https://www.sccourts.org/media/opinions/HTMLFiles/SC/26851.htm (acc. 2026-10-20).
  - Verified: Y.
- **SC7.** No 2025–26 SC Supreme Court decision on at-will employment or wrongful discharge was found. Method: captions of Op. Nos. 28240–28352 and a Court of Appeals scan of Op. Nos. 6085–6166.
  - Re-scan 2026-10-20 (SC 28250–28354, COA 6090–6165; published opinions only): same result. One tangential case: *Luce v. Lexington County Health Servs. Dist.*, Op. No. 28294 (S.C. Aug. 6, 2025), a certified question holding that shift-differential and call-back pay are "earnable compensation" for state retirement deductions.
  - Citation: https://www.sccourts.org/ (acc. 2026-10-20).
  - Verified: Y within that scope.

### SC-B. IP, trade secrets, confidentiality

- **SC8.** South Carolina has no statute limiting assignment of employee inventions. Method: searched every chapter of Titles 39 and 41 for "invention," with zero hits; other titles weren't searched.
  - Citation: https://www.scstatehouse.gov/code/title41.php and https://www.scstatehouse.gov/code/title39.php (acc. 2026-10-20).
  - Verified: Y (negative finding, within those titles).
- **SC9.** The SC Trade Secrets Act protects information with independent economic value and reasonable secrecy efforts. "Improper means" includes breach of a duty imposed by contract.
  - Citation: S.C. Code §39-8-20 — https://www.scstatehouse.gov/code/t39c008.php (acc. 2026-10-20).
  - Verified: Y.
- **SC10.** An employee has a statutory duty not to misuse a known trade secret, independent of any agreement.
  - A contractual secrecy duty is not void "for lack of a durational or geographical limitation."
  - Contract remedies aren't displaced (§39-8-110(B)(1)).
  - Citation: S.C. Code §39-8-30(B), (D) — same URL (acc. 2026-10-20).
  - Verified: Y.

### SC-C. Wages, deductions, clawbacks (Payment of Wages Act)

All at https://www.scstatehouse.gov/code/t41c010.php (acc. 2026-10-20). Statute. No amendment since 1993.

- **SC11.** "Wages" includes pay on a commission basis or "other method." It also includes vacation, holiday and sick pay due under employer policy or contract. Severance is not included: a 1990 amendment deleted "and severance" from the definition.
  - Citation: §41-10-10(2). Verified: Y.
- **SC12.** At hire, the employer must give written notice of wages, pay times and the deductions to be made. Changes must be "in writing at least seven calendar days" before they take effect.
  - Employers with fewer than five employees at all times during the preceding 12 months, and employers of domestic labor in private homes, are exempt from all of §41-10-30: notice, records and itemized statements (§41-10-20). *(Corrected 2026-10-20: the exemption is not limited to the notice duty.)*
  - Wage increases need no advance notice.
  - Citation: §41-10-30(A). Verified: Y.
- **SC13.** An employer "shall not withhold or divert any portion of an employee's wages" unless law requires or permits it, or the deduction was noticed in writing under §41-10-30(A).
  - Citation: §41-10-40(C). Verified: Y.
- **SC14.** A separated employee, "for any reason," must be paid within 48 hours or by the next regular payday, not more than 30 days later.
  - Citation: §41-10-50. Verified: Y.
- **SC15.** In a dispute, the employer must pay the conceded amount unconditionally. Accepting it is not a release of the balance.
  - Citation: §41-10-60. Verified: Y.
- **SC16.** An employee may recover "three times the full amount of the unpaid wages," plus costs and reasonable attorney fees "as the court may allow." Suit must be filed within 3 years. The statute doesn't call trebling discretionary; that comes from case law (*Rice*, via *Mathis*; see SC18). *(Corrected 2026-10-20.)*
  - Citation: §41-10-80(C). Verified: Y.
- **SC17.** The chapter's protections may not "be contravened or set aside by a private agreement."
  - Citation: §41-10-100. Verified: Y.
- **SC18.** Treble damages are discretionary. Trebling where there is a bona fide dispute "would be unjust and harsh," and reasonableness is judged when the wages were withheld.
  - Post-termination earnings are not "wages" under the Act.
  - Citation: *Mathis* (SC6), quoting *Rice v. Multimedia, Inc.*, 456 S.E.2d 381 (S.C. 1995) — https://www.sccourts.org/media/opinions/HTMLFiles/SC/26851.htm (acc. 2026-10-20).
  - Verified: Y (*Rice* only through *Mathis*).
- **SC19. CHANGED 2025–26 (case law).**
  - The court affirmed a Payment of Wages Act recovery for annual bonuses owed under an employment agreement. Treble damages were affirmed because the employer had no "good faith, bona fide basis" to withhold them (pg. 14–17). The court didn't separately analyze whether bonuses are "wages" under §41-10-10(2). *(Corrected 2026-10-20: the original stated that as a holding.)*
  - Vague bonus terms that the employer's lawyers drafted were read against the employer (pg. 10–11).
  - The 3-year limitations period is subject to the discovery rule (pg. 8–9, not 10–11).
  - A changed bonus formula didn't bind the employee without the 7-day written notice of §41-10-30(A) (pg. 12–14).
  - Prejudgment interest was reversed because the claim was unliquidated. Attorney fees were raised to $450/hr.
  - Citation: *Hess v. Morphis Pediatric Group of Lancaster, P.A.*, Op. No. 6115 (S.C. Ct. App. July 9, 2025) (Vinson, J.; Thomas and Hewitt, JJ., concurring) — https://www.sccourts.org/media/opinions/HTMLFiles/COA/6115.pdf (acc. 2026-10-20).
  - Verified: Y (read myself, re-read 2026-10-20). Later history, such as a cert petition, not checked.
- **SC20.** UNVERIFIED: no SC appellate case was found on deductions for unreturned property, devices or training costs, or on whether a negotiated release of a disputed wage claim survives §41-10-100. The search budget ran out before a targeted search.
- **SC21.** South Carolina's labor department (LLR) restates the 48-hour / 30-day final-pay rule and the 7-day notice for pay cuts. It gives no guidance specific to deductions.
  - Citations: https://llr.sc.gov/wage/faq.aspx and https://llr.sc.gov/wage/paymentofwages.aspx (acc. 2026-10-20).
  - Type: agency guidance. Verified: Y for the FAQ. The FAQ applies the 7-day notice to employers with 5 or more employees. The paymentofwages.aspx page states neither rule and only links to the FAQ. *(Corrected 2026-10-20.)*

### SC-D. Arbitration

- **SC22.** The arbitration notice "shall be typed in underlined capital letters, or rubber-stamped prominently, on the first page" of the contract. Without it, the contract is not subject to arbitration under the SC Act.
  - Citation: S.C. Code §15-48-10(a) — https://www.scstatehouse.gov/code/t15c048.php (acc. 2026-10-20).
  - Verified: Y (read myself).
- **SC23.** The SC Act doesn't cover employer–employee agreements "unless the agreement provides that this chapter shall apply."
  - Workers' compensation, unemployment and collective-bargaining claims can't be made subject to it.
  - An agreement to apply the Act "shall not be made a condition of employment."
  - Citation: §15-48-10(b)(2) — same URL (acc. 2026-10-20).
  - Verified: Y (read myself).
  - Conflict: the ticket brief's paraphrase said "specifically provides." The text says "provides."
- **SC24.** Unless the parties contract otherwise, the FAA governs agreements in transactions that in fact involve interstate commerce. The SC Act's notice rule is preempted only to the extent it would invalidate an FAA-covered agreement. Note: *Bennett* is a patient, insurer and provider-agreement case, not an employment case, and there the parties' choice-of-law clause selected the SC Act. *(Qualifiers added 2026-10-20.)*
  - Citation: *Bennett v. ACS Primary Care Physicians–Southeast, P.C.*, Op. No. 6089 (S.C. Ct. App. Sept. 18, 2024) — https://www.sccourts.org/media/opinions/HTMLFiles/COA/6089.pdf (pg. 10–12) (acc. 2026-10-20).
  - Verified: Y.
- **SC25. CHANGED 2025–26 (case law).** An employee's failure to opt out of an e-mailed arbitration program, plus continued work, was not acceptance as a matter of law, so no agreement was formed. Decided 3–2: Few, J., with Kittredge, C.J., and James, J.; Verdin, J., dissented, joined by Acting Justice Curtis. The court reversed the Court of Appeals (437 S.C. 236, 877 S.E.2d 486 (Ct. App. 2022)) and remanded for discovery and trial.
  - The opinion suggests that added consideration, or making the program a condition of employment, could change the result.
  - The court repeated that there is no public policy, federal or state, "favoring" arbitration (citing *Palmetto Construction Group*, Op. No. 28010 (2021)).
  - Citation: *Lampo v. Amedisys Holding, LLC*, Op. No. 28265 (S.C. Mar. 5, 2025) — https://www.sccourts.org/media/opinions/HTMLFiles/SC/28265.pdf (pg. 7–9) (acc. 2026-10-20).
  - Verified: Y (read myself). S.E.2d cite not checked.
- **SC26.** Arbitration terms in an adhesion contract were held unconscionable. The court refused to sever them despite a severability clause, because severing would "encourage sophisticated parties" to overreach. (Home-sale contract, not employment.)
  - Citation: *Damico v. Lennar Carolinas, LLC*, Op. No. 28114 (S.C. 2022) — https://www.sccourts.org/media/opinions/HTMLFiles/SC/28114.pdf (pg. 6, 9, 13) (acc. 2026-10-20).
  - Verified: Y.
- **SC27.** South Carolina courts won't read an arbitration clause to cover "outrageous torts" that were unforeseeable. *Partain* (2010) applied the rule.
  - In *Parsons v. John Wieland Homes* (2016), only two justices would have overruled it. No 2024–26 case abandoning it was found.
  - Citations:
    - *Aiken v. World Finance*, Op. No. 26313 (S.C. 2007) — https://www.sccourts.org/media/opinions/HTMLFiles/SC/26313.htm
    - *Partain v. Upstate Automotive Group*, Op. No. 26768 (S.C. 2010) — https://www.sccourts.org/media/opinions/HTMLFiles/SC/26768.htm
    - *Parsons*, Op. No. 27655 — https://www.sccourts.org/media/opinions/HTMLFiles/SC/27655.pdf (pg. 10)
    - all acc. 2026-10-20.
  - Verified: Y.
  - Conflict: a lead dating *Partain* to 2023, as a rejection of the exception, is wrong.
  - Upgraded 2026-10-20: in *Parsons*, Hearn, J. (joined by Beatty, J.) called the exception a viable principle but found it inapplicable, concurring in result. Acting Justice Toal, dissenting, treated it as viable and applicable. So three justices kept the exception alive.

### SC-E. Releases, references, devices

- **SC28.** An employer is immune for disclosing dates of employment and pay history. It is also immune for written answers to a prospective employer's written request about evaluations, reasons for separation and performance. Immunity is lost for knowingly or recklessly false information.
  - No service-letter or blacklisting statute was found in Title 41, Chapter 1 or 10.
  - Citation: S.C. Code §41-1-65 — https://www.scstatehouse.gov/code/t41c001.php (acc. 2026-10-20).
  - Verified: Y.
- **SC29.** No SC statute governing releases of employment claims was found in Title 41 or §15-48.
  - Citation: https://www.scstatehouse.gov/code/title41.php (acc. 2026-10-20).
  - Verified: Y within that scope.
- **SC30.** Under the Computer Crime Act:
  - "computer" includes, without limitation, "digital cellular telephones" and notebooks;
  - "computer hacking" includes use that "exceeds any right or permission granted by the appropriate principal";
  - the civil action lies only against a person **convicted** under the chapter.
  - Citation: S.C. Code §§16-16-10(a), (j)(5), 16-16-20, 16-16-25 — https://www.scstatehouse.gov/code/t16c016.php (acc. 2026-10-20).
  - Verified: Y.
- **SC31.** No SC statute on employee social-media or password privacy, or on employer expense reimbursement, was found. Method: searched Title 41 Chapters 1, 7, 8 and 10, Title 16 Chapters 16–17, and the 2025–26 ratifications.
  - The 2026 social-media act (R251, H. 4591) regulates platforms, not employers.
  - Citation: https://www.scstatehouse.gov/sess126_2025-2026/bills/rats.php (acc. 2026-10-20).
  - Verified: Y within that scope.

### SC-F. 2025–26 legislation; non-competes

- **SC32.** No 2025–26 statutory change was found to Title 41 (including E-Verify and wage payment), §15-48, §39-8, §16-16, minimum wage, non-competes or arbitration.
  - Method: read all 19 ratification sheets (R1–R277, log updated Aug. 26, 2026), searched them for the relevant code sections and terms, and checked code-page histories.
  - Re-check 2026-10-20: all linked sheets were read again (the verifier counted 21, not 19). Same result: Title 41 is touched only by R130 (amusement rides), R192 (a DHEC omnibus) and R264 (unemployment trust fund).
  - Citation: https://www.scstatehouse.gov/sess126_2025-2026/bills/rats.php (acc. 2026-10-20).
  - Verified: Y.
  - UNVERIFIED: pending, unratified non-compete bills, and anything ratified after Aug. 26, 2026.
- **SC33.** A covenant signed mid-employment needs consideration beyond continued at-will employment.
  - Citation: *Poole v. Incentives Unlimited*, 548 S.E.2d 207, Op. No. 25299 (S.C. 2001) — https://www.sccourts.org/media/opinions/HTMLFiles/SC/25299.htm (acc. 2026-10-20).
  - Verified: Y.
  - Conflict: the lead credited this rule to *Stonhard*. It comes from *Poole*.
- **SC34.** South Carolina courts won't rewrite an overbroad non-compete:
  - a covenant with no geographic limit can't be "reformed or blue-penciled" (*Stonhard*);
  - restrictions "cannot be rewritten by a court or limited by the parties' agreement" (*Poynter*). *Poynter* reversed only the trial judge's own rewritten territory. It never ruled on whether the contract's step-down tiers were valid, and it arose from a sale of a business. So "step-down clauses fail" is an inference, not a holding. *(Corrected 2026-10-20.)*
  - *Stonhard*'s rule is narrower than "no reformation at all": a covenant with no geographic limit may not be reformed "so as to add an entirely new term." It answered certified questions.
  - Citations:
    - *Stonhard, Inc. v. Carolina Flooring Specialists*, Op. No. 26047 (S.C. 2005) — https://www.sccourts.org/media/opinions/HTMLFiles/SC/26047.htm
    - *Poynter Investments v. Century Builders*, Op. No. 26821 (S.C. 2010) — https://www.sccourts.org/media/opinions/HTMLFiles/SC/26821.htm
    - both acc. 2026-10-20.
  - Verified: Y. *Poynter*'s S.E.2d cite is not checked.

### Indiana note on non-competes (cross-reference to ticket 02)

- **IN34.** Indiana non-competes are enforceable only "to the extent they are reasonable." The blue pencil "permits excising language but not rewriting."
  - *Heraeus* adds: "This doctrine, though, is really an eraser." A reformation clause can't authorize a court to add terms.
  - Citations:
    - *Central Indiana Podiatry, P.C. v. Krueger*, 882 N.E.2d 723 (Ind. 2008) — https://www.courtlistener.com/opinion/852486/central-indiana-podiatry-pc-v-krueger/
    - *Heraeus Medical, LLC v. Zimmer, Inc.*, No. 19S-PL-471 (Ind. Dec. 3, 2019) — https://caselaw.findlaw.com/court/in-supreme-court/2034943.html
    - both acc. 2026-10-20.
  - Verified: Y.

---

## Offer-letter clause checklist

| Clause | Federal | Indiana | South Carolina | Typical risk |
|---|---|---|---|---|
| **At-will** | No federal at-will rule; discrimination and retaliation limits apply (F1–F2). | Strong presumption. A definite term means cause is needed; "permanent" assurances to someone leaving a secure job can create a contract (IN1–IN5). | Guaranteed pay or duration in an offer can create a term contract (SC6). Handbook disclaimer must be underlined caps on page 1 and signed (SC1). Pre-July 2004 handbooks are a jury question (SC2). | **Medium.** The main risk is guarantee language ("first-year salary," "two-year earnings," "permanent"). |
| **IP / invention assignment** | Needs a signed writing (F5–F6). Use "hereby assign" (F7). Work-for-hire language alone doesn't cover contractors (F3, F8). | No statutory protection for employee-owned inventions (IN7). Contract law governs. | Same; none found (SC8). | **Low for employer form; medium for employee scope.** Breadth (off-hours work, post-employment work) is decided by contract reading, not statute, in both states. |
| **Confidentiality** | DTSA notice or lose exemplary damages and fees (F10–F12). Carve-outs for SEC (F14), Speak Out Act (F13), EEOC (F51). NLRA limits for non-supervisors (F15–F21). | UTSA preserves contract remedies (IN8). | NDA can be unlimited in time and place for trade secrets (SC10). | **Medium.** Missing DTSA notice and NLRA overbreadth are the common faults. NLRA law is in flux. |
| **Device / BYOD / return of property** | No deduction below minimum wage or overtime, even for negligence (F22–F25). No salary deduction for exempt staff (F26–F27). Personal-account access raises SCA risk (F32). *Van Buren* narrows CFAA (F31). | **No deduction purpose covers lost or unreturned property** (IN16). Fines are barred (IN19). Equipment purchases are capped (IN16). Conversion offers treble damages (IN26). Computer trespass covers phones (IN25). | Deduction lawful only if noticed in writing at hire or 7 days before a change (SC12–SC13). Treble-damages exposure (SC16). Computer-crime civil claim needs a conviction (SC30). | **High.** Final-paycheck setoffs for devices are the classic wage-claim trigger. |
| **Clawback (training, bonus, sign-on)** | Floor: FLSA free-and-clear (F22). Training loan upheld where the final week stayed at minimum wage (F28). FTC targets noncompete-linked "fees or penalties" (F61). Rule 10D-1 doesn't apply to private firms (F29). | Training reimbursement is a permitted purpose only by a revocable written assignment, and not for incentive-funded training (IN16). Physicians: post-July 2025 repayment tied to leaving can be a void noncompete (IN28). Bonus-as-wage test (IN14). | Commissions are wages, and contractually owed bonuses were recovered under the Act and trebled where withheld without a bona fide reason (SC11, SC19). Private agreements can't override the Act (SC17). | **High.** Revocability (IN) and notice (SC) undercut payroll recovery. Collect by a separate repayment agreement instead. |
| **Arbitration / class waiver** | Class waivers enforceable (F35). EFAA can take the whole case to court (F40–F47). Transportation-worker exemption widened (F38). Court must stay (F36). | State act covers employment (IN21). Case law unverified (IN22). | FAA governs interstate employment (SC24). SC Act needs an opt-in and page-1 notice and can't be a condition of employment (SC22–SC23). Opt-out-by-silence failed (SC25). One-sided terms won't be severed (SC26). Outrageous-torts carve-out (SC27). | **Medium.** Formation (affirmative assent), EFAA whole-case exposure, and the §1 exemption for delivery or driver roles. |
| **Non-compete** (ticket 02) | No federal rule; case-by-case FTC enforcement (F59–F61). | Reasonable plus blue pencil only (IN34). Physician–hospital ban (IN28). Continued employment is consideration (IN6). | No rewriting (SC34). Mid-employment covenants need new consideration (SC33). | **Medium–high.** Overbreadth voids the whole clause in SC, and in IN if there's nothing to strike. |
| **Severance / release** (often pre-promised in offers) | OWBPA checklist for 40+ (F50–F54). No bar on EEOC charges (F51–F52). FLSA claims not privately releasable (F56–F57). NLRA limits on terms (F15, F19). | Pay conceded wages unconditionally (IN12). No release statute (IN20). | Same (SC15, SC29). Wage-claim release is doubtful under §41-10-100 (SC17, SC20). | **Medium.** The common fault is conditioning earned final pay on signing. |

---

## Facts that decide outcomes

### Employer side
- **Paper trail.** Was each clause signed, and when: at hire or mid-employment (IN6, SC33)? Is there a signed handbook disclaimer, and was the handbook issued after June 30, 2004 (SC1–SC2)?
- **Deductions.**
  - Indiana: is there a written, personally signed, revocable assignment, countersigned and delivered within 10 days, for a listed purpose (IN15–IN16)?
  - South Carolina: was the deduction noticed in writing at hire or 7 days before the change (SC12–SC13)? Does the employer have fewer than five employees (SC12)?
- **Classification.** Is the employee exempt or non-exempt (F26–F27)? Does the deduction or repayment take any workweek below minimum wage or overtime (F22–F25)?
- **Training funding.** Was the training paid for with economic-development incentive money? If so, Indiana bars the deduction (IN16).
- **Device ownership.** Who owns the device? What did the employee sign about access, wipe and return? Did access reach personal cloud or e-mail accounts (F32, IN25, SC30)?
- **Notices.** Does every confidentiality agreement or policy updated after May 11, 2016 include the DTSA notice (F10)?
- **Arbitration formation.** Was assent affirmative (a signature or click), or opt-out-by-silence (SC25)? Does the work touch interstate goods movement (F38)?
- **Severance programs.** How many people are in the program, and what are their ages? That decides 21 versus 45 days and the (H) disclosure (F50). Are the affected employees supervisors? NLRA protections don't cover supervisors (F15).
- **Industry.** Physician–hospital relationships in Indiana (IN28).

### Employee side
- **Promises at hire.** Any written or oral promise of duration, guaranteed pay or "permanent" work, and what the employee gave up in reliance (IN4–IN5, SC5–SC6).
- **How employment ended.** Fired or quit? In Indiana that decides which statute and which forum (IN13).
- **Bad faith in withholding.** It decides 2x in Indiana (IN11) and 3x in South Carolina (SC16, SC18–SC19).
- **Age 40+ and the release.** Does the release meet every OWBPA element (F50–F54)?
- **Sexual harassment or assault facts.** Are they plausibly pleaded, and when did the dispute arise (F42–F46)? The circuit matters: 2d, 6th and 9th say whole case; 4th and 7th are open.
- **Inventions.** Made before hire, on the employee's own time and equipment, outside the employer's business? With no state statute, these facts only shape how a court reads the contract (IN7, SC8).
- **Bonus terms.** Is the bonus discretionary or earned, and is the wording vague? Vague terms are read against the employer in SC (SC19); IN uses a time-worked versus company-success test (IN14).
- **Arbitration enrollment.** Did the employee ever affirmatively accept it (SC25)?

---

## Creative or non-obvious angles

| # | Angle (CREATIVE) | Side | Risk / enforceability |
|---|---|---|---|
| 1 | Replace payroll deductions for devices with a **return-or-invoice clause plus a civil conversion claim**. In Indiana, IC 34-24-3-1 allows up to 3x damages and fees when the IC 35-43 elements are proven (IN26). | Employer | Medium. It requires proof of the criminal-conversion elements by a preponderance. It avoids the revocable-assignment and fine problems (IN15–IN19). Not available in the same form in SC, where the civil remedy needs a conviction (SC30). |
| 2 | Draft training repayment as a **separate pro-rated loan or promissory note**, not a wage assignment, capped at actual cost and never set off below the FLSA floor (F28). | Employer | Medium. Indiana assignments are revocable "at any time" (IN15), so the note is the durable instrument. FTC scrutiny of noncompete-linked "fees or penalties" (F61) and the Indiana physician rule (IN28) limit it. |
| 3 | In South Carolina, put the at-will disclaimer and the arbitration notice **both in underlined caps on page 1 of the offer letter**, and state that the FAA governs. | Employer | Low. That §41-1-110's "other document" covers an offer letter is my reading, not a verified holding. The FAA statement avoids reliance on the SC Act opt-in, which can't be required (SC23). |
| 4 | Use the **DTSA notice by cross-reference** to one policy, rather than editing every agreement (F10). | Employer | Low. The statute expressly allows it. The policy must actually state the reporting procedure. |
| 5 | An employee whose case includes a plausible sexual-harassment claim can **pull the entire case into court** (F45–F46), possibly even mid-arbitration (F46). | Employee | Medium. Settled in the 2d, 6th and 9th Circuits (F45–F47), open in the 4th and 7th (F48–F49). The claim must survive the pleading test. |
| 6 | An employee can argue a severance release of **Payment of Wages Act claims** is void under §41-10-100 ("set aside by a private agreement") (SC17). | Employee | High (uncertain). No SC case was found (SC20). A release of a bona fide disputed claim may well be upheld, and pressing this could cost the severance. |
| 7 | An employee with **no state invention statute** to rely on can ask for a prior-inventions schedule and a California-style carve-out (own time, own equipment, unrelated to the business) in the offer letter. | Employee | Low legal risk; the obstacle is negotiating leverage. Without the carve-out, breadth is a question of contract interpretation (IN7, SC8, IN34). |
| 8 | An employer can treat **NLRA confidentiality limits as live** despite GC 25-05, and add a §7 savings clause now, with a plan to revisit if *McLaren* is overruled (F19–F21). | Employer | Low. The Board still applies *McLaren* (F19), and the GC's push to overrule it (F20) isn't law yet. |
| 9 | An employer with delivery or driver roles should add a **state-law arbitration fallback** in case the FAA §1 exemption applies after *Flowers Foods* (F38). In Indiana the state act covers employment (IN21). In SC, the SC Act opt-in can't be a condition of employment (SC23). | Employer | Medium in SC, where the fallback may fail if it is mandatory. Lower in IN. |

---

## Open questions

1. Indiana appellate law on employment arbitration, class waivers and unconscionability (IN22). Not verified this pass.
2. Whether Indiana or South Carolina courts enforce a negotiated release of wage-statute claims (IN20, SC20), and whether a training-cost clawback can come out of final pay in either state.
3. Any 7th Circuit or 4th Circuit (or N.D./S.D. Ind., D.S.C.) EFAA decision on whole-case scope and the pleading standard (F48–F49). (*Diaz-Roa* (F47) was confirmed from the slip opinion on 2026-10-20.)
4. Whether the NLRB overrules *McLaren Macomb* or *Stericycle* in *Valley Radiology*, *Honeywell* or the severed *Beatrice Loving Heart* issue (F20–F21). Re-check before relying on F15–F21.
5. Pending South Carolina non-compete bills, and SC ratifications after Aug. 26, 2026 (SC32).
6. Indiana 2025–26 at-will decisions: not searched. The substance of P.L.67-2025 (minimum-wage definitions) (IN32).
7. Whether HEA 1004 (2025) also touched non-competes (IN28 note).
8. Whether §41-1-110's disclaimer rule reaches offer letters as an "other document" (angle 3).
9. Whether a 4th Circuit holding (not dicta) requires court or DOL approval of FLSA settlements (F57).
10. The holdings of *Herremans v. Carrera Designs* (7th Cir. 1998) and *Kopka, Landau & Pinkus v. Hansen* (Ind. Ct. App. 2007). Both exist, but their text was blocked, so neither is relied on here.

---

## Verification note

- **Depth: deep.**
  - Research ran as four parallel passes: federal IP, wages and devices; federal arbitration and releases; Indiana; South Carolina.
  - Each pass opened the primary source for every claim it marked verified.
  - I then re-opened and checked these myself: S.C. Code §15-48-10, *Bruce* (6th Cir.), *Flowers Foods* and *Jules* (preliminary prints), *Lampo* and *Hess* (sccourts.org PDFs), *Med-1* and *Heraeus* (FindLaw opinion text).
- **Sources used.**
  - Federal statutes and regulations: read on the LII mirror (law.cornell.edu), because uscode.house.gov deep links returned "not found" and ecfr.gov HTML was bot-blocked. EEOC regulations were read on the official eCFR API (current to 2026-10-16).
  - Indiana: the official 2026 Code files on iga.in.gov.
  - South Carolina: scstatehouse.gov code pages and sccourts.org opinions.
- **Cases verified only through later opinions** (each says so in place): *Ludwick* and *Small* (SC2–SC3), *Rice* (SC18), *Heder* (F28).
- **Tool limits.**
  - The shared web-search budget ran out partway through every pass.
  - CourtListener throttled and later showed a CAPTCHA, and Justia and Google Scholar blocked requests. No one tried to get around them.
  - Items left unchecked because of these limits are marked UNVERIFIED or listed under Open questions.
- **Removed as unconfirmable or wrong.**
  - "Doe v. TCSC, LLC" (not found).
  - A "2023 *Partain*" rejection of the outrageous-torts exception (wrong; see SC27).
  - *Martin v. Spring Break '83* (5th Cir.), recalled from memory and never opened.
  - A Sept. 2026 GC brief in "Atlassian" (secondary only).
  - A DOL training-repayment opinion letter (secondary only).
  - A claimed 7th Circuit EFAA ruling (none found).
- **Lead corrections** (prior research or the ticket brief):
  - The physician non-compete change is SEA 475 / P.L.207-2025, not HEA 1004.
  - The Indiana computer-trespass statute is IC 35-43-2-3, not the repealed IC 35-43-1-4.
  - The SC mid-employment consideration rule is *Poole*, not *Stonhard*.
  - §15-48-10(b)(2) says "provides," not "specifically provides."
- **Other conflicts:** the *McLaren* citation (F15), *Jarboe*'s year (IN5), and outdated statutory text quoted in *Steele* (IN11) and *Orr* (IN23).
- **Counts.** There are 129 numbered claims: F1–F61, IN1–IN34 and SC1–SC34.
  - **Verified: 124.**
  - **Unverified: 5** (F47, F49, IN9, IN22, SC20).
  - Nine of the 124 verified claims carry a sub-point marked UNVERIFIED. It is usually a reporter cite or a side detail: F7, F18, F28, F31, F57, F61, IN20, SC27 and SC32.
- No paid services were used. Quotes are under 15 words. Not legal advice.

---

## Sources

All accessed 2026-10-20.

| Citation | URL | Type | Verified |
|---|---|---|---|
| 42 U.S.C. §2000e-2 | https://www.law.cornell.edu/uscode/text/42/2000e-2 | Statute | Y |
| 42 U.S.C. §2000e-3 | https://www.law.cornell.edu/uscode/text/42/2000e-3 | Statute | Y |
| 17 U.S.C. §101 | https://www.law.cornell.edu/uscode/text/17/101 | Statute | Y |
| 17 U.S.C. §201 | https://www.law.cornell.edu/uscode/text/17/201 | Statute | Y |
| 17 U.S.C. §204 | https://www.law.cornell.edu/uscode/text/17/204 | Statute | Y |
| 35 U.S.C. §261 | https://www.law.cornell.edu/uscode/text/35/261 | Statute | Y |
| *Stanford v. Roche*, 563 U.S. 776 (2011) | https://www.law.cornell.edu/supct/html/09-1159.ZO.html | Case | Y |
| *CCNV v. Reid*, 490 U.S. 730 (1989) | https://www.law.cornell.edu/supremecourt/text/490/730 | Case | Y |
| 18 U.S.C. §1833 | https://www.law.cornell.edu/uscode/text/18/1833 | Statute | Y |
| 42 U.S.C. §§19402–19404 | https://www.law.cornell.edu/uscode/text/42/19403 | Statute | Y |
| 17 C.F.R. §240.21F-17 | https://www.law.cornell.edu/cfr/text/17/240.21F-17 | Regulation | Y |
| *McLaren Macomb*, 372 NLRB No. 58 | https://www.nlrb.gov/news-outreach/news-story/board-rules-that-employers-may-not-offer-severance-agreements-requiring | Agency decision | Y |
| *Stericycle*, 372 NLRB No. 113 | https://www.nlrb.gov/cases-decisions/weekly-summaries-decisions/summary-of-nlrb-decisions-for-week-of-july-31-august-4-0 | Agency decision | Y |
| NLRB GC 25-05 | https://www.nlrb.gov/news-outreach/news-story/gc-25-05-rescission-of-certain-general-counsel-memoranda | Agency guidance | Y |
| NLRB quorum restored | https://www.nlrb.gov/news-outreach/news-story/james-murphy-and-scott-mayer-sworn-in-as-board-members-0 | Agency | Y |
| *Prime Communications*, 374 NLRB No. 88 | https://www.nlrb.gov/cases-decisions/weekly-summaries-decisions/summary-of-nlrb-decisions-for-week-of-april-6-10-2026 | Agency decision | Y |
| NLRB GC 26-04 | https://apps.nlrb.gov/link/document.aspx/09031d4584351740 | Agency guidance | Y |
| *Beatrice Loving Heart*, 375 NLRB No. 56 | https://www.nlrb.gov/cases-decisions/weekly-summaries-decisions/summary-of-nlrb-decisions-for-week-of-september-28-1 | Agency decision | Y |
| 29 C.F.R. §531.35 | https://www.law.cornell.edu/cfr/text/29/531.35 | Regulation | Y |
| 29 C.F.R. §531.36 | https://www.law.cornell.edu/cfr/text/29/531.36 | Regulation | Y |
| 29 C.F.R. §531.3 | https://www.law.cornell.edu/cfr/text/29/531.3 | Regulation | Y |
| DOL WHD Fact Sheet #16 | https://www.dol.gov/agencies/whd/fact-sheets/16-flsa-wage-deductions | Agency guidance | Y |
| 29 C.F.R. §541.602 | https://www.law.cornell.edu/cfr/text/29/541.602 | Regulation | Y |
| 29 C.F.R. §541.603 | https://www.law.cornell.edu/cfr/text/29/541.603 | Regulation | Y |
| *Gordon v. City of Oakland*, 627 F.3d 1092 (9th Cir. 2010) | https://caselaw.findlaw.com/us-9th-circuit/1545305.html | Case | Y |
| 17 C.F.R. §240.10D-1 | https://www.law.cornell.edu/cfr/text/17/240.10D-1 | Regulation | Y |
| 18 U.S.C. §1030 | https://www.law.cornell.edu/uscode/text/18/1030 | Statute | Y |
| *Van Buren v. United States*, 593 U.S. 374 (2021) | https://www.supremecourt.gov/opinions/20pdf/19-783_k53l.pdf | Case | Y |
| 18 U.S.C. §§2701, 2707 | https://www.law.cornell.edu/uscode/text/18/2701 | Statute | Y |
| 9 U.S.C. §§1, 2 | https://www.law.cornell.edu/uscode/text/9/2 | Statute | Y |
| 9 U.S.C. §§401–402 (EFAA) | https://www.law.cornell.edu/uscode/text/9/402 | Statute | Y |
| *Epic Systems v. Lewis*, 584 U.S. 497 | https://www.law.cornell.edu/supremecourt/text/16-285 | Case | Y |
| *Southwest Airlines v. Saxon*, 596 U.S. 450 | https://www.law.cornell.edu/supremecourt/text/21-309 | Case | Y |
| *Bissonnette v. LePage Bakeries*, 601 U.S. 246 | https://www.law.cornell.edu/supremecourt/text/23-51 | Case | Y |
| *Smith v. Spizzirri*, 601 U.S. 472 | https://www.law.cornell.edu/supremecourt/text/22-1218 | Case | Y |
| *Morgan v. Sundance*, 596 U.S. 411 | https://www.law.cornell.edu/supremecourt/text/21-328 | Case | Y |
| *Flowers Foods v. Brock*, 608 U.S. 380 (2026) | https://www.supremecourt.gov/opinions/25pdf/608us2r37_i425.pdf | Case | Y |
| *Jules v. Andre Balazs Props.*, 608 U.S. 200 (2026) | https://www.supremecourt.gov/opinions/25pdf/608us1r31_8759.pdf | Case | Y |
| *Olivieri v. Stifel* (2d Cir. 2024) | https://govinfo.gov/content/pkg/USCOURTS-ca2-23-00658/pdf/USCOURTS-ca2-23-00658-0.pdf | Case | Y |
| *Cornelius v. CVS* (3d Cir. 2025) | https://www.govinfo.gov/content/pkg/USCOURTS-ca3-23-02961/pdf/USCOURTS-ca3-23-02961-0.pdf | Case | Y |
| *Memmer v. United Wholesale Mortg.* (6th Cir. 2025) | https://www.govinfo.gov/content/pkg/USCOURTS-ca6-24-01144/pdf/USCOURTS-ca6-24-01144-0.pdf | Case | Y |
| *Bruce v. Adams & Reese* (6th Cir. 2026) | https://www.opn.ca6.uscourts.gov/opinions.pdf/26a0054p-06.pdf | Case | Y |
| *Ding v. Structure Therapeutics* (9th Cir. 2026) | https://cdn.ca9.uscourts.gov/datastore/opinions/2026/08/19/25-1532.pdf | Case | Y |
| *Diaz-Roa v. Hermes Law* (2d Cir. 2026) | https://cases.justia.com/federal/appellate-courts/ca2/24-3223/24-3223-2026-09-30.pdf | Case (slip op., Justia copy) | Y (2026-10-20) |
| *Ralphs Grocery Co.*, 375 NLRB No. 25 (2026) | https://www.nlrb.gov/cases-decisions/weekly-summaries-decisions/summary-of-nlrb-decisions-for-week-of-august-10-14-2026 | Agency decision (summary) | Y (2026-10-20) |
| *Bopda v. Comcast* (4th Cir. 2024, unpub.) | https://www.govinfo.gov/content/pkg/USCOURTS-ca4-23-02148/pdf/USCOURTS-ca4-23-02148-0.pdf | Case | Y |
| 29 U.S.C. §626 (OWBPA) | https://www.law.cornell.edu/uscode/text/29/626 | Statute | Y |
| 29 C.F.R. §1625.22 | https://www.ecfr.gov/api/versioner/v1/full/2026-10-16/title-29.xml?part=1625&section=1625.22 | Regulation | Y |
| 29 C.F.R. §1625.23 | https://www.ecfr.gov/api/versioner/v1/full/2026-10-16/title-29.xml?part=1625&section=1625.23 | Regulation | Y |
| *Oubre v. Entergy*, 522 U.S. 422 | https://www.law.cornell.edu/supremecourt/text/522/422 | Case | Y |
| EEOC severance-waiver Q&A (2009) | https://www.eeoc.gov/laws/guidance/qa-understanding-waivers-discrimination-claims-employee-severance-agreements | Agency guidance | Y |
| *Brooklyn Savings Bank v. O'Neil*, 324 U.S. 697 | https://www.law.cornell.edu/supremecourt/text/324/697 | Case | Y |
| *Lynn's Food Stores*, 679 F.2d 1350 | https://static.case.law/f2d/679/cases/1350-01.json | Case | Y |
| *Walton v. United Consumers Club*, 786 F.2d 303 | https://static.case.law/f2d/786/cases/0303-01.json | Case | Y |
| *Taylor v. Progress Energy*, 493 F.3d 454 | https://static.case.law/f3d/493/cases/0454-01.json | Case (dicta) | Y |
| EEOC Commission votes, Jan. 2026 | https://www.eeoc.gov/commission-votes-january-2026 | Agency | Y |
| FTC accedes to vacatur (Sept. 2025) | https://www.ftc.gov/news-events/news/press-releases/2025/09/federal-trade-commission-files-accede-vacatur-non-compete-clause-rule | Agency | Y |
| FTC Non-Compete Rule page | https://www.ftc.gov/legal-library/browse/rules/noncompete-rule | Agency | Y |
| 91 FR 6507 (rule removal) | https://www.federalregister.gov/api/v1/documents/2026-02866.json | Regulation (FR) | Y |
| 90 FR 43606 (Gateway) | https://www.federalregister.gov/documents/full_text/html/2025/09/10/2025-17416.html | Agency (FR) | Y |
| 91 FR 21497 (Rollins) | https://www.federalregister.gov/documents/full_text/html/2026/04/22/2026-07844.html | Agency (FR) | Y |
| *Orr v. Westminster Village North*, 689 N.E.2d 712 | https://caselaw.findlaw.com/court/in-supreme-court/1089282.html | Case | Y |
| *Frampton v. Central Ind. Gas*, 297 N.E.2d 425 | https://www.courtlistener.com/opinion/2031331/frampton-v-central-indiana-gas-company/ | Case | Y |
| *McClanahan v. Remington Freight Lines*, 517 N.E.2d 390 | https://www.courtlistener.com/opinion/2097690/mcclanahan-v-remington-freight-lines-inc/ | Case | Y |
| *Romack v. Public Service Co.*, 511 N.E.2d 1024 | https://www.courtlistener.com/opinion/2062078/romack-v-public-service-co-of-indiana/ | Case | Y |
| *Jarboe v. Landmark*, 644 N.E.2d 118 | https://www.courtlistener.com/opinion/2150024/jarboe-v-landmark-community-newspapers-of-indiana-inc/ | Case | Y |
| *Med-1 Solutions v. Taylor* (Ind. Ct. App. 2024) | https://caselaw.findlaw.com/court/in-court-of-appeals/116719877.html | Case | Y |
| Indiana Code 2026, Title 22 (IC 22-2-2, -5, -6, -8, -9, -20; 22-5-3; 22-5-9; 22-6-3) | https://iga.in.gov/ic/2026/Title_22.html | Statute | Y |
| Indiana Code 2026, Title 24 (IC 24-2-3) | https://iga.in.gov/ic/2026/Title_24.html | Statute | Y |
| Indiana Code 2026, Title 34 (IC 34-24-3-1; 34-57-2) | https://iga.in.gov/ic/2026/Title_34.html | Statute | Y |
| Indiana Code 2026, Title 35 (IC 35-43-2-3; 35-43-4-3) | https://iga.in.gov/ic/2026/Title_35.html | Statute | Y |
| SB 14 (2026) enrolled, P.L.104-2026 | https://iga.in.gov/pdf-documents/124/2026/senate/bills/SB0014/SB0014.05.ENRH.pdf | Session law | Y |
| SB 169 (2026) enrolled, P.L.115-2026 | https://iga.in.gov/pdf-documents/124/2026/senate/bills/SB0169/SB0169.04.ENRH.pdf | Session law | Y |
| SEA 475 (2025), P.L.207-2025 | https://iga.in.gov/legislative/2025/bills/senate/475/details | Session law | Y |
| SB 132 (2026), dead | https://iga.in.gov/legislative/2026/bills/senate/132/details | Bill record | Y |
| *St. Vincent Hosp. v. Steele*, 766 N.E.2d 699 | https://www.courtlistener.com/opinion/853188/st-vincent-hospital-health-care-center-inc-v-steele/ | Case | Y |
| *Highhouse v. Midwest Orthopedic*, 807 N.E.2d 737 | https://www.courtlistener.com/opinion/852921/highhouse-v-midwest-orthopedic-institute-pc/ | Case | Y |
| *Central Ind. Podiatry v. Krueger*, 882 N.E.2d 723 | https://www.courtlistener.com/opinion/852486/central-indiana-podiatry-pc-v-krueger/ | Case | Y |
| *Heraeus Medical v. Zimmer* (Ind. 2019) | https://caselaw.findlaw.com/court/in-supreme-court/2034943.html | Case | Y |
| S.C. Code Title 41 Ch. 1 (§§41-1-65, 41-1-110) | https://www.scstatehouse.gov/code/t41c001.php | Statute | Y |
| S.C. Code Title 41 Ch. 10 (Payment of Wages Act) | https://www.scstatehouse.gov/code/t41c010.php | Statute | Y |
| S.C. Code Title 39 Ch. 8 (Trade Secrets Act) | https://www.scstatehouse.gov/code/t39c008.php | Statute | Y |
| S.C. Code Title 15 Ch. 48 (Uniform Arbitration Act) | https://www.scstatehouse.gov/code/t15c048.php | Statute | Y |
| S.C. Code Title 16 Ch. 16 (Computer Crime Act) | https://www.scstatehouse.gov/code/t16c016.php | Statute | Y |
| SC 2025–26 ratification log | https://www.scstatehouse.gov/sess126_2025-2026/bills/rats.php | Legislative record | Y |
| *Stiles v. American General Life* (S.C. 1999) | https://www.sccourts.org/media/opinions/HTMLFiles/SC/24945.htm | Case | Y |
| *Barron v. Labor Finders* (S.C. 2011) | https://www.sccourts.org/media/opinions/HTMLFiles/SC/27018.htm | Case | Y |
| *Conner v. City of Forest Acres* (S.C. 2005) | https://www.sccourts.org/media/opinions/HTMLFiles/SC/25961.htm | Case | Y |
| *Prescott v. Farmers Tel. Coop.* (S.C. 1999) | https://www.sccourts.org/media/opinions/HTMLFiles/SC/24948.htm | Case | Y |
| *Mathis v. Brown & Brown* (S.C. 2010) | https://www.sccourts.org/media/opinions/HTMLFiles/SC/26851.htm | Case | Y |
| *Hess v. Morphis Pediatric Group* (S.C. Ct. App. 2025) | https://www.sccourts.org/media/opinions/HTMLFiles/COA/6115.pdf | Case | Y |
| SC LLR wage FAQ | https://llr.sc.gov/wage/faq.aspx | Agency guidance | Y |
| *Bennett v. ACS Primary Care* (S.C. Ct. App. 2024) | https://www.sccourts.org/media/opinions/HTMLFiles/COA/6089.pdf | Case | Y |
| *Lampo v. Amedisys Holding* (S.C. 2025) | https://www.sccourts.org/media/opinions/HTMLFiles/SC/28265.pdf | Case | Y |
| *Damico v. Lennar Carolinas* (S.C. 2022) | https://www.sccourts.org/media/opinions/HTMLFiles/SC/28114.pdf | Case | Y |
| *Aiken v. World Finance* (S.C. 2007) | https://www.sccourts.org/media/opinions/HTMLFiles/SC/26313.htm | Case | Y |
| *Partain v. Upstate Automotive* (S.C. 2010) | https://www.sccourts.org/media/opinions/HTMLFiles/SC/26768.htm | Case | Y |
| *Parsons v. John Wieland Homes* (S.C. 2016) | https://www.sccourts.org/media/opinions/HTMLFiles/SC/27655.pdf | Case | Y (partly) |
| *Poole v. Incentives Unlimited* (S.C. 2001) | https://www.sccourts.org/media/opinions/HTMLFiles/SC/25299.htm | Case | Y |
| *Stonhard v. Carolina Flooring* (S.C. 2005) | https://www.sccourts.org/media/opinions/HTMLFiles/SC/26047.htm | Case | Y |
| *Poynter Invs. v. Century Builders* (S.C. 2010) | https://www.sccourts.org/media/opinions/HTMLFiles/SC/26821.htm | Case | Y |

---

## Independent verification (2026-10-20)

An independent verifier re-opened every authority in this file at a primary source or an official mirror. The 2025–26 items were read by the verifier directly. Older authorities were read in three parallel passes (federal, Indiana, South Carolina), whose findings the verifier reviewed. Edits made in place are tagged "(Corrected 2026-10-20)" or "(added 2026-10-20)". The original "Verification note" counts above are superseded by these.

**No fabricated or mis-cited authority was found.** Every case, statute, regulation, session law and agency action exists, and the court, date, docket and citation match. The 2025–26 change list stands, with the qualifiers noted below.

### Counts (129 numbered claims)
- **Confirmed: 104.**
- **Corrected: 21:** F7, F13, F38, F42, F57; IN1, IN3, IN4, IN8, IN10, IN24, IN28, IN30, IN31; SC12, SC16, SC19, SC21, SC24, SC30, SC34.
- **Removed: 0.**
- **Unverified: 4:** F49 (district courts), IN9, IN22, SC20. F47 was upgraded to confirmed.
- **Sub-points upgraded:** the reporter cites in F7 (563 U.S. 776), F28 (627 F.3d 1092; *Heder* opened directly) and F31 (593 U.S. 374); F18 (Macy sworn in Aug. 17, 2026); SC27 (the third bloc in *Parsons*).

### 2025–26 items re-opened by the verifier
- ***Flowers Foods v. Brock*** — No. 24-935, 608 U.S. 380 (May 28, 2026), unanimous (Gorsuch). Supreme Court preliminary print. Confirmed. Qualifier added to F38.
- ***Jules v. Andre Balazs Props.*** — No. 25-83, 608 U.S. 200 (May 14, 2026), unanimous (Sotomayor). Preliminary print. Confirmed as stated.
- ***Cornelius*** — 3d Cir. No. 23-2961, Apr. 2, 2025, precedential. govinfo. Confirmed.
- ***Memmer*** — 6th Cir. No. 24-1144, Apr. 18, 2025; reversed, Thapar dissenting. govinfo. Confirmed.
- ***Bruce*** — 6th Cir. No. 25-5210, Feb. 25, 2026, 168 F.4th 367 (as *Ding* cites it), Thapar dissenting. ca6 site. Confirmed.
- ***Ding*** — 9th Cir. No. 25-1532, Aug. 19, 2026, Rawlinson dissenting. ca9 site. Confirmed.
- ***Diaz-Roa*** — 2d Cir. No. 24-3223-cv, Sept. 30, 2026. Slip opinion (Justia copy). Upgraded to confirmed.
- ***Prime Communications*** — 374 NLRB No. 88, Apr. 7, 2026. NLRB weekly summary. Confirmed. The summary's "No. 48" for *McLaren* is a typo; GC 26-04 prints No. 58.
- **NLRB memos.** GC 25-05 (Feb. 14, 2025, Acting GC Cowen) rescinds GC 23-02, 23-05, 23-08 and 25-01, confirmed. GC 26-04 (Aug. 26, 2026, GC Carey) was read in full; it names *Valley Radiology* and *Honeywell*, confirmed.
- **NLRB quorum and later decisions.** The quorum release of Jan. 7, 2026 is confirmed. *Beatrice Loving Heart* (375 NLRB No. 56) is confirmed. The Oct. 5–9 summary was checked, and *Ralphs Grocery* (375 NLRB No. 25) was added to F21.
- **EEOC.** The Jan. 2026 vote page shows the harassment-guidance rescission on Jan. 22, 2026, 2–1 (Kotagal dissenting). The roster is Lucas (Chair), Kotagal and Panuccio. Confirmed.
- **FTC.** The Sept. 5, 2025 press release (3–1) is confirmed. The rule page says "not in effect." 91 FR 6507 (Feb. 12, 2026) removes 16 C.F.R. Part 910. 90 FR 43606 (*Gateway*) and 91 FR 21497 (*Rollins*) are confirmed via the FR API.
- **IC 22-5-9** — P.L.106-2026 SEC.16 = SEA 76 §16, effective July 1, 2026. Official code file and enrolled act. Confirmed; the scope is corrected in IN30.
- **IC 22-2-20** — P.L.109-2025, expires July 1, 2029. Confirmed; the meeting count is corrected in IN31.
- ***Lampo*** — Op. No. 28265 (S.C. Mar. 5, 2025), 3–2. sccourts.org PDF. Confirmed. Disposition and vote line added.
- ***Hess*** — Op. No. 6115 (S.C. Ct. App. July 9, 2025). sccourts.org PDF. Confirmed; SC19 corrected.

### Corrections (what changed)
- **F7:** the "agree to assign"/"hereby assign" contrast is in *Stanford*'s background and the dissent, not in fn. 2. Fn. 2 says only that the Court had no occasion to rule on it.
- **F13:** the operative Speak Out Act rule is §19403(a); §19402 is definitions.
- **F38:** *Flowers* rejected only the cross-state-lines rule. It reserved the independent-business and title-to-goods questions.
- **F42:** *Olivieri*'s test turns on when the claim accrued, not on the agreement's date.
- **F57:** the "wholly private settlements" quote is from *Walton*, not *Lynn's*. *Taylor* (4th Cir.) is an FMLA case.
- **IN1:** *Orr* didn't hold that handbooks can never be unilateral contracts, only that this one wasn't.
- **IN3:** the *McClanahan* quote reads "would be personally liable."
- **IN4:** *Romack* reversed summary judgment by adopting a Court of Appeals dissent. It made no final finding.
- **IN8:** the UTSA displaces only *conflicting* law. The 2x cap applies to the subsection (a) award.
- **IN10:** the 10-business-day rule runs back from the payment date.
- **IN24:** the infraction is in -1(a), the company liability in -2, and the immunity in -1(b).
- **IN28:** the ban covers only agreements "originally entered into" after July 1, 2025. The repayment rule applies only if repayment is based "solely or primarily" on new practice. The non-solicit exception covers current employees only.
- **IN30:** IC 22-5-9 also reaches continued employment after July 1, 2026, not just new hires. The cure process and penalty tiers were added.
- **IN31:** the protection covers one attendance conference *and* one case-conference meeting per calendar year.
- **SC12:** the small-employer exemption covers all of §41-10-30, plus domestic employers.
- **SC16:** the statute doesn't make trebling discretionary; *Rice* does.
- **SC19:** *Hess* didn't expressly hold that bonuses are "wages." Page cites were fixed, and the 7-day-notice and prejudgment-interest holdings were added.
- **SC21:** only the LLR FAQ states the rules; the other page doesn't.
- **SC24:** *Bennett* isn't an employment case, and the FAA default yields to the parties' contrary choice.
- **SC30:** the statute's text says "digital cellular telephones."
- **SC34:** *Poynter* never ruled on step-down tiers. *Stonhard*'s rule is narrower than stated.
- **Header and downstream text:**
  - The SC code pages show no "current through" date.
  - Summary, checklist, facts, angle 5, open question 3 and the Sources table were updated for *Diaz-Roa* and the reporter cites.
  - The checklist clawback cell was softened to match SC19.

### Source quality and conflicts
- **Rules that rest on secondary sources only:** none. The only secondary item, F47, now rests on the slip opinion.
- **Cases verified only through a later opinion** (unchanged): *Ludwick*, *Small* and *Rice*. Since the first pass, *Small* has been cited with its reporter in *Conner*.
- **Non-official mirrors used:**
  - *Diaz-Roa*: Justia copy of the slip opinion.
  - Indiana cases and *Heder*: Caselaw Access Project.
  - *Med-1* and *Heraeus*: FindLaw.
  - Federal statutes: LII.
- **Conflicts:**
  - *McLaren* is printed as "No. 48" in the Apr. 2026 summary but "No. 58" in GC 26-04. No. 58 is correct.
  - The SC ratification-sheet count differs between passes (19 vs. 21). The substantive result is the same.
  - *Steele*'s pre-2015 statutory text (already flagged at IN11).

### Not checked or still open
- **Reporter cites:**
  - *Bruce*'s 168 F.4th 367 was taken from *Ding*, not the reporter.
  - S.E.2d cites for *Barron*, *Lampo* and *Poynter*, and the N.E.3d cite for *Heraeus*.
  - Pin pages in *Epic* and *Brooklyn Savings*.
- **Indiana:**
  - Whether *Med-1* is published.
  - The SB 76 and SB 132 bill-status pages (a JavaScript app; SB 132's "dead" status is inferred).
  - What P.L.111-2026 (IC 35-43-2-3) and P.L.142-2026 (IC 34-24-3-1) changed.
  - The substance of P.L.67-2025.
- **Federal agencies:**
  - When Murphy became NLRB Chairman.
  - EEOC votes in months other than Jan. 2026.
  - SEC Rule 21F-17 enforcement in 2025–26.
- **Never re-run:** the keyword-scan negative findings (IN7, IN27, SC8, SC31) and the district-court EFAA search (F49). A web search found no 7th Circuit or N.D./S.D. Ind. or D.S.C. whole-case EFAA decision.
- **Access limits:** CourtListener rate-limited and Justia blocked some requests. No CAPTCHA was attempted.

### IC official check (2026 code download, 2026-10-20)
Checked against the official IGA 2026 Indiana Code text (`sources/indiana-code/IC-title-NN.txt`; all-title scans from the 2026 HTML download). URL form: https://iga.in.gov/laws/2026/ic/titles/NN.
- **IC 22-2-5-1** (IN10): confirmed. Semimonthly/biweekly, 10-business-day lag, void contracts, quitter paid next regular payday.
- **IC 22-2-5-2** (IN11): confirmed. Mandatory fees and costs; 2x only absent good faith (P.L.193-2015).
- **IC 22-2-6-1** (IN15): confirmed.
- **IC 22-2-6-2** (IN15–IN17): confirmed, with additions. The 2026 code prints two versions (P.L.104-2026 SEC.22, with (b)(19) and (f); P.L.115-2026 SEC.14, with updated (b)(10) and (d)(2) cross-references). **No listed purpose covers loss of, damage to, or failure to return employer property; (b)(15) covers only the *purchase* of necessary equipment or tools at vendor cost**, capped by (d), with (e) barring OSHA protective-equipment charges. Added from the text: (b)(6) employer-offered merchandise sold at the employee's written request; (b)(7) a written-instrument employer loan; (c) interest cap of bank prime plus 4% on loans and advances.
- **IC 22-2-6-4** (IN18): confirmed; also the decimal-point exception in (c)(2).
- **IC 22-2-8-1** (IN19): confirmed.
- **IC 22-2-9-2, -3** (IN12): confirmed.
- **IC 22-2-2-3, -4(c), -14.1** (IN32): confirmed. P.L.67-2025 SEC.2 is in -3's history; -4 was last amended by P.L.147-2020; -14.1 added by P.L.15-2026. Added: -4(c) applies to employers with at least 2 employees in a workweek.
- **IC 22-2-20-1 to -9** (IN31): confirmed. Added: employee documentation duty (-7) and reasonable effort to schedule electronically (-8).
- **IC 22-5-3-1, -2** (IN24): confirmed as corrected.
- **IC 22-5-9-1 to -12** (IN30): confirmed. Added: "knowingly or intentionally"; 3-year lookback (-8(a)); anti-retaliation for cooperating with the AG (-10).
- **IC 22-6-3-1** (IN23): confirmed (last amended P.L.113-2014).
- **IN33** (no 2025–26 public law in 22-2-5, 22-2-9, 22-6-3, 22-5-3, 24-2-3 histories): confirmed for the sections listed above.
- **IC 24-2-3-1(c), -2, -4(c)** (IN8): confirmed. The displacement clause is limited to conflicting law on trade-secret misappropriation.
- **IC 25-22.5-5.5-1.1 to -2.3** (IN28): confirmed (P.L.207-2025). Noted, not carried (ticket 02 scope): -2.5 bans primary-care physician noncompetes entered on or after July 1, 2023.
- **IC 34-57-2-1, -3** (IN21): confirmed; -1 amended by P.L.115-2026 SEC.82; consumer leases, sales and loans exempt.
- **IC 34-24-3-1** (IN26): confirmed (up to 3x actual damages, costs, fees, collection costs; text does not mention a conviction). What P.L.142-2026 SEC.5 changed: not determinable from the code text.
- **IC 35-43-2-3** (IN25): confirmed, including the cellular-device language. IC 35-43-1-4 repeal by P.L.158-2013 confirmed. What P.L.111-2026 SEC.6 changed: not determinable from the code text.
- **IC 35-43-4-3** (IN26): confirmed.
- **IN7 (no invention-assignment statute):** confirmed by re-scan of all 37 titles for "invention," "inventor" and "intellectual property" near "employ." Hits: IC 6-3-2-21.7 (patent income tax), IC 4-29.5-2-7 (gaming-compact definition), and a Title 21 higher-education foreign-student disclosure provision. None limits assignment.
- **Not re-run:** the IN20 waiver/release scan and the IN27 social-media, password and expense-reimbursement scans.
- **Corrected:** none. No IC claim in this file conflicts with the 2026 text.
