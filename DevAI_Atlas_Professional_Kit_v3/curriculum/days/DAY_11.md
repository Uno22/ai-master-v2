## NGÀY 11 — Multi-provider AI enrichment, fact-check, citations & editorial drafts

**Mục tiêu:** từ raw items đã được phép lấy dữ liệu, AI tạo **bài phân tích tiếng Việt có bằng chứng**, không tạo ra tin tự tưởng tượng.

**Lý thuyết (50 phút).** Model router dùng adapter + JSON schema + policy; không lấy model output làm quyền truy cập DB. Cần tách `source extraction` → `claim checking` → `draft generation` → `validation`. Multi-provider đem lại lựa chọn cost/quality nhưng fallback phải kiểm thử thực tế. Một model có thể là writer, model khác là critic; cả hai vẫn có thể cùng bịa nên **evidence link** quan trọng hơn đồng thuận. Prompt injection từ release body phải bị cô lập. Giá/latency tùy provider và thay đổi theo thời gian; log theo request thực.

**Prompt 11 — model routing + news enrich:**

```text
Implement an AI enrichment pipeline using Vercel AI SDK and server-only
provider adapters. Default writer provider configurable via env;
reviewer provider separately configurable (2 actual providers only
for MVP; DeepSeek/xAI as optional adapters when API tests pass).
Inputs: allowlisted source_items with title/URL/date and legally
retrievable excerpts; model MUST use only supplied evidence.
Output NewsDraft JSON schema: unique summary, what changed,
why developers care, affected SDK/API/workflows, action checklist,
claim->source citation mapping, uncertainty, risk level, category.
Prevent unsupported claims: validation fails if critical claim lacks
traceable source evidence. Classify pricing/deprecation/security/model
release as HIGH impact needing editor approval.
Use human-readable Vietnamese with links to original content;
do not reproduce a long source article.
Save DRAFT + AI usage/cost estimate + prompt/model/schema version.
Run evaluation on 10 seed items; show before/after editorial diffs.
```

**Đáp án mô phỏng bài đúng:**

> **Tiêu đề:** Bản phát hành SDK mới thay đổi cách gọi endpoint (ví dụ giả lập).  
> **Thay đổi:** API `operationOld` được đánh dấu deprecated — *chỉ viết khi có release note tương ứng*.  
> **Ảnh hưởng:** backend cần rà vị trí sử dụng endpoint và lịch sunset.  
> **Việc cần làm:** kiểm tra version hiện tại; test integration; lên lịch migration.  
> **Nguồn:** official changelog và GitHub release trong `post_sources`.  
> **Trạng thái:** `REVIEW_REQUIRED` nếu breaking/deprecation.

**Pass/Fail:** `claim_evidence` liên kết tới nguồn gốc cụ thể, link hợp lệ, không có giá/model ID ngoài evidence, reviewer đánh dấu vấn đề kiểm chứng được, tổng estimated cost có log. **Fail:** bài do AI viết “hãng vừa thông báo” dù không có chứng cứ chính thức.

**DoD:** 10 fixtures được đánh giá, 0 claim quan trọng unsupported trong các bài đủ điều kiện publish; dashboard hiện draft và nguồn; 2 providers thật gọi thành công bằng credentials lưu server (nếu API accounts khả dụng), nếu không thì đánh dấu adapter thứ hai chưa được nghiệm thu, không giả vờ đạt.

---

### BỔ SUNG V3 — GIAO BÀI THEO CHUẨN NGHIỆM THU

**Năng lực được kiểm chứng:** LLM draft→claim-level grounding→independent review→schema validation.

**Lý thuyết phải tự giải thích được:** Citation exists not imply substantiates; detect pricing/model/deprecation high risk.

**Bài thực hành bổ sung:** Three cases: official release, repost, rumour; quarantine rumour.

**Đầu ra xác định:** NewsDraft schema, evidence links, AI gateway and prompt versions. Từng artifact cần có owner, đường dẫn, trạng thái DRAFT/REVIEWED và liên kết với tiêu chí acceptance trong docs/TRACEABILITY_MATRIX.md.

**Negative testing:** Independent reviewer detects unsupported numeric assertion.

**Chu trình học:** 30–50 phút đọc official docs → 20 phút tự diễn đạt lại nguyên lý → 90–120 phút giao prompt cho Claude Code → 30–60 phút kiểm chứng file/diff/log → ghi learning log và phản biện. Nếu service mới phát sinh tiền, cần bạn cho phép trước.

**Rubric ngày 11 (10 điểm; cần ≥9 và không có blocker):** lý thuyết 2; chất lượng prompt và phạm vi 2; đầu ra đúng schema/file 2; tests có bằng chứng 2; bảo mật/nguồn và đánh giá rủi ro 2. Nếu thiếu bằng chứng test: tối đa 6/10, không được tự báo PASS.

**DoD:** Kiểm tra đủ file, evidence, test và quyền hạn; blocker còn tồn tại thì status=FAIL hoặc SKIP.

**Self-check:** Nếu agent nói “đã làm xong”, yêu cầu nó trả: danh sách file tạo/sửa, test command và exit code, 3 rủi ro còn lại, ảnh/URL/log nếu có, lý do mọi bài test bị skip, và trạng thái chưa xác minh.
