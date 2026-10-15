# Dependencies and correct build order (AI agent must honor)

1. Docs, constraints, source policy, schema and golden fixtures — before code.
2. Repo/bootstrap tools and CSS/components — before public pages.
3. Learning content parser + trusted lessons — before learning navigation/SEO.
4. Schema migrations, auth & RLS — before any editorial admin endpoints.
5. Source registry/safe fetch/normalize/dedupe — before AI writer; no network beyond allowlist.
6. AI adapter, cost registry, schema validation, citation grounding — before enabling draft writer.
7. Editorial approval/immutable content revisions — before publishing.
8. Scheduler jobs + manual run and logs — after idempotency and DB state are tested.
9. Search approved only, optional RAG after gold evaluation — after publication reads.
10. CI, UAT, security/load checks — before staging/prod sign-off; observe scheduled job after production deployment.

No skipped dependency: e.g. cannot implement automatic publish before admin RLS and evidence checker.
