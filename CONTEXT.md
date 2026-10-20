# ask-jeeves — glossary

**Mode** — whose side a request takes: *employer* or *employee*. Grant chooses it per request.

**Applied state** — the state whose law a memo applies, confirmed by Grant before research starts. It may be a *primary state* with a *backup state* when the governing law is uncertain.

**Choice-of-law clause** — a contract term naming the governing state. Courts don't always honor it, so it is evidence for the applied state, not the answer.

**Depth** — how much research and verification backs a memo: *quick*, *intermediate* or *deep*. Depth changes how much backs the memo, not which sections it has.

**Verification label** — the memo's statement of how its sources were checked: *unverified* (quick), *quick-verified* (intermediate), or a full *verification note* (deep).

**Issue-spotting memo** — the skill's output: risks, likelihood, what could go wrong later, recommendations, a creative solution, questions for a licensed attorney, and the applied state with reasons. It is never legal advice.

**Creative solution** — a non-obvious option, labeled as creative, with its risk and enforceability stated.

**Insider theft** — an employee or insider taking trade secrets, data or IT assets. Stolen devices and outside hacking are not insider theft.

**Restrictive covenant** — a non-compete, non-solicit, no-hire or confidentiality term.

**Adjacent field** — an area of law outside the three priority fields (for example wage-hour or data privacy) that is ranked include, defer or exclude.

**Attorney finder** — the step after research that returns a short ranked list of license-confirmed, customer-reviewed, budget-friendly attorneys for one *location option*.

**Location option** — where the attorney search centers: live location (with consent), a typed ZIP, the saved home location (city and ZIP only), or Aiken, SC.

**Mismatch** — a location option outside the applied state, which triggers a question about which license matters.

**Strong, not fully confirmed** — the attorney finder's second tier: attorneys who pass the practice, rating and review-count bars but lack a visible recent review, a second independent review platform, or a published fee. Shown only when fewer than 3 qualify, and never counted as qualified.

**Request** — one `/ask-jeeves` invocation: its input (pasted text, a file, or a described situation), mode, applied state and depth.

**Reference file** — a dated, built-in summary of verified law for one legal area, with a section per covered jurisdiction.

**State card** — a slim, dated summary of one state's law for a state without a reference file: its key statutes (pointing into the local statute library) and the 3–6 leading cases on restrictive covenants, IP assignment and wage payment. Built when Grant asks or after 3 logged runs of that state, at `references/state-cards/<ST>.md`. Quick mode can cover a state from its card, labeled "slim state card".

**Run log** — `~/.claude/ask-jeeves-run-log.md`, outside the repo: one line per delivered memo with only the date, applied state, backup and depth. It drives the state-card trigger.

**Candidate state** — the state the selection round proposes before Grant confirms it as the applied state.

**Plain-language pass** — the step that simplifies the memo's legalese before it is shown. Quotes, citations and defined terms are never changed by it.

**End goal** — the outcome Grant wants from a request, in his words (e.g. keep sole ownership of apps he built on his own time). It is asked first and steers the research, risk ranking, recommendations and creative options. It never overrides the safeguards.

**Stress test** — a request whose input is a draft from Grant's `contract-drafter` skill. Jeeves reads the draft from the other side by default, to find what a counterparty or court would attack before anyone signs.

**Handoff** — step 8: passing a memo's findings to `contract-drafter` as a drafting brief, opt-in only.
