---
area: state-card
state: <ST>
as_of: <YYYY-MM-DD>
verified: <YYYY-MM-DD>
sources: <research notes or ticket>; <Sources/ edition, if any>
---
# <State name>: slim state card

> For issue-spotting only. Not legal advice. Every claim cites its source; [UNVERIFIED] marks claims that could not be confirmed.

Template for `references/state-cards/<ST>.md` (ticket 27: built when Grant asks, or after 3 logged runs of a state other than IN or SC). Copy it to `<ST>.md`, fill every `<...>`, and delete this paragraph. Files whose names start with `_` are not cards: Jeeves never loads them and refreshes skip them.

A card is slimmer than a reference file. It covers the key statutes and the 3–6 leading cases on each field below, deep-researched and verified once. Quick mode can cover this state from the card, labeled `slim state card` (`templates/memo.md`). Anything not on the card is out of scope at quick: list it as a gap and offer intermediate or deep.

## Key statutes

One line per statute: what it does, then the citation. Point into the local statute library when `Sources/MANIFEST.md` has an edition for this state, otherwise give the official URL only.

- <what it does>. [cite: <statute cite>, Sources/<ST>/<edition>/text/<file> | <official URL>]
- Trade secrets: <the state's trade-secret act, or "none enacted">. [cite: ...]
- Restrictive covenants: <statute, or "common law only">. [cite: ...]
- IP assignment of employee inventions: <statute limiting assignment, or "none">. [cite: ...]
- Wage payment: <timing, final pay, deductions>. [cite: ...]

## Leading cases

3–6 per field. One line each: the holding in plain words, then the citation and the source it was read on.

### Restrictive covenants
- <holding>. [cite: <case>, <reporter cite> (<court> <year>), <URL>]

### IP assignment
- <holding>. [cite: ...]

### Wage payment
- <holding>. [cite: ...]

## Not on this card

- <what a quick memo can't cover from this card, for example insider-theft case law or a statute not researched>.

## Changes since last as-of

None yet. A refresh fills this in: date, each change tagged *substance* or *fix*, and its source (`docs/refresh-procedure.md`).
