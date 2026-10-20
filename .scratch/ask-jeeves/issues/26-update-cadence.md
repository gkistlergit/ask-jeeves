# Reference-file update cadence
Type: grilling
Status: open
Blocked by:

## Question

How, and how often, should Jeeves's built-in reference files be refreshed, and how should the skill report their age?

What exists today:
- Each file in `skills/ask-jeeves/references/` carries `as_of` and `verified` frontmatter, and the memo prints the oldest as-of date ([08](08-skill-structure.md)). Quick mode labels its memo unverified with that date ([10](10-depth-modes.md)).
- A scheduled task, `ask-jeeves-annual-code-refresh` (July 15), lists stale editions in the local statute library `Sources/` and short-list states with no local copy (`Sources/README.md`). It does not touch the reference files themselves.
- Research tickets 01–04 show what moved in 2025–26: the FTC non-compete rule's removal, NLRB GC memos, new state non-compete statutes (IN SEA 475, many others in [04](04-choice-of-law-and-state-survey.md)), arbitration case law and EFAA splits. State legislative changes cluster at each session's effective dates (often July 1 and January 1).

Decide, per file or per area:
1. **Cadence:** a fixed schedule (for example quarterly, or after each July 1 and January 1), triggered (when a run finds a law change newer than `as_of`), or both.
2. **Who runs it:** a scheduled task that re-runs the deep research and verifier and opens a PR, or a reminder that Grant starts by hand. It must stay free to run: no paid APIs.
3. **Staleness rule in the skill:** at what age a reference file stops being used without a live check (for example older than 6 or 12 months), and what the memo says when that happens.
4. **Change log:** whether a refresh records what changed since the last `as_of`, and where.

Recommendation to grill: twice-yearly refreshes after the July 1 and January 1 effective dates; a run that finds a newer law change flags the reference file as stale in the memo; references older than 12 months are treated as leads only, as in intermediate mode.
