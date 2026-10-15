# Risk register

| Risk | Likelihood | Severity | Mitigation | Stop condition |
|---|---|---|---|---|
| Generated fake news/claims | High | Critical | claim-to-evidence gates, review | unresolved critical claim |
| Copyright / forbidden source | Medium | Critical | permission registry, metadata-only | license unreviewed |
| RSS prompt injection | High | Critical | untrusted boundaries & no publish tool | tool misuse or secret access |
| Admin privilege escalation | Medium | Critical | server auth/RLS negative tests | guest read drafts |
| 2 parallel schedules | Medium | High | one scheduler + idempotency lock | duplicate publication |
| Excessive AI spend | Medium | High | budget guard and token caps | no hard cap |
| Provider API version change | High | Medium | capability checks+pin+regressions | undocumented endpoint usage |
| 14-day scope overflow | High | High | P0/P1/P2 and six lessons | six lessons non-reviewed |
| Unproven scaling claim | Medium | High | stage load measurements | unsupported QPS/SLO claims |
| Scheduled execution not observed | High | Medium | pending schedule proof; run next day | unverified “daily” claim |
