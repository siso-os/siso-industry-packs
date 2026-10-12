# T2 Ecosystem: what grows around OFM agencies

**First pass, 11 Oct 2026.** Public pages only (directory listings, public Telegram previews,
stats sites, public listings); no group joined, nothing behind a login, no one contacted.
Data: [`data/ecosystem_communities.jsonl`](data/ecosystem_communities.jsonl) (61 communities),
[`data/ecosystem_web.jsonl`](data/ecosystem_web.jsonl) (80 web surfaces). Quota 100: **141 mapped**.

## The map

| Surface | What exists | Biggest seen | What we can pull |
|---|---|---|---|
| Promotion / S4S | 13 Telegram shoutout and "drop" exchanges; Fiverr shoutout sellers | 12k members (Boost OnlyFans) | Prices per shoutout, promo formats, which platforms drive traffic |
| Chatter labour | 7 hiring channels + OFM job boards (Sirency, Swooped) | 8.7k (OFM Moguls Jobs & Hires) | Pay rates, shift patterns, role definitions from public job posts |
| Operators | Masterminds and owner groups on Telegram, Discord, Skool | 2-3k per real operator group | Public SOP excerpts, recurring pain points |
| Education | 18 courses: Gumroad guides $10-995, OFM University $99/month, €499 agency editions | VIP groups of 900+ "agency owners" | Their curricula = the industry's own playbook of departments and steps |
| Vendors | Supercreator, Infloww, OnlyMonster, Substy, FansBot communities | Supercreator claims 25k creators/agencies | Feature lists, pricing, what operators ask for |
| Traffic | TikTok/IG trend groups; link-in-bio tools (LinkForFans, Direct.me $15/mo, UniLink, Beacons) | 5.3k (FBA TikTok Trends) | Tracking-link and funnel patterns |
| AI content | AI-model generators sold to agencies (JustModels.AI), "OFM AI" clubs | small (≈150 members) | Early: how agencies plan AI models; ties to HALO's content-generation plan |
| Protection | Leak removal / DMCA firms (LeakStop, Remove.Tech, BranditScan) | n/a | Service tiers, agency pricing |
| Capital | Flippa OFM agency listings; Acquire.com | One listing: $1.3M+/year revenue claimed | Asking multiples, revenue per creator, staff, tools (listing claims) |
| Media and events | 11 newsletters, 3 podcasts, XBIZ, Free Speech Coalition events | n/a | Industry news, who the visible operators are |

## Read with care

1. **Sizes that are not OFM operators.** BlackHatWorld's 1M is the whole forum; r/onlyfansadvice
   (558k) is mostly creators; one 140k Discord looks like a content server. Flagged in the data
   (`review_flag`), excluded from the analysis below.
2. **Every "best agency / best tool" page is vendor-authored**, and course claims are marketing.

## What it says about the census

`[analysis]` Real operator-only groups sit at 1k-9k members; the biggest hiring channel is 8.7k;
course VIP groups claim 900+ owners each across 18+ courses. Course buyers and group members
overlap heavily, and many never run an agency. That supports **several thousand to low tens of
thousands of people who have tried to start an agency**, consistent with the 5,000-50,000 range
in [T1](T1-census.md), and it makes the solo-and-dead long tail visible. Sirency's 2026 claim of
"500+ agencies actively recruiting" `[vendor]` matches T1's operating-firm band.

## Next pulls (for T4-T5)

1. Public chatter job posts → `pay`, `roles`, `shifts` for named agencies.
2. Course curricula (public sales pages) → the department list the industry teaches itself.
3. Flippa listings → revenue per creator, margin, staff and tool stacks as sellers state them.
4. Vendor pricing pages → `tools.jsonl`.
