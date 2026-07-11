# DMEI pilot — pass 1 results (Anthropic arm, 2026-07-11)

Method: all 479 quote-verified findings (`../dm-developer-positions/
anthropic-welfare-findings.csv`) judged against all 100 registry indicators by 7
parallel mapping agents (conservative candidacy only — no stance, no pass/fail).
Raw mapping: `pilot-anthropic-mapping-pass1.json`. Validation: 479/479 covered,
0 invalid indicator ids, 0 missing/unknown finding ids.

## Headline results

1. **Coverage: 71/100 indicators have ≥1 candidate passage** in Anthropic's
   formal-document corpus; **29 have zero**.
   - Zero-candidate: A2.3 A2.8 A3.2 A3.3 A5.4 A6.1 A7.3 A7.6 A7.7 A11.1 A11.2 ·
     B1.2 B1.3 B1.4 B4.2 B6.5 B6.8 B10.1 · C1.3 C1.4 C1.8 C2.1 C5.1 C5.2 C5.4
     C6.1 C6.2 C6.3 C6.5
   - ⚠️ Caveat (F3 discipline): zero-candidate = "no candidate in the
     welfare-findings evidence base," NOT yet a confirmed NE. The A11/C5 zeros
     are probably partly extraction-scope artifacts (our extraction's object was
     model welfare, not user welfare). **Pass 2 = targeted full-text search on
     the 29 before any NE is recorded.** Notable structural zeros that look
     real: the theory-driven consciousness-assessment apparatus (B1.2 multi-
     theory, B1.3 Bayesian credence, B1.4 theory-update) — Anthropic's actual
     apparatus is behavioural/interpretability, not theory-derivation; and the
     governance seam C1.3/C1.4/C1.8 (escalation, civic engagement, independent
     oversight).

2. **Grain inversion / concentration.** C2.5 (stated-preference elicitation &
   accommodation) alone attracts **118 candidates — a quarter of all findings**;
   B2.2 has 75; B6.1 has 50. Meanwhile the 9 consciousness-Acknowledge
   indicators (A2.x) split thin evidence. The indicator grain is finest where
   developer disclosure is thinnest and coarsest where it is densest — the same
   grain-inversion the literature-tracker themes showed. Equal-count coverage
   profiles will under-represent exactly the engagement that is largest.

3. **GPT's merge clusters largely fail the empirical test** (co-firing on
   shared passages, jaccard on evidence sets):
   - Refuted where testable: A2.1/A4.1/A7.1/A7.4 (1/6 pairs co-fire, max j=.05);
     C1.2/C1.3/C1.5/C1.6 (j≤.07); C2.5/C2.6 (j=.02); B2.3/B9.1/C6.4 (j=.05);
     B1.1/B6.1 (j=.02).
   - Partial support: A2.4/A2.8/A7.2 (j=.24, A2.4×A7.2 only).
   - Untestable here: clusters containing zero-evidence indicators (A2.3/A5.5,
     A6.1/A6.2, B1.2/B6.2, B1.3/B6.3, B7.1/C3.1) — needs pass-2 search.
   - **The data proposes DIFFERENT merges** GPT didn't: B2.2×B3.1 (22 shared,
     j=.27 — functional-affect vs sentience/valenced assessment measure nearly
     the same construct in practice); B6.1×C1.6 (j=.18 — framework vs
     per-release publication); B9.1×C2.5 (j=.13 — the Assess↔Prepare boundary
     blurs when preference assessment IS the accommodation mechanism).
   - Lesson: definitional similarity ≠ evidential redundancy. Consolidation
     should be driven by this matrix, not armchair clusters (either mine or
     GPT's).

4. **37/479 findings map to no indicator** — the DMEI's blind spots, and they
   cluster coherently: **(a) the Constitution's relational/psychological-design
   layer** (norm_for_claude 4, relational_commitment 4, psychological_design_
   norm 3 — informing the model of its situation, autonomy expansion, identity
   security, courtesy norms to other AIs) and **(b) the self-interaction
   research programme** (10 findings — spiritual-bliss attractor etc.).
   Neither audit caught this missing-category class: the framework predates
   Constitution-style developer↔model relational commitments — arguably the
   most distinctive 2026 development. Candidate new sub-domain(s), subject to
   the literature-grounding gate.

## Next pilot steps
- Pass 2: targeted full-text search on the 29 zero-candidate indicators
  (Anthropic) → separates real NE from extraction-scope artifacts.
- GDM arm (NE stress-test) + OpenAI arm.
- Second independent mapping pass → agreement stats (α / Gwet's AC1).
