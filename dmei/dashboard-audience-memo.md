# DMEI dashboard — audiences & productisation memo (2026-07-11)

Purpose: decide who the dashboard is for and how to present the pilot data so
its value is obvious within seconds ("make things people want"), drawing on how
Epoch AI, AI Lab Watch, SaferAI, and FMTI productise their data. Written for
Mitchel's review before any rebuild.

## 1. How the comparables productise (researched 2026-07-11)

**Epoch AI** — product unit = the **annotated insight**: a quantified trend
statement packaged with its chart ("Training compute grows 5×/year"), standalone
and shareable. Navigation segments audiences explicitly: Data explorers
(researchers) / Publications & newsletter (journalists, policy) / Benchmarks
(technical). Credibility via methodology transparency and "trusted by
governments." Retention via newsletter and recurring Data Insights — the data is
a living feed, not a report. **Crucially: no rankings.** Epoch proves
descriptive, quantified findings can carry a whole product.

**AI Lab Watch** — product unit = the **scorecard matrix**, above the fold,
logo columns, % scores, instant horizontal comparison. Two drill directions
(by company, by category). Honest "transparent subjectivity." Auxiliary
products: commitment tracker, incidents database.

**SaferAI** — credibility first (TIME/TechCrunch/Guardian logos), then the
ratings table with headline conclusions ("35% is currently the highest…").
Freshness stamp ("up to date as of July 2026"). Company drill-down pages.
One notable device: *"59% is the best score if a company adopted all industry
best practices"* — a **frontier statistic** showing headroom, not just standing.

**FMTI** — ranked bar chart + **change-over-time** charts ("companies score
worse this year") + stratified analyses; company reports; GitHub data repo +
paper for reproducibility. Headlines = change + outliers.

**Cross-cutting lessons**
1. **Insight-first, data-backed.** All four lead with a conclusion consumable
   in <10s; the table/grid is layer two. Our current dashboard is data-first.
2. **Two drill directions**: by developer AND by question.
3. **Freshness & change** are the news peg ("as of…", "since last edition").
4. **Credibility scaffolding** is explicit: methodology links, data repos,
   press/endorsements.
5. **Researchers get the files**: versioned downloads (FMTI GitHub, Epoch hub).
6. **Retention product**: newsletter / editions / trackers — matches draft 4's
   Stage-1 "light-touch quarterly publications."
7. Scores are their common currency — but Epoch's insight-unit and SaferAI's
   frontier statistic show how to be compelling **without grades**, which is
   what descriptive-first requires of us.

## 2. The five audiences — jobs to be done, and what we already have

| audience | their job | our matching asset | needed affordance |
|---|---|---|---|
| **Journalists** | find a defensible story fast; survive fact-checking | the Google zero-vocabulary result; the moral-patient probability; "flat denial is a Violation"; the lens contrast | copy-ready headline stats WITH the verbatim quote attached; per-claim permalinks; as-of stamp; downloadable chart w/ attribution |
| **Policy makers** | brief a principal; evidence for disclosure policy | NE-dominance (64–79% silence) — directly relevant to SB 53/RAISE-style documentation mandates; per-stage profiles | one-screen neutral summary; printable; "state of public engagement" framing |
| **Researchers** | reuse data, verify method, cite | registry + verdicts JSONL + findings CSV; reliability stats; protocol | downloads section (versioned files), methods note, how-to-cite |
| **Org decision makers** | know where they/peers stand; what engagement would look like | developer "shape" narratives; the registry as a menu of legible actions; the frontier indicators | per-developer profile panels; "the frontier" section (descriptive roadmap, no ranking) |
| **New entrants** | orient; grasp the debate and who's engaged | the lens strip; stage questions in plain language; quote-anchored examples | narrative on-ramp before the grid; progressive disclosure; guide cross-links |

If the DMEI becomes a digitalminds.guide sub-project, **new entrants become the
default visitor** — the narrative layers matter most, with the grid as the deep
layer for the other four groups. Tone: the guide's "observational and grounded,
not breathless."

## 3. Proposed v2 structure (for approval)

**Layer 1 — "What the record shows" (above the fold).** Four-to-five headline
finding cards: one-sentence descriptive insight + minimal visual + "see the
evidence →" anchor into the grid. Candidates (all counts/quotes/absences — no
grades):
- *Breadth gradient*: "One developer's formal documents engage 91 of 100
  indicators; another's engage 21."
