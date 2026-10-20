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

Try each source once. If it's blocked, down, empty or behind a CAPTCHA, move to the next source. When the chain runs out, mark the claim [UNVERIFIED] with the reason. **Never bypass a CAPTCHA, a login or a human-verification page.**

| Authority | Try in order |
|---|---|
| U.S. Code | uscode.house.gov → law.cornell.edu/uscode → govinfo.gov |
| Federal regulations | ecfr.gov → federalregister.gov → law.cornell.edu/cfr |
| Federal agency actions | the agency's own site (ftc.gov, nlrb.gov, eeoc.gov, dol.gov, sec.gov) → federalregister.gov |
| Supreme Court / circuit opinions | supremecourt.gov or the circuit's own opinion page → case.law → Google Scholar → Justia (CourtListener often demands human verification; skip it if it does) |
| Indiana Code / acts | iga.in.gov serves only a JavaScript shell to WebFetch and curl, and api.iga.in.gov returns 403 (checked 2026-10-20). Use, in order: (1) the reference files, which were checked against the official 2026 Indiana Code download; (2) an Indiana court opinion quoting the section, `public.courts.in.gov/Decisions/api/Document/Opinion?Id=<id>` (a PDF); (3) an in.gov agency page (DOL, DWD, AG, ICRC) quoting it; (4) FindLaw or Justia, labeled **(mirror, secondary)**. For a section changed after the reference file's `as_of`, Grant can download the current code from iga.in.gov → any title → Reference Materials → "Download the <year> Indiana Code". |
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
