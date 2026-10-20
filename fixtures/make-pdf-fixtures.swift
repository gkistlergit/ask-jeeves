// Builds the two fictional PDF fixtures for the input-reading fallback (ticket 24) from mismatch-contract.md:
//   scanned-contract.pdf    one image-only page, no text layer (like a scan)
//   encrypted-contract.pdf  text layer, AES-encrypted with an empty user password and an owner password
// Usage, from the repo root: swift fixtures/make-pdf-fixtures.swift
import AppKit
import Foundation

let dir = URL(fileURLWithPath: "fixtures", isDirectory: true)
let text = try String(contentsOf: dir.appendingPathComponent("mismatch-contract.md"), encoding: .utf8)
    .replacingOccurrences(of: "**", with: "")
let page = CGRect(x: 0, y: 0, width: 612, height: 792)
let attrs: [NSAttributedString.Key: Any] = [.font: NSFont(name: "Times New Roman", size: 11) ?? NSFont.systemFont(ofSize: 11)]

func drawText(in cg: CGContext, scale: CGFloat) {
    NSGraphicsContext.saveGraphicsState()
    NSGraphicsContext.current = NSGraphicsContext(cgContext: cg, flipped: false)
    cg.scaleBy(x: scale, y: scale)
    NSAttributedString(string: text, attributes: attrs).draw(in: page.insetBy(dx: 60, dy: 60))
    NSGraphicsContext.restoreGraphicsState()
}

// Encrypted: real text layer, empty user password, owner password, 128-bit key.
var box = page
let encOpts: [CFString: Any] = [
    kCGPDFContextOwnerPassword: "fixture-owner",
    kCGPDFContextUserPassword: "",
    kCGPDFContextEncryptionKeyLength: 128,
    kCGPDFContextAllowsCopying: false,
]
let enc = CGContext(dir.appendingPathComponent("encrypted-contract.pdf") as CFURL, mediaBox: &box, encOpts as CFDictionary)!
enc.beginPDFPage(nil)
drawText(in: enc, scale: 1)
enc.endPDFPage()
enc.closePDF()

// Scanned: render the page to a 200 dpi bitmap, then place only that image in the PDF.
let s: CGFloat = 200.0 / 72.0
let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: Int(page.width * s), pixelsHigh: Int(page.height * s),
                           bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false,
                           colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
let bcg = NSGraphicsContext(bitmapImageRep: rep)!.cgContext
bcg.setFillColor(NSColor.white.cgColor)
bcg.fill(CGRect(x: 0, y: 0, width: CGFloat(rep.pixelsWide), height: CGFloat(rep.pixelsHigh)))
drawText(in: bcg, scale: s)
let image = rep.cgImage!
let scan = CGContext(dir.appendingPathComponent("scanned-contract.pdf") as CFURL, mediaBox: &box, nil)!
scan.beginPDFPage(nil)
scan.draw(image, in: page)
scan.endPDFPage()
scan.closePDF()
print("wrote fixtures/encrypted-contract.pdf and fixtures/scanned-contract.pdf")
