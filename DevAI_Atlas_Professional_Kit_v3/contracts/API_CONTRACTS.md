# App HTTP APIs — request, authority, outcome

| Route | Method | Role | Input | Response | Failure |
|---|---|---|---|---|---|
| /api/news | GET | guest | pagination + category | published-only summary, cited URL | 400 invalid filter |
| /api/search | GET | guest | sanitized query+limit | approved lesson/news hits | 429 throttle |
| /api/ask | POST | authenticated or guest limited (P1) | question max length | cited answer or abstain | 429, 503, no draft leakage |
| /api/admin/run-now | POST | ADMIN | idempotency key | accepted run ID, not completed claim | 401/403/409, cost guard |
| /api/admin/review/[id] | POST | EDITOR/ADMIN | decision, reason, content revision/ETag | reviewed revision record | 403/409 stale revision |
| /api/inngest | provider serve endpoint | signed Inngest webhook (not public user trigger) | verified event | handler response | 401 invalid signature |
| /auth/callback | GET | auth flow | one-time code/state | validated session redirect | invalid code/state → safe error |

Every API must validate input schema, authorize before read/write, implement safe errors/no stack traces, cap size and rate, emit correlation ID, and test negative paths. Service role is server-only; no admin operation based solely on UI visibility. Canonical original URLs are content links only, never arbitrary fetch target.

## Publishing transaction
Given approved exact article revision hash, `publication` verifies editor identity and review decision, source license still valid, claim evidence populated, and executes transaction saving published version + editorial audit + revision update; search event/index step is idempotent. A double-click must not yield two versions. Any failure leaves draft safely unpublished.
