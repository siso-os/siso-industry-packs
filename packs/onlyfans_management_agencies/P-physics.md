# P Physics: the OFM agency broken down to its fundamentals

Shaan (11 Oct): "how would Elon Musk break down this industry to its core fundamentals so we can
leverage what people have made everywhere else". This is that breakdown. Every number carries
`[source]`, `[vendor]` or `[analysis]`; evidence from [T4](data/firm_anatomy.jsonl) (21 agencies
profiled) and [T5](T5-software.md).

## 1. What the business is, with the industry's words removed

A person has a scarce asset: other people want **intimate attention** from them. Fans pay for four
things: **access** (subscription), **personal attention** (messages, custom requests), **content
units** (pay-per-view) and **live presence** (streams, tips). The platform is a payment and hosting
rail that keeps 20% `[source: onlyfans.com/terms]`.

An agency rents the creator's likeness and time and runs the three machines a creator cannot run
alone, on top of two support systems:

| | Machine | Turns | Into |
|---|---|---|---|
| 1 | **Attention** (traffic) | free attention on Reddit, X, TikTok, IG, cam sites | paying fans |
| 2 | **Conversation** (the sales floor) | paying fans | spend, one-to-one, 24/7 |
| 3 | **Inventory** (content) | creator time, shoots, AI | units to sell |
| A | **Supply** (talent) | recruiters, referrals, inbound | creators under contract |
| B | **Trust** (money and safety) | platform payouts, contracts, leaks, ID | creator paid right, protected, kept |

Everything an agency does is one of these five. Every department in T4 maps onto them.

## 2. The equation

```
creator gross  G = fans × spend per fan
fans           = reach × follow→subscribe rate × months retained
spend per fan  = subscription + PPV + tips + customs (+ live tips on cam sites)
agency net     = G × 0.80 × share  −  (chat labour + traffic + content + tools + overhead)
```

- **Share** 25-65% of the creator's 80%, as published by the agencies themselves `[vendor, T4]`:
  Bunny 25-50%, Louna's 30-50%, SirenCY 35%, MANGO 50% of net, FantasyRise 30-60%, Lookstars 65%
  (reported). 13 of 21 do not publish a rate.
- **Labour is the cost.** 10 creators at 24/7 cover need ~10-30 chatters at $3-8/hour, i.e.
  $5k-40k/month `[analysis, T5]`; software is ~$600-700/month `[analysis, T5]`.
- **Staff per creator varies 17×**: Bunny ~0.28 (112 staff, 400 creators) vs Everlasting Eros ≥5
  `[vendor, T4]`. Two different businesses share one name: a volume factory and a boutique.

## 3. The atomic units and their "idiot index" (price ÷ cost of the raw input)

| Unit | Raw cost today | What it sells for | Index | What happens next |
|---|---|---|---|---|
| Chatter hour | $3-8 human `[source]`; cents for an AI draft | the spend it closes | very high | **Commoditises first.** AI chat vendors already sell it (Supercreator, Substy) |
| Content unit | shoot time; cents with AI image/video | PPV price | very high | Commoditises; fully synthetic "AI models" remove the creator from supply |
| Fan reached | labour + accounts; paid ads mostly barred for adult | a subscriber | medium | Stays a **skill**: distribution on platforms that resist it |
| Creator signed | recruiter time + trust | years of share | low (scarce) | **Stays scarce.** Supply is the bottleneck |
| Dollar held | ledger + payout rails | creator's trust | n/a | **Stays**: whoever pays creators right keeps them |

## 4. What is physics and what is convention

| Physics (stays true) | Convention (will break) |
|---|---|
| Fans pay for personal attention; attention must be manufactured at scale | That attention must be a $5/hour human in a 3-shift rota |
| Supply of willing, trusted creators is finite | That content must come from shoots |
| One platform can change its rules overnight | Single-platform agencies (21 of 21 profiled are OnlyFans-first; only 2 mention cam/streaming) |
| Money held for creators is a liability | Agencies hiding commission and paying from spreadsheets |
| Distribution compounds (owned audiences, live rooms) | Per-creator SaaS pricing (breaks past ~10 creators, SISO Aug research) |

## 5. The precedent: YouTube multi-channel networks (2012-2016)

Maker Studios, Fullscreen and Machinima signed thousands of creators for 20-50% of revenue,
sold for hundreds of millions, and faded once YouTube's own tools gave creators what the networks
sold `[analysis; to source in T7]`. Lesson for OFM: a share taken for services software can give
away (chat, scheduling, analytics) does not last. What lasts is the **supply relationship, the
distribution, and the money infrastructure**.

