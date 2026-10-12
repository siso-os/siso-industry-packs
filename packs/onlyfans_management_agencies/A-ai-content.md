# A AI content: is it good enough, and what are agencies doing

Shaan (11 Oct): "automating content generation once AI gets good enough ... I'm pretty sure it is
good enough". Data: [`data/ai_content.jsonl`](data/ai_content.jsonl) (45 rows: vendors, models,
workflows, platform rules, laws, gaps). Vendor quality claims are labelled as such.

## Good enough today?

| Content | Verdict | Basis |
|---|---|---|
| **Photos** of a consenting creator | **Yes** | Identity LoRA (Flux) or Higgsfield-class "Soul ID" from 15-30 reference photos; unlimited consistent output |
| **Voice** (voice notes, PPV audio) | **Yes** | ElevenLabs clones from 1-30 minutes of audio; HALO already runs this (built) |
| **Short video** (< ~30 s) | **Mostly** | Kling 3 / Veo 3.1 hold identity for short clips; drift and hands fail beyond that |
| **Long video** | No | Identity drift; mainstream video models block explicit output at inference |
| **Chat** | **Allowed as drafts only** | OnlyFans terms bar fully automated chat; AI drafts, a human sends: what Supercreator-class tools sell |

So Shaan is right for photos and voice; short video is close; explicit video and fully automated
chat are not available through mainstream tools or allowed by the main platform.

## The rules that bind it

| Rule | What it says |
|---|---|
| OnlyFans | AI content only of the verified account holder, and labelled as AI |
| Fansly | Photorealistic AI content banned (2025) |
| Fanvue | The one major platform built for synthetic creators (consent, disclosure, moderation) |
| EU AI Act Art. 50 (from 2 Aug 2026) | Realistic AI images, video and audio must be labelled |
| US TAKE IT DOWN Act (May 2025) + state deepfake laws | Non-consensual intimate imagery, AI included, is a crime; takedown duties |

`[analysis]` The binding constraint is **consent and provenance**, not model quality. An agency
that can prove, per asset, which creator consented to which use is the one allowed to scale AI.
That is a rights-and-consent registry, which HALO lacks today (creator boundaries are free text).

## The stack (consenting creators)

1. **Identity**: LoRA training (ai-toolkit, kohya_ss) + ComfyUI pipelines, or a hosted Soul-ID tool.
2. **Video**: hosted Kling / Veo for short clips; open Wan 2.1 / LTX-Video to run ourselves.
3. **Voice**: ElevenLabs (built in HALO); open alternatives fish-speech, chatterbox.
4. **Labelling + consent record**: every generated asset tagged AI, linked to the consent scope.
5. **Schedule**: Postiz across social platforms; platform posting stays manual or official-API.

Hosted tooling runs about $500-800/month per agency `[vendor prices]`; all the open pieces are
already in SISO's repo bank ([T6](T6-open-source.md)).

## What nobody has yet (the gaps)

1. A per-asset **consent and provenance ledger** linking creator, scope, model and output.
2. **Identity-stable video past 30 seconds.**
3. An **AI-label pipeline** that satisfies the EU AI Act and platform rules automatically.
4. **Leak and deepfake monitoring** for the creator's real likeness (perceptual hashing +
   reverse search exist as parts, not as a service agencies run).
5. A **chat assistant that stays within platform rules**: drafts, persona memory, human send.
