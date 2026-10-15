# SOURCE TREE — complete file contract for the future application

**Total explicitly required project source files: 157.** This is a source IMPLEMENTATION CHECKLIST, not a claim these files exist. The kit contains all docs/prompts/schemas/fixtures necessary for AI-directed generation; the runnable application must be generated, deployed and tested separately.

Use `python project/audit_source_tree.py /path/to/devai-atlas` for the 144 P0 MVP files, or append `--all` to audit all 157 files including 13 P1 optional enhancements. The command must return exit code 0 before claiming source-file coverage for that scope. A file existing but containing placeholder/TODO is not implementation-complete, so static source audit is only the first gate.

## Coverage by area

### Core setup — 13 files
- [ ] `README.md`
- [ ] `CLAUDE.md`
- [ ] `AGENTS.md`
- [ ] `.gitignore`
- [ ] `.env.example`
- [ ] `.env.test.example`
- [ ] `package.json`
- [ ] `package-lock.json`
- [ ] `tsconfig.json`
- [ ] `next.config.ts`
- [ ] `eslint.config.mjs`
- [ ] `postcss.config.mjs`
- [ ] `components.json`

### Claude agent control — 7 files
- [ ] `.claude/settings.json`
- [ ] `.claude/agents/researcher.md`
- [ ] `.claude/agents/editor.md`
- [ ] `.claude/agents/security-reviewer.md`
- [ ] `.claude/skills/lesson-author/SKILL.md`
- [ ] `.claude/skills/news-verifier/SKILL.md`
- [ ] `.claude/skills/source-auditor/SKILL.md`

### CI/CD — 3 files
- [ ] `.github/workflows/ci.yml`
- [ ] `.github/workflows/security.yml`
- [ ] `.github/CODEOWNERS`

### Public UI — 17 files
- [ ] `src/app/layout.tsx`
- [ ] `src/app/globals.css`
- [ ] `src/app/page.tsx`
- [ ] `src/app/not-found.tsx`
- [ ] `src/app/error.tsx`
- [ ] `src/app/loading.tsx`
- [ ] `src/app/sitemap.ts`
- [ ] `src/app/robots.ts`
- [ ] `src/app/about/page.tsx`
- [ ] `src/app/sources/page.tsx`
- [ ] `src/app/learn/page.tsx`
- [ ] `src/app/learn/[track]/page.tsx`
- [ ] `src/app/learn/[track]/[lesson]/page.tsx`
- [ ] `src/app/news/page.tsx`
- [ ] `src/app/news/[slug]/page.tsx`
- [ ] `src/app/search/page.tsx`
- [ ] `src/app/ask/page.tsx`

### Auth & admin UI — 8 files
- [ ] `src/app/login/page.tsx`
- [ ] `src/app/signup/page.tsx`
- [ ] `src/app/admin/layout.tsx`
- [ ] `src/app/admin/page.tsx`
- [ ] `src/app/admin/sources/page.tsx`
- [ ] `src/app/admin/review/page.tsx`
- [ ] `src/app/admin/runs/page.tsx`
- [ ] `src/app/admin/metrics/page.tsx`

### API routes — 7 files
- [ ] `src/app/api/inngest/route.ts`
- [ ] `src/app/api/admin/run-now/route.ts`
- [ ] `src/app/api/admin/review/[id]/route.ts`
- [ ] `src/app/api/news/route.ts`
- [ ] `src/app/api/search/route.ts`
- [ ] `src/app/api/ask/route.ts`
- [ ] `src/app/auth/callback/route.ts`

### UI components — 11 files
- [ ] `src/components/layout/site-header.tsx`
- [ ] `src/components/layout/site-footer.tsx`
- [ ] `src/components/learning/track-card.tsx`
- [ ] `src/components/learning/lesson-renderer.tsx`
- [ ] `src/components/learning/quiz.tsx`
- [ ] `src/components/news/news-card.tsx`
- [ ] `src/components/news/source-evidence.tsx`
- [ ] `src/components/admin/editorial-queue.tsx`
- [ ] `src/components/admin/job-run-table.tsx`
- [ ] `src/components/ui/button.tsx`
- [ ] `src/components/ui/empty-state.tsx`

### Content & lesson logic — 11 files
- [ ] `content/tracks.yaml`
- [ ] `content/lessons/ai-vs-llm-and-agents.mdx`
- [ ] `content/lessons/tokens-context-and-hallucinations.mdx`
- [ ] `content/lessons/selecting-providers-by-eval.mdx`
- [ ] `content/lessons/prompt-and-json-contract.mdx`
- [ ] `content/lessons/claude-code-plan-verify.mdx`
- [ ] `content/lessons/workflows-agents-mcp-rag.mdx`
- [ ] `src/features/learning/tracks.ts`
- [ ] `src/features/learning/lesson-loader.ts`
- [ ] `src/features/learning/lesson-schema.ts`
- [ ] `src/features/learning/lesson-index.ts`

