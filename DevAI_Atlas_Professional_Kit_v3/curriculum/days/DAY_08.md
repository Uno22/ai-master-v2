## NGÀY 08 — Public website: learning experience, SEO và nội dung có phiên bản

**Mục tiêu:** website xem được trên local; từ homepage tới lesson thật có bài tập, lời giải, link nguồn. Không dùng dashboard admin làm giao diện chính.

**Lý thuyết (35 phút).** Next.js App Router; rendering static/SSR/ISR; MDX là bài học có nội dung + component. User journey cần lộ trình rõ, mục lục, breadcrumbs, đọc trên điện thoại, keyboard access, semantic headings, description, Open Graph, sitemap, canonical URLs và loading/error states. SEO không phải lý do tạo bài kém chất lượng số lượng lớn.

**Prompt 08 — giao toàn bộ UI cho Claude Code:**

```text
Implement DevAI Atlas public website phase 1.
Build responsive Next.js App Router + TypeScript + accessible UI.
Pages: /, /learn, /learn/[track], /learn/[track]/[lesson],
/news (empty/loading state), /search (keyword), /about, /sources.
Read content/tracks.yaml and versioned MDX under content/lessons.
Display level badges, objectives, prerequisites, table of contents,
Node/NestJS worked examples, exercise/solution, quiz, verified_at and
links to official docs. Do not write fake news or fake model rankings.
Generate 18-track syllabus + 6 reviewed seed lessons from docs.
Create sitemap/robots/OG metadata; add keyboard and mobile tests.
First show UI plan; only implement on my approval; return build/test output.
```

**Lời giải UI checklist:** từ Home click “AI Foundations” → Track → Lesson có ít nhất 1 ví dụ Node/NestJS, 3 câu quiz và lời giải có thể mở; mỗi bài có nguồn gốc và `verified_at`. Sidebar hiển thị 18 tracks, những bài chưa phát hành hiện “Coming soon”, không có link chết. Mobile width nhỏ không cuộn ngang. Search `prompt` trả lesson `Prompt & JSON schema`. **Lỗi thường gặp:** AI dựng homepage hoành tráng nhưng không viết nội dung thực → không đạt.

**DoD:** các URL nêu trên trả 200, 6 bài chất lượng đi qua editorial review, `npm run build` xanh, zero uncaught client errors, no fake articles.

---

### BỔ SUNG V3 — GIAO BÀI THEO CHUẨN NGHIỆM THU

**Năng lực được kiểm chứng:** Next.js App Router, MDX, responsive accessibility, canonical SEO, search.

**Lý thuyết phải tự giải thích được:** SEO/OG, safe rendering, loading/errors/not-found; minimal design system.

**Bài thực hành bổ sung:** Follow home→track→lesson; keyword search, keyboard/mobile smoke.

**Đầu ra xác định:** Public routes, 18-track navigation, 6 published only after review. Từng artifact cần có owner, đường dẫn, trạng thái DRAFT/REVIEWED và liên kết với tiêu chí acceptance trong docs/TRACEABILITY_MATRIX.md.

**Negative testing:** Không công bố “expert” nếu chỉ mới outline.

**Chu trình học:** 30–50 phút đọc official docs → 20 phút tự diễn đạt lại nguyên lý → 90–120 phút giao prompt cho Claude Code → 30–60 phút kiểm chứng file/diff/log → ghi learning log và phản biện. Nếu service mới phát sinh tiền, cần bạn cho phép trước.

**Rubric ngày 08 (10 điểm; cần ≥9 và không có blocker):** lý thuyết 2; chất lượng prompt và phạm vi 2; đầu ra đúng schema/file 2; tests có bằng chứng 2; bảo mật/nguồn và đánh giá rủi ro 2. Nếu thiếu bằng chứng test: tối đa 6/10, không được tự báo PASS.

**DoD:** Kiểm tra đủ file, evidence, test và quyền hạn; blocker còn tồn tại thì status=FAIL hoặc SKIP.

**Self-check:** Nếu agent nói “đã làm xong”, yêu cầu nó trả: danh sách file tạo/sửa, test command và exit code, 3 rủi ro còn lại, ảnh/URL/log nếu có, lý do mọi bài test bị skip, và trạng thái chưa xác minh.
