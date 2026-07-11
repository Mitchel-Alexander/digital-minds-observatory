#!/usr/bin/env python3
"""Build the DMEI evidence dashboard (single self-contained HTML).

v4 (2026-07-11, Mitchel's refinements on v3):
  - partial = flat light blue everywhere (stripes dropped; thin border keeps
    the mark delineated on white)
  - heatmap cells are CLICKABLE -> side panel lists that topic area's
    indicators for that developer/year, each opening its evidence
  - per-developer "Learn more" modal: per-document view (every corpus
    document incl. zero-evidence ones) + stage recap
  - the full record grid is COLLAPSED by default (permalinks auto-expand)
Rebuild:  python3 build_dmei_dashboard.py   ->  dmei-dashboard.html
"""
import json, csv, html, re, collections
from pathlib import Path

HERE = Path(__file__).resolve().parent
DP = HERE.parent / "dm-developer-positions"

reg = json.load(open(HERE / "registry-v40.json"))
DEVS = [("anthropic", "Anthropic"), ("openai", "OpenAI"), ("google", "Google")]
STAGE_N = {"Acknowledge": 45, "Assess": 27, "Prepare": 28}
YEARS = list(range(2019, 2027))

READINGS = {
    "anthropic": "Anthropic&rsquo;s formal documents engage nearly the whole framework: "
        "direct evidence on <strong>79 of the 100 indicators</strong>, spanning acknowledgment, "
        "measurement, and operating practice &mdash; almost all of it entering the record in "
        "2025&ndash;26.",
    "openai": "OpenAI&rsquo;s documents engage selectively: direct evidence on "
        "<strong>10 indicators</strong> &mdash; concentrated on how systems are perceived and how the "
        "assistant should describe itself &mdash; with partial evidence on 26 more. Its record starts "
        "earliest (2023) but has grown little since 2025.",
    "google": "Google&rsquo;s formal documents contain <strong>no direct evidence on any of the 100 "
        "indicators</strong>; on 21, safety work approaches the territory without engaging the "
        "digital-minds framing. Every cell in its heatmap is partial evidence.",
}
S2_TITLE = ("Nearly all of this engagement is new &mdash; the public record barely existed "
            "before 2024, and most of it dates from 2025&ndash;26.")

def short(doc):
    return (doc or "").replace(".txt", "").replace("anthropic-", "").replace("openai-", "").replace("google-", "")

def year_of(doc):
    m = re.search(r"(20\d\d)", doc or "")
    return int(m.group(1)) if m else None

# ---------- evidence assembly ----------
arm = {d: {} for d, _ in DEVS}
for dev in ["google", "openai"]:
    for line in open(HERE / f"pilot-arm-{dev}-verdicts.jsonl"):
        r = json.loads(line)
        arm[dev][r["indicator"]] = {
            "status": r["status"],
            "ev": [{"q": r["quote"], "d": short(r["doc"]), "g": r["rationale"]}] if r.get("quote") else [],
            "why": r["rationale"], "searches": r.get("searches", [])}

p2 = {json.loads(l)["indicator"]: json.loads(l) for l in open(HERE / "pilot-pass2-verdicts.jsonl")}
mapping = json.load(open(HERE / "pilot-anthropic-mapping-pass1.json"))
findings = {r["finding_id"]: r for r in csv.DictReader(open(DP / "anthropic-welfare-findings.csv"))}
ind2f = collections.defaultdict(lambda: {"best": [], "other": []})
for fid, m in mapping.items():
    for i in m["indicators"]:
        ind2f[i]["best" if m.get("best") == i else "other"].append(fid)

for e in reg:
    i = e["id"]
    if i in ind2f:
        picks = (ind2f[i]["best"] + ind2f[i]["other"])[:3]
        n_all = len(ind2f[i]["best"]) + len(ind2f[i]["other"])
        ev = [{"q": findings[f]["quote"], "d": short(findings[f]["doc_id"]), "g": findings[f]["gloss"]} for f in picks]
        arm["anthropic"][i] = {"status": "found", "ev": ev,
            "why": f"{n_all} candidate passage(s) in the quote-verified findings layer; showing {len(ev)}.", "searches": []}
    else:
        r = p2[i]
        arm["anthropic"][i] = {"status": r["status"],
            "ev": [{"q": r["quote"], "d": short(r["doc"]), "g": r["rationale"]}] if r.get("quote") else [],
            "why": r["rationale"], "searches": r.get("searches", [])}


# ---------- per-document counts (for the Learn-more modal) ----------
PUB = {"anthropic": "anthropic", "openai": "openai", "google": "google"}
registry_docs = [r for r in csv.DictReader(open(DP / "documents.csv")) if r["publisher"] in PUB.values()]
def doc_counts(dev):
    cnt = collections.defaultdict(lambda: [0, 0])  # short doc -> [direct, partial]
    if dev == "anthropic":
        for i, d in ind2f.items():
            for doc in {short(findings[f]["doc_id"]) for f in d["best"] + d["other"]}:
                cnt[doc][0] += 1
        for i, r in p2.items():
            if r.get("doc"):
                cnt[short(r["doc"])][0 if r["status"] == "found" else 1] += 1
    else:
        for i, c in arm[dev].items():
            if c["ev"]:
                cnt[c["ev"][0]["d"]][0 if c["status"] == "found" else 1] += 1
    rows = []
    for r in registry_docs:
        if r["publisher"] != dev: continue
        s = short(r["doc_id"])
        nf, np_ = cnt.get(s, [0, 0])
        rows.append({"t": r["title"], "y": r["date"][:4], "date": r["date"], "s": s, "nf": nf, "np": np_})
    rows.sort(key=lambda x: x["date"])
    return rows
