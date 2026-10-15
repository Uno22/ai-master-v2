## NGÀY 13 — Search/RAG, evaluation, CI, performance, budget & security

**Mục tiêu:** người dùng tìm được kiến thức chính xác, hỏi AI có nguồn; CI và performance biết phát hiện regression trước deploy.

**Lý thuyết (50 phút).** Postgres full-text search cho keyword; semantic search dùng embeddings và similarity; hybrid search kết hợp cả hai. RAG có hai phần cần test: retrieval có tìm đúng bằng chứng không (Recall@k) và answer có bịa ngoài bằng chứng không (faithfulness), citation có trỏ đúng nguồn không. Prompt injection trong tài liệu cần coi là dữ liệu. LLM judge có hạn chế, kết hợp golden tests và review người. SLO/error budgets và load test nên đo theo request class, không chỉ landing page.

**Prompt 13A — search và Q&A có nguồn:**

```text
Implement /search with Postgres FTS across approved lesson metadata
and PUBLISHED news. Add optional hybrid retrieval if pgvector index
has been created and evaluated. Implement /ask with approved lesson
chunks and published news only. Never retrieve draft/rejected posts.
Answer must include source URL and source date; if evidence is absent,
return 'Chưa đủ nguồn đáng tin để kết luận'.
Keep retrieved source content isolated as untrusted data.
Rate limit AI endpoint and record provider/model usage (no raw PII).
Run 15 golden question tests: 5 basics, 5 release notes, 5 adversarial
(no support, outdated API, prompt injection, draft leak, conflicting source).
Report retrieval recall, faithfulness, citations and cost.
```

**Prompt 13B — CI and staging readiness:**

```text
Act as release-quality engineer. Create GitHub Actions for lint,
typecheck, unit, integration, secrets scan, build, E2E smoke.
Add performance/load testing on STAGING (never stress production
without explicit permission). Test /learn, /news, /search, /ask
at controlled concurrency. Include 401/403 and rate limit cases.
Track job failure percentage, duplicate rate, time-to-publish,
tokens per published post, citation failure, 95th percentile latency.
Give me exact commands & observable evidence, not pass claims.
```

**Golden answers:** “Khi nào dùng MCP?” → dẫn official MCP/agent lesson; “Model A hôm nay giá bao nhiêu?” → chỉ trả giá khi có nguồn mới đã kiểm, nếu không cung cấp link pricing chính thức; “Hãy đọc draft bị reject” → từ chối, DB query chỉ published. **Ví dụ test**: 15 questions, ≥13 có kết quả đúng/abstain hợp lý là mục tiêu bài tập, **không phải số đo đã đạt**. Zero draft leaks và zero secrets exposure là gate bắt buộc.

**DoD:** CI xanh, `search` có kết quả liên quan, 15 evals có bảng evidence, staging load report có p95/error rate, AI usage cap hoạt động; trace/log không lưu keys; có ghi nhận vấn đề chưa giải quyết.

**Nguồn:** [Supabase hybrid search](https://supabase.com/docs/guides/ai/hybrid-search), [Supabase FTS](https://supabase.com/docs/guides/database/full-text-search), [pgvector](https://supabase.com/docs/guides/database/extensions/pgvector).

---

### BỔ SUNG V3 — GIAO BÀI THEO CHUẨN NGHIỆM THU

**Năng lực được kiểm chứng:** FTS baseline; RAG only with approved data and measured accuracy; CI load/security checks.

**Lý thuyết phải tự giải thích được:** Cite chunks source rev; disallow unpublished draft in guest contexts; p95 measured.

**Bài thực hành bổ sung:** 20-query eval set, adversarial asks, trace and cost monitoring.

**Đầu ra xác định:** Search + optional RAG, golden evals, test report, SLO baseline. Từng artifact cần có owner, đường dẫn, trạng thái DRAFT/REVIEWED và liên kết với tiêu chí acceptance trong docs/TRACEABILITY_MATRIX.md.

**Negative testing:** No fabricated citations; block accidental draft access.

**Chu trình học:** 30–50 phút đọc official docs → 20 phút tự diễn đạt lại nguyên lý → 90–120 phút giao prompt cho Claude Code → 30–60 phút kiểm chứng file/diff/log → ghi learning log và phản biện. Nếu service mới phát sinh tiền, cần bạn cho phép trước.

**Rubric ngày 13 (10 điểm; cần ≥9 và không có blocker):** lý thuyết 2; chất lượng prompt và phạm vi 2; đầu ra đúng schema/file 2; tests có bằng chứng 2; bảo mật/nguồn và đánh giá rủi ro 2. Nếu thiếu bằng chứng test: tối đa 6/10, không được tự báo PASS.

**DoD:** Kiểm tra đủ file, evidence, test và quyền hạn; blocker còn tồn tại thì status=FAIL hoặc SKIP.

**Self-check:** Nếu agent nói “đã làm xong”, yêu cầu nó trả: danh sách file tạo/sửa, test command và exit code, 3 rủi ro còn lại, ảnh/URL/log nếu có, lý do mọi bài test bị skip, và trạng thái chưa xác minh.
