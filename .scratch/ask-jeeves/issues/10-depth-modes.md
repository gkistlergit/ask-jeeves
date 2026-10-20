# Depth modes
Type: grilling
Status: resolved
Blocked by: 08

## Question

What exactly do quick, intermediate and deep each do: sources, number of searches, subagents, time and token budget, and the default when no depth is picked (brief: intermediate)? What does quick say about how current its reference files are?

Carried from [Skill structure and request flow](08-skill-structure.md): intermediate may dispatch subagents when necessary. Define the trigger (for example, more than N sources to open, or more than one legal area touched).

## Answer

Resolved 2026-10-20. Grant accepted the recommendations ("go for recs on tickets 10, 12 and 15").

| | Quick | Intermediate (default) | Deep |
|---|---|---|---|
| **Sources** | Built-in reference files only. No web. | Reference files, plus web checks for changes since each file's `as_of`, plus spot-checks of key claims | Fresh multi-source research per legal area, with primary sources preferred |
| **Searches** | 0 | About 5–8 WebSearch calls, and WebFetch of every cited source | No fixed cap. Each area subagent searches until its question is covered. |
| **Subagents** | None | Main thread by default. **Trigger:** dispatch one subagent per legal area when the request touches 2 or more legal areas **and** needs more than 8 sources opened, or when the applied state has no built-in reference file. | One research subagent per legal area touched (each using the research skill), then **one separate verifier subagent** that re-opens every citation |
| **Rough time** | 1–2 min | 5–10 min | 20–45 min |
| **Label** | "Unverified against current sources. Reference files current as of <oldest as_of>." | "Quick-verified" plus a one-line count (N confirmed, M marked unverified) | A full verification note (ticket 11) |

- **Quick and states without built-in files:** quick can't cover a state with no reference file. The skill says so and offers intermediate or deep. It never quietly fills the gap from memory.
- **Quick never cites** anything that isn't in a reference file.
- **Default:** intermediate when no depth is picked (from the brief).
- **Search limit hit:** fall back to direct WebFetch of official URLs. Anything still unchecked is marked [UNVERIFIED], and the label or verification note says the search limit was hit.
- **Budget:** no hard token cap. Deep warns up front that it takes 20–45 minutes.
- Staleness warnings on old reference files stay in the update-cadence fog.
