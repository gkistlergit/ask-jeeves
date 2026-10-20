# Built-in references for other states
Type: grilling
Status: resolved
Blocked by:

## Question

Should any state beyond Indiana and South Carolina get built-in, deep-verified reference files? If so, which states, and what decides it?

What exists today:
- Built-in references cover federal, IN and SC on the three priority fields. Other states are researched live at the chosen depth; quick mode can't cover them ([10](10-depth-modes.md)).
- The 50-state covenant survey in [04](04-choice-of-law-and-state-survey.md) (Part B) is a flagging aid only. AL, AK, GA and MS rows are UNVERIFIED.
- Since [22](22-manual-state-codes.md), the local statute library `Sources/` holds official employment-law text for 45 states plus DC, so live research can read most state statutes offline. That covers statute text only, not case law or the analysis a reference file carries.
- There is no usage data yet beyond the [19](19-test-skill.md) test runs.

Decide:
1. **Trigger:** add a state when Grant asks, when a state comes up in N real runs, or never (live research only).
2. **Scope per state:** a full reference file on all three fields, or a slim file (statute cites and as-of only) that leans on `Sources/`.
3. **Candidates now:** states likely to matter, such as neighbors of IN (IL, OH, MI, KY) or states with active non-compete law (CA, MN, NY), or none until usage shows a need.
4. **Upkeep:** each added state joins the refresh schedule decided in [26](26-update-cadence.md), so more states mean more refresh work.

Recommendation to grill: no new built-in states yet. Log the state of each real run, and revisit when one state appears in 3 or more runs; until then, live research plus `Sources/` covers other states.

## Answer

Grant took every recommendation (2026-10-20). To be built in [Build state cards and the run log](29-build-state-cards.md).

1. **Trigger: Grant's ask or 3 runs, whichever comes first.** At delivery, Jeeves appends one line per run to `~/.claude/ask-jeeves-run-log.md`, outside the public repo: the applied state (and backup), the date and the depth. Nothing else from the request goes in. When a state other than IN or SC reaches 3 runs, Jeeves says so in one line and adds "build state card <ST>" to the refresh queue from [26](26-update-cadence.md).
2. **Scope: a slim state card,** not a full reference file. It holds:
   - the key statutes, with pointers into `Sources/`;
   - the 3–6 leading cases on restrictive covenants, IP assignment and wage payment;
   - `as_of` and `verified` frontmatter.

   Each card is deep-researched and verified once. Quick mode can then cover that state, labeled "slim state card". A state is upgraded to a full reference file at about 10 runs, which becomes a new decision for Grant at that point.
3. **States now: none.** Indiana law governs Grant's agreement, SC covers the move, and no run has needed another state. California was raised, because it voids most non-competes, and was not added.
4. **Upkeep:** every state card joins the twice-yearly refresh and the 12-month staleness rule from 26. Card changes follow the same fix-vs-substance split for approval.
