# Regression suite (ticket 30)

Re-runs the ticket 19 done-when tests on the fictional fixtures, so a skill change or a reference refresh that breaks a memo fails before its PR merges.

```bash
python3 tests/regression/run.py
```

It takes about 25–35 minutes with 4 cases at a time, and exits 0 only when every check passes. A failed case re-runs once (`--retries`); the report shows a case that passed on retry with its first failure, so a flaky check stays visible. `report.md` in the output folder holds the summary table that goes in a refresh PR body.

## What it runs

Each case runs the skill headless with `claude -p "/jeeves-under-test …"`. `run.py` copies `skills/ask-jeeves` from the checkout under test into a sandbox under that name, so the installed `ask-jeeves` pin is never the one tested. Arguments set mode, depth, goal and input. An appended system prompt makes every question print as `QUESTION:` / `OPTIONS:` and takes its `SCRIPTED ANSWER:` from the case's list, because `claude -p` has no AskUserQuestion. It also tells the run to ask every question the skill requires, even one an argument seems to answer. Interactively, AskUserQuestion forces that pause; headless, a run once skipped step 3 when the state was passed as an argument. The reminder names no step, so a skill that drops a question still fails.

| Case | Fixture | Depth | Also checks |
|---|---|---|---|
| `offer-quick` | `sample-offer-letter.md` | quick | no web calls |
| `offer-intermediate` | `sample-offer-letter.md` | intermediate | at least 1 web call, at most 8 WebSearch |
| `citation-quick` | `offer-letter-with-citation.md` | quick | planted case marked NOT CHECKED |
| `citation-intermediate` | `offer-letter-with-citation.md` | intermediate | planted case marked NOT FOUND, never cited bare, listed in Bottom line |
| `mismatch-quick` | `mismatch-contract.md` | quick | primary and backup are IN and SC, Confidence Uncertain |
| `pdf-scanned-quick` | `scanned-contract.pdf` | quick | read through `scripts/pdf-text.swift`; mismatch checks |
| `pdf-encrypted-quick` | `encrypted-contract.pdf` | quick | read through `scripts/pdf-text.swift`, or by Read when Read opens it (it has an empty user password); mismatch checks |

Every case also checks the memo against `templates/memo.md`: every section in order, the disclaimer, the header lines with depth and label, the Bottom line goal verdict, the three Recommendation groups, the Creative option labels, at most 6 risks, the verification ending, and 600–900 words of prose. It also fails a case whose planted citation shows up bare in a run of support cites, and checks that the state confirmation (candidate block, then `OPTIONS: Confirm …`, then the answer) comes before any research that depends on the state: a WebSearch, WebFetch or subagent call, or a read of a state card. Headless runs often load the built-in area files before step 3; those hold federal, IN and SC law whichever state is picked, so reading them early doesn't count. The memo's Mode line must then use the confirmed state, and keep the backup when the answer kept one.

Free checks run first and need no model:
- `templates/memo.md` still has the sections pinned in `checks.py`. When the template changes on purpose, update `EXPECTED_SECTIONS` too.
- `pdf-text.swift` reads both PDF fixtures, word for word, as `mismatch-contract.md`.
- no file in `skills/ask-jeeves/` names the planted case, which would tell runs it's fake.
- the checker passes the ticket 19 memos in `tests/` and fails broken copies of them.

## Options

- `--cases offer-quick,citation-quick` runs a subset. `--jobs N` sets how many run at once. `--retries 0` turns off the re-run.
- `--repo <path>` tests another checkout, such as a refresh worktree or a deliberately broken copy.
- `--check-only <out folder>` re-checks saved traces without running the model.
- `--preflight-only` runs only the free checks, in about 5 seconds.

## Free to run, and safe

- Runs use the signed-in Claude account. `run.py` removes `ANTHROPIC_API_KEY` from each run's environment. The `cost_usd` figure in a trace is the list-price estimate Claude Code reports, not a charge. Intermediate cases use WebSearch and WebFetch; PDFs use local `swift` and `tesseract`.
- A full run is about 7–10 model runs, 25–35 minutes of the account's usage. When the account hits a usage limit, the case reads **NOT RUN** and the suite stops without retrying. A refresh PR then waits for Grant, the same as a failing suite.
- The fixtures and scripted answers are fictional. Keep them that way: this repo is public.
- Runs may not use Write or Edit, and the harness tells them to skip the run log and refresh queue. A case fails if any tool call other than Read names `~/.claude/ask-jeeves-run-log.md` or `~/.claude/ask-jeeves-refresh-queue.md`; the suite never rewrites those files itself, since a real Jeeves run may be logging at the same time.

## Word count

`checks.py` counts prose as the template defines it, and also drops citation brackets, bold labels, `(#n)` risk references and list markers. That runs about 15% under a plain `wc` of the same lines (the ticket 19 quick memo: 895 by the run's own count, 754 here), so a memo that just fits the cap by its own count never fails here, and one that ignores the cap still does.
