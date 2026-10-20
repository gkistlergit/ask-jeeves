# End goal: ask it and let it steer the memo
Type: grilling
Status: resolved
Blocked by: 08, 12

## Question

How does Jeeves capture Grant's end goal, for example "I must retain sole ownership of the 3 apps I created on my own time and with my own money", and how does that goal drive the research and the memo?

## Answer

Resolved 2026-10-20. Grant set the requirement: the skill asks for the end goal, and the goal drives the direction of the skill, with solutions crafted to reach it. Grant accepted the implementation details below by standing practice; he may veto any of them.

- **Asked first**, in plain chat, before mode and depth: one question with Grant's example. "No specific goal" is allowed. A `goal:"…"` argument pre-answers it. Jeeves restates the goal in one line for Grant to check.
- **Steers research.** Research targets the law that helps reach the goal, the law that blocks it, and the levers available (clauses to strike or narrow, carve-outs, documentation, timing). Deep subagents get the goal in generic legal terms. Grant's own wording stays out of search queries.
- **Shapes the memo** (`templates/memo.md`):
  - a **Goal** line in the header;
  - Bottom line opens with whether the goal is reachable (Likely / Uncertain / Unlikely) and why;
  - a new **Path to your goal** section with 3–6 ordered steps, each tied to a risk and its timing;
  - risks that threaten the goal come first and are tagged *(goal)*;
  - the recommendations and creative options are aimed at the goal.
- **Guardrails.** The goal never overrides the standing rules (ticket 15). If reaching it would need anything on the won't-do list, Jeeves says so and aims at the closest lawful version. The live-matter screen also runs against the goal. If the goal is unreachable, the memo says so plainly.
- **Test (ticket 19):** run `fixtures/sample-offer-letter.md` with the goal "keep sole ownership of 3 apps I built on my own time and money". §6 claims off-hours and unrelated inventions and leaves Exhibit A blank. The memo should rate the goal, put the §6 risk first, and give a path (narrow §6 before signing, fill Exhibit A with the apps, keep the work on personal time and equipment, and so on) with citations.
