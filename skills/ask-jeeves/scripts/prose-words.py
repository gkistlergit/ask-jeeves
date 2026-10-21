"""Counts a memo's prose words the way templates/memo.md defines them.

Usage: python3 prose-words.py < memo.md   (or pipe the memo in with a heredoc; nothing is saved)
Prints the total, one line per counted section, and whether it fits 600-900.

Counts: Bottom line, Path to your goal, State applied, Recommendations, Creative option,
Questions and Adjacent issues. Skips headings, bold labels, citations in brackets, (#n) risk refs,
list markers, tables, quoted clauses and their *In plain terms* lines, Sources and the ending.
"""
import re
import sys

COUNTED = ["Bottom line", "Path to your goal", "State applied", "Recommendations",
           "Creative option", "Questions for a licensed attorney", "Adjacent issues"]


def count(memo):
    per, cur = {}, None
    for line in memo.splitlines():
        if line.startswith("## "):
            title = line[3:].strip()
            cur = next((c for c in COUNTED if title.lower().startswith(c.lower())), None)
            continue
        s = line.strip()
        if cur is None or not s or s.startswith(("|", ">", "*In plain terms")):
            continue
        s = re.sub(r"\*\*[^*]+\*\*", " ", s)
        s = re.sub(r"\[[^\]]*\]", " ", s)
        s = re.sub(r"\(#[\d, #]+\)", " ", s)
        s = re.sub(r"^(\d+\.|[-*])\s+", "", s)
        per[cur] = per.get(cur, 0) + sum(1 for w in s.split() if re.search(r"[A-Za-z0-9]", w))
    return per


if __name__ == "__main__":
    per = count(sys.stdin.read())
    total = sum(per.values())
    for k in COUNTED:
        print(f"{per.get(k, 0):5}  {k}")
    verdict = "fits" if 600 <= total <= 900 else ("cut " + str(total - 900) if total > 900 else "add " + str(600 - total))
    print(f"{total:5}  total prose words: {verdict} (600-900)")
