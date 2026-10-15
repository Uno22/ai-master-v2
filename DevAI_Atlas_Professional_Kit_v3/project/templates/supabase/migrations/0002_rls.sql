-- DESIGN TEMPLATE. Enables deny-by-default RLS where no policies exist.
-- Privileged mutations must occur via a trusted server verifying admin/editor + revision.
alter table public.news_sources enable row level security;
alter table public.source_items enable row level security;
alter table public.news_clusters enable row level security;
alter table public.cluster_members enable row level security;
alter table public.news_posts enable row level security;
alter table public.post_sources enable row level security;
alter table public.ingestion_runs enable row level security;
alter table public.editorial_reviews enable row level security;
alter table public.profiles enable row level security;
alter table public.reading_progress enable row level security;
alter table public.bookmarks enable row level security;
alter table public.ai_usage enable row level security;
alter table public.audit_log enable row level security;

create policy "published_posts_public_read" on public.news_posts for select to anon,authenticated using (status='PUBLISHED');
create policy "profiles_owner_read" on public.profiles for select to authenticated using (id=(select auth.uid()));
-- Do not create a profiles UPDATE policy for self; role must never be self-assignable.
create policy "progress_owner_read" on public.reading_progress for select to authenticated using (user_id=(select auth.uid()));
create policy "progress_owner_write" on public.reading_progress for insert to authenticated with check (user_id=(select auth.uid()));
create policy "progress_owner_update" on public.reading_progress for update to authenticated using (user_id=(select auth.uid())) with check (user_id=(select auth.uid()));
create policy "bookmarks_owner_read" on public.bookmarks for select to authenticated using (user_id=(select auth.uid()));
create policy "bookmarks_owner_write" on public.bookmarks for insert to authenticated with check (user_id=(select auth.uid()));
create policy "bookmarks_owner_delete" on public.bookmarks for delete to authenticated using (user_id=(select auth.uid()));
-- Source metadata public exposure belongs in explicit safe read-only view or server select;
-- drafts/run/evidence/audit should not have public policies.
