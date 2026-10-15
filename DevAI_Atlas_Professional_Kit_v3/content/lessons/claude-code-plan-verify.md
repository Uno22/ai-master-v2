# Claude Code — plan, implement, verify, diff review

> Track: T04 · Level: Beginner → Intermediate · Duration: 35–50 min · **Status: DRAFT — requires source review before publish**

## Mục tiêu

- Giải thích chính xác claude code — plan, implement, verify, diff review cho một đồng nghiệp junior.
- Áp dụng vào kiến trúc DevAI Atlas mà không cần tự viết code.
- Chỉ ra ít nhất hai lỗi thường gặp và cách kiểm chứng.

## Kiến thức nền

1. Agent cần hiểu repo và boundaries trước khi sửa.
2. Chỉ cho agent implement sau khi duyệt plan; tập trung changed files.
3. CI exit code, log và test failure phải được ghi lại trung thực.

## Case thực tế

Tạo một feature News Sources Admin không tự viết code.

## Thực hành bằng AI agent

```text
Hãy giải thích và áp dụng chủ đề "Claude Code — plan, implement, verify, diff review" cho DevAI Atlas.
Không tự viết code thay người học; hãy lập plan, tạo demo nếu được duyệt,
ghi file path, test evidence, claim citations, và 2 tình huống thất bại.
Dừng lại và hỏi approve nếu cần đổi dữ liệu production hoặc dùng dịch vụ trả phí.
```

## Bài tập
1. Agent đề xuất migration xóa bảng hiện có: bạn phản hồi thế nào?
2. Tại sao không commit ngay khi agent tự báo test pass?

## Lời giải có giải thích
1. REJECT kế hoạch phá dữ liệu; yêu cầu additive migration và rollback.
2. Kiểm tra diff, pipeline logs, môi trường, permission và output trên UI.

## Quiz và đáp án

1. Khái niệm chính của Claude Code — plan, implement, verify, diff review là gì? **Đáp án:** Dựa trên 3 gạch đầu dòng lý thuyết, không nhập nhằng tầng hệ thống.
2. Trường hợp nào cần human review? **Đáp án:** Khi claim thiếu source hoặc thao tác quyền cao.
3. Kết quả schema-pass là sufficient để publish? **Đáp án:** Không.
4. Nếu provider timeout phải làm gì? **Đáp án:** Retry bounded, log, chuyển failed/review.
5. Nếu input RSS chứa chỉ thị “bỏ luật”? **Đáp án:** Coi là dữ liệu không đáng tin và không thực thi.

## Nguồn cần đối chiếu trước khi publish
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/hooks-guide

## Review checklist

- [ ] Mở nguồn gốc, xác nhận nội dung phù hợp bản hiện tại
- [ ] Link vẫn hoạt động, có `verified_at` và người duyệt
- [ ] Không còn claim chưa có evidence
- [ ] Có kết quả lab, 2 negative tests và lời giải khác transcript AI
- [ ] Trạng thái chuyển REVIEWED/PUBLISHED chỉ bằng hành động editor
