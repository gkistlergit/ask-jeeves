# Reference refresh procedure

Scheduled tasks follow this to keep Jeeves's reference files, state cards and local statute library current, and to build queued state cards. It implements the decisions in `.scratch/ask-jeeves/issues/26-update-cadence.md` and `27-other-state-references.md`.

| Task | When | Scope |
|---|---|---|
| `ask-jeeves-annual-code-refresh` | July 15 | every reference file and state card, plus the statute library (step 6) |
| `ask-jeeves-january-refresh` | January 15 | the same |
| `ask-jeeves-weekly-refresh-queue` | weekly | only the files listed in `~/.claude/ask-jeeves-refresh-queue.md`, and any `build state card <ST>` lines there (see "Building a state card"); does nothing when it is empty or missing |

## Rules for every run

- **Free to run.** WebSearch and WebFetch only: no paid APIs, LLM APIs or metered services.
- **Public repo.** Nothing about Grant beyond "Noblesville, IN 46060", and no party names or input text from any Jeeves run.
- **Sourcing.** Follow `skills/ask-jeeves/references/research-resilience.md`: its search budgets, fallback chain, flat subagents and no browser. Never bypass a CAPTCHA, login, bot check or robots.txt, and never touch LexisNexis portals: their terms bar agents.
- **Never work in the main checkout.** Branch from `origin/main` in a new worktree: `git -C ~/Developer/ask-jeeves fetch origin && git -C ~/Developer/ask-jeeves worktree add ../ask-jeeves-refresh-<date> -b refresh/<date> origin/main`.
- **Stop and report to Grant** when a check fails, a step is denied, or anything is hard to undo. When a push, merge or deploy is denied, give him one runnable block for that step.

## Steps

1. **Pick the files.** For a full run, every file in `skills/ask-jeeves/references/` and `skills/ask-jeeves/references/state-cards/` with `as_of` frontmatter, skipping files whose names start with `_`. For the weekly run, the files named in the queue, each with its queued changes. A `build state card <ST>` line is not a refresh: handle it by "Building a state card" below.
2. **Research each file.** Dispatch one deep research subagent per file, all flat. Each one checks the file's authorities for changes after its `as_of` (new statutes, amendments, repeals, rules, controlling decisions), plus any queued change, at most 6 searches. When all have returned, dispatch **one** verifier subagent that re-opens, with WebFetch, every source behind a proposed change.
3. **Tag each change.**
   - *Substance:* a change to what a rule says, a holding, the date a law takes effect, a risk or likelihood rating, or an authority added or removed.
   - *Fix:* a renewed date, a URL, citation format, the "pg. N" style, a typo.
   - Anything the verifier is unsure about counts as substance.
4. **Edit the file.** Apply verified changes only. Under `## Changes since last as-of`, replace "None yet." (or add above older entries) a `### <date> refresh` block with one line per change: `- [substance|fix] <what changed> (<source URL>)`. Set `as_of` to the research date and `verified` to the verifier's date. A file that needed no change still gets its dates renewed, which is a fix.
5. **Open the PR.** Commit and push the branch, then `gh pr create --repo gkistlergit/ask-jeeves`. Title it `Reference refresh <date>: fixes only` or `Reference refresh <date>: substance, needs Grant's review`, and list every change by tag in the body.
   - **Fixes only:** merge under Grant's standing go: `gh pr merge <n> --merge --match-head-commit <verified sha>`. Then deploy:
     1. In `~/Developer/claude-global-settings`, on a new branch, run `bin/harness bump ask-jeeves`, then `tests/settings/run.sh`. Open a PR, and merge it the same way when the tests pass.
     2. Pull main, then run `bin/harness install --dry-run`. If it would change anything besides `ask-jeeves`, stop and report. Otherwise run `bin/harness install`.
     3. Check that `~/.claude/skills/ask-jeeves` resolves to the new pin.
   - **Any substance change:** leave the PR open and send Grant its link with the substance lines.
6. **Statute library (July and January runs only).** For each `Sources/MANIFEST.md` edition downloaded more than 12 months ago:
   - If its route works with curl and robots.txt allows it, re-download it by the route in `Sources/_reports/slice*.md` or ticket 22's Answer. Honor crawl delays, then run `scripts/ingest-code.sh <ST> <edition> <path>`.
   - Otherwise list it for Grant with the exact link: Indiana (iga.in.gov), Pennsylvania (browser only), and the states skipped in ticket 22 (AR, MS, TN code, OH, OK).
   - Commit `Sources/MANIFEST.md` changes with the PR. `Sources/` itself stays local.
7. **Clear the queue.** Once a file's PR is open, remove that file's lines from `~/.claude/ask-jeeves-refresh-queue.md`, a card's `build state card <ST>` line included. Leave lines for files that weren't handled.
8. **Report to Grant** in at most 12 lines: the PRs and whether each went live, substance changes and new cards waiting for review, what was re-downloaded, the hand-download list, and anything that failed.

## Building a state card

A queue line `build state card <ST>` comes from SKILL.md step 6 (a state other than IN or SC reached 3 logged runs) or from Grant asking. Build each card in its own worktree and branch, `state-card/<ST>` from `origin/main`, so a fix-only refresh PR never waits behind it.

1. **Skip it** when `skills/ask-jeeves/references/state-cards/<ST>.md` already exists on `origin/main`, or an open PR adds it. Clear the line and say so in the report.
2. **Research.** Dispatch three deep research subagents, all flat: one each for restrictive covenants, IP assignment of employee inventions, and wage payment in that state. Each finds the key statutes and the 3–6 leading cases on its field, at most 6 searches, following `research-resilience.md`. For statute text, read the state's `Sources/` edition first when `Sources/MANIFEST.md` lists one. Have one of the three also name the state's trade-secret act. Start from the state's row in `references/choice-of-law.md` Part 3 and its official code site in `references/state-codes-part1.md` or `part2.md`.
3. **Verify.** When all three have returned, dispatch **one** verifier subagent that re-opens every source with WebFetch. Drop what fails; mark what it couldn't open `[UNVERIFIED: reason]`.
4. **Write the card.** Copy `references/state-cards/_template.md` to `references/state-cards/<ST>.md` and fill it. Point a statute into `Sources/<ST>/<edition>/text/` when the edition exists, otherwise give the official URL only. Set `as_of` to the research date and `verified` to the verifier's date. Leave "Changes since last as-of" as "None yet."
5. **PR.** A new card always waits for Grant, as a substance change. Title it `State card <ST>: new, needs Grant's review`, and list each statute and case in the body with its verifier status. Never merge it under the standing go. Clear the queue line once the PR is open (step 7).

