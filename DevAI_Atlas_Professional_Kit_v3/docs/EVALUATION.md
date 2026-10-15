# LLM Evals and release gates

## Gold datasets
Start with 20 news fixtures: 5 official announcements, 4 duplicates, 3 unsupported rumors, 2 date/time traps, 2 injections, 2 contradictory sources, 2 license-denied. Each has expected decision, known claim evidence, reviewer rationale. Search Q/A gold: >=20 queries (10 known, 5 ambiguous, 5 cannot answer). Editorial evaluator blind to writer model where feasible.

## Metrics
- News: source precision, per-claim grounded precision, source-link resolution, hallucination count, duplicate rate, high-impact publication without review count (must equal 0), coverage of allowed sources, cost per published item.
- Search: retrieval recall@k, attribution precision, answer correctness, abstention accuracy, draft-leak count (must equal 0).
- Ops: schedule completion, delay, failure rate, retries, mean publish lag, p95 query latency, daily AI cost and 95% CI if sample warrants.

## Suggested starter thresholds, adjustable with documented rationale
0 high-risk auto-publish; 0 fake citations known gold; 0 guest draft reads; 100% schema-valid published articles; >=95% primary-source URL valid at publish time; >=90% gold classification pass (subject to sample size); 100% 18 UAT mandatory tests pass before release (or explicitly defer P1 tests); no 5xx from baseline smoke. These are **release objectives**, not current achieved metrics.

## Evaluation process
Run dataset on writer prompt vN and reviewer vN. Compare to expected decisions; investigate fail cases, add regression, repeat after provider/prompt schema change. Human adjudicates disagreements. Independent evaluation is not model self-rating.
