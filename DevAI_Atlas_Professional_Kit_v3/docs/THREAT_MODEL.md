# Threat model (STRIDE-lite + AI-specific)

| Threat | Entry | Asset | Defense | Evidence |
|---|---|---|---|---|
| Prompt injection | RSS/GitHub release body | secrets/publish rights | treat untrusted data; no model tool credentials | injection fixture prevents tool action |
| SSRF | source redirects/DNS | internal services | domain & IP allowlist across redirects | private IP blocked |
| XSS/MDX | malformed article | visitor session | sanitize/escape; trusted MDX only | test `<script>` inert |
| Role escalation | profile update/API payload | editorial rights | trusted role lookup, RLS | normal user cannot set admin |
| RLS bypass | server-side service key | drafts/private user data | privileged server-only narrowly scoped | guest cannot fetch drafts |
| News hallucination | writer model | published claims | claim-level evidence+editorial gate | fabricated model ID quarantined |
| Budget explosion | retry loops/ask endpoint | money/API quota | caps, budgets, alert, circuit breaker | 429 & quota tests |
| Copyright violation | source scraper | IP/compliance | ToS/licensing allowlist, metadata-only | disabled source no content |

Threat reviews must mention browser/server/worker/LLM trust boundaries and stop controls, not only prompt instructions.
