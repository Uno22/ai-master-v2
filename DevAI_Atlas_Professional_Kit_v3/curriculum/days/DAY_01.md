## NGÀY 01 — AI ecosystem, model selection và bản đồ học AI

**Mục tiêu:** phân biệt chatbot/coding agent/API/model/provider; tránh nhầm “dùng Claude Code để code” với “website phải dùng Claude API”.

**Lý thuyết (45 phút).** AI là lĩnh vực rộng; LLM là mô hình sinh/hiểu ngôn ngữ; model chạy qua dịch vụ Chat, API hoặc tích hợp tool. `token` ảnh hưởng giá, độ trễ, context; `hallucination` là đầu ra không có bằng chứng; `reasoning` không bảo đảm sự thật. ChatGPT/Claude/Gemini là giao diện người dùng; Claude Code/Codex/Copilot/Gemini CLI là coding workflow; OpenAI/Anthropic/Google/DeepSeek/xAI API là hạ tầng gọi model từ website. GitHub không phải LLM provider. So sánh `quality`, `tool/schema support`, `latency`, `price`, `context`, `data handling`, `availability`, `eval pass rate` và vendor risk.

**Thực hành:** mở một cuộc chat (ChatGPT hoặc Claude), giao cho AI nghiên cứu **chính website DevAI Atlas** và chủ đề học đầu tiên. Kiểm tra từng đường link được dẫn; không coi một bảng model tự tạo là fact cho 2026.

**Prompt 01 — research có dẫn nguồn:**

```text
Tôi là backend leader Node.js/NestJS, mới ứng dụng AI chuyên sâu.
Mục tiêu 14 ngày: dùng Claude Code xây website DevAI Atlas, tập hợp kiến thức
AI dành cho lập trình viên và cập nhật tin AI hằng ngày.
Hãy tạo decision matrix so sánh Claude Code, OpenAI/Codex, Google Gemini,
DeepSeek, Grok/xAI, GitHub Copilot cho 5 use cases:
1) lập PRD; 2) coding agent; 3) trích xuất release notes; 4) viết digest;
5) reviewer độc lập.
Mỗi nhận xét về tính năng phải có tài liệu CHÍNH THỨC, URL, ngày kiểm tra,
đánh dấu UNKNOWN nếu không thể xác thực. Không tự bịa giá hoặc model ID.
Phân biệt app Chat, coding agent, API và model.
Cuối cùng lập syllabus 18 tracks theo beginner→expert.
```

**Lời giải mong đợi:** Claude Code được chọn là **driver viết mã**; một model khác đánh giá tính chính xác tin/citations; gọi API riêng ở website; lesson và news đều hiển thị provenance. Nếu AI viết “model X luôn mới nhất” mà không có ngày kiểm chứng → **FAIL**.

**Bằng chứng hoàn thành:** `docs/PROVIDER_MATRIX.md`, `content/tracks.yaml` nháp, danh sách ít nhất 10 tài liệu official kèm URL. **Câu hỏi tự kiểm tra:** “Claude Code và Claude API khác nhau ở đâu?” — *Agent thực thi công việc trên repo vs endpoint model được website gọi*. “Giá của gói chat có bao gồm phí API website không?” — *Không mặc định*.

---

### BỔ SUNG V3 — GIAO BÀI THEO CHUẨN NGHIỆM THU

**Năng lực được kiểm chứng:** Phân biệt sản phẩm Chat, model, coding agent, API, tool, MCP, embeddings và RAG; so sánh bằng evidence.

**Lý thuyết phải tự giải thích được:** Đối chiếu model/API capabilities có nguồn chính thức. Không phán model tốt nhất khi chưa có eval; tránh giá không kiểm chứng.

**Bài thực hành bổ sung:** Một bảng 6 providers × 6 use cases; ít nhất 2 nguồn official/provider; phản biện thiên lệch.

**Đầu ra xác định:** Provider decision matrix và roadmap 18 tracks. Từng artifact cần có owner, đường dẫn, trạng thái DRAFT/REVIEWED và liên kết với tiêu chí acceptance trong docs/TRACEABILITY_MATRIX.md.

**Negative testing:** Từ chối mọi quyết định chứa model ID không tra cứu được.

**Chu trình học:** 30–50 phút đọc official docs → 20 phút tự diễn đạt lại nguyên lý → 90–120 phút giao prompt cho Claude Code → 30–60 phút kiểm chứng file/diff/log → ghi learning log và phản biện. Nếu service mới phát sinh tiền, cần bạn cho phép trước.

**Rubric ngày 01 (10 điểm; cần ≥9 và không có blocker):** lý thuyết 2; chất lượng prompt và phạm vi 2; đầu ra đúng schema/file 2; tests có bằng chứng 2; bảo mật/nguồn và đánh giá rủi ro 2. Nếu thiếu bằng chứng test: tối đa 6/10, không được tự báo PASS.

**DoD:** Kiểm tra đủ file, evidence, test và quyền hạn; blocker còn tồn tại thì status=FAIL hoặc SKIP.

**Self-check:** Nếu agent nói “đã làm xong”, yêu cầu nó trả: danh sách file tạo/sửa, test command và exit code, 3 rủi ro còn lại, ảnh/URL/log nếu có, lý do mọi bài test bị skip, và trạng thái chưa xác minh.
