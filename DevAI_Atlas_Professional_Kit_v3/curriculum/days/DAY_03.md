## NGÀY 03 — Ứng dụng AI cho Technical Leader, fact-check và editorial judgement

**Mục tiêu:** biến AI thành analyst/reviewer chứ không phải người quyết định thay leader.

**Lý thuyết (40 phút).** Với feature, leader cần scope, assumptions, unknowns, acceptance criteria, dependency, risk, owner, timeline. Với content, editor cần phân biệt **sự kiện** (đã xác minh), **phân tích/tác động** (suy luận có cơ sở), **ý kiến** (đánh dấu chủ quan) và **tin chưa xác nhận**. Ai dẫn nguồn không kiểm tra được thì không được phê duyệt.

**Case:** Stakeholder nói: “Làm website có tất cả kiến thức AI, update mọi tin tức, đẹp như top công nghệ, deploy sau 14 ngày.” Đây là yêu cầu không thể đo vì “tất cả”, “mọi”, “đẹp” không có ngưỡng.

**Prompt 03 — AI làm BA + solution architect:**

```text
Act as Product Analyst + Technical Lead. Analyze this request:
"Website tổng hợp kiến thức AI cho dev từ cơ bản đến nâng cao nhất,
mỗi ngày tự nghiên cứu tin thị trường, có thể dùng cho nhiều người dùng".
Tạo bảng:
- Facts, Assumptions, Open questions, Out of scope
- MVP P0, P1, P2 theo 14 ngày / 3-4 giờ ngày
- 12 acceptance criteria có thể kiểm chứng từ UI, DB, logs
- Các rủi ro: nguồn, copyright, cost, hallucination, auth, cron,
  retry, data quality, failover
- ADR cần quyết định, lý do lựa chọn / tradeoffs
- Quá trình review bằng chứng trước khi leader approve.
Không đánh đồng 14 ngày với kho hoàn chỉnh hoặc chịu tải triệu users.
```

**Đáp án trọng điểm:** Scope P0 phải ưu tiên **6 bài hoàn chỉnh**, 18 syllabus, 1 daily job, ít nhất 3 nguồn có thể fetch thực tế, 1 dashboard admin và URL công khai; các bài còn lại ở backlog. Leader ký duyệt rủi ro news automation sau khi có replay test. Chưa được phép lấy dữ liệu công ty đưa vào AI thì dùng dữ liệu tổng hợp.

**Thực hành role-play:** Cho model A đề xuất “auto đăng tất cả”, nhờ model B phản biện bản quyền và sai sự thật, đưa ra decision log. **DoD:** 10+ yêu cầu có Given/When/Then; tách facts/opinion; 3 ADR ban đầu và biên bản quyết định.

---

### BỔ SUNG V3 — GIAO BÀI THEO CHUẨN NGHIỆM THU

**Năng lực được kiểm chứng:** Áp dụng AI vào refinement, ADR, roadmap, risk register và content provenance.

**Lý thuyết phải tự giải thích được:** Facts vs inferences vs opinion, cân nhắc copyright, access dữ liệu công ty.

**Bài thực hành bổ sung:** Bản requirement mơ hồ thành >=12 Given/When/Then và 3 ADR.

**Đầu ra xác định:** PRD/ADR/acceptance criteria và editorial policy. Từng artifact cần có owner, đường dẫn, trạng thái DRAFT/REVIEWED và liên kết với tiêu chí acceptance trong docs/TRACEABILITY_MATRIX.md.

**Negative testing:** Nhờ reviewer độc lập bác 3 claim không nguồn.

**Chu trình học:** 30–50 phút đọc official docs → 20 phút tự diễn đạt lại nguyên lý → 90–120 phút giao prompt cho Claude Code → 30–60 phút kiểm chứng file/diff/log → ghi learning log và phản biện. Nếu service mới phát sinh tiền, cần bạn cho phép trước.

**Rubric ngày 03 (10 điểm; cần ≥9 và không có blocker):** lý thuyết 2; chất lượng prompt và phạm vi 2; đầu ra đúng schema/file 2; tests có bằng chứng 2; bảo mật/nguồn và đánh giá rủi ro 2. Nếu thiếu bằng chứng test: tối đa 6/10, không được tự báo PASS.

**DoD:** Kiểm tra đủ file, evidence, test và quyền hạn; blocker còn tồn tại thì status=FAIL hoặc SKIP.

**Self-check:** Nếu agent nói “đã làm xong”, yêu cầu nó trả: danh sách file tạo/sửa, test command và exit code, 3 rủi ro còn lại, ảnh/URL/log nếu có, lý do mọi bài test bị skip, và trạng thái chưa xác minh.
