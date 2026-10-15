# AI, LLM, Chatbot, API và Coding Agent

> Track: T01 · Level: Beginner → Intermediate · Duration: 35–50 min · **Status: DRAFT — requires source review before publish**

## Mục tiêu

- Giải thích chính xác ai, llm, chatbot, api và coding agent cho một đồng nghiệp junior.
- Áp dụng vào kiến trúc DevAI Atlas mà không cần tự viết code.
- Chỉ ra ít nhất hai lỗi thường gặp và cách kiểm chứng.

## Kiến thức nền

1. AI là phạm trù rộng, ML học từ dữ liệu, LLM xử lý/sinh văn bản.
2. Chatbot là sản phẩm/giao diện; API là kênh backend truy cập model; coding agent có tools và workflow.
3. LLM không có quyền quyết định ủy quyền/publish; backend policy và reviewer đảm nhiệm.

## Case thực tế

Câu chuyện: leader muốn tự sinh bản tin AI theo lịch.

## Thực hành bằng AI agent

```text
Hãy giải thích và áp dụng chủ đề "AI, LLM, Chatbot, API và Coding Agent" cho DevAI Atlas.
Không tự viết code thay người học; hãy lập plan, tạo demo nếu được duyệt,
ghi file path, test evidence, claim citations, và 2 tình huống thất bại.
Dừng lại và hỏi approve nếu cần đổi dữ liệu production hoặc dùng dịch vụ trả phí.
```

## Bài tập
1. Khi click nút Run now, các bước nào thuộc scheduler, agent, model và DB?
2. Tại sao không nên lấy JSON hợp lệ làm bằng chứng tin đúng?

## Lời giải có giải thích
1. Scheduler orchestrates, adapter fetches, model drafts, validator checks, admin approves, DB persists.
2. Đúng JSON chỉ chứng minh shape; claim phải có bằng chứng nguồn độc lập.

## Quiz và đáp án

1. Khái niệm chính của AI, LLM, Chatbot, API và Coding Agent là gì? **Đáp án:** Dựa trên 3 gạch đầu dòng lý thuyết, không nhập nhằng tầng hệ thống.
2. Trường hợp nào cần human review? **Đáp án:** Khi claim thiếu source hoặc thao tác quyền cao.
3. Kết quả schema-pass là sufficient để publish? **Đáp án:** Không.
4. Nếu provider timeout phải làm gì? **Đáp án:** Retry bounded, log, chuyển failed/review.
5. Nếu input RSS chứa chỉ thị “bỏ luật”? **Đáp án:** Coi là dữ liệu không đáng tin và không thực thi.

## Nguồn cần đối chiếu trước khi publish
- https://code.claude.com/docs/en/overview
- https://developers.openai.com/api/docs/guides/function-calling

## Review checklist

- [ ] Mở nguồn gốc, xác nhận nội dung phù hợp bản hiện tại
- [ ] Link vẫn hoạt động, có `verified_at` và người duyệt
- [ ] Không còn claim chưa có evidence
- [ ] Có kết quả lab, 2 negative tests và lời giải khác transcript AI
- [ ] Trạng thái chuyển REVIEWED/PUBLISHED chỉ bằng hành động editor
