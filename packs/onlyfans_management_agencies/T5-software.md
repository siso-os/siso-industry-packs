# T5 Software: what OFM agencies run on

**First pass, 11 Oct 2026.** 50 tools from public pricing pages:
[`data/tools.jsonl`](data/tools.jsonl). `used_by` (which top firms use which tool) fills in during T4.

| Category | Tools | Price shape |
|---|---:|---|
| CRM / chatting / inbox | 12 | Per creator account: Infloww $40-150, Supercreator $64-279, CreatorHero $250 flat, OnlyMonster $79; Substy free + 15% commission or $69-99; EU tools (Offmy, MYMIK, MyPuls) free under a revenue floor |
| Anti-detect browsers | 10 | $5-99/month (Dolphin Anty, Multilogin, AdsPower, GoLogin…). Listed because agencies buy them to run many accounts; mechanics out of scope |
| Payroll / payouts | 5 | Deel (~$49/contractor), Trolley (quote), Paxum ($1.50/transaction), Wise, time tracking (Hubstaff $5-25/user) |
| Fan and cam platforms | 7 | OnlyFans takes 20% (creator keeps 80%); Fansly, Fanvue; cam platforms Chaturbate, Stripchat, CamSoda |
| Traffic and posting | 7 | Link-in-bio (Direct.me $15 VIP), scheduling (Later, Buffer, Hootsuite $99-399/user) |
| Leak protection | 2 | LeakRemover $99/month; Remove.Tech quote |
| Content | 2 | AI voice (ElevenLabs), AI image/video |
| Multistreaming | 2 | Restream, OBS |
| Team ops | 3 | ClickUp, Notion, time tracking |

## A 10-creator agency's software bill

`[analysis]` About **$600-700/month**, most of it the chat CRM (Infloww at $40 × 10 = $400), then
an anti-detect browser (~$89) and leak removal (~$99). Software is small next to labour: 24/7
chat cover for 10 creators needs roughly 10-30 chatters (3-5 creators per chatter per shift, 3 shifts) at $3-8/hour (T1 signals), i.e.
about $5k-40k/month at 173 hours each, before PPV commission.

`[analysis]` Confirms SISO's August finding: every agency-specific tool sells the **fan layer**
(inbox, AI chat, analytics), priced per creator. Nobody in this list sells contracts, creator
statements, payouts with a creator ledger, recruiting or streaming operations as an agency
system. Those are the parts HALO already built ([home case](C-case-halo.md)).

## Corrections

- OnlyFans' fee was recorded as 30% by a secondary source; it is 20% (onlyfans.com/terms).
