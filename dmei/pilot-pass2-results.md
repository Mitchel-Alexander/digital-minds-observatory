# DMEI pilot — pass 2 results (zero-candidate resolution, 2026-07-11)

Method: the 29 indicators with zero pass-1 candidates were re-searched against
the FULL 11-document Anthropic corpus (targeted multi-strategy search; 3 agent
groups + 3 groups run inline after agents hit a session limit). Discipline:
"found"/"partial" require a character-exact quote (all 20 **mechanically
verified verbatim** against source, 0 failures); "not_found" requires the
documented search-term list. Verdicts: `pilot-pass2-verdicts.jsonl`.

## Outcome: 8 found · 12 partial · 9 not_found

### The 8 false absences — pass-1 zeros that were NOT real, by failure mode

**Extraction-scope artifacts** (evidence exists but our extraction's object was
model welfare, so user-welfare/design content was never extracted):
- **A11.1, A11.2, C5.1, C5.4 found; C5.2 partial** — the entire
  human-interaction module lives in the Constitution (feeling-expression
  calibration, anti-reliance design duty, break-character-to-clarify-AI-status,
  uncertainty-reflecting self-representation). Confirms GPT's "separate
  human-interaction module" as a genuinely distinct object.

**Pass-1 mapping recall misses** (evidence was IN the findings dataset; the
mapper didn't connect it):
- **A3.3** intentional agency — robust-agency-as-moral-grounds, w/ reasoning
  (Opus 4.8 §7.4, Fable §7.1.1)
- **C2.1** inclusive moral-standing scope — agency grounds as alternative to
  valenced experience (Fable §7.1.1)
- **B4.2** uncertainty-aware moral-standing decisions — "acting where the
  expected benefits justify the costs" (Opus 4.8)
- **B6.5** welfare research contribution — Eleos external access + dedicated
  Model Welfare team

→ Protocol lesson, quantified: **28% of pass-1 zeros were false**, split
between the two predicted failure modes. Single-pass anything (extraction OR
mapping) under-recalls; the targeted-search backstop is not optional. This is
audit finding F3 with a measured magnitude.

### The 12 partials — the Notes-layer goldmine

Each rationale documents exactly where the corpus approaches but misses the
construct — real-material pass/fail boundary conditions for the codebook:
- A3.2 (understanding appears only in quoted MODEL transcripts — no developer
  position), A6.1 (facts of non-persistence disclosed; the user-facing
  *illusion* never acknowledged), A7.6 (public conversation acknowledged;
  public *stake in decisions* not), B1.3 (probabilistic humility without any
  stated/updated credence), B1.4 (richer-methods commitment not tied to
  consciousness science), **B10.1 (clause ii robustly assessed — the
  'encouragement of user delusion' metric — clause i never: a live multi-barrel
  demonstration, audit F8)**, C1.8 (Eleos assesses the model ≠ oversees the
  developer), C5.2, C6.1, **C6.2 (the only pause commitments are
  capability-triggered, never consciousness-triggered)**, C6.3 (info-hazard
  language exists but for bioweapons evals), C6.5.

### The 9 real absences — legitimate NE/0-coverage for the MOST engaged developer

A2.3 (theory pluralism) · A2.8 (absence-of-evidence epistemics) · A5.4
(matters-to meta-criterion) · A7.3 (justification drift) · A7.7 (pharma
burden-of-proof) · B1.2 (multi-theory derivation) · B6.8 (deliberative
credence-setting) · C1.3 (welfare escalation ladder) · C1.4 (civic engagement).

Two kinds, with different draft-4 implications:
- **Discriminating frontier (keep)**: B1.2, C1.3, C1.4, B6.8 — decidable,
  meaningful, and genuinely unmet even at the top of the field; these are the
  indicators that give the index headroom.
- **Researcher-shaped constructs (reword or move to an experimental module)**:
  A7.3 and A5.4 phrase demands no formal document is likely to ever satisfy in
  those terms; A7.7 additionally belongs to the human-interaction module and
  presumes a contested analogy (both audits flagged it).

## Consolidated pilot status
- Pass 1: 479 findings → 100 indicators (71 evidenced, mapping + co-firing).
- Pass 2: 29 zeros resolved → **79/100 indicators now evidenced or partial
  for Anthropic; 9 confirmed absent; 12 partial.**
- Remaining: GDM arm (NE stress-test), OpenAI arm, second independent mapping
  pass for agreement stats.
