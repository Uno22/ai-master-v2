## NGÀY 10 — Collectors thực tế: RSS/API, canonical URLs, de-duplication và source compliance

**Mục tiêu:** lấy dữ liệu thật từ **ít nhất 3 nguồn có API/feed hợp lệ** (không phụ thuộc HTML scrape), chuẩn hóa và lưu mà không tạo tin trùng.

**Lý thuyết (45 phút).** RSS/Atom/API có schema, pagination, ETag/Last-Modified, timestamp, rate-limit, 429/503, timeout, caching. Canonical URL cần bỏ tracking query, giữ query có ý nghĩa, xử lý redirect có kiểm soát, chống SSRF; GUID/source ID đáng tin hơn URL nếu publisher giữ ổn định. Dedup exact (`source_id/external_id/canonical`) + semantic clustering (các báo cùng nói một release). Cần loại các bài quá cũ bị coi nhầm là “hôm nay”. Không bypass paywall hoặc copy full article trái phép.

**Prompt 10 — lập adapters và mocks trước, rồi live check:**

```text
Create a source-registry/ingestion module with adapter interfaces:
RssAtomAdapter, GitHubReleaseAdapter and ProviderChangelogAdapter
(last one only if official page offers allowed access; otherwise use
manual source links/feed entries, NO undocumented scraping).
Start with 3-5 sources whose access and terms we can confirm.
For each: source type, allowed endpoint, license notes, freshness,
timeouts, rate limits, last-success timestamp.
On a single run: fetch metadata, normalize, validate timestamps,
canonicalize safe URLs, dedupe by stable source key, cluster similar
items, save source_items and ingestion_run with counters and logs.
Implement bounded retry/backoff with 429 Retry-After handling;
Do not request localhost/private network, recheck redirect hops.
Support --dry-run/test fixtures before live requests.
Test exact duplicate, UTM variant, missing date, malformed XML,
slow source, 429, forbidden source, redirects, duplicate concurrent jobs.
Return sample outputs from REAL verified sources with URLs (no invented
articles), SQL checks and test run IDs.
```

**Ví dụ đáp án dedupe:**

```text
A: https://provider.example/news/release-1?utm_source=x
B: https://provider.example/news/release-1?utm_source=y
=> cùng 1 canonical URL; INSERT 1 source_item, duplicate_count += 1
C: Official changelog và GitHub release nói cùng tính năng
=> 2 source_items, có thể cùng 1 cluster, KHÔNG xóa evidence phụ
```

> Host `provider.example` là fixture minh họa, không phải nguồn được whitelist. Chỉ lấy nguồn live đã kiểm tra chính sách và endpoint.

**Bằng chứng:** chạy thủ công 2 lần, số bài mới lần thứ hai bằng 0 (nếu input không đổi), `ingestion_runs` có counters đúng; một source lỗi vẫn giữ kết quả source khác; không có payload HTML độc hại đi vào prompt quyền cao.

**Nguồn thực hành:** [GitHub REST releases](https://docs.github.com/en/rest/releases/releases), [OpenAI API changelog](https://developers.openai.com/api/docs/changelog), [Gemini API release notes](https://ai.google.dev/gemini-api/docs/changelog), [Hugging Face Papers](https://huggingface.co/papers/trending).

---

### BỔ SUNG V3 — GIAO BÀI THEO CHUẨN NGHIỆM THU

**Năng lực được kiểm chứng:** RSS/official APIs, attribution/licensing, allowlist, canonical URL, exact/semantic dedupe.

**Lý thuyết phải tự giải thích được:** Không scrape paywalls; GitHub Releases != git tags; rate limits 403/429.

**Bài thực hành bổ sung:** Batch sample 20 real items with metadata, no invented content; flaky feed failure.

**Đầu ra xác định:** At least 3 working source adapters and fixture tests. Từng artifact cần có owner, đường dẫn, trạng thái DRAFT/REVIEWED và liên kết với tiêu chí acceptance trong docs/TRACEABILITY_MATRIX.md.

**Negative testing:** Check duplicate rerun creates zero extra source items.

**Chu trình học:** 30–50 phút đọc official docs → 20 phút tự diễn đạt lại nguyên lý → 90–120 phút giao prompt cho Claude Code → 30–60 phút kiểm chứng file/diff/log → ghi learning log và phản biện. Nếu service mới phát sinh tiền, cần bạn cho phép trước.

**Rubric ngày 10 (10 điểm; cần ≥9 và không có blocker):** lý thuyết 2; chất lượng prompt và phạm vi 2; đầu ra đúng schema/file 2; tests có bằng chứng 2; bảo mật/nguồn và đánh giá rủi ro 2. Nếu thiếu bằng chứng test: tối đa 6/10, không được tự báo PASS.

**DoD:** Kiểm tra đủ file, evidence, test và quyền hạn; blocker còn tồn tại thì status=FAIL hoặc SKIP.

**Self-check:** Nếu agent nói “đã làm xong”, yêu cầu nó trả: danh sách file tạo/sửa, test command và exit code, 3 rủi ro còn lại, ảnh/URL/log nếu có, lý do mọi bài test bị skip, và trạng thái chưa xác minh.
