---
title: "Site anatomy: services + booking module (beauty salon, hair salon, nail salon, barber, spa and massage as skins)"
---

# Site anatomy: the services + booking module

Written by SISO-AGENCY (reader), 7 Oct 2026, for UI-HUB (ask t-0496). Same shape as `packs/restaurants/07-site-anatomy.md`. Machine twin: `slots.json` (36 slots, same text).
Tags: **[data]** = counted by us from fetched HTML; **[by eye]** = looked at in a headless browser screenshot; **[research]** = a published source; **[reasoned]** = our inference or an ADR.
Field names: `business.*` are in the frozen `site.json/1`. Everything else (`services[]`, `staff[]`, `booking.*`, `policy.*`, `photos[]`, `hours`, `rating`, `reviews[]`, `contact.*`, `attributes[]`) is a **proposed name** for SISO-SITES to confirm.

## 1. Sources, and how honest the counts are
- 43 candidate URLs tried (final run) with `sites/_fetch.py` (free, no model); **32 of 43 loaded** (31 distinct sites; Pall Mall was listed twice) (HTTP 200; Treatwell, Drybar, Rainbow Room, Great Clips, Four Seasons blocked or dead; the rest of the guessed Vietnamese and Thai URLs did not exist). Raw JSON: `_data/siso-agency/industries/pack-salons/`.
- Of the 32: **6 are booking platforms** (Fresha, Booksy, Vagaro, GlossGenius, Mindbody, Square Appointments), **4 are product brands with salons attached** (Hershesons, Murdock, Nails Inc, Sanctuary), **5 rendered as JavaScript shells** (Sassoon, Blow Dry Bar, Bluntcut, Health Land, Heavenly Spa; 30Shine rendered by eye only), 1 is a Japanese-language mirror (Asia Herb). That leaves **17 readable operator sites** (Pall Mall, Toni&Guy, Floyd's, Murdock, Hershesons, Nails Inc, Lash Lounge, Massage Envy, Elements, Oasis, Let's Relax, Divana, Best Spa Hoi An, Dahan Spa Hoi An, Halo Hoi An, Bamboo Spa VN, Hairsalon Da Nang). Every "n of 17" below is over those 17; it is a floor for JS sites and a ceiling for regex (the regexes read nav words, so `staff`, `careers`, `newsletter` over-fire).
- Eight homepages were looked at by eye: Pall Mall, Toni&Guy, Best Spa Hoi An, Dahan Spa, Halo Hoi An, 30Shine, Let's Relax, Oasis.
- **Gap:** only 8 of 17 are Southeast Asian and only 5 small Vietnamese salons were reachable. Bangkok and Hoi An independents mostly have no site of their own, which is exactly our market. NYC independents (Rainbow Room, Jin Soon) did not load. Treatwell (the biggest EU marketplace) blocked us.
- **What we own, `siso-booking-kit`** (SISO fork of MIT `thebookingkit`; module copy at `_archive/2026-08-27-melanotresses-site-public-safe/modules/siso-booking`): timezone-aware slot maths, `BookingCalendar.jsx` (calendar + slots + form), `BookingAdmin.jsx` (operator screen: close a date, override hours, cancel), Cloudflare handlers, D1 atomic overlap-guarded insert, optional Stripe deposit, Resend mail, private `.ics`, cancel tokens, honest `configured:false` health. **It is a booking engine, not a salon site.** It has no service list, price board, staff cards, gallery or hero. Those are what UI-HUB must build; the restaurant kit's header, bars, footer, reviews, hero, map and team sections carry over.

## 2. The sitemap

