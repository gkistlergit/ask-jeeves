# Use Jeeves from Grant's phone
Type: task
Status: claimed
Blocked by:

## Question

Grant wants Jeeves to work from his phone (2026-10-20). Two routes. Build both, then say which is the default:
1. **Full Jeeves, driven from the phone.** Grant runs it in a Claude Code session on his Mac and drives that session from his phone: Remote Control, or claude.ai/code. The statute library, the scripts, the run log and the refresh queue all stay on the Mac. Live location from the Mac app gives the Mac's location, not the phone's. On the phone, use a typed ZIP, or have Grant type the city the phone shows. Document the steps and test one run from the phone.
2. **Quick Jeeves in claude.ai chat** (phone app). Package the skill for claude.ai through the claude-global-settings `claudeAi` flag and `harness build-zips`. It covers quick mode only, with the built-in references and state cards:
   - no `Sources/`, scripts, run log or refresh queue;
   - typed location only;
   - an attorney finder that uses web search only if chat allows it.

   SKILL.md has to detect that environment and say what's missing, rather than fail.

Never put Grant's personal facts in the zip. It is built from the public repo.

Done when a quick memo and an attorney-finder run both work from the phone through each route, or a route is shown not to work, with the reason recorded.

## Answer

Repo side built and live 2026-10-20: ask-jeeves#7 merged (`54eda44`), pinned with `claudeAi: true` by claude-global-settings#74 (`d766748`), and `vendor/ask-jeeves` reinstalled at that sha. How-to: `docs/phone.md`.

**Default: route 1** whenever the Mac is on. It's the full skill. Route 2 is the fallback for a quick memo when the Mac is off or out of reach.

- **Route 1, full Jeeves driven from the phone.** On the Mac: `cd ~ && caffeinate -i claude remote-control --name jeeves` (the desktop app's per-session Remote Control works too). On the phone: Claude app → Code → `jeeves`, then `/ask-jeeves`. The statute library, scripts, run log and refresh queue stay on the Mac. Live location reads the Mac, so SKILL.md step 7 and the attorney-finder consent step now say so and offer a typed ZIP or the city the phone shows. Documents: paste the text, or save to iCloud Drive and give the Mac path.
- **Route 2, chat Jeeves in claude.ai.** SKILL.md now checks where it runs before step 1. Full Jeeves means a shell with `uname -s` = `Darwin` and `~/.claude/` present. Anything else, including claude.ai's Linux code sandbox, is chat Jeeves: quick only, built-in references and state cards, plain-chat questions, typed locations only, no run log, refresh queue, `reading-input.md` or contract-drafter leads, and one opening line saying what it can't do. The attorney finder runs inline with the chat's web search, or gives the bar referral and legal-aid routes when search is off.
- **Zip:** `harness build-zips` writes `~/Developer/claude-global-settings/build/claude-ai/ask-jeeves.zip`: 134 KB, 19 files, the skill folder only (SKILL.md, references, state-card template, memo template, the Mac-only scripts). No `Sources/`. Frontmatter rewritten for claude.ai (`disable-model-invocation` dropped, "Only use when the user explicitly asks for this skill by name." appended). The only personal fact is the home city and ZIP, Noblesville, IN 46060, which this repo's CLAUDE.md already allows in public. No employer, email or street address.

**Phone tests (Grant), pending:**
- [ ] Route 1: quick memo from the phone over Remote Control: `/ask-jeeves` runs and the questions render on the phone.
- [ ] Route 1: attorney finder with a typed ZIP.
- [x] Route 2: upload the zip on claude.ai, then from the phone app ask for ask-jeeves: it says it's chat Jeeves and writes a quick memo. Grant, 2026-10-20: zip uploaded, and chat Jeeves wrote a quick memo. (He didn't say which device he used, or whether it opened with the chat Jeeves line.)
- [ ] Route 2: attorney finder with web search on in that chat.
