# Approve and deploy
Type: task
Status: open
Blocked by: 19

## Question

Show Grant the tested result and wait for his go. Then install the symlink, confirm `/ask-jeeves` is invocable, commit to claude-global-settings, and list open items in the map.

**Updated 2026-10-20 (Grant: use gkistlergit/ask-jeeves as the skill's saved location).** Deploy means:
1. Merge the skill PR in `gkistlergit/ask-jeeves`, which puts `skills/ask-jeeves/` on main.
2. In `claude-global-settings`, open a PR that adds `"ask-jeeves": {"repo": "gkistlergit/ask-jeeves", "sha": "<merged commit>", "path": "skills", "skills": ["ask-jeeves"], "patches": false, "claudeAi": false}` to `skillPackages` and deletes `skills/ask-jeeves/` (the placeholder and the old resilience copy).
3. Merge it, then run the repo's install so `~/.claude/skills/ask-jeeves` points at `vendor/ask-jeeves/skills/ask-jeeves` at the pinned commit.
4. Confirm `/ask-jeeves` resolves.
