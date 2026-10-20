# Map: ask-jeeves skill

Labels: wayfinder:map

## Destination

An `ask-jeeves` skill installed at `claude-global-settings/skills/ask-jeeves` (symlinked into `~/.claude/skills/`) and invocable as `/ask-jeeves`. It passes every done-when test in the brief: the state-selection test, three depth memos on a sample offer letter, a caught fake citation, and the attorney finder on all four location options. It is backed by dated, deep-verified federal, Indiana and South Carolina research on the three priority fields. This map records each decision and lists the open items.

## Notes

- **Execution override.** This effort carries execution through to building, testing and installing the skill. That overrides wayfinder's plan-only default. The build, test and deploy tickets (18–20) are real work, not decisions.
- **Domain:** U.S. employment law, issue-spotting only (not legal advice). Law must be current as of **October 2026**. Flag anything that changed in 2025–2026.
- **Default jurisdiction:** federal law plus Indiana until Grant confirms otherwise. Built-in reference files cover federal, Indiana and South Carolina.
- **Priority fields:** (1) insider theft of IT assets, data and trade secrets; (2) restrictive covenants (non-competes, non-solicits, confidentiality); (3) employee contracts. "Insider theft" means employees or insiders taking trade secrets or data, not stolen devices or outside hacking.
- **Deep verification standard applies to design research.** Every source, case, statute and regulation is opened and confirmed real, and each claim is checked against it. Primary and authoritative sources are preferred, weak ones are flagged, and conflicts are noted. Anything unconfirmed is removed or marked UNVERIFIED. Each research file ends with a verification note. A separate verifier agent re-opens every source after the research agent finishes.
- **Quotes under 15 words.** Write page references as "pg. N".
- **HITL stops:** every grilling and prototype ticket goes to Grant, who answers for himself. Other stops: the pre-build summary (17) and the pre-deploy go (20). Research tickets run AFK.
- **Privacy:** this repo is **public**. Grant's home street address never appears in this repo, in URLs or in public queries. Searches use the city or ZIP only (Noblesville, IN 46060). The skill itself lives in the private `claude-global-settings` repo.
- **Free to run:** no paid APIs or metered services. Use web search and fetch only.
- **Prior research:** `~/Developer/ai-solutions-llc-research-indiana-ip-law` and `~/Developer/ai-solutions-llc-research-attorney-shortlist` may be used as leads only. Re-verify everything and copy nothing in unverified.
- **Research record:** findings live in `research/` on main, kept as the design record. This overrides wayfinder's throwaway-branch default because Grant asked to keep the research files.
- **Skills to consult:** grilling and domain-modeling on HITL tickets, research on research tickets, prototype on the memo ticket, writing-for-agents and superpowers:writing-skills when building.
- **Glossary:** `CONTEXT.md`.

## Decisions so far

- Charting round: the skill is named `ask-jeeves`. It installs in `claude-global-settings/skills` with a symlink. The map and research live in `gkistlergit/ask-jeeves`. Prior research is used as leads only. Destination and execution override confirmed. Free-to-run confirmed.

## Not yet specified

- **Update cadence.** How and how often the reference files are refreshed, and how the skill reports their age. This depends on how the reference files are laid out (08) and what changes fastest (01–04).
- **Other states.** Whether any state beyond IN and SC gets built-in reference files (depends on 04 and on usage).
- **claude.ai chat availability.** Whether to also package a zip for claude.ai or Desktop chat.
- **Test-case growth.** Whether the fixtures become a re-runnable regression suite.

## Out of scope

- Advice on a live legal matter, litigation strategy, and contacting or hiring an attorney on Grant's behalf (brief: boundaries).
- Stolen devices and outside hacking (brief: "IT theft" default).
