#!/usr/bin/env python3
"""ask-jeeves regression suite (ticket 30). One command:

    python3 tests/regression/run.py

Runs the skill headless (`claude -p`) on the fictional fixtures, with every question answered
from a script, then checks each memo and trace with `checks.py`. Exits 0 when every case passes.

Options:
  --repo PATH        the ask-jeeves checkout whose skill is tested (default: this one)
  --cases a,b        run only these case ids (default: all; see CASES)
  --jobs N           cases run in parallel (default 4)
  --out DIR          where traces, memos and report.md go (default: a new temp folder)
  --check-only DIR   re-check the traces in an earlier --out folder; runs no model
  --preflight-only   run only the free checks: template drift, PDF extraction, checker self-test
  --model NAME       passed to claude --model (default: the account's default)

Free to run: it uses the signed-in Claude account (ANTHROPIC_API_KEY is removed from the child
environment), WebSearch/WebFetch for intermediate cases, and local swift and tesseract for PDFs.
"""
import argparse
import concurrent.futures as cf
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import checks  # noqa: E402

SKILL_NAME = "jeeves-under-test"

# Scripted answers. All facts are the fixtures' own (fictional); nothing about Grant.
OFFER = {
    "goal": "Keep sole ownership of 3 apps I built on my own time and money",
    "answers": [
        "End goal: the goal given in the arguments.",
        "Goal restatement check: Yes, that's my goal.",
        "Where the employee works: the Indianapolis, Indiana office 3 days a week, remote from home in Indianapolis the rest.",
        "Where the employee lives: Indianapolis, Indiana.",
        "Where the employer is based and operates: Indianapolis, Indiana.",
        "Key events: none yet. The offer isn't signed; no resignation, data access or competing work.",
        "Governing law or court in the document: Indiana law, Marion County, Indiana courts (section 8).",
        "Occupation and pay: Senior Data Engineer, $128,000.",
        "Signing date: not signed yet.",
        "State confirmation: Confirm Indiana.",
    ],
}
MISMATCH = {
    "goal": "Know whether I could take a customer success job with a competitor in Georgia after I leave",
    "answers": [
        "End goal: the goal given in the arguments.",
        "Goal restatement check: Yes, that's my goal.",
        "Where the employee works: fully remote from home in Aiken, South Carolina, 100% of the time.",
        "Where the employee lives: Aiken, South Carolina.",
        "Where the employer is based and operates: based in Carmel, Indiana; serves accounts across the Southeast.",
        "Key events: none yet. Still employed; no resignation, data access or competing work.",
        "Governing law or court in the document: Indiana law, exclusive Hamilton County, Indiana courts (section 11).",
        "Occupation and pay: Customer Success Manager, $74,000.",
        "Signing date: March 3, 2026, signed electronically from Aiken, South Carolina.",
        "State confirmation: Primary with backup notes, when a backup is offered; otherwise Confirm <the primary>.",
    ],
}
MISMATCH_STATE = {"states": {"IN", "SC"}, "confidence": "Uncertain"}
# The planted case in offer-letter-with-citation.md. If the skill names it, runs know it's fake.
PLANTED_TELLS = ["Hartwell", "258 N.E.3d"]

# No case runs sample-offer-letter.md: offer-letter-with-citation.md is the same letter plus the planted
# cite, with the same answers, so the citation cases run every check an offer case would.
CASES = [
    {"id": "citation-quick", "fixture": "offer-letter-with-citation.md", "depth": "quick", "state": "IN",
     "planted": "Hartwell", **OFFER},
    {"id": "citation-intermediate", "fixture": "offer-letter-with-citation.md", "depth": "intermediate", "state": "IN",
     "planted": "Hartwell", **OFFER},
    {"id": "mismatch-quick", "fixture": "mismatch-contract.md", "depth": "quick",
     "expect_state": MISMATCH_STATE, **MISMATCH},
    {"id": "pdf-scanned-quick", "fixture": "scanned-contract.pdf", "depth": "quick", "pdf": "scanned-contract.pdf",
     "expect_state": MISMATCH_STATE, **MISMATCH},
    {"id": "pdf-encrypted-quick", "fixture": "encrypted-contract.pdf", "depth": "quick", "pdf": "encrypted-contract.pdf",
     "expect_state": MISMATCH_STATE, **MISMATCH},
]
TIMEOUT = {"quick": 15 * 60, "intermediate": 35 * 60}

