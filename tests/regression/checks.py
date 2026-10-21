"""Checks for one ask-jeeves regression run: the memo and the tool-call trace.

Stdlib only. `run.py` calls `check_case`; `python3 checks.py <memo.md>` checks a saved memo's
sections and word count by itself.
"""
import json
import re
import sys
from pathlib import Path

# Pinned from templates/memo.md on main (ticket 30). Pinned, not read from the skill under test,
# so a skill change that drops a section fails here. `template_drift` flags a deliberate change.
EXPECTED_SECTIONS = [
    "Bottom line",
    "Path to your goal",
    "State applied and why",
    "Risks",
    "Recommendations",
    "Creative option",
    "Questions for a licensed attorney",
    "Adjacent issues flagged",
    "Sources",
]
# The template's word count covers these sections only.
PROSE_SECTIONS = [
    "Bottom line",
    "Path to your goal",
    "State applied and why",
    "Recommendations",
    "Creative option",
    "Questions for a licensed attorney",
    "Adjacent issues flagged",
]
WORDS_MIN, WORDS_MAX = 600, 900
DISCLAIMER = "Not legal advice. Jeeves spots issues to raise with a licensed attorney; it is not a lawyer."
DEPTH = {
    "quick": {"depth": "Quick", "label": "Unverified against current sources", "ending": "Verification: none this request."},
    "intermediate": {"depth": "Intermediate", "label": "quick-verified", "ending": "Verification: quick-verified."},
}
# Research that depends on the applied state (SKILL.md step 4): any web or subagent call, or reading a
# state card. A headless run often loads the built-in area files up front, before step 3. Those
# hold federal, IN and SC law whichever state is picked, so reading them early doesn't count.
RESEARCH_FILES = re.compile(r"references/state-cards/[A-Z]{2}\.md")
RESEARCH_TOOLS = {"WebSearch", "WebFetch", "Agent", "Task"}
STATES = {
    "Indiana": "IN", "South Carolina": "SC", "Georgia": "GA", "North Carolina": "NC",
    "Tennessee": "TN", "Florida": "FL", "Federal": "US",
}
# Grant's real run log and refresh queue. Test runs may read them, never write them.
LOG_FILES = re.compile(r"ask-jeeves-(run-log|refresh-queue)\.md")
MEMO_START, MEMO_END = "=== MEMO START ===", "=== MEMO END ==="


def template_drift(template_path):
    """The template's ## headings, when they no longer match EXPECTED_SECTIONS."""
    text = Path(template_path).read_text()
    block = text.split("```", 2)[1] if "```" in text else text
    found = [l[3:].strip() for l in block.splitlines() if l.startswith("## ")]
    return None if found == EXPECTED_SECTIONS else found


# ---------- trace ----------

def load_trace(path):
    """Events from a `claude -p --output-format stream-json` file, in order."""
    events = []
    for line in Path(path).read_text().splitlines():
        line = line.strip()
        if line.startswith("{"):
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return events


def steps(events):
    """Flatten the trace to (kind, payload, in_subagent): kind is 'text' or 'tool'."""
    out = []
    for ev in events:
        if ev.get("type") != "assistant":
            continue
        sub = bool(ev.get("parent_tool_use_id"))
        for block in ev.get("message", {}).get("content", []):
            if block.get("type") == "text":
                out.append(("text", block.get("text", ""), sub))
            elif block.get("type") == "tool_use":
                out.append(("tool", {"name": block.get("name"), "input": block.get("input", {})}, sub))
    return out


def result_event(events):
    for ev in reversed(events):
        if ev.get("type") == "result":
            return ev
    return {}


def is_research(tool):
    if tool["name"] in RESEARCH_TOOLS:
        return True
    if tool["name"] == "Read":
        return bool(RESEARCH_FILES.search(str(tool["input"].get("file_path", ""))))
    return False


def extract_memo(trace_steps, result_text=""):
    texts = [p for k, p, sub in trace_steps if k == "text" and not sub] + [result_text or ""]
    for t in reversed(texts):
        if MEMO_START in t and MEMO_END in t:
            return t.split(MEMO_START, 1)[1].split(MEMO_END, 1)[0].strip()
    for t in reversed(texts):
        if "# Jeeves memo:" in t:
            return t[t.index("# Jeeves memo:"):].strip()
    return ""


# ---------- memo ----------

def sections(memo):
    """{heading: body} for each ## section, plus '_header' and the ordered heading list."""
    out, order, cur, buf = {}, [], "_header", []
    for line in memo.splitlines():
        if line.startswith("## "):
            out[cur] = "\n".join(buf)
            cur, buf = line[3:].strip(), []
            order.append(cur)
        else:
            buf.append(line)
    out[cur] = "\n".join(buf)
    return out, order


