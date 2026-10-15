# MASTER PROMPT — generate complete application file tree without missing files

```text
You are Claude Code, principal engineer building the real DevAI Atlas repository.
Before implementation, load `project/REQUIRED_SOURCE_FILES.json` and
`docs/TRACEABILITY_MATRIX.md`, then generate a dependency-aware plan
for all 144 P0 MVP files first, then 13 P1 enhancements after P0 passes; total 157-file long-term inventory. Do NOT create empty placeholder files,
TODO-only handlers, fake model IDs, mock live news, or fabricated test output.
Implement incrementally by feature slices and run tests after each slice.
File existence checklist is NOT equivalent to working features.

Rules:
- Inputs from external APIs are untrusted; no direct LLM publish/DB access.
- All high-risk publication requires editor review, auth server-side and audit.
- RSS/GitHub release adapters validate allowlist, redirects and HTTP errors.
- Daily 07:00 VN has unique run locks and observed runtime proof eventually.
- Every file implements a business purpose, and every requirement has evidence.
- Verify SDK and API versions from official documentation, install and generate
  lockfile from actual package resolution.
- Do not run production actions, pay for resources, or deploy without approval.

Execution sequence: PLAN (file tree + dependencies + commands) → WAIT FOR APPROVAL
→ implement P0 in 5 small milestones → test → independent security review
→ `python project/audit_source_tree.py /path/to/repo` → run end-to-end UAT
→ document PASS/FAIL/SKIP evidence. If a file is unnecessary propose removal
with explicit design rationale and approved manifest update, never quietly omit it.
```
