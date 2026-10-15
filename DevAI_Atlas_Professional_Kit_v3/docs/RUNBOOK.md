# Operator runbook (to implement + verify)

## Daily before 07:00 VN
Check source permissions/availability, DB health, Inngest sync, publish queue, secret validity, budgets and incident banners. A scheduled config without observed run is `PENDING_SCHEDULED_PROOF`.

## No news today
Distinguish zero eligible items from fetch outage. Empty verified day shows “Không có cập nhật đã kiểm chứng”, but if all adapters failed show “Nguồn tạm gián đoạn”, not a fabricated report.

## Job failed
Capture run ID, step, safe logs and service status; pause high-risk publishing, retry only failed steps with same idempotency key, verify counts, alert admin. On 429 use Retry-After; source disabled after repeated policy/reliability failures. Preserve original metadata.

## Wrong published article
Unpublish/retract via admin, delete cache/search index, log correction, notify if substantial misinformation; verify approvals/revision/source and add gold eval fixture.

## Security incident
Disable Run Now/high-risk integration, revoke affected credentials, rotate tokens, close privileged source, inspect audit, roll back and notify stakeholders as legally required. Do not feed raw secrets to LLM.

## Rollback
Use last known working deployment/DB migration rollback plan; backup before irreversible migration, maintain feature flags for AI and news publish; don't assume SQL `DROP TABLE` reversible. Validate public pages and scheduled run after restoring.
