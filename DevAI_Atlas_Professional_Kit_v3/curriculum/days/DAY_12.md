## NGÀY 12 — Scheduler 07:00 VN, durable jobs, replay, review queue & publication

**Mục tiêu:** hệ thống **tự chạy hằng ngày sau khi deploy**, không phụ thuộc máy tính cá nhân hoặc cuộc chat; có nút Run Now và job recovery.

**Lý thuyết (45 phút).** Scheduler chỉ phát tín hiệu; workflow background chạy nhiều bước có retry độc lập. Exactly-once là kỳ vọng khó bảo đảm hoàn toàn; dùng idempotent DB constraints và transactional writes để đạt **effectively-once**. Concurrency control tránh hai lịch đụng nhau. Dead-letter/review cần thấy số lần thử, lỗi, record ảnh hưởng. Cron timezone là lỗi phổ biến. Human review cho high-impact content không được bỏ qua khi AI tự tin.

**Prompt 12 — automation production-safe:**

```text
Implement daily-intelligence workflow with Inngest durable functions.
Schedule once per day at 07:00 Asia/Ho_Chi_Minh (use timezone-aware
cron supported by installed SDK; verify the exact SDK version).
Expose an authenticated admin Run Now action with an idempotency key.
Stages: fetch -> normalize/dedupe -> rank -> AI draft -> validation
-> editorial queue -> publish ONLY low-risk eligible content
-> reindex/cache -> job report.
High-impact security/API-pricing/deprecation/model claims => needs review.
If no verified material, publish no new article; show 'No verified news'.
Persist run_id, each step outcome, failure reason, retries, cost, totals.
Prevent overlapping jobs, prevent 2 posts for same canonical source.
Test scheduler conversion to UTC, replay, crash mid-step, 429,
partial source failure, empty day, editor reject/approve, retry budget.
Add a runbook with how to pause automatic publishing and trigger replay.
Do not activate the production cron before my explicit approval.
```

**Bài giải timezone:** VN = UTC+7 quanh năm. Một scheduler chỉ dùng UTC: `0 0 * * *` → 07:00 VN. Một scheduler hỗ trợ timezone prefix: dùng `TZ=Asia/Ho_Chi_Minh 0 7 * * *` **nếu syntax được xác minh với SDK cài thực tế**. Chỉ cấu hình **một** cách, không tạo hai jobs. Lịch không bảo đảm uptime 100% hoặc timing đúng đến phút; logs/alerts giúp phát hiện miss.

**Bằng chứng nghiệm thu:** manual run pass, hàng đợi xuất draft, approve một draft lưu `published` và source links; rerun không duplicate; auto-publish HIGH impact bị block; lỗi nguồn riêng không làm mất cả ngày; cron cấu hình hiển thị trên dashboard nhà cung cấp. **Tối thiểu ngày 12:** có deploy staging cho job và theo dõi sau lượt chạy theo lịch thật; manual trigger một lần **không** phải bằng chứng daily cron đã chạy thật.

**Nguồn:** [Inngest schedules](https://www.inngest.com/docs/durable-execution/guides-and-advanced/events-and-triggers/schedules-and-delayed-starts), [Inngest durable execution](https://www.inngest.com/docs/durable-execution), [Vercel Cron usage](https://vercel.com/docs/cron-jobs/usage-and-pricing), [Vercel security](https://vercel.com/docs/cron-jobs/manage-cron-jobs).

---

### BỔ SUNG V3 — GIAO BÀI THEO CHUẨN NGHIỆM THU

**Năng lực được kiểm chứng:** 07:00 VN scheduled Inngest; replay, idempotency, run logs, editor approval.

**Lý thuyết phải tự giải thích được:** Use one scheduler; `TZ=Asia/Ho_Chi_Minh 0 7 * * *` or UTC equivalent.

**Bài thực hành bổ sung:** Simulate retries, duplicate concurrent runs, failed source, partial success.

**Đầu ra xác định:** Daily job + manual replay + run history + approved publication. Từng artifact cần có owner, đường dẫn, trạng thái DRAFT/REVIEWED và liên kết với tiêu chí acceptance trong docs/TRACEABILITY_MATRIX.md.

**Negative testing:** Do not claim actual scheduled run before observed event.

**Chu trình học:** 30–50 phút đọc official docs → 20 phút tự diễn đạt lại nguyên lý → 90–120 phút giao prompt cho Claude Code → 30–60 phút kiểm chứng file/diff/log → ghi learning log và phản biện. Nếu service mới phát sinh tiền, cần bạn cho phép trước.

**Rubric ngày 12 (10 điểm; cần ≥9 và không có blocker):** lý thuyết 2; chất lượng prompt và phạm vi 2; đầu ra đúng schema/file 2; tests có bằng chứng 2; bảo mật/nguồn và đánh giá rủi ro 2. Nếu thiếu bằng chứng test: tối đa 6/10, không được tự báo PASS.

**DoD:** Kiểm tra đủ file, evidence, test và quyền hạn; blocker còn tồn tại thì status=FAIL hoặc SKIP.

**Self-check:** Nếu agent nói “đã làm xong”, yêu cầu nó trả: danh sách file tạo/sửa, test command và exit code, 3 rủi ro còn lại, ảnh/URL/log nếu có, lý do mọi bài test bị skip, và trạng thái chưa xác minh.
