# Scanned and encrypted PDF input
Type: task
Status: resolved
Blocked by:

## Question

Step 1 says to read the input in full, but two common PDF types failed on 2026-10-20:
- A scanned PDF has no text layer, and the Read tool can't render pages without `pdftoppm`. What worked: extract the page images and run `tesseract` locally.
- An AES-encrypted PDF fails in pypdf without `cryptography`. What worked: macOS PDFKit through a short Swift script.

Add an input-reading fallback to SKILL.md step 1, or a small reference file. It must keep every byte local (no upload or OCR service, per the free-to-run and privacy rules), and Jeeves must tell Grant the text came from OCR and that the PDF is authoritative.

Done when the fallback is written down and checked on one scanned and one encrypted fixture. The fixtures must be fictional, never Grant's documents.

## Answer

Done 2026-10-20 on `skill/v1` (39ebf1a, draft PR gkistlergit/ask-jeeves#1).
- SKILL.md step 1 points unreadable PDFs to the new `references/reading-input.md`. That file runs `scripts/pdf-text.swift`:
  - macOS PDFKit reads the text layer, including AES-encrypted files with an empty user password.
  - Pages with under 50 characters of text are rendered at 300 dpi and OCR'd with local `tesseract`.
  - If `tesseract` is missing, Jeeves reads the page PNG with the Read tool.
  - A password-locked file goes back to Grant to unlock. Jeeves never guesses a password.
- Jeeves tells Grant the text came from OCR, and that the PDF is authoritative. It checks quoted clauses against the page image. Nothing leaves the Mac.
- Checked on two fictional fixtures, `fixtures/scanned-contract.pdf` and `fixtures/encrypted-contract.pdf`, built from `mismatch-contract.md` by `fixtures/make-pdf-fixtures.swift`.
  - pypdf fails on both: no `cryptography` for the encrypted file, no text layer in the scan.
  - The script's output matched the source word for word on both.
