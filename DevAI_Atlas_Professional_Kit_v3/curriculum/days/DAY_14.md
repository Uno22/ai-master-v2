## NGÀY 14 — Deploy public, QA cuối, vận hành lâu dài và bằng chứng daily run

**Mục tiêu:** website công khai thật có HTTPS, đường link bài học, tin tức, quản trị, và job mỗi ngày; bạn có thể dừng/sửa/hồi phục hệ thống.

**Lý thuyết (35 phút).** Staging và production sử dụng các environment secrets riêng; migration trước deploy phải review/backup; post-deploy smoke; rollback ứng dụng khác rollback dữ liệu. Public launch cần tài liệu privacy/attribution, chính sách sử dụng nguồn, error page, sitemap, robots, analytics tuân thủ. Một ngày có scheduler failure phải có alert và nút replay. Deploy **không** chứng minh toàn bộ bài báo tương lai sẽ chính xác; editorial quality là công việc liên tục.

**Prompt 14 — release manager:**

```text
Act as release manager for DevAI Atlas MVP v1.0.
Before any production change, show deploy plan and require my approval.
Verify: 18 learning track pages; >=6 complete reviewed lessons;
3+ permitted source adapters with live evidence; news ingest + dedupe;
AI drafts with source citations + review queue; admin RBAC;
manual Run Now; 07:00 Vietnam daily schedule configured;
retry logs and duplicate prevention; search; SEO; rate limits;
CI/test evidence, security checks, cost limits and runbook.
Deploy Vercel + Supabase + Inngest with server-only secrets,
perform smoke tests and provide redacted logs/screenshots.
Do not auto-claim cron successful before a real scheduled invocation.
Produce release note, known issues, rollback strategy and monitoring plan.
```

**UAT checklist bắt buộc:**

| ID | Thử nghiệm người dùng | Điều kiện PASS |
|---|---|---|
| UAT-01 | Guest vào `/learn` | 18 tracks không link chết |
| UAT-02 | Đọc một bài beginner | Có explanation, ví dụ dev, quiz, đáp án, sources |
| UAT-03 | Đọc bài expert chưa xuất bản | Không fake content, trạng thái minh bạch |
| UAT-04 | Xem `/news` | Có nguồn và thời điểm, không bịa |
| UAT-05 | Click original article | Đến URL hợp lệ, không chuyển trái ý |
| UAT-06 | Rerun ingestion cùng dữ liệu | Không duplicate posts |
| UAT-07 | Một feed trả 429/timeouts | Source khác vẫn xử lý, lỗi được ghi |
| UAT-08 | Guest tìm `/admin` | Bị chặn server-side |
| UAT-09 | Editor duyệt HIGH-impact | Chỉ publish sau approval, có audit |
| UAT-10 | Tin đầu vào mang prompt injection | Không thực thi tool, không tiết lộ secret |
| UAT-11 | `/search` | Tìm đúng bài theo keyword |
| UAT-12 | `/ask` không có bằng chứng | Từ chối kết luận hoặc nói thiếu nguồn |
| UAT-13 | Không có tin phù hợp | Không sinh tin giả để đủ số lượng |
| UAT-14 | Job Run Now | Có run ID, counts, logs, duration, cost |
| UAT-15 | Lịch 07:00 VN | Cấu hình đúng timezone; theo dõi lượt chạy thật kế tiếp |
| UAT-16 | Mobile + SEO | UI usable, title/description/sitemap đúng |
| UAT-17 | Rate limit & budgets | Request vượt giới hạn bị từ chối hợp lý |
| UAT-18 | Deploy + rollback | Có runbook/known issues, staging vs prod secrets tách |

**Tiêu chí tốt nghiệp (không nới lỏng):** UAT-01..14,16..18 PASS, UAT-15 xác minh cấu hình và **sau lượt lịch thực tế** kiểm tra event logs để chuyển sang `VERIFIED_DAILY_RUN`. Ngày 14 có thể hoàn tất deployment nhưng lượt 07:00 tiếp theo chưa xảy ra; trạng thái phải ghi rõ `PENDING_SCHEDULED_PROOF`, không nói đã chạy mỗi ngày khi chưa quan sát thấy. Public uptime/scale chỉ tuyên bố theo đo đạc.

**Artifacts:** URL public (sau khi bạn thực hành), repository, CI report, production smoke results, runbook, `docs/POST_LAUNCH_CHECKLIST.md`, screenshot logs và báo cáo chi phí. Sau đó vận hành, lặp lại editorial quality gate mỗi ngày.

---

### BỔ SUNG V3 — GIAO BÀI THEO CHUẨN NGHIỆM THU

**Năng lực được kiểm chứng:** Staging→production review with security, rollback, logging and scheduled proof.

**Lý thuyết phải tự giải thích được:** Secrets and service roles server only; test by role; distinguish pending schedule proof.

**Bài thực hành bổ sung:** Run UATs, record redacted logs/screenshots, manual trigger, follow scheduled run.

**Đầu ra xác định:** Public HTTPS, evidence pack, known issues, rollback and runbook. Từng artifact cần có owner, đường dẫn, trạng thái DRAFT/REVIEWED và liên kết với tiêu chí acceptance trong docs/TRACEABILITY_MATRIX.md.

**Negative testing:** Do not award runtime 10/10 without external acceptance evidence.

**Chu trình học:** 30–50 phút đọc official docs → 20 phút tự diễn đạt lại nguyên lý → 90–120 phút giao prompt cho Claude Code → 30–60 phút kiểm chứng file/diff/log → ghi learning log và phản biện. Nếu service mới phát sinh tiền, cần bạn cho phép trước.

**Rubric ngày 14 (10 điểm; cần ≥9 và không có blocker):** lý thuyết 2; chất lượng prompt và phạm vi 2; đầu ra đúng schema/file 2; tests có bằng chứng 2; bảo mật/nguồn và đánh giá rủi ro 2. Nếu thiếu bằng chứng test: tối đa 6/10, không được tự báo PASS.

**DoD:** Kiểm tra đủ file, evidence, test và quyền hạn; blocker còn tồn tại thì status=FAIL hoặc SKIP.

**Self-check:** Nếu agent nói “đã làm xong”, yêu cầu nó trả: danh sách file tạo/sửa, test command và exit code, 3 rủi ro còn lại, ảnh/URL/log nếu có, lý do mọi bài test bị skip, và trạng thái chưa xác minh.
