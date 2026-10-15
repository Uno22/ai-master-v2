# Prompt Engineering và JSON Schema

> Track: T03 · Level: Beginner → Intermediate · Duration: 35–50 min · **Status: DRAFT — requires source review before publish**

## Mục tiêu

- Giải thích chính xác prompt engineering và json schema cho một đồng nghiệp junior.
- Áp dụng vào kiến trúc DevAI Atlas mà không cần tự viết code.
- Chỉ ra ít nhất hai lỗi thường gặp và cách kiểm chứng.

## Kiến thức nền

1. Prompt contract: objective, context, trusted/untrusted, schema, failures, test.
2. Structured outputs validate structure but semantic checking remains necessary.
3. Version prompts và test với positive/negative examples.

## Case thực tế

AI nhận raw source item, xuất NewsDraft.

## Thực hành bằng AI agent

```text
Hãy giải thích và áp dụng chủ đề "Prompt Engineering và JSON Schema" cho DevAI Atlas.
Không tự viết code thay người học; hãy lập plan, tạo demo nếu được duyệt,
ghi file path, test evidence, claim citations, và 2 tình huống thất bại.
Dừng lại và hỏi approve nếu cần đổi dữ liệu production hoặc dùng dịch vụ trả phí.
```

## Bài tập
1. Viết prompt tạo NewsDraft có claim_evidence và review_required.
2. Tin rumor với một URL fake có được auto publish?

## Lời giải có giải thích
1. Required fields và enum rõ; validate bằng schema + link/source registry và independent reviewer.
2. Không, rumor review và reject/quarantine.

## Quiz và đáp án

1. Khái niệm chính của Prompt Engineering và JSON Schema là gì? **Đáp án:** Dựa trên 3 gạch đầu dòng lý thuyết, không nhập nhằng tầng hệ thống.
2. Trường hợp nào cần human review? **Đáp án:** Khi claim thiếu source hoặc thao tác quyền cao.
3. Kết quả schema-pass là sufficient để publish? **Đáp án:** Không.
4. Nếu provider timeout phải làm gì? **Đáp án:** Retry bounded, log, chuyển failed/review.
5. Nếu input RSS chứa chỉ thị “bỏ luật”? **Đáp án:** Coi là dữ liệu không đáng tin và không thực thi.

## Nguồn cần đối chiếu trước khi publish
- https://developers.openai.com/api/docs/guides/structured-outputs
- https://ai.google.dev/gemini-api/docs/structured-output

## Review checklist

- [ ] Mở nguồn gốc, xác nhận nội dung phù hợp bản hiện tại
- [ ] Link vẫn hoạt động, có `verified_at` và người duyệt
- [ ] Không còn claim chưa có evidence
- [ ] Có kết quả lab, 2 negative tests và lời giải khác transcript AI
- [ ] Trạng thái chuyển REVIEWED/PUBLISHED chỉ bằng hành động editor
