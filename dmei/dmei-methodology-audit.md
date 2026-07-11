# DMEI Methodology Audit — 2026-07-11

Audit of *Digital Minds Engagement Index — Indicator Framework, Partner Draft (2)*
(Structure v40, June 2026; 100 indicators, Acknowledge 45 / Assess 27 / Prepare 28).
Conducted for the Observatory's developer-positions track ahead of any adoption.
Auditor context: the 2026-06-22 review (pre-dating the developer-positions work),
the comparables research (FMTI, AI Lab Watch, SaferAI, Midas, content-analysis ICR
practice), and operational experience from building the 479-finding quote-verified
Anthropic evidence layer over a 60-doc / 7-developer registry corpus.

## Verdict

Methodologically serious and unusually honest about its own limitations (§6's
"'descriptive' is a posture maintained against the grain of the instrument" is a
concession most indices never make). The architecture is right: literature grounding
as the inclusion gate gives it the external-derivation property our codebook v1
lacked; the concept×stage matrix is the two-axis structure we independently arrived
at; NE≠0 is ahead of FMTI; the no-composite Stage 1 + conditional Stage 2 matches
the Observatory's descriptive-first ruling exactly.

The weaknesses concentrate in **operationalization** — the layer between framework
and reproducible data. That is precisely the layer our project has already built
tooling for, so most fixes are direct transplants.

## Strengths (keep as-is)

1. **Literature grounding as a hard inclusion gate** — external yardstick, not
   developer-derived; the anti-mirror property.
2. **NE distinct from 0** — silence never coded as considered rejection.
3. **Coverage profile, not a grade; composite deferred and conditional** on
   institutional housing, with honest CDP/GRI layering precedent.
4. **§6 Limitations** — concedes indicator-set-as-choice, implicit weighting via
   indicator granularity, Acknowledge tilt, symbolic-layer measurement.
5. **Right of reply** (RDR/SaferAI practice) and sourced, contestable codings.
6. **Concept sub-domains × Acknowledge→Assess→Prepare** structure, externally
   anchored (Long/Sebo/Butlin; FMTI/OECD parallels).

## Findings (severity-ordered), each with a directly-implementable fix

### F1 — The corpus is not operationally defined (highest severity)
§1 scopes "formal documentation" (RSPs, system/model cards, specs, welfare
statements), yet the worked example codes from two *blog posts* (Exploring Model
Welfare; the deprecation-commitments update). Without a bounded, versioned corpus:
NE is ill-defined (absence *from what?*), codings are irreproducible (two coders
search different corpora), and longitudinal comparison breaks as the corpus
silently grows or documents are edited (the Midas lesson: developers change
documents quietly).
**Fix (transplant):** a registry-defined corpus per developer — explicit document
list with doc-type, capture date, content hash, archived snapshot (our
`documents.csv` + the planned provenance layer). Report codings per document class
(cards / frameworks / specs / canonical-policy blogs) so the blog boundary becomes
a stratum decision rather than an inconsistency.

### F2 — No mechanical evidence verification
The protocol requires "the exact quoted passage," but nothing checks quotes are
verbatim. Extraction experience: paraphrase drift occurs even with careful,
quote-instructed extraction; our validator's normalized-substring gate is what made
the 479-finding dataset credible. At 100 indicators × 12 developers × 2 coders,
unverified quotes will drift.
**Fix (transplant):** `validate_findings.py`-style hard gate — a coding only counts
if its quote verifies as a substring of the registry document.

### F3 — Search/recall protocol unspecified; NE inherits coder recall
"A coder searches the developer's in-scope public corpus" has no recall guarantee.
Empirical result from our pipeline: two independent passes over the *same* document
returned 106 vs 82 findings with only partial overlap. An NE produced by one
coder's search is weak evidence of absence — and NE is the framework's most
important cell (it is how the index discriminates silence).
**Fix (transplant):** (a) deterministic term-library pre-screening (our
`library.py`) to surface candidate passages per indicator before human judgment;
(b) two independent passes with span-overlap union (our protocol); (c) report
per-indicator retrieval support so NE claims are auditable.

### F4 — The promised "Notes" codebook layer is absent
§3 claims "accompanying notes act as a compact embedded codebook" handling edge
cases — but sampled Appendix A entries carry only Definition + Grounding, no
pass/fail conditions. Abstract indicators (A1.1 categorical framing, A7.3
justification drift, A2.4 validity-of-method) will not reach usable agreement
without them. ICR practice: iterate the codebook to α≥0.8 on a pilot *before*
deployment, not report agreement after round 1 (the draft currently promises the
latter).
**Fix:** write the Notes layer; pilot on a gold set first (see Pilot, below).

