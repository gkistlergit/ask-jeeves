# Skill structure and request flow
Type: grilling
Status: resolved
Blocked by:

## Question

How is the skill laid out and how does a request flow? Decide the order of the opening questions (mode, then state, then depth, or something else), whether arguments can pre-answer them, the reference-file layout (per legal area, per state, or both), how reference files show their as-of date, and whether deep mode uses subagents.

## Answer

Resolved 2026-10-20 with Grant.

- **Request flow.** A request opens with the input: pasted text, a file path, or a described situation. One AskUserQuestion round asks **mode** (employer or employee) and **depth** (quick, intermediate, deep; default intermediate). The state-selection round (ticket 09) follows and ends with Grant confirming the **applied state**. Research starts only after that confirmation.
- **Arguments pre-answer.** `/ask-jeeves employer deep IN <text or path>` fills any of mode, depth and state, keywords in any order. Only missing ones are asked. The state is always confirmed in the state-selection round, even when passed.
- **Reference-file layout: per legal area, state sections inside.** `references/insider-theft.md`, `references/restrictive-covenants.md`, `references/employee-contracts.md`, each sectioned Federal / Indiana / South Carolina; plus `references/choice-of-law.md` (state survey), `references/adjacent-fields.md`, `references/attorney-finder.md`. Revisit a per-state matrix only if more states are built in.
- **As-of date.** Every reference file has frontmatter `as_of: YYYY-MM-DD` and `verified: YYYY-MM-DD`. The memo's verification label prints the oldest as-of date among the files it loaded ("Reference files current as of 2026-10-20"). A staleness warning threshold is left to the update-cadence fog.
- **Subagents by depth.** Quick reads reference files only, no web. Intermediate runs web search in the main thread and **may dispatch subagents when necessary** (Grant's amendment; ticket 10 defines the trigger). Deep dispatches one research subagent per legal area touched, each running the research skill, then one verifier subagent that re-opens every citation.
- **Attorney finder is opt-in, after the memo.** One question offers it and asks the location option. It runs as a subagent at every depth and never runs unasked.
- **Skill files.** `SKILL.md` (flow, guardrails, question wording), `references/` as above, `templates/memo.md` (content from ticket 12), frontmatter `disable-model-invocation: true` so only `/ask-jeeves` triggers it. Fixtures and test results live in the public ask-jeeves repo, not the skill.
- **Glossary.** Added *request*, *reference file*, *candidate state* to `CONTEXT.md`.
- **Plain-language pass (added by Grant, 2026-10-20).** Before the memo is shown, the skill runs the `humanizer` skill over the memo prose and simplifies any legalese a non-lawyer would stumble on. Quotes, citations, statute and case names, and defined glossary terms stay verbatim. Where a quoted contract or statute clause is hard to read, the memo adds a short "in plain terms" line after it. Ticket 12 settles how that line looks on the page.
