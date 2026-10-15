# Model routing and API capability matrix

Do not hardcode model ID in curriculum. Deployment owner verifies current IDs, API paths, provider ToS, pricing, tool/JSON support, input/output limits from official docs and pins them in environment policy and config reviewed in PR.

| Operation | Quality requirement | Fallback | Human gate |
|---|---|---|---|
| Classify topic | cheap, stable schema | deterministic rule + review | unusual case |
| Draft Vietnamese summary | grounded synthesis | alternate enabled model with eval proof | high-impact |
| Verify claims | source-based independent reviewer | human only if provider down | yes high-impact |
| RAG answer | citation & abstention | keyword search/read-only | none for public allowed data |
| Coding source development | diff and test results | another agent independent review | before merge |

Use per-task measured eval scores, timeouts, data handling, latency, token caps and budget. Fallback must use verified capability; price compare from current pricing page, no promise “best” from marketing alone. Trace provider/model ID, prompt version, usage/cost estimates, but NEVER log confidential raw prompts or secrets.