HARNESS = """REGRESSION TEST RUN of the ask-jeeves skill (invoked here as /{skill}). Nobody is at the keyboard, and AskUserQuestion is unavailable. Follow the skill exactly, with only these changes:

1. Whenever the skill says to ask Grant something, in chat or with AskUserQuestion, print it in chat as
   QUESTION: <the question>
   OPTIONS: <option> / <option> / ...   (omit this line for an open question)
   then print `SCRIPTED ANSWER: <answer>` on its own line, taking the answer from the list below, and carry on as if Grant had replied. Ask every question and confirmation the skill requires, even when an argument or the input seems to answer it already, unless the skill itself says to skip it. Print the state confirmation in step 3 this way too, right after the candidate-state block, with every option the skill lists. Use a scripted answer only for the question it answers. A question with no scripted answer takes the skill's stated default; print `SCRIPTED ANSWER: (default) <answer>`.
2. Step 6: do not write ~/.claude/ask-jeeves-run-log.md or ~/.claude/ask-jeeves-refresh-queue.md, skip the state-card trigger, and skip the attorney-finder and contract-drafter questions. Steps 7 and 8 never run.
3. Never use the Write or Edit tools. Put any working files, such as PDF text output, in a new folder under {scratch}.
4. Print the finished memo exactly once, between a line `=== MEMO START ===` and a line `=== MEMO END ===`.

Scripted answers:
{answers}
"""


def build_sandbox(repo, root):
    """A folder whose project skill is the skill under test, plus copies of the fixtures."""
    sb = root / "sandbox"
    skill = sb / ".claude/skills" / SKILL_NAME
    shutil.copytree(repo / "skills/ask-jeeves", skill)
    md = skill / "SKILL.md"
    md.write_text(re.sub(r"^name: ask-jeeves$", f"name: {SKILL_NAME}", md.read_text(), count=1, flags=re.M))
    # SKILL.md cites the glossary as ../../CONTEXT.md from its own folder.
    shutil.copy(repo / "CONTEXT.md", sb / ".claude/CONTEXT.md")
    (sb / "fixtures").mkdir()
    for f in (repo / "fixtures").iterdir():
        if f.suffix in {".md", ".pdf"} and f.name != "README.md":  # the README names the planted cite
            shutil.copy(f, sb / "fixtures" / f.name)
    (sb / "scratch").mkdir()
    return sb