### Ingestion and source integrity — 10 files
- [ ] `src/features/ingestion/adapters/rss.ts`
- [ ] `src/features/ingestion/adapters/github-releases.ts`
- [ ] `src/features/ingestion/adapters/official-api.ts`
- [ ] `src/features/ingestion/source-registry.ts`
- [ ] `src/features/ingestion/safe-fetch.ts`
- [ ] `src/features/ingestion/normalize.ts`
- [ ] `src/features/ingestion/canonical-url.ts`
- [ ] `src/features/ingestion/dedupe.ts`
- [ ] `src/features/ingestion/verify.ts`
- [ ] `src/features/ingestion/ingest.ts`

### News/editorial — 7 files
- [ ] `src/features/news/types.ts`
- [ ] `src/features/news/schema.ts`
- [ ] `src/features/news/repository.ts`
- [ ] `src/features/news/queries.ts`
- [ ] `src/features/news/approval.ts`
- [ ] `src/features/news/publication.ts`
- [ ] `src/features/news/risk-policy.ts`

### AI integration — 12 files
- [ ] `src/features/ai/providers/openai.ts`
- [ ] `src/features/ai/providers/anthropic.ts`
- [ ] `src/features/ai/providers/gemini.ts`
- [ ] `src/features/ai/providers/deepseek.ts`
- [ ] `src/features/ai/providers/xai.ts`
- [ ] `src/features/ai/model-registry.ts`
- [ ] `src/features/ai/router.ts`
- [ ] `src/features/ai/news-writer.ts`
- [ ] `src/features/ai/claim-grounding.ts`
- [ ] `src/features/ai/independent-reviewer.ts`
- [ ] `src/features/ai/prompts.ts`
- [ ] `src/features/ai/costs.ts`

### Auth, search, worker and libs — 15 files
- [ ] `src/features/auth/require-role.ts`
- [ ] `src/features/auth/session.ts`
- [ ] `src/features/search/fts.ts`
- [ ] `src/features/search/retrieve.ts`
- [ ] `src/features/search/answer.ts`
- [ ] `src/inngest/client.ts`
- [ ] `src/inngest/functions/daily-intelligence.ts`
- [ ] `src/inngest/functions/manual-run.ts`
- [ ] `src/lib/supabase/client.ts`
- [ ] `src/lib/supabase/server.ts`
- [ ] `src/lib/supabase/admin.ts`
- [ ] `src/lib/config.ts`
- [ ] `src/lib/logger.ts`
- [ ] `src/lib/time.ts`
- [ ] `src/lib/rate-limit.ts`

### SQL & data — 5 files
- [ ] `supabase/config.toml`
- [ ] `supabase/migrations/0001_core.sql`
- [ ] `supabase/migrations/0002_rls.sql`
- [ ] `supabase/migrations/0003_fts.sql`
- [ ] `supabase/seed.sql`

### Tests and evaluation — 15 files
- [ ] `tests/unit/canonical-url.test.ts`
- [ ] `tests/unit/lesson-schema.test.ts`
- [ ] `tests/unit/news-schema.test.ts`
- [ ] `tests/unit/risk-policy.test.ts`
- [ ] `tests/unit/news-dedupe.test.ts`
- [ ] `tests/integration/rls.test.ts`
- [ ] `tests/integration/authz.test.ts`
- [ ] `tests/integration/ingestion-replay.test.ts`
- [ ] `tests/integration/safe-fetch.test.ts`
- [ ] `tests/integration/publish-transaction.test.ts`
- [ ] `tests/e2e/public-navigation.spec.ts`
- [ ] `tests/e2e/editorial.spec.ts`
- [ ] `tests/evals/golden-news.json`
- [ ] `tests/evals/golden-rag.json`
- [ ] `tests/evals/run-news-eval.ts`

### Ops — 16 files
- [ ] `scripts/seed-lessons.ts`
- [ ] `scripts/verify-sources.ts`
- [ ] `scripts/smoke.ts`
- [ ] `scripts/audit-source-tree.py`
- [ ] `docs/PRD.md`
- [ ] `docs/ARCHITECTURE.md`
- [ ] `docs/DATA_MODEL.md`
- [ ] `docs/EDITORIAL_POLICY.md`
- [ ] `docs/SOURCE_POLICY.md`
- [ ] `docs/SECURITY.md`
- [ ] `docs/EVALUATION.md`
- [ ] `docs/TEST_PLAN.md`
- [ ] `docs/RUNBOOK.md`
- [ ] `docs/DEPLOYMENT.md`
- [ ] `docs/RELEASE_CHECKLIST.md`
- [ ] `docs/TRACEABILITY_MATRIX.md`

## Principles for no missing file
- Every required file must exist and be non-empty. A stub throwing `Not implemented` cannot pass functional acceptance.
- source root README documents all installation and env vars; `.env.example` has names only.
- database migrations are reviewable, additive and have RLS tests; no live creds needed for kit.
- six sample lesson Markdown documents in this kit are DRAFT and cannot count as published until edited, converted/imported into application and verified.
- include `package-lock.json` generated by package install; never invent lockfile hashes.
- all third-party SDK APIs must be verified against current official docs before coding.
- runtime, CI, RLS, network integrations and daily schedule must be empirically tested.
