---
title: "Site anatomy: food & drink offer module (cafes, coffee, bakeries, desserts, restaurants, bars, street food)"
---

# Site anatomy: the food & drink offer module

Written by SISO-AGENCY (reader), 7 Oct 2026, for UI-HUB. It extends the core slot table in `_data/siso-agency/INDUSTRY-RUN.md` section 2 with the Menu module's slots. Machine-readable twin: `slots.json` (41 slots, same text).
Tags: **[data]** = counted by us; **[research]** = a published source; **[reasoned]** = our inference or an ADR.
Field names: `business.*` are in the frozen `site.json/1`. Every other field (`photos[]`, `hours`, `rating`, `reviews[]`, `menu.*`, `contact.*`, `delivery.*`, `attributes[]`, `copy.*`) is a **proposed name** for SISO-SITES to confirm in the enrichment schema.

> **Read with UI-HUB's anatomy** (`Great_Library_of_SISO/banks/siso-ui-hub/surfaces/landing-site.md`): it crawled 212 Vietnamese and 100 overseas café and restaurant sites plus 15 platform sites, so its page and slot prevalence is the stronger count. This file adds what that one lacks: which of our built variants fills each slot, what each slot does with thin data, and the `site.json` fields it reads. (SISO-AGENCY, 7 Oct)

## 1. Sources and how the 19 sites were chosen
- `INDUSTRY-RUN.md` and `THE-UI-SYSTEM.md`: the core slots, the Menu module, what a slot is.
- restaurant-app `template-variants.md` and `user-needs-by-page.md`: our built variants and per-page user goals; `bali-apps-benchmark.md` (GoFood, GrabFood, ShopeeFood, Chope, Traveloka: category chips, sticky cart, vouchers, ratings near the action).
- `hq/industries/cafes/research/2026-10-07-checklists-and-platforms.md`: Gueduek and Uca 2017 (93 Istanbul restaurant sites, 51 items), Temizkan and Aktepe 2023 (14 Michelin sites, 30 items), Ariker 2012 (full list not obtained), BentoBox, Popmenu, Owner.com (verified); Toast and Square only partly read.
- `hq/industries/cafes/INDUSTRY.md` and `2026-10-07-checklist-check.md`: our decisions (Vietnam overlay, data gate, real prices only, footer mark, phone and desktop).
- The 19 outlines in `packs/restaurants/sites/*.md`: HTML only, fetched 7 Oct 2026.

**The 19, by why they are in:** platform-built (Atelier Crenn, Dado's, Saffy's on BentoBox; Cyclo Noodles on Owner.com; Kuma's Corner on WordPress; Ottolenghi and Ozone on Shopify; Gail's on Wix; Tartine on Elementor); design-led (Dishoom, Noma, Atelier Crenn, Ottolenghi, Prufrock, Monmouth, Blue Bottle); Vietnam (Cong Ca Phe, Hum, Black Sheep for Hong Kong); ours (Cafe 89, Kikas).
**"Best 5 design-led"** = Dishoom, Noma, Atelier Crenn, Ottolenghi, Prufrock. Our pick by design reputation and how much of the outline rendered; it is a judgement, not a ranking from a source. Noma and Atelier Crenn are fine dining, so their weight for cafes is low [reasoned].

**How to read the counts.** I hand-counted from nav, home headings, page lists and footers. The outlines are HTML only: Cong, Hum, Gail's, Black Sheep and Tartine rendered thin (JavaScript), so every n/19 is a **floor**. The tool's own `Features` regex is not used for counts where it clearly over-fires (it flags `events_private` on 18 of 19 and `language_switch` on 17 of 19, including sites with no switch). Where I quote it, I say "by regex".

## 2. The sitemap

| Page type | n/19 | Best 5 | Who | Do we ship it? |
|---|---|---|---|---|
| Home | 19 | 5 | all | Yes, always |
| About / story (page or section) | 17 | 4 | all but Cong, Ottolenghi | Yes, as a page at rich data, else a home block |
| Visit: location and hours | 15 | 4 | all but Atelier Crenn, Gail's, Hum, Ozone | Yes, always (a section or a page) |
| Menu (page or section) | 11 | 3 | Atelier Crenn, Cafe 89, Cyclo, Dado's, Dishoom, Gail's, Hum, Kikas, Kuma's, Prufrock, Saffy's | Yes, always (the retail and brand sites have none) |
| Careers | 11 | 3 | most | No |
| Shop / merch / beans | 11 | 5 | brands and roasters | No (Catalogue module) |
| Gift cards | 9 | 3 | US and UK sites | No in Vietnam |
| Reservations | 8 | 4 | restaurants | Restaurants and bars only |
| Events / private dining / catering | 8 | 4 | restaurants | Restaurants and bars, if on their own page |
| Multi-location list | 8 | 2 | groups | No |
| Order online / delivery | 6 | 0 | Black Sheep, Cyclo, Dado's, Gail's, Hum, Kuma's | Yes as a button to Grab/ShopeeFood, not a page |
| Loyalty / app | 6 | 1 | | No (ADR 0011) |
| Press and awards | 5 | 1 | | No (claims, ADR 0003) |
| Dedicated Contact page | 5 | 1 | | No: folded into Visit |
| FAQ page | 2 | 1 | Atelier Crenn, Monmouth | As a home block from known facts |
| Gallery page | 0 | 0 | gallery is always a section | Section only |