### F5 — Binary coding hides a distinction the draft itself makes
"A stated commitment is treated as a weaker pass than a demonstrated practice" —
but coding is 1/0/NE, so "weaker pass" has no cell. This is an undefined state
smuggled into a binary scheme. Our data shows the distinction is frequent and real
(forward_commitment vs implemented_measure families; AI Lab Watch's
announced≠demonstrated).
**Fix:** record a facet on every 1: `committed` vs `demonstrated` (a factual
property of the passage, not an ordering). Aligns with the planned commitment
register.

### F6 — Indicator co-firing double-counts single passages
One paragraph (e.g. the Opus 4 welfare-section introduction) plausibly satisfies
A2.1, A4.1, A5.2, A7.1 and A7.2 simultaneously. Coverage counts then weight one
passage five times; §6 concedes the granularity-as-implicit-weighting problem
abstractly, but it is measurable and partly fixable.
**Fix:** run a co-firing analysis (empirically possible now with the findings
dataset); merge or hierarchize indicators with high co-occurrence; report
distinct-evidence-passage counts alongside indicator counts.

### F7 — The 0 cell will be nearly empty in practice
"Assessed but not satisfied" requires evidence of considered rejection — but
formal documents almost never record reasoned negatives (our corpus: Google and
Mistral are pure silence; the reasoned-negative case, Suleyman, lives in an essay,
i.e. the discourse layer, outside scope). Without an operational rule for 0,
the trichotomy collapses to presence/absence.
**Fix:** define 0 as *explicit negative statement, quoted*; expect and report its
rarity honestly; decide deliberately whether reasoned-negatives warrant a bounded
discourse-exception analogous to the canonical-policy-blog rule.

### F8 — Compound (conjunctive) indicators
C6.2 bundles three conditions (conditional development + pause + non-deploy);
A7.3 bundles distinguish + guard. Conjunctions depress agreement and make partial
satisfaction invisible.
**Fix:** decompose, or state the conjunction rule (all-required vs any) per
indicator in the Notes layer.

### F9 — Grounding anchors are young and partly unpublished
Multiple indicators ground exclusively in working papers and forthcoming volumes
(Eleos working papers; Keeling & Street 2026; Butlin & Lappas forthcoming).
The gate is right, but grounding ≠ settled literature, and the anchor set reflects
a small research community (§6 concedes the research-programme import).
**Fix:** tier groundings (peer-reviewed / working paper / forthcoming) and flag
indicators whose only anchors are non-peer-reviewed — the "evidence-tier
transparency" point from the June review, now concrete. Optional descriptive stat:
use the 1,281-work corpus to quantify literature breadth behind each sub-domain.

### F10 — Coder pool and independence unspecified
Dual independent coding is promised; the project is currently single-author.
If coding is LLM-assisted (viable — our workflow is a working model), that must be
disclosed and validated (two independent passes + verification gate + human
adjudication), with agreement reported per stage as planned.

### F11 — No version control for the instrument itself
"Structure v40" implies heavy iteration, but there is no changelog or versioned
release; when indicators change, prior codings silently lose comparability (the
Midas lesson applied to the index rather than the developers). Also: C-series
numbering still skips C4 (flagged 06-22, unfixed).
**Fix:** versioned releases with a changelog; codings stamped with the instrument
version (mirrors our CODEBOOK.md versioning rule).

## ADDENDUM 2026-07-11 (later): GPT 5.6 audit of draft (3) — cross-check

