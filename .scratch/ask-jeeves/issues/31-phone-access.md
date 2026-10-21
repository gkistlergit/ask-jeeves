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
