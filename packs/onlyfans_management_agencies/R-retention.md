# R Retention: keeping creators for years

Shaan (11 Oct): "creator churn is huge. So gamification around keeping creators happy, rewarding
them at certain milestones, inciting them to ... refer more creators ... how to keep them staying
for years and years". Data: [`data/retention_patterns.jsonl`](data/retention_patterns.jsonl)
(55 mechanics from OFM and other industries); HALO's own inventory was read from SISO's notes
and is kept private (it contains implementation detail).

## 1. Where HALO stands

`[analysis]` HALO has a **full gamification engine, but it points at chatters, not creators**:
quests with XP and in-house currency, shift missions, a leaderboard and rank ladder, a reward
shop with vouchers, and a manager review queue (all built). On the creator side it has the
foundations (onboarding portal, contracts and e-sign, calendar and announcements, referral
links with partner history and monthly commission tracking) but **no creator-facing progression,
milestones, tenure rewards, renewal flow or referral tiers**. Referral tiers are designed, not
built; the recruiter pipeline is missing.

So the engine exists. The job is to point a second copy of it at creators.

## 2. Why creators leave

From public agency blogs and forums (unverified rates, labelled as such in the data):

1. **The maths feels unfair**: 20% platform + 30-50% agency leaves the creator 30-56% of gross.
2. **Lock-in without accountability**: long exclusive terms with no performance clause.
3. **Burnout**: always-on posting and chat pressure.
4. **Opacity**: creators can't see what was earned, by whom, and what was taken (13 of 21
   profiled agencies don't even publish a rate).
5. **Nothing to lose by leaving**: no status, no accrued benefit, a rival offers a lower cut.

`[analysis]` Causes 1, 4 and 5 are structural and software can fix them; 2 is a contract choice;
3 is what AI content and a good team remove.

## 3. What to borrow (ranked by fit)

| Mechanic | Borrowed from | How it works for a creator |
|---|---|---|
| **Split that improves with tenure and results** | Twitch tier locks, sales accelerators | Agency share steps down (e.g. 40% → 35% → 30%) at revenue or tenure milestones; once earned, a tier is locked for 12 months |
| **Creator-refers-creator, two levels, capped** | eXp Realty revenue share, referral guilds | Referrer earns a share of the agency's commission on the creator they bring for 12 months; a small second level for 6 months; nothing deeper (keeps it out of pyramid territory) |
| **Status the creator can show** | Airbnb Superhost, YouTube plaques, Uber Pro | Named tiers with visible badges and real perks (priority shoots, better AI quota, faster payouts) re-qualified each quarter |
| **Milestone rewards** | YouTube Creator Awards, sales President's Club | Physical and cash rewards at $10k / $50k / $100k / $1M lifetime; an annual trip or summit for the top tier |
| **Guarantee with clawback, first 90 days** | Cam studios, sports signing bonuses | A floor income while the account ramps, earned back if targets hit |
| **Live statement, every payout** | Music royalty statements | What fans paid, the platform fee, the agency share, what each chatter sold: the opacity cause, removed |
| **Fair exit clause** | Performance-based employment | Creator may leave if the agency misses an agreed floor; the agency earns loyalty by not trapping people |
| **Burnout guard** | Gig-platform streak design, done humanely | Streaks reward consistency but have rest days built in; AI content covers rest weeks |
| **Mentorship ladder** | K-pop trainee systems, esports academies | Senior creators coach new ones for a stipend + a small share; they become the referral engine |
| **Win-back** | Subscription businesses | A defined path back for a creator who left, with tier memory |

## 4. The design: "Creator Career"

`[analysis]` One loop built from HALO's existing chatter engine, its referral tracking and its
contracts, plus a real ledger:

1. **Earn**: every payout posts to a per-creator ledger; the creator sees a live statement.
2. **Level**: lifetime earnings and tenure move the creator through named tiers; each tier
   lowers the agency share and unlocks perks; tiers lock for 12 months.
3. **Quest**: weekly creator quests (content shot, live hours streamed across platforms, new
   fan milestones) pay in-house currency spendable in the existing reward shop.
4. **Refer**: each creator has a referral link; referred creators' first 12 months pay the
   referrer, visible on the same statement; two levels maximum.
5. **Rest**: AI content (photo and voice today) keeps the account posting while the creator
   takes planned time off; rest days don't break streaks.
6. **Renew**: 60 days before term end, the system builds the renewal offer from the creator's
   own numbers and tier; no renewal is silent.

Software it needs, all already in SISO's GitHub bank: a ledger (Formance Ledger / TigerBeetle /
Blnk), the CRM (Twenty) for referral trees, e-sign (Documenso / DocuSeal) for renewals, and
HALO's own quest engine. See [T6](T6-open-source.md).

## 5. Guardrails

- Two referral levels and a 12-month cap: rewards for bringing people, never for recruiting
  recruiters indefinitely.
- No mechanic that pressures output beyond what the creator agreed to.
