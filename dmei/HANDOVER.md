# DMEI — handover notes (written 2026-07-12, end of build session)

For the next Claude instance (or human) picking this up. Read alongside
`README.md` (project home) and the memory file
`digitalminds-engagement-index.md` (full chronology).

## What this is

The **Digital Minds Engagement Index**: a 100-indicator framework measuring how
frontier AI developers publicly engage with digital-minds questions in their
formal documents. This folder contains the framework (Partner Draft 4), the
machine-readable indicator registry, a completed three-developer methodology
pilot with dual-coder reliability, and a partner-facing evidence dashboard.
It sits in the Observatory repo on the **`dmei` branch — deliberately not on
`main`** (main deploys to the public GitHub Pages site; this is unpublished).

## Current state (all complete as of 2026-07-12)

- **Framework**: `DMEI-partner-draft-4.md` — Draft 4, built on Draft 2's
  methodology (Draft 3's cuts reversed), every section provenance-tagged
  [D2]/[D2·rev]/[new]. §5 lists indicator revisions PROPOSED but NOT yet
  applied to the registry (registry stays v40 until Mitchel resolves them → v41).
- **Registry**: `registry-v40.csv/.json` — 100 indicators verbatim from Draft 2
  (+ Draft 3's provisional-grounding variants for C1.8/C1.9 preserved).
- **Pilot** (read `pilot-3dev-results.md` + `pilot-agreement-results.md` first):
  coverage Anthropic 79f/12p/9n · OpenAI 10f/26p/64n · Google 0f/21p/79n;
  dual-coded (Claude + GPT 5.6 blind), Protocol B reliable (AC1 .70/.67, zero
  polar disagreements), Protocol A = retrieval only, never comparative.
  All ~440 quotes mechanically verified verbatim; every absence carries its
  search log. Headline finding: the three corpora share raw phenomena; what
  differs is the LENS (welfare / scheming-risk / capability-hazard).
- **Dashboard**: `dmei-dashboard.html` (single self-contained file, v4.8) —
  rebuild with `python3 build_dmei_dashboard.py`. Structure: header →
  stage cards (stacked, shared-scale bars, self-labelling counts) →
  three developer blocks with a GLOBAL "By date | By document" toggle
  (per-year activity heatmap ⟷ doc×topic matrix; rows identical across views;
  cells click through to quoted evidence; absences show search-trail chips) →
  collapsed full record (permalinks like `#A7.1-anthropic` auto-expand) →
  data & method. Styled to digitalminds.guide tokens (may become a guide
  sub-project). Serve locally: launch config `dmei` (port 5188) in the parent
  workspace `.claude/launch.json`.

## Data lineage (what feeds what)

`build_dmei_dashboard.py` reads, from THIS folder: registry-v40.json,
pilot-3dev-status.json, pilot-arm-{google,openai}-verdicts.jsonl,
pilot-pass2-verdicts.jsonl, pilot-anthropic-mapping-pass1.json — and from
`../dm-developer-positions/` (the Observatory's developer-positions track, NOT
in this repo): `anthropic-welfare-findings.csv` (479 quote-verified findings)
and `documents.csv` (the 60-doc corpus registry). **Snapshot copies of those
two files are in `source-data/`** so this branch is self-contained; if
rebuilding outside the original machine, point the script there.
The fulltext corpus and `validate_findings.py` (the verbatim-quote gate) live
in `dm-developer-positions/` on Mitchel's machine — not committed here
(full document texts; copyright).

## Open threads, in rough priority

1. **Mitchel's copy pass** on the three READINGS sentences (top of
   build_dmei_dashboard.py) and Draft 4's editorial text — all still my
   stand-in copy.
2. **Draft 4 §5 resolutions** → registry v41 (de-doctrinalise 5 indicators,
   split multi-barrels, evidence-based merges only, two visible modules,
   candidate additions incl. developer↔model relational commitments +
   model–model interaction research). Then the Notes layer, written FROM the
   pilot's ~100 partials.
3. **The lens blog post** — first Epoch-style insight post (one finding,
   ~600 words, full quotes: same shutdown-avoidance behaviour, three framings).
   Explicitly cut from the dashboard to be done justice separately.
4. **Guide-route port** — if DMEI becomes a digitalminds.guide sub-project,
   the dashboard is already in guide tokens; the view toggle is an ordinary
   React pattern.
5. **Quarterly update protocol** — re-run the coding on new documents; codings
   are version-stamped against the registry. The GPT coder's memos
   (`~/Downloads/dmei-pilot-handoff.zip`) hold unmined methodology feedback.
6. **Right of reply** before any real publication — committed in the
   methodology; NOT yet done (this branch being non-deployed is what keeps
   the current state "unpublished").

## Hard-won gotchas

- **Descriptive-first principle is standing law** (memory:
  observatory-descriptive-first-principle): no scores, rankings, orderings,
  or red/green semantics anywhere; absence is a neutral zero; "partial" is a
  named gap, never a grade. The presence ramp is sequential blue by design.
- **Every quote must survive the verbatim gate** (normalised substring of the
  source document). Extraction/coding without mechanical verification drifts.
- **Single-pass anything under-recalls** (~28% of first-pass absences were
  false): two passes + targeted search before any absence claim.
- **Preview tab quirks**: preview_screenshot can RELOAD the page and reset
  JS state — set state via URL hash or screenshot immediately after the eval;
  subagents die instantly at subscription session limits (main loop survives —
  finish inline or wait for reset).
- The Observatory repo's `main` carries undeployed site checkpoints —
  **pushing main deploys the live site**. Keep DMEI work on this branch until
  a deliberate publish decision.
