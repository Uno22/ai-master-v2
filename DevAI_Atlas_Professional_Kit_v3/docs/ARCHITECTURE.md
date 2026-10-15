# Architecture — v1 bounded modular monolith

## Components
Next.js App Router public SSR/static for lessons/news/search; trusted Markdown/MDX commit-reviewed in Git; Supabase Postgres for dynamic news/users/workflow; Inngest durable scheduled job; server-only AI provider adapters; no browser API keys; search Postgres FTS baseline, optional pgvector after eval; GitHub Actions CI; Vercel hosting.

## Data flow
1. Cron event obtains run fingerprint(day,job version); DB unique lock prevents concurrent duplicate.
2. Source registry allowlist → read-only fetch adapters → normalize with source ID/published_at/canonical URL → idempotent source upsert.
3. Cluster and rank; draft writer consumes text as untrusted data; backend validates schema+evidence; insert draft and queue.
4. Editor reviews high-impact item with source diff and claim checks. Mutation executed by authorized app role; publishes atomically; writes audit.
5. Search indexes only published text with version pointer; browser reads published only.

## Module ownership
`src/app`: presentation and thin authenticated endpoints; `src/features/learning`: trusted content parse; `src/features/news`: publication state machine; `src/features/ingestion`: adapters and dedupe; `src/features/ai`: model routing and checks; `src/features/auth`: admin enforcement; `src/features/search`: FTS/RAG; `src/inngest`: orchestration; `src/lib`: shared typed config/time/logger.

## Rules
No MCP or LLM tool is granted direct publishing or unrestricted DB writes. SSRF protection: static allowlist per source, HTTPS preferred, DNS/IP resolution checks, prohibit private/loopback/link-local/metadata targets, revalidate every redirect, size/time limits. Do not render raw remote MDX or HTML; encode source text and sanitize. Authorization before queries; RLS is defense-in-depth, not permission granted by UI. Secrets never serialized to client. Persist evidence lineage, import source with retention/rights.

## Failure containment
One source error never blocks others; provider timeout yields review-required draft or failure, not fabricated story. Retry bounded with exponential backoff; handle 429 Retry-After; DLQ/manual retry; run records state partial/failed/success. Concurrent runs protected with database lock and unique indexes; no 2 schedulers. Circuit breaker and daily budget protect from cost spikes. Logs omit secrets and personal details.

## Decision tradeoffs
MDX for editor-reviewed lessons (git/version/review), DB for frequently changing news; FTS before hybrid RAG (fast, cheap, testable); full microservices deferred until measured scale justifies it; Inngest as one scheduler to avoid duplicate trigger. Observability of official release vs time discovered is necessary for provenance.
