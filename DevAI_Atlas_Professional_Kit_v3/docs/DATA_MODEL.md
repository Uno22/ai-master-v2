# Data model and invariants

`news_sources`: allowed RSS/API adapters, tier, endpoint, usage policy, status, updatedAt.
`source_items`: original source GUID, canonical_url, publish/discover times, content hash; UNIQUE(source_id, external_id), UNIQUE(canonical_url) as appropriate; canonicalization must not merge distinct release announcements.
`news_clusters` / `cluster_members`: group related items, do not delete original evidence; n:n relation with keyed IDs.
`news_posts`: slug, title, verified_at, risk, status, revision, main_content, writer model/prompt version; status transition only by server. `post_sources`: individual evidence link to claim_id and source_item ID.
`editorial_reviews`: reviewer actor and decision/reason/version; no editor approval without verified session; article approved must not change silently after approval.
`ingestion_runs`: run_key UNIQUE, started_at, completed_at, source/status counts, reason, cost, partial errors.
`profiles`: account_id derived from auth.users, role granted only via privileged administrative workflow, row ownership.
`reading_progress/bookmarks`: owner-only RLS; guest not required for public content.
`ai_usage/audit_log`: append-only backend-only, scrub request secrets.
`lessons_index`: slug, content repo commit/revision, status, verified_at; only reviewed lessons shown to users.
`knowledge_chunks` (P1): approved-only content + revision pointer + source link and rights policy.

## Invariants
Canonical source URL and GUID unique; external content cannot drive SQL identifiers; published post includes editor audit if high-risk; review only applies to exact revision/hash; no publishing after source revoked; source times UTC ISO8601, display by reader locale. Soft delete/retention for legal requests; do not delete evidence just because near-duplicate cluster. Atomic publish ensures no post without evidence. On update, re-review if material content changed.

## Transaction state transitions
DISCOVERED→NORMALIZED→VERIFIED→DRAFT→IN_REVIEW→APPROVED→PUBLISHED; any state may move to QUARANTINED after detection of source/rights error; REJECTED immutable without new revision. Daily completion distinct from publication count.
