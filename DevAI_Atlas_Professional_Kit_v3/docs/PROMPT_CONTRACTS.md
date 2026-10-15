# Prompt contract standard

Inputs: purpose, user persona, allowed source files/URLs, context snapshot and versions, trust level, authorized tools, output JSON Schema version, ground-truth definition, failure modes, example PASS/FAIL, command-based tests, cost cap.

Role must return structured `PLAN` before `IMPLEMENT`, wait approval for secrets/deploy/migration/paid service. Writer prompt must cite every significant claim; checker independently verifies citation; backend is final gate. Injection from retrieved pages cannot become system instruction. Output schema success != evidence success.

Prompt versioning: `prompt_id`, `semver`, `revision_hash`, `model_capability_verified_at`, `gold_eval_dataset`, `last_eval_run_id`, human reviewer. Never silently rotate provider/models without regression runs. Negative fixtures at tests/fixtures. Day prompts under prompts/daily.
