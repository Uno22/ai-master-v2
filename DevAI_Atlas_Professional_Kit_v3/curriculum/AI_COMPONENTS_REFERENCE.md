# AI COMPONENTS REFERENCE — Applied AI Engineering

> 45 components. Đây là reference tóm tắt bổ sung cho 18 tracks, không thay cho 144 bài học chuyên sâu. Không học thuật toán training/gradient descent ở mức nghiên cứu.

| Thành phần | Nguyên lý | Ứng dụng DevAI Atlas |
|---|---|---|
| **AI / ML / Deep Learning** | AI là umbrella; ML học pattern từ dữ liệu; DL dùng neural networks | Không nhầm model AI với sản phẩm SaaS gọi model API. |
| **GenAI / Foundation Models** | Model tạo văn bản/ảnh/âm thanh mới trên patterns | Biết ranh giới model và runtime instructions. |
| **Tokens** | Đơn vị model xử lý; quyết định context, cost, latency | Gắn limit/cost trước khi chạy digest. |
| **Context Window** | Dung lượng thông tin trong một lượt model | Chunk release notes và truy xuất đúng đoạn. |
| **Hallucination** | Claim thiếu bằng chứng, dù câu trả lời nghe hợp lý | Reject fake pricing nếu không source. |
| **Prompt hierarchy** | Ranh giới system/developer/user vs untrusted material | Bài báo không thể yêu cầu agent tiết lộ API key. |
| **Few-shot examples** | Cặp input/output minh họa, phải giữ định dạng và quy tắc | Cho 2 tin PASS/FAIL để kiểm reviewer. |
| **Context engineering** | Quản lý ngữ cảnh, files, retrieved sources, memory, scope | Chỉ nạp docs liên quan ngày 11. |
| **Structured outputs** | Schema shape ràng buộc key/type; không tự xác minh semantic | Zod/JSON Schema pass rồi check evidence. |
| **Tool / function calling** | Model yêu cầu tool; backend kiểm quyền và chạy | Writer chỉ có tool đọc, publish do editor. |
| **MCP** | Giao thức hỗ trợ trao đổi tools, resources, prompts giữa clients/servers | Dùng MCP read-only với GitHub; không expose DB admin. |
| **Coding agents** | LLM + codebase tools + plan/edit/run/test loop | Claude Code tạo migrations với approval. |
| **Skills, hooks, subagents** | Skills=procedures; hooks=lifecycle reactions; subagent=role/worker | News-verifier skill + security reviewer agent. |
| **Deterministic workflow** | State machine/steps với behavior predictable | Fetch→normalize→dedupe→draft→review. |
| **Autonomous agent** | LLM tự chọn một số bước, rủi ro tool misuse | Research agent đề xuất query nhưng không tự publish. |
| **Prompt injection** | Instructions embedded in data/tool output to hijack model | RSS contains “ignore policy” and must be inert. |
| **RAG** | Retrieve relevant approved context before answering | Ask: cite lesson revision, otherwise abstain. |
| **Embeddings** | Vector biểu diễn tương đồng, không giải quyết accuracy tự động | Index approved knowledge chunks only. |
| **Chunking** | Cắt tài liệu để indexing/retrieval; mất ngữ cảnh khi sai | Chunk long changelog keeping heading/version info. |
| **FTS vs vector vs hybrid** | Keyword exact match vs semantic vs combination | FTS cho model ID/deprecation, vector cho câu hỏi khái niệm. |
| **Reranking** | Sắp lại retrieval candidates theo relevance | Tăng grounded citation precision khi đủ dữ liệu. |
| **Grounding & citations** | Claim phải map evidence thực sự supporting | Không dùng link root website thay cho changelog event. |
| **Evals** | Gold set + exact/task/source scoring + human adjudication | 20 news fixtures, 20 search questions. |
| **LLM-as-judge** | Evaluator model không phải chân lý; cần calibration | Judge may prefer fluent fabricated response. |
| **Multi-provider routing** | Chọn model bởi measured capabilities/cost/limits | Draft cheap candidate then stronger reviewer only if eval supports. |
| **Streaming** | Tokens đến dần, UX tốt nhưng partial validation | Do not stream unverified news to public page. |
| **Retries/backoff** | Giới hạn retry, phân biệt 429/5xx và non-retryable | Respect GitHub Retry-After / ratelimit. |
| **Idempotency** | Replay cùng event không tạo duplicate effect | Daily job run key + unique(source_id, external_id). |
| **Scheduling** | Cloud cron đúng timezone và observed execution proof | TZ=Asia/Ho_Chi_Minh 0 7 * * *. |
| **Queues/durable jobs** | Step-wise recovery và retry qua restart | Inngest stages resumed after provider outage. |
| **RBAC vs RLS** | Business role guard vs DB row policy | Guest cannot see draft even if API bug. |
| **SSRF** | Fetch arbitrary URL could access internal service | Allowlist, DNS IP validation and redirect checks. |
| **XSS/remote MDX** | Rendering untrusted executable markup nguy hiểm | Only trusted lessons as MDX, external RSS as escaped text. |
| **Data governance** | PII, retention, source rights, audit evidence | No company secrets in prompt/logs. |
| **Observability** | Traces/logs/metrics across each workflow step | Run ID links source→draft→review→post. |
| **Cost guardrails** | Tokens, tool costs, rate limits, per-task budgets | Hard stop when daily budget reached. |
| **SLO / error budget** | Measure real reliability instead of assertions | After deploy monitor uptime and failed run rate. |
| **Multimodal model** | Images/audio/video inputs; extraction & privacy risks | PDF extraction for tutorials with permitted source. |
| **Open-weight/local inference** | Self-host weights under license/hardware constraints | Only if privacy/cost requires, not model training. |
| **AI product design** | Workflow UX, trust, fallback, corrections | Clearly state news uncertainty and source time. |
| **Technical Leader AI** | Use AI to refine PRD/ADR/tickets/incident and reviews | Leader approves critical decisions, no silent business rules. |
| **Eval-driven development** | Ship after measured regression gates, not “model feels better” | Run same fixtures after provider switch. |
| **AI market intelligence** | Claims/release metadata over time, source tier and uncertainty | Trend requires counted events and time windows. |
| **Content versioning** | Editorial revision and update triggers, not live overwrite | Article version hash changes => re-review. |
| **Safety & human oversight** | Risk-based human approval for consequential actions | Security/deprecation/price changes require editor. |

