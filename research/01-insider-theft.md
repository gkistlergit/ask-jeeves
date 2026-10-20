# Insider theft of IT assets, data and trade secrets: Federal, Indiana, South Carolina (as of 2026-10-20)

Resolves ticket `.scratch/ask-jeeves/issues/01-insider-theft-law.md`. Planning research for the ask-jeeves skill. Not legal advice.

**Tags.** `[V]` = checked against the opened primary text. `[UNVERIFIED: why]` = not confirmed. `[INFERENCE]` = my reasoning from verified sources, not a holding. `CHANGED 2025–26` = a change in 2025 or 2026. All sources were accessed 2026-10-20. Quotes are under 15 words. "Slip op. pg. N" is the court's printed page.

## Summary (10 lines)

1. **Trade secrets.** All three systems use the same core test: secret information with independent value, protected by reasonable secrecy measures. The federal claim is the DTSA. Indiana has its UTSA (IC 24-2-3) and South Carolina has the SCTSA (§39-8). Each has a 3-year discovery-rule limitations period and caps exemplary damages at 2x. `[V]`
2. **DTSA notice.** An employer that leaves the §1833(b) immunity notice out of an employee or contractor agreement cannot get exemplary damages or fees against that worker. This applies to agreements entered or updated after 2016-05-11. `[V]`
3. **Computer-access law.** The CFAA turns on code-based "gates," not use policies (*Van Buren*). The 4th Circuit (SC) already read it narrowly (*WEC*). The 7th Circuit's agency theory (*Citrin*) is in doubt `[INFERENCE]`. Indiana and SC computer-crime statutes are broader, and SC's reaches "unauthorized purpose" use. `[V]`
4. **Displacement.** Indiana's UTSA displaces all conflicting state law on trade-secret misappropriation except contract and criminal law. That wipes out idea-misappropriation and CVRA-conversion claims over information (*HDNet*), but not civil RICO (*AGS Capital*). SC displaces tort and restitution claims but keeps contract remedies. The DTSA preempts nothing, except that the §1833(b) whistleblower immunity applies under state trade-secret law too. `[V]`
5. **Injunctions.** A DTSA injunction cannot stop someone from taking a job. An Indiana UTSA injunction can, on "harvesting" facts (*Ackerman*). A federal district court reads Indiana law to limit inevitable disclosure to bad-faith taking (*Dearborn*), and the Court of Appeals applied the same narrow approach (*Med-1*). No Indiana Supreme Court case states that limit. `[V]`/`[INFERENCE]`
6. **Treble damages.** Indiana's CVRA (up to 3x plus fees) covers theft and conversion of tangible devices. Indiana civil RICO (mandatory 3x) survives UTSA displacement. SCUTPA allows 3x for willful violations, but its fit with employee disputes is UNVERIFIED. `[V]`/`[UNVERIFIED]`
7. **Criminal.** Federal: EEA §1832 (10 years) and §1831 (15 years). Indiana: IC 35-43-1-7, taking trade-secret data from a computer (Level 6 felony). SC: §39-8-90 (10 years / $100k), plus the Computer Crime Act. `[V]`
8. **CHANGED 2025–26.** (a) *NRA Group v. Durenleau* (3d Cir. 2025; amended opinion Oct. 7, 2025; cert. denied Mar. 30, 2026, No. 25-1033): breaking a computer-use policy without code-based hacking is not a CFAA violation, and passwords with no independent economic value of their own are not trade secrets. Persuasive only in IN and SC. (b) Indiana P.L.111-2026 (SEA 119, signed 2026-03-05, effective 2026-07-01) added cell phones to the "computer network" definition in computer trespass (IC 35-43-2-3). (c) Minor Indiana 2025–26 edits to the CVRA predicate list, the theft statute and the RICO predicate list (not insider-theft relevant). `[V]`
9. **No change found.** No 2025–26 change to the DTSA, CFAA or EEA text (govinfo 2024 edition plus LII notes), to IC 24-2-3, or to the SC chapters (online Code is current through the 2025 session). The SC 2026 session was not checked. `[UNVERIFIED]` for SC 2026.
10. **What decides outcomes.** Identifying the secret with particularity, proof of secrecy measures, forensic proof of taking, code-based access limits, signed agreements with the DTSA notice, and the new employer's knowledge.

---

## Federal

### F1. Defend Trade Secrets Act (civil), 18 U.S.C. §1836, §1839
- **Who may sue.** The "owner of a trade secret that is misappropriated" may sue if the secret relates to a product or service "used in, or intended for use in," interstate or foreign commerce. §1836(b)(1). `[V]` Federal courts have original jurisdiction, §1836(c). The 2016 law struck the old "exclusive" wording `[V]`, so state courts likely share jurisdiction `[INFERENCE]`.
- **What counts as a trade secret, §1839(3).** All forms of business, technical and other information, including "programs, or codes," "whether tangible or intangible." Two requirements:
  - (A) the owner took "reasonable measures to keep such information secret"; and
  - (B) the information has independent economic value from not being generally known or readily ascertainable through proper means "by another person who can obtain economic value." `[V]`
- **Misappropriation, §1839(5).** Either (A) acquisition by someone who knows or has reason to know it came by improper means, or (B) disclosure or use without consent. Theory (B) applies where the person:
  - used improper means;
  - knew or had reason to know the secret was acquired under a duty to keep it secret or limit its use (the usual employee theory); or
  - learned it by accident or mistake before a material change of position. `[V]`
- **Improper means, §1839(6).** Includes theft, bribery, misrepresentation, breach or inducement of a breach of a duty to maintain secrecy, and espionage. It *excludes* "reverse engineering, independent derivation, or any other lawful means." `[V]`
- **Remedies, §1836(b)(3)** `[V]`:
  - **Injunction** against "actual or threatened misappropriation." It may **not** (I) "prevent a person from entering into an employment relationship." Conditions on employment must rest on "evidence of threatened misappropriation and not merely on the information the person knows." It also may not (II) conflict with a state law prohibiting restraints on a lawful profession, trade or business.
  - **Affirmative acts** to protect the secret.
  - **Royalty injunction** in "exceptional circumstances."
  - **Damages.** Actual loss plus unjust enrichment not counted in actual loss; *or* a reasonable royalty.
  - **Exemplary damages** up to **2x** for willful and malicious misappropriation.
  - **Attorney's fees** to the prevailing party for a bad-faith claim, a bad-faith motion to terminate an injunction (made or opposed), or willful and malicious misappropriation.
- **Ex parte civil seizure, §1836(b)(2).** Allowed "only in extraordinary circumstances." The applicant must show eight findings `[V]`, including:
  - a Rule 65 order would be inadequate because the target would evade it;
  - immediate irreparable injury;
  - likely success;
  - actual possession by the target;
  - the target would destroy or hide the matter if given notice; and
  - no publicity by the applicant.

  The order requires a hearing within 7 days and security, and a federal officer executes it. A wrongful-seizure claim is available. `[V]`
- **Limitations, §1836(d).** 3 years from actual or constructive discovery. A continuing misappropriation is "a single claim." `[V]`
- **Effective date.** The 2016 amendments apply to misappropriation where "any act occurs on or after" 2016-05-11. Pub. L. 114-153 §2(e), note to §1833. `[V]`
- **No preemption, §1838.** Except §1833(b), the chapter does not "preempt or displace any other remedies," civil or criminal, federal or state. `[V]` So the DTSA stacks with state UTSA claims; state displacement rules still govern the state-law claims (see IN4, SC4). `[INFERENCE]`
- **Extraterritorial reach, §1837.** The chapter applies abroad if the offender is a US citizen, permanent resident or US organization, or if "an act in furtherance" occurred in the US. `[V]`
- **Status 2025–26.** Section text and notes in the govinfo 2024 edition and on LII show no amendment after 2016. `[V]` The OLRC site (uscode.house.gov) was in a "temporary format" and its section pages returned "Page Not Found," so OLRC's current text through Pub. L. 119-121 could not be checked. `[UNVERIFIED: OLRC unreachable]`

### F2. DTSA whistleblower immunity and the employer notice, 18 U.S.C. §1833(b)
- **Immunity, §1833(b)(1).** An individual is not criminally or civilly liable "under any Federal or State trade secret law" for disclosing a trade secret that is made either:
  - (A) in confidence to a federal, state or local government official, directly or indirectly, or to an attorney, "solely for the purpose of reporting or investigating a suspected violation of law"; or
  - (B) in a complaint or other filing in a lawsuit or proceeding, if filed under seal. `[V]`
