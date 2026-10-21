# Regression suite for the fixtures
Type: task
Status: claimed
Blocked by:

## Question

Turn the done-when tests from [19](19-test-skill.md) into a suite that can be re-run, using fictional fixtures only:
- quick and intermediate memos on `fixtures/sample-offer-letter.md`;
- the planted fake citation in `fixtures/offer-letter-with-citation.md`;
- the state-mismatch flow on `fixtures/mismatch-contract.md`;
- the PDF fixtures from [24](24-pdf-input.md).

A run fails when a memo:
- loses a template section;
- falls outside the 600–900 word count;
- misses the NOT FOUND or NOT CHECKED marking on the fake citation;
- skips the state confirmation.

Then wire the suite into the twice-yearly refresh from [26](26-update-cadence.md)/[28](28-build-update-cadence.md): the refresh runs it before opening its PR, and puts the result in the PR body.

Done when the suite runs with one command and passes on main, fails on a deliberately broken copy, and the refresh task runs it.