def run_case(case, sb, out, model, sub=""):
    d = out / case["id"] / sub
    d.mkdir(parents=True, exist_ok=True)
    args = ["employee", case["depth"]] + ([case["state"]] if case.get("state") else [])
    args += [f'goal:"{case["goal"]}"', str(sb / "fixtures" / case["fixture"])]
    prompt = f"/{SKILL_NAME} " + " ".join(args)
    system = HARNESS.format(skill=SKILL_NAME, scratch=sb / "scratch" / case["id"] / sub,
                            answers="\n".join(f"- {a}" for a in case["answers"]))
    cmd = [
        "claude", "-p", prompt, "--output-format", "stream-json", "--verbose", "--no-session-persistence",
        "--append-system-prompt", system,
        "--allowedTools", "Read", "Glob", "Grep", "WebSearch", "WebFetch", "Skill", "Agent", "Task",
        "Bash(swift:*)", "Bash(uname:*)", "Bash(test:*)", "Bash(mkdir:*)", "Bash(ls:*)", "Bash(wc:*)", "Bash(date:*)", "Bash(python3:*)",
        "--disallowedTools", "AskUserQuestion", "Write", "Edit", "NotebookEdit",
    ] + (["--model", model] if model else [])
    env = {k: v for k, v in os.environ.items() if k not in ("ANTHROPIC_API_KEY", "CLAUDECODE")}
    (d / "command.json").write_text(json.dumps({"prompt": prompt, "append_system_prompt": system}, indent=2))
    t0 = time.time()
    with open(d / "trace.jsonl", "w") as fh:
        try:
            p = subprocess.run(cmd, cwd=sb, env=env, stdout=fh, stderr=subprocess.PIPE, text=True,
                               timeout=TIMEOUT[case["depth"]])
            err = p.stderr[-2000:] if p.returncode else ""
        except subprocess.TimeoutExpired:
            err = f"timed out after {TIMEOUT[case['depth']]}s"
    return case["id"], sub, round(time.time() - t0), err


def evaluate(case, d, run_err=""):
    fails, info, memo = checks.check_case(case, d / "trace.jsonl")
    if run_err:
        fails.insert(0, f"claude -p: {run_err.strip()[:300]}")
    (d / "memo.md").write_text(memo + "\n")
    (d / "result.json").write_text(json.dumps({"id": case["id"], "pass": not fails, "fails": fails, **info}, indent=2))
    return fails, info


# ---------- free checks ----------

def pdf_words(text):
    text = re.sub(r"<!--.*?-->", " ", text)
    text = re.sub(r"[*#_>`]", " ", text)
    return [w.strip(".,;:") for w in text.split() if re.search(r"[A-Za-z0-9]", w)]


def preflight(repo, out):
    """(name, failures) for the checks that need no model run."""
    results = []
    drift = checks.template_drift(repo / "skills/ask-jeeves/templates/memo.md")
    results.append(("template sections match the suite", [] if drift is None else [
        f"templates/memo.md headings are now {drift}; update EXPECTED_SECTIONS in tests/regression/checks.py"]))
    ref = pdf_words((repo / "fixtures/mismatch-contract.md").read_text())
    for name in ("scanned-contract.pdf", "encrypted-contract.pdf"):
        dest = out / "pdf" / name.split(".")[0]
        if not shutil.which("swift"):
            results.append((f"pdf-text.swift reads {name}", ["swift not found; this check needs macOS"]))
            continue
        p = subprocess.run(["swift", str(repo / "skills/ask-jeeves/scripts/pdf-text.swift"),
                            str(repo / "fixtures" / name), str(dest)], capture_output=True, text=True)
        f = []
        if p.returncode:
            f.append(f"pdf-text.swift exited {p.returncode}: {(p.stdout + p.stderr).strip()[:200]}")
        elif pdf_words((dest / "all.txt").read_text()) != ref:
            got = pdf_words((dest / "all.txt").read_text())
            first = next((i for i, (a, b) in enumerate(zip(ref, got)) if a != b), min(len(ref), len(got)))
            f.append(f"text differs from mismatch-contract.md at word {first}: "
                     f"{' '.join(got[first:first + 6])!r} vs {' '.join(ref[first:first + 6])!r}")
        results.append((f"pdf-text.swift reads {name}", f))
    leaks = [str(f.relative_to(repo)) for f in (repo / "skills/ask-jeeves").rglob("*")
             if f.is_file() and f.suffix in {".md", ".py", ".swift"}
             and any(t in f.read_text(errors="ignore") for t in PLANTED_TELLS)]
    results.append(("skill never mentions the planted citation", [f"named in {', '.join(leaks)}" for _ in leaks[:1]]))
    results.append(("checker self-test", self_test(repo)))
    return results


