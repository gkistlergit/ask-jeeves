# Build state cards and the run log
Type: task
Status: claimed
Blocked by: 28

## Question

Build what [27](27-other-state-references.md) decided:
- **SKILL.md step 6:** append the run-log line (applied state and backup, date, depth) to `~/.claude/ask-jeeves-run-log.md`. When a non-IN/SC state reaches 3 runs, say so and queue "build state card <ST>" in `~/.claude/ask-jeeves-refresh-queue.md`.
- **Template** `references/state-cards/<ST>.md`: statutes with `Sources/` pointers, 3–6 leading cases per field, `as_of` and `verified` frontmatter, and a "Changes since last as-of" section.
- **Quick mode:** cover a state that has a card, labeled "slim state card".
- **Refresh tasks from 28:** handle a "build state card" queue item (deep research plus the verifier, then a PR that waits for Grant's review), and include existing cards in the twice-yearly refresh.

This waits on 28 because it edits the same SKILL.md steps and the same scheduled tasks.

Done when a dry run on a fictional request logs the run correctly, a third logged run of a fixture state queues a card, and the quick-mode label is checked on a sample card. Clean up the sample card and the test log entries afterwards.
