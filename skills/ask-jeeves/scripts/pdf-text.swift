// Reads a PDF the Read tool can't: scanned (no text layer) or encrypted with an empty user password.
// Usage: swift pdf-text.swift <file.pdf> <new empty output folder>
// Writes page-N.txt (text layer), page-N.png (300 dpi render, image-only pages) and
// page-N.ocr.txt (local tesseract OCR), plus all.txt with every page in order.
// Everything stays on this Mac. Exit codes: 2 can't open, 3 needs a password, 4 bad arguments.
import AppKit
import Foundation
import PDFKit

let args = CommandLine.arguments
guard args.count == 3 else {
    FileHandle.standardError.write("usage: swift pdf-text.swift <file.pdf> <output folder>\n".data(using: .utf8)!)
    exit(4)
}
let out = URL(fileURLWithPath: args[2], isDirectory: true)
try? FileManager.default.createDirectory(at: out, withIntermediateDirectories: true)

guard let doc = PDFDocument(url: URL(fileURLWithPath: args[1])) else {
    print("CANNOT OPEN: not a readable PDF")
    exit(2)
}
if doc.isLocked && !doc.unlock(withPassword: "") {
    print("LOCKED: this PDF needs a password. Ask Grant to open it himself and export an unlocked copy.")
    exit(3)
}

let tesseract = ["/opt/homebrew/bin/tesseract", "/usr/local/bin/tesseract", "/usr/bin/tesseract"]
    .first { FileManager.default.isExecutableFile(atPath: $0) }

func render(_ page: PDFPage, to url: URL) -> Bool {
    let box = page.bounds(for: .mediaBox)
    let scale: CGFloat = 300.0 / 72.0
    guard let rep = NSBitmapImageRep(
        bitmapDataPlanes: nil, pixelsWide: Int(box.width * scale), pixelsHigh: Int(box.height * scale),
        bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false,
        colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0),
        let ctx = NSGraphicsContext(bitmapImageRep: rep) else { return false }
    let cg = ctx.cgContext
    cg.setFillColor(NSColor.white.cgColor)
    cg.fill(CGRect(x: 0, y: 0, width: CGFloat(rep.pixelsWide), height: CGFloat(rep.pixelsHigh)))
    cg.scaleBy(x: scale, y: scale)
    cg.translateBy(x: -box.origin.x, y: -box.origin.y)
    page.draw(with: .mediaBox, to: cg)
    guard let png = rep.representation(using: .png, properties: [:]) else { return false }
    return (try? png.write(to: url)) != nil
}

func ocr(_ png: URL) -> String {
    guard let tesseract else { return "" }
    let p = Process()
    p.executableURL = URL(fileURLWithPath: tesseract)
    p.arguments = [png.path, "-"]
    let pipe = Pipe()
    p.standardOutput = pipe
    p.standardError = FileHandle.nullDevice
    guard (try? p.run()) != nil else { return "" }
    let data = pipe.fileHandleForReading.readDataToEndOfFile()
    p.waitUntilExit()
    return String(data: data, encoding: .utf8) ?? ""
}

var all = ""
for i in 0..<doc.pageCount {
    guard let page = doc.page(at: i) else { continue }
    let n = i + 1
    let text = page.string ?? ""
    try? text.write(to: out.appendingPathComponent("page-\(n).txt"), atomically: true, encoding: .utf8)
    var source = "text"
    var body = text
    var line = "page \(n): text layer \(text.count) chars"
    if text.trimmingCharacters(in: .whitespacesAndNewlines).count < 50 {
        let png = out.appendingPathComponent("page-\(n).png")
        if render(page, to: png) {
            let read = ocr(png)
            try? read.write(to: out.appendingPathComponent("page-\(n).ocr.txt"), atomically: true, encoding: .utf8)
            line += " | image \(png.lastPathComponent)"
            if read.isEmpty {
                source = "image only: Read the PNG"
                line += tesseract == nil ? " | no tesseract: Read the PNG" : " | OCR found no text"
            } else {
                source = "ocr"
                body = read
                line += " | ocr \(read.count) chars"
            }
        }
    }
    all += "<!-- page \(n) (\(source)) -->\n\(body)\n\n"
    print(line)
}
try? all.write(to: out.appendingPathComponent("all.txt"), atomically: true, encoding: .utf8)
print("pages: \(doc.pageCount) | encrypted: \(doc.isEncrypted) | all.txt in \(out.path)")
