# Cost model, capacity and fail controls

Costs: coding tool seat separate from deployed AI provider API; provider input/output tokens, source subscriptions, embeddings, database, workflow execution, Vercel hosting, logging, domain. No fixed 2026 prices here: retrieve each official provider pricing page before estimate.

Formula: `daily = sum((input_tokens*input_rate)+(output_tokens*output_rate)+tool/search/fetch+embeddings) + retries`; monthly = actual daily runs + user RAG usage + fixed infrastructure, with 30-day assumption stated. Track cost per approved article and per answered question. Budgets example (CONFIGURE, NOT CLAIM): daily provider cost soft alarm at 70%, hard stop at 100%, max 50 fetched items/source/run, max 3 retries, max 2 writer attempts/item, max user queries/min according to service plan.

Capacity: use FTS+CDN static cache first, block unbounded RAG and crawling; verify p95, QPS, error budget and storage, then scale. ‘Many users’ ≠ ‘million concurrent’. Load test with granted staging budget and record reproduction environment/DB size.
