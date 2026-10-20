// Usage: swift scripts/pdf2txt.swift <in.pdf> <out.txt>. Extracts text with macOS PDFKit.
import Foundation
import PDFKit
let a = CommandLine.arguments
guard a.count == 3, let doc = PDFDocument(url: URL(fileURLWithPath: a[1])) else { exit(1) }
var s = ""
for i in 0..<doc.pageCount { s += (doc.page(at: i)?.string ?? "") + "\n\u{0C}\n" }
try s.write(toFile: a[2], atomically: true, encoding: .utf8)
