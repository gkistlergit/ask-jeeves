# Build the skill
Type: task
Status: claimed
Blocked by: 17

## Question

Build `skills/ask-jeeves/` in this repo (moved from claude-global-settings, 2026-10-20): SKILL.md plus dated reference files per legal area for federal, IN and SC, drawn only from verified research. Follow writing-for-agents and superpowers:writing-skills.

Carried from Grant (2026-10-20): the skill already holds `references/research-resilience.md`, which covers the search budget, the official-source fallbacks, flat subagents, no browser or clipboard, and time limits (claude-global-settings PR #59). SKILL.md must load it before any web research or subagent dispatch, and the build must keep its limits consistent with [Depth modes](10-depth-modes.md).

Carried from [Memo format](12-memo-format.md): Indiana Code cites failed the quick check because iga.in.gov doesn't render through WebFetch. Use the official URL pattern that the research 05 follow-up finds, and put it in research-resilience.md's fallback table.
