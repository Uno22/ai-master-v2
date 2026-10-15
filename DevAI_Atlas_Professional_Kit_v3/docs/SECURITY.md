# Security baseline (deployment blocker list)

- Identity: Supabase SSR session verified server-side; cannot rely on client role flag, URL or cookies as authority; admin roles only trusted server/DB path.
- Data: RLS all user-owned/post draft tables; deny by default; service_role/secret keys exclusively trusted backend functions with minimal surface. Tests as guest/user/editor/admin.
- LLM: external texts untrusted; tool calls validated backend, no sensitive files/secrets, no direct model write/publish, no tool outputs used as new instructions. Prompt injection fixture included.
- Ingestion SSRF: only pre-registered official host and fixed endpoints; block private IP/loopback/metadata and redirects to them, DNS rebinding checks; enforce timeout/size/decompression limits, content types, max items, API budgets.
- XSS: no unsanitized article HTML/markdown JSX; HTML escaping; remote MDX forbidden. Sanitize URLs, external links with rel noopener; CSP when production.
- Authn/authz: CSRF review for cookie-auth mutations, brute force protection, no self-service admin role, auditable editor actions, secure logout and session expiry.
- Secrets: never committed/test fixtures; GitHub secret scan and env validation, rotate leaked keys, least privilege tokens; no PII in traces.
- Supply chain: lockfile, pinned CI actions versions, dependency audit, SCA and package allowlist, permissions minimal.
- Abuse: rate limits for search/ask/run-now, quotas, cost caps, provider backoff, prevent unbounded tool loops.
- Privacy/IP: collect minimal personal data, retention policy, deletion workflow, right to index/embedding, licensed sources only.
- Incident: disable scheduler & API, quarantine dubious articles, rollback previous deploy, rotate keys, export sanitized logs and notify affected users when required.

Security check must show both positive and negative tests; checking only that UI hides /admin is not sufficient.
