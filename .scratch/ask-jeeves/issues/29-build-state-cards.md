# Build state cards and the run log
Type: task
Status: resolved
Blocked by: 28

## Question

Build what [27](27-other-state-references.md) decided:
- **SKILL.md step 6:** append the run-log line (applied state and backup, date, depth) to `~/.claude/ask-jeeves-run-log.md`. When a non-IN/SC state reaches 3 runs, say so and queue "build state card <ST>" in `~/.claude/ask-jeeves-refresh-queue.md`.
- **Template** `references/state-cards/<ST>.md`: statutes with `Sources/` pointers, 3–6 leading cases per field, `as_of` and `verified` frontmatter, and a "Changes since last as-of" section.
- **Quick mode:** cover a state that has a card, labeled "slim state card".
- **Refresh tasks from 28:** handle a "build state card" queue item (deep research plus the verifier, then a PR that waits for Grant's review), and include existing cards in the twice-yearly refresh.

This waits on 28 because it edits the same SKILL.md steps and the same scheduled tasks.

Done when a dry run on a fictional request logs the run correctly, a third logged run of a fixture state queues a card, and the quick-mode label is checked on a sample card. Clean up the sample card and the test log entries afterwards.

## Answer

Built and live 2026-10-20: ask-jeeves#5 merged (`e113745`), pinned by claude-global-settings#70, and `vendor/ask-jeeves` reinstalled at that sha.

- **Run log** (SKILL.md step 6): each delivered memo appends `- <date> | <applied ST> | backup <ST or none> | <depth>` to `~/.claude/ask-jeeves-run-log.md`. Nothing else from the request goes in, and a request routed straight to the attorney finder isn't logged.
- **3-run trigger:** a state other than IN or SC that appears in 3 or more log lines (as applied or backup, this run included) gets a one-line notice and a `build state card <ST>` line in the refresh queue. This is skipped if the card exists or is already queued. Grant can ask for a card at any time.
- **Template:** `references/state-cards/_template.md`. Files starting with `_` are never loaded or refreshed.
- **Quick mode:** covers a state from its card. The label adds `; slim state card`, and the ending names the card, its `as_of` and what's not on it (`templates/memo.md`). Cards fall under the 12-month rule.
- **Refresh:** `docs/refresh-procedure.md` puts cards in the twice-yearly full run. A new section, "Building a state card", builds a queued card with three flat research subagents and one verifier into its own `state-card/<ST>` PR, which always waits for Grant. The weekly and July task prompts say so. The January task prompt wasn't updated (auto mode denied the edit). Its run still covers cards, because the procedure's step 1 now includes them.
- **Dry runs** (scratch copy, log and queue redirected to scratch, fictional fixtures, no web calls): a quick Denver request with a sample CO card logged `- 2026-10-20 | CO | backup none | quick` with the `slim state card` label and ending. A third logged OR run queued `build state card OR` with the one-line notice, and a fourth didn't queue it again. The sample card and test files were deleted. The real run log doesn't exist yet, and the queue is empty.

