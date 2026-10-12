# X Borrow map: who already solved each piece, and where HALO stands

Every moving piece of an agency (from [P-physics](P-physics.md)) has been solved at scale in some
other industry. This map says which one, what they use, what is open source, and HALO's state
([home case](C-case-halo.md)). OSS names are candidates for T6 to verify (licence, health,
already in the SISO bank or new).

HALO column: **Built** · **Partial** · **Missing** (from SISO's notes, 11 Oct; business level).

## Machine 1: Attention (traffic)

| Piece | Solved best by | Their tools | Open source to lift | HALO |
|---|---|---|---|---|
| Multi-account posting and scheduling | Social media agencies | Later, Buffer, Hootsuite | Postiz, Mixpost | Missing |
| Funnel tracking (link → sub → spend) | Affiliate / performance marketing | Voluum, RedTrack, Keitaro | PostHog, Matomo | Missing |
| Trend and content-winner detection | Media buyers, TikTok shops | Pentos, Exolyt | Own scrapers + benchmark scoring (SISO already built one for a client) | Partial |
| Live audiences on many sites | Cam studios, Twitch esports orgs | Restream, studio software | OBS, OvenMediaEngine | **Built** (cross-streaming) |
| Shoutout / S4S exchange | Ad networks | Telegram exchanges (T2) | none | Missing |

## Machine 2: Conversation (the sales floor)

| Piece | Solved best by | Their tools | Open source to lift | HALO |
|---|---|---|---|---|
| Unified inbox across platforms | Customer support / BPO | Zendesk, Intercom | Chatwoot, Zammad (team, creator and cam-site chat only: OnlyFans has no public API, so its DMs stay in Infloww-class tools; see [STACK](STACK.md)) | Missing |
| Shifts, rota, coverage | Call centres (workforce management) | NICE, Genesys, Five9 | Cal.com + own rota | Partial |
| Revenue per chatter per shift | Sales orgs | Salesforce, Gong | Twenty + own attribution | Missing |
| QA scorecards and coaching | Contact-centre QA | MaestroQA, Playvox | none known (T6) | Missing |
| AI drafting and closing | AI sales assistants | Supercreator Izzy, Substy | open LLMs + own prompts | Partial (AI voice) |
| Fan value segments (who spends) | Ecommerce CRM, mobile-game "whale" ops | Klaviyo, LiveOps | Twenty, PostHog cohorts | Missing |
| Gamified incentives | Sales SPIFs | Spinify, Ambition | own | **Built** (no measurement under it) |

## Machine 3: Inventory (content)

| Piece | Solved best by | Their tools | Open source to lift | HALO |
|---|---|---|---|---|
| Media library, tagging, rights | Digital asset management, newsrooms | Bynder, Frame.io | Immich, ResourceSpace | Partial (Drive pipeline) |
| Shoot planning | UGC / production agencies | StudioBinder | Plane | Partial |
| AI image, video, voice | AI studios | Higgsfield, ElevenLabs | ComfyUI | Partial (AI voice) |
| Content calendar per creator | Publishers | CoSchedule | Postiz, Plane | Missing |

## Support A: Supply (creators)

| Piece | Solved best by | Their tools | Open source to lift | HALO |
|---|---|---|---|---|
| Sourcing and pipeline | Recruiting / staffing | Greenhouse, Bullhorn | OpenCATS, Twenty | Partial |
| Recruiter / referral bounties | Referral networks, real-estate brokerages | PartnerStack | own | **Built** |
| Onboarding, ID, contracts | Fintech KYC, talent agencies | Persona, Yoti, DocuSign | Documenso, DocuSeal | **Built** (contracts) |
| Talent development | K-pop trainee systems, sports academies | internal | Plane | Missing |

## Support B: Trust (money and safety)

| Piece | Solved best by | Their tools | Open source to lift | HALO |
|---|---|---|---|---|
| Creator money as a liability, per-creator ledger | Talent trust accounting, marketplaces | Stripe Connect, Hyperwallet | Formance Ledger, TigerBeetle, Blnk | Partial (hand-rolled) |
| Statements and splits | Music royalty accounting | Curve, Exactuals | none known (T6) | Partial |
| Contractor pay and tax forms | Gig platforms | Deel, Trolley | Frappe HR, Kimai | **Built** (payroll) |
| Leak removal | Anti-piracy firms | Ceartas, LeakRemover | none known | Missing |
| Account and credential safety | IT / password managers | 1Password | Vaultwarden | Partial |

## Reading the map

1. **HALO has built the hard, unsold half**: live distribution, supply bounties, contracts,
   payroll. 21 of 21 agencies profiled sell OnlyFans management; only 2 mention streaming at all.
2. **HALO is missing Machine 2**, the sales floor, which is where agency revenue is made. Every
   piece of it has a mature model in call centres and sales orgs, and Chatwoot + Twenty + an
   attribution layer gets most of the way.
3. **Machine 1 beyond streaming is empty**: posting, funnel tracking and trend detection come
   straight from social and affiliate agencies, and SISO already built a trend benchmark for a
   client.
4. The biggest structural fix is **Trust**: a real ledger (Formance/TigerBeetle class) under the
   payroll and statements HALO already has.
