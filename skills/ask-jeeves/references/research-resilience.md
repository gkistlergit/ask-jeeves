---
as_of: 2026-10-20
---

# Research resilience: how not to get stuck

These rules apply to every web check at intermediate and deep depth, and to the attorney finder. They come from what stalled the design research on 2026-10-20.

## 1. Web search is a scarce, shared budget

WebSearch calls count against one budget shared by the main thread and every subagent. That budget ran out several times during the design research.

- **Budget per request:** intermediate gets at most 8 searches in total. Deep gets at most 6 per area subagent, and the verifier gets 0 (it re-opens known URLs with WebFetch).
- **Fetch before you search.** When you know the authority, build its official URL and WebFetch it (see the table below). Search only to find a URL you can't build.
- **On a rate-limit or quota error:** don't retry the search. Switch to WebFetch of official URLs for the rest of the request. Mark anything still unchecked [UNVERIFIED], and state in the label or verification note that the search limit was hit.

## 2. Fallback chain per source type

**Step 0, the local statute library (statutes only).** Before any web lookup of a state statute, read `~/Developer/ask-jeeves/Sources/MANIFEST.md`. If the state has an edition there, grep its `Sources/<ST>/<edition>/text/` for the section and cite it as `<cite> (<edition> <State> Code, official download)`. Say so when the edition predates a change you found. An edition downloaded more than 12 months ago is a lead only (§7): confirm the section on the official site before citing it. The library is local and gitignored, so it may be missing on another machine; then go straight to the chain below.

Try each source once. If it's blocked, down, empty or behind a CAPTCHA, move to the next source. When the chain runs out, mark the claim [UNVERIFIED] with the reason. **Never bypass a CAPTCHA, a login or a human-verification page.**

| Authority | Try in order |
|---|---|
| U.S. Code | uscode.house.gov → law.cornell.edu/uscode → govinfo.gov |
| Federal regulations | ecfr.gov → federalregister.gov → law.cornell.edu/cfr |
| Federal agency actions | the agency's own site (ftc.gov, nlrb.gov, eeoc.gov, dol.gov, sec.gov) → federalregister.gov |
| Supreme Court / circuit opinions | supremecourt.gov or the circuit's own opinion page → case.law → Google Scholar → Justia (CourtListener often demands human verification; skip it if it does) |
| Indiana Code / acts | Step 0 first (the 2026 edition is in the library). Otherwise: iga.in.gov serves only a JavaScript shell to WebFetch and curl, and api.iga.in.gov returns 403 (checked 2026-10-20). Use, in order: (1) the reference files, which were checked against the official 2026 Indiana Code download; (2) an Indiana court opinion quoting the section, `public.courts.in.gov/Decisions/api/Document/Opinion?Id=<id>` (a PDF); (3) an in.gov agency page (DOL, DWD, AG, ICRC) quoting it; (4) FindLaw or Justia, labeled **(mirror, secondary)**. For a section changed after the reference file's `as_of`, Grant can download the current code from iga.in.gov → any title → Reference Materials → "Download the <year> Indiana Code". |
| Indiana cases | in.gov/courts opinions → case.law → Google Scholar |
| South Carolina Code / bills | scstatehouse.gov → none (mark [UNVERIFIED]) |
| South Carolina cases | sccourts.org opinions → case.law → Google Scholar |
| Other states | the legislature's own code site → the state court's opinion page → case.law |

## 3. Subagents: flat, bounded, and finished before they return

- **Flat fan-out only.** A subagent Jeeves dispatches must not dispatch subagents of its own. Nested agents handed back early during the design research, before their children reported, and left work half-done.
- **Finish before returning.** Each subagent writes its complete result, including a partial result if it ran out of budget, before it replies. It never returns with background work still running.
- **One writer per file.** No two agents edit the same file at once. The verifier starts only after every area subagent has returned.
- **Scope cap.** Give each subagent one legal area and one state, plus its search budget from §1.

## 4. No shared browser, computer-use or clipboard

Research uses WebFetch and WebSearch only. Don't drive the browser pane or computer-use, and don't touch the clipboard. During the design research a site script wrote to Grant's clipboard, and parallel agents moved each other's browser tabs. License lookups that need a browser go to Grant to open himself (see the attorney finder).

## 5. Time limits: deliver, don't hang

- Targets: quick takes 1–2 minutes, intermediate 5–10, and deep 20–45.
- If deep passes about 45 minutes, stop waiting. Deliver the memo with what is verified, list the gaps under the verification note, and offer to continue.
- When a subagent fails or returns empty, re-run that slice once in the main thread. If it fails again, mark that area's claims [UNVERIFIED] and move on.
- Tell Grant in one line which area Jeeves is on whenever a step will take more than a couple of minutes.

## 6. Calling a case NOT FOUND

A citation earns `[NOT FOUND: possibly fabricated]` only after all of these come back empty:
1. **the court's own opinion search**, for example `public.courts.in.gov/Decisions/api/Document/Opinion?Id=<id>` or the Indiana opinions search, sccourts.org opinions, or the circuit's opinion page;
2. **case.law**, which only covers older volumes. For anything reported after about 2018, its silence proves nothing;
3. **one WebSearch** for the exact reporter cite in quotes, plus one for the case name with the court and year;
4. a check that the reporter volume and page fit the stated year and court. For example, look at what the cited page actually holds: a made-up cite often lands on a real page that holds another case, or another state's entries.

Google Scholar blocks WebFetch. Use it only through WebSearch result snippets. If steps 1 to 3 can't be reached (site down, CAPTCHA, search limit hit), mark the citation `[UNVERIFIED: could not check]`, never NOT FOUND. A real case must never be called fake because the tools failed.

## 7. Age rule and the refresh queue

**12-month rule.** A reference file or state card (`references/state-cards/<ST>.md`) whose `as_of` frontmatter is more than 12 months before today (the frontmatter governs over any date in the body), or a `Sources/` edition downloaded more than 12 months ago, is **stale**. Refreshes run every mid-July and mid-January, so a stale file means a refresh was missed.
- *Quick:* still use it, but the memo's label and ending say `reference may be out of date` (`templates/memo.md`).
- *Intermediate and deep:* treat a stale file as leads only. Re-check every point you take from it on a live source, and spend searches there first. A point you can't re-check is `[n, UNVERIFIED: reference file stale]`.

**Refresh queue.** When an intermediate or deep run finds a law change dated after a reference file's `as_of` (a new statute, amendment, repeal, rule or controlling decision), flag it in the verification line (`Reference out of date: <file>, <change>`) and append one line to `~/.claude/ask-jeeves-refresh-queue.md`, creating the file if needed:

```
- <today, YYYY-MM-DD> | references/<file>.md | <the change, in generic legal terms> | <official source URL>
```

The line names the law only: never a party, employer, person or any text from the input. The same format carries `build state card <ST>` lines from SKILL.md step 6, with the card's path as the file. A weekly scheduled task refreshes queued files, builds queued cards (`docs/refresh-procedure.md` in the repo) and clears the lines it handles. Don't edit reference files during a run; the installed copy is pinned.

## Changes since last as-of

### 2026-10-20 ticket 30

- [fix] §6 example made generic: it named the regression fixture's planted citation, which told test runs it was fake (`tests/regression/README.md`)
