# NGÀY 04 — CLAUDE CODE & GIT OPERATIONS

**Copy toàn bộ khối prompt bên dưới vào Claude Code** (sau khi đã đọc `prompts/00_MASTER_SYSTEM_PROMPT.md`). Đây là PROMPT GIAO VIỆC, không phải bài học thay thế.

## A. Input cần cung cấp
- Repository: `devai-atlas`, branch feature tương ứng ngày 04; current git status và app version.
- References: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/TRACEABILITY_MATRIX.md`, ngày 04 trong curriculum.
- Official documentation: `docs/OFFICIAL_SOURCES.md`; tra lại docs khi tính năng/version có thể thay đổi.
- Không có credentials production là bình thường: chạy local fixtures, report SKIPPED cho integration live.

## B. Prompt thực thi đầy đủ

```text
You are the DevAI Atlas phase-04 implementing agent.
Goal: Plan→approve→implement→verify→review; quản lý agent permissions và an toàn khi viết code.
Background: AI-first education + daily AI intelligence project for developers;
user is technical leader and will not write code by hand.
Expected output: Repository skeleton, CLAUDE.md, CI, README, agent review log

Scope and file contract:
- First inspect repo, versioned docs, current branch, conflicts, installed libs.
- Target artifacts (do not create fake empty placeholders): CLAUDE.md, README.md, .github/workflows/ci.yml, .env.example, package.json.
- If paths don't exist, propose in PLAN. If existing paths conflict, STOP and ask.
- Never rewrite unrelated files, secrets, content previously approved without a diff.

Theory verification requirements:
Agent tự sửa file không đồng nghĩa test pass. Check diff, shell permission, env, no auto production.

Implementation exercise:
Lập plan trước khi tạo source, CI chạy build/test, diff review.

Process:
1. Before touching files, provide PLAN with file-by-file add/modify list,
   dependency impacts, exact commands/tests and realistic failure conditions.
2. Wait for explicit approval. Implement in isolated slices.
3. After each slice run typecheck/lint/test/build as relevant and record real exit codes.
4. Create/adjust unit tests, negative tests, authorization and source integrity tests.
5. Review diff; write acceptance evidence by criterion ID.
6. Report remaining uncertainty and operational/monetary costs; no fabricated success.

Failure condition / hard blocker to check: Fail nếu commit secret, hay chi phí phát sinh khi chưa được phép.
Never deploy, publish externally, edit production database, or incur charges without explicit consent.
Stop conditions: missing source licensing, unavailable keys for live tests,
failing security tests, unverified API features, or destructive schema changes.

Final answer must include sections: FILES | DIFF SUMMARY | TEST COMMANDS & CODES |
ACCEPTANCE EVIDENCE | SOURCE VERIFICATION | RISKS | SKIPPED | NEXT APPROVAL.
```

## C. Mẫu lời giải / Expected output

Agent tự sửa file không đồng nghĩa test pass. Check diff, shell permission, env, no auto production.

**Bằng chứng cần thấy:** Lập plan trước khi tạo source, CI chạy build/test, diff review..

**Trường hợp phải FAIL hoặc SKIP:** Fail nếu commit secret, hay chi phí phát sinh khi chưa được phép.

## D. Rubric chấm bằng chứng (10 điểm)

| Hạng mục | Điểm tối đa | Điều kiện nhận đủ |
|---|---:|---|
| Scope + plan đúng | 2 | Có file-by-file plan, không sửa file ngoài scope |
| Kiến thức + source | 2 | Dẫn docs đúng, không claim thiếu nguồn |
| Artifacts | 2 | Các đường dẫn trong hợp đồng được tạo hoặc ghi rõ BLOCKED |
| Kiểm thử | 2 | Commands/exit codes thật; negative tests có expected result |
| Security + vận hành | 2 | Không leak secret; không bypass approval; có risk log |

**DoD:** ≥9/10, không còn critical blocker, và evidence pack đầy đủ. Không tự ghi 10/10 cho runtime khi chưa chạy thật.
