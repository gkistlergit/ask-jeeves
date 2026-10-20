# Local statute library

Official state codes that Grant downloads, kept on this Mac for Jeeves to search offline. **The code files themselves are gitignored**: they are large and this repo is public. Only this README and `MANIFEST.md` are committed.

## Layout

```
(the download stays where Grant saved it; MANIFEST.md records the path)
Sources/<ST>/<edition>/text/   plain text, one file per title, made by scripts/ingest-code.sh
```

`<ST>` is the two-letter state code (`IN`, `SC`, `US` for federal). `<edition>` is the code year or the session the code is current through (`2026`, `2025-session`).

## Adding a state

1. Download the official code from the state's site. `skills/ask-jeeves/references/state-codes-*.md` lists where each state publishes it.
2. Put the download anywhere. Then run:
   ```bash
   scripts/ingest-code.sh <ST> <edition> <path-to-download-folder-or-file>
   ```
   It converts HTML, Word and PDF files to text in `text/`, and adds a row to `MANIFEST.md`.
3. Commit `MANIFEST.md` only.

## How Jeeves uses it

Before any web lookup of a state statute, Jeeves checks `MANIFEST.md`. If the applied state has an edition here, Jeeves greps `text/` for the section and cites it as `<cite> (<edition> <State> Code, official download)`. It also says when the edition is older than the reference file's `as_of`, or older than a law change it found. See `skills/ask-jeeves/references/research-resilience.md`.
