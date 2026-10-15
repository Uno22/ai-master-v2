# Token, context, hallucinations và grounding

> Track: T01 · Level: Beginner → Intermediate · Duration: 35–50 min · **Status: DRAFT — requires source review before publish**

## Mục tiêu

- Giải thích chính xác token, context, hallucinations và grounding cho một đồng nghiệp junior.
- Áp dụng vào kiến trúc DevAI Atlas mà không cần tự viết code.
- Chỉ ra ít nhất hai lỗi thường gặp và cách kiểm chứng.

## Kiến thức nền

1. Tokens ảnh hưởng độ dài và chi phí; context là dữ liệu model nhìn thấy ở invocation.
2. Hallucination là thông tin không được chứng minh; citation URLs có thể sai hoặc không hỗ trợ claim.
3. Grounding yêu cầu claim liên kết evidence item; người hoặc validator độc lập xác minh.

## Case thực tế

Một release note ghi 3 API changes nhưng bản tóm tắt invent thêm giá.

## Thực hành bằng AI agent

```text
Hãy giải thích và áp dụng chủ đề "Token, context, hallucinations và grounding" cho DevAI Atlas.
Không tự viết code thay người học; hãy lập plan, tạo demo nếu được duyệt,
ghi file path, test evidence, claim citations, và 2 tình huống thất bại.
Dừng lại và hỏi approve nếu cần đổi dữ liệu production hoặc dùng dịch vụ trả phí.
```

## Bài tập
1. Trong 4 claim, một claim thiếu release URL: hệ thống xử lý thế nào?
2. Điều gì xảy ra khi context quá dài?

## Lời giải có giải thích
1. Claim không evidence: reject hoặc REVIEW_REQUIRED, tuyệt đối không auto-publish.
2. Có thể mất thông tin hoặc bị cắt theo giới hạn; xử lý bằng chunk/retrieve và validation.

## Quiz và đáp án

1. Khái niệm chính của Token, context, hallucinations và grounding là gì? **Đáp án:** Dựa trên 3 gạch đầu dòng lý thuyết, không nhập nhằng tầng hệ thống.
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
