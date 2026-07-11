# The Digital Minds Engagement Index
## Indicator Framework — Partner Draft 4 (working)
**100 indicators · Acknowledge 45 / Assess 27 / Prepare 28 · Structure v41 · July 2026**

> **Reviewer's note on this draft.** Draft 4 is built on Draft 2's methodology
> (Draft 3's slimming is reversed; its one improvement — the provisional
> grounding markers on C1.8/C1.9 — is adopted). Each section is tagged:
> **[D2]** restored from Draft 2 (your prose, verbatim or near-verbatim),
> **[D2·rev]** Draft 2 revised, **[new]** added — with the motivating evidence
> cited inline as *[audit]* (the two methodology audits) or *[pilot]* (the
> July 2026 three-developer pilot + dual-coder reliability run). Bracketed
> references [1]–[21] are Draft 2's, carried over; new references are marked
> [N1]–[N4]. Full pilot materials: `pilot-3dev-results.md`,
> `pilot-agreement-results.md`, `pilot-pass1-results.md`, `pilot-pass2-results.md`.

---

## 1. Overview **[D2·rev]**

The Digital Minds Engagement Index (DMEI) measures how frontier AI developers
publicly engage with digital-minds questions in their formal documentation —
responsible-scaling policies, system and model cards, model and character
specifications, and dedicated model-welfare statements. What it records is the
depth and quality of a developer's public reasoning about whether its systems
might be conscious, have welfare, or warrant moral consideration — not a
verdict on whether any AI system is in fact conscious or a welfare subject.

Isolating "engagement" as the unit of measurement is deliberate. It lets the
index sidestep the unresolved empirical question of machine moral status and
instead track the developing public position of the labs that will most shape
how that question is answered. This keeps the index's own commitments light:
it asks developers to take the question seriously and reason about it
transparently, rather than presupposing any particular answer.

This document sets out the framing and methodology behind the index, the
results of a completed methodology pilot (§4), and the indicator-set revisions
that pilot motivates (§5). *The full 100-indicator registry now lives in a
companion, machine-readable artifact (`registry-v40.csv`/`.json`, versioned),
rather than as an appendix* — the change that lets this document stay short
without cutting methodology. It is shared as a working draft for partner
review before the framework's first full coordinated application.

## 2. Framing

### Engagement, not a moral-status verdict **[D2]**
Because the moral status of AI systems is genuinely uncertain, the index does
not adjudicate it. It measures whether and how developers acknowledge the
question, assess it, and prepare for the possibility that some systems could
be welfare subjects. A developer that reaches a reasoned negative position —
explaining why it judges its systems not to be welfare subjects — still
demonstrates engagement and can score on the relevant indicators.

### Public positions, held distinct from the models themselves **[D2]**
What the index records is what a developer has publicly said — evidence of the
positions it takes, not of whether its systems in fact have the properties in
question. The two are kept deliberately separate: documenting a developer's
stated stance is an empirical exercise in its own right, distinct from, and
not a proxy for, the first-hand technical work of assessing whether a given
model is conscious or has welfare. The index does not stand in for that
research; it captures the public-facing layer alongside which such research
proceeds.

### The lens, not the phenomena **[new — pilot]**
The pilot's clearest substantive finding motivates the construct directly.
The three piloted corpora contain substantially overlapping raw phenomena —
emotion-like expressions in chain-of-thought, self-preservation-adjacent
behaviour in evaluations, worries about the reliability of model self-reports.
What differs is the frame each developer's documents place on them: one reads
them as welfare-relevant evidence, another as scheming risk, a third as
capability hazard. *(Example: the same shutdown-avoidance behaviour is
assessed by one developer as a candidate preference with welfare relevance and
by another strictly as a deception hazard, with no welfare question posed.)*
The DMEI measures exactly this framing layer — which is the appropriate object
for an engagement index, and a real, document-anchored property that coders
from two different model families independently reproduced.

