# ADR-0002: single Inngest scheduled workflow

Status: ACCEPTED AS DESIGN. Decision: Inngest daily 07:00 Asia/Ho_Chi_Minh plus controlled manual trigger. No overlapping GitHub cron/Vercel cron schedule. Durable steps and DB idempotency for safe replay, logs and retries. Alternative: GitHub Actions scheduled, simpler but weaker per-step durability; Vercel Cron, trigger only. Revisit at usage/cost/operational constraints and API compatibility reviews.
