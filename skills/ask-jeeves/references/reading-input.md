---
as_of: 2026-10-20
verified: 2026-10-20
---

# Reading an input PDF the Read tool can't

Use this when the Read tool fails on a PDF or returns little or no text. Typical causes:
- a scanned document with no text layer;
- an encrypted PDF;
- `pdftoppm` not installed (the Read tool needs it to render pages).

All reading happens on this Mac. The file and its text never go to an upload or OCR web service or a paid API.

## Steps

1. **Extract.** Pick a new, empty folder in the scratchpad and run:
   ```bash
   swift <skill folder>/scripts/pdf-text.swift "<file.pdf>" "<scratchpad>/<new folder>"
   ```
   The script prints one line per page, then writes `all.txt` with every page in order. Each page carries a `<!-- page N (text | ocr | image only) -->` marker.
   - **Text layer:** used as is. This covers encrypted PDFs that open with an empty user password, which macOS PDFKit reads where pypdf needs the `cryptography` package (or `pycryptodome`).
   - **Under 50 characters of text on a page:** the script renders that page to `page-N.png` at 300 dpi and runs local `tesseract` on it, writing `page-N.ocr.txt`.
   - **Exit 3, "LOCKED":** the PDF needs a password. Ask Grant to open it himself and export an unlocked copy. Jeeves never guesses or cracks a password.
2. **Image-only pages.** If a page reads "image only" (no `tesseract`, or OCR found nothing), Read its `page-N.png` with the Read tool.
3. **Read `all.txt` in full.** That counts as reading the input for step 1.
4. **Tell Grant in one line** that the text came from OCR or decryption of `<file>`, and that the PDF is the authoritative copy.
5. **Quote from the page image.** OCR can garble characters, for example "1n" for "in" or "2:5:3" for "2.5.3". Before a clause goes into the memo as a quote, check it against the page image, and fix only obvious OCR errors.

The output folder stays in the scratchpad. Save the text anywhere else only when Grant asks, and only where he says.

## Checked

On 2026-10-20 the script read the two fictional fixtures `fixtures/scanned-contract.pdf` and `fixtures/encrypted-contract.pdf` (built by `fixtures/make-pdf-fixtures.swift`). Both came back matching `fixtures/mismatch-contract.md` word for word. pypdf fails on the encrypted fixture without `cryptography`, and the scanned fixture has no text layer, so both reproduce the original failures.

## Changes since last as-of

### 2026-10-20 refresh

- [fix] Dates renewed; no change found in PDFKit, tesseract or pypdf since as-of (https://developer.apple.com/documentation/pdfkit)
- [fix] Noted `pycryptodome` as pypdf's alternative to `cryptography` for AES-encrypted PDFs (https://pypdf.readthedocs.io/en/stable/user/encryption-decryption.html)
