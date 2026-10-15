## NGÀY 09 — Database, Supabase auth, admin editor và permissions

**Mục tiêu:** data model theo PHẦN I, trang admin nhìn được records, quyền guest/editor/admin hoạt động.

**Lý thuyết (45 phút).** Database migration = thay đổi schema có version; indexes hỗ trợ query; unique constraints chống trùng; RLS bảo vệ row nhưng không thay thế kiểm soát API; `service_role` thường bypass RLS và chỉ dùng server trusted. Session phải được xác minh từ backend. Metadata external URL cần validate trước khi dùng tránh SSRF/open redirects. Secrets trong encrypted environment variables, không lộ client bundle.

**Prompt 09 — migrations + RLS + admin:**

```text
Implement DevAI Atlas phase 2 in Supabase.
Create reviewed migrations for news_sources, source_items, clusters,
news_posts, post_sources, editorial_reviews, ingestion_runs,
profiles, reading_progress, bookmarks, ai_usage and audit_log.
Enforce unique canonical source item keys and foreign key consistency.
Enable and test RLS for user-owned data. Public may SELECT ONLY
published articles and public source metadata; cannot read drafts/jobs.
Admin/editor role must be derived from trusted server/DB logic;
normal users cannot self-assign privileged roles.
Implement /admin/sources, /admin/review, /admin/runs with auth.
Test guest GET, POST, forged admin role, XSS payload, invalid URL,
unauthorized publish, RLS bypass attempts; don't run prod migrations.
Return migration diff and rollback-safe plan before executing.
```

**Lời giải permission matrix:**

| Người dùng | Đọc bài public | Xem draft | Review & Publish | Sửa nguồn | Thay bookmarks của người khác |
|---|---|---|---|---|---|
| Guest | Yes | No | No | No | No |
| Logged-in user | Yes | No | No | No | No |
| Editor | Yes | Yes | Yes (qua server validation) | Theo chính sách (mặc định No) | No |
| Admin | Yes | Yes | Yes | Yes | No (trừ quy trình hỗ trợ được audit) |

**Bài test quan trọng:** Guest sửa request để `status=PUBLISHED` → 403, DB giữ DRAFT. User gửi `role=ADMIN` trong profile update → từ chối. ID trong query không được để lộ post chưa duyệt. **DoD:** tests chứng minh quyền; có demo account guest/editor/admin bằng dữ liệu giả; migration rollback script/plan; `audit_log` ghi approve/reject/run.

---

### BỔ SUNG V3 — GIAO BÀI THEO CHUẨN NGHIỆM THU

**Năng lực được kiểm chứng:** Schema/migrations, auth SSR, RBAC/DB RLS, least privilege.

**Lý thuyết phải tự giải thích được:** Review service_role bypass; admin role never editable by user; account creation does not grant editor.

**Bài thực hành bổ sung:** Guest/editor/admin matrix, RLS tests, copy a public article.

**Đầu ra xác định:** Supabase migration, policies, protected admin, negative tests. Từng artifact cần có owner, đường dẫn, trạng thái DRAFT/REVIEWED và liên kết với tiêu chí acceptance trong docs/TRACEABILITY_MATRIX.md.

**Negative testing:** Fail nếu anonymous có thể read draft hoặc write news.

**Chu trình học:** 30–50 phút đọc official docs → 20 phút tự diễn đạt lại nguyên lý → 90–120 phút giao prompt cho Claude Code → 30–60 phút kiểm chứng file/diff/log → ghi learning log và phản biện. Nếu service mới phát sinh tiền, cần bạn cho phép trước.

**Rubric ngày 09 (10 điểm; cần ≥9 và không có blocker):** lý thuyết 2; chất lượng prompt và phạm vi 2; đầu ra đúng schema/file 2; tests có bằng chứng 2; bảo mật/nguồn và đánh giá rủi ro 2. Nếu thiếu bằng chứng test: tối đa 6/10, không được tự báo PASS.

**DoD:** Kiểm tra đủ file, evidence, test và quyền hạn; blocker còn tồn tại thì status=FAIL hoặc SKIP.

**Self-check:** Nếu agent nói “đã làm xong”, yêu cầu nó trả: danh sách file tạo/sửa, test command và exit code, 3 rủi ro còn lại, ảnh/URL/log nếu có, lý do mọi bài test bị skip, và trạng thái chưa xác minh.