The second precedent is the **cam studio** (Colombia, Romania, 20+ years): physical studios,
shifts, monitors, per-model payroll, multi-site streaming. It is the closest operating model to
HALO's streaming arm and is unmapped in OFM research so far.

## 6. So what wins

`[analysis]` The agency that wins in five years:

1. Owns **supply** (a recruiter/referral network creators trust),
2. owns **distribution** across many platforms at once, live included,
3. runs **conversation and content as AI-assisted software**, humans as QA and closers,
4. runs **trust** (ledger, statements, payouts, contracts, leak protection) as infrastructure.

HALO already has 1 (recruiters), 2 (cross-streaming) and 4 (back office) in some form, and is
missing 3. Full mapping: [X-borrow-map.md](X-borrow-map.md).

## 7. What the industry is missing, from first principles

`[analysis]` Set the five machines against what the 21 profiled agencies and 50 tools actually
provide (T4, T5, R, A):

1. **A creator career, not a contract.** No profiled agency offers visible progression, tenure
   economics or referral tiers to creators; churn is the industry's tax. See [R](R-retention.md).
2. **Money people can see.** Most agencies hide the rate; none publish live per-creator
   statements. Trust is the cheapest retention lever and nobody pulls it.
3. **Consent and provenance per asset.** AI content is good enough for photos and voice, and the
   binding constraint is proof of consent. Nobody runs a consent ledger. See [A](A-ai-content.md).
4. **Multi-platform distribution.** 21 of 21 are OnlyFans-first; only 2 mention streaming. One
   policy change at one platform is an existential risk the industry ignores.
5. **A measured sales floor.** Vendors measure chatters; nobody connects chatter, fan, content
   unit and creator payout in one ledger, so nobody knows true margin per creator.
6. **Software priced for agencies, not per creator.** Every vendor charges per creator account,
   which punishes growth.

HALO already covers 4 (cross-streaming) and part of 1 and 2 (referral tracking, payroll,
contracts). The cheapest big wins are 1 and 2: point HALO's existing chatter gamification engine
at creators and put a ledger under the money.

## 8. Take-over physics: the five laws, and the loops that win

Shaan (12 Oct): "what are the fundamental core physics of the industry that we need to cover if
we want to take over the industry?" `[analysis]`

### The five laws

| Law | What it means | What you must own to win |
|---|---|---|
| **1. Money follows two power laws** | The top 1% of creators take ~33% of revenue; within each creator, a few fans (whales) make most of the spend, most of it in their first 48 hours | Sign creators *before* they are top (draft picks, not bidding wars); find and serve whales across every creator |
| **2. Supply is finite, perishable and trust-bound** | A creator's value to an agency = monthly take × months she stays. Careers are short; trust breaks once | Tenure: Creator Career, live statements, fair exits; and a supply pipe that refills itself (creators recruiting creators) |
| **3. Attention is rented, and the rails can switch off** | Traffic comes from Reddit, TikTok, X and IG, all hostile to adult content; OnlyFans owns the fan relationship; card networks are the real regulator (OnlyFans' 2021 ban attempt came from banks) | Multi-platform presence (fan platforms + cam sites + live), traffic as a real department, every fan relationship mirrored where terms allow |
| **4. The cost of personal attention is going to zero** | ~70% of revenue is conversation; AI drafts collapse chat cost; AI collapses content cost | An AI-assisted sales floor and content line, so the break-even creator drops from ~$5.6k to ~$2.4k a month |
| **5. What AI cannot fake becomes the scarce good** | Real person, real consent, real-time presence | Live streaming (2 of 21 top agencies offer it), proof of consent per asset, identity security, leak protection |

### Why nobody has taken over yet

No agency **compounds**. Each is a silo: its playbooks, fan data and traffic die with it, and
its creators can leave with nothing to lose. That is why the industry is 5,000-50,000 small
firms and agencies sell for ~2× profit.

### The three loops that make one firm compound

1. **Data loop:** more creators → more data on what sells, to whom, when → better AI drafts,
   pricing and content → more earnings per creator → more creators.
2. **Supply loop:** creators and recruiters in one capped referral tree → every creator signed is
   a recruiter → supply refills itself.
3. **Traffic loop:** an internal network of creators cross-promoting each other (in-house S4S)
   plus live rooms on many sites → attention generated inside the network, not rented outside it.

### Two routes in, best taken together

- **Be the operating system:** sell HALO's back office (ledger, statements, Creator Career,
  contracts, payroll, streaming, consent) to other agencies, priced per agency. No vendor sells
  it; every agency on it feeds the data loop.
- **Roll up:** agencies trade at ~2× annual profit `[vendor: broker listings]`. Buy the ones
  already running on the OS, lift their margin with AI chat and their value with retention, and
  the same profit is worth more inside a firm whose creators stay.
