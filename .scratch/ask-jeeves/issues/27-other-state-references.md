# Built-in references for other states
Type: grilling
Status: claimed
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