DOCROWS = {dev: doc_counts(dev) for dev, _ in DEVS}

# ---------- groups ----------
seen = collections.OrderedDict()
for e in reg:
    seen.setdefault((e["stage"], e["subdomain"]), []).append(e["id"])
GROUPS = [{"stage": k[0], "sub": k[1], "ids": v} for k, v in seen.items()]

# ---------- S1 stage columns ----------
STAGE_META = {
    "Acknowledge": ("Does the company say the question matters?", "e.g. does it acknowledge its systems might have welfare?"),
    "Assess": ("Has it tried to measure or evaluate it?", "e.g. does it assess its models&rsquo; possible welfare?"),
    "Prepare": ("Has it changed how it operates in response?", "e.g. does it have welfare-relevant policies or roles?"),
}
prof = {d: {stg: collections.Counter(arm[d][e["id"]]["status"] for e in reg if e["stage"] == stg)
        for stg in STAGE_N} for d, _ in DEVS}

MAXSTAGE = max(STAGE_N.values())  # shared scale: one indicator = equal width in every card

def stage_col(stg):
    q, eg = STAGE_META[stg]
    key = ('<div class="prow pkey"><span></span>'
           '<span class="pnum key" style="grid-column:2/4">'
           '<span class="kf">direct</span> <span class="kp">partial</span> <span class="kn">none</span></span></div>')
    rows = ""
    n = STAGE_N[stg]
    track_pct = 100 * n / MAXSTAGE
    for dev, label in DEVS:
        c = prof[dev][stg]
        f, p, nf = c.get("found", 0), c.get("partial", 0), c.get("not_found", 0)
        tip = f"{label}: of {n} {stg} indicators — {f} with direct evidence, {p} partial, {nf} with no public evidence"
        seg = ""
        if f: seg += f'<span class="sg f" style="width:{100*f/n:.1f}%"></span>'
        if p: seg += f'<span class="sg p" style="width:{100*p/n:.1f}%"></span>'
        rows += (f'<div class="prow" title="{html.escape(tip)}"><span class="plab">{label}</span>'
                 f'<span class="tcell"><span class="ptrack" style="width:{track_pct:.1f}%">{seg}</span></span>'
                 f'<span class="pnum">{f} &middot; {p} &middot; {nf}</span></div>')
    return (f'<div class="stg"><span class="sk">{stg}</span><p class="q1">{q}</p>'
            f'<p class="n">{STAGE_N[stg]} indicators &mdash; {eg}</p>{key}{rows}</div>')

stage_cols = "".join(stage_col(s) for s in ["Acknowledge", "Assess", "Prepare"])

# ---------- S2 heatmaps (clickable cells) ----------
SUBSHORT = {
    "Ontological framing": "Ontological framing", "Consciousness & subjective experience": "Consciousness & experience",
    "Cognition & internal states": "Cognition & internal states", "Welfare capacity (aversive & positive states)": "Welfare capacity",
    "Moral status & criteria": "Moral status & criteria", "Identity & individuation": "Identity & individuation",
    "Welfare as an organisational concern": "Welfare as org. concern", "Safety–welfare interaction": "Safety–welfare interaction",
    "Responsible communication": "Responsible communication", "Welfare interests": "Welfare interests",
    "Emotional alignment": "Emotional alignment", "Consciousness assessment": "Consciousness assessment",
    "Cognition & internal-states assessment": "Cognition assessment", "Welfare-capacity assessment": "Welfare-capacity assessment",
    "Moral-status assessment": "Moral-status assessment", "Identity assessment": "Identity assessment",
    "Welfare-assessment methods & welfare case": "Welfare-assessment methods", "Integrated safety–welfare assessment": "Integrated safety–welfare",
    "Responsible-research assessment": "Responsible-research assessment", "Welfare-interests assessment": "Welfare-interests assessment",
    "Emotional-alignment assessment": "Emotional-alignment assessment", "Welfare governance & accountability": "Welfare governance",
    "Welfare-protective practices": "Welfare-protective practices", "Safety–welfare coordination": "Safety–welfare coordination",
    "Emotional alignment & design": "Emotional alignment & design", "Responsible-research practices": "Responsible-research practices",
}

def heat_cell(dev, gi, ids, Y):
    idocs = INDDOCS[dev]
    nf = sum(1 for i in ids if any(year_of(d) == Y for d in idocs.get(i, {}).get("d", ())))
    np_ = sum(1 for i in ids if any(year_of(d) == Y for d in idocs.get(i, {}).get("p", ())))
    if nf:
        op = 0.45 if nf == 1 else (0.7 if nf <= 3 else 1.0)
        style = f"background:rgba(47,127,230,{op})"; cls = "hmc"
    elif np_:
        style = "background:#c7e0fb"; cls = "hmc"
    else:
        style = ""; cls = "hmc empty"
    tip = f"{Y}: {nf} direct, {np_} partial of {len(ids)} — click for detail"
    return (f'<button class="{cls}" style="{style}" data-g="{gi}" data-y="{Y}" '
            f'title="{html.escape(tip)}" aria-label="{html.escape(tip)}"></button>')

