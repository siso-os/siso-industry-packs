# T1 Census: how many OFM agencies exist

**Second estimate, 11 Oct 2026** (high end raised after Shaan's read; see below). Four methods run by Haiku research agents the same day; inputs
in [`data/census_signals.jsonl`](data/census_signals.jsonl). Not yet second-read; every number
below is `[source]`, `[vendor]` or `[analysis]`.

## The answer

| Population | Low | High | What counts |
|---|---:|---:|---|
| **Operating agencies** | **1,000** | **3,000** | A website, staff beyond the founder, more than one creator |
| **All "agencies"** | **5,000** | **50,000** | Anything selling OFM management, including one-person and part-time operations, on any fan platform |
| Top 1% of the high | | **~500** | The ranked list in T3 |

`[analysis]` The industry is a long tail: a few hundred real firms, a few thousand small teams,
and many thousands of solo "managers". Only 19% of directory-listed agencies publish a legal
entity and 6% publish their rates `[source: Desirely, Aug 2026]`, so most firms are invisible to
registries, which is why bottom-up counts come out low.

## Method by method

| Method | Low | High | Key inputs |
|---|---:|---:|---|
| 1. Top-down market math | 1,600 | 36,000 | OnlyFans FY2024: 4.6M creator accounts, $7.2B gross `[source: Fenix accounts]`. Creators worth managing (≥ ~$1k/month): 100k-300k `[analysis]`. Share managed 20-50% `[analysis]`; +20% for Fansly/Fanvue. Average roster 15 (low) to 5 (high) |
| 2. Software-vendor signals | 1,500 | 25,000 | Infloww claims 5,000+ agency customers, CreatorHero 891+, Substy 200+ (all `[vendor]`; Infloww also counts solo managers); OnlyFinder claims 80 of the top 100 agencies `[vendor]`, implying ~100 firms everyone agrees are major. Weakest method: few vendors publish an agency count |
| 3. Bottom-up public lists | 200 | 600 | Desirely directory: 431 listed, 248 full profiles `[source]`. UK Companies House shows almost no firms naming the trade `[source]`. This is the public-facing floor, not the total |
| 4. Labour signals | 500 | 5,000+ | Phoenix Creators: 5,000+ entities claim agency status, ~60% solo `[vendor]`. 3 chatters per creator for 24/7 cover; chatters $3-8/h + PPV commission `[source]` |

### Method 1 worked

- Low: 100,000 manageable creators × 20% managed × 1.2 platforms = 24,000 managed ÷ 15 per
  agency = **1,600**.
- High: 300,000 × 50% × 1.2 = 180,000 managed ÷ 5 per agency = **36,000**.

`[analysis]` The two weak links are the share managed (a "30% of creators use agencies" figure
circulates without a primary source) and the average roster. T2/T3 will replace both with
counts from the firms we profile.

## Why the high end is 50,000

Shaan (11 Oct): "there's definitely more than 1 to 3,000, I'd say this goes to like 50,000".
`[analysis]` The data supports that as the **high** for all agencies, not as the central case:

- Method 1's high is already 36,000 using OnlyFans + 20% for other platforms. Fansly alone
  reports ~3.2M creator accounts (unsourced so far); weighting it nearer OnlyFans, plus Fanvue
  and AI-model operations, moves the high to ~45,000-55,000.
- Infloww alone claims 5,000+ agency customers; vendors only see the firms that pay for
  software, and solo managers mostly do not.
- Courses and communities (T2) sell "start your OFM agency" at scale; their claimed student
  counts are the check on this number and are being collected now.

The framework takes the top 1% from the **high** estimate, so the ranked list grows from ~200 to
~500 firms; T4 still profiles the top 25 in depth.

## Earlier reasoning (first estimate)

Methods 1 and 4 agreed on **5,000-20,000** for all agencies once the solo share is applied;
methods 2 and 3 agree on **1,000-3,000** for operating firms (431 public-facing × 2-7 for the
ones that do not list). The outliers (36,000 and 200) rest on the two weakest inputs.

## Open

1. Re-read Fenix FY2024 accounts directly for creator accounts and payouts.
2. Source the creator earnings distribution (share above $1k/month) from a primary dataset.
3. Pull per-vendor agency counts from Infloww, Supercreator, CreatorHero and OnlyMonster pages.
4. Dedupe Desirely + ranking lists + LinkedIn into `data/firms.jsonl` (T3).
5. Turn T2 ecosystem sizes (course students, community members) into a fifth census method.

## Ocean enumeration: first attempt, 11 Oct 2026 (then parked)

| Enumerator | Result |
|---|---|
| crt.sh certificate logs | BLOCKED: 502 on every query (retried twice by hand) |
| domainsdb.info | BLOCKED: now needs an API key |
| UK Companies House + OpenCorporates search | 70 entities ([`data/ocean_registry_jobs.jsonl`](data/ocean_registry_jobs.jsonl)); some keywords 403 |
| Job boards (OnlineJobs.ph, Indeed, Jooble) | BLOCKED to plain fetches (JavaScript pages); retry through the camofox browser |

Parked by Shaan the same day: "It doesn't really matter if we get 50,000 agencies ... It's all the
peripheral research." The 5,000-50,000 range stands; effort moves to retention, AI content, OSS
and the SaaS we can replace.