def self_test(repo):
    """The checker passes the ticket-19 memos and fails broken copies of them."""
    f = []
    good = (repo / "tests/memo-quick.md").read_text()
    good_i = (repo / "tests/memo-intermediate.md").read_text()
    if checks.check_memo(good, "quick") or checks.check_planted_citation(good, "quick"):
        f.append("rejects the known-good tests/memo-quick.md")
    if checks.check_memo(good_i, "intermediate") or checks.check_planted_citation(good_i, "intermediate"):
        f.append("rejects the known-good tests/memo-intermediate.md")
    no_creative = re.sub(r"## Creative option.*?(?=## Questions)", "", good, flags=re.S)
    if not any("Creative option" in x for x in checks.check_memo(no_creative, "quick")):
        f.append("passes a memo with no Creative option section")
    long = good.replace("## Risks", (checks.find_section(checks.sections(good)[0], "Path to your goal") * 3) + "\n## Risks", 1)
    if not any("words" in x for x in checks.check_memo(long, "quick")):
        f.append("passes a memo over 900 words")
    if not checks.check_planted_citation(good.replace("NOT CHECKED: quick mode", "confirmed 2026-10-20"), "quick"):
        f.append("passes a quick memo whose planted citation isn't marked NOT CHECKED")
    if not checks.check_planted_citation(good_i.replace("NOT FOUND", "UNVERIFIED"), "intermediate"):
        f.append("passes an intermediate memo whose planted citation isn't marked NOT FOUND")
    block = ("Candidate state: Indiana. Why: x\nBackup: South Carolina. Why: y\nConfidence: Uncertain: z\n"
             "Confirm the applied state with a licensed attorney before relying on this.\n"
             "QUESTION: Which state?\nOPTIONS: Confirm Indiana / Use South Carolina instead / Primary with backup notes / Other state\n"
             "SCRIPTED ANSWER: Primary with backup notes")
    web = ("tool", {"name": "WebSearch", "input": {}}, False)
    ok, _ = checks.check_state_confirmation([("text", block, False), web], MISMATCH_STATE)
    early, _ = checks.check_state_confirmation([web, ("text", block, False)], MISMATCH_STATE)
    skipped, _ = checks.check_state_confirmation([("text", block.split("QUESTION")[0], False), web])
    if ok:
        f.append(f"rejects a good state confirmation: {ok}")
    if not early:
        f.append("passes research that ran before the state confirmation")
    if not skipped:
        f.append("passes a candidate-state block with no confirmation question")
    return f

# ---------- main ----------

