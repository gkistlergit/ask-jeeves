# Regression suite for the fixtures
Type: task
Status: resolved
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

## Answer

Built and live 2026-10-20. ask-jeeves#8 merged (`a0929b2`), claude-global-settings#77 pins it, and `vendor/ask-jeeves` is reinstalled at that sha. Usage-limit handling is in a follow-up PR.

- **One command:** `python3 tests/regression/run.py` (`tests/regression/README.md`). Each case runs the skill headless with `claude -p`, as `/jeeves-under-test`, copied from the checkout under test. The run uses the signed-in account and no API key. Questions print as `QUESTION:` / `OPTIONS:`, and each answer comes from a scripted `SCRIPTED ANSWER:` list of fictional fixture facts.
- **Cases:** quick and intermediate on `sample-offer-letter.md`, and the same on `offer-letter-with-citation.md`. The mismatch flow at quick, plus the scanned and encrypted PDFs.
- **Checks:**
  - every template section, in order, with its required labels;
  - 600–900 words of prose (`checks.py` counts conservatively);
  - the planted cite marked NOT CHECKED at quick and NOT FOUND at intermediate, and never bare in a run of support cites;
  - the candidate block, the confirmation question and its answer, all before any state-dependent research (web, subagent, state card);
  - the memo using the confirmed state;
  - for the mismatch cases, IN and SC as primary and backup with Confidence Uncertain;
  - no tool call that writes the run log or the refresh queue.
- **Free checks first:**
  - template drift against the pinned sections;
  - `pdf-text.swift` on both PDFs, word for word against `mismatch-contract.md`;
  - a guard that the skill never names the planted cite;
  - a checker self-test on the ticket 19 memos and broken copies of them.
- **Retries:** a failed case re-runs once, and the report keeps the first failure. A usage-limit error reads NOT RUN and stops the suite.
- **Results:**
  - The branch passed all 7 cases and all 5 free checks. Model runs were on `1bee042`, whose skill, fixtures and docs match `a0929b2`; the final checker re-checked them.
  - A broken copy failed `citation-quick`. Its SKILL.md drops the step 3 confirmation, labels no quick cites, omits Creative option and caps prose near 300 words. The run lost the Creative option section, and planted cite [7] appeared bare twice.
  - A fresh run on `a0929b2` hit the account's usage limit on every case, so it tested nothing. Re-run it once usage resets.
- **Gaps the first runs found, fixed in #8:**
  - Headless memos ran 990–1,030 words: new `scripts/prose-words.py`, run from SKILL.md step 5.
  - Runs listed the planted cite among support cites: the template gains `[n, NOT CHECKED]` and a no-support-run rule.
  - `research-resilience.md` §6 named the planted cite as its example, which told runs it was fake: the example is now generic.
  - One run skipped step 3 when the state came as an argument: the harness now says to ask every required question.
- **Refresh wiring:** `docs/refresh-procedure.md` step 5 runs the suite before every refresh or state-card PR and pastes `report.md` into the body. A suite that fails or doesn't run never merges under the standing go. Steps 6–9 are renumbered. All three scheduled-task prompts now say so; the January prompt also covers state cards now, closing ticket 29's gap.
- **Cost:** a full run is about 7–10 model runs, 25–35 minutes of the account's usage. Claude Code's list-price estimate is about $5–6 per quick case. Today's build ran about 22 model runs and hit the usage limit. Whether that's acceptable usage for each refresh is Grant's call.

