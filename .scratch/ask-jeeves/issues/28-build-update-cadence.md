# Build the reference update cadence
Type: task
Status: claimed
Blocked by: 26

## Question

Build what [26](26-update-cadence.md) decided. Work on a branch, open a PR, and ship it under Grant's standing merge-and-deploy go once the checks pass.

1. **Skill (`skills/ask-jeeves/`):**
   - Staleness rule: a reference file or `Sources/` edition older than 12 months. Quick mode adds "reference may be out of date" to the memo; intermediate and deep treat it as leads only and check every point live. Update `SKILL.md` and `references/research-resilience.md`.
   - When a run finds a law change newer than a file's `as_of`: flag it in the verification line and append a dated line (file, change, source URL) to `~/.claude/ask-jeeves-refresh-queue.md`. No party names or input text in the queue.
2. **Change log:** add an empty "Changes since last as-of" section to the end of each reference file that has `as_of`.
3. **Refresh procedure:** one written procedure (for example `references/refresh.md` or a repo `docs/` page) that a scheduled run follows per file: deep research plus a separate verifier, each change tagged *substance* or *fix* (unsure counts as substance), the change-log section filled in, `as_of`/`verified` renewed, then a PR. A PR with only fixes may merge and deploy; a PR with any substance change waits for Grant.
4. **Scheduled tasks (free to run):**
   - Extend `ask-jeeves-annual-code-refresh` (July 15) to run the refresh procedure on every reference file, besides its `Sources/` checks.
   - Add a January 15 twin.
   - Add a weekly task that refreshes the files queued in `~/.claude/ask-jeeves-refresh-queue.md` and clears each line it handles.
   - The twice-yearly tasks re-download `Sources/` editions they can reach and list hand-download states (IN, and the skipped states in [22](22-manual-state-codes.md)) for Grant.

Done when: the PR is merged and deployed, the three tasks are listed in the app, a dry run of the weekly task on a test queue line opens a fix-only PR (or reports nothing to change), and quick mode on a reference file back-dated by 13 months in a scratch copy shows the out-of-date label.
