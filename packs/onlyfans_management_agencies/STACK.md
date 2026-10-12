# STACK: the software for a 30-creator agency, on HALO

Shaan (12 Oct): "what about software stack wise". One stack, by machine ([P](P-physics.md)):
**keep** what HALO built, **lift** open source already in SISO's repo bank ([T6](T6-open-source.md)),
**buy** only where nothing open is close or a platform forces it.

**Hard constraint** `[analysis]`: OnlyFans has no public API. Fan-inbox tools (Infloww,
Supercreator) work inside the creator's logged-in session through a desktop app or browser
extension. So an open-source inbox such as Chatwoot cannot read OnlyFans DMs. It fits team
support, creator support and cam-site chat, not the OnlyFans sales floor. This corrects the
"Chatwoot for the fan inbox" line in [X](X-borrow-map.md) and [T8](T8-first-principles.md).

## The spine (one database, one ledger)

| Piece | Choice | Source | Why |
|---|---|---|---|
| Database | Postgres | keep (HALO is moving to it) | One home for creators, fans, sales, staff |
| Money ledger | **Formance Ledger** (MIT) | lift | Double-entry, per-creator accounts, creator money held as a liability; TigerBeetle only if volume demands it |
| Permissions | HALO roles, enforced server-side | keep + fix | Who sees which creator |
| Automation glue | n8n | keep (HALO uses it) | Moves data between the pieces |
| Owner dashboards | Metabase over Postgres | lift | Margin per creator, chatter and traffic source |

## By machine

| Machine | Keep (HALO) | Lift (bank) | Buy |
|---|---|---|---|
| **Supply** | Onboarding portal, contracts + e-sign, referral tracking, recruiter bounties | Twenty (creator and recruiter pipeline, referral tree), Cal.com (check-ins) | ID/age checks: Persona or Yoti |
| **Conversation** | Chatter quest engine, payroll, Buzz (team chat) | Kimai (shift hours) if payroll needs it | **Infloww or Supercreator** for OnlyFans DMs and AI drafts (~$40-60 per creator per month); export its sales into the ledger |
| **Attention** | Oracle cross-streaming (OvenMediaEngine) | Postiz (Reddit/X/TikTok/IG scheduling), Dub (tracking links), PostHog (funnels) | Paid shoutouts as needed |
| **Inventory** | AI voice (ElevenLabs), Drive content pipeline, Plane (briefs) | Immich (creator vault with face search), ComfyUI + ai-toolkit (identity LoRAs, run on rented GPU) | ElevenLabs; hosted short video (Kling/Veo) until open video catches up |
| **Trust** | Payroll, statements to build on the ledger | Formance Ledger, Vaultwarden (creator platform logins in a vault), imagehash + search-by-image (leak detection) | Payout rails (Wise/Paxum), contractor tax (Deel/Trolley), leak takedowns (a DMCA service) |

## What it costs a month at 30 creators

| Item | Monthly |
|---|---:|
| Fan inbox (Infloww at $40-50 × 30) | $1,200-1,500 |
| ElevenLabs + hosted video credits | ~$100-300 |
| Rented GPU for identity models | ~$100-300 |
| Leak takedown service | ~$100-300 |
| ID checks (Persona from $250) | ~$250 |
| Hosting for the open-source pieces (HALO's VPS) | already paid |
| **Total software** | **~$1,750-2,650**, i.e. ~$60-90 per creator |

Replaced by open source instead of SaaS: Slack, Notion/ClickUp, Calendly, Zapier, Linktree,
Buffer/Later, Hubstaff, 1Password, Amplitude ([S](S-saas-replace.md)).

## Build vs buy, the one decision that matters

`[analysis]` **Buy the OnlyFans inbox now; own everything around it.** Building a session-level
OnlyFans client is a terms-of-service and account-ban risk for no strategic gain. The moat is
the ledger, Creator Career, the consent record, traffic and streaming, and those are all
lift-and-own. Revisit when a platform offers an official API (Fanvue and cam sites are the first
places to build a native inbox).
