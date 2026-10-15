## NGÀY 07 — Product Design, PRD, sitemap, architecture & content seed

**Mục tiêu:** chốt spec có thể code; chuẩn bị đủ nội dung thật trước khi dựng UI.

**Lý thuyết (45 phút).** Information architecture khác software architecture. IA trả lời “người dùng học gì, tìm thế nào?”; software architecture trả lời “tài nguyên, security, costs, data flow, deploy ra sao?”. Nội dung evergreen phải có editorial revision; tin thời gian thực có `freshness` và source policy. ADR ghi quyết định và tradeoff; DoD định nghĩa thứ cần **quan sát được**.

**Prompt 07 — tạo tài liệu hoàn chỉnh trước khi code:**

```text
Using the 18-track knowledge map and daily-news spec,
author docs/PRD.md, ARCHITECTURE.md, DATA_MODEL.md, SOURCE_POLICY.md,
EDITORIAL_POLICY.md, TEST_PLAN.md, SECURITY.md and 3 ADRs.
Create sitemap and wireframes in plain markdown:
Home -> Tracks -> Lessons -> Source docs
Home -> Today -> Category -> News details -> Original source
Search -> Lessons/News; Admin -> Sources/Pending/Runs.
Seed exactly 6 fully written lessons:
1. AI vs LLM vs API, 2. Token/context/hallucination,
3. Choosing AI providers, 4. Prompt + JSON schema,
5. Claude Code plan→test, 6. Agents vs MCP vs RAG.
Each lesson has learning objectives, prereqs, clear theory,
Node/NestJS case, exercise + worked answer, quiz + answers,
official URLs, verified_at date and status DRAFT.
Do not fake citations or fabricate product features. Require my review.
```

**Lời giải bài mẫu — Lesson “Agent vs workflow”:** workflow cố định `fetch→normalize→dedupe→validate→publish review`; agent có thể đề xuất thay đổi thứ tự dựa theo tin, nhưng không vượt quyền publish; MCP là cách gắn tool chứ không phải “một AI thông minh hơn”; RAG là lấy bằng chứng. Bài tập: phân loại 4 hoạt động và chỉ ra tool nào cần human approval. Đáp án: read release = read-only; draft = AI operation; review = human editor; publish = server-authorized mutation. **Không cho agent tự gắn chữ Expert vào bài không qua nội dung kiểm chứng.**

**Go/No-Go ngày 7:** chưa có ít nhất 3 nguồn khả dụng/được phép hoặc chưa chứng minh editor gate thì scope news auto-publish phải chuyển sang draft-only. **DoD:** PRD pass review, 6 lesson drafts, data model và test plan có mọi đối tượng P0.

---
# TUẦN 2 — XÂY WEBSITE THẬT, DAILY INTELLIGENCE, DEPLOY

### BỔ SUNG V3 — GIAO BÀI THEO CHUẨN NGHIỆM THU

**Năng lực được kiểm chứng:** PRD, IA, architecture, data model, editorial policy, representative real learning content.

**Lý thuyết phải tự giải thích được:** MDX local content chỉ cho trusted authors; remote MDX không chạy trực tiếp.

**Bài thực hành bổ sung:** Review user journeys, sitemap, six lessons with source/quiz/answers.

**Đầu ra xác định:** PRD+Architecture+SQL review+6 full lessons+source registry. Từng artifact cần có owner, đường dẫn, trạng thái DRAFT/REVIEWED và liên kết với tiêu chí acceptance trong docs/TRACEABILITY_MATRIX.md.

**Negative testing:** No-Go nếu 3 sources chưa được phép hoặc editor gate thiếu.

**Chu trình học:** 30–50 phút đọc official docs → 20 phút tự diễn đạt lại nguyên lý → 90–120 phút giao prompt cho Claude Code → 30–60 phút kiểm chứng file/diff/log → ghi learning log và phản biện. Nếu service mới phát sinh tiền, cần bạn cho phép trước.

**Rubric ngày 07 (10 điểm; cần ≥9 và không có blocker):** lý thuyết 2; chất lượng prompt và phạm vi 2; đầu ra đúng schema/file 2; tests có bằng chứng 2; bảo mật/nguồn và đánh giá rủi ro 2. Nếu thiếu bằng chứng test: tối đa 6/10, không được tự báo PASS.

**DoD:** Kiểm tra đủ file, evidence, test và quyền hạn; blocker còn tồn tại thì status=FAIL hoặc SKIP.

**Self-check:** Nếu agent nói “đã làm xong”, yêu cầu nó trả: danh sách file tạo/sửa, test command và exit code, 3 rủi ro còn lại, ảnh/URL/log nếu có, lý do mọi bài test bị skip, và trạng thái chưa xác minh.