| Page type | n/17 | Who | Do we ship it? |
|---|---|---|---|
| Home | 17 | all | Yes |
| Services and prices (page or section) | 15 | Halo, Pall Mall, Dahan, Let's Relax, Best Spa, Bamboo Spa, Oasis | Yes, always. It is the core page: **a price board is the menu** |
| Book (page or entry) | 17 | Halo `/dat-lich/`, Pall Mall `/book-online/`, Let's Relax booking sub-domain, Murdock bookings sub-domain | Yes, as a page at tier 2 and a button always |
| Team / stylists / barbers | 12 (weak) | Pall Mall BARBERS, T&G Our Experts, Massage Envy | Only with named real staff |
| Gallery / photos | 11 | Best Spa, Dahan, Halo | Section; page at 6+ photos |
| About / story | not counted | most | Home block, page when sourced |
| Contact / Visit | 16 | all with hours | Yes, always |
| Gift cards, memberships | 12, 11 | US/UK chains, Oasis | No in Vietnam; one band elsewhere only if the owner lists it |
| Locations (groups) | 8 | T&G, Let's Relax, Oasis, Pall Mall | No for single sites |
| Shop / products | 8 | brands | No (Catalogue module) |
| Careers / academy | 12 | chains | No (R19) |
| Blog / news | not counted | Best Spa, Halo, Bamboo | No |

**Shape follows data richness [reasoned]**

| Tier | What the business has | Shape |
|---|---|---|
| 0 Below the gate | under 3 photos, or no hours, address or rating | One-pager: Hero, Services list (names only), Visit, contact rail; `noindex` |
| 1 Passed, thin | 3-5 photos, a price board photo or listing, 12 reviews | One-pager with anchors: Services and prices, Gallery, Visit; Book = Zalo/WhatsApp/Call |
| 2 Rich | 6+ photos, priced services, named staff, 25+ reviews | Home, Services, Team, Gallery, Visit; Book page |
| 3 Claimed | owner gave hours and services | Tier 2 plus live calendar (siso-booking-kit) |

## 3. The slots, page by page, in order

Order on Home is the order on the page. "Built by us" names either `siso-booking-kit` (calendar only) or restaurant-app, Cafe 89 and Kikas sections we can adapt. "Variants worth building" are clearly different looks for the variation engine (`hq/direction/VARIATION-ENGINE.md`: 2-4 per slot).

### Global

| Slot | Job | Prevalence | Variants worth building | Built by us | Thin-data behaviour | Reads (`site.json`) |
|---|---|---|---|---|---|---|
| **Header + nav + language** | Name, 3-5 links (Services, Team, Gallery, Visit), language flags, one Book button always visible | 17/17. every operator has a header; 17 of 17 carry a Book/Reserve control in or beside it (Pall Mall: BOOK NOW + SHOP NOW boxes; Best Spa: green pill; T&G: BOOK first link); 8 of 17 have a language switch (Halo flags EN/KO/VN; Dahan KO/EN/JA/ZH) | Top bar + Book pill; centred logo split nav (Halo); dark bar with outlined Book; drawer for secondary links only | Cafe 89 header with data-vi/en switch; restaurant-app nav (top, dark side, full-screen drawer) | Wordmark from name; Services, Visit only if no staff or gallery; Book pill = Zalo/call link until booking exists; switch only for languages we have copy in | `['business.name', 'logo.wordmark', 'nav.items[]', 'langs[]', 'booking.url|contact.primary_action']` |
| **Sticky contact rail / action bar** | Call, Zalo/WhatsApp/LINE/Kakao and Book under the thumb on every page | 8/17. Best Spa, Halo, 30Shine, Dahan (6 chat apps in a row), Oasis, Let's Relax, Health Land float a right or left rail of Call/Zalo/WhatsApp/Messenger; 8 of 8 SEA sites have one, 0 of the UK/US barber and hair sites | Right-edge vertical icon rail (Best Spa, 30Shine); left floating pills with number printed (Halo); bottom 3-button bar (Book, Call, Zalo); header row of chat logos (Dahan) | Cafe 89 mobile-bar; Kikas mobile-shortcuts; restaurant-app cta-section/primary | Never hide. Directions always exists; add Zalo/Call/WhatsApp/LINE/Kakao only when the real handle exists; Book only when booking exists, else Call replaces it | `['contact.zalo', 'contact.phone', 'contact.whatsapp', 'contact.line', 'contact.kakao', 'business.maps_url', 'booking.url']` |
| **Footer** | Hours, address, map, contact, socials, language, SISO heart + icon | 16/17. 16 of 17 show hours; footers carry the cancellation line on 4 of 17 | F4 full info (hours, map, channels); F3 dark minimal row; F2 taped card; F1 ghost wordmark | Kikas footer; Cafe 89 footer; restaurant-app RestaurantFooterPro | Always shown; drop empty columns; minimum name, address, map, SISO mark | `['business.*', 'hours', 'contact.*', 'business.social', 'langs[]']` |
| **SEO and schema** | HairSalon / BeautySalon / NailSalon / DaySpa / BarberShop LocalBusiness schema with hasOfferCatalog, noindex under the gate | not countable from HTML. invisible in HTML outlines; schema type regex found on a minority; Reserve-with-Google is the platform lever (GlossGenius, Square, Fresha all pitch it) | Not a UI slot (SISO-SITES machine) | SISO-SITES machine | Below the gate publish noindex; schema fields only for data that exists; skin sets the @type (barber = BarberShop, nails = NailSalon, spa = DaySpa, hair = HairSalon, else BeautySalon) | `['business.*', 'hours', 'rating', 'services[]', 'gate.passed']` |

