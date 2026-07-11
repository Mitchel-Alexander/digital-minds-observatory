# DMEI — project home

Working files for the **Digital Minds Engagement Index** (previously living only
as loose docx in `~/Downloads`). Decision 2026-07-11: **build draft (4) on
draft (2)'s methodology**, achieving draft (3)'s brevity by relocating the
indicator registry to a companion artifact (this folder) — not by cutting the
methodology.

## Files

- `registry-v40.csv` / `registry-v40.json` — the 100-indicator registry
  extracted **verbatim from Partner Draft (2)** (Structure v40, June 2026).
  Validated: 100 entries; Acknowledge 45 / Assess 27 / Prepare 28; 26
  stage×sub-domain groups; every entry has definition + grounding.
  Fields: id, stage, subdomain, name, definition, grounding, provisional,
  grounding_draft3_provisional.

## Draft (2) vs draft (3) — settled facts (2026-07-11)

- Registries are **identical except C1.8 and C1.9 groundings**: draft (3)
  re-grounds both as "Grounding (provisional)" governance reference points
  (SaferAI dims, FMTI subdomain) with "related lit for later anchoring" —
  (3)'s one genuine improvement (honest about the hard-gate exception); both
  variants preserved in the registry files. **Recommended for draft (4): adopt
  (3)'s provisional grounding for these two** (or find DM-literature anchors).
- Everything else (3) changed was subtraction from the methodology layer:
  right-of-reply, "coverage profile not a grade", Stage-1/2 composite-deferral
  roadmap, dual-coding/Krippendorff protocol, worked example, comparator
  section, Limitations section, References/bibliography — plus two regressions
  in surviving text ("coding"→"scoring"; NE excluded from the denominator).

## Draft (4) revision agenda

See `../dmei-methodology-audit.md` — my full audit (F1–F11) + the GPT 5.6
cross-audit addendum + the merged priority list. Headlines: restore (2)'s
guardrails; NE back in the denominator; registry-defined corpus + provenance;
verbatim quote-verification gate; write the Notes/codebook layer; de-doctrinalize
A2.5/A2.7/A6.1/A6.2/A7.7; consolidation via empirical co-firing (pilot), not
armchair merges; human-interaction + experimental-practices module boundaries;
indicator-admission matrix; instrument versioning/changelog.

Related: the Observatory developer-positions track
(`../dm-developer-positions/`) supplies the operational layer (document
registry, fulltext corpus, quote-verified findings dataset, validation tooling)
— the DMEI's Stage-1 evidence base. Proposed next step: a 3-developer pilot
(Anthropic / Google DeepMind / OpenAI) dry-running all 100 indicators.
