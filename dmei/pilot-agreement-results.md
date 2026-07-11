# DMEI pilot — inter-coder agreement results (Claude vs GPT 5.6, 2026-07-11)

Independent blind run by GPT 5.6 from `dmei-pilot-bundle.zip` (its outputs +
memos: `~/Downloads/dmei-pilot-handoff.zip`, extracted copy analysed here).
Validation of GPT's run: 479/479 mapping coverage, 0 invalid IDs, and **0 quote
verification failures across all three search arms** — the verbatim-quote
protocol transferred perfectly to a different model family.

## Protocol B (targeted search): RELIABLE

| arm | raw agreement | Cohen κ | Gwet AC1 | hard disagreements (found↔not_found) |
|---|---|---|---|---|
| Google | 0.75 | 0.28 | **0.70** | **none** |
| OpenAI | 0.75 | 0.49 | **0.67** | **none** |

- κ is depressed by the prevalence paradox (65–79% not_found marginals) — AC1
  is the appropriate statistic here, exactly as GPT's own audit anticipated.
- **Zero polar disagreements in 200 cells.** Every disagreement is at the
  partial boundary (ours-partial↔GPT-not_found 11–14 cells per arm and
  vice versa) — i.e., precisely the boundary the missing Notes layer is
  supposed to govern. The disagreement pattern *is* the codebook to-do list.
- Found-level consensus: GPT's 7 OpenAI founds (A1.2, A7.2, A9.1, A11.2,
  B10.1, C5.3, C5.5) are a strict subset of our 10; our extras (A1.1, A2.1,
  A11.1) went GPT-partial, not GPT-absent. Google: both coders 0 found.
- Both coders independently reproduced the headline: Google 0f/~2xp/~78n,
  OpenAI's engagement concentrated in the Model Spec consciousness clause +
  GPT-4o anthropomorphization work, "safety analogue without welfare link" as
  the dominant partial shape.

## Protocol A (findings→indicator mapping): UNDER-CONSTRAINED

479×100 binary cells: raw 0.978 / AC1 0.977 (inflated by sparsity);
**Krippendorff α 0.23, positive agreement 0.24, mean per-finding jaccard
0.125, best-match 65/257** — poor, and diagnostically so:

- The disagreement is *structural, not random*: our coder mapped whole finding
  families to broad indicators (C2.5: ours 114 vs GPT 10; B2.2: 69 vs 12;
  B6.1: 48 vs 4; C1.6: 40 vs 3), while GPT mapped more conservatively per
  finding but more liberally to Acknowledge constructs (A7.1: GPT 36 vs ours
  16; A7.2: 32 vs 18). Different implicit candidacy thresholds + different
  granularity readings of broad indicators = audit finding F4 (no Notes
  layer) manifesting exactly as predicted.
- Real definitional ambiguities surfaced: e.g. B1.5 ("use of mechanistic
  interpretability" *in consciousness assessment*) — we mapped Anthropic's
  emotion-probe work to it 22×; GPT read the definition as
  consciousness-assessment-specific and mapped none. Both readings are
  defensible; the definition must choose.
- GPT's own §3.9 caution is right and becomes protocol: **Protocol A is a
  retrieval experiment feeding candidate evidence to Protocol B — not a
  company-comparison dataset.** Comparative claims rest on Protocol B only,
  where reliability is demonstrated.

## GPT's protocol recommendations (adopt list)

Convergent with our audits and now empirically motivated; the genuinely new
ones (→ draft-4 / next reliability round):
1. **Component checklists per indicator** + structured partial-reason codes
   (e.g. `SAFETY_ANALOGUE_NO_WELFARE_LINK` — names our "lens" finding).
2. **`evidence_voice` hierarchy** (developer position → policy → practice →
   model output → quoted third party → metadata); model output caps at
   partial for position indicators. Formalizes the transcript≠position rule.
3. **`welfare_subject` field** (model / user / worker / public / mixed) —
   the human-vs-model welfare lexical trap, made structural.
4. **`model_scope` rule** (§3.8): whether company-wide policies satisfy
   flagship-model indicators — a genuinely new gap neither prior audit caught.
5. Minimum standard for "with reasoning" (≥1 explicit premise/mechanism/
   trade-off).
6. Stage rule for cross-stage co-firing (Acknowledge=proposition,
   Assess=method, Prepare=organisational rule; same passage may fire multiple
   stages via distinct clauses).
7. Report reliability separately per layer (status / assignment / best) —
   our own two-layer result (B reliable, A not) proves the point.

## Where this leaves the pilot

Complete. All planned evidence is in: 3-developer coverage (Protocol B,
reliable), dual-coder agreement (α/AC1 by layer), co-firing data, partials
inventory (59 ours + ~49 GPT), decidability flags, and two independent
methodology audits plus a coder-feedback memo set. Next artifact: the
**draft-4 revision memo** consolidating audits + pilot evidence into concrete
edits (registry fields, Notes layer, split/merge list, coding protocol,
restored guardrails).