### Home

| Slot | Job | Prevalence | Variants worth building | Built by us | Thin-data behaviour | Reads (`site.json`) |
|---|---|---|---|---|---|---|
| **Hero** | Say what and where in 2 seconds; one action (Book) | 17/17. Book button in hero: Pall Mall, Best Spa (Book a Treatment + Our Services), 30Shine (phone-number box), Toni&Guy via BOOK nav; no auto-rotation needed but 15 of 17 ship a carousel; moving hero: Pall Mall video + arrows, T&G full-bleed video | Full-bleed one photo + scrim + Book (Best Spa); three-up photo strip of real cuts (Halo: three side-by-side client photos, no text); product-detail close crop (Dahan oil pour); promo banner with phone-number box (30Shine) | restaurant-app hero-section (15 templates); Cafe 89 hero; Kikas hero | With 3+ photos: still full-bleed with scrim, name, one line ('Hair salon, Hoi An'), Book (Zalo/Call). With 0-2 photos: wordmark-led on a generated texture of the skin (never fake interiors) | `['photos[]', 'business.name', 'business.category', 'booking.url|contact.primary_action']` |
| **Essentials strip** | Open now, hours, phone/Zalo, directions in one glance | 5/17. Halo shows hours + phone in a top bar on every page; Best Spa strip of 4 trust chips (therapists, oils, hotel pick-up, near beach); nobody shows computed 'open now' | Top utility bar with hours + phone (Halo); chip row of real attributes (Best Spa); open-now pill under hero | restaurant-app essentials-section/primary | Show only what exists; open-now from hours; no hours = address + Directions only | `['hours', 'business.address', 'contact.*', 'attributes[]']` |
| **Services overview** | The 3-8 service families with a from-price and an arrow to the full list | 15/17. 30Shine cards (Cat toc from 94.000 VND, Uon dinh hinh from 386.000, doi mau from 199.000); Best Spa Signature Treatments 'from 1.100.000 VND' + RESERVE NOW; Let's Relax cards with THB price + Booking button | Photo cards with from-price (30Shine); signature 2-3 with Reserve button (Best Spa); text list with durations; tabbed families (Hair, Colour, Nails) | restaurant-app menu-section (adapt); NO service-card block in the kit | From the price board photo or listing only: family names, no prices unless real and sourced; 'See prices on Zalo' when none | `['services[].name', 'services[].price?', 'services[].duration?', 'services[].source']` |
| **Featured / signature treatments** | 1-3 best sellers with price, duration and Book | 9/17. Best Spa two signature packages; Let's Relax four-hands massage tier; Oasis 2h / 2.5h / 3h+ package rows; Dahan menu and prices page | Two-up signature cards with Reserve (Best Spa); duration ladder 60/90/120 (Bamboo Spa nav items are literally these); single hero treatment | none | Only when the price board lists packages; else hide | `['services[].featured', 'services[].price', 'services[].duration']` |
| **Team teaser** | 3-4 faces of real people with role, links to Team | 12/17. staff regex 12 of 17 but mostly nav words; Pall Mall BARBERS page, T&G Our Experts, Massage Envy Therapists | Face row with first name + role; barber picker cards (book with this barber) | restaurant-app team section | Hide unless named staff exist in their own page or Maps photos captions; never invent a stylist | `['staff[].name', 'staff[].role', 'staff[].photo']` |
| **Before / after + work gallery** | Proof of the result: real client work | 12/17. Halo hero IS three real client photos; Lash Lounge Before & After nav; Dahan photos page; before/after regex only 2 of 17, gallery 11 of 17 | Three-up real-work strip (Halo); before/after slider (2 photos); masonry; Instagram grid | restaurant-app gallery-section grid/masonry; Instagram grid | Under 6 photos fold into Hero; owner photos only; generated imagery shows the kind of work (never claimed as theirs) and is labelled | `['photos[].kind', 'photos[].url', 'instagram.handle']` |
| **Reviews and proof** | Real rating + count + 1-3 real quotes | 16/17. Best Spa shows dated TripAdvisor-style quotes; Pall Mall quotes '24,000+ 5-star reviews'; 30Shine runs a star rating prompt | Rating + count from Google chip; 3-quote row; quote carousel with pause; platform rating badge | restaurant-app review-section (12 variants) | Real rating and count with Google link; under 5 reviews hide the slot; never paraphrase | `['rating', 'review_count', 'reviews[]', 'maps_url']` |
| **How booking works / what to expect** | Three steps and what happens after you book (deposit, reminder, late policy) | 6/17. Lash Lounge What To Expect + FAQs; Dahan booking form; 30Shine 'book in 30 seconds, pay after the cut, cancel free' | Three-step strip; 'what to expect' card; policy line under the button | none | Only the facts we know (call/Zalo to book); no policy text we did not source | `['booking.steps[]', 'policy.*']` |
| **Memberships, packages, gift cards** | Offer to come back or give a visit | 12/17. gift cards 12 of 17, memberships 11 of 17 (mostly US/UK chains: Massage Envy, Elements, Lash Lounge, Hershesons); in SEA: Oasis online gift redeem, Let's Relax packages; absent at Vietnamese small shops | One-line band (gift card + membership) not a page; package ladder (3 sessions, 10 sessions); voucher QR | none | OFF unless the owner lists it; no gift card page in Vietnam | `['offers.gift_cards', 'offers.memberships', 'offers.packages[]']` |
| **Location teaser** | Address, map link, 'how to find us' in two lines | 7/17. map embeds on 7 of 17 | Static map card with Directions; landmark line; Grab link | restaurant-app/Kikas map | Address + Directions from maps_url; no embed below gate | `['business.address', 'business.maps_url', 'landmarks[]']` |
| **FAQ** | Answers from known facts (parking, payment, walk-in, language spoken) | not countable from HTML. FAQ pages on Lash Lounge, Massage Envy, T&G; not on the Vietnamese sites | Accordion; chip questions | none | Generate only from site.json facts; hide otherwise (this is also the ADR 0013 assistant's list) | `['attributes[]', 'policy.*', 'langs[]']` |
| **Instagram / social strip** | Fresh work | 14/17. instagram links 14 of 17; Halo top bar socials | Grid of 6; link row | restaurant-app Instagram grid | Link only unless owner supplies photos | `['instagram.handle', 'photos[]']` |

### Services

| Slot | Job | Prevalence | Variants worth building | Built by us | Thin-data behaviour | Reads (`site.json`) |
|---|---|---|---|---|---|---|
| **Page header + category tabs** | Jump between Hair / Colour / Nails or Massage / Facial / Body without scrolling | 12/17. Best Spa has 6 child pages (Massage, Ear Care & Grooming, Facial, Hair Wash & Head Spa, Packages, Nail Care); Bamboo Spa per-package pages; Elements 12 massage types; Toni&Guy Services | Sticky tab chips; side category rail; accordion families | none | Category chips from service names; single list under 8 items | `['services[].category']` |
| **Price list** | Name, duration, price with its source, Book on the row | 15/17. Halo has a PRICE LIST page and BOOK NOW page; Pall Mall PRICE LIST page; Dahan menu and prices page; Let's Relax Spa Menu with THB; Best Spa VND from-prices | Rows with duration + price + Book button; price board photo image kept as the source; two-column price list per family; from-price only | none (the kit's service catalogue is host config with priceCents, no UI list) | Prices only from their own board photo or page, shown with 'Prices from their board, Sep 2026'; no price = name and duration only + 'Ask on Zalo' | `['services[].name', 'services[].price', 'services[].duration', 'services[].source']` |
| **Add-ons and durations** | Choose 60/90/120 or add a scrub/ear care | 5/17. Bamboo VIP 1 90 min / VIP 2 120 min; Oasis hour ladder; Elements Add-ons page | Duration segmented control; add-on checkbox rows | kit services[] has durationMinutes | Hide if only one duration known | `['services[].variants[]']` |
| **Per-service detail** | What it is, how long, who it suits (one paragraph, no claims) | 11/17. Elements and Massage Envy each have a page per massage type | Short detail drawer; inline expand | none | Only written by us about the kind of service, never claims | `['services[].description']` |
| **Dietary / skin / allergy notes** | Patch test, pregnancy, skin type warnings | 3/17. Elements Prenatal; Lash Lounge What to expect | Notice line per service | none | Only if the owner gives it; never inferred | `['services[].notes']` |

