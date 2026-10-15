-- DESIGN TEMPLATE. Review/test in local Supabase before applying; not production-ready by mere presence.
create extension if not exists pgcrypto;
create table if not exists public.news_sources (
 id uuid primary key default gen_random_uuid(), name text not null, source_tier text not null check(source_tier in ('A','B','C')),
 kind text not null check(kind in ('RSS','GITHUB_RELEASES','OFFICIAL_API')), endpoint text not null,
 canonical_site text not null, usage_policy text not null, enabled boolean not null default false,
 last_checked_at timestamptz, created_at timestamptz not null default now());
create table if not exists public.source_items (
 id uuid primary key default gen_random_uuid(), source_id uuid not null references public.news_sources(id), external_id text not null,
 canonical_url text not null, title text not null, source_published_at timestamptz not null,
 discovered_at timestamptz not null default now(), metadata jsonb not null default '{}'::jsonb,
 unique(source_id,external_id), unique(source_id,canonical_url));
create table if not exists public.news_clusters (
 id uuid primary key default gen_random_uuid(), fingerprint text not null unique, topic text, first_seen_at timestamptz not null default now());
create table if not exists public.cluster_members (
 cluster_id uuid not null references public.news_clusters(id), source_item_id uuid not null references public.source_items(id), primary key(cluster_id,source_item_id));
create table if not exists public.news_posts (
 id uuid primary key default gen_random_uuid(), cluster_id uuid references public.news_clusters(id), slug text unique not null,
 title_vi text not null, summary_vi text not null, dev_impact text not null default '',
 status text not null default 'DRAFT' check(status in ('DRAFT','IN_REVIEW','REJECTED','APPROVED','PUBLISHED','QUARANTINED')),
 risk text not null default 'HIGH' check(risk in ('LOW','MEDIUM','HIGH')),
 confidence text not null default 'LOW', review_required boolean not null default true,
 revision integer not null default 1 check(revision>0), source_published_at timestamptz,
 verified_at timestamptz, published_at timestamptz, created_at timestamptz not null default now());
create table if not exists public.post_sources (
 post_id uuid not null references public.news_posts(id), item_id uuid not null references public.source_items(id),
 claim_id text not null, primary key(post_id,item_id,claim_id));
create table if not exists public.ingestion_runs (
 id uuid primary key default gen_random_uuid(), run_key text unique not null, status text not null default 'RUNNING',
 triggered_by text not null, fetched_count integer not null default 0, duplicate_count integer not null default 0,
 drafted_count integer not null default 0, published_count integer not null default 0,
 error_count integer not null default 0, cost_estimate_usd numeric(14,6) not null default 0,
 started_at timestamptz not null default now(), finished_at timestamptz);
create table if not exists public.editorial_reviews (
 id uuid primary key default gen_random_uuid(), post_id uuid not null references public.news_posts(id),
 reviewer_id uuid not null references auth.users(id), revision integer not null,
 decision text not null check(decision in ('APPROVE','REJECT','NEEDS_CHANGES')),
 reason text not null, reviewed_at timestamptz not null default now());
create table if not exists public.profiles (
 id uuid primary key references auth.users(id) on delete cascade,
 role text not null default 'USER' check(role in ('USER','EDITOR','ADMIN')), created_at timestamptz not null default now());
create table if not exists public.reading_progress (
 user_id uuid not null references auth.users(id) on delete cascade, lesson_slug text not null,
 progress_status text not null default 'NEW', updated_at timestamptz not null default now(), primary key(user_id,lesson_slug));
create table if not exists public.bookmarks (
 user_id uuid not null references auth.users(id) on delete cascade,
 target_type text not null, target_id text not null, primary key(user_id,target_type,target_id));
create table if not exists public.ai_usage (
 id uuid primary key default gen_random_uuid(), operation text not null,
 provider text not null, model text not null, token_in integer not null default 0, token_out integer not null default 0,
 cost_estimate_usd numeric(14,6) not null default 0, run_id uuid references public.ingestion_runs(id), created_at timestamptz not null default now());
create table if not exists public.audit_log (
 id uuid primary key default gen_random_uuid(), actor_id uuid, action text not null,
 target_id text not null, metadata jsonb not null default '{}'::jsonb, occurred_at timestamptz not null default now());