def find_section(secs, name):
    for k in secs:
        if k.lower().startswith(name.lower()):
            return secs[k]
    return None


def prose_words(memo):
    """Words of prose as templates/memo.md counts them."""
    secs, _ = sections(memo)
    total = 0
    for name in PROSE_SECTIONS:
        body = find_section(secs, name) or ""
        for line in body.splitlines():
            s = line.strip()
            if not s or s.startswith("|") or s.startswith(">") or s.startswith("*In plain terms"):
                continue
            s = re.sub(r"\*\*[^*]+\*\*", " ", s)        # bold labels
            s = re.sub(r"\[[^\]]*\]", " ", s)            # citations
            s = re.sub(r"\(#[\d, #]+\)", " ", s)         # risk refs like (#1)
            s = re.sub(r"^(\d+\.|[-*])\s+", "", s)       # list markers
            total += sum(1 for w in s.split() if re.search(r"[A-Za-z0-9]", w))
    return total


def check_memo(memo, depth):
    """Structure and length failures for a memo at `depth` ('quick' or 'intermediate')."""
    fails = []
    if not memo:
        return ["no memo found in the run output"]
    lines = [l for l in memo.splitlines() if l.strip()]
    if not lines[0].startswith("# Jeeves memo:"):
        fails.append("first line is not '# Jeeves memo: …'")
    if DISCLAIMER not in memo:
        fails.append("disclaimer missing")
    head = "\n".join(lines[:6])
    if not re.search(r"^Goal:", head, re.M):
        fails.append("header has no Goal: line")
    mode = next((l for l in lines[:6] if l.startswith("Mode:")), "")
    d = DEPTH[depth]
    if not mode:
        fails.append("header has no Mode: line")
    else:
        if f"Depth: {d['depth']}" not in mode:
            fails.append(f"Mode line lacks 'Depth: {d['depth']}'")
        if d["label"] not in mode:
            fails.append(f"Mode line lacks the label '{d['label']}'")
        if "Applied state:" not in mode:
            fails.append("Mode line lacks 'Applied state:'")
    secs, order = sections(memo)
    got = [next((e for e in EXPECTED_SECTIONS if h.lower().startswith(e.lower())), None) for h in order]
    for e in EXPECTED_SECTIONS:
        if e not in got:
            fails.append(f"section missing: ## {e}")
    present = [g for g in got if g]
    if present != [e for e in EXPECTED_SECTIONS if e in present]:
        fails.append("sections out of template order: " + ", ".join(present))
    bl = find_section(secs, "Bottom line") or ""
    if not re.search(r"\*\*Goal:\*\*\s*(Likely|Uncertain|Unlikely)", bl):
        fails.append("Bottom line doesn't open with **Goal:** Likely/Uncertain/Unlikely")
    st = find_section(secs, "State applied") or ""
    if "Confirm the applied state with a licensed attorney" not in st:
        fails.append("State applied lacks the confirm-with-an-attorney line")
    rec = find_section(secs, "Recommendations") or ""
    for g in ("Before signing", "On the job", "When leaving"):
        if f"**{g}" not in rec:
            fails.append(f"Recommendations lacks the **{g}** group")
    cr = find_section(secs, "Creative option") or ""
    for label in ("Creative, not standard practice", "**Risk:**", "**Enforceability:**"):
        if label not in cr:
            fails.append(f"Creative option lacks {label}")
    risks = find_section(secs, "Risks") or ""
    rows = [l for l in risks.splitlines() if re.match(r"\|\s*\d+\s*\|", l)]
    if not rows:
        fails.append("Risks table has no rows")
    elif len(rows) > 6:
        fails.append(f"Risks table has {len(rows)} rows (max 6)")
    if d["ending"] not in memo:
        fails.append(f"verification ending lacks '{d['ending']}'")
    if not re.search(r"\[\d+", memo):
        fails.append("no [n] citations")
    n = prose_words(memo)
    if not WORDS_MIN <= n <= WORDS_MAX:
        fails.append(f"prose is {n} words (template: {WORDS_MIN}–{WORDS_MAX})")
    return fails


