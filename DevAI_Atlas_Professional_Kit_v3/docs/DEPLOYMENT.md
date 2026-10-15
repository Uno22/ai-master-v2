# Deployment playbook — Vercel + Supabase + Inngest

1. GitHub repository & least privilege branch protection. Separate staging and prod project credentials and database.
2. Provision Supabase, review migrations locally; apply to staging, test auth/RLS/constraints; approve production migration with backup/restore plan.
3. Deploy Next.js to staging Vercel; configure only server runtime env keys where appropriate (never `NEXT_PUBLIC_*` for secrets); ensure domain/HTTPS and security headers.
4. Connect Inngest endpoint, confirm registered functions; choose ONE scheduler `TZ=Asia/Ho_Chi_Minh 0 7 * * *`; test manual Run now against live allowed sources; monitor runs.
5. Wire provider API keys, quota/cost caps; verify model IDs and support from official docs; make worker draft-only by default.
6. Test independent roles (guest/user/editor/admin), 18 tracks, six reviewed lessons, news, source URLs, metadata/SEO, search, 429 retry, no duplicate, no prompt injection.
7. CI build/test/security audit must pass; final approval then production deploy; run public smoke; document URL, timestamp, commit, owner, known issues.
8. After next *real* scheduled 07:00 execution, record run ID to close UAT-15; until then `PENDING_SCHEDULED_PROOF`.

Setup guide is not proof of production. Requires user's actual account actions and keys.
