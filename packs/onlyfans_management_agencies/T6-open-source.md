# T6 Open source: what SISO's GitHub network already holds

Shaan (11 Oct): "what github things are out there to help us and what core fundamental SaaS
platforms that we use that we could automate from our network on GitHub".

| | Count |
|---|---:|
| Repos examined by two Haiku sweeps | **265** (193 ops/retention/money, 72 content/growth) |
| Of those already in the SISO repo bank (script check, 211k names) | 115 |
| Reviewed shortlist ([`data/oss_curated.jsonl`](data/oss_curated.jsonl)), live GitHub stats | **35** |
| Shortlist already in the bank | **35 of 35** |

The sweeps' own verdicts were star-count based and are marked `UNREVIEWED`
([`oss_retention_ops.jsonl`](data/oss_retention_ops.jsonl),
[`oss_content_growth.jsonl`](data/oss_content_growth.jsonl)). The shortlist below is the
reviewed set. **Every piece of the agency can be lifted from repos SISO already banks.**

## The shortlist, by machine

| Machine | Repos (stars, licence) |
|---|---|
| Conversation | chatwoot/chatwoot (38k, custom open), kimai/kimai (5k, AGPL), usememos/memos (64k, MIT) |
| Attention | gitroomhq/postiz-app (37k, AGPL), PostHog/posthog (40k), dubinc/dub (25k), growthbook/growthbook (8k), datarhei/restreamer (5k, Apache), OvenMediaEngine (3k, AGPL; HALO uses it), bluenviron/mediamtx (20k, MIT) |
| Inventory | Comfy-Org/ComfyUI (137k, GPL), ostris/ai-toolkit (12k, MIT), bmaltais/kohya_ss (13k, Apache), InstantID (12k, Apache), Wan2.1 (17k, Apache), LTX-Video (11k, Apache), fish-speech (33k), chatterbox (27k, MIT), voicebox (57k, MIT), makeplane/plane (61k, AGPL), immich (116k, AGPL) |
| Supply | twentyhq/twenty (58k), open-mercato (2k, MIT), documenso (15k, AGPL), docuseal (19k, AGPL), cal.diy (49k, MIT) |
| Trust | formancehq/ledger (1k, MIT), tigerbeetle (17k, Apache), blnk (0.5k, Apache), frappe/hrms (9k, GPL), spicedb (7k, Apache), vaultwarden, imagehash (2k, MIT), search-by-image (4k, GPL) |
| Glue | n8n-io/n8n (207k, fair-code) |

## Licence notes

- AGPL/GPL (Plane, Immich, Postiz, Documenso, DocuSeal, Kimai, ComfyUI, OvenMediaEngine) is fine
  to run for our own agency; it bites only if we ship a modified version to others as a service.
- "Open" models are not all open: check each model's weights licence before commercial use
  (some video models carry community licences with limits).
- n8n is fair-code, not OSI open source.
