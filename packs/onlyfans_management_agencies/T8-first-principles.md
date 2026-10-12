# T8 First principles: rebuilding the agency from zero

The agency we would build if we started today, from the physics ([P](P-physics.md)), the
borrowed solutions ([X](X-borrow-map.md)), what the visible top does ([T7](T7-analysis.md)),
retention ([R](R-retention.md)), AI content ([A](A-ai-content.md)) and open source ([T6](T6-open-source.md)),
set against HALO ([C](C-case-halo.md)). Inputs: [`data/unit_economics.jsonl`](data/unit_economics.jsonl)
(59 numbers, mostly agency-blog figures, so read them as directional) and
[`data/precedents.jsonl`](data/precedents.jsonl) (cam studios, YouTube MCNs, esports, K-pop).

## 1. The money, per creator

```
agency revenue per creator = gross × 0.80 (platform keeps 20%) × share
```

| | Human chat floor | AI drafts + human closers |
|---|---:|---:|
| Chat cost per creator per month | $1,500 (offshore, $1.2-1.8k `[vendor]`) | ~$600 `[analysis: -60%]` |
| Tools per creator | ~$65 ([T5](T5-software.md)) | ~$65 |
| **Break-even creator gross** at a 35% share | **~$5,600/month** | **~$2,400/month** |
| Contribution at the "average managed creator" ($7,300 `[vendor]`) | $479 (23% of agency revenue) | $1,379 (67%) |

`[analysis]` Three consequences:

1. **The average managed creator barely pays for a human chat floor.** Agency profit comes
   from the top of the roster; the rest are carried. That is why agencies push 40-60% shares
   and lock-ins, and why creators leave.
2. **AI-assisted chat moves break-even from ~$5.6k to ~$2.4k a month.** On OnlyFans' own
   distribution (top 10% earn over $1k, top 1% over $10k `[source]`), that roughly **doubles to
   triples the number of creators worth managing**. AI does not just cut cost; it opens a market
   the industry cannot serve today.
3. **Agencies sell for about 2× annual profit `[vendor: broker listing]`** because the creators
   can walk. Retention is enterprise value: every year of expected creator tenure is worth more
   than any cost saving.

Revenue comes from conversation, not subscriptions: ~70% of platform revenue is DMs/PPV and
~4% subscriptions `[source: Sacra]`, and ~83% of a new fan's spend lands in the first 48 hours
`[analysis, vendor data]`. The sales floor is the factory.

## 2. The org, built from the five machines (sized for 30 creators)

| Machine | Roles | Ratio | Software does | Humans do |
|---|---|---|---|---|
| **Supply** | Recruiters (commission + referral tree), creator success managers, onboarding & compliance | 1 success manager per 10-15 creators | Pipeline, referral attribution, contracts, ID, renewal offers | Trust, relationship, the hard conversations |
| **Attention** | Traffic leads by platform (Reddit, TikTok, X, IG), streaming operators, shoutout buyer | 1 traffic lead per platform; 1 stream operator per live room | Scheduling, tracking links, trend detection, multistream | Taste, account health, community |
| **Conversation** | AI-assisted chat floor, closers per shift, QA lead, fan-data analyst | 1 closer per 5-8 creators per shift with AI drafts (vs 3-5 without) | Drafts, fan memory, whale alerts, attribution | Closing, judgement, boundaries |
| **Inventory** | Content producer, AI content operator, editor | 1 AI operator per 15-20 creators | Identity-consistent photo/voice, captioning, AI labels, consent check | Shoots, creative direction, final approval |
| **Trust** | Finance (ledger, statements, payouts, payroll), legal/DMCA, security | 1 finance lead; DMCA bought | Ledger, statements, payouts, leak scanning, credential vault | Disputes, takedown escalation, audits |

Plus one **owner view** across all five: margin per creator, per chatter, per traffic source.

## 3. The operating loop

- **Daily:** traffic posts → tracking links → new fans → first-48-hour sales sequence (AI draft,
  human close) → content units sold → every sale posts to the ledger.
- **Weekly:** creator quests and milestones paid ([R](R-retention.md)); chat QA review; traffic
  source scorecard; content plan from what sold.
- **Monthly:** creator statements (gross → platform → agency → creator, line by line); payouts;
  tier re-qualification; referral payouts; staff pay from the same ledger.
- **Quarterly:** renewal offers built from each creator's own numbers; platform-risk review
  (share of revenue per platform).

## 4. Keep, drop, invent

| Keep (the visible top does it) | Drop (convention) | Invent (nobody does it) |
|---|---|---|
| Chat floor + account management (19 and 15 of 21) | Hidden rates (14 of 21 hide them) | Creator Career: tiers, locked splits, referral tree |
| Leak protection as standard (14 of 21) | Long lock-ins without performance floors | Live per-creator statements from a real ledger |
| Recruiting through referrals (9 of 21) | Per-creator SaaS pricing | Consent and provenance ledger for AI content |
| Short-video traffic (TikTok 9, Reddit 8) | OnlyFans-only distribution | Cross-platform live distribution as a default (2 of 21 do any) |

Precedent check ([data/precedents.jsonl](data/precedents.jsonl)): YouTube networks and cam
studios failed where they trapped creators and took cuts that left them a poor living, and
survived where they gave real services (brand deals, tools, support). Colombia's 2021 labour
ruling and K-pop's 7-year contract cap show regulation arrives for trapped labour. **Portability
and a livable creator net are design requirements, not kindness.**

## 5. The software, and the build order against HALO

| # | Build | Why first | Lift from (in SISO's bank) | HALO today |
|---|---|---|---|---|
| 1 | **Ledger + live creator statements + Creator Career** (point the chatter quest engine at creators; referral tiers on the existing referral tracking) | Retention is enterprise value; trust is the cheapest lever | Formance Ledger / TigerBeetle, Twenty, HALO's quest engine and referrals | Engine built (chatters), referrals built, ledger hand-rolled |
| 2 | **Fan inbox + AI drafts + attribution** (chatter → fan → content unit → payout) | Moves break-even from ~$5.6k to ~$2.4k; doubles the market | Buy the OnlyFans inbox (Infloww-class: no public API); own attribution in the ledger + PostHog; Chatwoot for cam-site and creator chat ([STACK](STACK.md)) | Missing |
| 3 | **Consent ledger + AI content pipeline** (photo and voice first) | Rest weeks without lost income; legal licence to scale AI | ComfyUI, ai-toolkit, fish-speech/ElevenLabs, Immich | AI voice built; consent missing |
| 4 | **Traffic machine** (scheduling, tracking links, trend scoring) | Traffic is everyone's weak department | Postiz, Dub, PostHog, SISO's trend benchmark | Missing (streaming built) |
| 5 | **Leak protection** | Table stakes for 14 of 21 | Buy a takedown service; imagehash + reverse search for detection | Missing |

Already done by HALO and not rebuilt: cross-platform live streaming, contracts and e-sign,
payroll, onboarding, recruiter bounties.

## 6. What would prove this wrong

1. AI-drafted chat sells materially less than human chat at the same fan (test: A/B on one
   creator for 30 days, revenue per fan).
2. Creators value a lower split far more than tiers and statements (test: churn of creators
   offered Creator Career vs a flat cut).
3. A platform bans AI drafts outright or tightens AI-content rules (watch: OnlyFans terms).
4. Cross-platform live revenue stays small next to OnlyFans revenue (measure: share of
   creator gross by platform after 90 days).