def check_planted_citation(memo, depth, name="Hartwell"):
    """The fake case must carry NOT CHECKED (quick) or NOT FOUND (intermediate) and never support."""
    fails = []
    secs, _ = sections(memo)
    src = find_section(secs, "Sources") or ""
    src_lines = [l for l in src.splitlines() if name in l]
    want = "NOT CHECKED" if depth == "quick" else "NOT FOUND"
    wrong = "NOT FOUND" if depth == "quick" else "NOT CHECKED"
    if not src_lines:
        return [f"planted citation ({name}) not listed in Sources"]
    if not any(want in l for l in src_lines):
        fails.append(f"planted citation not marked {want} in Sources: {src_lines[0][:160]}")
    if any(wrong in l for l in src_lines):
        fails.append(f"planted citation marked {wrong} at {depth}")
    if depth != "quick" and any(re.search(r"\(confirmed", l) for l in src_lines):
        fails.append("planted citation marked confirmed")
    num = re.match(r"\s*\[(\d+)", src_lines[0])
    if num:
        n = num.group(1)
        body = memo.split("## Sources", 1)[0]
        # A bare [n] is fine right beside its label, as in "[NOT CHECKED: quick mode] [27]".
        bare = [m for m in re.finditer(rf"\[{n}\]", body)
                if want.lower() not in body[max(0, m.start() - 40):m.end() + 40].lower()]
        if bare:
            fails.append(f"planted citation [{n}] used bare {len(bare)}x in the memo body (needs its {want} label)")
    if depth != "quick":
        bl = find_section(secs, "Bottom line") or ""
        if name not in bl and "NOT FOUND" not in bl:
            fails.append("intermediate Bottom line doesn't list the NOT FOUND input citation")
    return fails


# ---------- state confirmation ----------

def check_state_confirmation(trace_steps, expect=None):
    """The candidate-state block and its confirmation question come before any research.

    `expect`: optional {"states": {"IN", "SC"}, "confidence": "Uncertain"} for the mismatch flow.
    """
    fails, info = [], {}
    cand_i = conf_i = ans_i = None
    for i, (kind, p, sub) in enumerate(trace_steps):
        if kind != "text" or sub:
            continue
        if cand_i is None and "Candidate state:" in p:
            cand_i, info["block"] = i, p[p.index("Candidate state:"):][:4000]
        if cand_i is not None and conf_i is None and re.search(r"OPTIONS:[^\n]*Confirm", p):
            conf_i = i
        if conf_i is not None and ans_i is None:
            # The answer follows the confirmation's OPTIONS line, in the same block or a later one.
            seg = p[p.rfind("OPTIONS:"):] if i == conf_i else p
            if "SCRIPTED ANSWER:" in seg:
                ans_i = i
                info["answer"] = seg.split("SCRIPTED ANSWER:", 1)[1].splitlines()[0].strip()
    first_research = next((i for i, (k, p, s) in enumerate(trace_steps) if k == "tool" and is_research(p)), None)
    info["first_research"] = None if first_research is None else trace_steps[first_research][1]["name"]
    if cand_i is None:
        return ["no 'Candidate state:' block shown"], info
    if conf_i is None:
        fails.append("no state-confirmation question (OPTIONS with 'Confirm …') after the candidate block")
    if ans_i is None:
        fails.append("no scripted answer to the state confirmation")
    gate = ans_i if ans_i is not None else (conf_i if conf_i is not None else cand_i)
    if first_research is not None and first_research < gate:
        fails.append(f"research ({trace_steps[first_research][1]['name']}) ran before the state was confirmed")
    if "Confirm the applied state with a licensed attorney" not in info["block"]:
        fails.append("candidate block lacks 'Confirm the applied state with a licensed attorney…'")
    prim = re.search(r"Candidate state:\s*\**([A-Za-z .]+?)\**\s*[.(]", info["block"])
    back = re.search(r"Backup:\s*\**([A-Za-z .]+?)\**\s*[.(]", info["block"])
    info["primary"] = prim.group(1).strip() if prim else None
    info["backup"] = back.group(1).strip() if back else None
    if expect:
        block = info["block"]
        got = {STATES.get(m.group(1).strip(), m.group(1).strip()) for m in (prim, back) if m}
        if got != expect["states"]:
            fails.append(f"primary/backup are {sorted(got)}, expected {sorted(expect['states'])}")
        if expect.get("confidence") and not re.search(rf"Confidence:\s*\**{expect['confidence']}", block):
            fails.append(f"Confidence is not {expect['confidence']}")
    return fails, info


def check_applied_state(memo, sinfo):
    """The memo's header uses the state the scripted answer confirmed."""
    ans, prim, back = sinfo.get("answer") or "", sinfo.get("primary"), sinfo.get("backup")
    mode = next((l for l in memo.splitlines() if l.startswith("Mode:")), "")
    m = re.search(r"Applied state:\s*\**([A-Za-z .]+?)\**\s*[(·;]", mode)
    applied = m.group(1).strip() if m else None
    if not (ans and prim and applied):
        return []
    if re.search(r"Use .+ instead", ans):
        want = back
    else:
        want = prim
    fails = []
    # "Indiana" and "IN" name the same state; compare postal codes.
    code = lambda x: STATES.get(x.strip().rstrip("."), x.strip().rstrip("."))
    if want and code(applied) != code(want):
        fails.append(f"memo applies {applied}, but the confirmed answer was '{ans}' ({want})")
    if "backup notes" in ans.lower() and back and f"backup: {back}" not in mode.replace("**", ""):
        fails.append(f"answer kept {back} as backup, but the Mode line lacks 'backup: {back}'")
    return fails