- **Anti-retaliation suits, (b)(2).** The individual may disclose the secret to their own attorney and use it in court, if they file it under seal and disclose it only by court order. `[V]`
- **Notice duty, (b)(3)(A).** An employer "shall provide notice of the immunity" in "any contract or agreement with an employee" that governs use of trade secrets or other confidential information. `[V]`
  - **Cross-reference option, (B).** The employer complies by cross-referencing a policy document, given to the employee, that sets out its reporting policy for suspected violations of law. `[V]`
  - **Sanction, (C).** A non-compliant employer "may not be awarded exemplary damages or attorney fees" under §1836(b)(3)(C) or (D) "against an employee to whom notice was not provided." `[V]`
  - **Scope, (D).** Applies to contracts "entered into or updated after" 2016-05-11. `[V]`
- **"Employee," (b)(4).** Includes "any individual performing work as a contractor or consultant." `[V]`
- **Limit, (b)(5).** The immunity does not authorize, or limit liability for, otherwise unlawful acts "such as the unlawful access of material by unauthorized means." `[V]`
- **Practical consequences** `[INFERENCE]`:
  - Missing notice does not defeat liability or an injunction. It removes only the 2x exemplary damages and fees, and only against the un-noticed worker.
  - An "updated" agreement after 2016 triggers the duty, so old forms re-signed or amended need the notice.
  - The immunity covers *disclosure* to a lawyer or official. It does not cover *taking* data by hacking.
- **Related, SEC Rule 21F-17(a), 17 C.F.R. §240.21F-17.** "No person may take any action to impede" an individual from communicating with SEC staff about a possible securities violation, including by enforcing or threatening to enforce a confidentiality agreement. There is a carve-out for attorney-client material. `[V]` The rule's text reaches "any person," not only public companies, so any employer's confidentiality clause is exposed where the information concerns a possible securities violation. `[INFERENCE]`

### F3. Economic Espionage Act (criminal), 18 U.S.C. §§1831–1832
- **§1832, theft of trade secrets.** Requires:
  - intent to convert a trade secret related to a product or service used in or intended for use in interstate or foreign commerce;
  - to the economic benefit of anyone but the owner;
  - intending or knowing the offense will injure the owner; and
  - knowing theft or unauthorized appropriation, copying, downloading, uploading or transmitting, or receiving or possessing it knowing it was stolen. Attempt and conspiracy are covered.

  Penalties: individuals up to **10 years**; organizations fined the greater of **$5M or 3x the value** of the secret, including avoided R&D. `[V]`
