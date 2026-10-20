# Test results (ticket 19)

All runs are of `skill/v1`, 2026-10-20. Fixtures are in `fixtures/` (fictional). Each memo test ran employee mode, Indiana, with the goal "keep sole ownership of 3 apps built on my own time and money", on `fixtures/offer-letter-with-citation.md`, which contains a planted fake case.

| Test | Result | Evidence |
|---|---|---|
| Quick memo | **Pass.** No web calls; fake cite marked NOT CHECKED and not relied on; all sections present; 895 words of prose | `tests/memo-quick.md`, `tests/trace-quick.md` |
| Intermediate memo, "quick-verified" | **Pass.** 5 of 8 searches; fake cite marked NOT FOUND (the cited page holds Ohio entries); all sections present; about 880 words | `tests/memo-intermediate.md`, `tests/trace-intermediate.md` |
| Deep memo, full verification note | **Pass.** About 27 min of the 45-min limit; 4 area subagents plus 1 verifier (22 confirmed, 3 corrected, 1 not found); fake cite NOT FOUND, listed in Bottom line, not used as support | `tests/memo-deep.md`, `tests/trace-deep.md` |
| State mismatch (IN-law contract, a move to SC planned) | **Pass**, run live with Grant on 2026-10-20. Jeeves pre-filled from the document, asked one round of state questions (work, home, employer, events, counsel), found no override statute, and recommended **Indiana primary, SC backup** with reasons and a 4-row differences table. It flagged **Uncertain** (planned move, signed in SC), and held research until Grant confirmed ("Indiana with SC backup notes"). Grant gave his real-world goal and facts, which are kept out of this public repo. | `fixtures/mismatch-contract.md` |
| Deep memo on Grant's real goal (deep part of the state-mismatch test) | **Pass**, 2026-10-20. 4 area subagents plus 1 verifier: 36 sources checked, 33 confirmed, 3 corrected, 0 unverified, 0 not found; 880 words of prose; humanizer pass done. Memo shown in chat only; its facts stay out of this repo. | none (by design) |
| Attorney finder, 4 locations | **Pass**, 2026-10-20 (Grant chose the locations and answered each prompt). Home (Noblesville): 0 qualified. Aiken, SC with the mismatch flag (Grant chose an Indiana license): 0 qualified, as expected, since no nearby lawyer lists an Indiana admission; SC-only near-misses were flagged so he can switch. Typed ZIP: Grant typed 46060, the same as Home, so the typed path ran with no network call and the Home results were reused. Live location: the IP fallback returned the wrong city (approximate, as disclosed); the new Jeeves Location app returned the correct city and ZIP after the macOS prompt; that location also qualified 0. Every run used 8 of 8 searches, reported "fewer than 3" honestly, gave the budget routes and listed near-misses. No bar was lowered and no one was contacted. | n/a |

## Gaps the tests found, all fixed on skill/v1
- State confirmation assumed a backup state, so it now has a no-backup variant (8233b59).
- "Legal deadline" is now defined; an offer sign-by date isn't one (8233b59).
- The word count is now defined, and NOT CHECKED was added to the source statuses (8233b59).
- The intermediate fan-out trigger was too eager; it's now 3+ areas (8233b59).
- The `as_of` change search is skipped when the files are under 30 days old (8233b59).
- Searching authority names quoted in the input is allowed (8233b59).
- Deep subagents no longer use the research skill, which nests an agent. Federal law goes with each area (f09147b).
- The local statute library is now step 0. There's an explicit NOT FOUND procedure that never calls a real case fake because a tool failed (f09147b).

## Process notes from the real-goal deep run (2026-10-20, not yet fixed)
- The real input document arrived after research began, so the area research had targeted the stand-in. The skill has no step for re-scoping when the input changes mid-run. The verifier still covered every source the memo cites.
- A scanned PDF input had no text layer, and the Read tool couldn't render it (no `pdftoppm`). Extracting the page images and running `tesseract` worked. An AES-encrypted PDF failed in pypdf (no `cryptography`) but opened in macOS PDFKit. Step 1 has no OCR or encrypted-PDF guidance.
- Attorney finder: firm sites and third-party mirrors rarely show review dates, so the "review in the last 24 months" test failed most candidates. Every one of the 8 searches was needed before the "fewer than 3" route triggered.

## Process notes from the attorney-finder runs (2026-10-20)
- 0 of 3 locations had a qualifying attorney. The binding constraint is the recency rule (a review dated within 24 months), since aggregators and snippets rarely show dates; a second independent review source is next. This is a design question for Grant, ticketed as [Attorney-finder recency rule](../.scratch/ask-jeeves/issues/25-attorney-finder-recency.md).
- Live location: a bare script or `swift` run is denied with no prompt; locationd prompts only a bundled app. Fixed with `scripts/jeeves-location/` on skill/v1 (2dbba99).
- One subagent WebFetched a FindLaw profile despite the snippets-only rule, and disclosed it. The rule held everywhere else.