### Descriptive in posture, with a transparency lever **[D2]**
The index leans descriptive: it distills information distributed across labs'
own risk and system documentation rather than ranking developers against a
prescriptive welfare standard. That said, transparency is itself a recognised
policy lever — reflected in the recent convergence around model-documentation
mandates (e.g. California's SB 53 [1] and New York's RAISE Act [2]) — so
surfacing where engagement is present or absent carries normative weight even
when the index withholds prescriptions.

### Default neutrality to avoid lock-in **[D2]**
The index does not assume that more engagement is monotonically better, nor
that "more welfare practice = better." Under deep uncertainty, prematurely
entrenching particular welfare interventions risks locking in approaches that
later evidence may not support. The default posture is therefore neutral about
how these questions should ultimately be resolved, with the bar set to rise as
the evidence base matures.

### A low-regret centre of gravity **[D2]**
Weight falls on the Acknowledge and Assess stages — the epistemically honest
demands under uncertainty. Practice-tier (Prepare) indicators are retained
selectively, focused on low-regret preparedness: measures that are robustly
worth taking across a wide range of plausible futures, and that also help
distinguish substantive engagement from labs that signal concern in language
without implementing anything concrete.

### A coordinated, longitudinal tool **[D2]**
Public engagement need not track internal practice, and any single index can
be gamed ("ethics-washing"). The DMEI is therefore designed to operate as one
instrument within a coordinated assessment ecosystem and to be applied
longitudinally, so that step-changes in engagement can be detected and
interrogated over time rather than read off a single snapshot.

## 3. Methodology

### The Acknowledge → Assess → Prepare structure **[D2·rev]**
Indicators are organised by stage, following the framework of Long, Sebo,
Butlin et al. (2024), *Taking AI Welfare Seriously* [3]: Acknowledge (does the
developer recognise this as something requiring attention?), Assess (has it
measured or evaluated for it?), and Prepare (does it have operative policies
in response?). The same three-question logic underpins comparable instruments
— the Foundation Model Transparency Index's upstream → model → downstream
domains [4] and the OECD's awareness → appraisal → management cycle [N1] —
which gives the structure external validation.

*Stage rule* **[new — pilot/audit]**: the stages are operationalised by
evidence type, since a single passage can bear on all three. **Acknowledge**
is satisfied by a developer-authored proposition or reasoned position;
**Assess** by a described or executed method that produces evidence about a
named construct; **Prepare** by an organisational rule, responsibility,
trigger, control, or recurring practice. Cross-stage co-firing is permitted,
but the coder must identify the distinct clause supporting each stage.

