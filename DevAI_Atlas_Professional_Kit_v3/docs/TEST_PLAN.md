# Risk-based test plan

Unit: schema validation, URL canonicalization, dedupe keys, tier/source rank, risk classification, transitions, lesson metadata, access matrix. Integration: DB RLS, authenticated edit, source failure/retry, 3 adapters fetch (respect ToS), idempotency after crash, enqueue/approve/publish, budget and 429. E2E: user learn→quiz, search→source, editor draft→approve, guest denied admin; mobile + keyboard.

AI eval: golden fake claims/release dates/low-evidence rumors/injections. Security: SSRF (localhost, private IP, redirect, DNS rebind), XSS (encoded and raw), CSRF, role escalation, service secret not browser, RLS. Performance: p95, rate limiting, CDN cache, N+1, request cost with realistic measured load. Recovery: replay after partial write, two concurrent triggers, provider outage and disabled source.

A TEST is PASS only with executed command, environment, exit code, trace/screenshot/URL, tested commit hash and timestamp. Test SKIP because no credentials is not PASS. All blocker tests must pass before production.
