# Scanned and encrypted PDF input
Type: task
Status: open
Blocked by:

## Question

Step 1 says to read the input in full, but two common PDF types failed on 2026-10-20:
- A scanned PDF has no text layer, and the Read tool can't render pages without `pdftoppm`. What worked: extract the page images and run `tesseract` locally.
- An AES-encrypted PDF fails in pypdf without `cryptography`. What worked: macOS PDFKit through a short Swift script.

Add an input-reading fallback to SKILL.md step 1, or a small reference file. It must keep every byte local (no upload or OCR service, per the free-to-run and privacy rules), and Jeeves must tell Grant the text came from OCR and that the PDF is authoritative.

Done when the fallback is written down and checked on one scanned and one encrypted fixture. The fixtures must be fictional, never Grant's documents.
