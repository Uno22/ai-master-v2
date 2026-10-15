# Phân biệt Workflows, Agents, MCP và RAG

> Track: T06 · Level: Beginner → Intermediate · Duration: 35–50 min · **Status: DRAFT — requires source review before publish**

## Mục tiêu

- Giải thích chính xác phân biệt workflows, agents, mcp và rag cho một đồng nghiệp junior.
- Áp dụng vào kiến trúc DevAI Atlas mà không cần tự viết code.
- Chỉ ra ít nhất hai lỗi thường gặp và cách kiểm chứng.

## Kiến thức nền

1. Workflow là state transition có bước xác định; agent quyết định một số bước trong ranh giới cho phép.
2. MCP là chuẩn kết nối tools/data, không phải model và không mặc nhiên an toàn.
3. RAG truy xuất approved texts để cải thiện grounded answering, không thay thế editorial control.

## Case thực tế

Daily intelligence từ release docs tới bản tin public.

## Thực hành bằng AI agent

```text
Hãy giải thích và áp dụng chủ đề "Phân biệt Workflows, Agents, MCP và RAG" cho DevAI Atlas.
Không tự viết code thay người học; hãy lập plan, tạo demo nếu được duyệt,
ghi file path, test evidence, claim citations, và 2 tình huống thất bại.
Dừng lại và hỏi approve nếu cần đổi dữ liệu production hoặc dùng dịch vụ trả phí.
```

## Bài tập
1. Lập state machine INGESTED→VERIFIED→DRAFT→REVIEWED→PUBLISHED.
2. RSS yêu cầu agent gọi admin endpoint sẽ được xử lý ra sao?

## Lời giải có giải thích
1. Backend kiểm soát publish; tool dispatcher không tin nguồn và chỉ proposal từ model.
2. Ignore untrusted instruction, log injection signal, no external publish.

## Quiz và đáp án

1. Khái niệm chính của Phân biệt Workflows, Agents, MCP và RAG là gì? **Đáp án:** Dựa trên 3 gạch đầu dòng lý thuyết, không nhập nhằng tầng hệ thống.
2. Trường hợp nào cần human review? **Đáp án:** Khi claim thiếu source hoặc thao tác quyền cao.
3. Kết quả schema-pass là sufficient để publish? **Đáp án:** Không.
4. Nếu provider timeout phải làm gì? **Đáp án:** Retry bounded, log, chuyển failed/review.
5. Nếu input RSS chứa chỉ thị “bỏ luật”? **Đáp án:** Coi là dữ liệu không đáng tin và không thực thi.

## Nguồn cần đối chiếu trước khi publish
- https://modelcontextprotocol.io/introduction
- https://genai.owasp.org/llm-top-10/

## Review checklist

- [ ] Mở nguồn gốc, xác nhận nội dung phù hợp bản hiện tại
- [ ] Link vẫn hoạt động, có `verified_at` và người duyệt
- [ ] Không còn claim chưa có evidence
- [ ] Có kết quả lab, 2 negative tests và lời giải khác transcript AI
- [ ] Trạng thái chuyển REVIEWED/PUBLISHED chỉ bằng hành động editor