def check_pdf_read(events, pdf, tell="Keystone Ledger"):
    """The PDF reached the run: through pdf-text.swift, or a Read that worked.

    reading-input.md sends a PDF to pdf-text.swift only when Read fails on it. Read sometimes
    hands the encrypted fixture (empty user password) to the model as a document block, so either
    route passes. The preflight runs pdf-text.swift on both fixtures itself, and the mismatch
    checks prove the contract's content arrived.
    """
    calls, hits = {}, set()
    for ev in events:
        for b in ev.get("message", {}).get("content", []) if isinstance(ev.get("message"), dict) else []:
            if b.get("type") == "tool_use":
                inp = json.dumps(b.get("input", {}))
                if pdf in inp and ("pdf-text.swift" in inp or b.get("name") == "Read"):
                    calls[b.get("id")] = "pdf-text.swift" if "pdf-text.swift" in inp else "Read"
            elif b.get("type") == "tool_result":
                c = b.get("content", "")
                # Read returns either extracted text or the PDF itself as a document block,
                # which the model reads natively.
                if tell in json.dumps(c) or (isinstance(c, list) and any(x.get("type") == "document" for x in c if isinstance(x, dict))):
                    hits.add(b.get("tool_use_id"))
    swift = [i for i, how in calls.items() if how == "pdf-text.swift"]
    if swift:
        return []  # the script wrote all.txt; the run reads it next, and the memo checks cover the content
    if any(i in hits for i in calls):
        return []
    return [f"{pdf}: no pdf-text.swift run, and no Read of it returned the contract text"]


def tool_counts(trace_steps):
    counts = {}
    for k, p, s in trace_steps:
        if k == "tool":
            counts[p["name"]] = counts.get(p["name"], 0) + 1
    return counts


def check_case(case, trace_path):
    """All failures for one case, plus a short info dict for the report."""
    events = load_trace(trace_path)
    st = steps(events)
    res = result_event(events)
    memo = extract_memo(st, res.get("result", ""))
    counts = tool_counts(st)
    fails = []
    limit = re.search(r"out of usage credits|usage limit|rate limit", str(res.get("result", "")), re.I)
    if res.get("is_error") and limit:
        # The account hit a limit before the skill ran: nothing about the skill was tested.
        return [f"NOT RUN: account limit ({limit.group(0)}); re-run when usage resets"], {"not_run": True}, ""
    if not events:
        fails.append("empty trace (claude -p produced no events)")
    if res.get("is_error"):
        fails.append(f"run ended in error: {res.get('subtype')} {str(res.get('result'))[:200]}")
    fails += check_memo(memo, case["depth"])
    web = counts.get("WebSearch", 0) + counts.get("WebFetch", 0)
    if case["depth"] == "quick" and web:
        fails.append(f"quick made {web} web calls (allowed: 0)")
    if case["depth"] == "intermediate":
        if counts.get("WebSearch", 0) > 8:
            fails.append(f"intermediate used {counts['WebSearch']} WebSearch calls (max 8)")
        if not web:
            fails.append("intermediate made no web calls")
    if case.get("planted"):
        fails += check_planted_citation(memo, case["depth"], case["planted"])
    sf, sinfo = check_state_confirmation(st, case.get("expect_state"))
    fails += sf
    fails += check_applied_state(memo, sinfo)
    for k, p, s in st:
        if k == "tool" and p["name"] != "Read" and LOG_FILES.search(json.dumps(p["input"])):
            fails.append(f"a {p['name']} call touched {LOG_FILES.search(json.dumps(p['input'])).group(0)} "
                         "(test runs must not log; check that file by hand)")
            break
    if case.get("pdf"):
        fails += check_pdf_read(events, case["pdf"])
    info = {
        "words": prose_words(memo) if memo else 0,
        "tools": counts,
        "state_answer": sinfo.get("answer"),
        "cost_usd_list": round(res.get("total_cost_usd") or 0, 2),
        "seconds": round((res.get("duration_ms") or 0) / 1000),
    }
    return fails, info, memo


if __name__ == "__main__":
    for p in sys.argv[1:]:
        m = Path(p).read_text()
        depth = "intermediate" if "Depth: Intermediate" in m else "quick"
        f = check_memo(m, depth)
        print(f"{p}: {prose_words(m)} words, {depth}: " + ("PASS" if not f else "FAIL\n  - " + "\n  - ".join(f)))
