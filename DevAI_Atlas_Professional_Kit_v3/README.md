# DevAI Atlas — Professional AI Learning + Daily Intelligence Implementation Kit v3

**Start here:** `curriculum/AI_First_14_Day_AI_Developer_Knowledge_Hub_V3.md` or `curriculum/INDEX.md` → `prompts/00_MASTER_SYSTEM_PROMPT.md` → `prompts/daily/DAY_01.md`.

## What you receive
- 14 complete day plans, 14 production-minded Claude Code task prompts and 8 specialized reviewer prompts;
- 18 tracks / 144 module **syllabus**, 6 complete illustrative draft lessons (not all verified as publish-ready);
- Product/architecture/security/editorial/automation/LLMOps docs, 3 schemas, synthetic fixtures and audit scripts;
- file-by-file source implementation checklist for **144 P0 MVP files + 13 P1 optional files = 157 total**; a real Next.js app is **not yet built**.

## How to use without writing code by hand
Open the kit in Claude Code (or copy docs into a new repo). Give the master prompt, then a day prompt. Review the PLAN. Approve only scoped changes. Ask agent to run tests, show real outputs and diff; check acceptance gate. Repeat daily. Do not pass production keys via chat.

## Verify the kit
`python tests/validate_kit.py` (requires `PyYAML` and `jsonschema`) runs static completeness checks; it does not validate Next.js deployment. When Claude Code has implemented the application, execute `python project/audit_source_tree.py /path/to/devai-atlas` plus CI/UAT; missing source files result in error.

## Reality boundaries
- This ZIP is a **curriculum+specification+agent kit**, not a deployable production site.
- 14 days target a quality MVP: 6 reviewed lessons and reliable daily news workflow. 144 full lessons take continued writing/review after launch.
- No real API keys, provider charges or production deploy included.

## References
See `docs/OFFICIAL_SOURCES.md` for source documentation. Reverify fast-changing SDK capabilities, model IDs and pricing at actual implementation time.
