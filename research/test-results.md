# Test results (ticket 19)

All runs are of `skill/v1`, 2026-10-20. Fixtures are in `fixtures/` (fictional). Each memo test ran employee mode, Indiana, with the goal "keep sole ownership of 3 apps built on my own time and money", on `fixtures/offer-letter-with-citation.md`, which contains a planted fake case.

| Test | Result | Evidence |
|---|---|---|
| Quick memo | **Pass.** No web calls; fake cite marked NOT CHECKED and not relied on; all sections present; 895 words of prose | `tests/memo-quick.md`, `tests/trace-quick.md` |
| Intermediate memo, "quick-verified" | **Pass.** 5 of 8 searches; fake cite marked NOT FOUND (the cited page holds Ohio entries); all sections present; about 880 words | `tests/memo-intermediate.md`, `tests/trace-intermediate.md` |
| Deep memo, full verification note | **Pass.** About 27 min of the 45-min limit; 4 area subagents plus 1 verifier (22 confirmed, 3 corrected, 1 not found); fake cite NOT FOUND, listed in Bottom line, not used as support | `tests/memo-deep.md`, `tests/trace-deep.md` |
| State mismatch (IN-law contract, a move to SC planned) | **Pass**, run live with Grant on 2026-10-20. Jeeves pre-filled from the document, asked one round of state questions (work, home, employer, events, counsel), found no override statute, and recommended **Indiana primary, SC backup** with reasons and a 4-row differences table. It flagged **Uncertain** (planned move, signed in SC), and held research until Grant confirmed ("Indiana with SC backup notes"). Grant gave his real-world goal and facts, which are kept out of this public repo. | `fixtures/mismatch-contract.md` |
| Attorney finder, 4 locations | **Pending.** Needs Grant for license checks; no "Jeeves Location" Shortcut yet, so live location uses the IP fallback | n/a |

## Gaps the tests found, all fixed on skill/v1
- State confirmation assumed a backup state, so it now has a no-backup variant (8233b59).
- "Legal deadline" is now defined; an offer sign-by date isn't one (8233b59).
- The word count is now defined, and NOT CHECKED was added to the source statuses (8233b59).
- The intermediate fan-out trigger was too eager; it's now 3+ areas (8233b59).
- The `as_of` change search is skipped when the files are under 30 days old (8233b59).
- Searching authority names quoted in the input is allowed (8233b59).
- Deep subagents no longer use the research skill, which nests an agent. Federal law goes with each area (f09147b).
- The local statute library is now step 0. There's an explicit NOT FOUND procedure that never calls a real case fake because a tool failed (f09147b).
