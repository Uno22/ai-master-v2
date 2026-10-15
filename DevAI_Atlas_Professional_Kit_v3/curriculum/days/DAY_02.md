## NGÀY 02 — Prompt & Context Engineering, JSON schema, prompt testing

**Mục tiêu:** biến prompt mơ hồ thành hợp đồng có input/output/test để giao agent làm tin tức và lesson.

**Lý thuyết (40 phút).** Cấu trúc prompt tốt: role, purpose, context, source constraints, input data, process constraints, output schema, failure mode, acceptance tests. `Structured Outputs` nhằm ràng buộc cấu trúc; valid JSON **không đồng nghĩa** nội dung đúng. Input bên ngoài cần đối xử như dữ liệu không tin cậy. Few-shot hữu ích khi đưa cả ví dụ pass/fail. Version prompt để chạy regression và so sánh model.

**Case:** Một official release note có cập nhật API breaking change. Bạn cần một bài ngắn bằng tiếng Việt, có đường link gốc, tác động developer và không suy diễn.

**Prompt 02 — tạo JSON schema và 3 fixtures:**

```text
Bạn là AI content architect của DevAI Atlas.
Thiết kế 2 JSON Schemas có version:
A. Lesson: slug, title, track, level, objectives, prerequisites,
   explanation, realistic_example, exercise, sample_solution,
   quiz, source_urls[], verified_at, status.
B. NewsDraft: canonical_source_url, source_published_at, discovered_at,
   claim_evidence[], title_vi, summary_vi, what_changed,
   developer_impact, action_items[], uncertainty[],
   category, risk_level, review_required, status.
Quy tắc: mỗi claim trọng yếu phải map tới source URL; không đủ bằng chứng
thì confidence LOW và review_required=true. Không lấy link tự tưởng tượng.
Tạo 3 fixtures: official release; trùng nguồn đổi URL query; tin đồn chưa xác minh.
Cho đáp án PASS/FAIL và test scenarios để Claude Code tự implement.
```

**Đáp án mẫu rút gọn cho tin đồn:**

```json
{
  "title_vi": "Chưa xác minh: thông tin lan truyền về model mới",
  "canonical_source_url": "https://example.org/unverified-demo",
  "claim_evidence": [],
  "uncertainty": ["Chưa tìm thấy công bố từ provider"],
  "category": "Models",
  "risk_level": "HIGH",
  "review_required": true,
  "status": "DRAFT"
}
```

> URL `example.org` ở trên là **fixture giả**, chỉ dùng cho test, không được đăng thành tin thật. Đây là ví dụ output; fields bắt buộc bổ sung timestamp và schema version khi hiện thực.

**Bài kiểm tra:** JSON thiếu `canonical_source_url` → schema fail; có link nhưng claim không chứng minh được → grounding fail; duplicate URL có `utm_*` → dedupe; press rumor → không auto publish.

**Sản phẩm:** `docs/PROMPT_CONTRACTS.md`, `docs/EDITORIAL_POLICY.md` nháp, `tests/fixtures/{official-release,duplicate-url,rumor}.json` do AI tạo.

---

### BỔ SUNG V3 — GIAO BÀI THEO CHUẨN NGHIỆM THU

**Năng lực được kiểm chứng:** Xây prompt contract, structured outputs và regression fixtures; ngôn ngữ prompt không thay thế backend authorization.

**Lý thuyết phải tự giải thích được:** Có output schema chưa chứng minh sự thật. Phân biệt system instructions, untrusted source, retrieval context.

**Bài thực hành bổ sung:** 1 prompt vague→structured, 3 fixtures và eval rubric.

**Đầu ra xác định:** JSON schema Lesson / NewsDraft và 3 fixtures. Từng artifact cần có owner, đường dẫn, trạng thái DRAFT/REVIEWED và liên kết với tiêu chí acceptance trong docs/TRACEABILITY_MATRIX.md.

**Negative testing:** Tạo lỗi schema, grounding, nguồn bịa; ghi expected FAIL.

**Chu trình học:** 30–50 phút đọc official docs → 20 phút tự diễn đạt lại nguyên lý → 90–120 phút giao prompt cho Claude Code → 30–60 phút kiểm chứng file/diff/log → ghi learning log và phản biện. Nếu service mới phát sinh tiền, cần bạn cho phép trước.

**Rubric ngày 02 (10 điểm; cần ≥9 và không có blocker):** lý thuyết 2; chất lượng prompt và phạm vi 2; đầu ra đúng schema/file 2; tests có bằng chứng 2; bảo mật/nguồn và đánh giá rủi ro 2. Nếu thiếu bằng chứng test: tối đa 6/10, không được tự báo PASS.

**DoD:** Kiểm tra đủ file, evidence, test và quyền hạn; blocker còn tồn tại thì status=FAIL hoặc SKIP.

**Self-check:** Nếu agent nói “đã làm xong”, yêu cầu nó trả: danh sách file tạo/sửa, test command và exit code, 3 rủi ro còn lại, ảnh/URL/log nếu có, lý do mọi bài test bị skip, và trạng thái chưa xác minh.