**True one-pagers:** Cafe 89, Kikas, Gail's; Dado's is one long page of 12 "segments" plus order and class pages [data]. The platform sites each have 3 to 9 top-level pages [research].

**Recommendation: shape follows data richness [reasoned]**

| Tier | What the business has | Shape |
|---|---|---|
| 0 Below the gate | under 3 photos, or no hours, address or rating | One-pager: Hero, Essentials, What it's like (if attributes), Visit; `noindex`; 2-button bar |
| 1 Passed the gate, thin | 3 to 5 photos, 12 reviews, menu categories or up to 15 items | One-pager with 3 anchors (Menu, Our place, Visit) = the Cafe 89 / Kikas shape |
| 2 Rich | 6+ photos, 16+ items (some priced), 25+ reviews, a sourced story | 4 pages: Home, Menu, Our place, Visit; gallery becomes a home section |
| 3 Restaurant or bar | booking, events or catering on their own page | Tier 2 plus Reservations and Events pages |

Why: 3 of 19 are real one-pagers and both of ours are; a menu with 16+ items stops being a section on a phone [reasoned]; the one thing that turns a page into a business is order or reserve, and that is a button, not a page.

## 3. The slots, page by page, in order

Order on Home is the order on the page. Built-variant names are restaurant-app section names (`src/domains/customer-facing/landing/sections/*`, `template-variants.md`), Cafe 89 and Kikas. The prevalence cell gives n/19 and (n/5) for the best 5 design-led sites.

### Global

