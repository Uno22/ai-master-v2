# PROMPT XỬ LÝ KHI AGENT LÀM SAI HOẶC TEST FAIL

```text
Stop feature work. Do not hide, delete, or override failing tests.
Provide (1) exact test command + exit code + redacted error,
(2) first observable failure and most likely 3 hypotheses,
(3) smallest reversible fix plan with affected files,
(4) regression test proving bug then fix,
(5) rollback and deployment impact.
Do not change unrelated files or schema. Ask approval before write.
If failure is secrets/service/config unavailable, mark BLOCKED and describe manual steps.
```
