# Traceability matrix — NO MISSING FILE GATE

| Req | Day | Code/file groups needed | Tests and evidence | Release status |
|---|---|---|---|---|
| R-01 | 07–08 | content/tracks.yaml, content/lessons, src/features/learning, src/app/learn | 18 tracks + 6 verified lessons, links | NOT BUILT |
| R-02 | 07–08 | lesson schema, lesson renderer, content metadata | validate quiz + answers + source | NOT BUILT |
| R-03 | 08,11 | src/app/news, src/features/news | source URLs + timestamps/no fake | NOT BUILT |
| R-04 | 10 | src/features/ingestion/adapters, source registry | 3 allowed live sources + ToS evidence | NOT BUILT |
| R-05 | 10,12 | normalize, dedupe, migrations | rerun/concurrency tests | NOT BUILT |
| R-06 | 02,11 | schema, prompt, evidence validator, ai adapters | gold dataset eval, fake URL reject | NOT BUILT |
| R-07 | 09,11–12 | editor UI, authorization, publish transaction | high-risk cannot auto publish | NOT BUILT |
| R-08 | 12 | inngest scheduler, runs DB, run page, alert | manual replay + real schedule log | NOT BUILT |
| R-09 | 09 | auth, RLS, migrations, middleware/server checks | guest/editor/admin negative tests | NOT BUILT |
| R-10 | 13 | search FTS; RAG optional P1 | golden search & no draft leak | NOT BUILT |
| R-11 | 08–14 | CI, security, SEO, tests, budgets | exit code, audit results | NOT BUILT |
| R-12 | 14 | deployment env, runbook, metrics, rollback | public smoke + scheduled proof | NOT BUILT |

`NOT BUILT` is truthful: this kit is **curriculum + implementation contract**, not deployed Next.js system. Claude Code must update every row to PASS only after run evidence in `audit/ACCEPTANCE_EVIDENCE.md`. Verify missing paths via project/SOURCE_TREE.md.
