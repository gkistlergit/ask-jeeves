# Build the skill
Type: task
Status: resolved
Blocked by: 17

## Question

Build `skills/ask-jeeves/` in this repo (moved from claude-global-settings, 2026-10-20): SKILL.md plus dated reference files per legal area for federal, IN and SC, drawn only from verified research. Follow writing-for-agents and superpowers:writing-skills.

Carried from Grant (2026-10-20): the skill already holds `references/research-resilience.md`, which covers the search budget, the official-source fallbacks, flat subagents, no browser or clipboard, and time limits (claude-global-settings PR #59). SKILL.md must load it before any web research or subagent dispatch, and the build must keep its limits consistent with [Depth modes](10-depth-modes.md).

Carried from [Memo format](12-memo-format.md): Indiana Code cites failed the quick check because iga.in.gov doesn't render through WebFetch. Use the official URL pattern that the research 05 follow-up finds, and put it in research-resilience.md's fallback table.

## Answer

Built 2026-10-20 on branch `skill/v1` (draft PR gkistlergit/ask-jeeves#1): `skills/ask-jeeves/SKILL.md` (151 lines), `templates/memo.md`, and the seven reference files listed in the PR (about 1,500 lines, 727 `[cite:]` tags). Every Indiana Code citation was checked against the official 2026 Indiana Code download; none contradicted the research. Corrections:
- IC 22-4-15-1 was amended in 2025–26.
- IC 22-2-6-2 allows no deduction for lost or unreturned property.

No Indiana statute limits assignment of employee inventions; all 37 titles were scanned. The end goal from ticket 21 is wired into the flow and the template.