### Team

| Slot | Job | Prevalence | Variants worth building | Built by us | Thin-data behaviour | Reads (`site.json`) |
|---|---|---|---|---|---|---|
| **Staff / stylist profiles** | Name, role, speciality, photo; pick who to book | 12/17. Pall Mall BARBERS (each independent barber sets own prices and schedule); T&G Our Experts; Fresha/Vagaro/Booksy build their marketplace on per-pro profiles; Vagaro 'Professionals' nav | Grid of cards with Book with me; list with specialities; single owner profile | restaurant-app team section | One-person shops: owner line only if sourced; no invented stylists | `['staff[]']` |
| **Academy / careers** | Hire or train | 12/17. careers regex 12 of 17; T&G Pro Academy, Sassoon Academy | One link in footer | none | OFF on free preview (R19) | `['careers.url']` |

### Book

| Slot | Job | Prevalence | Variants worth building | Built by us | Thin-data behaviour | Reads (`site.json`) |
|---|---|---|---|---|---|---|
| **Booking entry** | Get from 'I want a haircut' to a confirmed slot | 17/17. Every site has a Book control. Destinations seen: own page (Pall Mall /book-online/, Halo /dat-lich/), sub-domain booking engine (Murdock bookings. sub-domain, Let's Relax booking.letsrelaxspa.com/book), salon finder first for groups (Toni&Guy), a form (Dahan reservation form page), phone-number box with callback (30Shine), WhatsApp/Zalo/LINE only (Oasis, Best Spa rail) | A: in-page calendar + slots (our kit); B: Zalo/WhatsApp/LINE deep link with prefilled text; C: request form (name, service, time, channel); D: hand-off to their own platform link (Fresha/Booksy/Vagaro/Treatwell) | siso-booking-kit BookingCalendar + server/booking-handler (D1 atomic overlap guard, deposits via Stripe, .ics, cancel tokens), BookingAdmin | UNCLAIMED: Book = Zalo (VN), WhatsApp or LINE (TH) or Call using the real number; if a Fresha/Booksy/Vagaro URL is on their Maps listing use it (D). Never show a calendar with invented availability. CLAIMED: calendar from owner's hours + services (A). | `['booking.mode', 'booking.url', 'contact.*', 'services[]', 'hours']` |
| **Service + staff + time picker** | Choose service, optionally person, then slot | 7/17. 7 of 17 route into a booking_platform (Fresha/Vagaro/Mindbody/etc by regex) | Service-first stepper; barber-first; calendar-first | kit BookingCalendar (services, slot grid, form) | Only after claim | `['services[]', 'staff[]', 'availability']` |
| **Deposit and cancellation policy** | Set expectations and cut no-shows | 4/17. deposit/cancellation regex 4 of 17 (Murdock, Oasis, Divana, Dahan); platforms (GlossGenius No-Show Protection, Square cancellation template) sell it | One-line policy under Book; checkbox | kit: Stripe deposit mode + cancellation tokens | Only owner's stated policy; none = no line | `['policy.deposit', 'policy.cancel']` |
| **Confirmation + reminders** | Say it worked and add to calendar | not countable from HTML. platforms: reminders, .ics; not visible in static HTML | On-page confirmation + .ics; message via Zalo/WhatsApp | kit .ics export + Resend mail | Not offered unclaimed | `['booking.confirmation']` |

### Visit

| Slot | Job | Prevalence | Variants worth building | Built by us | Thin-data behaviour | Reads (`site.json`) |
|---|---|---|---|---|---|---|
| **Hours** | Opening hours incl. late nights, lunch closures | 16/17. hours strings on 16 of 17; Halo 08:00-19:00 in top bar | Open-now pill + week table; compact line | Cafe 89 | Hours from Maps only if verified; else 'call to confirm' | `['hours']` |
| **Map + directions + parking** | Find it and arrive | 7/17. map embed 7 of 17 | Directions button; static map; Grab link | Kikas/Cafe 89 map | Directions link only | `['business.maps_url', 'parking']` |
| **Contact channels** | Zalo, phone, WhatsApp, LINE, Kakao, Messenger by local habit | 8/17. Dahan shows Kakao, LINE, WhatsApp, Zalo, Telegram, Instagram in one row; Halo Zalo, WhatsApp, phone, Messenger | Icon row with real handles; QR codes for Zalo/LINE | none | Only handles that exist; Vietnam order Zalo, phone, Messenger (ADR 0008) | `['contact.*']` |
| **Walk-in / good to know** | Walk-ins welcome, hotel pick-up, languages spoken, payment | 6/17. Best Spa: Free Hotel Pick-up chip; Pall Mall 'walk-ins welcome anytime' | Chip list | none | Amenities from Maps attributes only | `['attributes[]']` |

### Optional

| Slot | Job | Prevalence | Variants worth building | Built by us | Thin-data behaviour | Reads (`site.json`) |
|---|---|---|---|---|---|---|
| **Shop / retail** | Sell products | 8/17. shop_retail 8 of 17 mostly brands (Hershesons, Murdock, Nails Inc, Sanctuary are really shops with a salon) | none | none | OFF; Catalogue module | `['shop.url']` |
| **Locations list (groups)** | Pick a branch before booking | 8/17. T&G salon finder; Let's Relax, Oasis, Health Land, Pall Mall | Branch cards | none | OFF for single sites | `['locations[]']` |
| **Skin: nails extra** | Style catalogue (colours, art, press-on) and a nail-art photo basket | not countable from HTML. Nails Inc, Lash Lounge style pages; see skins in 07 | Photo basket grid | none | Only owner/nail photos | `['photos[kind=nail]']` |
| **Skin: barber extra** | Barber picker, walk-in queue, shave and beard services | not countable from HTML. Pall Mall barbers page, Floyd's | Barber cards | none | Walk-in line only if stated | `['staff[]', 'policy.walkin']` |
| **Skin: spa extra** | Treatment rooms, therapist gender request, duration ladder, couples | not countable from HTML. Oasis, Bamboo, Let's Relax, Best Spa | Duration ladder + add-ons | none | Only stated options | `['services[].variants[]']` |

## 4. The booking flow the best sites use

1. **One Book control in the header and in the hero, same label, never hidden.** 17 of 17 [data]. Pall Mall pairs BOOK NOW with SHOP NOW; Best Spa uses a filled pill; Toni&Guy puts BOOK first in the nav [by eye].
2. **Pick where, then what, then when.** Groups (Toni&Guy: salon finder first) ask for the branch; independents skip straight to service. Service-first is how Halo and Pall Mall's own booking pages start [data: URLs].
3. **Prices sit on the choice step.** Let's Relax and Best Spa show the price and a Book/Reserve button on each treatment row [by eye]. This is the single strongest pattern: *price, duration, Book on the same row*.
4. **A low-friction fallback beside the calendar.** Every SEA site pairs the form with a chat rail: Halo (Zalo, WhatsApp, phone, Messenger), Best Spa (Call, Zalo, Facebook, map), Dahan (Kakao, LINE, WhatsApp, Zalo, Telegram) [by eye]. 8 of 8 SEA operators; 0 of the UK/US barber and hair sites [data].
5. **Phone number as booking (30Shine).** The hero has a box "enter your phone number to book, pay after the cut, cancel for free"; the chain calls back. That is Vietnam's native form of booking and needs no calendar [by eye].
6. **Deposit and cancellation line under the button** on 4 of 17 [data] and sold as a feature by GlossGenius ("No-Show Protection") and Square ("Cancellation Policy Template") [data].

**What this means for us:** the booking kit is the claimed state. For an unclaimed Maps-only site, the booking slot is a **channel button**: Zalo deep link (VN), WhatsApp or LINE (TH, tourists), phone otherwise; Fresha/Booksy/Vagaro URL if the Maps listing carries one. No calendar, no invented availability (ADR 0003).

## 5. What the best do that most don't, by eye

1. **Halo Hoi An: the hero is three real client photos side by side**, no text, no stock; the proof of work is the hero. Top bar prints hours and phone; floating Zalo, WhatsApp and phone pills; EN/KO/VN flags in the nav [by eye]. Cheapest, truest design on the list.
2. **Best Spa Hoi An: a four-chip trust strip** (therapists, oils, free hotel pick-up, near An Bang beach) under the hero, plus from-prices and a Reserve button on each signature treatment, plus a right-edge rail (Call, Zalo, Facebook, map) [by eye].
3. **Dahan Spa: the language switch is the first element** (KO, EN, JA, ZH flags), and six chat logos under the wordmark. The site is written Korean-first because Korean visitors are its market [by eye]. Confirms ADR 0008: languages follow visitors, and Hoi An/Da Nang need Korean.
4. **30Shine: the price is on the service card** ("from 94.000 VND"), the booking box asks only for a phone number, a star prompt sits next to it [by eye].
5. **Pall Mall: video hero with one BOOK NOW**, barber-by-barber pages, and an honest "walk-ins welcome" [by eye]. **Toni&Guy: the opposite**, a muted blurry video, a cookie wall on top and BOOK that leads to a salon finder; heavy for a phone [by eye]. Avoid.

**What nobody does but should**
1. **Computed "open now" from hours** (0 of 17 [data]).
2. **Price with its source**, "prices from their board, Sep 2026" (0 of 17).
3. **Zalo-first booking on a clean fast static page**: the SEA sites have the rail but cluttered pages (carousels on 15 of 17 [data]).
4. **A thin-data form for every slot**: every platform assumes a claimed account.
5. **Barber-style walk-in status** without a calendar.

## 6. Rules attached to slots (extends restaurants R1-R20)
- **S1** One Book action, same label everywhere; on Maps-only data it is a channel button, not a calendar. [data: 17 of 17 have one]
- **S2** Prices only when real and sourced (board photo, own page, platform listing). A service list with no prices beats a wrong price. [ADR 0003; 15 of 17 show prices [data]]
- **S3** No invented staff, no invented before/after, no invented policy. Staff and policy only from their own page. [ADR 0003]
- **S4** Chat rail on phone for SEA: Zalo then phone then Messenger (VN), WhatsApp and LINE (TH), Kakao added where Korean visitors show up. [ADR 0008; [by eye] 5 of 5]
- **S5** Hero is a still; any gallery has a pause control. [ADR 0007; 15 of 17 ship a carousel [data]]
- **S6** Real client work only in the gallery; generated imagery shows the kind of treatment and is never claimed as theirs. [R8]
- **S7** No gift card, membership, shop or careers page unless the owner lists it. [R19, ADR 0011]
- **S8** Prices in local currency as written (VND with dots, THB). Never convert.
- **S9** The assistant (ADR 0013) answers only: hours, where, walk-in, price of a listed service, languages spoken, how to book.

## 7. Per-skin differences

| Skin | Photo basket | Extra slot | Services emphasis | Booking emphasis |
|---|---|---|---|---|
| **Hair salon** | cuts and colour on real people, chairs, entrance | Before/after strip; stylist cards | cut, colour, treatment, wash/blow-dry; price from-ranges by hair length | by stylist and service; Zalo for VN |
| **Barber** | chair, fade close-ups, shop front | Barber picker; walk-in status | cut, beard, shave, head wash (30Shine and Pall Mall model) | walk-in first; call or Zalo; calendar optional |
| **Nail salon** | hands: sets, art, colours; table setups | Style catalogue (colour, art, gel/acrylic) | set, fill, gel, pedicure; duration matters (60-120 min) | fortnightly regulars; rebook link; photo of design sent over Zalo |
| **Beauty salon** | facial/lash/brow results, treatment room | Treatment menu by area (face, lash, brow, wax) | many small priced items; patch-test note | by treatment; deposit more common |
| **Spa / massage** | rooms, garden, oils; therapist at work | Duration ladder (60/90/120); couples; hotel pick-up | package ladders, add-ons; foreign visitors; USD/THB habit | WhatsApp/Zalo/LINE/Kakao rail; hotel pick-up; deposit rare |

Personality for the variation engine [reasoned]: barber = street or premium; hair = lively or cosy; nails = playful; beauty = calm; spa = calm or cosy.

## 8. The Vietnam overlay (ADR 0008)
- **Channels:** Zalo deep link first (`zalo.me/<number>`), then phone, then Messenger; Facebook page last. Halo, Best Spa, Dahan, Bamboo all carry these [by eye + data].
- **Languages:** VI first; EN switch; **KO for Đà Nẵng and Hội An** (Dahan's whole site is Korean-first); ZH where reviews show it. Header flag switch like Halo and Dahan.
- **Booking:** Zalo or callback replaces the calendar for walk-in-led shops (30Shine's phone box). Grab link for "get there" is useful for spas (hotel guests).
- **Prices:** VND with dots (`1.100.000 VND`, `94.000VND`), "from" prices on cards, taken from the price board photo; most small shops post prices as a photo, which we read once at build time and cite.
- **Habit:** hotel pick-up (free) is a headline benefit at Hoi An spas; show only if listed.
- **Thailand:** LINE and WhatsApp for tourists; THB prices; Let's Relax and Oasis are chains with branch lists.

## 9. Gaps for UI-HUB: what is not built

| Gap | Why | What to build |
|---|---|---|
| **Service price board** (rows, durations, source note, Book on row) | the kit has `services[]` config but no UI list | One list component with 3 variants (rows, two-column, from-price cards) |
| **Staff / barber cards** | restaurant team section is bio-heavy | Card row: face, first name, role, Book with me; hides without real staff |
| **Booking entry that adapts** | kit is a calendar only | Button that resolves to Zalo, WhatsApp, LINE, Call, platform URL or the calendar from `booking.mode` |
| **Contact rail** with 3-7 channels incl. Kakao and LINE | restaurant bars have 2-4 | Rail/bottom-bar variants driven by `contact.*` |
| **Work gallery under 6 photos** | restaurant gallery assumes more | Three-up real-work strip (the Halo pattern) |
| **Language switch with KO** | Cafe 89 only VI/EN | Tokenised copy, flag switch |
| **Trust chip strip** | none | Chips from attributes (Best Spa pattern) |
| **Price-source note and open-now** | not built | small text blocks |

## 10. Open items
- Treatwell, Drybar, Rainbow Room, Jin Soon, Great Clips, Sassoon (JS) not read; NYC and EU marketplace patterns are from vendor pages only (Fresha, Booksy, Vagaro, GlossGenius, Square), shallow.
- Booking flows were read from nav targets and the home page, not by clicking through; step counts beyond entry are inferred from platform pages [reasoned].
- Skin-by-skin counts are not separable at N=17; per-skin claims in section 7 are mostly [reasoned].
