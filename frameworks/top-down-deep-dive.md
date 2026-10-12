# Industry top-down deep dive

A reusable method for researching an **agency industry** from the top down: count every firm on
the planet, find the top 1%, take each one apart, and rebuild the agency from first principles.

It sits **beside** the seven-stage pack in the [README](../README.md), not instead of it. The
seven-stage pack studies one operator and the software they need; the top-down dive studies the
whole population of firms and what separates the best. A pack run through both has stages
`00-06` (seven-stage) and `T0-T8` plus `C` (top-down) in the same folder.

First run: [`packs/onlyfans_management_agencies/`](../packs/onlyfans_management_agencies/)
(11 Oct 2026, from Shaan's brief in `.agents/source/2026-10-11-shaan-ofm-deep-dive.md`).

## Rules

- Public business information only. No individual's personal data, nothing behind a login,
  never contact a firm or anyone on the researcher's behalf.
- Every number carries its source URL, its date and a label: `[source]` (stated by someone
  else), `[vendor]` (a firm's claim about itself), `[analysis]` (our arithmetic or judgement).
- Firm claims are claims. "Top agency" lists are often paid placements; treat them as signals,
  never as proof.
- Data first: every firm, tool and signal is a row in a `.jsonl` file. The prose files are
  readings of the data, not the data.

## Build on what exists first

Before any fresh search, read the estate's earlier research on the industry with reader
agents, list what was already known, and re-verify each old claim (CONFIRMED / CHANGED /
UNVERIFIABLE) before it enters a data file. Record the prior sources in `T0-prior-research.md`.

## Passes (from SISO's top-1,000 industries method)

The ranking borrows the shape of `SISO_Agency/hq/industries/TOP-1000-METHOD.md` (t-0486):

1. **Counts by script, free:** directories, registries, job boards, GitHub search, as data.
2. **Scores by reader agents, one pass:** every firm gets the rubric scores, each with a source.
3. **Hand pass on the top tier:** re-score the top rows one at a time with a one-line basis;
   hand rows override pass 2.
4. **Deep pass on the top 25:** full anatomy from published sources.

Scores use logs (`log10(x+1)`) for size signals so one huge firm cannot drown the rest, and
the page shows the formula next to the result.

## Order: the ocean before the iceberg

Shaan (11 Oct): "you're just mapping out the tip of the iceberg ... how we actually map out the
whole ocean". Run **P and X first** (the physics and the borrow map are the lens), the census by
**enumeration** (below), then the firms. Profiling famous firms is the tip; the machines, the
whole population and the borrowed solutions are the ocean.

## The stages

| Stage | File | Question | Done when |
|---|---|---|---|
| T0 Prior research | `T0-prior-research.md` | What did we already know? | Every earlier estate source listed, old claims re-verified |
| C Home case | `C-case-<firm>.md` | How is the client's own firm built, on the same fields as T4? | The client mapped as a firm (business level only, no code, no personal data); used as the yardstick in T7 and T8 |
| P Physics | `P-physics.md` | What is the business with the industry's words removed: its machines, its equation, its atomic units, what is physics and what is convention? | Every department of every firm maps onto the machines; each atomic unit has a raw cost and a price |
| X Borrow map | `X-borrow-map.md` | For each moving piece, which other industry solved it best, with what tools and what open source, and where the home case stands? | Every piece of P has a source industry, a tool, an OSS candidate and a home-case status |
| Owner lanes | `R-*.md`, `A-*.md`, `S-*.md` … | The deep questions the owner cares about most (for OFM: creator retention, AI content, SaaS we can replace) | Each answered with data files, HALO-style home-case status and a design, not just a survey |
| T1 Census | `T1-census.md` + `data/census_signals.jsonl` | How many firms exist on the planet? | A low and a high estimate, each from **at least three independent methods**, every input sourced |
| T2 Ecosystem | `T2-ecosystem.md` + `data/ecosystem_*.jsonl` | What grows around the firms: communities, courses, job boards, marketplaces, vendors, events? | Every surface mapped with its size and what can be pulled from it; feeds the census (T1) and the candidate list (T3) |
| T3 Top 1% | `T3-top-firms.md` + `data/firms.jsonl` | Who are the top 1%, and how do we know? | A ranked list of at least `max(25, 1% of the high census)` firms, each scored on the evidence rubric below |
| T4 Anatomy | `T4-anatomy.md` + `data/firm_anatomy.jsonl` | How is each top firm built and run? | The top 25 profiled on the anatomy fields below, gaps marked `unknown`, never guessed; the rest of the ranked list carries scores only |
| T5 Software | `T5-software.md` + `data/tools.jsonl` | What does the industry run on? | Every tool seen, by category, with price, what it does and which firms use it |
| T6 Open source | `T6-open-source.md` + `data/oss.jsonl` | What exists free on GitHub and in public datasets? | Repos, scrapers, datasets and models per function; each marked ALREADY IN THE BANK or NEW |
| T7 Analysis | `T7-analysis.md` | What do the top 1% do that the rest (and the home case) don't? | Each claim backed by counts from the jsonl files (top-tier vs the rest) |
| T8 First principles | `T8-first-principles.md` | If we built this agency from zero, what are all the moving pieces and what software would we build? | The org, the unit economics, the operating loop and a build list, each traced to T4-T7 evidence and set against the home case |

### T1 Census: at least three independent methods

Each method gives its own low/high; the final estimate is the range they agree on, with the
disagreement explained.

1. **Top-down market math.** Platform-reported creators/customers and revenue → the share
   worth managing → the share actually managed → divided by average roster size.
2. **Software-vendor signals.** Specialist tools publish "used by N agencies" claims. Take the
   largest, correct for overlap and inflation.
3. **Bottom-up public lists.** Directories, rankings, company registries (UK Companies House
   and others searchable without login), public LinkedIn company pages. Dedupe by name/domain.
4. **Labour signals.** Open job posts for the industry's signature roles, distinct employers,
   staffing ratios → implied firm count.
5. **Community signals.** Size of founder communities and courses that produce firms.

**Map the ocean by enumeration, not samples.** Lists and rankings only show the visible firms.
Enumerate every source that touches every firm, then estimate the unseen:

| Enumerator | What it lists | Access |
|---|---|---|
| Certificate-transparency logs (crt.sh) and domain zone data | every domain whose name carries the trade's words | public, rate-limited |
| Common Crawl index | every crawled page using the trade's phrases → distinct domains | public, bulk |
| Company registries in bulk (UK Companies House, OpenCorporates) | every entity by name and activity code | public downloads |
| Places data (Overture, as in the top-1,000 method) | every listed premises in the category | public |
| Job posts over 12 months | every distinct employer hiring the signature role | public boards |
| Vendor customer pages, ecosystem directories (T2) | firms named as customers or members | public |

Then estimate the population including firms no source caught, using **capture-recapture**
across independent lists (Lincoln-Petersen `N ≈ n1 × n2 / overlap`, or Chao1 for many lists).
Lists built from each other (a ranking copied from a directory) are not independent.

Separate **all firms** (including one-person operations) from **operating firms** (a
registered entity, a website and paid staff). The top 1% is taken from the high estimate of
all firms, which keeps the bar honest.

### T2 Ecosystem: work backwards from where the firms gather

Firms in a young industry cluster around shared surfaces. Map each from public pages only
(directory listings, public channel previews, stats sites, public listings); never join a
private group, log in or contact anyone.

| Surface | Examples of what to log |
|---|---|
| Communities | Discord servers and Telegram channels for operators, staff hiring, training, client recruiting, promotion exchanges (member counts from public directories) |
| Education | Courses and gurus: price, claimed students, claimed firms launched |
| Labour | Job boards, staffing/outsourcing firms, training/certification |
| Supply | Client-recruiting marketplaces, directories, review sites |
| Demand | Promotion, traffic and ad services the firms buy for their clients |
| Vendors | Software, content production, AI generation, finance, legal, takedown services |
| Capital | Firm-for-sale listings (asking price, revenue, clients) |
| Media | Events, newsletters, podcasts, YouTube channels |

Two outputs: (1) census inputs (a course claiming N firms launched, a server of N owners);
(2) a "what can be pulled" list: public SOPs, templates, price lists, job posts and listings
that become data for T4-T5.

### T3 Top 1%: evidence rubric

Score each candidate 0-3 on each line; rank by total, ties broken by revenue evidence.

| Signal | Evidence that counts |
|---|---|
| Revenue / GMV | Registry accounts, press with figures, the firm's own figures (`[vendor]`, weighted down) |
| Scale | Clients managed, staff count (LinkedIn headcount band, job posts), offices |
| Hiring | Open roles now, countries hired in, seniority of roles |
| Reputation | Independent press, appearance across many unpaid lists, practitioner mentions |
| Longevity | Years operating, registry incorporation date |
| Footprint | Web traffic (public estimates), social following of the firm itself |

### T4 Anatomy fields (per firm)

`departments`, `org_chart`, `roles` (with shifts and locations), `pay` (by role, as published
in job posts), `offer` (services sold), `pricing` (rev share, retainers, tiers), `contract_terms`
(length, exit, exclusivity, as published), `client_acquisition` (how they win clients),
`traffic_acquisition` (how they win customers for the clients), `tools`, `geography`,
`founded`, `entity`, `sources`.

### T7 Analysis: the comparison

For every anatomy field and tool category, count how often it appears in the top tier vs the
rest of the sampled population. Report differences larger than 20 percentage points as
findings, smaller ones as noise. Name the sample sizes.

### T8 First principles

1. The job to be done for the client and for the end customer, stated without the industry's
   own vocabulary.
2. The unit economics: revenue per client, cost per client (labour, tools, acquisition),
   margin, the break-even roster.
3. Every moving piece: departments, roles, handoffs, the daily/weekly loop, the data each
   step makes.
4. What to keep from the top 1%, what to drop, what nobody does yet.
5. The software we would build: per moving piece, lift (OSS from T6), buy (from T5) or build,
   and why.

## Data files

All in `packs/<slug>/data/`, one JSON object per line, UTF-8.

| File | One row per | Required keys |
|---|---|---|
| `census_signals.jsonl` | A number that feeds the census | `method`, `metric`, `value`, `unit`, `date`, `url`, `label` |
| `firms.jsonl` | A firm (any tier) | `id`, `name`, `domain`, `country`, `tier` (`top`/`rest`), `score`, `signals`, `sources` |
| `firm_anatomy.jsonl` | A top firm's profile | `firm_id` + the T4 fields |
| `ecosystem_communities.jsonl` | A Discord/Telegram community | `id`, `name`, `platform`, `url`, `members`, `purpose`, `what_could_be_pulled`, `sources` |
| `ecosystem_web.jsonl` | A website, course, board, vendor or listing | `id`, `name`, `url`, `kind`, `audience_size`, `price`, `claims`, `what_could_be_pulled`, `sources` |
| `tools.jsonl` | A software tool | `name`, `category`, `url`, `price`, `price_unit`, `does`, `used_by` (firm ids), `sources` |
| `oss.jsonl` | A repo / dataset / scraper | `repo`, `url`, `function`, `licence`, `stars`, `last_commit`, `bank_status`, `verdict` |

## Quotas (top-down)

| | Minimum |
|---|---|
| Independent census methods | **3** |
| Firms in `firms.jsonl` | **100** |
| Ecosystem surfaces mapped in T2 | **100** |
| Top-tier firms profiled in T4 | **25** (or 1% of the high census, whichever is larger, if evidence allows) |
| Tools in `tools.jsonl` | **40** |
| OSS repos / datasets examined | **100** (the seven-stage quota, shared) |