## Cách học sâu một thành phần (không viết code tay)

1. Nêu định nghĩa bằng lời của bạn; phân biệt hai khái niệm dễ nhầm.
2. Đọc documentation sơ cấp + kiểm tra date/limits.
3. Tạo prompt giao Claude Code một case cụ thể của DevAI Atlas.
4. Yêu cầu runnable demonstration/diagram hoặc mock test, không chỉ một đoạn văn.
5. Cho AI khác phản biện bằng rubrics; audit claims, performance, security, cost.
6. Khi hiểu đúng, lưu note, fail case, decision tradeoff và update trigger vào module.

## Nguồn chính

- [Claude Code](https://code.claude.com/docs/en/overview)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code hooks](https://code.claude.com/docs/en/hooks-guide)
- [OpenAI tools](https://developers.openai.com/api/docs/guides/function-calling)
- [OpenAI structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
- [Gemini schema](https://ai.google.dev/gemini-api/docs/structured-output)
- [DeepSeek tools](https://api-docs.deepseek.com/guides/tool_calls/)
- [xAI Docs](https://docs.x.ai/)
- [GitHub Releases](https://docs.github.com/en/rest/releases/releases)
- [GitHub Rate limits](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api)
- [Next.js App Router](https://nextjs.org/docs/app)
- [Next.js MDX](https://nextjs.org/docs/app/guides/mdx)
- [Supabase RLS](https://supabase.com/docs/guides/database/postgres/row-level-security)
- [Inngest Scheduler](https://www.inngest.com/docs/durable-execution/guides-and-advanced/events-and-triggers/schedules-and-delayed-starts)
- [Vercel AI SDK](https://ai-sdk.dev/docs/introduction)
- [OWASP LLM risks](https://genai.owasp.org/llm-top-10/)
- [MCP](https://modelcontextprotocol.io/introduction)
- [GitHub Copilot](https://docs.github.com/en/copilot)
- [Gemini API](https://ai.google.dev/gemini-api/docs)
- [Anthropic tools](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview)
- [OpenAI API](https://developers.openai.com/api/docs)
