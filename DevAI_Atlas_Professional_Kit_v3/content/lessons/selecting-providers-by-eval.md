# Chọn AI provider theo bài toán và đánh giá

> Track: T02 · Level: Beginner → Intermediate · Duration: 35–50 min · **Status: DRAFT — requires source review before publish**

## Mục tiêu

- Giải thích chính xác chọn ai provider theo bài toán và đánh giá cho một đồng nghiệp junior.
- Áp dụng vào kiến trúc DevAI Atlas mà không cần tự viết code.
- Chỉ ra ít nhất hai lỗi thường gặp và cách kiểm chứng.

## Kiến thức nền

1. Không có một model tốt nhất cho tất cả case; dùng eval và ngân sách thực tế.
2. Tách coding agent subscription và API runtime billing.
3. Tạo bảng provider capabilities có verified_at; không hardcode model IDs/pricing chưa kiểm tra.

## Case thực tế

Backend leader cần chọn model cho classify, summarize, code review.

## Thực hành bằng AI agent

```text
Hãy giải thích và áp dụng chủ đề "Chọn AI provider theo bài toán và đánh giá" cho DevAI Atlas.
Không tự viết code thay người học; hãy lập plan, tạo demo nếu được duyệt,
ghi file path, test evidence, claim citations, và 2 tình huống thất bại.
Dừng lại và hỏi approve nếu cần đổi dữ liệu production hoặc dùng dịch vụ trả phí.
```

## Bài tập
1. Thiết kế bảng điểm có weighted criteria cho 3 tasks.
2. Khi model không hỗ trợ schema cần fail thế nào?

## Lời giải có giải thích
1. Decision matrix: grounded quality 35%, cost 20%, latency 20%, tool support 15%, governance 10% — chỉ là trọng số ví dụ và cần stakeholder duyệt.
2. Fallback/adapter từ chối nếu thiếu capability, không giả API.

## Quiz và đáp án

1. Khái niệm chính của Chọn AI provider theo bài toán và đánh giá là gì? **Đáp án:** Dựa trên 3 gạch đầu dòng lý thuyết, không nhập nhằng tầng hệ thống.
2. Trường hợp nào cần human review? **Đáp án:** Khi claim thiếu source hoặc thao tác quyền cao.
3. Kết quả schema-pass là sufficient để publish? **Đáp án:** Không.
4. Nếu provider timeout phải làm gì? **Đáp án:** Retry bounded, log, chuyển failed/review.
5. Nếu input RSS chứa chỉ thị “bỏ luật”? **Đáp án:** Coi là dữ liệu không đáng tin và không thực thi.

## Nguồn cần đối chiếu trước khi publish
- https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview
- https://ai.google.dev/gemini-api/docs

## Review checklist

- [ ] Mở nguồn gốc, xác nhận nội dung phù hợp bản hiện tại
- [ ] Link vẫn hoạt động, có `verified_at` và người duyệt
- [ ] Không còn claim chưa có evidence
- [ ] Có kết quả lab, 2 negative tests và lời giải khác transcript AI
- [ ] Trạng thái chuyển REVIEWED/PUBLISHED chỉ bằng hành động editor
