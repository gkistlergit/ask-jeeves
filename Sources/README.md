# Local statute library

Official state codes that Grant downloads, kept on this Mac for Jeeves to search offline. **The code files themselves are gitignored**: they are large and this repo is public. Only this README and `MANIFEST.md` are committed.

## Layout

```
(the download stays where Grant saved it; MANIFEST.md records the path)
Sources/<ST>/<edition>/text/   plain text, one file per title, made by scripts/ingest-code.sh
```

`<ST>` is the two-letter state code (`IN`, `SC`, `US` for federal). `<edition>` is the code year or the session the code is current through (`2026`, `2025-session`).

## Adding a state

**Download only what's needed.** Only states on the *download short list* need a local copy: those whose official code site our tools can't read. The state-codes reference files mark them; Indiana is one. Download **only the employment titles** listed for that state (non-compete, trade secrets, wage payment, computer crime), not the whole code. Prefer **HTML or XML over PDF**. Leave the download in `~/Downloads`; the script reads it in place and records the path.

**Refresh yearly.** A scheduled task (`ask-jeeves-annual-code-refresh`, July 15) lists stale editions and short-list states with no local copy.

1. Download the official code from the state's site. `skills/ask-jeeves/references/state-codes-*.md` lists where each state publishes it.
2. Put the download anywhere. Then run:
   ```bash
   scripts/ingest-code.sh <ST> <edition> <path-to-download-folder-or-file>
   ```
   It converts HTML, Word and PDF files to text in `text/`, and adds a row to `MANIFEST.md`.
3. Commit `MANIFEST.md` only.

## How Jeeves uses it

Before any web lookup of a state statute, Jeeves checks `MANIFEST.md`. If the applied state has an edition here, Jeeves greps `text/` for the section and cites it as `<cite> (<edition> <State> Code, official download)`. It also says when the edition is older than the reference file's `as_of`, or older than a law change it found. See `skills/ask-jeeves/references/research-resilience.md`.
