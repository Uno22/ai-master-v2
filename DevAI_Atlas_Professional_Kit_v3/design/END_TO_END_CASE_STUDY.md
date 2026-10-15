# Worked capstone — a release becomes a verifiable digest (synthetic scenario)

**The following is fictional fixture data.** Do not show as real AI news. Scenario: GitHub repo's published release metadata appears at `https://example.org/devai-demo/v2`, with API method removal. This domain is only a mock stand-in.

## 1. Request
“As a backend leader, I want to know what changed today, if it breaks existing integrations, what PRD/ticket to create, and to read a Vietnamese summary with original references.” Acceptance: one article per distinct event; no high-risk autopublish; dates, link, code impact and action items; editor review.

## 2. Sources
Source registry record: `{id: github-official-example, tier: A, adapter: github-releases, allowed_hosts: [api.github.com], usage_policy: metadata-only}`. In reality verify repo owner and license, releases API and rate limits.

## 3. Fetched input
`{ guid: release/123, canonical: https://example.org/devai-demo/v2, source_published_at: 2026-10-15T12:00Z, discovered_at: 2026-10-16T00:00Z, title: v2 deprecates method A }`.

## 4. Normalize + dedupe
Track canonical release URL and GUID. Re-run same payload must increment duplicate_count without writing another `source_items` row. Two publishers same event form one news cluster but evidence items retained separately.

## 5. Claim extraction
`C1: method A is deprecated` → evidence release text/link; `C2: all Node apps must migrate immediately` → unsupported inference until migration guide. C2 is dropped or labeled conditional, not fact.

## 6. Draft writer
Vietnamese title: `[DEMO] Có thay đổi ở API phiên bản v2`; summary explains test case, not actual event. Developer impact includes affected user criteria; action: check SDK integration tests; source and published date displayed.

## 7. Validate
Schema NewsDraft valid, but C2 fails grounding; `risk_level=HIGH`, `review_required=true`, `status=DRAFT`. Even two models agree, reviewer approval still mandatory.

## 8. Publish process
Editor logs in, sees original link/date, diff, C1/C2; requests correction, re-generates and reruns evidence validator; approves immutable revision; backend checks role and atomically saves published article+audit; search index updates only then.

## 9. Daily job & failure
Cron executes by schedule, run stores counts. One source 429 → bounded Retry-After; other sources proceed; partial run logs; manual replay same run idempotently. Zero quality-eligible articles → do not write fake filler.

## 10. User experience
Guest reads `/news/[slug]`, sees publisher and evidence, title and verified_at; `/ask` answers “What changed?” from approved content only; if no source or draft-only, assistant abstains.

## 11. How to test without coding yourself
Give `prompts/daily/DAY_10.md` (ingest) → reviewer checks terminal actual output; `DAY_11` (claim) → inject fake claim and see quarantine; `DAY_12` (schedule) → manual replay; `DAY_14` → staging QA with real URLs and test accounts.

## 12. Completion evidence
File diffs, CI commands exit 0, source registry permissions, DB unique index and RLS test, redacted run log/ID, published article link after explicit approval, scheduled first execution observed. Screenshot or AI statement alone is insufficient.