Mitchel commissioned an independent GPT 5.6 audit, run against **Partner Draft (3)**
(new: downloaded 2026-07-11, 42KB vs (2)'s 63KB). Verified against (3) directly:

**Draft (3) is a substantial slimming that DROPPED guardrails (2) had** — my audit
praised several things that no longer exist. Verified 2026-07-11 (full 100-entry
field diff, correcting an earlier sampled claim): registries are identical EXCEPT
C1.8/C1.9 groundings — draft (3) re-grounds both as "Grounding (provisional)"
governance reference points (SaferAI dims / FMTI subdomain), its one genuine
improvement (honest hard-gate exception; GPT flagged these correctly). C4 gap /
"v40" / uncited-OECD nits unfixed in both. Otherwise (3) changes only the
methodology layer, entirely by subtraction plus two regressions. Removed: "Public positions held
distinct from the models" framing; **"Sourced and contestable" (right of reply)**;
**"A coverage profile, not a grade"**; **"How indicators are coded" (dual coding +
Krippendorff)**; the worked example; §4 comparators; **§5 staged Stage-1/Stage-2
roadmap (composite deferral)**; **§6 Limitations**. Changed: "Binary coding" →
"Binary **scoring**"; NE now **"excluded from the denominator"** (in (2) coverage
was counted against the full indicator set); "ordinal indicators under
consideration for the scoring-design phase". Net: (3) drifts toward a scoring
instrument while shedding the descriptive-first protections.

**GPT audit quality: high, largely convergent.** Convergent with F1 (corpus/unit —
GPT adds subsidiaries/employee-papers/authoritative-position rules + a nested
developer+release design), F4 (codebook — richer checklist), F5 (commitment vs
implemented), F6 (redundancy — with a concrete, testable consolidation-cluster
list), F8 (compound — longer list), F10 (dual coding — adds Gwet's AC1, apt for
prevalence-skewed data), F11 (versioning/"measurement invariance"), pilot-first.

**GPT's genuine additions I missed:**
- **NE-denominator arithmetic rewards opacity** (its top finding — real in (3);
  a between-draft regression rather than a (2) flaw, but the deeper point stands:
  for an engagement index, absence-after-completed-search IS the observation).
- **Doctrinally-loaded indicators** (A2.5 internal-process primacy, A2.7 alien-
  consciousness "would likely", A6.1 persistence-as-illusion, A6.2, A7.7 pharma
  analogy): require endorsing contested positions rather than engaging the
  question. Reword around disclosure of alternatives/evidence/uncertainty.
- **Construct multiplicity** named as such (disclosure breadth / philosophical
  sophistication / assessment quality / institutional preparedness).
- **Human-interaction module boundary** (A11.2/B10.1/C5.5 = user-welfare, a
  different construct) — independently validates our two-axis lexicon finding
  (perception lens ≠ welfare lens).
- **Missing categories**: incident response/remediation, staff/budget resources,
  eval reproducibility, **scale-sensitivity (copies/runtime)**, downstream/API/
  open-weight responsibilities, preservation-vs-privacy conflicts, model
  inventory, appeals/remedy.
- **Indicator-admission matrix**: literature grounding necessary but insufficient
  (relevance, distinctness, observability, reliability, gaming-resistance…).
- Experimental-practices module (euphorics C2.7, cooperative arrangements C3.2)
  separated from core.

**Where GPT's audit is weaker / needs care:**
- Prescriptions without mechanisms — no quote-verification requirement anywhere;
  "search status: complete/incomplete" is unknowable without a bounded registry
  corpus + deterministic pre-screen (our F1/F3 tooling is the how); "double-code
  20–30%" is weaker than two-pass-everything.
- Its proposed **stance field** (affirmative/negative/uncertain/mixed) and
  **ordered substantive scale** (absent<mentioned<reasoned<operationally-evidenced)
  are interpretation and ordering — in tension with the descriptive-first ruling.
  Flat passage-type facets (≈ our type system) capture the same information
  without the maturity ordering; stance stays deferred (or, if DMEI adopts it,
  quote-anchored + flat + explicitly labelled interpretive).
- Several recommendations (weighting-sensitivity schemes, normalization) target
  the Stage-2 composite that (2) had deferred — though (3)'s drift toward scoring
  language makes GPT's aim fair for the document as written.

**Merged priority (supersedes the single-audit list):** (0) decide whether (3)'s
guardrail removals were intentional — restore right-of-reply, profile-not-grade,
composite-deferral, coding protocol, limitations, or house them in a methods annex;
(1) fix NE denominator; (2) registry-defined corpus + provenance; (3) quote gate;
(4) Notes/codebook layer w/ GPT's checklist; (5) de-doctrinalize the flagged
indicators; (6) consolidation guided by an EMPIRICAL co-firing pilot rather than
armchair clusters; (7) module boundaries (human-interaction; experimental);
(8) admission matrix; (9) versioning/changelog. The 3-developer pilot adjudicates
(5)/(6) and measures 0-rarity, decidability, and pass rates before any re-slimming.

## Recommended next step: an empirical pilot (propose-before-build)

Everything above except F9/F11 is testable *now* with assets in hand: dry-run the
100 indicators against the registry corpus for three developers — Anthropic (rich
case), Google DeepMind (the draft's own NE case), OpenAI (perception-lens case) —
using the 479-finding dataset as candidate evidence passages. Measures: per-
indicator decidability, co-firing matrix, 0-cell rarity, formal-doc coverage
(which indicators require blogs), and two-pass agreement. Output: evidence to fix
F4–F8 and a tested coding protocol, before any DMEI adoption into the track.
Phase-1-admissible throughout (descriptive; no scores, no orderings).