- **§1831, economic espionage.** Same acts, intending or knowing the offense will benefit a foreign government, instrumentality or agent. Individuals face up to $5M and **15 years**; organizations the greater of $10M or 3x value. `[V]`
- **History, 2012.** The Theft of Trade Secrets Clarification Act, Pub. L. 112-236, replaced "included in a product that is produced for or placed in" commerce with "a product or service used in or intended for use in" commerce. `[V]` That followed *United States v. Aleynikov*, 676 F.3d 71 (2d Cir. 2012), which reversed an EEA conviction under the narrower old wording. `[V]` (The causal link is `[INFERENCE]` from timing and wording. The statute's notes do not state it.)
- **National Stolen Property Act, 18 U.S.C. §2314.** *Aleynikov* held that interstate transmission "of purely intangible property" is beyond the NSPA. A copied source-code file is not "goods." `[V]` §2314 itself (govinfo 2024 ed.) reaches "goods, wares, merchandise, securities or money" worth $5,000 or more. `[V]` Physical devices remain "goods" `[INFERENCE]`.

### F4. Computer Fraud and Abuse Act, 18 U.S.C. §1030
- **Main insider prongs** `[V]`:
  - (a)(2)(C): intentionally accessing a computer "without authorization or exceeds authorized access," and thereby obtaining information from any protected computer;
  - (a)(4): access with intent to defraud that furthers the fraud and obtains anything of value;
  - (a)(5)(A): knowingly transmitting a program, code or command that intentionally causes damage without authorization;
  - (a)(5)(B)–(C): unauthorized access that recklessly causes damage, or causes damage and loss.
- **Definitions** `[V]`:
  - "Exceeds authorized access," §1030(e)(6): access with authorization, then using it to obtain or alter information "the accesser is not entitled so to obtain or alter."
  - "Damage," (e)(8): any impairment to the integrity or availability of data, a program, a system or information.
  - "Loss," (e)(11): reasonable costs, including response, damage assessment and restoration, and lost revenue or consequential damages "because of interruption of service."
  - "Protected computer," (e)(2)(B): one used in or affecting interstate commerce.
- **Civil action, §1030(g).** Available to anyone who suffers damage or loss, for compensatory damages and injunctive or equitable relief. Requirements `[V]`:
  - the conduct must involve one of the factors in (c)(4)(A)(i)(I)–(V). The usual one is (I): loss aggregating at least **$5,000** in a 1-year period. Damages under (I) alone are "limited to economic damages."
  - **Limitations:** 2 years from the act or from discovery of the damage.
- ***Van Buren v. United States*, 593 U.S. 374 (2021)** (6–3, Barrett, J.):
  - **Holding.** A person exceeds authorized access when they access a computer with authorization but then obtain information in "particular areas of the computer—such as files, folders, or databases" that are off limits to them. Slip op. pg. 20; syllabus pg. 1. `[V]`
  - **Gates.** Liability under both clauses turns on "a gates-up-or-down inquiry." Slip op. pg. 13. `[V]`
  - **Footnote 8.** The Court did not decide whether the gates are "only" technological ("code-based") or also include limits in contracts or policies. Slip op. pg. 13 n.8. `[V]`
  - **Damage and loss.** These "focus on technological harms—such as the corruption of files." They are "ill fitted" to remedying misuse of information an employee may permissibly access. Slip op. pg. 15. `[V]`
  - **Use policies.** The Court rejected a reading that would make "every violation of a computer-use policy" a crime. Slip op. pg. 17. `[V]`
- **Fourth Circuit (SC): *WEC Carolina Energy Solutions LLC v. Miller*, 687 F.3d 199 (4th Cir. 2012).** The case arose between two South Carolina companies.
  - It "adopt[ed] a narrow reading" of "without authorization" and "exceeds authorized access." `[V]`
  - It rejected "any interpretation that grounds CFAA liability on a cessation-of-agency theory." `[V]`
  - Employees who downloaded confidential files to personal computers against policy, using access they had, "may have misappropriated information" but did not violate the CFAA. `[V]`
  - Their remedies lie in state law (conversion, tortious interference, conspiracy, trade secrets). `[V]`
- **Seventh Circuit (IN): *International Airport Centers, L.L.C. v. Citrin*, 440 F.3d 418 (7th Cir. 2006) (Posner, J.).** Two holdings `[V]`:
  - (1) Installing a secure-erasure program to wipe an employer laptop was a "transmission" under §1030(a)(5)(A).
  - (2) The employee's breach of the duty of loyalty "terminated his agency relationship" and with it his authorization.

  Holding (2) looks inconsistent with *Van Buren*'s gates reading, which does not turn on the user's purpose. `[INFERENCE]` Holding (1), deliberate destruction of data, still fits (a)(5)(A), whose "without authorization" modifies *damage*, not access. `[INFERENCE]` No 7th Circuit decision after *Van Buren* on this was found. `[UNVERIFIED: no search budget left; see Open questions]`
- **CHANGED 2025–26: *NRA Group, LLC v. Durenleau*, No. 24-1123 (3d Cir.)**
  - **Filed** 2025-08-26 (precedential; Hardiman, McKee, Ambro, JJ.; opinion by Ambro). On 2025-10-07 the court granted panel rehearing, vacated the August opinion and filed an amended opinion; the order says the changes "do not affect the disposition of the appeal." The same order denied rehearing en banc. `[V]` (order opened) A second en banc petition was denied 2025-11-10. `[V]` (SCOTUS docket 25-1033 and the cert petition)
  - **Supreme Court.** Justice Alito denied a stay application, No. 25A841, on 2026-01-28. `[V]` NRA Group then filed a certiorari petition, **No. 25-1033** (filed 2026-02-06; respondents waived a response). **Certiorari was denied 2026-03-30.** `[V]` (docket opened) The Third Circuit decision is final.
  - **Holdings** (August slip op. pg. 4, 23–24, 26–29; repeated without change in the amended opinion, cert. App. 6a, 27a–28a):
    - "absent evidence of code-based hacking," the CFAA does not support claims based on current employees' breach of workplace computer-use policies. `[V]`
    - Passwords that protect proprietary information "are not themselves trade secrets" under the DTSA or Pennsylvania law. The reasoning is that these passwords had no independent economic value and were not "the product of any special formula or algorithm"; the value lay in what they protected (slip op. pg. 4, 26–29). `[V]`
    - Employers should use contract, business-tort, fraud and other claims instead (slip op. pg. 24). `[V]`
  - **Facts.** A coworker logged in for a sick colleague with her permission and emailed a password spreadsheet. The employees had made internal harassment complaints; NRA sued "just weeks" after one resigned and the other was fired. `[V]` The court quoted *WEC* with approval. `[V]`
  - **Amended text.** Now read in the cert. petition appendix (Vol. I, App. 3a–39a, filed on the SCOTUS docket). The CFAA and trade-secret holdings are word-for-word the same. Per the petition, the amendment corrected a factual point about the timing of the CEO's email. `[V]` Reporter cites: the petition gives **154 F.4th 153** for the amended opinion and 153 F.4th 1333 for the earlier decision; Leagle gives 153 F.4th 1333 for the August opinion. `[UNVERIFIED: party filing and Leagle only; reporter not opened]`
  - **Weight.** Persuasive in the 4th and 7th Circuits, not binding. `[INFERENCE]`
- **DOJ charging policy, Justice Manual 9-48.000 (updated May 2022).** DOJ will not bring "exceeds authorized access" cases where authorization was conditioned by a contract or policy, except ones that entirely prohibit access to particular files or areas. It will not bring cases on automatic-withdrawal-of-authorization theories. Prosecutors must prove access to an off-limits area, "not merely" later misuse. `[V]` No 2025–26 revision appeared on the page. `[V]`

### F5. Other federal points
- **No federal civil conversion or "theft of data" claim was researched.** Physical devices are state-law conversion or replevin. `[INFERENCE]`
- **The FTC non-compete rule and NLRB memos** are restrictive-covenant topics. They are left to the covenant ticket and not verified here. `[UNVERIFIED: out of scope]`

---

## Indiana

### IN1. Indiana Uniform Trade Secrets Act, IC 24-2-3
- **Trade secret, IC 24-2-3-2.** Information "including a formula, pattern, compilation, program, device, method, technique, or process" that:
  - (1) derives independent economic value from not being generally known to, and not readily ascertainable by proper means by, others who can obtain economic value from it; and
  - (2) is the subject of efforts "reasonable under the circumstances to maintain its secrecy." `[V]`
- **Improper means and misappropriation.** These track the UTSA. The definition of improper means has no express reverse-engineering exclusion. `[V]`
- **Remedies** `[V]`:
  - *Injunction, §3:* actual or threatened misappropriation may be enjoined, plus an extra reasonable period to eliminate commercial advantage. A royalty injunction is available in exceptional circumstances, and affirmative acts may be ordered.
  - *Damages, §4:* actual loss plus unjust enrichment, or a royalty. Exemplary damages up to **2x** for willful and malicious misappropriation.
  - *Attorney's fees, §5:* for a bad-faith claim, bad-faith motion practice, or willful and malicious misappropriation.
  - *Secrecy, §6:* the court preserves secrecy through protective orders, in-camera hearings and sealing.
- **Limitations, §7.** 3 years from actual or constructive discovery. Continuing misappropriation is a single claim. `[V]`
- **Displacement, §1(c).** The chapter "displaces all conflicting law of this state" on trade-secret misappropriation, "except contract law and criminal law." `[V]`
- **Currency.** The section histories show no amendment after P.L.137-2021 (to §8 only). The 2026 IGA text matches the chapter. No change in 2025–26. `[V]`
- ***Amoco Production Co. v. Laird*, 622 N.E.2d 912 (Ind. 1993)** `[V]`:
  - Indiana adopted the UTSA "substantially as promulgated," so case law from other UTSA states is relevant authority.
  - Information is "not readily ascertainable" where duplicating it requires "a substantial investment of time, expense, or effort." The court rejected an "economic infeasibility" standard.
  - A compilation of partly public elements can still be a trade secret.
  - The plaintiff must identify the secrets and prove they exist.
- ***Infinity Products, Inc. v. Quandt*, 810 N.E.2d 1028 (Ind. 2004)** `[V]`:
  - Indiana's displacement clause is broader than the uniform act's.
  - The UTSA displaces **respondeat superior**: a new employer is not vicariously liable for a hired employee's misappropriation "absent the proof of scienter" (knows or has reason to know). The departed salesman was liable; his new employer was not.
  - **Secrecy measures** that counted as evidence: locked offices, locked file cabinets, computer passwords.
  - The court left open whether civil treble damages based on criminal acts fall within the criminal-law exception.
- ***Ackerman v. Kimball International, Inc.*, 652 N.E.2d 507 (Ind. 1995)** `[V]`:
  - Upheld a UTSA injunction barring a departing executive from working for *any* competitor for one year.
  - The basis was his "pre-departure harvesting" of proprietary information, which created a threat of misappropriation.
  - IC 24-2-3-3 permits enjoining the *acceptance of employment* in such a case.
- **Inevitable disclosure.**
  - *Dearborn v. Everett J. Prescott, Inc.*, 486 F. Supp. 2d 802 (S.D. Ind. 2007), reads *Ackerman* as Indiana recognizing inevitable disclosure "on extreme facts." It limits the theory to a "rare and narrow set of circumstances" where the employee acted in bad faith in taking or threatening to take confidential information. `[V]`
  - *Med-1 Solutions, LLC v. Taylor*, No. 24A-PL-450 (Ind. Ct. App. Nov. 25, 2024) (Vaidik, J.; the plaintiffs are the RevOne companies) cited *Dearborn* and applied the same narrow approach, affirming denial of a preliminary injunction. It called the inevitable-disclosure assertion "little more than speculation." It quoted the trial court's finding that the evidence fell short of showing the employee "actually retrieved, downloaded, or transferred" confidential data. `[V via FindLaw copy; Indiana Lawyer/IBJ report matches]` Whether *Med-1* is published or precedential: `[UNVERIFIED]`.
  - *Dearborn* is a federal district court's prediction of Indiana law, not an Indiana holding. `[V]`

### IN2. Duty of loyalty (common law)
- ***Kopka, Landau & Pinkus v. Hansen*, 874 N.E.2d 1065 (Ind. Ct. App. 2007)** `[V]`:
  - An employee owes a fiduciary duty of loyalty and must not actively and directly compete for customers or employees while employed.
  - The employee may *prepare* to compete, but cannot "use confidential information peculiar to his employer's business" before leaving.
  - Asking coworkers about leaving was preparation, not breach.

  Interplay with UTSA displacement: a loyalty claim that rests only on misusing secret information risks displacement. `[INFERENCE from HDNet]`

### IN3. Criminal and civil-treble statutes (Indiana Code, 2026 text)
- **"Property," IC 35-31.5-2-253.** Applies throughout Title 35. It expressly includes "intangibles," "trade secrets," and "(15) data." Property is "of another person" if that person has a possessory or proprietary interest, "even if" the accused also has one. `[V]`
- **Theft, IC 35-43-4-2.** Knowingly or intentionally exerting unauthorized control over another's property "with intent to deprive" them of any part of its value or use. Grading `[V]`:
  - Class A misdemeanor by default;
  - Level 6 felony at $750 to under $50,000;
  - Level 5 felony at $50,000 or more.
- **Conversion, IC 35-43-4-3.** The same unauthorized control *without* the intent to deprive. Class A misdemeanor. `[V]`
- **Unauthorized control and exerting control, IC 35-43-4-1.** "Unauthorized" includes control exerted "in a manner or to an extent other than" consented to. "Exert control" includes "possess" and "transfer." `[V]` A former employee keeping a company laptop or copying files beyond what was permitted fits these words. `[INFERENCE]`
- **Offense against intellectual property, IC 35-43-1-7.** Knowingly or intentionally, without authorization, modifying or destroying data or programs, or "discloses or takes" data that is a trade secret under IC 24-2-3-2 or otherwise confidential by law, residing on a computer or network. **Level 6 felony.** `[V]` Unchanged since 2014. `[V]`
- **Offense against computer users, IC 35-43-1-8.** Covers disrupting or denying computer services; destroying, taking or damaging equipment; damaging a computer; or introducing a contaminant. `[V]` Grading: Level 6 felony; Level 5 at a $750–$50,000 loss, with intent to defraud, or if it impairs a government operation or public service; Level 4 at $50,000 or more or if it endangers human life. Level 5 and 4 versions are also deceptive acts actionable by the Attorney General. `[V]`
- **Computer trespass, IC 35-43-2-3(b).** Knowingly or intentionally accessing a computer system or network, or any part of one, "without the consent of the owner." Class A misdemeanor. `[V]` "Access" includes "retrieve data from" and "make use of resources of." `[V]`
  - **CHANGED 2025–26.** P.L.111-2026 added to the "computer network" definition: "includes a cellular telephone or other wireless or cellular communications device." `[V]` (diffed against the 2025 IGA text) The act is **SEA 119 (2026), "Grooming,"** signed by the Governor 2026-03-05. SECTION 6 amends IC 35-43-2-3, effective **July 1, 2026**. `[V]` (enrolled act and IGA bill record opened)
  - "Without the consent" is a consent test, not *Van Buren*'s federal gates test, and no Indiana appellate reading after *Van Buren* was found. `[INFERENCE]`/`[UNVERIFIED]`
- **Crime Victims Relief Act (CVRA), IC 34-24-3-1.** A person who "suffers a pecuniary loss as a result of a violation of" **IC 35-43** (which includes theft, conversion, offense against intellectual property, offense against computer users and computer trespass) may recover `[V]`:
  - up to **3x actual damages**;
  - costs and a reasonable attorney's fee; and
  - travel and time expenses.

  You cannot recover both punitive damages and CVRA amounts (IC 34-24-3-3). `[V]`
  - **CHANGED 2025–26.** P.L.142-2026 added IC 25-37.5 (valuable-metal dealers) to the predicate list. This does not matter for insider theft. `[V]`
- **Theft statute edit (2026).** P.L.80-2026 added "domestic animal" to the Level 6 theft list. Not relevant. `[V]`
- **Indiana RICO.** The predicate list was amended by P.L.186-2025, P.L.148-2026 and P.L.153-2026; theft remains a predicate (see the creative-angles section). `[V]` What changed (diff of the 2024, 2025 and 2026 IGA text): P.L.186-2025 updated a controlled-substance-analog cross-reference. P.L.148-2026 and P.L.153-2026 added "(42) Sale of alcohol without a permit." Neither matters for insider theft. `[V]`
  - *Corrupt business influence, IC 35-45-6-2:* a Level 5 felony, including conducting an enterprise's activities "through a pattern of racketeering activity." `[V]`
  - *Pattern, IC 35-45-6-1(d):* at least 2 related incidents, the last within 5 years of a prior one. `[V]` "Racketeering activity" includes **theft (IC 35-43-4-2)**. It does not list IC 35-43-1-7. `[V]`
  - *Civil remedy, IC 34-24-2-6(b):* on a preponderance showing, the court "shall order" 3x actual damages, costs, a reasonable attorney's fee and allowable punitive damages, with a jury right. `[V]` A TRO or preliminary injunction requires "immediate danger of significant loss or damage" (§6(a)). `[V]`

### IN4. Displacement of other Indiana claims
- ***HDNet, LLC v. North American Boxing Council*, 972 N.E.2d 920 (Ind. Ct. App. 2012)** `[V]`:
  - The UTSA displaces **common-law idea misappropriation even where the information is not a trade secret.** The court adopted the majority "two-tier" view: information is either a protected trade secret or unprotected general knowledge.
  - "If the information is a trade secret, the plaintiff's claim is preempted"; if not, the plaintiff has no legal interest. (HDNet quoting *Hauck Mfg. v. Astec*.)
  - A **CVRA civil-conversion** claim over ideas is also displaced. The CVRA is not "derivative" of criminal law the way RICO is. Information or ideas protected by contract are not displaced.
  - Subsequent history: the Indiana Supreme Court denied transfer (reported Dec. 11, 2012). `[V: secondary only, The Indiana Lawyer; no Indiana docket lookup]`
- ***AGS Capital Corp. v. Product Action International, LLC*, 884 N.E.2d 294 (Ind. Ct. App. 2008).** The UTSA "does not preempt a civil RICO claim," which is "additional punishment" for patterned criminal violations. The court largely affirmed a preliminary injunction on UTSA and RICO grounds where ex-employees brought a competitor a "library" of process information. It reversed one overbroad provision (affirmed in part, reversed in part; one judge partly dissented). `[V]`
- **What survives** `[INFERENCE from IC 24-2-3-1(c), HDNet, AGS, Quandt]`:
  - contract claims (NDA, return-of-property, invention assignment);
  - criminal prosecution;
  - civil RICO;
  - claims for **wrongs distinct from information misuse**, such as keeping a physical laptop, destroying data (IC 35-43-1-8 or CFAA), or loyalty breaches like soliciting customers while employed.

  Whether a CVRA claim for a *tangible device* survives is untested; it does not "pertain to" trade secrets, so displacement should not apply. `[INFERENCE]`

---

## South Carolina

### SC1. South Carolina Trade Secrets Act, S.C. Code §39-8-10 to -130
- **Improper means, §39-8-20(1).** Includes breaching duties imposed by "the common law, statute, contract, license, protective order." `[V]`
- **Misappropriation, (2).** Adds plain "acquisition ... by improper means" without a knowledge element. `[V]`
- **Trade secret, (5)(a).** Value from not being generally known or readily ascertainable "by the public or any other person who can obtain economic value," plus reasonable secrecy efforts. `[V]`
- **Combinations, (5)(b).** A trade secret may be a simple fact or a series of minor items whose "collective effect" must be considered. `[V]`
- **Statutory employee duty, §39-8-30(B).** An employee informed of, or who should reasonably have known of, a trade secret must not use or disclose it without permission. The duty exists "independently of and in addition to" any written NDA, non-compete or other agreement. `[V]`
- **NDAs need no time or geographic limit, §39-8-30(D).** A contractual duty not to disclose or to limit use "must not be considered void ... for lack of a durational or geographical limitation." `[V]`
- **Civil action, §39-8-30(C)** `[V]`.
- **Remedies** `[V]`:
  - *Damages, §39-8-40:* actual damages (loss or unjust enrichment, or a royalty), reducible for a good-faith change of position. "Separate exemplary damages" up to **2x** on a finding of "wilful, wanton, or reckless disregard." That is a lower bar than the DTSA's or Indiana's "willful and malicious." `[V]`
  - *Injunction, §39-8-50:* actual or threatened misappropriation; the extension period accounts for "average rate of business growth"; royalty injunctions; affirmative acts. `[V]`
  - *Attorney's fees, §39-8-80:* for a bad-faith claim, bad-faith injunction practice, or **"wilful misappropriation"** (no "malicious" needed). `[V]`
- **Discovery shield, §39-8-60.** Before ordering discovery of designated trade secrets, the court must find "substantial need." That requires particularized pleading, direct relevance, substantial prejudice and likely admissibility. Real-time database access is generally barred, and materials are returned at the end of the case. `[V]` *Laffitte v. Bridgestone Corp.*, 381 S.C. 460 (2009): §39-8-60(B) applies in "any civil action," and the Rule 26(c) balancing test also governs. `[V]`
- **Limitations, §39-8-70.** 3 years from discovery; continuing misappropriation is a single claim. `[V]`
- **Currency.** Section histories show 1997 Act No. 38 and nothing later. The online Code is "current through the 2025 Session." `[V]` 2026 session: `[UNVERIFIED: SC bill search returned no usable results]`.

### SC2. Criminal, §39-8-90, and the Computer Crime Act, §16-16-10 et seq.
- **Trade secret theft, §39-8-90.** Requires intent to (or reason to believe it will) injure the owner and benefit another. Covers stealing, wrongful appropriation, copying, downloading, uploading or transmitting, receiving, solicitation, attempt and conspiracy. Penalty: up to **$100,000 and/or 10 years.** `[V]` It is listed as a **Class E felony** in §16-1-90(E). `[V]` (First-degree computer crime, §16-16-20(2), is listed as a Class F felony.)
- **Computer Crime Act definitions, §16-16-10** `[V]`:
  - "Computer" includes "digital cellular telephones" and other handhelds.
  - "Property" includes data and software, tangible or intangible, "and data while in transit."
  - **"Unauthorized use"** includes "authorized use" of a computer "in a manner not explicitly or implicitly authorized." That is a purpose or manner test.
  - "Computer hacking" includes use "in a manner that exceeds any right or permission granted."
- **Offenses and grading, §16-16-20** `[V]`:
  - The offense: wilfully, knowingly, maliciously, and "without authorization or for an unauthorized purpose," accessing a computer to defraud, obtain property or commit a crime, or altering, damaging or destroying a computer or data.
  - *First degree:* gain or loss over $10,000. Felony, $50k / 5 years.
  - *Second degree:* over $1,000, *or* where the person "deprives the owner of possession of, or takes, transfers, conceals, or retains possession of" any computer, data or computer-related property. Misdemeanor, up to $10k / 1 year (first offense).
  - *Third degree:* $1,000 or less, or hacking.
  - Each computer affected is a separate violation.
- **Civil action, §16-16-25.** Against a person "convicted under this chapter," for compensatory damages, restitution and attorney's fees. Recoverable items include verification costs, repair or replacement, lost profits while the system was unusable, and data restoration. `[V]` No conviction means no civil claim under this section. `[V]` Other civil remedies are preserved ("In addition to other civil remedies"). `[V]`
- **Inference.** SC's "unauthorized purpose" and "retains possession of ... data" wording reaches employee misuse that *WEC*/*Van Buren* put outside the federal CFAA. But the civil route needs a conviction first. `[INFERENCE]`

### SC3. Larceny, breach of trust, conversion, loyalty, SCUTPA
- **Larceny, §16-13-30.** Petit larceny covers goods and "choses in action" of $2,000 or less. Grand larceny (over $2,000) is a felony: up to 5 years (to $10k) or 10 years ($10k and up). `[V]`
- **Breach of trust with fraudulent intent, §16-13-230.** "Guilty of larceny," graded at the same $2,000 / $10,000 thresholds. `[V]` This fits an employee entrusted with company devices or funds. `[INFERENCE]`
- **Conversion (civil).** The "unauthorized assumption and exercise of the right of ownership" over "goods or personal chattels" of another. *Moore v. Weinberg*, 383 S.C. 583 (2009). Money counts if identifiable. `[V]` Whether SC recognizes conversion of electronic data or other intangibles: `[UNVERIFIED]`. Conversion claims based on trade-secret misappropriation are displaced (SC4). `[V statute]`
- **Duty of loyalty.** "An employee has a duty of fidelity to his employer." *Berry v. Goodyear Tire & Rubber Co.*, 270 S.C. 489 (1978), citing *Lowndes Products, Inc. v. Brower*, 259 S.C. 322 (1972). In *Berry*, disloyal side work for a competitor justified discharge and forfeited release pay. `[V]` *Lowndes*: "The first issue ... in every trade secret case" is whether a trade secret exists. `[V]`
- **SC Unfair Trade Practices Act, §39-5-20 and §39-5-140.** Unfair or deceptive acts "in the conduct of any trade or commerce." A private action requires "ascertainable loss." The court **shall** award **3x** for a willful or knowing violation ("knew or should have known"), plus mandatory attorney's fees on a violation. `[V]` Whether SC courts allow SCUTPA claims in employer–employee trade secret disputes, or require an adverse public-interest impact: `[UNVERIFIED: no SC case opened]`. If the claim rests on trade-secret misappropriation, §39-8-110 displaces it. `[INFERENCE]`

### SC4. Displacement, §39-8-110 and §39-8-30(E)
- **What is displaced, (A).** The Act "displaces conflicting tort, restitutionary, and other law" that provides civil remedies for trade-secret misappropriation. `[V]`
- **What is kept, (B).** Contractual remedies ("whether or not based upon misappropriation") and the SC Tort Claims Act. `[V]`
- **Other claims, (C).** Civil claims "not based upon misappropriation" follow ordinary rules. `[V]`
- **§39-8-30(E).** The chapter applies to "any and all civil remedies" based on misappropriation or protection of a trade secret. `[V]`
- **Comparison.** SC's text is the uniform act's narrower version (tied to "misappropriation of a trade secret"), not Indiana's broader "pertaining to" clause. Whether SC courts follow HDNet's rule that non-secret information claims are also displaced: `[UNVERIFIED: no SC appellate case found or opened]`.

---

## Facts that decide outcomes

### Employer side (what wins)
1. **A specific list of the secrets.** Courts reject "everything about our software." *IDX Systems Corp. v. Epic Systems Corp.*, 285 F.3d 581 (7th Cir. 2002): a 43-page description "does not separate the trade secrets from the other information." `[V]` *Amoco*: the plaintiff must identify the secrets. `[V]` *Lowndes*: whether a secret exists comes first. `[V]`
2. **Documented secrecy measures.** Locked rooms and cabinets, passwords (*Quandt*); NDAs, access tiers and need-to-know. The reasonableness requirement is statutory in all three systems. `[V]` The Illinois-law six-factor list in *Learning Curve Toys, Inc. v. PlayWood Toys, Inc.*, 342 F.3d 714 (7th Cir. 2003) treats the Restatement factors as "instructive guidelines," not a rigid test. `[V]` Indiana: *Amoco* treats the Restatement §757 factors as helpful guidance (quoting a Maryland case) and relied on the sixth factor, ease of duplication. `[V]`
3. **Cost to recreate.** A substantial investment of time and money shows the information is "not readily ascertainable" (*Amoco*). `[V]`
4. **Forensic proof of taking.** Downloads, USB transfers, personal email or cloud uploads, and wiping. *Ackerman*'s "harvesting" won a one-year employment bar. *Med-1* failed for lack of download or transfer evidence. `[V]`
5. **Code-based access limits** for any CFAA claim: role permissions, revoked credentials, and use of another person's login. *Van Buren*, *WEC* and *NRA Group* defeat policy-only theories. `[V]` A claim for after-departure use of revoked credentials fits "without authorization." `[INFERENCE]`
6. **CFAA $5,000 "loss"** built from response, assessment and restoration costs. Technological harm is required (*Van Buren* pg. 15). `[V]`
7. **Signed agreements with the §1833(b) notice** (or a cross-referenced policy), so 2x exemplary damages and fees stay available. `[V]`
8. **The new employer's knowledge.** In Indiana there is no respondeat superior under the UTSA (*Quandt*), so the employer must prove the new employer knew or had reason to know. `[V]` Promptly sending a notice letter to the new employer can create that knowledge. `[INFERENCE]`
9. **Timing.** File within 3 years of discovery (DTSA, IN, SC trade secrets) and within 2 years for the CFAA. Move fast for an injunction; delay undercuts irreparable harm. `[V statutes]`/`[INFERENCE]` on delay.
10. **SC statutory duty.** Even without an NDA, SC employees owe a duty not to use or disclose known secrets (§39-8-30(B)). `[V]`

### Employee side (what wins)
1. **General skill, knowledge and public information** are not secrets. Indiana's two-tier view (*HDNet*) means non-secret information gives the employer no tort claim, though contract claims survive. `[V]`
2. **Weak secrecy practices**: no access controls, broad sharing, no NDAs. `[V statutes]`
3. **Authorized access.** If the employee could open the files, the CFAA probably fails (*WEC*, 4th Cir. binding in SC; *Van Buren*; *NRA Group*). `[V]`
4. **No use or disclosure, prompt return, and a certification of deletion.** These undercut "threatened misappropriation" and inevitable disclosure (*Dearborn*, *Med-1*). `[V]`/`[INFERENCE]`
5. **No DTSA notice** means no exemplary damages or fees under the DTSA against that employee. `[V]`
6. **Whistleblowing**: disclosure in confidence to a lawyer or government official, or under seal, is immune (§1833(b)). The SEC bars enforcing NDAs against SEC reporting (Rule 21F-17). `[V]` Hacking to obtain the material is not immunized (§1833(b)(5)). `[V]`
7. **Displacement defenses**: in Indiana, attack conversion, idea and unjust-enrichment counts (*HDNet*). In SC, attack tort counts based on misappropriation (§39-8-110). `[V]`
8. **The DTSA cannot bar employment** (§1836(b)(3)(A)(i)). This is weaker in Indiana because of *Ackerman*. `[V]`
9. **Preparing to compete is lawful** (*Kopka*): forming an entity or lining up equipment, but no active competition or use of confidential information before leaving. `[V]`
10. **Retaliation context.** Suits filed soon after protected complaints draw scrutiny. *NRA Group*'s suit followed harassment complaints and came weeks after the employees left. The opinion opens: "In the wrong hands, the law becomes a hammer in search of a nail." `[V]` (Its retaliation-law effect is outside this ticket.)

---

## Creative or non-obvious angles (each with risk)

1. **Indiana civil RICO for mandatory treble damages** (*AGS Capital*; IC 34-24-2-6). Two or more related **thefts** (IC 35-43-4-2, e.g., several downloads or devices, since data and trade secrets are "property") within 5 years can form a pattern. Civil RICO survives UTSA displacement, and 3x plus fees is *mandatory*.
   - **Risk:** high. You must prove criminal theft elements, including intent to deprive, and an "enterprise," by a preponderance. *HDNet* confined *AGS* to RICO's "schematic" design. It is aggressive against a lone employee. `[INFERENCE]`
2. **Pair the DTSA with an Indiana UTSA claim to get an employment bar.** A DTSA injunction cannot stop a job; Indiana UTSA relief can, on harvesting facts (*Ackerman*).
   - **Risk:** medium. It requires bad-faith taking (*Dearborn*, *Med-1*) and is a short, limited bar. `[INFERENCE]`
3. **Indiana CVRA treble damages for the hardware.** Seek 3x for a retained laptop, phone or drive as theft or conversion of *tangible* property, a wrong distinct from information misuse.
   - **Risk:** medium. *HDNet* displaced CVRA conversion of *ideas*; no case tests devices. Keep the device claim factually separate from the data claim. `[INFERENCE]`
4. **Contract claims as the displacement-proof core.** Both states save contract remedies, and SC NDAs need no time or geographic limit (§39-8-30(D)). Draft a return-and-certify clause, a device-return clause, a liquidated-damages clause and the §1833(b) notice.
   - **Risk:** low to medium. Liquidated damages must be a reasonable estimate. This was not researched. `[UNVERIFIED]`
5. **SC criminal referral to reach policy-based misuse.** SC Code §16-16-20 covers "unauthorized purpose" and *retaining* data, conduct the CFAA no longer reaches. A conviction then opens §16-16-25 civil damages and fees.
   - **Risk:** high and slow. The prosecutor controls the case. Using criminal threats to gain civil leverage can raise ethics and extortion problems. That point was not verified for IN or SC rules. `[UNVERIFIED]`
6. **Employee side: audit the agreement for the §1833(b) notice before negotiating.** If the notice is missing, the employer's fee and 2x exposure under the DTSA disappears, which changes settlement math.
   - **Risk:** low. State fee statutes (IN §5, SC §39-8-80) still apply. `[V]`
7. **Employee side: SC's discovery shield cuts both ways.** §39-8-60 forces the plaintiff to plead with particularity and show "substantial need" before getting the defendant's own trade secrets, such as a new employer's code.
   - **Risk:** low. `[V]`
8. **Federal criminal route.** It runs through EEA §1832, not the NSPA, for pure data (*Aleynikov*), and not "exceeds authorized access" on policy theories (JM 9-48.000).
   - **Risk:** DOJ priorities. `[V]`

---

## Open questions
1. ~~The amended *NRA Group* opinion and certiorari.~~ Resolved by the independent verification: the amended text matches, and cert. was denied 2026-03-30 (No. 25-1033). Only the reporter cites remain unconfirmed.
2. **Post-*Van Buren*** CFAA employee cases in the 7th Circuit, 4th Circuit, S.D./N.D. Ind. and D.S.C. Is *Citrin*'s agency theory still followed?
3. **Indiana:** whether the Indiana Supreme Court has spoken on UTSA displacement since 2012 (*HDNet* transfer was denied in 2012, per a secondary report). Whether a CVRA device claim survives displacement. The CVRA limitations period. The effective date of P.L.142-2026 (SB 271). Whether *Med-1* is published. (Resolved by the verifier: P.L.111-2026 is SEA 119, effective 2026-07-01; the RICO-list changes are listed in IN3.)
4. **SC:** acts from the 2026 session. Appellate cases on §39-8-110 scope, especially non-secret information. Conversion of electronic data. Whether SCUTPA reaches employer–employee disputes. (Resolved: §39-8-90 is a Class E felony.)
5. **Federal:** whether any 2025–26 public law touched §§1030 or 1831–1839, checked against the OLRC once its site is back.
6. **Choice of law:** how an Indiana-employer / SC-resident employee case picks between IUTSA and SCTSA (for the applied-state step).

---

## Verification note
- **Opened and read (primary):**
  - **Federal statutes:** 18 U.S.C. §§1030, 1831, 1832, 1833, 1836, 1837, 1838, 1839, from the govinfo **2024 edition** HTML, with amendment notes read. LII pages for §§1030, 1832, 1833, 1836 and 1839 were checked for later amendments (none listed).
  - **Federal rule and policy:** 17 C.F.R. §240.21F-17 via the eCFR API (2026-10-01 point in time); DOJ Justice Manual 9-48.000.
  - **Federal opinions:** *Van Buren* slip opinion (supremecourt.gov PDF, text extracted locally with macOS PDFKit); *NRA Group* August 2025 slip opinion and the October 2025 rehearing order (ca3.uscourts.gov); SCOTUS docket 25A841.
  - **Indiana Code:** IC 24-2-3-1 to -8, IC 34-24-3-1 to -3, IC 34-24-2-6, IC 34-11-2-4 and -7, IC 35-31.5-2-253, IC 35-43-1-7, IC 35-43-1-8, IC 35-43-2-3, IC 35-43-4-1 to -3, IC 35-45-6-1 and -2. All read on iga.in.gov (the 2026 Code, rendered in a browser tab). The 2025 versions of IC 35-43-2-3, IC 35-43-4-2, IC 35-43-1-7 and IC 34-24-3-1 were read to diff the 2026 changes.
  - **SC Code:** chapters 39-8, 16-16, 39-5 (§§20, 140) and 16-13 (§§30, 210, 230) on scstatehouse.gov, with the currency note.
- **Case texts.** These were read in full text from the Harvard Caselaw Access Project static archive (static.case.law), a primary-text mirror of the official reporters. That text **lacks star pagination**, so no pin cites are given for these cases:
  - federal: *WEC*, *Citrin*, *PepsiCo*, *Aleynikov*, *IDX*, *Learning Curve*, *Dearborn*;
  - Indiana: *Amoco*, *Quandt*, *HDNet*, *AGS Capital*, *Kopka*, *Ackerman*;
  - SC: *Lowndes*, *Laffitte*, *Moore*, *Berry*.
- **How claims were checked.** Each `[V]` claim was matched to text in the opened source; quotes were copied from it. Statutory currency was checked from section history lines and, for Indiana, by diffing the 2025 and 2026 text.
- **Not verified:** everything tagged `[UNVERIFIED]`. *Med-1* was read only through FindLaw's copy (two WebFetch summaries). Its quotes were cross-checked against *Dearborn*'s own text, which matched.
- **Prior research.** Used for leads only (Heraeus, Med-1). No claim rests on it.
- **Tool limits** (relevant to completeness):
  - The OLRC site was down. CourtListener and Justia blocked access (a human-verification page and HTTP 403); CAPTCHAs were not bypassed.
  - **The shared web-search budget ran out mid-task**, so post-*Van Buren* circuit cases, SC 2026 acts and SC displacement case law could not be searched.
  - An SC legislature bill query was tried and returned nothing usable.
- **Source-quality concerns.**
  - govinfo's 2024 US Code edition may lag 2025–26 enactments. LII is unofficial.
  - The SC online Code is unofficial (the print edition controls) and is current only through 2025.
  - CAP text is OCR'd and has minor typos ("Ackennan," "Seott").
  - Leagle (secondary) is the only source for the *NRA Group* F.4th cite.
  - Secondary leads are tagged above and none stands alone for a rule.
  - **Conflict noted:** web snippets dated the *NRA Group* opinion both 2025-08-26 and 2025-10-07. Both are right: Aug 26 is the original (vacated) and Oct 7 the amended opinion.

## Sources

| # | Citation | URL | Type | Accessed | Verified |
|---|---|---|---|---|---|
| 1 | 18 U.S.C. §1836 (2024 ed.) | https://www.govinfo.gov/content/pkg/USCODE-2024-title18/html/USCODE-2024-title18-partI-chap90-sec1836.htm | Primary | 2026-10-20 | Y |
| 2 | 18 U.S.C. §1839 | https://www.govinfo.gov/content/pkg/USCODE-2024-title18/html/USCODE-2024-title18-partI-chap90-sec1839.htm | Primary | 2026-10-20 | Y |
| 3 | 18 U.S.C. §1833 | https://www.govinfo.gov/content/pkg/USCODE-2024-title18/html/USCODE-2024-title18-partI-chap90-sec1833.htm | Primary | 2026-10-20 | Y |
| 4 | 18 U.S.C. §§1831, 1832, 1837, 1838 | https://www.govinfo.gov/content/pkg/USCODE-2024-title18/html/USCODE-2024-title18-partI-chap90-sec1832.htm (and sec1831, sec1837, sec1838) | Primary | 2026-10-20 | Y |
| 5 | 18 U.S.C. §1030 | https://www.govinfo.gov/content/pkg/USCODE-2024-title18/html/USCODE-2024-title18-partI-chap47-sec1030.htm | Primary | 2026-10-20 | Y |
| 6 | LII 18 U.S.C. §§1030, 1832, 1833, 1836, 1839 (currency check) | https://www.law.cornell.edu/uscode/text/18/1030 | Secondary host of primary text | 2026-10-20 | Y |
| 7 | OLRC uscode.house.gov (unavailable) | https://uscode.house.gov/browse.html | Primary | 2026-10-20 | N |
| 8 | *Van Buren v. United States*, 593 U.S. 374 (2021) | https://www.supremecourt.gov/opinions/20pdf/19-783_k53l.pdf | Primary | 2026-10-20 | Y |
| 9 | *NRA Group, LLC v. Durenleau*, No. 24-1123 (3d Cir. Aug. 26, 2025) (vacated on panel rehearing) | https://www2.ca3.uscourts.gov/opinarch/241123p.pdf | Primary | 2026-10-20 | Y |
| 10 | *NRA Group*, order granting panel rehearing (3d Cir. Oct. 7, 2025) | https://www2.ca3.uscourts.gov/opinarch/241123po.pdf | Primary | 2026-10-20 | Y |
| 11 | *NRA Group*, Aug. 2025 opinion as reported (153 F.4th 1333 per Leagle; corrected label, this is not the amended opinion) | https://www.leagle.com/decision/infco20250827171 | Secondary | 2026-10-20 | N |
| 11a | *NRA Group*, amended opinion (Oct. 7, 2025), in cert. petition App. Vol. I, 3a–39a (154 F.4th 153 per petition) | https://www.supremecourt.gov/DocketPDF/25/25-1033/397161/20260224131620918_NRA%20-%20Appx%20Vol%20I%20%202.6.26.pdf | Primary text in party filing | 2026-10-20 | Y (cite N) |
| 11b | SCOTUS docket 25-1033 (cert. denied 2026-03-30) | https://www.supremecourt.gov/docket/docketfiles/html/public/25-1033.html | Primary | 2026-10-20 | Y |
| 11c | Indiana SEA 119 (2026), P.L.111-2026, enrolled act | https://iga.in.gov/pdf-documents/124/2026/senate/bills/SB0119/SB0119.06.ENRH.pdf | Primary | 2026-10-20 | Y |
| 11d | S.C. Code §16-1-90 (felony classification) | https://www.scstatehouse.gov/code/t16c001.php | Primary (unofficial online Code) | 2026-10-20 | Y |
| 11e | 18 U.S.C. §2314 (2024 ed.) | https://www.govinfo.gov/content/pkg/USCODE-2024-title18/html/USCODE-2024-title18-partI-chap113-sec2314.htm | Primary | 2026-10-20 | Y |
| 12 | SCOTUS docket 25A841 | https://www.supremecourt.gov/docket/docketfiles/html/public/25A841.html | Primary | 2026-10-20 | Y |
| 13 | *WEC Carolina Energy Solutions LLC v. Miller*, 687 F.3d 199 (4th Cir. 2012) | https://static.case.law/f3d/687/cases/0199-01.json | Primary (CAP) | 2026-10-20 | Y |
| 14 | *Int'l Airport Ctrs., L.L.C. v. Citrin*, 440 F.3d 418 (7th Cir. 2006) | https://static.case.law/f3d/440/cases/0418-01.json | Primary (CAP) | 2026-10-20 | Y |
| 15 | *PepsiCo, Inc. v. Redmond*, 54 F.3d 1262 (7th Cir. 1995) | https://static.case.law/f3d/54/cases/1262-01.json | Primary (CAP) | 2026-10-20 | Y |
| 16 | *United States v. Aleynikov*, 676 F.3d 71 (2d Cir. 2012) | https://static.case.law/f3d/676/cases/0071-01.json | Primary (CAP) | 2026-10-20 | Y |
| 17 | *IDX Sys. Corp. v. Epic Sys. Corp.*, 285 F.3d 581 (7th Cir. 2002) | https://static.case.law/f3d/285/cases/0581-01.json | Primary (CAP) | 2026-10-20 | Y |
| 18 | *Learning Curve Toys, Inc. v. PlayWood Toys, Inc.*, 342 F.3d 714 (7th Cir. 2003) | https://static.case.law/f3d/342/cases/0714-01.json | Primary (CAP) | 2026-10-20 | Y |
| 19 | 17 C.F.R. §240.21F-17 | https://www.ecfr.gov/api/versioner/v1/full/2026-10-01/title-17.xml?part=240&section=240.21F-17 | Primary | 2026-10-20 | Y |
| 20 | DOJ Justice Manual 9-48.000 (May 2022) | https://www.justice.gov/jm/jm-9-48000-computer-fraud | Primary (agency policy) | 2026-10-20 | Y |
| 21 | IC 24-2-3-1 to -8 (2026) | https://iga.in.gov/laws/2026/ic/titles/24#24-2-3 | Primary | 2026-10-20 | Y |
| 22 | IC 34-24-3-1 to -3 (2026; 2025 for diff) | https://iga.in.gov/laws/2026/ic/titles/34#34-24-3-1 | Primary | 2026-10-20 | Y |
| 23 | IC 34-24-2-6; IC 34-11-2-4, -7 | https://iga.in.gov/laws/2026/ic/titles/34#34-24-2-6 | Primary | 2026-10-20 | Y |
| 24 | IC 35-31.5-2-253; 35-43-1-7; 35-43-1-8; 35-43-2-3; 35-43-4-1, -2, -3 (2026; 2025 for diff) | https://iga.in.gov/laws/2026/ic/titles/35#35-43-4-2 | Primary | 2026-10-20 | Y |
| 25 | IC 35-45-6-1, -2 | https://iga.in.gov/laws/2026/ic/titles/35#35-45-6-1 | Primary | 2026-10-20 | Y |
| 26 | *Amoco Prod. Co. v. Laird*, 622 N.E.2d 912 (Ind. 1993) | https://static.case.law/ne2d/622/cases/0912-01.json | Primary (CAP) | 2026-10-20 | Y |
| 27 | *Infinity Prods., Inc. v. Quandt*, 810 N.E.2d 1028 (Ind. 2004) | https://static.case.law/ne2d/810/cases/1028-01.json | Primary (CAP) | 2026-10-20 | Y |
| 28 | *HDNet, LLC v. N. Am. Boxing Council*, 972 N.E.2d 920 (Ind. Ct. App. 2012) | https://static.case.law/ne2d/972/cases/0920-01.json | Primary (CAP) | 2026-10-20 | Y (history N) |
| 29 | *AGS Capital Corp. v. Prod. Action Int'l, LLC*, 884 N.E.2d 294 (Ind. Ct. App. 2008) | https://static.case.law/ne2d/884/cases/0294-01.json | Primary (CAP) | 2026-10-20 | Y |
| 30 | *Kopka, Landau & Pinkus v. Hansen*, 874 N.E.2d 1065 (Ind. Ct. App. 2007) | https://static.case.law/ne2d/874/cases/1065-01.json | Primary (CAP) | 2026-10-20 | Y |
| 31 | *Ackerman v. Kimball Int'l, Inc.*, 652 N.E.2d 507 (Ind. 1995) | https://static.case.law/ne2d/652/cases/0507-01.json | Primary (CAP) | 2026-10-20 | Y |
| 32 | *Dearborn v. Everett J. Prescott, Inc.*, 486 F. Supp. 2d 802 (S.D. Ind. 2007) | https://static.case.law/f-supp-2d/486/cases/0802-01.json | Primary (CAP) | 2026-10-20 | Y |
| 33 | *Med-1 Solutions, LLC v. Taylor*, No. 24A-PL-450 (Ind. Ct. App. Nov. 25, 2024) | https://caselaw.findlaw.com/court/in-court-of-appeals/116719877.html | Primary text on secondary host | 2026-10-20 | Partial (via summaries; publication status N) |
| 34 | S.C. Code §§39-8-10 to -130 | https://www.scstatehouse.gov/code/t39c008.php | Primary (unofficial online Code) | 2026-10-20 | Y |
| 35 | S.C. Code §§16-16-10 to -40 | https://www.scstatehouse.gov/code/t16c016.php | Primary (unofficial online Code) | 2026-10-20 | Y |
| 36 | S.C. Code §§39-5-20, -140 | https://www.scstatehouse.gov/code/t39c005.php | Primary (unofficial online Code) | 2026-10-20 | Y |
| 37 | S.C. Code §§16-13-30, -210, -230 | https://www.scstatehouse.gov/code/t16c013.php | Primary (unofficial online Code) | 2026-10-20 | Y |
| 38 | *Lowndes Prods., Inc. v. Brower*, 259 S.C. 322, 191 S.E.2d 761 (1972) | https://static.case.law/sc/259/cases/0322-01.json | Primary (CAP) | 2026-10-20 | Y |
| 39 | *Laffitte v. Bridgestone Corp.*, 381 S.C. 460 (2009) | https://static.case.law/sc/381/cases/0460-01.json | Primary (CAP) | 2026-10-20 | Y |
| 40 | *Moore v. Weinberg*, 383 S.C. 583, 681 S.E.2d 875 (2009) | https://static.case.law/sc/383/cases/0583-01.json | Primary (CAP) | 2026-10-20 | Y |
| 41 | *Berry v. Goodyear Tire & Rubber Co.*, 270 S.C. 489, 242 S.E.2d 551 (1978) | https://static.case.law/sc/270/cases/0489-01.json | Primary (CAP) | 2026-10-20 | Y |

## Independent verification (2026-10-20)

A second agent re-checked this file from scratch on 2026-10-20. It fetched every source again itself and did not rely on the first agent's downloads.

**What was re-opened**
- **Federal statutes and rules:** 18 U.S.C. §§1030, 1831, 1832, 1833, 1836, 1837, 1838, 1839 and 2314 (govinfo 2024 ed., including the notes on Pub. L. 114-153 §2(e) and Pub. L. 112-236). LII source-credit lines for §§1030, 1831–1833, 1836 and 1839. 17 C.F.R. §240.21F-17 (eCFR, 2026-10-01; the latest amendment is dated 2016-12-31). Justice Manual 9-48.000 ("updated May 2022").
- **Federal opinions and dockets:** *Van Buren* slip opinion (supremecourt.gov). *NRA Group* Aug. 26, 2025 opinion and Oct. 7, 2025 order (ca3.uscourts.gov). The amended opinion, read in the cert. petition appendix. The cert. petition itself. SCOTUS dockets 25A841 and 25-1033.
- **CAP full text (static.case.law), checked for name, court, date, author and the quoted passages:** *WEC*, *Citrin*, *PepsiCo*, *Aleynikov*, *IDX*, *Learning Curve*, *Dearborn*, *Amoco*, *Quandt*, *Ackerman*, *HDNet*, *AGS Capital*, *Kopka*, *Lowndes*, *Laffitte*, *Moore* and *Berry*.
- **Indiana Code:** the 2024, 2025 and 2026 IGA title files, with sections extracted and diffed: IC 24-2-3-1 to -8; 34-24-3-1, -3; 34-24-2-6; 35-31.5-2-253; 35-43-1-7, -8; 35-43-2-3; 35-43-4-1 to -3; 35-45-6-1, -2. Also the IGA 2026 bill records (SB 119, SB 271, SB 185, HB 1052, HB 1165) and the SEA 119 enrolled act.
- **SC Code** (scstatehouse.gov): chapters 39-8 and 16-16, §§39-5-20 and -140, §§16-13-30 and -230, §16-1-90, and the site's currency note.
- ***Med-1*:** the FindLaw copy, plus the Indiana Lawyer/IBJ report.

**Counts**
- **Authorities:** 61 checked (26 federal, 26 Indiana, 9 SC). All 61 exist and match the stated court, date and citation. **No fabricated or mis-cited authority was found.**
- **Claims:**
  - Confirmed: every `[V]` claim not listed below matched the opened text.
  - Corrected: 12.
  - Removed: 0.
  - Upgraded from UNVERIFIED to verified: 7.
  - Still UNVERIFIED: 14.

**Corrections**
1. *NRA Group*: the file said no certiorari petition was listed. In fact, petition No. 25-1033 was filed 2026-02-06 and **denied 2026-03-30**. A second en banc petition was also denied 2025-11-10.
2. *NRA Group*: the amended opinion was unverified, and the 153 F.4th 1333 cite was labelled as the amended opinion. The amended text is now read: its holdings match the August opinion word for word. The cert. petition gives 154 F.4th 153 for the amended opinion. Leagle gives 153 F.4th 1333 for the August opinion. Sources row 11 is relabelled, and rows 11a–11b are added.
3. *NRA Group* password holding narrowed. The opinion does not say "passwords alone" are never trade secrets. It held these passwords lacked independent economic value and were not the product of a special formula.
4. *NRA Group* "hammer in search of a nail": the court said this of "the law" in the wrong hands, not of the CFAA specifically.
5. *NRA Group* facts: the suit came "just weeks" after the employees resigned or were fired, not weeks after their complaints.
6. *AGS Capital*: the injunction was affirmed in part and reversed in part (one overbroad provision), not affirmed outright.
7. Summary 4: "The DTSA preempts nothing" now notes the §1833(b) exception. That immunity applies under state trade-secret law.
8. §1836(c): "not exclusive" was retagged as `[INFERENCE]`. The verified fact is that the 2016 act struck "exclusive."
9. Inevitable disclosure (Summary 5, IN1): *Dearborn* is labelled a federal district court's prediction of Indiana law, and *Med-1* as applying a narrow approach. The "actually retrieved…" phrase is *Med-1* quoting the trial court. The caption and judge are added.
10. Rule 21F-17: the inference was limited to public or regulated companies, but the rule's text reaches "any person." The inference was revised.
11. IC 35-43-1-8 grading: added the omitted Level 5 trigger (impairing a government or public service) and Level 4 trigger (endangering human life).
12. *HDNet*: the "preempted" quote is attributed as HDNet quoting *Hauck*. "Contract claims are not displaced" is restated as HDNet's actual point: information or ideas protected by contract.

**Upgraded to verified**
1. P.L.111-2026 is SEA 119 (2026), signed 2026-03-05. Its IC 35-43-2-3 amendment takes effect 2026-07-01.
2. The RICO predicate-list changes: P.L.186-2025 updated a cross-reference, and P.L.148/153-2026 added alcohol sales without a permit.
3. *HDNet*: transfer was denied. The only source is The Indiana Lawyer, which is secondary.
4. §2314: the text was opened.
5. §39-8-90 is a Class E felony (§16-1-90(E)).
6. Indiana's use of the Restatement factors (*Amoco*).
7. The *NRA Group* amended-opinion text.

**Still UNVERIFIED (tried once where noted)**
1. Federal 2025–26 amendments to §§1030 and 1831–1839. OLRC still returns "Page Not Found." The govinfo 2024 edition and LII credits show nothing after 2020/2016, and a web search found no enactment.
2. Post-*Van Buren* 7th Circuit treatment of *Citrin*. Tried once by web search; nothing found.
3. The SC 2026 session. The scstatehouse search returned no usable results, and a web search found nothing.
4. SCUTPA in employer–employee disputes. Tried once; only secondary public-interest material was found.
5. SC conversion of electronic data.
6. SC appellate cases on §39-8-110 scope.
7. Whether *Med-1* is published. CourtListener was rate-limited (HTTP 429).
8. *NRA Group* reporter cites (from the party filing and Leagle only).
9. An Indiana post-*Van Buren* reading of computer trespass.
10. The effective date of P.L.142-2026.
11. Liquidated-damages law.
12. The ethics of criminal referral as civil leverage.
13. The FTC and NLRB items (out of scope).
14. Whether a CVRA device claim survives displacement. This is untested and remains `[INFERENCE]`.

**Source-quality flags**
- *Med-1* rests on FindLaw plus a news report.
- *HDNet*'s transfer history rests on The Indiana Lawyer.
- The *NRA Group* reporter cites rest on a party's cert. petition and Leagle.
- The SC online Code is unofficial and current only through the 2025 session.
- LII is unofficial, and OLRC is still unreachable.
- No rule in the file rests on a secondary source alone.

**Could not check:** OLRC currency through Pub. L. 119-120, CourtListener (rate-limited), SC 2026 acts, and the Indiana courts' own docket for *Med-1* and *HDNet*.

**The 2025–26 change list stands.** *NRA Group*, P.L.111-2026 and the minor Indiana edits are all confirmed against primary text. The list now also notes the cert. denial, the SEA 119 effective date, and the 2025–26 RICO-list edits, none of which matters for insider theft.

### IC official check (2026 code download, 2026-10-20)

Each section was read in `sources/indiana-code/IC-title-NN.txt` (official 2026 iga.in.gov download) while building `references/insider-theft.md`. No claim was contradicted.

- **IC 24-2-3-1(c)** (displacement, "pertaining to," contract and criminal law excepted): confirmed.
- **IC 24-2-3-2** (trade secret, improper means, misappropriation; no reverse-engineering exclusion): confirmed.
- **IC 24-2-3-3** (injunction, extension, royalty, affirmative acts): confirmed. The employment bar comes from *Ackerman*'s reading, not the text.
- **IC 24-2-3-4** (damages, 2x exemplary): confirmed, refined: a royalty is available only when neither loss nor unjust enrichment is provable, and the 2x cap applies to the subsection (a) award.
- **IC 24-2-3-5, -6, -7**: confirmed.
- **IC 24-2-3-8** (last amended P.L.137-2021; chapter otherwise unchanged): confirmed.
- **IC 34-24-3-1** (CVRA; IC 35-43 predicate; up to 3x, costs, fee, travel, time; P.L.142-2026 in history): confirmed, refined: the list also covers employee-time expenses and "other reasonable costs of collection." Effective date of P.L.142-2026 is not in the text: not found.
- **IC 34-24-3-2**: checked; retailer presumption, no claim rests on it.
- **IC 34-24-3-3** (no double recovery of punitive and CVRA amounts): confirmed.
- **IC 34-24-2-6** (civil RICO: mandatory 3x, costs, fee, punitive; jury; TRO/preliminary-injunction showing): confirmed.
- **IC 34-11-2-4, -7**: read; no claim in this file rests on them. The CVRA limitations period remains open.
- **IC 35-31.5-2-253** (property includes intangibles, trade secrets, data; "of another person"): confirmed.
- **IC 35-43-1-7** (Level 6; last amended P.L.168-2014): confirmed.
- **IC 35-43-1-8** (grading incl. government/public-service and endangering-life triggers; AG deceptive act): confirmed.
- **IC 35-43-2-3** (computer trespass; "access"; cellular-device sentence; P.L.111-2026 in history): confirmed, refined: consent may come from the owner or "the owner's licensee." The July 1, 2026 effective date is from the enrolled act, not this text.
- **IC 35-43-4-1** (exert control; "unauthorized"): confirmed.
- **IC 35-43-4-2** (grading; P.L.80-2026 domestic animal): confirmed.
- **IC 35-43-4-3** (conversion, Class A misdemeanor): confirmed.
- **IC 35-45-6-1** (pattern; theft listed, IC 35-43-1-7 not listed; items (41)–(42); P.L.186-2025, P.L.148-2026, P.L.153-2026 in history): confirmed.
- **IC 35-45-6-2** (Level 5): confirmed.