SHORTDOC = {
    "general-language-assistant-paper-2021": "HHH paper \u201921", "responsible-scaling-policy-2023": "RSP 1.0 \u201923",
    "claude-3-model-card-2024": "Claude 3 \u201924", "claude-3-7-sonnet-system-card-2025": "3.7 Sonnet \u201925",
    "claude-opus-4-sonnet-4-system-card-2025": "Opus 4 \u201925", "claude-opus-4-5-system-card-2025": "Opus 4.5 \u201925",
    "claude-constitution-persona-2026": "Constitution \u201926", "claude-opus-4-6-system-card-2026": "Opus 4.6 \u201926",
    "responsible-scaling-policy-2026": "RSP 3.1 \u201926", "opus48-system-card-2026": "Opus 4.8 \u201926",
    "fable5-mythos5-system-card-2026": "Fable/Mythos 5 \u201926",
    "gpt2-model-card-2019": "GPT-2 \u201919", "gpt3-model-card-2020": "GPT-3 \u201920",
    "dalle2-system-card-2022": "DALL\u00b7E 2 \u201922", "gpt4-system-card-2023": "GPT-4 \u201923",
    "gpt4o-system-card-2024": "GPT-4o \u201924", "o1-system-card-2024": "o1 \u201924",
    "gpt4-5-system-card-2025": "GPT-4.5 \u201925", "preparedness-framework-2025": "Preparedness FW \u201925",
    "o3-o4-mini-system-card-2025": "o3/o4-mini \u201925", "gpt5-system-card-2025": "GPT-5 \u201925",
    "model-spec-2025": "Model Spec \u201925",
    "gopher-technical-report-2021": "Gopher \u201921", "gemini-1-0-technical-report-2023": "Gemini 1.0 \u201923",
    "gemini-1-5-technical-report-2024": "Gemini 1.5 \u201924", "frontier-safety-framework-1-2024": "FSF 1 \u201924",
    "gemini-2-5-pro-model-card-2025": "Gemini 2.5 Pro \u201925", "frontier-safety-framework-3-2025": "FSF 3 \u201925",
    "gemini-3-pro-fsf-safety-report-2025": "Gemini 3 FSF report \u201925", "gemini-3-pro-model-card-2025": "Gemini 3 Pro \u201925",
}

def ind_docs(dev):
    """per indicator: which documents give direct / partial evidence"""
    out = {}
    if dev == "anthropic":
        for i in (e["id"] for e in reg):
            dd, pp = set(), set()
            if i in ind2f:
                dd = {short(findings[f]["doc_id"]) for f in ind2f[i]["best"] + ind2f[i]["other"]}
                r = p2.get(i)
            else:
                r = p2.get(i)
            if r and r.get("doc"):
                (dd if r["status"] == "found" else pp).add(short(r["doc"]))
            if dd or pp: out[i] = {"d": sorted(dd), "p": sorted(pp - dd)}
    else:
        for i, c in arm[dev].items():
            if not c["ev"]: continue
            doc = c["ev"][0]["d"]
            out[i] = {"d": [doc] if c["status"] == "found" else [], "p": [doc] if c["status"] == "partial" else []}
    return out
INDDOCS = {dev: ind_docs(dev) for dev, _ in DEVS}

def doc_matrix_html(dev):
    docs = DOCROWS[dev]
    nd = len(docs)
    zero = {d["s"] for d in docs if d["nf"] == 0 and d["np"] == 0}
    head = ""
    for d in docs:
        lab = SHORTDOC.get(d["s"], d["s"])
        cls = "dhlab zero" if d["s"] in zero else "dhlab"
        head += f'<span class="{cls}" title="{html.escape(d["t"])} ({d["y"]})">{html.escape(lab)}</span>'
    rows = f'<div class="hmrow dmxh"><span class="hmlab"></span><span class="hmcells">{head}</span></div>'
    cur_stage = ""
    idocs = INDDOCS[dev]
    for gi, g in enumerate(GROUPS):
        if g["stage"] != cur_stage:
            cur_stage = g["stage"]
            rows += f'<div class="hmstage">{cur_stage}</div>'
        cells = ""
        for d in docs:
            key = d["s"]
            nf = sum(1 for i in g["ids"] if key in idocs.get(i, {}).get("d", ()))
            np_ = sum(1 for i in g["ids"] if key in idocs.get(i, {}).get("p", ()))
            if nf:
                op = 0.45 if nf == 1 else (0.7 if nf <= 3 else 1.0)
                style = f"background:rgba(47,127,230,{op})"; cls = "hmc dmxc"
            elif np_:
                style = "background:#c7e0fb"; cls = "hmc dmxc"
            else:
                style = ""; cls = "hmc dmxc empty"
            tip = f'{SHORTDOC.get(key, key)}: {nf} direct, {np_} partial of {len(g["ids"])} \u2014 click for detail'
            cells += (f'<button class="{cls}" style="{style}" data-g="{gi}" data-doc="{html.escape(key)}" '
                      f'title="{html.escape(tip)}" aria-label="{html.escape(tip)}"></button>')
        lab = SUBSHORT.get(g["sub"], g["sub"])
        rows += f'<div class="hmrow"><span class="hmlab">{lab}</span><span class="hmcells">{cells}</span></div>'
    return (f'<div class="hm dmx" style="--nd:{nd}">{rows}</div>'
            f'<p class="caveat" style="margin-top:10px">Same rows as the topic view; columns are the developer&rsquo;s '
            f'documents in publication order. A cell shows how many indicators in that topic area are evidenced by '
            f'that document; greyed columns are documents with no digital-minds content &mdash; their silence is part '
            f'of the record.</p>')