| Slot | Job | Prevalence | Evidence | Built variants | Thin-data behaviour | Reads (`site.json`) |
|---|---|---|---|---|---|---|
| **Header + nav + language** | Name or wordmark, 3 to 5 links, VI/EN switch, one action button | 19/19 (5/5 best). every site has a header nav; 7 of 19 add a conversion button in it (Reservations, Order Online, Book a table); 4 have a language switch | [data] counts; [research] Gueduek and Uca nav items; [reasoned] 3 to 5 links | restaurant-app nav (top and dark side nav); Cafe 89 header (data-vi/en switch); Kikas header (Menu burger) | Wordmark from name (no logo file needed); 3 links max (Menu, Our place, Visit); drop 'Our place' if there is no story or 3+ photos; no switch if only one language of copy exists | `['business.name', 'logo.wordmark', 'nav.items[]', 'langs[]', 'contact.primary_action']` |
| **Sticky action bar (phone)** | The 2 to 4 main actions under the thumb at all times | 4/19 (1/5 best). only 4 of 19 expose a fixed bar in their HTML (Atelier Crenn, Cafe 89, Dado's, Kikas); all 3 verified platforms ship one | [data] 4 of 19; [research] platforms note B1 to B3 | restaurant-app cta-section/primary (mobile sticky bar); Cafe 89 mobile-bar (Drinks, Corner, Directions); Kikas mobile-shortcuts (2 buttons) | Never hide: Directions is always possible from maps_url. Add Zalo or Call only when the number exists; add Order only when a Grab/ShopeeFood/own link exists. Minimum 2 buttons; with only Directions, show it full width | `['business.maps_url', 'contact.zalo', 'contact.phone', 'delivery.grab', 'delivery.shopee', 'menu.exists']` |
| **Footer** | Close the page: hours, address, contact, socials, SISO mark | 17/19 (4/5 best). 17 of 19 outlines show a footer (Cong and Gail's did not render one) | [data]; [research] social 72.0% Gueduek and Uca; ADR 0007 | Kikas footer; Cafe 89 footer; restaurant-app footer variations | Always shown. Drop empty columns; at minimum name, address, map link and the SISO line | `['business.name', 'business.address', 'hours', 'contact.*', 'business.social', 'langs[]']` |
| **SEO and schema** | LocalBusiness / Restaurant / Menu schema, hreflang, sitemap, noindex below the gate | 15/19. 15 of 19 publish a sitemap (Blue Bottle, Cafe 89, Cong, Kikas do not: two of them are ours); schema is invisible in outlines | [data] sitemap counts; [research] Popmenu emits schema.org Menu/MenuItem (platforms note B2) | SISO-SITES machine (not a UI slot) | Below the gate (3 photos, hours, address, rating, menu items or categories) publish with noindex; above it, schema fields only for data that exists | `['business.*', 'hours', 'rating', 'review_count', 'menu.items[]', 'gate.passed']` |

### Home

| Slot | Job | Prevalence | Evidence | Built variants | Thin-data behaviour | Reads (`site.json`) |
|---|---|---|---|---|---|---|
| **Hero** | Say what this place is in 2 seconds; one main action | 19/19 (5/5 best). every site has a hero or lead block. A conversion button in the hero: 5 of 19 (Dado's, Cyclo, Gail's, Kuma's, Monmouth); two soft links: Cafe 89, Kikas; hero gallery with pause: 2 (Atelier Crenn, Dado's); video: 2 (Cyclo, Noma) | [data] counts; [research] platforms put Order/Reserve first | restaurant-app hero-section: primary, gradient-words, video-overlay, classic-center, minimal-center, logo-center, blur-fade, split-left (15 templates); restaurant-app About hero primary/template-2/template-3; Cafe 89 hero; Kikas hero | With 3 photos: one still full-bleed photo with a gradient scrim, name, one-line kind ('cafe, Da Nang'), one action. With 0 to 2 photos: wordmark-led or generated atmosphere image; never a carousel or a blank box. Headline is our copy, never a claim | `['business.name', 'business.kind_vi', 'business.kind_en', 'business.area', 'photos[0..2]', 'copy.hero_headline', 'copy.hero_sub', 'contact.primary_action']` |
| **Essentials strip** | Open now, hours, call or Zalo, directions, delivery buttons, in one glance | 0/19 (0/5 best). 0 of 19 have a named strip. Dado's puts Call, Instagram, Email in its header; Noma and Saffy's put hours in the footer only | [data] 0 of 19; [research] hours 8.6% vs 64% check (Gueduek and Uca; INDUSTRY.md); [reasoned] | restaurant-app essentials-section/primary (hours, map link, WhatsApp/chat chips) | Show only what exists. Open-now chip from hours; if no hours, show address plus Directions only. Zalo and Grab/ShopeeFood buttons only with real links | `['hours', 'business.address', 'business.maps_url', 'contact.zalo', 'contact.phone', 'delivery.grab', 'delivery.shopee']` |
| **Featured menu** | Let them see the food and drink on the home page and tap through to the menu | 7/19 (2/5 best). 7 of 19 put menu content on the home page (Cafe 89, Kikas, Gail's, Dado's, Prufrock, Saffy's, Dishoom) | [data] 7 of 19; [research] 91% look up the menu online (INDUSTRY.md) | restaurant-app menu-section/signature-dishes; Cafe 89 drinks-section (filter chips); Kikas menu-section (tabs with photos) | No menu: show 3 to 6 category names as tiles with 'See on Grab' or 'Ask on Zalo' if links exist, else hide the slot. Some items without prices: list items, no price column | `['menu.categories[]', 'menu.items[0..8]{name,desc,price,price_source,photo}']` |
| **Specials / today** | Time-boxed offer or what is new | 1/19 (0/5 best). 1 of 19 on food sites (Kuma's 'Burger of the Quarter'); 3 retail sites do 'new arrivals' | [data] 1 of 19; [reasoned] | restaurant-app specials-section grid and slider; restaurant-app promo-section/primary | Hide unless the owner posts a special on their own page; never generate promotions | `['specials[]{title,desc,valid_until,photo}']` |
| **What it's like** | Atmosphere and amenities as 3 to 6 cards (wifi, outdoor, laptop-friendly, kids, parking) | 5/19 (2/5 best). 5 of 19 have vibe copy or atmosphere blocks (Cafe 89, Kikas, Saffy's, Dishoom, Prufrock); amenity chips: 0 of 19 (Cyclo's archived Owner home has them [research]) | [data] 5 of 19; [research] checklist-check gap 1 | Cafe 89 corner-section ('our corner' cards); Kikas place-section; restaurant-app cuisine-philosophy-section (4 pillar cards) | Fill from Maps attributes (8 of 10 trial cafes had them [data: checklist-check]); with none, one sentence of vibe copy and a photo, or hide | `['attributes[]{key,label_vi,label_en,icon}', 'copy.vibe', 'photos[]']` |
| **Story teaser** | Who, since when, why, in 2 to 3 sentences with a link to Our place | 17/19 (4/5 best). 17 of 19 have about or story content somewhere (page or section) | [data] 17 of 19; [research] description and history 13 of 14 Michelin | restaurant-app story-section/primary; restaurant-app About story timeline x2; Kikas place-section | From their own social self-description, summarised; if none, hide and let What it's like carry it. Never invent a founding year | `['copy.story_short', 'business.social.bio', 'founded (only if sourced)']` |
| **Gallery** | Show the place and the product | 5/19 (2/5 best). 5 of 19 have a gallery or hero-gallery section (Atelier Crenn, Cyclo, Dado's, Dishoom, Kuma's) | [data] 5 of 19; INDUSTRY.md: gallery at 6+ photos [reasoned] | restaurant-app gallery-section/grid; restaurant-app About venue-gallery masonry + lightbox | Needs 6 or more of their own photos; at 3 to 5, fold them into Hero and What it's like and hide the gallery; at 0 show nothing | `['photos[]{url,alt,w,h}']` |
| **Reviews and proof** | Rating, count, 3 real quotes, link to read more on Google | 3/19 (1/5 best). 3 of 19 put proof on the home page (Cafe 89 reviews, Kuma's press quotes, Dishoom awards) | [data] 3 of 19; [research] 96% read reviews (INDUSTRY.md); Owner puts reviews on home (platforms B6) | restaurant-app review-section: classic, image-masonry, glass-swiper, grid, minimal, modern, featured, testimonial; restaurant-app ratings summary; awards x2; Cafe 89 review-section ('write on Google') | 12 reviews: rating + count + 'read on Google' + 2 to 3 short real quotes in a static row (no swiper). Under 5 reviews or rating under 4.0: show the count and Google link only, or hide. Never show a rating we did not fetch | `['rating', 'review_count', 'reviews[0..3]{author,text,stars,date,url}', 'business.maps_url']` |
| **Order / delivery band** | Send hungry people to Grab, ShopeeFood or the owner's own ordering | 3/19 (1/5 best). 3 of 19 have a band or action tiles (Dishoom tiles, Gail's delivery and pick-up, Kuma's find a location / order online) | [data] 3 of 19; [research] Grab/Shopee over 90% of VN delivery (INDUSTRY.md) | restaurant-app essentials delivery partners chips; restaurant-app cta-section/primary | Only with a real store link. One link: a single button; two: Grab and ShopeeFood side by side. None: hide | `['delivery.grab', 'delivery.shopee', 'delivery.own_url']` |
| **Location teaser** | Map link, address, landmark; leads to Visit | 8/19 (2/5 best). 8 of 19 (Cafe 89, Cyclo, Dado's, Kikas, Kuma's, Monmouth, Ottolenghi, Dishoom) | [data] 8 of 19 | restaurant-app map-section/primary; Cafe 89 visit-section; Kikas visit-section | Address + 'Open in Maps' button always; skip the embed on the home page | `['business.address', 'business.maps_url', 'how_to_find']` |
| **FAQ** | Answer the 5 questions people ask | 0/19 (0/5 best). 0 of 19 on the home page; Atelier Crenn has an FAQ page, Monmouth lists FAQs in nav; Owner puts FAQ on homepage [research] | [data] 2 of 19 on a page; [research] Owner.com homepages (platforms B6) | restaurant-app About FAQ (listed in INDUSTRY-RUN core table) | Generate 3 to 5 from known facts only (open now, wifi, Zalo, parking, Grab). Under 3 facts: hide | `['faq[]{q,a}', 'derived from hours, attributes, contact, delivery']` |
| **Instagram strip** | Show the social feed as proof of life | 1/19 (0/5 best). 1 of 19 as a section (Dado's 'Follow Us'); social links appear on about 15 of 19 by regex | [data] 1 of 19; [research] Cheesetique feed (platforms B1) | restaurant-app instagram-section/primary | Hide unless the owner has a public Instagram with 6 usable images we may show; otherwise a plain social link in the footer | `['business.social.instagram', 'photos[]']` |
| **Newsletter signup** | Collect emails | 6/19 (3/5 best). 6 of 19 show it in the outline (12 of 19 by regex); platforms put it on every site | [data] 6 of 19; INDUSTRY.md 'seen but left out' | none (restaurant-app has no static variant) | Omit by default | `['newsletter.enabled']` |

### Menu

| Slot | Job | Prevalence | Evidence | Built variants | Thin-data behaviour | Reads (`site.json`) |
|---|---|---|---|---|---|---|
| **Page header + category nav** | Tabs or chips to jump by category; sticky on scroll | 4/19 (1/5 best). 4 of 19 (Cafe 89 chips, Kikas tabs, Dado's tabs, Dishoom daypart menus) | [data] 4 of 19; [research] user-needs-by-page (category chips) | Cafe 89 drinks-section chips; Kikas menu-section tabs; restaurant-app menu-section/overview (tabbed grid) | 1 category: no nav. 2 to 3: inline tabs. 4 or more: scrollable chips | `['menu.categories[]{id,name_vi,name_en}']` |
| **Item list** | Name, one-line description, price (when real), tags, optional photo | 11/19 (3/5 best). 11 of 19 have a menu page or section; menu 79.6% (Istanbul), item descriptions on all 3 platforms | [data] 11 of 19; Gueduek and Uca 79.6%; platforms B6 | restaurant-app menu-section/overview; Kikas menu cards with photos; Cafe 89 drinks list | No menu data: do not show an empty page; show the category tiles from Maps, an 'Ask on Zalo / see on Grab' button, or hide the Menu nav item. Items without price: name + description only. Items without photo: text rows, no grey boxes | `['menu.items[]{name_vi,name_en,desc,price,price_source,tags[],photo,category}']` |
| **Dietary and allergen tags** | Vegan, vegetarian, gluten-free, spicy tags per item | 1/19 (1/5 best). 1 of 19 with a dedicated page (Atelier Crenn); Dado's uses icons [research] | [data] 1 of 19; [research] 2 of 3 platforms | restaurant-app DishCard tags (planned) | Show tags only if the owner's menu states them; never infer. Hide the legend if there are none | `['menu.items[].tags[]', 'menu.dietary_note']` |
| **Price source note** | Say where the prices came from and when | 0/19 (0/5 best). 0 of 19; our own rule | [reasoned] ADR 0003 | none yet | Small line 'Prices from their menu, Sep 2026' shown only when any price is shown | `['menu.price_source', 'menu.price_as_of']` |
| **Order from menu** | Take the next step: order on Grab/ShopeeFood or own link | 6/19 (0/5 best). 6 of 19 have an order link in nav or hero (Black Sheep, Cyclo, Dado's, Gail's, Hum, Kuma's); 0 of the 5 design-led | [data] 6 of 19 | restaurant-app menu-section viewAllHref / delivery deep link | Real store link only; else Directions plus 'ask on Zalo' | `['delivery.grab', 'delivery.shopee', 'delivery.own_url', 'contact.zalo']` |
| **PDF fallback link** | A downloadable menu as a secondary link | 1/19 (0/5 best). 1 of 19 (Kuma's, beside an HTML menu) | [data] 1 of 19; platforms B2 | none | Never the only menu. Offer only if the owner supplied a PDF | `['menu.pdf_url']` |

### Our place

| Slot | Job | Prevalence | Evidence | Built variants | Thin-data behaviour | Reads (`site.json`) |
|---|---|---|---|---|---|---|
| **Story + hero** | The full story with a photo | 17/19 (4/5 best). 17 of 19 have story content | [data] 17 of 19 | restaurant-app About hero primary/template-2/template-3; restaurant-app story-section/primary; Kikas place-section; Cafe 89 corner-section | With under 3 sentences of sourced story: no separate page; use the home Story teaser and What it's like | `['copy.story', 'business.social.bio', 'photos[]']` |
| **Timeline / milestones** | Key years | 0/19 (0/5 best). 0 of 19 in the outlines | [data] 0 of 19; [reasoned] | restaurant-app About story timeline primary and template-2 | Hide unless the owner states dates | `['timeline[]{year,text}']` |
| **Team** | Faces of the people | 1/19 (1/5 best). 1 of 19 clearly (Noma 'People'); team section 7 of 14 Michelin sites | [data] 1 of 19; [research] Michelin team 7 of 14 | restaurant-app team-section/primary | Hide unless the owner's page has names and photos | `['team[]{name,role,photo}']` |
| **Values / sourcing** | Short pillars about how they work | 4/19 (1/5 best). 4 of 19 (Atelier Crenn producers, Monmouth farm info, Ozone sourcing, Blue Bottle brand) | [data] 4 of 19 | restaurant-app cuisine-philosophy-section (4 pillars) | Hide unless sourced from the owner; a generated 'we use fresh beans' is a claim | `['values[]{title,text,icon}']` |
| **Awards and press** | Recognition | 5/19 (1/5 best). 5 of 19 (Black Sheep, Cyclo, Dishoom, Kuma's, Tartine) | [data] 5 of 19; Michelin awards 13 of 14 | restaurant-app awards-section primary/template-2 | Hide; Google rating moves to Reviews. Only owner-stated awards | `['awards[]', 'press[]']` |

### Visit

| Slot | Job | Prevalence | Evidence | Built variants | Thin-data behaviour | Reads (`site.json`) |
|---|---|---|---|---|---|---|
| **Hours** | Opening hours by day, with open-now and holiday note | 15/19 (4/5 best). hours content appears on about 15 of 19 sites (regex; Noma and Saffy's footers); Istanbul sites 8.6%; Michelin 6 of 14 | [data] regex 15 of 19 (loose); [research] Gueduek and Uca; INDUSTRY.md | restaurant-app essentials-section; Cafe 89 visit-section; Kikas visit-section | No hours: hide the table; show 'Check hours on Google Maps' with the maps_url button. Do not guess hours | `['hours{mon..sun[]}', 'hours.special']` |
| **Map + directions** | Get them to the door | 15/19 (4/5 best). 15 of 19 mention location or stores; an embed on 2 (Cafe 89, Dado's); a directions link on about 5 (Cafe 89, Cyclo, Dado's, Noma, Kikas) | [data]; [research] map 80.6% Istanbul; Michelin 13 of 14 | restaurant-app map-section/primary (embed); Cafe 89 visit-section (Open Maps); Kikas visit-section | Always a directions button from maps_url; the embed is optional and lazy; no coordinates: address text and Maps link only | `['business.address', 'business.maps_url', 'geo{lat,lng}']` |
| **How to find us** | One written line from nearby landmarks and the alley or floor | 0/19 (0/5 best). 0 of 19; our own addition (INDUSTRY.md) | [data] 0 of 19; [reasoned] | none yet | Generate from map neighbours only if two or more known landmarks; else hide | `['how_to_find{vi,en}', 'nearby[]']` |
| **Contact channels** | Zalo, phone, Messenger, email, in that order for Vietnam | 12/19 (3/5 best). contact details show on about 12 of 19 (dedicated Contact page or nav item on 5: Atelier Crenn, Black Sheep, Kuma's, Saffy's, Dado's section); phone and address 89.2% in Istanbul; Zalo on 0 of 19 | [data]; [research] Gueduek and Uca 89.2%; ADR 0008 | restaurant-app essentials-section chips (WhatsApp/chat) | Zalo needs a number or link: with none, phone; with none, Messenger from the Facebook page; with none, Maps only | `['contact.zalo', 'contact.phone', 'contact.messenger', 'contact.email']` |
| **Good to know** | Amenities, parking, payment, seating as chips | 0/19 (0/5 best). 0 of 19 as a block; parking coded in 3 of 14 Michelin sites | [data] 0 of 19; [research] checklist-check gap 1 | Cafe 89 corner-section (cards) | From Maps attributes only; fewer than 3 attributes: merge into What it's like, else hide | `['attributes[]', 'parking', 'payment_methods[]']` |
| **Enquiry form** | Events, groups, catering enquiries | 3/19 (2/5 best). 3 of 19 (Dado's modals, Atelier Crenn 'Inquire Now', Cyclo contact); information form 62.4% in Istanbul | [data] 3 of 19; [research] Gueduek and Uca 62.4% | none static | Omit; in Vietnam Zalo replaces forms | `['contact.form.enabled']` |

### Optional: Reservations

| Slot | Job | Prevalence | Evidence | Built variants | Thin-data behaviour | Reads (`site.json`) |
|---|---|---|---|---|---|---|
| **Reserve a table** | Book via link, phone or Zalo (restaurants, bars) | 8/19 (4/5 best). 8 of 19 (Atelier Crenn, Black Sheep, Dishoom, Hum, Noma, Ottolenghi, Ozone, Saffy's); all by external widget or link; online reservation 41.9% in Istanbul | [data] 8 of 19; [research] Gueduek and Uca 41.9%; platforms B1 | restaurant-app reservations domain (archived library booking set; not static yet) | Restaurants and bars only. No booking system: a 'Reserve on Zalo / call' button; never a fake calendar | `['reservations.url', 'contact.zalo', 'contact.phone']` |

### Optional: Events and groups

| Slot | Job | Prevalence | Evidence | Built variants | Thin-data behaviour | Reads (`site.json`) |
|---|---|---|---|---|---|---|
| **Events, private dining, catering** | Groups, parties, catering enquiries | 8/19 (4/5 best). 8 of 19 (Atelier Crenn, Black Sheep, Dado's, Dishoom, Kuma's, Noma, Prufrock, Saffy's) | [data] 8 of 19 | none (restaurant-app has no static variant) | Restaurants and bars with events on their own page; else omit | `['events[]', 'private_dining.text', 'catering.text']` |

### Optional: Gift cards

| Slot | Job | Prevalence | Evidence | Built variants | Thin-data behaviour | Reads (`site.json`) |
|---|---|---|---|---|---|---|
| **Gift cards** | Sell vouchers | 9/19 (3/5 best). 9 of 19, mostly US and UK | [data] 9 of 19; INDUSTRY.md left out | restaurant-app gift-cards domain (legacy) | Omit in Vietnam | `['gift_cards.url']` |

### Optional: Locations

| Slot | Job | Prevalence | Evidence | Built variants | Thin-data behaviour | Reads (`site.json`) |
|---|---|---|---|---|---|---|
| **Multi-location list** | One page per branch | 8/19 (2/5 best). 8 of 19 are multi-site groups (Black Sheep, Blue Bottle, Cong, Dishoom, Kuma's, Monmouth, Ottolenghi, Tartine) | [data] 8 of 19 | none | Single-site cafes: omit. Chains are out of scope for the free-site run | `['locations[]']` |

### Optional: Loyalty

| Slot | Job | Prevalence | Evidence | Built variants | Thin-data behaviour | Reads (`site.json`) |
|---|---|---|---|---|---|---|
| **Loyalty / rewards / app** | Points, club, app download | 6/19 (1/5 best). 6 of 19 (Black Sheep, Cong, Cyclo, Kuma's, Noma, Ozone) | [data] 6 of 19; ADR 0011 | restaurant-app loyalty domain (HeroSection, MembershipShowcase, TierHighlights, leaderboard) | Off; inbound request only (ADR 0011) | `['loyalty.enabled']` |

### Optional: Shop

| Slot | Job | Prevalence | Evidence | Built variants | Thin-data behaviour | Reads (`site.json`) |
|---|---|---|---|---|---|---|
| **Shop / merch / beans** | Sell goods online | 11/19 (5/5 best). 11 of 19, including all 5 design-led sites (retail-led: Blue Bottle, Monmouth, Ozone) | [data] 11 of 19; best5 5 of 5 | none | Out of scope for the free-site run; the Catalogue module covers it | `['shop.url']` |

### Optional: Careers

| Slot | Job | Prevalence | Evidence | Built variants | Thin-data behaviour | Reads (`site.json`) |
|---|---|---|---|---|---|---|
| **Careers** | Hiring | 11/19 (3/5 best). 11 of 19 in nav or footer | [data] 11 of 19; Gueduek and Uca 20.4% | none | Omit by default | `['careers.url']` |

## 4. Rules attached to slots
One line each, with the evidence. The same text is in each slot's `rules` in `slots.json`.

| # | Rule (do / don't) and its evidence | Attached to |
|---|---|---|
| R1 | One primary action in the hero; a second link may be quiet. (Dado's, Cyclo, Gail's, Kuma's, Monmouth each lead with one button [data]; platforms put Order or Reserve first [research: B6 of the platforms note]) | Hero, Order / delivery band, Order from menu |
| R2 | No auto-advancing carousels. Hero is one still photo; if there is a gallery, it has a pause control (Atelier Crenn and Dado's hero galleries ship 'pause' buttons [data]; WCAG 2.2 SC 2.2.2 [research]; NN/g on auto-forwarding carousels [research, cited from memory, not re-fetched]) | Hero, Gallery, Reviews and proof |
| R3 | The menu is HTML, never only a PDF. 18 of 19 have no PDF menu link; the one that does (Kuma's) also has an HTML menu [data]; all 3 platforms ship HTML menus [research: platforms note B6] | Featured menu, Page header + category nav, Item list, PDF fallback link |
| R4 | Show a price only when it is real and sourced (their menu photo, page or delivery listing); otherwise show the item only, and never a placeholder price (ADR 0003 [reasoned]). Missing prices cost visits [research: INDUSTRY.md 'what loses them']; prices appear on 28% of 93 Istanbul sites, 12 of 14 Michelin sites and all 3 platforms [data: Gueduek and Uca 2017; Temizkan and Aktepe 2023]. Soften with 'see prices and order on Grab' when the store link exists | Featured menu, Specials / today, Item list, Price source note |
| R5 | Key actions are exposed at both widths: on desktop in the header, on phone in a fixed bottom bar of 2 to 4 buttons (Menu, Directions, Zalo/Call, Order). Bento: Call + Order; Cafe 89: 3 buttons; Kikas: 2 [data]; all 3 platforms ship a sticky bar [research]. Touch targets at least 44x44 pt [research: Apple HIG, in user-needs-by-page.md] | Header + nav + language, Sticky action bar (phone), Essentials strip, Page header + category nav, Map + directions, Contact channels |
| R6 | Hours and 'open now' are visible without scrolling on phone and repeated in the footer. Only 8.6% of Istanbul sites show hours [data: Gueduek and Uca], yet 64% of customers check them [research: INDUSTRY.md]. A cheap advantage | Essentials strip, Location teaser, Hours |
| R7 | Reviews: show the real rating and count with 'from Google' attribution plus up to 3 real quotes; never invent or paraphrase a quote (ADR 0003 [reasoned]). Only 3 of 19 put proof on the home page [data]; 96% of customers read reviews first [research: INDUSTRY.md] | Reviews and proof, Awards and press |
| R8 | Photos are the owner's own first; generated imagery shows the kind of product, never their exact dishes (ADR 0003 [reasoned]). Photos are the top-coded item: restaurant photo 94.6% [data: Gueduek and Uca] | Hero, What it's like, Gallery, Instagram strip, Story + hero |
| R9 | Language switch in the header, Vietnamese first, English second, same URL pattern. 4 of 19 show a visible switch (Cafe 89, Hum, Noma, Black Sheep) [data]; 40.9% of Istanbul sites, 13 of 14 Michelin sites [data] | Header + nav + language |
| R10 | Contact order in Vietnam: Zalo deep link, then phone, then Messenger (ADR 0008 [reasoned]). None of the 19 sites shows Zalo, GrabFood or ShopeeFood [data]; the two together hold over 90% of delivery [data: INDUSTRY.md] | Sticky action bar (phone), Essentials strip, Order / delivery band, Order from menu, Contact channels, Enquiry form, Reserve a table |
| R11 | Every slot has a thin-data form or hides itself; no empty frames, no 'coming soon', no lorem. Below the data gate the site is published noindex (ADR 0002 [reasoned]) | SEO and schema, Specials / today, What it's like, Story teaser, Gallery, Order / delivery band, FAQ, Instagram strip, Story + hero, Timeline / milestones, Team, How to find us, Good to know, Multi-location list |
| R12 | No claims we cannot source: no 'best', 'organic', 'award', 'since'. Awards, press and sourcing stories only from the owner's own page (ADR 0003 [reasoned]) | Hero, Specials / today, What it's like, Story teaser, Reviews and proof, FAQ, Dietary and allergen tags, Story + hero, Timeline / milestones, Team, Values / sourcing, Awards and press, Hours, How to find us, Good to know, Events, private dining, catering |
| R13 | Header nav has 3 to 5 links on a small business. Atelier Crenn, Cyclo, Kuma's, Monmouth have 10 to 20 entries; Cafe 89, Kikas and Prufrock have 3 to 5 [data]; nav consistency scored 89.2% and ease 84.9% in Istanbul [data]. [reasoned] that fewer is better at 5 pages | Header + nav + language |
| R14 | A side nav is dark only (restaurant-app side nav; UI-HUB rule in THE-UI-SYSTEM.md [reasoned]) | Header + nav + language |
| R15 | The directions button opens the native map app link (maps_url) on phone; the embed is secondary and lazy-loaded. An embed shows on 2 of 19; a directions link on about 5 [data]; map is 80.6% in Istanbul [data] | Location teaser, Map + directions |
| R16 | Footer: hours, address and map link, contact, socials, language, then 'Built with heart + SISO icon', small, linking to the agency site; no claim line (ADR 0007 [reasoned]). Social links in footers: 72.0% [data: Gueduek and Uca] | Footer |
| R17 | Reserve and gift cards are for restaurants and bars, not cafes. Reservations show on 8 of 19, gift cards on 9 of 19, mostly US and UK sites [data]; cafes do not book tables and Vietnamese cafes do not sell gift cards (INDUSTRY.md cafe check [reasoned]) | Reserve a table, Events, private dining, catering, Gift cards |
| R18 | Dietary and allergen info as per-item tags from the owner's menu; never inferred. Only Atelier Crenn gives it a page, Dado's uses icons [data]; 2 of 3 platforms tag items [research] | Item list, Dietary and allergen tags |
| R19 | Newsletter and careers are off by default on a free preview the owner has not claimed. Careers on 11 of 19 and newsletter visible on 6 of 19 [data], but both are noise for a 3-person cafe [reasoned] | Newsletter signup, Enquiry form, Loyalty / rewards / app, Shop / merch / beans, Careers |
| R20 | Item descriptions are one line, written by us about the kind of drink or dish, never a claim about theirs. All 3 platforms show descriptions [research: B6] | Featured menu, Item list |
## 5. What the best do that most don't, and what nobody does but should

**The best five do, and most don't**
1. **Put the next step in the header as one button** (Atelier Crenn and Noma: Reservations; Dishoom: Book a table / Menus). Only 7 of 19 have a header button [data].
2. **Keep the home page short and let photos carry it** (Atelier Crenn: hero, one text block, signup; Noma: one article; Prufrock: four blocks). Most sites stack 10 to 20 sections [data].
3. **Give each outlet or menu its own page** (Dishoom's per-cafe and per-menu pages: All Day, Breakfast, Drinks, Puddings) [data]. For us that means Menu tabs, not extra pages.
4. **Write one line of vibe copy that is a promise** (Dishoom "love letter to Bombay"; Saffy's "eat with your hands, drink with your friends") [data]. We write ours; never a claim.
5. **Pause controls on moving heroes** (Atelier Crenn and Dado's) [data].
6. **Story as proof**: producers, farms, people (Atelier Crenn, Monmouth, Ozone, Noma) [data]. Only if the owner supplies it.

**What nobody does, but the evidence says we should**
1. **The Vietnam overlay.** 0 of 19 show Zalo, GrabFood or ShopeeFood, including our own two and the two other Vietnamese sites [data]. The two delivery apps hold over 90% of delivery [data: INDUSTRY.md]. A Zalo-first bar and Grab/ShopeeFood buttons are open ground.
2. **An essentials strip** (open now, hours, call or Zalo, directions) in the first screen. 0 of 19 [data]. 64% of customers check hours and location [research]; only 8.6% of Istanbul sites show hours [data].
3. **Open-now computed from hours**, and a **written "how to find us"** from landmarks. 0 of 19 [data]. Answers the second job, and gives Google text.
4. **Amenity chips from the Maps listing** (wifi, outdoor, laptop, kids, parking). 0 of 19 as a block [data]; the enrichment trial found attributes for 8 of 10 cafes [data].
5. **Price with its source**, "Prices from their menu, Sep 2026". 0 of 19 [data]. Turns Shaan's real-prices rule into trust.
6. **A thin-data form for every slot.** Every platform and every study assumes a full client. Ours must look finished at 3 photos and 12 reviews.
7. **Both widths as equals**, with the key actions in the header on desktop and in the bar on phone. Only 4 of 19 expose a fixed bar [data].

## 6. Gaps for UI-HUB: slots with no good built variant yet

| Gap | Why | What to build |
|---|---|---|
| **Essentials strip with Zalo and Grab/ShopeeFood** | restaurant-app's strip has WhatsApp and chat chips only; INDUSTRY-RUN core gap | Static chip row: open-now, hours, Zalo, Call, Directions, Grab, ShopeeFood; each hides when its field is empty |
| **Static, photo-led hero for thin data** | INDUSTRY-RUN core gap; the 15 restaurant-app heroes assume video or a full set | One-photo hero with scrim and wordmark fallback; one action |
| **Sticky bar that adapts to which actions exist** | Cafe 89's has 3 fixed buttons, Kikas's 2 | 2 to 4 buttons, each driven by a field, Directions as the floor |
| **Menu page for 0 to 15 items, no prices, no photos** | menu-section assumes a full item list, prices and images; the Menu domain is "planned" | Text-row list, category chips, source-aware price column, "see on Grab" fallback |
| **Reviews at 12 and below** | review-section assumes 3 featured Supabase reviews; no "from Google" attribution | Static quote row with rating, count, Google link; hides under 5 |
| **What it's like from Maps attributes** | Cafe 89's "our corner" is hand-written | Chip and card block filled from `attributes[]` |
| **How to find us, FAQ from facts, price source note** | not built | Small text blocks generated from known fields |
| **Reservations without a booking system** | restaurant-app's is a full app domain | A "Reserve on Zalo / call / link" block; no calendar |
| **Events, private dining, catering** | none in restaurant-app | One text-and-photo block with an enquiry link (restaurants and bars only) |
| **Dietary tags** | "planned" DishCard | Tag chips on item rows |
| **Vietnamese and English text on every slot** | only Cafe 89 has `data-vi/en` | Tokenised copy for every slot; the switch in the header |
| **Gallery below 6 photos** | gallery-section/grid and the masonry assume a full set | Rule: fold into Hero and What it's like |

**Already well covered:** reviews (12 restaurant-app variants), heroes (15), story and timeline, team, map, footer (Kikas), Instagram grid. Nothing in the restaurant-app has been re-platformed onto tokens yet (INDUSTRY-RUN section 3.1), which is the real work.

## 7. Open items
- The Ariker 2012 list of 29 items was not obtained; Toast and Square sites were not verified (platforms note).
- Counts are floors on thin renders; a rendered-DOM pass (headless) on the 5 JS sites would tighten them.
- NN/g carousel and WCAG 2.2.2 are cited from memory, not re-fetched this run.
- INDUSTRY.md says "real prices only, with a source"; the checklist check says "no prices, ever". I followed ADR 0003 as INDUSTRY.md states it (sourced prices allowed). UI-HUB: confirm with Shaan.
