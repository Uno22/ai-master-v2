# Source policy and market research integrity

## Allowed source classes
Primary official API/release notes/docs, first-party GitHub release for verified owner/repository, publisher RSS/API if ToS allows metadata processing, paper metadata with correct license and attribution. Do not assume robots.txt equals reuse permission.

## Before enabling an adapter
1. Verify canonical domain/owner/repo by browsing original provider page.
2. Check acceptable access mechanism, robots/terms/license, attribution required, copyright, rate limit and API auth.
3. Keep metadata-first ingestion and link to original, no full-text republishing; reject paywalls/prohibited scraping.
4. Record `license_checked_at`, registry owner, allowlisted host, max fetch frequency, TOS_URL, permitted_fields, data retention.
5. Label unsupported/no feed as MANUAL_ONLY. Avoid arbitrary user-supplied URL crawling.

## Source quality
Tier A primary official release/pricing/docs; Tier B respected news/peer-reviewed research; Tier C social/rumor. Pricing/security/model release/breaking claims from Tier B/C require Tier A confirmation or explicit unverified draft and human review. Papers may be unreviewed preprints; mark study limitations.

## Fact fidelity
Differentiate event date, published date, first discovered date, last checked date. Evidence can be permalink, paragraph identifier or API payload hash; a generic home page is insufficient. Sources with 404, modified terms, or license concerns must be disabled or quarantined. Weekly source registry audit after launch.
