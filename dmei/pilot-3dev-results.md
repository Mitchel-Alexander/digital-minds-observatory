# DMEI pilot — three-developer coverage results (2026-07-11)

All 100 indicators coded against each developer's formal-document corpus.
Anthropic = pass-1 evidence mapping + pass-2 targeted search; OpenAI & Google =
full targeted-search arms (6 agent groups each, same protocol: exact quotes
mechanically verified — 0 failures across 200 arm verdicts — and documented
searches behind every absence). Per-indicator verdicts:
`pilot-arm-google-verdicts.jsonl`, `pilot-arm-openai-verdicts.jsonl`,
`pilot-pass2-verdicts.jsonl`; consolidated status: `pilot-3dev-status.json`.

## The matrix (found / partial / not_found)

| stage | Anthropic | OpenAI | Google |
|---|---|---|---|
| Acknowledge (45) | 37f · 3p · 5n | 7f · 13p · 25n | 0f · 10p · 35n |
| Assess (27) | 22f · 3p · 2n | 1f · 9p · 17n | 0f · 7p · 20n |
| Prepare (28) | 20f · 6p · 2n | 2f · 4p · 22n | 0f · 4p · 24n |
| **TOTAL** | **79f · 12p · 9n** | **10f · 26p · 64n** | **0f · 21p · 79n** |

## Developer profiles

**Anthropic** — engagement across all three stages; absences are the
discriminating frontier (multi-theory assessment, welfare escalation ladder,
civic engagement, deliberative credence-setting) plus researcher-shaped
constructs (A7.3, A5.4, A7.7).

**OpenAI** — every found sits in the perception/communication/design cluster:
A1.1/A1.2 (deliberate framing choices — the GPT-4 "agentic" footnote, the
"hallucinations"-anthropomorphization caveat), A2.1/A7.2 (Model Spec: AI
consciousness "a matter of research and debate"), A9.1 (calibrated
communication — a flat "No, I am not conscious" is marked a *Violation*),
A11.1/A11.2 + B10.1 (GPT-4o anthropomorphization / emotional-reliance
assessment), C5.3 (the model-spec self-representation clause), C5.5
(interaction-harm mitigation). Zero founds in moral status, welfare capacity,
organisational welfare concern, or welfare governance. Exactly the
perception-lens profile the term-fingerprints predicted.

**Google/GDM** — zero founds; the corpus contains no consciousness, sentience,
or model-welfare vocabulary at all. The 21 partials are all one shape: the raw
phenomena appear (Gemini 3 Pro "expresses frustration" in chain-of-thought;
self-proliferation and shutdown-adjacent evals; eval-awareness confound
analysis; CoT-faithfulness assessment; the Gopher model-vs-persona
distinction) **but always under a pure safety/misalignment lens** — never a
welfare frame.

## The headline finding: the lens, not the phenomena

The three corpora contain substantially overlapping raw phenomena
(emotion-like CoT expressions, self-preservation-adjacent behaviour,
self-report-reliability worries, eval-awareness). What differs is the frame
each developer's documents put on them: welfare-relevant evidence (Anthropic),
scheming/misalignment risk (OpenAI: B9.1 — the o1 shutdown-avoidance evals
never ask whether the behaviour constitutes a preference), or capability
hazard (Google: B2.2, A8.3). The DMEI measures exactly this framing layer —
which is the right object for an engagement index, and worth stating in
draft 4's framing section.

## Methodological payoffs for draft 4

1. **The `partial` status carried the signal.** For OpenAI/Google, 21–26% of
   cells are partials that binary 1/0/NE would have flattened into
   indistinguishable zeros — losing precisely the "approaches the construct
   through a different lens" content that makes the comparison informative.
   Draft 4 should adopt partial (or the committed/demonstrated facet family)
   as a first-class code.
2. **Absence dominates the field** (64–79% for the other two developers).
   The NE-denominator decision is not an edge case — it is most of the data.
   Draft (2)'s full-denominator arithmetic is the only honest option.
3. **Indicator discrimination confirmed.** The instrument produces a clean,
   quote-anchored gradient (79f → 10f → 0f) with per-cell audit trails —
   the DMEI's core design works on real documents.
4. **Per-indicator search protocols transfer.** The same 6-group protocol ran
   unchanged across three corpora; NE claims carry documented search lists
   throughout. This is the coding protocol draft 4 §"How indicators are coded"
   should specify.

## Pilot remaining
- Independent GPT coder run (bundle ready: `dmei-pilot-bundle.zip`) →
  agreement statistics (Krippendorff's α / Gwet's AC1).
- Analysis backlog: co-firing consolidation memo; Notes-layer drafting from
  the 12+26+21 partials; zero-candidate → new-indicator proposals
  (Constitution relational layer; self-interaction research).
