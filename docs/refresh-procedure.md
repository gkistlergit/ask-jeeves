# Reference refresh procedure

Scheduled tasks follow this to keep Jeeves's reference files and local statute library current. It implements the decisions in `.scratch/ask-jeeves/issues/26-update-cadence.md`.

| Task | When | Scope |
|---|---|---|
| `ask-jeeves-annual-code-refresh` | July 15 | every reference file, plus the statute library (step 6) |
| `ask-jeeves-january-refresh` | January 15 | the same |
| `ask-jeeves-weekly-refresh-queue` | weekly | only the files listed in `~/.claude/ask-jeeves-refresh-queue.md`; does nothing when it is empty or missing |

## Rules for every run

- **Free to run.** WebSearch and WebFetch only: no paid APIs, LLM APIs or metered services.
- **Public repo.** Nothing about Grant beyond "Noblesville, IN 46060", and no party names or input text from any Jeeves run.
- **Sourcing.** Follow `skills/ask-jeeves/references/research-resilience.md`: its search budgets, fallback chain, flat subagents and no browser. Never bypass a CAPTCHA, login, bot check or robots.txt, and never touch LexisNexis portals: their terms bar agents.
- **Never work in the main checkout.** Branch from `origin/main` in a new worktree: `git -C ~/Developer/ask-jeeves fetch origin && git -C ~/Developer/ask-jeeves worktree add ../ask-jeeves-refresh-<date> -b refresh/<date> origin/main`.
- **Stop and report to Grant** when a check fails, a step is denied, or anything is hard to undo. When a push, merge or deploy is denied, give him one runnable block for that step.

## Steps

1. **Pick the files.** For a full run, every file in `skills/ask-jeeves/references/` with `as_of` frontmatter. For the weekly run, the files named in the queue, each with its queued changes.
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
7. **Clear the queue.** Once a file's PR is open, remove that file's lines from `~/.claude/ask-jeeves-refresh-queue.md`. Leave lines for files that weren't handled.
8. **Report to Grant** in at most 12 lines: the PRs and whether each went live, substance changes waiting for review, what was re-downloaded, the hand-download list, and anything that failed.