def report(out, pre, rows, repo, rechecked=False):
    head = subprocess.run(["git", "-C", str(repo), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
    dirty = subprocess.run(["git", "-C", str(repo), "status", "--porcelain", "skills", "fixtures"],
                           capture_output=True, text=True).stdout.strip()
    ok = all(not f for _, f in pre) and all(not r[1] for r in rows)
    not_run = any(r[2].get("not_run") for r in rows)
    lines = [f"### ask-jeeves regression suite: {'PASS' if ok else 'NOT RUN (account limit)' if not_run else 'FAIL'}",
             (f"Re-checked saved traces in `{out}` with the checker at `{head or 'unknown'}`, {date.today()}." if rechecked else
              f"Skill at `{head or 'unknown'}`{' (uncommitted changes in skills/ or fixtures/)' if dirty else ''}, run {date.today()}."), "",
             "| Check | Result | Detail |", "|---|---|---|"]
    for name, f in pre:
        lines.append(f"| {name} | {'pass' if not f else '**FAIL**'} | {'; '.join(f)} |")
    for cid, f, info in rows:
        t = info.get("tools", {})
        detail = (f"{info.get('words', 0)} words; {t.get('WebSearch', 0)} searches, {t.get('WebFetch', 0)} fetches; "
                  f"state answer: {info.get('state_answer') or 'none'}; {info.get('seconds', 0)}s")
        notes = [f"**{x}**" for x in f] + info.get("earlier", [])
        verdict = "**NOT RUN**" if info.get("not_run") else "**FAIL**" if f else ("pass on retry" if info.get("earlier") else "pass")
        lines.append(f"| {cid} | {verdict} | {detail}{'<br>' + '<br>'.join(notes) if notes else ''} |")
    text = "\n".join(lines) + "\n"
    (out / "report.md").write_text(text)
    return ok, text


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", type=Path, default=HERE.parent.parent)
    ap.add_argument("--cases")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--check-only", type=Path)
    ap.add_argument("--preflight-only", action="store_true")
    ap.add_argument("--model")
    ap.add_argument("--retries", type=int, default=1,
                    help="re-run a failed case this many times; the report keeps every failure (default 1)")
    a = ap.parse_args()
    repo = a.repo.resolve()
    cases = CASES
    if a.cases:
        want = a.cases.split(",")
        unknown = set(want) - {c["id"] for c in CASES}
        if unknown:
            sys.exit(f"unknown case ids: {', '.join(sorted(unknown))}")
        cases = [c for c in CASES if c["id"] in want]

    if a.check_only:
        out = a.check_only.resolve()
        rows = []
        for c in cases:
            if (out / c["id"] / "trace.jsonl").exists():
                f, info = evaluate(c, out / c["id"])
                rows.append((c["id"], f, info))
        ok, text = report(out, [], rows, repo, rechecked=True)
        print(text + f"\nFull results: {out}")
        sys.exit(0 if ok else 1)

    out = (a.out or Path(tempfile.mkdtemp(prefix=f"ask-jeeves-regression-{date.today()}-"))).resolve()
    out.mkdir(parents=True, exist_ok=True)
    pre = preflight(repo, out)
    if a.preflight_only:
        ok, text = report(out, pre, [], repo)
        print(text + f"\nFull results: {out}")
        sys.exit(0 if ok else 1)
    if not shutil.which("claude"):
        sys.exit("claude CLI not found on PATH")
    if platform.system() != "Darwin":
        # SKILL.md treats a shell that isn't macOS as chat Jeeves (quick only), so intermediate cases can't pass.
        sys.exit(f"model cases need macOS: on {platform.system()} the skill runs as chat Jeeves. "
                 "Run the suite on the Mac, or use --preflight-only or --check-only here.")

    sb = build_sandbox(repo, out)
    print(f"Running {len(cases)} cases, {a.jobs} at a time. Traces in {out}", flush=True)
    results = {c["id"]: [] for c in cases}  # per case: (subfolder, fails, info) for each attempt
    todo = [(c, "") for c in cases]
    for attempt in range(a.retries + 1):
        with cf.ThreadPoolExecutor(max_workers=a.jobs) as pool:
            futs = [pool.submit(run_case, c, sb, out, a.model, sub) for c, sub in todo]
            for fu in cf.as_completed(futs):
                cid, sub, secs, err = fu.result()
                case = next(c for c in cases if c["id"] == cid)
                f, info = evaluate(case, out / cid / sub, err)
                results[cid].append((sub, f, info))
                print(f"  {cid}{' ' + sub if sub else ''}: {'pass' if not f else 'FAIL'} in {secs}s", flush=True)
        if any(r[-1][2].get("not_run") for r in results.values()):
            print("  account limit hit: stopping, no retries", flush=True)
            break
        todo = [(c, f"retry{attempt + 1}") for c in cases if results[c["id"]][-1][1]]
        if not todo:
            break
    rows = []
    for c in cases:
        tries = results[c["id"]]
        sub, f, info = tries[-1]
        earlier = [f"{s or 'first run'} failed: {'; '.join(x)}" for s, x, _ in tries[:-1]]
        if earlier:
            info = {**info, "earlier": earlier}
        rows.append((c["id"] + (f" ({sub})" if sub else ""), f, info))
    ok, text = report(out, pre, rows, repo)
    print("\n" + text + f"\nFull results: {out}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
