# PRD — DevAI Atlas v1.0 (AI Developer Knowledge Hub)

## Problem & audience
Developers thiếu hệ thống AI kiến thức đáng tin có phân cấp và cập nhật. Technical leader cần biết cập nhật nào tác động tới code/chi phí/bảo mật và cần đưa vào sprint.

## Product goals
G1: Thư viện 18 tracks / 144 module syllabus, ít nhất sáu seed lessons được editor duyệt có lý thuyết, lab, lời giải, nguồn. G2: news ingestion 3+ allowed sources; hằng ngày đề xuất draft + có provenance, no fake news. G3: Admin manage sources/editorial/runs; RBAC. G4: mobile SEO, search, privacy. G5: operational evidence, cost cap, rollback.

## Non-goals trong 14 ngày
Không tự viết đủ 144 modules, không prometheus-grade high-scale, không tự huấn luyện LLM, không autonomous high-impact publishing, không đa tenant billing, không full market prediction/stock advice, không tải tràn lan/copy trang bên thứ ba.

## Personas
- New developer: bắt đầu tracks, đọc lesson/quiz, tìm theo keyword.
- Senior/leader: tra API changes, so sánh provider, xem implication và nguồn.
- Editor: duyệt/sửa bài, minh bạch claim và bằng chứng.
- Admin: thay registry, schedules, permissions, quality, usage.

## User journeys
U1 public Home→/learn→track→lesson→quiz→official docs; U2 Home→/news→detail→original release; U3 /search keyword→lesson/post published; U4 editor login→draft→review→publish→audit; U5 admin→source registry→Run now→run status→errors; U6 user question→retrieval approved only→answer cited or abstain.

## Requirements with IDs
- R-01: 18 track pages; no broken nav; 6 lessons fully drafted and reviewed before publication.
- R-02: Lesson contains objectives, prereq, glossary, theory, example, exercise, worked answer, five quiz answers, references, verified_at.
- R-03: News list/details include source canonical URL, source_date, discovered_at, verified_at, changes, dev impact, confidence, uncertainty.
- R-04: Sources include allowed metadata and compliance status; at least 3 live adapters after permissions review.
- R-05: Normalize/canonicalize/dedupe; replay must not duplicate.
- R-06: Schema checked NewsDraft with claim evidence and review_required; never invent facts.
- R-07: HIGH risk security/pricing/breaking/deprecation/rumor waits for editor approval; no direct model publish.
- R-08: Schedule daily 07:00 VN, manual replay, bounded retry, run ID/status and error trace.
- R-09: Auth, strict authorization, RLS, no role self-escalation, server-only secrets.
- R-10: Search approved data; RAG P1 with citations and negative-case checks.
- R-11: CI tests/build, SEO and accessibility, security and budget policy.
- R-12: Staging/prod deployment with documented rollback, smoke, scheduled-run proof after real event.

## Acceptance and release gates
No public release when guest reads draft, fake source/claim, missing editor gate, exposed secrets, unauthorized admin mutation, unreviewed source licensing, unbounded costs, failed CI, absent rollback or non-functional daily jobs. A scheduled trigger configured is not an observed execution.

## Definition of Done
Use `docs/TRACEABILITY_MATRIX.md`, score only with independently reproducible evidence; verified_at applies to individual claims and capability docs. No blank placeholder pages masquerading as expert material.