def dev_block(dev, label):
    rows = ""; cur_stage = ""
    for gi, g in enumerate(GROUPS):
        if g["stage"] != cur_stage:
            cur_stage = g["stage"]
            rows += f'<div class="hmstage">{cur_stage}</div>'
        cells = "".join(heat_cell(dev, gi, g["ids"], Y) for Y in YEARS)
        lab = SUBSHORT.get(g["sub"], g["sub"])
        rows += f'<div class="hmrow"><span class="hmlab">{lab}</span><span class="hmcells">{cells}</span></div>'
    yhead = "".join(f'<span class="hmyr">{y}</span>' for y in YEARS)
    return (f'<div class="devblock" data-dev="{dev}"><div class="devhead"><h3>{label}</h3></div>'
            f'<p class="reading">{READINGS[dev]}</p>'
            f'<div class="view view-topic"><div class="hm"><div class="hmrow hmhead"><span class="hmlab"></span>'
            f'<span class="hmcells">{yhead}</span></div>{rows}</div></div>'
            f'<div class="view view-docs" hidden>{doc_matrix_html(dev)}</div></div>')

dev_blocks = "".join(dev_block(dev, label) for dev, label in DEVS)

# ---------- payload ----------
payload = {
    "devs": DEVS,
    "reg": {e["id"]: {"name": e["name"], "def": e["definition"], "stage": e["stage"], "sub": e["subdomain"]} for e in reg},
    "groups": GROUPS,
    "cells": {d: arm[d] for d, _ in DEVS},
    "inddocs": INDDOCS,
    "docmeta": {dev: {d["s"]: {"lab": SHORTDOC.get(d["s"], d["s"]), "t": d["t"]} for d in DOCROWS[dev]} for dev, _ in DEVS},
}

page = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Digital Minds Engagement Index — the public record</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{--paper:#ffffff;--ink:#171717;--muted:#6b7280;--faint:#9aa0ac;--line:#e5e7eb;
--blue:#2f7fe6;--blue-lt:#c7e0fb;--blue-bd:#8fb8ee;--accent:#4098ff;--accent-light:rgba(64,152,255,.10);--card:#f9fafb}
*{box-sizing:border-box;margin:0}
body{background:var(--paper);color:var(--ink);font:400 15px/1.6 "Plus Jakarta Sans",system-ui,sans-serif;padding:40px 20px 80px}
::selection{background:#afd3f9;color:var(--ink)}
.wrap{max-width:1060px;margin:0 auto}
.kicker{font:600 11px/1 "Plus Jakarta Sans";letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
h1{font:600 40px/1.13 "Cormorant Garamond",serif;letter-spacing:-.01em;margin:10px 0 14px}
.lede{max-width:760px;color:rgba(23,23,23,.72)}
.caveat{max-width:760px;margin-top:10px;font-size:13px;color:var(--faint)}
section{margin-top:56px}
h2{font:600 27px/1.25 "Cormorant Garamond",serif;letter-spacing:-.01em;margin-bottom:6px;max-width:820px}
.sub{color:var(--muted);font-size:13.5px;max-width:740px;margin-bottom:18px}
.stages{display:grid;grid-template-columns:1fr;gap:14px;margin:18px 0 0}
.stg{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px}
.stg .sk{font:600 11px/1 "Plus Jakarta Sans";letter-spacing:.14em;text-transform:uppercase;color:var(--accent)}
.stg .q1{font-size:14.5px;font-weight:600;color:var(--ink);margin-top:7px}
.stg .n{font-size:12px;color:var(--faint);margin:4px 0 12px}
.prow{display:grid;grid-template-columns:96px 1fr 84px;gap:12px;align-items:center;margin:7px 0}
.plab{font-size:12px;color:var(--muted)}
.tcell{display:block}
.ptrack{height:14px;border:1.4px solid var(--line);border-radius:5px;overflow:hidden;display:flex;background:#eef1f5}
.sg{display:block;height:100%}
.sg.f{background:var(--blue);border-right:2px solid #fff}
.sg.p{background:var(--blue-lt)}
.pnum{font-size:12px;color:var(--muted);text-align:right;font-variant-numeric:tabular-nums}
.pkey{margin:2px 0 -1px}
.pnum.key{font-size:9.5px;letter-spacing:.02em;text-transform:uppercase;color:var(--faint);white-space:nowrap}
.pnum.key span{margin-left:7px}
.pnum.key span::before{content:"";display:inline-block;width:7px;height:7px;border-radius:2px;margin-right:3px;vertical-align:0}
.kf::before{background:var(--blue)}
.kp::before{background:var(--blue-lt);border:1px solid var(--blue-bd)}
.kn::before{background:#eef1f5;border:1px solid var(--line)}
.devblock{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:20px 22px;margin-top:18px}
.devhead{display:flex;justify-content:space-between;align-items:baseline}
.devblock h3{font:600 22px/1.2 "Cormorant Garamond",serif}
.viewbar{display:flex;justify-content:flex-end;margin:2px 0 10px}
.vtabs{display:flex;border:1px solid var(--line);border-radius:99px;overflow:hidden;background:#fff}
.vtab{border:none;background:none;font:600 12px "Plus Jakarta Sans";color:var(--muted);padding:6px 14px;cursor:pointer}
.vtab.active{background:var(--accent-light);color:#1a56ad}
.dmx .hmcells{grid-template-columns:repeat(var(--nd),1fr)}
.dmxh .hmcells{align-items:end}
.dhlab{font:500 10px/1.15 "Plus Jakarta Sans";color:var(--muted);writing-mode:vertical-rl;transform:rotate(180deg);justify-self:center;max-height:104px;overflow:hidden;white-space:nowrap}
.dhlab.zero{color:#c2c7cf}
.reading{font-size:14px;color:var(--ink);max-width:820px;margin:8px 0 16px}
.hm{max-width:640px}
.hmrow{display:grid;grid-template-columns:210px 1fr;gap:10px;align-items:center;margin:3px 0}
.hmlab{font-size:11.5px;color:var(--muted);text-align:right;line-height:1.25}
.hmcells{display:grid;grid-template-columns:repeat(8,1fr);gap:3px}
.hmc{display:block;height:15px;border-radius:3px;border:none;padding:0;cursor:pointer}
.hmc.empty{background:#f1f3f6}
.hmc:hover{outline:1.6px solid var(--ink);outline-offset:1px}
.hmc:focus-visible{outline:2px solid var(--ink);outline-offset:1px}
.hmyr{font-size:10.5px;color:var(--faint);text-align:center}
.hmhead{margin-bottom:5px}
.hmstage{font:600 10.5px/1 "Plus Jakarta Sans";letter-spacing:.13em;text-transform:uppercase;color:var(--faint);margin:12px 0 5px;display:grid;grid-template-columns:210px 1fr}
.hmstage::before{content:""}
.hmlegend{display:flex;gap:20px;flex-wrap:wrap;margin-top:14px;font-size:12.5px;color:var(--muted)}
.sw{display:inline-block;width:13px;height:13px;border-radius:3px;vertical-align:-2px;margin-right:6px}
.legend{display:flex;gap:26px;flex-wrap:wrap;align-items:center;padding:14px 18px;background:var(--card);border:1px solid var(--line);border-radius:10px;font-size:13px;color:var(--muted);margin-bottom:14px}
.mk{display:inline-block;width:15px;height:15px;border-radius:4px;vertical-align:-3px;margin-right:7px}
.mk.f{background:var(--blue)}
.mk.p{background:var(--blue-lt);border:1px solid var(--blue-bd)}
.mk.n{background:transparent;border:1.6px solid var(--faint)}
.stage{margin-top:34px}
.stage h3{font:600 20px/1.2 "Cormorant Garamond",serif;padding-bottom:8px;border-bottom:2px solid var(--ink)}
.stage .q{font-size:13px;color:var(--muted);margin:6px 0 4px}
.subhead{font:600 11px/1 "Plus Jakarta Sans";letter-spacing:.14em;text-transform:uppercase;color:var(--faint);margin:20px 0 4px}
.ghead,.grow{display:grid;grid-template-columns:64px 1fr 120px 120px 120px;gap:8px;align-items:center}
.ghead{font-size:11px;color:var(--faint);text-transform:uppercase;letter-spacing:.1em;padding:6px 0;position:sticky;top:0;background:var(--paper);z-index:2}
.ghead span:nth-child(n+3){text-align:center}
.grow{padding:5px 0;border-top:1px solid var(--line);font-size:13.5px}
.grow:hover{background:#f5f8fd}
.gid{color:var(--faint);font-size:12px;font-variant-numeric:tabular-nums}
.cell{display:flex;justify-content:center}
.cbtn{width:38px;height:17px;border-radius:5px;border:none;cursor:pointer;padding:0}
.cbtn.f{background:var(--blue)}
.cbtn.p{background:var(--blue-lt);border:1px solid var(--blue-bd)}
.cbtn.n{background:transparent;border:1.6px solid var(--faint)}
.cbtn:focus-visible{outline:2px solid var(--ink);outline-offset:2px}
#recToggle{display:block;margin:6px 0 0;border:1px solid var(--line);background:var(--card);color:var(--ink);font:600 13.5px "Plus Jakarta Sans";border-radius:10px;padding:12px 18px;cursor:pointer;width:100%;text-align:left}
#recToggle:hover{border-color:var(--accent);color:var(--accent)}
#recBody[hidden]{display:none}
.meta{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px}
.mcard{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px 20px;font-size:13.5px;color:var(--muted)}
.mcard h3{font:600 15px "Plus Jakarta Sans";color:var(--ink);margin-bottom:8px}
.mcard a{color:var(--accent);text-decoration:none}
.mcard a:hover{text-decoration:underline}
.mcard li{margin:4px 0 4px 16px}
#panel{position:fixed;top:0;right:-520px;width:min(500px,94vw);height:100vh;background:#fff;border-left:1px solid var(--line);box-shadow:-12px 0 40px rgba(23,23,23,.10);transition:right .22s ease;z-index:10;overflow-y:auto;padding:26px 28px}
#panel.open{right:0}
#panel .pk{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--faint)}
#panel h4{font:600 21px/1.25 "Cormorant Garamond",serif;margin:6px 0 4px}
#panel .pdef{font-size:13px;color:var(--muted);margin-bottom:14px}
#panel .pdev{display:flex;gap:10px;align-items:center;margin:14px 0 8px;font-weight:600}
.chip{font-size:11px;font-weight:600;letter-spacing:.04em;padding:3px 9px;border-radius:99px}
.chip.found{background:var(--blue);color:#fff}
.chip.partial{background:var(--blue-lt);color:#1d4f96;border:1px solid var(--blue-bd)}
.chip.not_found{border:1.4px solid var(--faint);color:var(--faint)}
blockquote{font-size:13.5px;color:var(--ink);border-left:3px solid var(--blue-lt);padding-left:12px;margin:10px 0}
blockquote cite{display:block;font-style:normal;font-size:11.5px;color:var(--faint);margin-top:6px}
#panel .why{font-size:13px;color:var(--muted)}
#panel .srch{margin-top:10px}
#panel .srch span{display:inline-block;font-size:11.5px;color:var(--muted);border:1px solid var(--line);border-radius:99px;padding:2px 9px;margin:2px 3px 2px 0}
#close{position:absolute;top:14px;right:16px;border:none;background:none;font-size:22px;color:var(--faint);cursor:pointer}
.ilist{margin-top:10px}
.irow{display:grid;grid-template-columns:48px 1fr auto;gap:8px;align-items:center;padding:7px 0;border-top:1px solid var(--line);font-size:13px;cursor:pointer}
.irow:hover{background:#f5f8fd}
.irow .yr{font-size:11.5px;color:var(--faint);font-variant-numeric:tabular-nums}
#veil{position:fixed;inset:0;background:rgba(23,23,23,.16);opacity:0;pointer-events:none;transition:opacity .2s;z-index:9}
#veil.open{opacity:1;pointer-events:auto}
footer{margin-top:64px;font-size:12px;color:var(--faint);border-top:1px solid var(--line);padding-top:16px;max-width:760px}
</style></head><body><div class="wrap">
<div class="kicker">Digital Minds Engagement Index &middot; the public record &middot; as of July 2026</div>
<h1>How frontier AI developers engage with digital-minds questions</h1>
<p class="lede">Researchers increasingly ask whether advanced AI systems could be conscious, have
welfare, or warrant moral consideration. This page records how the three largest frontier AI
developers engage with those questions in their <strong>formal public documents</strong> &mdash;
system and model cards, safety frameworks, model specifications, and welfare statements.
Every claim on this page traces to a verbatim quoted passage, or to a documented search that
found none.</p>
<p class="caveat">This is a record of public engagement, not a score: it registers the
<em>presence</em> of documented engagement, never its adequacy or sincerity &mdash; and &ldquo;no public
evidence&rdquo; describes the public record, not what happens inside a company.</p>

<section>
<h2>What the record shows today</h2>
<p class="sub">The framework looks for 100 indicators of engagement in each developer&rsquo;s
documents &mdash; each one grounded in the research literature, grouped into three stages:</p>
<div class="stages">__STAGECOLS__</div>
</section>

<section>
<h2>__S2TITLE__</h2>
<p class="sub">Each developer&rsquo;s record, by topic area and year: a cell is filled when documents published
that year evidence indicators in that topic area. Deeper blue = more indicators with direct
evidence; light blue = partial evidence only. <strong>Click any cell</strong> to see the indicators behind it,
or switch the view between dates and documents.</p>
<div class="viewbar"><div class="vtabs" id="viewtabs"><button class="vtab active" data-v="topic">By date</button><button class="vtab" data-v="docs">By document</button></div></div>
__DEVBLOCKS__
<div class="hmlegend">
<span><span class="sw" style="background:rgba(47,127,230,.45)"></span>1 indicator, direct</span>
<span><span class="sw" style="background:rgba(47,127,230,.7)"></span>2&ndash;3</span>
<span><span class="sw" style="background:#2f7fe6"></span>4+</span>
<span><span class="sw" style="background:#c7e0fb"></span>partial only</span>
<span><span class="sw" style="background:#f1f3f6"></span>no public evidence</span>
</div>
<p class="caveat" style="margin-top:12px">Cells date the <em>documents</em>: they show the years in which evidence
was published, read from a single 2026 coding. Change across future editions
will be tracked from the first quarterly update. Deterministic term-screening of the full corpus
corroborates the early empty years.</p>
</section>

<section>
<h2>The full record</h2>
<p class="sub">All 100 indicators, cell by cell &mdash; the reference layer beneath everything above.
Each cell opens to the quoted evidence, the coder&rsquo;s rationale, and &mdash; for absences &mdash; the searches
that were run. Cells link directly (e.g. <span style="font-variant-numeric:tabular-nums">#A7.1-anthropic</span>),
so any cell can be cited.</p>
<button id="recToggle" aria-expanded="false">Show the full record &mdash; 100 indicators &times; 3 developers &nbsp;&#9662;</button>
<div id="recBody" hidden>
<div class="legend" style="margin-top:14px">
<span><span class="mk f"></span><strong>Direct evidence</strong></span>
<span><span class="mk p"></span><strong>Partial</strong> &mdash; approaches the indicator; a named gap</span>
<span><span class="mk n"></span><strong>No public evidence</strong> &mdash; documented search found none</span>
</div>
<div id="grid"></div>
</div>
</section>

<section>
<h2>Data &amp; method</h2>
<div class="meta">
<div class="mcard"><h3>How this was made</h3>
<li>30 formal documents (2019&ndash;2026), registry-defined, captured July 2026</li>
<li>Independently coded twice, by coders from different model families</li>
<li>Status-level agreement 0.75; no found&harr;absent disagreements in 200 dual-coded cells</li>
<li>Every quote mechanically verified verbatim against its source</li>
<li>Every absence claim carries its documented search list</li></div>
<div class="mcard"><h3>Use this data</h3>
<li><a href="registry-v40.csv">Indicator registry (CSV)</a> &middot; <a href="registry-v40.json">JSON</a></li>
<li><a href="pilot-3dev-status.json">Per-cell status (JSON)</a></li>
<li><a href="pilot-arm-openai-verdicts.jsonl">OpenAI verdicts</a> &middot; <a href="pilot-arm-google-verdicts.jsonl">Google verdicts</a> &middot; <a href="pilot-pass2-verdicts.jsonl">Anthropic search verdicts</a></li>
<li>Methodology: DMEI Partner Draft 4 (on request)</li></div>
<div class="mcard"><h3>Citing &amp; updates</h3>
<li>Cite as: Digital Minds Engagement Index, pilot evidence, July 2026 &mdash; with the cell permalink for specific claims</li>
<li>Designed for quarterly updates; each edition version-stamped against the registry</li>
<li>Developers are offered a right of reply before publication</li></div>
</div>
</section>

<footer>Digital Minds Engagement Index &middot; registry v40 &middot; record as of July 2026.
Statuses describe the public record at capture date and unfold to their evidence.</footer>
</div>

<div id="veil"></div>
<aside id="panel" aria-label="Evidence detail"><button id="close" aria-label="Close">&times;</button><div id="pbody"></div></aside>

<script>
const D=__PAYLOAD__;
const STL={found:"f",partial:"p",not_found:"n"};
const LBL=Object.fromEntries(D.devs);
const grid=document.getElementById("grid");
let curStage="";
for(const g of D.groups){
  if(g.stage!==curStage){
    curStage=g.stage;
    const s=document.createElement("div");s.className="stage";
    const qs={Acknowledge:"Does the company say the question matters?",Assess:"Has it tried to measure or evaluate it?",Prepare:"Has it changed how it operates in response?"};
    s.innerHTML=`<h3>${g.stage}</h3><p class="q">${qs[g.stage]||""}</p>
      <div class="ghead"><span>ID</span><span>Indicator</span><span>Anthropic</span><span>OpenAI</span><span>Google</span></div><div class="rows"></div>`;
    grid.appendChild(s);
  }
  const rows=grid.lastChild.querySelector(".rows");
  const sh=document.createElement("div");sh.className="subhead";sh.textContent=g.sub;rows.appendChild(sh);
  for(const id of g.ids){
    const r=document.createElement("div");r.className="grow";
    r.innerHTML=`<span class="gid">${id}</span><span>${D.reg[id].name}</span>`;
    for(const[dev,label]of D.devs){
      const c=D.cells[dev][id];
      const cd=document.createElement("span");cd.className="cell";
      const b=document.createElement("button");
      b.className="cbtn "+STL[c.status];
      b.id=`${id}-${dev}`;
      b.title=`${label} · ${id}: ${c.status.replace("_"," ")}`;
      b.setAttribute("aria-label",b.title);
      b.addEventListener("click",()=>openPanel(dev,label,id,true));
      cd.appendChild(b);r.appendChild(cd);
    }
    rows.appendChild(r);
  }
}
const panel=document.getElementById("panel"),veil=document.getElementById("veil"),pbody=document.getElementById("pbody");
function esc(s){const d=document.createElement("div");d.textContent=s||"";return d.innerHTML}
function openPanel(dev,label,id,setHash){
  const c=D.cells[dev][id],reg=D.reg[id];
  let h=`<div class="pk">${reg.stage} · ${reg.sub}</div><h4>${id} — ${esc(reg.name)}</h4>
  <p class="pdef">${esc(reg.def)}</p>
  <div class="pdev">${label}<span class="chip ${c.status}">${c.status.replace("_"," ")}</span></div>`;
  for(const e of c.ev){h+=`<blockquote>&ldquo;${esc(e.q)}&rdquo;<cite>${esc(e.d)}</cite></blockquote><p class="why">${esc(e.g)}</p>`;}
  if(!c.ev.length)h+=`<p class="why">${esc(c.why)}</p>`;
  else if(c.why&&!c.ev.some(e=>e.g===c.why))h+=`<p class="why" style="margin-top:8px">${esc(c.why)}</p>`;
  if(c.searches&&c.searches.length){h+=`<div class="srch"><div class="pk" style="margin-bottom:6px">Searches run</div>${c.searches.map(s=>`<span>${esc(s)}</span>`).join("")}</div>`;}
  pbody.innerHTML=h;panel.classList.add("open");veil.classList.add("open");
  if(setHash)history.replaceState(null,"",`#${id}-${dev}`);
}
function openHeatPanel(dev,gi,Y){
  const g=D.groups[gi],label=LBL[dev];
  const yr=d=>{const m=(d||"").match(/20\d\d/);return m?+m[0]:null};
  const hits=[],misses=[];
  for(const id of g.ids){
    const e=D.inddocs[dev][id]||{d:[],p:[]};
    if(e.d.some(x=>yr(x)===Y))hits.push([id,"found"]);
    else if(e.p.some(x=>yr(x)===Y))hits.push([id,"partial"]);
    else misses.push(id);
  }
  let h=`<div class="pk">${label} · ${Y} · ${g.stage}</div><h4>${esc(g.sub)}</h4>
  <p class="pdef">Indicators in this topic area evidenced by ${label}&rsquo;s documents published in ${Y}. Click one for its evidence.</p><div class="ilist">`;
  for(const[id,st]of hits){h+=`<div class="irow" data-id="${id}" data-dev="${dev}"><span class="chip ${st}">${st}</span><span>${id} — ${esc(D.reg[id].name)}</span><span class="yr"></span></div>`;}
  h+=`</div>`;
  if(!hits.length)h+=`<p class="why">No indicators in this topic area are evidenced by documents from ${Y}.</p>`;
  if(misses.length)h+=`<p class="why" style="margin-top:10px">${misses.length} other indicator${misses.length>1?"s":""} in this topic area ${misses.length>1?"have":"has"} no evidence in documents from ${Y}.</p>`;
  pbody.innerHTML=h;panel.classList.add("open");veil.classList.add("open");
  pbody.querySelectorAll(".irow").forEach(r=>r.addEventListener("click",()=>openPanel(r.dataset.dev,LBL[r.dataset.dev],r.dataset.id,true)));
}
function openDocPanel(dev,gi,doc){
  const g=D.groups[gi],label=LBL[dev],meta=D.docmeta[dev][doc]||{lab:doc,t:doc};
  const hits=[],misses=[];
  for(const id of g.ids){
    const e=D.inddocs[dev][id]||{d:[],p:[]};
    if(e.d.includes(doc))hits.push([id,"found"]);
    else if(e.p.includes(doc))hits.push([id,"partial"]);
    else misses.push(id);
  }
  let h=`<div class="pk">${label} · ${esc(meta.lab)} · ${g.stage}</div><h4>${esc(g.sub)}</h4>
  <p class="pdef">${esc(meta.t)} — indicators in this topic area evidenced by this document. Click one for its evidence.</p><div class="ilist">`;
  for(const[id,st]of hits){h+=`<div class="irow" data-id="${id}" data-dev="${dev}"><span class="chip ${st}">${st}</span><span>${id} — ${esc(D.reg[id].name)}</span><span class="yr"></span></div>`;}
  h+=`</div>`;
  if(!hits.length)h+=`<p class="why">No indicators in this topic area are evidenced by this document.</p>`;
  if(misses.length)h+=`<p class="why" style="margin-top:10px">${misses.length} other indicator${misses.length>1?"s":""} in this topic area ${misses.length>1?"have":"has"} no evidence in this document.</p>`;
  pbody.innerHTML=h;panel.classList.add("open");veil.classList.add("open");
  pbody.querySelectorAll(".irow").forEach(r=>r.addEventListener("click",()=>openPanel(r.dataset.dev,LBL[r.dataset.dev],r.dataset.id,true)));
}
function closeAll(){panel.classList.remove("open");veil.classList.remove("open");history.replaceState(null,"",location.pathname)}
document.getElementById("close").addEventListener("click",closeAll);
veil.addEventListener("click",closeAll);
document.addEventListener("keydown",e=>{if(e.key==="Escape")closeAll()});
document.querySelectorAll(".devblock").forEach(b=>{
  const dev=b.dataset.dev;
  b.querySelectorAll(".hmc").forEach(c=>c.addEventListener("click",()=>{
    if(c.dataset.doc)openDocPanel(dev,+c.dataset.g,c.dataset.doc);
    else openHeatPanel(dev,+c.dataset.g,+c.dataset.y);
  }));
});
document.querySelectorAll("#viewtabs .vtab").forEach(t=>t.addEventListener("click",()=>{
  document.querySelectorAll("#viewtabs .vtab").forEach(x=>x.classList.toggle("active",x===t));
  document.querySelectorAll(".devblock").forEach(b=>{
    b.querySelector(".view-topic").hidden=t.dataset.v!=="topic";
    b.querySelector(".view-docs").hidden=t.dataset.v!=="docs";
  });
}));
const recToggle=document.getElementById("recToggle"),recBody=document.getElementById("recBody");
function expandRecord(){recBody.hidden=false;recToggle.setAttribute("aria-expanded","true");recToggle.innerHTML="Hide the full record &nbsp;&#9652;";}
function collapseRecord(){recBody.hidden=true;recToggle.setAttribute("aria-expanded","false");recToggle.innerHTML="Show the full record &mdash; 100 indicators &times; 3 developers &nbsp;&#9662;";}
recToggle.addEventListener("click",()=>recBody.hidden?expandRecord():collapseRecord());
(function(){
  const m=location.hash.match(/^#([ABC]\\d+\\.\\d+)-(anthropic|openai|google)$/);
  if(!m)return;
  const[,id,dev]=m;const lbl=LBL[dev];
  if(D.reg[id]&&lbl){expandRecord();openPanel(dev,lbl,id,false);
    const el=document.getElementById(`${id}-${dev}`);
    if(el)el.scrollIntoView({block:"center"});}
})();
</script></body></html>"""

page = page.replace("__STAGECOLS__", stage_cols)
page = page.replace("__S2TITLE__", S2_TITLE)
page = page.replace("__DEVBLOCKS__", dev_blocks)
page = page.replace("__PAYLOAD__", json.dumps(payload, ensure_ascii=False))
out = HERE / "dmei-dashboard.html"
out.write_text(page)
print(f"built {out.name}: {out.stat().st_size//1024} KB")
