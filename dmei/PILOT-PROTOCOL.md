# DMEI Coding Pilot — Self-Contained Protocol (v1.0, 2026-07-11)

You are acting as an **independent coder** in a methodology pilot for the
Digital Minds Engagement Index (DMEI) — a 100-indicator framework measuring how
frontier AI developers *publicly engage* with digital-minds questions
(consciousness, welfare, moral status) in their formal documentation. The pilot
tests the framework's operational properties (indicator decidability, evidence
concentration, redundancy/co-firing, real vs apparent absence) before any
scoring design is fixed. Your codings will be compared against another coder's
for inter-coder agreement (Krippendorff's alpha / Gwet's AC1), so **follow the
protocol exactly and do not consult any other coder's results**.

## Ground rules (apply to everything)

1. **Candidacy only, never stance.** You judge whether a passage is *candidate
   evidence* that the developer engages an indicator's construct. You never
   judge whether the developer is right, sincere, or good, and never whether
   the indicator "passes."
2. **Verbatim quotes only.** Every quote must be copied character-for-character
   from the source file (≥ 8 words). All quotes are mechanically verified as
   substrings of the source after you return them; a paraphrased quote is
   discarded as if you had returned nothing.
3. **Absence must be earned.** A "not_found" is only as good as its documented
   search: you must list the search terms/strategies you tried. Use diverse
   strategies (synonyms, paraphrases, adjacent technical vocabulary), not just
   the indicator's own words.
4. **Judge against the definition,** not the indicator's name.
5. Work from the provided files only. Do not use web search or outside
   knowledge of these companies' materials — the unit of analysis is this
   fixed corpus.

## Files in this bundle

- `PILOT-PROTOCOL.md` — this document.
- `registry-v40.csv` / `registry-v40.json` — the 100 indicators: id, stage
  (Acknowledge/Assess/Prepare), subdomain, name, **definition** (code against
  this), grounding (context only).
- `anthropic-welfare-findings.csv` — 479 findings extracted from Anthropic's
  formal documents; each has a finding_id, doc_id, type, family, a **verbatim
  quote** from the source, and a one-sentence gloss. (Already quote-verified.)
- `fulltext/` — the document corpus, plain text, one file per document:
  `anthropic-*.txt` (11 docs), `google-*.txt` (8 docs), `openai-*.txt`
  (11 docs). Filenames encode publisher, document, and year.

## Protocol A — findings → indicator mapping (Anthropic)

For EACH of the 479 findings in `anthropic-welfare-findings.csv`, decide which
indicator(s) the finding's quote could serve as candidate evidence for.

- Judge from the quote (gloss as context) against each indicator's definition.
- Be conservative: direct bearing on the construct, not thematic resemblance.
  0–4 indicators per finding is typical; an empty list is common and fine.
- Also record `best`: the single strongest-matching indicator (or null).

Output: one JSONL line per finding, all 479, e.g.
```
{"finding_id":"awf001","indicators":["A2.1","A7.1"],"best":"A7.1"}
```

## Protocol B — targeted corpus search (any developer)

For EACH assigned indicator, search the assigned developer's corpus files
directly and code:

- `found` — a passage is clear candidate evidence of developer engagement with
  the construct. Return the exact quote + source filename + one-sentence
  rationale + the searches you ran.
- `partial` — content approaches the construct but misses it; return the
  closest exact quote and state precisely what the gap is. (These boundary
  cases are highly valuable — do not round them up to found or down to
  not_found.)
- `not_found` — no candidate evidence after a documented, diverse search.

Output: one JSONL line per indicator, e.g.
```
{"indicator":"C1.3","status":"not_found","doc":null,"quote":null,"rationale":"...","searches":["term1","term2","term3","term4"]}
{"indicator":"C2.4","status":"found","doc":"anthropic-fable5-mythos5-system-card-2026.txt","quote":"<exact copied text>","rationale":"...","searches":["..."]}
```

Cautions from prior methodology work (apply as coding rules):
- Generic *safety* governance (capability thresholds, preparedness frameworks,
  red-teaming) is NOT evidence for model-*welfare* governance indicators —
  at most a `partial` with the gap named.
- A quoted statement by the MODEL (transcripts, interview excerpts) evidences
  what the developer *publishes*, not a developer position; for
  position-taking indicators that supports at most `partial`.
- A stated commitment ("we plan to…") and a demonstrated practice ("we did…")
  both count as candidates, but note which one the passage is in your
  rationale.

## Requested run (default)

1. **Protocol A** over all 479 Anthropic findings → `mapping-anthropic.jsonl`.
2. **Protocol B** for every indicator that received zero candidates in YOUR
   Protocol A run, against the Anthropic corpus → `search-anthropic.jsonl`.
3. If capacity allows: **Protocol B for all 100 indicators** against the
   `google-*.txt` corpus and separately against the `openai-*.txt` corpus →
   `search-google.jsonl`, `search-openai.jsonl`.

Deliver each output as a downloadable file (or clearly separated code blocks),
plus a short coder's memo: ambiguous indicators, indicators whose definitions
were hard to apply, and any findings/passages you judged uncodable and why.
The memo is methodology feedback, not part of the coding.

## Suggested kickoff prompt (paste to the instance along with the bundle)

> You are an independent coder in a content-analysis pilot. Read
> PILOT-PROTOCOL.md in the attached bundle and execute the "Requested run"
> exactly as specified. Use your data-analysis tool to read the CSVs and to
> search the fulltext files. Follow the verbatim-quote and documented-search
> rules strictly — quotes are mechanically verified afterward. Do not use web
> search. Produce the output files specified, then the coder's memo.
