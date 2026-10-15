# Provider / product decision matrix — competency, not marketing rankings

| Surface | Definition | Use in curriculum | Use in deployed website | Critical check |
|---|---|---|---|---|
| Anthropic Claude Code | agentic coding environment | Primary implementation driver | Not required runtime | permissions, CLAUDE.md, skills/docs |
| Anthropic Claude API | model endpoint | tool use, summaries/evidence | optional provider | model+tool support, ToS/data handling |
| OpenAI (ChatGPT/Codex/API) | consumer Chat, coding and API surfaces separately | independent review / API engineering | optional provider | current API/model+schema behavior |
| Google Gemini | consumer Chat + API + coding tools | multimodal, research, verification | optional provider | Gemini API schema/function compatibility |
| DeepSeek | API and models | cost/performance evaluation | optional provider | strict output support, endpoint, policies |
| xAI Grok | API/model product | model comparison | optional provider | xAI docs and availability |
| GitHub Copilot | IDE/agentic coding product | code review/comparison | development tool only | plan vs features/permissions |
| GitHub Releases | developer platform/API (not model) | source for update tracking | tier-A verified repo adapter | version, publisher & rate limits |

Selection process: (1) list concrete tasks, (2) obtain current official capability matrix, (3) run same gold set, (4) record latency, grounded precision, cost, failure conditions, (5) document tradeoffs/lock-in/privacy, (6) choose per task and retain fallback. No blanket ‘best model’ claim without method, period and measured scores.
