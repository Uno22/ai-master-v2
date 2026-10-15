## NGÀY 04 — Claude Code thực chiến: PLAN → IMPLEMENT → VERIFY

**Mục tiêu:** điều khiển coding agent chuyên nghiệp để dựng repo, không viết từng dòng code.

**Lý thuyết (35 phút).** Coding agent có khả năng đọc/sửa file/chạy command tùy quyền được cấp; vì vậy thao tác shell, secret, file deletion, production deploy đều cần ranh giới. Workflow tốt: đọc repo → plan chia nhỏ → approve → implement → test → inspect diff → commit. `CLAUDE.md` lưu project rules; Git giữ lịch sử. Tool output không phải bằng chứng nếu bạn chưa thấy CI/website hoạt động.

**Thực hành:** cài theo docs chính thức Claude Code phù hợp OS, kiểm tra Git/Node, tạo repo **`devai-atlas`** và cho agent scaffold. Không thêm API key vào `.env.example` dưới dạng giá trị thật.

**Prompt 04 — master bootstrap:**

```text
You are the implementation agent for DevAI Atlas.
First inspect current directory and available tools. DO NOT write source yet.
Create a PLAN with phases, file tree, dependencies, risks, deployment workflow
and exact tests. Our architecture: Next.js App Router + TypeScript,
versioned MDX lessons + Supabase PostgreSQL/Auth + Inngest scheduled news
pipeline + Vercel AI SDK multi-provider adapters + Vercel deployment.
Guest can read public content; admin controls sources/editorial queue.
Rules: no secrets in repo; no destructive migration; no auto-deploy;
no paid-service actions or external publishes without my approval.
After I approve, scaffold minimum repo, README, .env.example,
CLAUDE.md, .gitignore, tests placeholders and CI pipeline.
Show every changed file, commands, exit codes, and next review checkpoint.
```

**Lời giải kiểm tra:** `git status` không chứa `.env`; `npm run build`/typecheck (hoặc scripts thực tế) pass; README đủ local setup; file tree đúng phân tách content/news/ingestion. Coding agent phải hỏi permission cho shell/network theo môi trường. **Fail:** agent tự tạo production resource/tự commit credentials/tự đưa pipeline lên lịch ngay khi chưa được duyệt.

**Artifacts:** `CLAUDE.md`, `README.md`, `.github/workflows/ci.yml`, khung thư mục ở PHẦN I, log test đầu tiên. **Quiz:** “Review diff để làm gì khi AI viết code?” — *Phát hiện hành động ngoài scope, code yếu, secret và regression trước khi merge*.

---

### BỔ SUNG V3 — GIAO BÀI THEO CHUẨN NGHIỆM THU

**Năng lực được kiểm chứng:** Plan→approve→implement→verify→review; quản lý agent permissions và an toàn khi viết code.

**Lý thuyết phải tự giải thích được:** Agent tự sửa file không đồng nghĩa test pass. Check diff, shell permission, env, no auto production.

**Bài thực hành bổ sung:** Lập plan trước khi tạo source, CI chạy build/test, diff review.

**Đầu ra xác định:** Repository skeleton, CLAUDE.md, CI, README, agent review log. Từng artifact cần có owner, đường dẫn, trạng thái DRAFT/REVIEWED và liên kết với tiêu chí acceptance trong docs/TRACEABILITY_MATRIX.md.

**Negative testing:** Fail nếu commit secret, hay chi phí phát sinh khi chưa được phép.

**Chu trình học:** 30–50 phút đọc official docs → 20 phút tự diễn đạt lại nguyên lý → 90–120 phút giao prompt cho Claude Code → 30–60 phút kiểm chứng file/diff/log → ghi learning log và phản biện. Nếu service mới phát sinh tiền, cần bạn cho phép trước.

**Rubric ngày 04 (10 điểm; cần ≥9 và không có blocker):** lý thuyết 2; chất lượng prompt và phạm vi 2; đầu ra đúng schema/file 2; tests có bằng chứng 2; bảo mật/nguồn và đánh giá rủi ro 2. Nếu thiếu bằng chứng test: tối đa 6/10, không được tự báo PASS.

**DoD:** Kiểm tra đủ file, evidence, test và quyền hạn; blocker còn tồn tại thì status=FAIL hoặc SKIP.

**Self-check:** Nếu agent nói “đã làm xong”, yêu cầu nó trả: danh sách file tạo/sửa, test command và exit code, 3 rủi ro còn lại, ảnh/URL/log nếu có, lý do mọi bài test bị skip, và trạng thái chưa xác minh.