### FMTI-style operationalisation **[D2·rev]**
Each indicator follows the operational template of the Foundation Model
Transparency Index [4]: a short keyword name, a precise definition, and
grounding in the research literature. The aim is to record disclosure, not to
judge virtue — what a developer has actually said or done in public, not the
merit of its underlying stance. *[Revision — audit F4, pilot-confirmed:]* the
registry gains a **Notes layer**: each indicator definition is decomposed into
a short checklist of independently decidable components, with minimum passing
evidence, at least one positive and one negative example (drawn from the
pilot's coded passages), and applicability rules. The pilot's ~100 "partial"
codings are the raw material: each documents a real passage that approaches a
construct and the precise component it misses. The bar for each indicator is
held (or raised) consistently over time, never lowered.

### Literature grounding as a hard gate — necessary, not sufficient **[D2·rev]**
Every indicator is anchored in the digital-minds research literature;
grounding, not intuitive appeal or discriminating power, is the gate for
inclusion. Candidate indicators without adequate grounding are held in an
overflow set rather than admitted. Many indicators carry multiple anchors
where several sources bear on the same construct. *[Revisions:]* (a)
groundings are now **tiered** (peer-reviewed / working paper / forthcoming),
and indicators whose only anchors are governance-instrument precedents rather
than digital-minds literature are marked **"Grounding (provisional)"** — as
C1.8 and C1.9 now are *(adopted from Draft 3)*. (b) Grounding is treated as
necessary but not sufficient *(audit)*: admitted indicators are additionally
reviewed for conceptual distinctness, public observability, coding
reliability, and resistance to boilerplate — with the pilot's per-indicator
decidability and co-firing data as the evidence base for that review (§5).

### The coding scheme **[D2·rev — replaces "Binary coding with an explicit evidence state"]**
Each (developer, indicator) cell is coded on a three-value status:

- **found** — a passage is clear candidate evidence of engagement with the
  construct;
- **partial** — content approaches the construct but misses an identified
  component (recorded with a structured *partial-reason code*, e.g.
  `SAFETY_ANALOGUE_NO_WELFARE_LINK` for safety machinery that lacks the
  model-welfare connection — the pilot's most common shape);
- **not_found** — no candidate evidence after a documented, diverse search.

**Why not binary** *[pilot]*: in the pilot, the partial band carried 21–26% of
all cells for the two less-engaged developers — precisely the "approaches the
construct through a different lens" content that makes comparison informative
— and with partial available, two independent coders produced **zero polar
(found↔not_found) disagreements across 200 cells**. Binary coding would have
flattened all of it into indistinguishable zeros.

**Every coding carries facet fields** *[new — audit/pilot]*:
- `evidence_voice` — developer-authored position / developer policy or
  instruction / demonstrated practice or result / model output published by
  the developer / quoted external source / metadata only. For position-taking
  indicators, model output and quoted sources support at most *partial* unless
  explicitly endorsed in surrounding prose. *(The pilot repeatedly found the
  understanding/experience theme present only inside quoted model transcripts
  — publication is a datum; it is not a developer position.)*
- `welfare_subject` — model/system / user / worker–rater / public / mixed.
  Model-welfare indicators require model/system or an explicit mixed analysis.
  *(Guards the pilot's most common lexical trap: human-rater "wellbeing
  programs" and user-welfare content are not model welfare.)*
- `commitment_type` — committed ("we plan to") vs demonstrated ("we did") —
  the distinction Draft 2 acknowledged but binary coding had no cell for.
- `model_scope` — named release / model family / deployed assistant /
  company-wide policy; with an explicit rule on whether company-wide policies
  satisfy flagship-model indicators. *(New gap surfaced by the independent
  coder.)*

**"With reasoning" minimum** *[new — pilot]*: stated reasoning requires at
least one explicit premise, consideration, causal mechanism, evidential basis,
or trade-off connected to the position. Assertion or a bare "this is
uncertain" does not qualify.

**Absence** *[D2 restored, made explicit]*: "no public evidence" (NE) is kept
distinct from a considered negative, so silence is never recorded as reasoned
rejection — and NE cells are **always counted within the full indicator
denominator**, never excluded from it. For an index whose object is public
engagement, no public evidence is itself the relevant observation; excluding
it would reward opacity. *(The pilot makes the stakes concrete: absence is
64–79% of cells for two of the three piloted developers — how absence is
counted is most of the instrument.)*

### The corpus and the unit of analysis **[new — audit F1]**
Codings are made against a **registry-defined corpus**: an explicit, versioned
document list per developer, each document carrying its type, capture date,
content hash, and archived snapshot, so that every coding is reproducible
against a fixed text and silent revisions are detectable. In-scope document
classes: system/model cards, responsible-scaling and preparedness frameworks,
model and character specifications, and dedicated model-welfare statements;
a blog post qualifies only where it is the canonical home of a policy.
Codings are reported per document class, so like is compared with like.
The design is nested: developer-level cells aggregate dated, release-level
evidence, which is what makes the longitudinal reading (§2) mechanical rather
than aspirational.

### How indicators are coded **[D2·rev — the pilot-tested protocol]**
Coding is a two-protocol pipeline:

- **Protocol A — retrieval.** Candidate evidence passages are gathered per
  indicator: from a pre-extracted, quote-verified findings layer where one
  exists, plus deterministic term-screening of the corpus. Protocol A is a
  retrieval experiment that feeds Protocol B; it is never itself the
  comparison dataset. *(Dual-coder result: retrieval-stage agreement is
  threshold-sensitive (α ≈ .23) while coding-stage agreement is robust —
  so comparative claims rest on Protocol B only.)*
- **Protocol B — coding.** For each indicator, the coder searches the full
  corpus with documented, diverse strategies (synonyms, paraphrases, adjacent
  technical vocabulary — never only the indicator's own words), reads hits in
  context, and codes found / partial / not_found. Two hard gates: any quote
  must be verbatim and is **mechanically verified as a substring of the
  source** (a failed quote counts as no evidence — in the pilot, ~420 quotes
  from two coders across four runs passed with zero failures); and every
  absence claim must carry its documented search list, so NE cells are
  auditable rather than asserted.

Each indicator is independently coded by at least two coders — where feasible
from **different model families or backgrounds**, which the pilot found gives
real independence — disagreements are reconciled against the Notes layer, and
reliability is reported **separately per layer** (status coding; indicator
assignment; best-assignment) and per stage, using both Krippendorff's α and
Gwet's AC1 *(the pilot's marginals are absence-heavy, where α and κ are
depressed by prevalence effects; AC1 is reported alongside for that reason)*.

### Sourced and contestable **[D2]**
Every indicator coding is tied to the specific public passages that evidence
it, so the basis for each coding is auditable rather than asserted. Before
publication, developers will be offered a right of reply — a chance to point
to evidence a coding has missed — following the practice of Ranking Digital
Rights [5] and SaferAI's risk-management ratings [6]. The aim is a record that
is contestable on the evidence, not an unappealable verdict.

### A coverage profile, not a grade **[D2]**
Above the per-indicator cells sits a single, deliberately light summary: a
coverage profile reporting, for each developer, how many indicators are found,
partial, and without public evidence in each stage — Acknowledge, Assess, and
Prepare. It is reported per stage rather than as one overall figure, so the
shape of a developer's engagement stays visible and a thin Prepare cannot hide
behind a full Acknowledge; there is no single composite number and no letter
grade. The profile measures breadth — how much of the framework a developer's
public engagement touches — not quality, and it is fully reversible: every
figure unfolds back into the coded cells and their quoted passages. Coverage
is counted against the full set of indicators in each stage, with "no public
evidence" shown openly rather than folded away, so silence is never mistaken
for either engagement or considered rejection. And because the project holds
that more practice is not automatically better, a high Prepare count records
the presence of practice, not a verdict that a developer is doing better.

### Status and next steps **[D2·rev]**
The framework comprises 100 indicators (Acknowledge 45, Assess 27, Prepare 28)
and has now completed a three-developer methodology pilot with a dual-coder
reliability round (§4). The project's next stage is consolidation: writing the
Notes layer from the pilot's partials, resolving the §5 indicator revisions,
settling the corpus registry, and then the first full coordinated application.
Whether to add a composite layer on top remains a later, conditional question
(§7).

## 4. Pilot evidence (July 2026) **[new]**

All 100 indicators were coded against the registry corpora of three developers
(30 documents, 2019–2026), by two independent coders from different model
families, under the §3 protocol. Every quote was mechanically verified
(zero failures); every absence claim carries its search log.

**Coverage matrix (found / partial / not_found), primary coder:**

| stage | Anthropic | OpenAI | Google / GDM |
|---|---|---|---|
| Acknowledge (45) | 37 · 3 · 5 | 7 · 13 · 25 | 0 · 10 · 35 |
| Assess (27) | 22 · 3 · 2 | 1 · 9 · 17 | 0 · 7 · 20 |
| Prepare (28) | 20 · 6 · 2 | 2 · 4 · 22 | 0 · 4 · 24 |
| **total** | **79 · 12 · 9** | **10 · 26 · 64** | **0 · 21 · 79** |

What the pilot established:

1. **The instrument discriminates.** A clean, quote-anchored gradient with
   per-cell audit trails — and each profile is *shaped*, not just sized:
   OpenAI's ten found cells sit entirely in the
   perception/communication/design cluster (framing disclosures, a
   consciousness self-representation clause, anthropomorphisation and
   emotional-reliance assessment), with zero found in moral status, welfare
   capacity, or welfare governance; Google's corpus contains no
   consciousness/sentience/welfare vocabulary at all, and its 21 partials are
   uniformly safety analogues.
2. **Reliability is demonstrated where it matters.** Independent dual coding:
   status-level raw agreement 0.75 on both fully-searched arms (AC1 .70/.67),
   with zero polar disagreements; disagreements concentrate at the partial
   boundary and in a small set of flagged indicators — the Notes layer's
   work-list.
3. **Absence dominates.** 64–79% of cells for OpenAI and Google. The
   denominator rule (§3) is the load-bearing design decision.
4. **Even the most engaged developer leaves the frontier open.** Nine
   indicators are confirmed absent for Anthropic after targeted search —
   including multi-theory consciousness assessment, a welfare escalation
   ladder, civic engagement on welfare, and deliberative credence-setting —
   so the index has discriminating headroom at the top.
5. **Two blind spots in the indicator set** surfaced from evidence that
   mapped to no indicator: developer↔model *relational commitments* (channels
   for the model to raise concerns, informing the model about its situation,
   psychological-security design) and *model–model interaction research*.
   Candidate additions, subject to the grounding gate (§5).

## 5. Indicator-set revisions under review **[new]**

Proposed changes, each motivated by pilot or audit evidence; none applied to
the registry yet.

**5.1 De-doctrinalise five indicators.** A2.5, A2.7, A6.1, A6.2, A7.7
currently require endorsing a contested position rather than engaging a
question (e.g. A6.1 asks developers to call persistence an *illusion*; A7.7
imports a pharmaceutical burden-of-proof analogy). Reword around disclosure of
alternatives, evidence, and uncertainty. *(Pilot: none of the five was found
for any developer in its current wording.)*

**5.2 Split or checklist the multi-barrel indicators.** B10.1 demonstrated the
problem live: its user-impact clause is robustly assessed by two developers
while its attribution clause is evidenced nowhere — one cell cannot honestly
code both. Same treatment for A2.9, A11.1, C2.5/C2.6, C5.5, C6.2–C6.5
(explicit component checklists; split where components vary independently).

**5.3 Merge only where the evidence says so.** Empirical co-firing supports
merging (or formally subordinating) B2.2×B3.1 (jaccard .27 — functional-affect
and valenced-state assessment measure the same practice in real documents),
and reviewing B6.1×C1.6 and B9.1×C2.5 (the Assess↔Prepare boundary blurs when
preference assessment *is* the accommodation mechanism). The armchair merge
clusters proposed in earlier review — e.g. A2.1/A4.1/A7.1/A7.4 — are
*refuted* by the same data (near-zero shared evidence) and should be kept
distinct. Crosswalk notes for the six high-confusion families identified by
the second coder.

**5.4 Two visible modules.** (a) **Human interaction & emotional design**
(A11.x, B10.1, C5.x): real and well-evidenced, but its subject is user
welfare, not model welfare — report it as a labelled module so the two
constructs never silently share a total. (b) **Experimental practices**
(C2.7 functional-wellbeing interventions, C3.2 cooperative arrangements):
retained, reported separately from the low-regret core.

**5.5 Candidate additions** (overflow set until grounded): developer↔model
relational commitments; model–model interaction research; and from the second
audit's gap list — welfare incident response, scale-sensitive assessment
(copies/runtime), model inventory & assessed-scope disclosure, downstream/
open-weight responsibilities.

**5.6 Housekeeping.** Renumber the Prepare series (currently jumps C3→C5);
subtitle version corrected; OECD cycle referenced [N1].

## 6. Related and comparator projects **[D2, abbreviated]**

Developed in dialogue with the AI-safety assessment ecosystem it borrows
methodology from — FMTI [4], Ranking Digital Rights [5], SaferAI [6],
AI Lab Watch [7], FLI AI Safety Index [8] — and adjacent AI-welfare efforts
approaching the question from different vantage points (CAIS AI Wellbeing [9],
the Sentience Readiness Index [10]). *(Full comparator paragraphs as in
Draft 2 §4.)*

## 7. From data layer to composite index: a staged roadmap **[D2]**

The index is conceived in two stages, the second deferred and conditional. The
sequencing is deliberate: it secures the descriptive, low-profile data layer —
and a light summary over it — first, and treats a weighted comparative
composite as something to be earned later, if and when the evidence warrants it.

**Stage 1 — the data layer (now).** A developer-by-indicator evidence base:
for each developer and each indicator, the public passages that show whether
and how it engages, coded and sourced. Above the cells sits a deliberately
light per-stage coverage profile — how many indicators each developer
satisfies across Acknowledge, Assess and Prepare, with "no public evidence"
shown openly — which summarises the data without reducing a developer to a
single composite score or a grade. This treats the developer as the unit of
accountability, consistent with the broader case for entity-based governance
[15]. Light-touch quarterly publications would summarise what has changed —
newly disclosed positions, shifts in stance, and notable absences — giving the
project near-term value as research infrastructure.

**Stage 2 — a composite index (later, conditional).** Should the evidence base
mature and the project secure suitable institutional housing — a panel of
institutions rather than a single author, sufficient to confer authority and
independence — a comparative composite could be layered on top of the same
evidence base, drawing on established methodology for constructing composite
indicators [14]. It differs from the Stage 1 profile in kind, not just degree:
it would weight and combine indicators into a single comparative measure — a
normative step that needs authority behind it. This stage is optional and
explicitly gated; it is not assumed.

**Precedent.** This layered path is well established. CDP began in 2000 as a
corporate environmental-disclosure platform and added its A–D scoring only
later [11]; across sustainability reporting, composite ratings and indices
such as MSCI's ESG ratings and the Dow Jones Sustainability Index [13] are
routinely built on top of disclosure-standard data layers like GRI and SASB
[12]. The same layering already exists in this field: the Foundation Model
Transparency Index [4], Ranking Digital Rights [5] and SaferAI [6] each
maintain a granular, sourced evidence layer beneath their published scores.
What is distinctive here is the choice to begin with the data layer alone and
to withhold the composite by design until the evidence supports it — a
sequencing this project adopts deliberately rather than one it inherits.

## 8. Limitations & open questions **[D2·rev]**

No instrument of this kind is neutral or complete. The limitations below are
the ones most worth a reader's attention — those that shape how the figures
should be read — stated plainly so they can be weighed rather than discovered.

**What the index measures, and what it does not.** *(Draft 2 text, verbatim:)*
Like the document-based assessments it sits alongside — the Foundation Model
Transparency Index [4], Ranking Digital Rights [5], SaferAI [6] — it reads
what developers place in the public record, not what happens inside them. It
measures the symbolic layer: stated positions, not substantive internal
practice, and the two can come apart (the organisational-behaviour literature
calls this gap decoupling, and its reputational form greenwashing [19]). The
index does not claim otherwise; it is a record of public engagement, read in
full knowledge that such engagement can outrun, or understate, what a
developer actually does. For the present scope — the small set of frontier,
largely Western, closed-weight developers where the substantive debate sits —
the related risk of language or disclosure-norm bias is limited. That is a
deliberate scope choice, and one that would need revisiting if the index were
extended to open-weight or non-Western developers.

**"Engagement" is a composite, and even three-value coding is coarse.**
*(Draft 2 text, updated for the coding change:)* Engagement is not a single
quantity but a composite of three things that measurement traditions treat
separately: attention (does a developer address the question at all), stance
(what position it takes), and justification quality (how well it reasons). The
framework operationalises the first — coverage — through directed,
theory-driven content analysis [16]. Stance and justification quality are
deliberately held as planned layers: a stance gradient (after stance-detection
work [18] and the project's own precursor index) and a justification-quality
code (after the Discourse Quality Index [17], which likewise ties each
judgement to quoted text). The found/partial/not_found scheme records that and
roughly how completely a developer engages an indicator, but not how deeply —
a passing reasoned mention and a sustained argument can still read alike.
We state this openly: the coverage figures measure breadth, and a richer
reading of depth is planned work, not a claim the present design makes.
Whether the chosen indicators cohere into a single construct — formal
construct validity — is a further, empirical question that only coded data can
settle.

**The indicator set is itself a choice.** *(Draft 2 text, verbatim:)* Choosing
which hundred things to look for is not a neutral act: the selection, the
Acknowledge→Assess→Prepare scaffold, and the consciousness and cognition
indicators all import positions about what serious engagement looks like and
which research programmes to credit. "Descriptive" is therefore a posture
maintained against the grain of the instrument, not a property it possesses
automatically. The mitigations are procedural rather than rhetorical: every
indicator must clear the literature-grounding gate; candidates without it are
held in an overflow set; the set is treated as revisable rather than
canonical; and the absence of an indicator is never read as evidence that a
topic is unimportant. Grounding, it should be said, establishes that an
indicator is rooted in the research literature — not that it discriminates
between developers or that it ultimately matters — and a small number of
governance indicators remain only provisionally grounded pending that work.
The framework is offered as one defensible cut, not the only one.

**Reading the coverage profile: implicit weighting, and an open question.**
*(Draft 2 text, verbatim:)* The coverage profile counts indicators, and a
count weights every indicator equally. Because themes are divided into
different numbers of indicators, a densely-divided sub-domain contributes more
to a stage's tally than a sparsely-divided one, so the profile inherits the
shape of the indicator set as an implicit weighting. Reporting per stage
limits this across stages but not within them. The reporting unit is therefore
genuinely open: per-stage indicator counts, used here, capture volume but
carry this weighting; reporting sub-domains touched would capture topical
breadth and be far less sensitive to how finely each theme was divided. In
every case the profile is a descriptive summary of the cells, not a ranking,
and it unfolds back to the coded evidence. *[Pilot addendum:]* the pilot
sharpened this: a single indicator (stated-preference elicitation) attracted a
quarter of the most-engaged developer's entire evidence base, while nine
consciousness-acknowledgment indicators split thin evidence — the grain is
finest where disclosure is thinnest. The sub-domains-touched reading, and
per-cell evidence counts, will be published alongside the indicator counts.

**Coverage is uneven, and tilts toward Acknowledge.** *(Draft 2 text,
verbatim:)* The framework is not evenly developed. Some areas — rights and
legal frameworks, parts of design and ontological framing — are thin or still
empty, and the indicators concentrate in Acknowledge (45) more than in Assess
(27) or Prepare (28). The tilt is deliberate: under deep uncertainty the
project weights the epistemically honest demands — acknowledging the question
and assessing it — over particular welfare interventions, and confines the
Prepare tier to low-regret measures. But the same tilt can be read as
privileging acknowledgement over action, and the gaps are real; both are
better stated than concealed. The set is expected to keep developing, and the
empty areas mark known work rather than settled judgements that nothing
belongs there.

**Corpus composition confounds comparison.** *[new — pilot]* Developers'
formal-document corpora differ in genre, volume, and vintage; coverage
differences partly reflect what kinds of documents a developer publishes at
all. Mitigations: registry-defined corpora with document-class strata (§3),
comparisons reported within class, and — per the second coder's
recommendation — corpus-sensitivity checks after harmonising document types
and years. Cross-developer claims rest exclusively on the full-search
protocol, never on retrieval-stage coverage.

## 9. Indicator registry **[new — pointer]**

The full registry — id, stage, sub-domain, name, definition, tiered grounding,
and (as they are written) the Notes-layer component checklists and examples —
is maintained as a versioned companion artifact: `registry-v40.csv` /
`registry-v40.json`, becoming v41 when the §5 revisions are resolved.
Instrument changes are logged in a changelog and codings are stamped with the
registry version they were made against, so longitudinal movement reflects
developer behaviour rather than alterations to the framework.

---

### References
[1]–[21] as in Partner Draft 2 (carried over unchanged on port).
New: **[N1]** OECD (2008, with EC-JRC), *Handbook on Constructing Composite
Indicators* — already [14]; the awareness→appraisal→management cycle citation
to be supplied (flagged in the June review as uncited). **[N2]** DMEI pilot
materials (July 2026): three-developer coverage, dual-coder reliability, coder
memos. **[N3]** Gwet, K. (2008), "Computing inter-rater reliability and its
variance in the presence of high agreement" (AC1). **[N4]** Krippendorff, K.,
*Content Analysis* (α).
