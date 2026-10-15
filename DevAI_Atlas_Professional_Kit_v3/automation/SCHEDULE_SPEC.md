# Schedule contract

- Business time: 07:00 Asia/Ho_Chi_Minh daily.
- Inngest cron: `TZ=Asia/Ho_Chi_Minh 0 7 * * *` as shown by official timezone support; equivalent `0 0 * * *` UTC for Vietnam when timezone offset +07:00 no DST.
- Only one automated scheduler; separate `Run now` sends typed event and same DB dedupe protection.
- Run key scoped to day/time window + job version; concurrency lock and unique DB constraint.
- Persist started/finished/step status/counts/failed sources/cost/alert; avoid secrets in logs.
- Day 14 must distinguish schedule set `CONFIGURED`, manual replay `MANUAL_TESTED`, and real daily trigger `VERIFIED_DAILY_RUN`. Only third proves actual automatic run.
- On first failure notify admin; repeated failures pause high-impact publication. If provider time windows change, review cron and source rate limits.