- *The zero*: "Google's formal documents contain no consciousness, sentience,
  or model-welfare vocabulary at all."
- *The lens*: "The same model behaviour is welfare evidence in one company's
  documents, a scheming risk in another's."
- *The silence*: "For two of three developers, most of the framework — 64–79%
  of indicators — has no public evidence."
- *The frontier*: "Nine indicators are evidenced by no developer — the open
  edge of public engagement." (SaferAI's headroom device, descriptivised.)

**Layer 2 — Compare & explore.** Coverage profiles (existing) + per-developer
profile panels (the pilot's "shape" narratives + their strongest evidence) +
the lens strip. Two drill directions: by developer, by stage/sub-domain.

**Layer 3 — The evidence grid.** As built (100×3, click-through to quotes and
search trails). Add per-cell permalinks (#A2.4-google) so every cell is citable.

**Layer 4 — Use this data.** Downloads (registry, verdicts, findings CSV),
methods note (dual-coded, quote-verified, corpus as-of dates, reliability
figures), how-to-cite, update cadence ("updated quarterly" per draft 4 Stage 1),
contact/right-of-reply note.

**Cross-cutting:** as-of stamp in the header; "copy citation" on finding cards;
attribution baked into any exported visual.

**Explicitly not adopted from comparables:** overall scores, rankings, ranked
bar charts, letter grades, red/green semantics — Phase-2-gated per the
descriptive-first principle. The substitute currency is the *quantified
descriptive finding* (Epoch's unit) + the *auditable cell* (ours alone).

## 4. RESOLUTION (Mitchel, 2026-07-11): context-level, not profession, is the design axis

New entrants = the assumed core user — but "new entrant" includes **low-context
journalists and policy aides**, not just curious readers. Lead with clear,
non-sensationalised headline insights backed by data. Design consequences:

1. **Headlines must be world-facing, not instrument-facing.** My §3 candidates
   assumed the reader knows what an "indicator" is. Test for every card: does it
   parse for someone who has never heard of model welfare? Structure per card:
   plain-language sentence → precise formulation (instrument vocabulary) →
   verbatim evidence, each one click deeper.
2. **Inoculation against sensationalism is a design job.** The topic trends
   sensational ("AI company thinks its chatbot is alive"); our job is to make
   the sober sentence the most copyable one on the page — scope qualifiers
   ("in formal public documents") inside the sentence, not footnoted; the
   verbatim source line attached to every claim.
3. **Progressive disclosure IS the architecture**: plain finding → precise
   claim → quote → grid cell → data file. Low-context users stop early;
   researchers fall through.
4. Resolves Q3 (no audience routing — low-context users don't self-identify
   into lanes) and Q4 ("the frontier" → plain + neutral phrasing: "questions no
   company has answered publicly" — plainer AND less normative; convergence).
5. Q1/Q2: headline cut favours plainest-language findings; developer profiles
   stay on-page (single-file constraint) as compact panels.

## 5. Open questions for Mitchel (superseded — kept for record)
1. Which headline findings make the Layer-1 cut (suggest 4 of the 5)?
2. Per-developer profile panels: modal/section on this page, or future
   sub-pages (guide-route-shaped)?
3. Explicit audience routing ("for journalists / researchers / policy…") vs
   letting the layers do the work (my lean: the latter; routing labels can
   read as marketing).
4. Does "the frontier" framing stay comfortably descriptive for you, or does
   naming it risk normative reading? (It is a count of empty cells; but the
   word "frontier" edges toward aspiration.)
