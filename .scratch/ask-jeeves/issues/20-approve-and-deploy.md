# Approve and deploy
Type: task
Status: resolved
Blocked by: 19, 23, 24

## Question

Show Grant the tested result and wait for his go. Then install the symlink, confirm `/ask-jeeves` is invocable, commit to claude-global-settings, and list open items in the map.

**Updated 2026-10-20 (Grant: use gkistlergit/ask-jeeves as the skill's saved location).** Deploy means:
1. Merge the skill PR in `gkistlergit/ask-jeeves`, which puts `skills/ask-jeeves/` on main.
2. In `claude-global-settings`, open a PR that adds `"ask-jeeves": {"repo": "gkistlergit/ask-jeeves", "sha": "<merged commit>", "path": "skills", "skills": ["ask-jeeves"], "patches": false, "claudeAi": false}` to `skillPackages` and deletes `skills/ask-jeeves/` (the placeholder and the old resilience copy).
3. Merge it, then run the repo's install so `~/.claude/skills/ask-jeeves` points at `vendor/ask-jeeves/skills/ask-jeeves` at the pinned commit.
4. Confirm `/ask-jeeves` resolves.

## Answer

Deployed 2026-10-20 under Grant's standing merge-and-deploy go, after tickets 19, 23 and 24 resolved.
1. Merged gkistlergit/ask-jeeves#1 at the verified head `2dbba99`. Merge commit `355f95d`.
2. Merged gkistlergit/claude-global-settings#60 (`d312235`). It adds `ask-jeeves` to `skillPackages`, pinned to `355f95d` with path `skills`, and deletes the `skills/ask-jeeves/` placeholder. `tests/settings/run.sh` passed: 70 passed, 0 failed.
3. Installed one package only, because a full `harness install` step 6 would delete the unmanaged `~/.claude/skills/contract-drafter`, and Grant chose the one-package route. The install did the installer's own fetch into `vendor/ask-jeeves` (shallow fetch of `355f95d`, detached) and relinked only `~/.claude/skills/ask-jeeves` to `vendor/ask-jeeves/skills/ask-jeeves`. A later full install sees the pin and skips the fetch.
4. `harness drift` reports every managed symlink pointing into the repo. Its one drift item is `contract-drafter`, which was unmanaged before this deploy. The link resolves to the pinned `SKILL.md`, which has `name: ask-jeeves`. Running `/ask-jeeves` in a fresh session was not tried, because skills load at session start.

Open items: [Attorney-finder recency rule](25-attorney-finder-recency.md); [Remaining state codes: find a way to download them](22-manual-state-codes.md), now unblocked; the fog in the map.
