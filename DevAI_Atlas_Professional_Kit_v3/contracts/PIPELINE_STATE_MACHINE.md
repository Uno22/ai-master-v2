# Daily intelligence workflow state machine

SOURCE_UNCHECKED → FETCHED → NORMALIZED → VERIFIED/NEEDS_REVIEW → DRAFTED → GROUNDED → IN_REVIEW → APPROVED → PUBLISHED

Exceptional transitions: any unlicensed/untrusted/stale/unsupported object → QUARANTINED; invalid parsed item → REJECTED; any step failure → FAILED_RETRYABLE if bounded and non-unsafe; older approved revision changed → IN_REVIEW.

**Formal invariants**
- For every `source_id/external_id` only one source_item row regardless of retries.
- For every `news_cluster_id` and event version only one published active canonical post.
- No HIGH-risk post without valid editor approval and exact content revision.
- At publish all citations resolve to retained source items and comply with policy.
- No public news row exposes an unpublished draft even if frontend misroutes.
- A completed scheduled job may yield 0 posts; zero is not failure if sources actually scanned.
- Partial source outage logged as PARTIAL, not “no news today”.

**Failure/retry matrix**: network timeout retry bounded; HTTP 429 follow Retry-After; 404 page disabled/metadata mismatch review; invalid schema quarantine; LLM provider outage fallback only if capability tested; DB conflict idempotent; script dangerous instruction in source always data-only.
