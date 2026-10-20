# Test the skill
Type: task
Status: resolved
Blocked by: 18

## Question

Run the done-when tests: the contract-state versus work-state mismatch, the sample offer letter at all three depths, the planted fake citation at intermediate and deep, and the attorney finder on all four locations including the mismatch flag. Record the results in `fixtures/` and `research/test-results.md`.

## Progress (2026-10-20)

Still claimed. All tests except the attorney finder have passed; details are in `research/test-results.md`.

- **Deep depth of the state-mismatch test: passed.** It ran on Grant's real goal, with the real agreement as input, and his facts stay out of this repo. 4 area subagents plus 1 verifier checked 36 sources: 33 confirmed, 3 corrected, 0 unverified, 0 not found. The memo has 880 words of prose, and the humanizer pass was done.
- **Attorney finder: 1 of 4 locations run** (Home). It used 8 of 8 searches and found 0 who qualify. Jeeves said so, gave the Indiana budget routes, and listed the near-misses with reasons, without lowering the bar. Still to run:
  - Aiken, SC, including the mismatch question (IN vs SC license);
  - a typed ZIP;
  - live location. No "Jeeves Location" Shortcut exists yet, so this goes to consent and then the IP fallback.
- **New gaps, ticketed:** [Input document changes mid-run](23-input-changes-mid-run.md) and [Scanned and encrypted PDF input](24-pdf-input.md).

Done when: the three remaining locations have each run, with results in `research/test-results.md`. Then set `Status: resolved` and add the context pointer to the map.

## Answer

All done-when tests pass (2026-10-20). Details are in `research/test-results.md`.
- **Memos:** quick, intermediate and deep each passed. The planted fake citation was caught at intermediate and deep.
- **State mismatch:** passed live, including a deep run on Grant's real goal.
- **Attorney finder:** all four location options ran.
  - Home, Aiken and live location each found 0 who qualify. Each run reported that honestly, with budget routes and near-misses.
  - The Aiken mismatch flag and question worked.
  - Typed entry resolved with no network call.
  - Live location now uses the bundled Jeeves Location app (skill/v1 2dbba99), which replaced the untested Shortcut design from [Live device location: what tool exists](07-live-location-tool.md).

Gaps found during testing were fixed:
- [Input document changes mid-run](23-input-changes-mid-run.md)
- [Scanned and encrypted PDF input](24-pdf-input.md)
- the location app

Open for Grant, not blocking deploy: [Attorney-finder recency rule](25-attorney-finder-recency.md).
