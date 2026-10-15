# ADR-0001: lessons in version-controlled Markdown, news in Postgres

Status: ACCEPTED AS DESIGN; implementation unverified. Context: evergreen lessons have slow editorial cycles, daily news rapid revisions. Decision: trusted locally committed Markdown/MDX for approved lessons with Git review; Postgres stores dynamic news, source and audit. Avoid evaluating arbitrary external MDX and hidden bulk generated content. Consequences: publishing lessons requires CI/deploy (acceptable MVP), news publishing needs auth/transactions. Revisit when content editing team needs independent CMS.
