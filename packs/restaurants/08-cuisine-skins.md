# 08 Cuisine skins: one menu template, 39 skins

Shaan, 7 Oct 07:00: cuisines are not industries; they are skins on one menu template. This file groups the **416 menu rows** of `SISO_Agency/hq/industries/INDEX.csv` (task said 417; the file has 416) into **39 skins** plus one bucket (`not-menu`) of 10 misrouted service rows. Every row maps to exactly one skin (`skins.json` -> `mapping`, gcid -> skin).

**Rule (VARIATION-ENGINE §7):** a skin biases the personality's pools; it never replaces the personality. Palette schemes below are a bias on the personality's scheme, and type pairs are a bias on its T1–T6 pool.

**Counts:** no-site = Overture 2026-09-23.1, counted 7 Oct 2026, summed over Đà Nẵng, HCM, Bangkok, London. Rows are not de-duplicated across skins' parent rows (e.g. "Restaurant" 29,339 already includes businesses also tagged by cuisine), so the grand total (116,232) overstates unique businesses. Rank = summed no-site, then top score.

**Grounding:** reference sites were checked reachable on 7 Oct (HTTP 200) but conventions are **reasoned** unless a skin says otherwise; no page was read in depth. Two skins (`hotpot`, `izakaya-yakitori`) have zero no-site as matched, so they rank last.

## Rank table
| # | Skin | Rows | No-site | DN | HCM | BKK | LON |
|---|---|---|---|---|---|---|---|
| 1 | Everyday restaurant | 7 | 30,758 | 1,884 | 7,611 | 20,492 | 771 |
| 2 | Coffee house | 4 | 19,129 | 2,161 | 8,580 | 7,943 | 445 |
| 3 | Cafe and brunch | 4 | 11,569 | 1,267 | 4,546 | 4,788 | 968 |
| 4 | Thai restaurant | 1 | 9,057 | 31 | 202 | 8,771 | 53 |
| 5 | Bar, pub and nightlife | 11 | 5,197 | 292 | 876 | 2,594 | 1,435 |
| 6 | Fast food, burgers and fried chicken | 4 | 4,500 | 242 | 1,069 | 2,567 | 622 |
| 7 | Local eatery / diner | 7 | 3,760 | 633 | 2,805 | 307 | 15 |
| 8 | Noodle house | 10 | 3,288 | 58 | 205 | 3,019 | 6 |
| 9 | Vietnamese restaurant | 3 | 2,637 | 436 | 1,943 | 219 | 39 |
| 10 | Bakery and pastry | 2 | 2,583 | 222 | 848 | 1,243 | 270 |
| 11 | Bubble tea and drink stand | 1 | 2,576 | 201 | 1,541 | 797 | 37 |
| 12 | Japanese | 27 | 2,479 | 49 | 367 | 1,997 | 66 |
| 13 | Dessert and ice cream | 7 | 2,235 | 85 | 389 | 1,677 | 84 |
| 14 | Chinese | 18 | 2,014 | 61 | 475 | 1,279 | 199 |
| 15 | Seafood | 3 | 1,846 | 293 | 793 | 719 | 41 |
| 16 | Vegetarian, healthy and organic | 7 | 1,082 | 138 | 622 | 274 | 48 |
| 17 | Indian and South Asian | 38 | 980 | 62 | 202 | 546 | 170 |
| 18 | Steakhouse and meat dishes | 4 | 933 | 10 | 65 | 849 | 9 |
| 19 | Korean | 2 | 932 | 97 | 312 | 484 | 39 |
| 20 | Tea house | 2 | 896 | 97 | 456 | 310 | 33 |
| 21 | Sandwich, deli and snack | 7 | 868 | 33 | 90 | 614 | 131 |
| 22 | Cocktail, wine and lounge | 5 | 855 | 53 | 251 | 303 | 248 |
| 23 | BBQ and grill | 14 | 823 | 82 | 259 | 455 | 27 |
| 24 | Sushi | 3 | 781 | 20 | 121 | 584 | 56 |
| 25 | Pizzeria | 3 | 773 | 39 | 118 | 388 | 228 |
| 26 | Karaoke / KTV | 1 | 753 | 101 | 414 | 230 | 8 |
| 27 | Buffet and self-service | 3 | 659 | 16 | 60 | 577 | 6 |
| 28 | Juice and smoothie | 1 | 523 | 40 | 276 | 170 | 37 |
| 29 | Italian | 13 | 361 | 16 | 37 | 193 | 115 |
| 30 | Middle Eastern and Mediterranean | 23 | 303 | 4 | 8 | 56 | 235 |
| 31 | Latin American and Caribbean | 35 | 287 | 5 | 28 | 83 | 171 |
| 32 | European bistro and fine dining | 49 | 235 | 12 | 42 | 71 | 110 |
| 33 | Themed cafe | 8 | 199 | 31 | 123 | 35 | 10 |
| 34 | American and comfort | 23 | 107 | 3 | 17 | 55 | 32 |
| 35 | Southeast Asian regional | 30 | 104 | 3 | 18 | 63 | 20 |
| 36 | Kebab and shawarma | 7 | 99 | 0 | 3 | 23 | 73 |
| 37 | African restaurant | 7 | 51 | 1 | 1 | 3 | 46 |
| 38 | Hotpot | 7 | 0 | 0 | 0 | 0 | 0 |
| 39 | Izakaya and yakitori | 5 | 0 | 0 | 0 | 0 | 0 |
| – | Not a menu business | 10 | 0 | 0 | 0 | 0 | 0 |

---

## 1. Everyday restaurant (generic + pan-Asian + fusion)  (`everyday-restaurant`)
- **No-site total:** 30,758 (DN 1,884 / HCM 7,611 / BKK 20,492 / LON 771), top score 34.51. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (7):** Restaurant (29,339), Asian restaurant (1,363), Asian fusion restaurant (56), Eclectic restaurant, Fusion restaurant, Pan-Asian restaurant, Western restaurant
- **Why grouped:** The catch-all rows (Restaurant, Asian, Fusion, Eclectic, Western). No cuisine to lean on, so personality does all the work; this skin is the neutral baseline.
- **Photo basket:** lead = dish close-ups, interior, people. Slots: dish close-up -> hero and first 6 menu cards; interior -> atmosphere strip; people/staff -> about; exterior -> visit block.
- **Palette bias:** TonalSpot default; Neutral if calm; Vibrant if street. Follows the personality scheme unchanged. Ground: from hero photo tone.
- **Type bias:** Follows personality (T1/T4 cosy, T2/T6 street, T3/T5 premium). No skin bias.
- **Copy voice:** Plain, warm, specific: say what they cook and where.
  - VI: {name}: {dish} và {dish2}, nấu mỗi ngày / EN: {name}: {dish} and {dish2}, cooked daily
  - VI: Mở cửa {hours} tại {area} / EN: Open {hours} in {area}
  - VI: {rating} sao từ {n_reviews} lượt đánh giá / EN: {rating} stars from {n_reviews} reviews
- **Extra slot:** none
- **Menu shape:** By category as the business lists it (starters, mains, drinks); flat list when under ~15 items. Prices: Board photo or delivery app (Grab/ShopeeFood in VN, LINE MAN in Bangkok); if neither, show dishes without prices.
- **Pairs with personalities:** cosy, lively, calm
- **Reference:** mass-market casual menu-first site <https://www.wagamama.com>

## 2. Coffee house (coffee shop, stand, store)  (`coffee-house`)
- **No-site total:** 19,129 (DN 2,161 / HCM 8,580 / BKK 7,943 / LON 445), top score 28.35. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (4):** Coffee shop (19,129), Coffee stand, Coffee store, Coffee vending machine
- **Why grouped:** Vietnam-style coffee shops: drink-led, seating mood, signature drinks (cà phê muối, bạc xỉu). Merges coffee shop/stand/store/vending (same menu logic).
- **Photo basket:** lead = drink close-ups, interior, counter/barista. Slots: drink close-up -> hero and drink cards; interior seating -> atmosphere; counter/barista -> about; menu board -> menu fallback.
- **Palette bias:** TonalSpot or Fidelity (browns, creams) for cosy; Vibrant for street stands; Monochrome for specialty/premium. Ground: light cream ground by default; dark for evening-leaning interiors.
- **Type bias:** T1 (warm serif) for cosy; T4 for playful; T2 for street stands.
- **Copy voice:** Slow and sensory: the drink, the seat, the hour.
  - VI: {drink} – ly đặc trưng của {name} / EN: {drink}, the signature cup at {name}
  - VI: Chỗ ngồi {seating}, mở từ {open} / EN: Seating: {seating}. Open from {open}
  - VI: Ghé {area}, uống một ly / EN: Find us in {area}, have a cup
- **Extra slot:** none (optional: wifi/work-friendly badge only if reviews say it)
- **Menu shape:** By drink type (coffee, tea, smoothie, food), sizes as variants. Prices: Board photo most common; Grab/ShopeeFood listing second.
- **Pairs with personalities:** cosy, calm, street
- **Reference:** specialty coffee, photo-led product pages (reasoned; page not fetched) <https://www.blueboottlecoffee.com>

## 3. Cafe and brunch (cafe, brunch, breakfast, pancake)  (`cafe-brunch`)
- **No-site total:** 11,569 (DN 1,267 / HCM 4,546 / BKK 4,788 / LON 968), top score 27.93. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (4):** Cafe (11,005), Brunch restaurant (461), Pancake restaurant (103), Breakfast restaurant
- **Why grouped:** Food plus coffee, daytime. Brunch/breakfast/pancake have the same visual logic as cafe (plated food in daylight).
- **Photo basket:** lead = plated dishes, interior (daylight), drinks. Slots: plated dish -> hero; interior -> second hero or collage; drinks -> menu cards; people -> about.
- **Palette bias:** TonalSpot, Expressive for playful; FruitSalad if colourful plating. Ground: light.
- **Type bias:** T1 or T4 (rounded, friendly). T5 for minimal brunch spots.
- **Copy voice:** Bright and easy: the table, the light, the plate.
  - VI: Bữa sáng và brunch tại {name} / EN: Breakfast and brunch at {name}
  - VI: {dish} – món được nhắc nhiều nhất / EN: {dish}, the dish people mention most
  - VI: Mở cửa từ {open} / EN: Open from {open}
- **Extra slot:** none
- **Menu shape:** By daypart (breakfast, brunch, drinks, sweet) then category. Prices: Board photo or app; small menus often fully typed from photos.
- **Pairs with personalities:** cosy, playful, calm
- **Reference:** daylight bakery-cafe site, photo-led (reasoned) <https://www.gailsbread.co.uk>

## 4. Thai restaurant  (`thai`)
- **No-site total:** 9,057 (DN 31 / HCM 202 / BKK 8,771 / LON 53), top score 24.72. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (1):** Thai restaurant (9,057)
- **Why grouped:** The 4th largest single row, almost all Bangkok. Thai in Bangkok means everything from street stalls to dinner rooms; skin leans on dish colour and heat.
- **Photo basket:** lead = dish close-ups (curries, noodles), street counter / open wok, interior. Slots: dish close-up -> hero; open wok or street counter -> about; interior -> atmosphere.
- **Palette bias:** Vibrant or Expressive (chilli red, lime, gold); Fidelity for premium dining rooms. Ground: light for street; dark for premium.
- **Type bias:** T6 or T2 for street; T3 for premium; Thai script needs a Thai-capable fallback (not in T1–T6 guarantee: add to type check).
- **Copy voice:** Direct and flavour-first; heat level is a feature.
  - VI: {dish} cay vừa hoặc cay nhiều, tại {name} / EN: {dish}, made to your spice level, at {name}
  - VI: Ăn tại chỗ hoặc mang đi: {hours} / EN: Dine in or take away: {hours}
  - VI: {rating} sao – {n_reviews} đánh giá / EN: {rating} stars, {n_reviews} reviews
- **Extra slot:** Spice-level selector on dish cards (only when the menu data lists it); else none.
- **Menu shape:** By dish type (curries, stir-fries, noodles, rice, salads); sets for groups. Prices: Delivery app (LINE MAN/Grab) in Bangkok; board photo for street.
- **Pairs with personalities:** street, lively, premium
- **Reference:** Thai restaurant site, dish-led (reasoned) <https://www.thaitable.co.uk>; Thai cafe group, reachable 7 Oct <https://www.rosasthaicafe.com>

## 5. Bar, pub and nightlife (bar, pub, bar and grill, brewery, sports, queer, salsa)  (`pub-bar-nightlife`)
- **No-site total:** 5,197 (DN 292 / HCM 876 / BKK 2,594 / LON 1,435), top score 13.23. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (11):** Bar (2,890), Pub (1,101), Bar & grill (522), Queer bar (219), Salsa bar (216), Gastropub (140), Brewery (52), Sports bar (33), Gay bar (24), Dance restaurant, Brewpub
- **Why grouped:** Beer-and-night venues. Cocktail/wine/lounge split off because they are premium and photo-led; this group is volume and events.
- **Photo basket:** lead = interior at night, drinks/taps, people/crowd, events/DJ. Slots: night interior -> hero; taps/drinks -> menu cards; crowd/event -> events strip; exterior sign -> visit.
- **Palette bias:** Vibrant or Rainbow on dark; Expressive for playful venues. Ground: dark.
- **Type bias:** T2 or T6 (condensed, loud); T4 if playful.
- **Copy voice:** Short, loud, specific: what is on tonight.
  - VI: Đêm nay tại {name}: {event} / EN: Tonight at {name}: {event}
  - VI: Happy hour {happy_hours} / EN: Happy hour {happy_hours}
  - VI: Mở đến {close} / EN: Open until {close}
- **Extra slot:** Happy hour + events strip (only if hours/events exist in data); else none.
- **Menu shape:** By drink type (beer, cocktails, spirits, bites); bar bites last. Prices: Board photo; rarely on apps.
- **Pairs with personalities:** lively, street, playful
- **Reference:** reasoned (no live site read)

## 6. Fast food, burgers and fried chicken  (`fast-food-burger-chicken`)
- **No-site total:** 4,500 (DN 242 / HCM 1,069 / BKK 2,567 / LON 622), top score 15.74. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (4):** Fast food restaurant (3,123), Chicken restaurant (898), Hamburger restaurant (330), Fish & chips restaurant (149)
- **Why grouped:** Delivery-first formats: fast food, fried chicken, burgers, fish and chips (takeaway). The site is a menu plus an order button.
- **Photo basket:** lead = product shots (burger, bucket), counter, exterior. Slots: product shot -> hero; combo shots -> menu cards; counter/exterior -> visit.
- **Palette bias:** Vibrant or Rainbow (primary red/yellow); Expressive for playful. Ground: light, saturated.
- **Type bias:** T6 (heavy grotesk) or T4.
- **Copy voice:** Fast: item, price, order.
  - VI: Combo {combo} chỉ {price} / EN: {combo} combo, {price}
  - VI: Giao tận nơi trong {area} / EN: Delivery across {area}
  - VI: Mở đến {close} / EN: Open until {close}
- **Extra slot:** Delivery-first: order buttons (Grab/ShopeeFood/LINE MAN/own phone) above the fold; menu below.
- **Menu shape:** By combos then single items then sides/drinks. Prices: Delivery app almost always: pull prices from it.
- **Pairs with personalities:** street, playful, lively
- **Reference:** burger brand; order-first (403 to curl, not read) <https://www.honestburgers.co.uk>

## 7. Local eatery / diner (diner, cơm quán, family, lunch, takeout)  (`diner-eatery`)
- **No-site total:** 3,760 (DN 633 / HCM 2,805 / BKK 307 / LON 15), top score 22.34. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (7):** Diner (3,760), Family restaurant, Lunch restaurant, Meal delivery, Porridge restaurant, Rice restaurant, Takeout restaurant
- **Why grouped:** Surprising: "Diner" (3,760) in Vietnam and Thailand is the neighbourhood eatery (rice plates, set lunches), not an American diner. Merges family, lunch, rice, porridge, takeout, meal delivery.
- **Photo basket:** lead = tray/plate of the day, counter/display, street frontage. Slots: plate/tray -> hero; counter display -> menu; frontage -> visit (people find these by the street).
- **Palette bias:** TonalSpot, Neutral; Vibrant for loud street spots. Ground: light.
- **Type bias:** T5 or T6; T1 for family feel.
- **Copy voice:** Home-cooked and daily: what is on today.
  - VI: Hôm nay có: {dish}, {dish2} / EN: On today: {dish}, {dish2}
  - VI: Cơm trưa {price} / EN: Lunch plate {price}
  - VI: Gần {landmark}, mở {hours} / EN: Near {landmark}, open {hours}
- **Extra slot:** Daily specials strip only if the owner supplies it; else none.
- **Menu shape:** By set/plate then sides; rotating daily. Prices: Board photo, hand-written menu board (needs OCR); few apps.
- **Pairs with personalities:** street, cosy, calm
- **Reference:** reasoned (no live site read)

## 8. Noodle house (ramen, udon, soba, Chinese noodles, soup)  (`noodle-house`)
- **No-site total:** 3,288 (DN 58 / HCM 205 / BKK 3,019 / LON 6), top score 21.79. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (10):** Ramen restaurant (3,073), Soup restaurant (215), Chinese noodle restaurant, Champon noodle restaurant, Cold noodle restaurant, Dan Dan noodle restaurant, Noodle shop, Soba noodle shop, Udon noodle restaurant, Yakisoba Restaurant
- **Why grouped:** Merged on one logic: a bowl hero, a short menu by base/broth, toppings as modifiers. Ramen is the largest row (3,073). Pho stays in Vietnamese because its site looks and sounds different.
- **Photo basket:** lead = bowl close-up (steam), open kitchen/counter, interior (counter seats). Slots: bowl -> hero and each menu card; open kitchen/counter -> about; counter seats -> atmosphere.
- **Palette bias:** Vibrant or Fidelity; Monochrome for premium ramen bars. Ground: dark for ramen/izakaya feel; light for Chinese noodle.
- **Type bias:** T2 or T6 (condensed/heavy); T3 for premium.
- **Copy voice:** Broth-first, minimal: base, bowl, extras.
  - VI: {broth} – nước dùng ninh {hours_simmer} / EN: {broth}, simmered for {hours_simmer}
  - VI: Thêm topping: {topping} / EN: Add: {topping}
  - VI: {n_seats} chỗ ngồi tại quầy / EN: {n_seats} counter seats
- **Extra slot:** Base + toppings builder (only if toppings listed); else none.
- **Menu shape:** By base/broth, then toppings and sides. Prices: Board photo or app; fixed bowl prices common.
- **Pairs with personalities:** street, premium, lively
- **Reference:** ramen chain, bowl-led (reachable 7 Oct) <https://www.ippudo.com>; noodle bowl brand <https://www.wagamama.com>

## 9. Vietnamese restaurant (incl. pho, country food)  (`vietnamese`)
- **No-site total:** 2,637 (DN 436 / HCM 1,943 / BKK 219 / LON 39), top score 21.32. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (3):** Vietnamese restaurant (2,583), Country food restaurant (46), Pho restaurant (8)
- **Why grouped:** Local cuisine in DN and HCM. Includes pho and country food (món quê) because the table and the menu logic are the same.
- **Photo basket:** lead = dish close-ups (bún, phở, cơm), family table, market/ingredient shots. Slots: dish -> hero; table scene -> atmosphere; ingredients -> about.
- **Palette bias:** TonalSpot (herb green, chilli red), Fidelity. Ground: light.
- **Type bias:** T1 or T5; diacritics are the first check (full Vietnamese).
- **Copy voice:** Home and place: the dish, the region, the family.
  - VI: {dish} theo cách {region} / EN: {dish}, the {region} way
  - VI: Bàn {n_seats} chỗ, đặt trước {phone} / EN: Tables for {n_seats}, book on {phone}
  - VI: {n_reviews} khách đã ghé / EN: {n_reviews} guests have visited
- **Extra slot:** none
- **Menu shape:** By dish type (khai vị, món chính, canh, cơm, đồ uống). Prices: Board photo or Grab/ShopeeFood.
- **Pairs with personalities:** cosy, calm, street
- **Reference:** reasoned (no live site read)

## 10. Bakery and pastry  (`bakery-pastry`)
- **No-site total:** 2,583 (DN 222 / HCM 848 / BKK 1,243 / LON 270), top score 18.42. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (2):** Bakery (2,583), Chinese bakery
- **Why grouped:** Case-led: photos of the display. Pre-order cakes is the money slot.
- **Photo basket:** lead = display case, product close-ups (bread, cakes), people at counter. Slots: display case -> hero; product close-ups -> cards; baker -> about.
- **Palette bias:** TonalSpot or Content (warm neutrals); Expressive for cake shops. Ground: light.
- **Type bias:** T1 or T4.
- **Copy voice:** Fresh and made-by-hand: the bake, the hour.
  - VI: Ra lò mỗi sáng lúc {bake_time} / EN: Out of the oven daily at {bake_time}
  - VI: Đặt bánh trước {lead_days} ngày / EN: Order cakes {lead_days} days ahead
  - VI: {dish} – bán chạy nhất / EN: {dish}, the best seller
- **Extra slot:** Pre-order form for cakes (date, size, message), only if the business takes custom orders.
- **Menu shape:** By product (bread, pastry, cake) with a custom-order section. Prices: Board photo, Facebook posts, sometimes Zalo.
- **Pairs with personalities:** cosy, playful, calm
- **Reference:** bakery brand site (reachable 7 Oct) <https://www.gailsbakery.com>

## 11. Bubble tea and drink stand  (`bubble-tea`)
- **No-site total:** 2,576 (DN 201 / HCM 1,541 / BKK 797 / LON 37), top score 10.02. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (1):** Bubble tea store (2,576)
- **Why grouped:** Order-and-go with toppings: a builder UI more than a menu. 2,576 no-site, mostly HCM and Bangkok.
- **Photo basket:** lead = drink cup close-ups, storefront/counter, menu board. Slots: cup shots -> hero and cards; counter -> about; menu board -> OCR source.
- **Palette bias:** Expressive, FruitSalad (candy palette), Vibrant. Ground: light, saturated.
- **Type bias:** T4 or T6.
- **Copy voice:** Playful and short: flavour names, sizes.
  - VI: {drink} – chọn đường, đá, topping / EN: {drink}: choose sugar, ice and toppings
  - VI: Size M {price_m} · Size L {price_l} / EN: Size M {price_m} · Size L {price_l}
  - VI: Giao qua {app} / EN: Delivery via {app}
- **Extra slot:** Toppings builder (size, sugar, ice, toppings) if the menu has toppings.
- **Menu shape:** By drink type (milk tea, fruit tea, cheese foam, smoothies) + toppings list. Prices: Delivery app most often; board photo for stands.
- **Pairs with personalities:** playful, lively, street
- **Reference:** reasoned (no live site read)

## 12. Japanese (restaurant, regional, donburi, tonkatsu, tempura, curry, teishoku)  (`japanese`)
- **No-site total:** 2,479 (DN 49 / HCM 367 / BKK 1,997 / LON 66), top score 26.22. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (27):** Japanese restaurant (2,479), Authentic Japanese restaurant, Japanese curry restaurant, Japanese regional restaurant, Japanized western restaurant, Macrobiotic restaurant, Miso cutlet restaurant, Dojo restaurant, Monjayaki restaurant, Oden restaurant, Okonomiyaki restaurant, Donburi restaurant … +15 more
- **Why grouped:** All the Japanese sit-down formats except sushi, noodles and izakaya. Menu is by dish family; the photo story is plated dishes and clean interiors.
- **Photo basket:** lead = plated dishes (top-down), interior (wood, counter), chef/open kitchen. Slots: plated dish -> hero; chef/kitchen -> about; interior -> atmosphere.
- **Palette bias:** Monochrome or Fidelity (ink, wood, one red accent); Neutral for calm. Ground: light for casual; dark for ryotei/kaiseki.
- **Type bias:** T3 or T5; T1 for casual. Needs Japanese-capable fallback if the owner uses kanji.
- **Copy voice:** Precise and quiet: ingredient, technique, season.
  - VI: {dish} – {ingredient} theo mùa / EN: {dish}, with seasonal {ingredient}
  - VI: Set trưa {price} / EN: Lunch set {price}
  - VI: {n_seats} chỗ ngồi, đặt bàn {phone} / EN: {n_seats} seats, reserve on {phone}
- **Extra slot:** Set menus (course price, what is included) when the data has sets.
- **Menu shape:** By dish family (don, katsu, tempura, sets) with sets first. Prices: Board or delivery app; set menus on a photo.
- **Pairs with personalities:** premium, calm, cosy
- **Reference:** premium Japanese, photo-led (reachable 7 Oct) <https://www.nobu.com>; casual Japanese-inspired <https://www.wagamama.com>

## 13. Dessert and ice cream  (`dessert-ice-cream`)
- **No-site total:** 2,235 (DN 85 / HCM 389 / BKK 1,677 / LON 84), top score 13.04. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (7):** Dessert shop (1,206), Ice cream shop (1,029), Berry restaurant, Cendol restaurant, Chocolate cafe, Dessert restaurant, Sundae restaurant
- **Why grouped:** Dessert shops, ice cream, sundae, chè/cendol, chocolate cafe. Same macro-shots of sweet things and a flavour list.
- **Photo basket:** lead = dessert macro shots, flavour display, interior. Slots: macro shot -> hero; flavour tubs -> cards; interior -> atmosphere.
- **Palette bias:** Expressive, FruitSalad; Content for pastel shops. Ground: light, pastel.
- **Type bias:** T4 (rounded) or T1.
- **Copy voice:** Sweet and visual: names of flavours, not adjectives.
  - VI: {flavour}, {flavour2}, {flavour3} – đổi vị mỗi tuần / EN: {flavour}, {flavour2}, {flavour3}: flavours change weekly
  - VI: Ly {size}: {price} / EN: {size} cup: {price}
  - VI: Thêm topping: {topping} / EN: Add: {topping}
- **Extra slot:** Toppings/flavour builder when the data has toppings.
- **Menu shape:** By product (cup, cone, sundae) then toppings/flavours. Prices: Board photo or app.
- **Pairs with personalities:** playful, cosy, lively
- **Reference:** chocolate brand, macro-led (reachable 7 Oct) <https://www.hotelchocolat.com>

## 14. Chinese (regional, dim sum, dumplings, delivery)  (`chinese`)
- **No-site total:** 2,014 (DN 61 / HCM 475 / BKK 1,279 / LON 199), top score 20.36. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (18):** Chinese restaurant (1,813), Dim sum restaurant (155), Taiwanese restaurant (43), Dumpling restaurant (3), Delivery Chinese restaurant, Cantonese restaurant, Fujian restaurant, Hakka restaurant, Hunan restaurant, Jiangsu restaurant, Mandarin restaurant, Guizhou restaurant … +6 more
- **Why grouped:** Chinese incl. Cantonese, dim sum, dumplings, Taiwanese and the sub-regional cuisines. Menu is long and numbered; round-table groups matter.
- **Photo basket:** lead = dish close-ups (shared plates), round table with group, interior (lanterns). Slots: dish -> hero; group table -> atmosphere; dumpling/dim sum steamers -> gallery.
- **Palette bias:** Vibrant or Fidelity (red/gold); Monochrome for upscale. Ground: light for casual; dark for banquet.
- **Type bias:** T3 for upscale; T6/T5 for casual. Needs Chinese-capable fallback if the owner supplies it.
- **Copy voice:** Generous and shared: dishes for the table.
  - VI: {dish} cho nhóm {n_people} người / EN: {dish} for a group of {n_people}
  - VI: Dim sum mỗi ngày từ {open} / EN: Dim sum daily from {open}
  - VI: Đặt bàn nhóm: {phone} / EN: Group booking: {phone}
- **Extra slot:** Group booking (party size, date) when the venue has large tables.
- **Menu shape:** By category and numbered dishes; set menus for groups. Prices: Board photo, app, or none.
- **Pairs with personalities:** lively, premium, street
- **Reference:** dumpling brand, open-kitchen proof (reachable 7 Oct) <https://www.dintaifung.com.tw>; reachable; reasoned only <https://www.chinatown.com>

## 15. Seafood  (`seafood`)
- **No-site total:** 1,846 (DN 293 / HCM 793 / BKK 719 / LON 41), top score 20.58. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (3):** Seafood restaurant (1,846), Oyster bar restaurant, Angler fish restaurant
- **Why grouped:** Seafood restaurants in DN/HCM and Bangkok are price-by-weight and tank-led. The photo of the tank or catch is the hero.
- **Photo basket:** lead = catch / tank / live display, dish close-ups, outdoor seating. Slots: catch/tank -> hero; cooked dish -> cards; seating by the sea -> atmosphere.
- **Palette bias:** Vibrant or Fidelity (sea blue, coral); TonalSpot. Ground: light, outdoor feel.
- **Type bias:** T6 or T1.
- **Copy voice:** Fresh today, priced by weight.
  - VI: Hải sản tươi sống, giá theo {unit} / EN: Live seafood, priced by {unit}
  - VI: {dish} – chế biến theo yêu cầu / EN: {dish}, cooked to order
  - VI: Bàn ngoài trời {n_seats} chỗ / EN: {n_seats} outdoor seats
- **Extra slot:** Price-by-weight table / live-catch list only if prices exist; else none.
- **Menu shape:** By seafood type (fish, crab, shrimp, shellfish) then cooking method. Prices: Board photo; prices change daily so mark them as a guide.
- **Pairs with personalities:** lively, street, cosy
- **Reference:** reasoned (no live site read)

## 16. Vegetarian, healthy and organic  (`vegetarian-healthy`)
- **No-site total:** 1,082 (DN 138 / HCM 622 / BKK 274 / LON 48), top score 17.04. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (7):** Vegetarian restaurant (532), Health food store (479), Health food restaurant (71), Organic restaurant, Raw food restaurant, Tofu restaurant, Organic food store
- **Why grouped:** Strong in VN (Buddhist vegetarian) and Bangkok; includes health food stores and organic food stores as product lists.
- **Photo basket:** lead = bowls and plates (green), ingredients, interior (plants). Slots: bowl -> hero; ingredients -> about; interior -> atmosphere.
- **Palette bias:** Neutral or TonalSpot (greens); Content. Ground: light.
- **Type bias:** T5 or T1.
- **Copy voice:** Calm and honest: ingredients, no promises about health.
  - VI: Món chay từ {ingredient} tươi / EN: Plant-based dishes from fresh {ingredient}
  - VI: Thực đơn chay đầy đủ / EN: Full vegetarian menu
  - VI: Mở cửa {hours} / EN: Open {hours}
- **Extra slot:** none (dietary tags only if on the menu)
- **Menu shape:** By meal type; products by shelf for stores. Prices: Board photo, app.
- **Pairs with personalities:** calm, cosy, playful
- **Reference:** reasoned (no live site read)

## 17. Indian and South Asian (incl. halal, haleem, biryani, Pakistani)  (`indian-south-asian`)
- **No-site total:** 980 (DN 62 / HCM 202 / BKK 546 / LON 170), top score 16.89. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (38):** Indian restaurant (401), Haleem restaurant (284), Halal restaurant (240), Pakistani restaurant (21), Afghan restaurant (13), Bangladeshi restaurant (11), Sri Lankan restaurant (7), Nepalese restaurant (3), Bengali restaurant, Biryani restaurant, Gujarati restaurant, Hyderabadi restaurant … +26 more
- **Why grouped:** 38 rows folded together because the site pattern is the same: curry-and-bread menu, halal cue, delivery. Halal and haleem are the biggest rows.
- **Photo basket:** lead = curry and bread (top-down), tandoor/open kitchen, interior. Slots: curry -> hero; tandoor -> about; interior -> atmosphere.
- **Palette bias:** Vibrant or Expressive (saffron, red); Fidelity for premium. Ground: dark or light.
- **Type bias:** T6 or T1; Devanagari fallback optional.
- **Copy voice:** Rich and warm: spice, tandoor, the table.
  - VI: {dish} – cay vừa, cay nhiều / EN: {dish}, mild or hot
  - VI: Halal: {halal_note} / EN: Halal: {halal_note}
  - VI: Giao hàng trong {area} / EN: Delivery in {area}
- **Extra slot:** Delivery-first when an app listing exists; halal badge only if the data says so.
- **Menu shape:** By course (starters, curries, breads, biryani). Prices: Delivery app or board photo.
- **Pairs with personalities:** lively, street, premium
- **Reference:** Indian cafe brand, story-led (reachable 7 Oct) <https://www.dishoom.com>

## 18. Steakhouse and meat dishes (steak, chophouse)  (`steakhouse`)
- **No-site total:** 933 (DN 10 / HCM 65 / BKK 849 / LON 9), top score 19.01. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (4):** Steak house (933), Chophouse restaurant, Meat dish restaurant, Cheesesteak restaurant
- **Why grouped:** Dinner, premium, sometimes group. Photos of cuts and interiors.
- **Photo basket:** lead = steak on the plate, interior (dark), chef/grill. Slots: steak -> hero; interior -> atmosphere; grill -> about.
- **Palette bias:** Monochrome or Fidelity (charcoal, ember). Ground: dark.
- **Type bias:** T3 or T6.
- **Copy voice:** Confident and plain: cut, weight, temperature.
  - VI: {cut} {weight}g, nướng {doneness} / EN: {cut} {weight}g, cooked {doneness}
  - VI: Đặt bàn {phone} / EN: Reserve on {phone}
  - VI: Rượu vang theo ly / EN: Wine by the glass
- **Extra slot:** Reservations, optional.
- **Menu shape:** By course; steaks by cut and weight. Prices: Menu photo/PDF; rarely apps.
- **Pairs with personalities:** premium, lively, cosy
- **Reference:** reasoned (no live site read)

## 19. Korean (non-BBQ)  (`korean`)
- **No-site total:** 932 (DN 97 / HCM 312 / BKK 484 / LON 39), top score 18.56. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (2):** Korean restaurant (932), Soondae restaurant
- **Why grouped:** Korean stews, rice, fried chicken, soondae. BBQ is its own skin; this one is stews and one-dish meals.
- **Photo basket:** lead = bubbling stews, banchan spread, interior. Slots: stew -> hero; banchan -> gallery; interior -> atmosphere.
- **Palette bias:** Vibrant or Rainbow; Expressive for playful. Ground: light or dark.
- **Type bias:** T6 or T4; Korean fallback is already required by the engine.
- **Copy voice:** Hearty, sharing, hot.
  - VI: {dish} sôi sùng sục / EN: {dish}, still bubbling
  - VI: Kèm {n_banchan} món ăn kèm / EN: With {n_banchan} side dishes
  - VI: Đặt bàn nhóm {phone} / EN: Group booking {phone}
- **Extra slot:** none
- **Menu shape:** By dish type (stews, rice, noodles, sets). Prices: Board or app.
- **Pairs with personalities:** lively, street, playful
- **Reference:** not reachable; reasoned <https://www.kimchee.co>

## 20. Tea house  (`tea-house`)
- **No-site total:** 896 (DN 97 / HCM 456 / BKK 310 / LON 33), top score 14.66. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (2):** Tea house (896), Chinese tea house
- **Why grouped:** Quiet tea rooms. Different from bubble tea: calm, ritual, slower.
- **Photo basket:** lead = tea service, interior (still), tea leaves/craft. Slots: tea service -> hero; interior -> atmosphere; leaves -> about.
- **Palette bias:** Neutral or Monochrome (celadon, ink). Ground: light, desaturated.
- **Type bias:** T3 or T5.
- **Copy voice:** Calm and unhurried.
  - VI: Trà {tea}, pha tại bàn / EN: {tea}, brewed at your table
  - VI: Phòng trà, {n_seats} chỗ / EN: Tea room, {n_seats} seats
  - VI: Mở {hours} / EN: Open {hours}
- **Extra slot:** none
- **Menu shape:** By tea type (green, oolong, black), with a short snack list. Prices: Board photo.
- **Pairs with personalities:** calm, premium, cosy
- **Reference:** reasoned (no live site read)

## 21. Sandwich, deli and snack (incl. bánh mì style)  (`sandwich-deli`)
- **No-site total:** 868 (DN 33 / HCM 90 / BKK 614 / LON 131), top score 9.43. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (7):** Deli (662), Sandwich shop (186), Snack bar (20), Hoagie restaurant, Po’ boys restaurant, Toast restaurant, Vegetarian cafe and deli
- **Why grouped:** Counter-led takeaway: items by filling, order-ahead for offices.
- **Photo basket:** lead = product close-ups, counter, packaging. Slots: product -> hero; counter -> about; packaging -> gallery.
- **Palette bias:** Vibrant or TonalSpot. Ground: light.
- **Type bias:** T6 or T5.
- **Copy voice:** Grab-and-go, honest: fillings.
  - VI: {dish} với {filling} / EN: {dish} with {filling}
  - VI: Đặt trước cho văn phòng / EN: Pre-order for offices
  - VI: Mở từ {open} / EN: Open from {open}
- **Extra slot:** Pre-order for groups, optional.
- **Menu shape:** By item then fillings/sides. Prices: Board or app.
- **Pairs with personalities:** street, playful, lively
- **Reference:** reasoned (no live site read)

## 22. Cocktail, wine and lounge  (`cocktail-wine-lounge`)
- **No-site total:** 855 (DN 53 / HCM 251 / BKK 303 / LON 248), top score 7.37. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (5):** Cocktail bar (361), Lounge bar (262), Wine bar (128), Tapas bar (57), Hookah bar (47)
- **Why grouped:** Premium bars: photo-led, dark, reservations.
- **Photo basket:** lead = drink close-ups (moody), interior, bartender. Slots: drink -> hero; interior -> atmosphere; bartender -> about.
- **Palette bias:** Monochrome or Fidelity (dark, brass). Ground: dark.
- **Type bias:** T3 or T5.
- **Copy voice:** Understated and precise: the pour, the room.
  - VI: {cocktail} – {ingredients} / EN: {cocktail}: {ingredients}
  - VI: Đặt bàn cho {n_people} người / EN: Reserve for {n_people}
  - VI: Happy hour {happy_hours} / EN: Happy hour {happy_hours}
- **Extra slot:** Reservations plus events/happy hour.
- **Menu shape:** By drink type (signature, classic, wine, bites). Prices: Menu photo; rarely apps.
- **Pairs with personalities:** premium, calm, lively
- **Reference:** premium bar-restaurant (reachable 7 Oct) <https://www.sushisamba.com>

## 23. BBQ and grill (Korean BBQ, yakiniku, barbecue, satay, mutton, offal BBQ)  (`bbq-grill`)
- **No-site total:** 823 (DN 82 / HCM 259 / BKK 455 / LON 27), top score 18.22. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (14):** Barbecue restaurant (823), Korean barbecue restaurant, Korean beef restaurant, Korean rib restaurant, Grill, Mutton barbecue restaurant, Offal barbecue restaurant, Mongolian barbecue restaurant, Ikan bakar restaurant, Lechon restaurant, Tongue restaurant, Grill store … +2 more
- **Why grouped:** Table grills. The site sells the group night: the grill photo, the meat platter, the table.
- **Photo basket:** lead = grill in use / meat platters, group table, interior. Slots: grill shot -> hero; platters -> cards; group -> atmosphere.
- **Palette bias:** Vibrant or Fidelity (charcoal, ember); Rainbow for loud spots. Ground: dark.
- **Type bias:** T2 or T6.
- **Copy voice:** Fire and sharing: platters, groups, table.
  - VI: Set nướng cho {n_people} người: {price} / EN: Grill set for {n_people}: {price}
  - VI: Đặt bàn nhóm {phone} / EN: Group booking {phone}
  - VI: {dish}, nướng tại bàn / EN: {dish}, grilled at your table
- **Extra slot:** Group booking (party size, date, set).
- **Menu shape:** By set/platter then by meat/seafood then sides. Prices: Board photo; sets often on the board.
- **Pairs with personalities:** lively, street, premium
- **Reference:** grill-adjacent premium (reachable 7 Oct); reasoned <https://www.sushisamba.com>

## 24. Sushi (restaurant, conveyor, temaki)  (`sushi-omakase`)
- **No-site total:** 781 (DN 20 / HCM 121 / BKK 584 / LON 56), top score 18.23. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (3):** Sushi restaurant (781), Conveyor belt sushi restaurant, Temaki restaurant
- **Why grouped:** Sushi is the Japanese skin that earns its own: omakase and set menus change the booking slot.
- **Photo basket:** lead = nigiri close-ups, counter (chef at work), interior. Slots: nigiri -> hero; counter/chef -> about; interior -> atmosphere.
- **Palette bias:** Monochrome or Neutral (ink, cedar); Vibrant for conveyor. Ground: light for casual; dark for omakase.
- **Type bias:** T3 or T5; T6 for conveyor.
- **Copy voice:** Precise and respectful: fish, rice, hands.
  - VI: Omakase {price}, {n_seats} chỗ quầy / EN: Omakase {price}, {n_seats} counter seats
  - VI: Set sushi {n_pieces} miếng / EN: Sushi set, {n_pieces} pieces
  - VI: Đặt trước {phone} / EN: Reserve on {phone}
- **Extra slot:** Omakase/set-menu card (courses, price, seats, booking), only when the data has it.
- **Menu shape:** By set (omakase, nigiri sets) then à la carte. Prices: Board photo or booking page.
- **Pairs with personalities:** premium, calm, playful
- **Reference:** omakase-led premium site (reachable 7 Oct) <https://www.nobu.com>

## 25. Pizzeria (pizza, pizza delivery, Neapolitan)  (`pizzeria-delivery`)
- **No-site total:** 773 (DN 39 / HCM 118 / BKK 388 / LON 228), top score 21.98. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (3):** Pizza restaurant (762), Pizza delivery (11), Neapolitan restaurant
- **Why grouped:** Delivery-first, with a sit-down variant. Decide by delivery links in the data.
- **Photo basket:** lead = pizza top-down, oven/pizzaiolo, interior. Slots: pizza -> hero and cards; oven -> about; interior -> atmosphere.
- **Palette bias:** Vibrant or Expressive (tomato, basil). Ground: light.
- **Type bias:** T6 or T4.
- **Copy voice:** Hot and fast: size, toppings, order.
  - VI: Pizza {size} chỉ {price} / EN: {size} pizza, {price}
  - VI: Giao tận nơi {area} / EN: Delivered across {area}
  - VI: Lò củi, nướng tại chỗ / EN: Wood oven, baked on the spot
- **Extra slot:** Delivery-first: order buttons above the fold; size + toppings builder if data allows.
- **Menu shape:** By pizza type then sides/drinks. Prices: Delivery app; board for sit-down.
- **Pairs with personalities:** street, playful, lively
- **Reference:** pizza brand, product-led (reachable 7 Oct) <https://www.pizzapilgrims.co.uk>; delivery-first chain (reachable 7 Oct) <https://www.pizzaexpress.com>

## 26. Karaoke / KTV  (`karaoke-ktv`)
- **No-site total:** 753 (DN 101 / HCM 414 / BKK 230 / LON 8), top score 8.36. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (1):** Karaoke bar (753)
- **Why grouped:** A room-booking business wearing a bar menu. 753 no-site.
- **Photo basket:** lead = room interiors, lighting/crowd, drinks. Slots: room -> hero; lighting -> atmosphere; menu -> cards.
- **Palette bias:** Rainbow or Vibrant on dark. Ground: dark.
- **Type bias:** T6 or T2.
- **Copy voice:** Loud and bookable: rooms, hours, packages.
  - VI: Phòng {n_people} người: {price}/giờ / EN: Room for {n_people}: {price} per hour
  - VI: Mở đến {close} / EN: Open until {close}
  - VI: Đặt phòng {phone} / EN: Book a room: {phone}
- **Extra slot:** Room booking (size, hour) - closer to booking module than menu; flag it.
- **Menu shape:** By room type + drinks and snacks. Prices: Board photo; rarely apps.
- **Pairs with personalities:** lively, street, playful
- **Reference:** reasoned (no live site read)

## 27. Buffet and self-service  (`buffet-self-service`)
- **No-site total:** 659 (DN 16 / HCM 60 / BKK 577 / LON 6), top score 12.11. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (3):** Buffet restaurant (659), Pay by weight restaurant, Self service restaurant
- **Why grouped:** Price-per-head: the offer is the page (price, hours, what is included).
- **Photo basket:** lead = spread/stations, dining hall, people. Slots: spread -> hero; hall -> atmosphere.
- **Palette bias:** Vibrant or TonalSpot. Ground: light.
- **Type bias:** T6 or T5.
- **Copy voice:** Generous and clear: price per head, what is included.
  - VI: Buffet {price}/người / EN: Buffet {price} per person
  - VI: Giờ mở cửa {hours} / EN: Open {hours}
  - VI: Đặt bàn nhóm {phone} / EN: Group booking {phone}
- **Extra slot:** Price-per-head card and group booking.
- **Menu shape:** By session (lunch/dinner) with a price table. Prices: Board or Facebook posts.
- **Pairs with personalities:** lively, street, cosy
- **Reference:** reasoned (no live site read)

## 28. Juice and smoothie  (`juice-smoothie`)
- **No-site total:** 523 (DN 40 / HCM 276 / BKK 170 / LON 37), top score 8.89. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (1):** Juice shop (523)
- **Why grouped:** Fruit-led drink counter; close to bubble tea but healthy.
- **Photo basket:** lead = fruit/cup close-ups, counter, menu board. Slots: cup -> hero; fruit -> about; board -> OCR.
- **Palette bias:** FruitSalad or Expressive. Ground: light, bright.
- **Type bias:** T4.
- **Copy voice:** Fresh and plain: fruit names.
  - VI: {fruit} ép tại chỗ / EN: {fruit}, pressed to order
  - VI: Size {size}: {price} / EN: {size}: {price}
  - VI: Mở {hours} / EN: Open {hours}
- **Extra slot:** Toppings/boosters optional.
- **Menu shape:** By drink type + add-ons. Prices: Board or app.
- **Pairs with personalities:** playful, lively, calm
- **Reference:** reasoned (no live site read)

## 29. Italian (trattoria, regional)  (`italian-trattoria`)
- **No-site total:** 361 (DN 16 / HCM 37 / BKK 193 / LON 115), top score 16.73. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (13):** Italian restaurant (361), Ligurian restaurant, Northern Italian restaurant, Piedmontese restaurant, Lombardian restaurant, Marche restaurant, Piadina restaurant, Roman restaurant, Sicilian restaurant, Tuscan restaurant, Venetian restaurant, Sardinian restaurant … +1 more
- **Why grouped:** Dine-in Italian (not pizza-first). Menu by course; wine list matters.
- **Photo basket:** lead = pasta close-ups, interior, wine/bar. Slots: pasta -> hero; interior -> atmosphere; bar -> about.
- **Palette bias:** TonalSpot or Fidelity (tomato, olive). Ground: light or warm dark.
- **Type bias:** T1 or T3.
- **Copy voice:** Warm and generous: pasta, wine, the table.
  - VI: {dish} làm tại chỗ / EN: {dish}, made in house
  - VI: Đặt bàn {phone} / EN: Reserve on {phone}
  - VI: Rượu vang {region} / EN: {region} wines
- **Extra slot:** none
- **Menu shape:** By course (antipasti, pasta, mains, dolci). Prices: Menu photo or app.
- **Pairs with personalities:** cosy, premium, calm
- **Reference:** Italian chain, reachable 7 Oct <https://www.pizzaexpress.com>

## 30. Middle Eastern and Mediterranean (excl. kebab)  (`middle-east-mediterranean`)
- **No-site total:** 303 (DN 4 / HCM 8 / BKK 56 / LON 235), top score 11.33. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (23):** Turkish restaurant (66), Middle Eastern restaurant (64), Lebanese restaurant (58), Mediterranean restaurant (43), Greek restaurant (27), Arab restaurant (18), Algerian Restaurant (11), Persian restaurant (5), Kosher restaurant (4), Syrian restaurant (4), Moroccan restaurant (3), Jewish restaurant … +11 more
- **Why grouped:** Turkish, Lebanese, Mediterranean, Greek, Persian and neighbours; mezze-sharing.
- **Photo basket:** lead = mezze/sharing plates, interior, grill. Slots: mezze -> hero; grill -> about.
- **Palette bias:** Expressive or Fidelity (terracotta, olive). Ground: light.
- **Type bias:** T1 or T6.
- **Copy voice:** Sharing and generous.
  - VI: Mezze cho nhóm {n_people} người / EN: Mezze for {n_people}
  - VI: {dish}, nướng than / EN: {dish}, charcoal-grilled
  - VI: Giao hàng {area} / EN: Delivery in {area}
- **Extra slot:** none
- **Menu shape:** By course (mezze, grills, mains). Prices: App or board.
- **Pairs with personalities:** lively, cosy, calm
- **Reference:** reasoned (no live site read)

## 31. Latin American and Caribbean  (`latin-caribbean`)
- **No-site total:** 287 (DN 5 / HCM 28 / BKK 83 / LON 171), top score 11.53. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (35):** Caribbean restaurant (75), Mexican restaurant (69), South American restaurant (51), Brazilian restaurant (28), Jamaican restaurant (17), Latin American restaurant (14), Colombian restaurant (12), Peruvian restaurant (7), Tex-Mex restaurant (6), Ecuadorian restaurant (3), Guatemalan restaurant (3), Argentinian restaurant (2) … +23 more
- **Why grouped:** 33 rows (Mexican, Brazilian, Peruvian...). Small but colourful; one site pattern.
- **Photo basket:** lead = colourful plates, bar/drinks, interior. Slots: plate -> hero; drinks -> cards.
- **Palette bias:** Rainbow or Expressive. Ground: light or dark.
- **Type bias:** T6 or T4.
- **Copy voice:** Bright and social.
  - VI: {dish} và {drink} / EN: {dish} and {drink}
  - VI: Mở đến {close} / EN: Open until {close}
  - VI: Đặt bàn {phone} / EN: Book on {phone}
- **Extra slot:** none (happy hour if bar)
- **Menu shape:** By course and sharing plates. Prices: Menu photo or app.
- **Pairs with personalities:** playful, lively, street
- **Reference:** reasoned (no live site read)

## 32. European bistro and fine dining  (`european-bistro`)
- **No-site total:** 235 (DN 12 / HCM 42 / BKK 71 / LON 110), top score 8.5. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (49):** French restaurant (77), European restaurant (49), British restaurant (44), German restaurant (20), Portuguese restaurant (20), Spanish restaurant (18), Bistro (4), Eastern European restaurant (3), Basque restaurant, Bavarian restaurant, Bulgarian restaurant, Central European restaurant … +37 more
- **Why grouped:** 49 rows: French, German, Spanish, British, Nordic, fine dining. The only skins that lean premium by default.
- **Photo basket:** lead = plated dishes, interior, sommelier/bar. Slots: plate -> hero; interior -> atmosphere.
- **Palette bias:** Monochrome or Fidelity. Ground: light or dark by photo.
- **Type bias:** T3 or T5.
- **Copy voice:** Quiet and craft: ingredient, region, season.
  - VI: {dish}, {ingredient} theo mùa / EN: {dish}, seasonal {ingredient}
  - VI: Thực đơn {n_courses} món / EN: {n_courses}-course menu
  - VI: Đặt bàn {phone} / EN: Reserve on {phone}
- **Extra slot:** Tasting-menu card + reservations when data has it.
- **Menu shape:** By course; tasting menu on top. Prices: Menu photo/PDF.
- **Pairs with personalities:** premium, calm, cosy
- **Reference:** premium dining site (reachable 7 Oct); reasoned <https://www.sushisamba.com>

## 33. Themed cafe (animal, comic, cosplay, art, internet)  (`themed-cafe`)
- **No-site total:** 199 (DN 31 / HCM 123 / BKK 35 / LON 10), top score 7.95. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (8):** Internet cafe (199), Animal cafe, Art cafe, Cat cafe, Children's cafe, Comic cafe, Cosplay cafe, Dog cafe
- **Why grouped:** Experience is the product; the drinks are secondary.
- **Photo basket:** lead = the theme (animals, comics, art), people, drinks. Slots: theme -> hero; people -> about.
- **Palette bias:** Expressive or Rainbow. Ground: light or dark by theme.
- **Type bias:** T4 or T6.
- **Copy voice:** Playful and rule-clear (hours, entry, house rules).
  - VI: Gặp {animals} tại {name} / EN: Meet the {animals} at {name}
  - VI: Giá vào cửa {price} / EN: Entry {price}
  - VI: Mở {hours} / EN: Open {hours}
- **Extra slot:** Entry/session info.
- **Menu shape:** By drinks with an entry/price block. Prices: Board photo.
- **Pairs with personalities:** playful, lively, cosy
- **Reference:** reasoned (no live site read)

## 34. American and comfort (regional US, Canadian, Cajun, Southern)  (`american-comfort`)
- **No-site total:** 107 (DN 3 / HCM 17 / BKK 55 / LON 32), top score 12.91. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (23):** American restaurant (97), Hawaiian restaurant (7), Canadian restaurant (3), Cajun restaurant, Californian restaurant, Creole restaurant, Mid-Atlantic restaurant (US), New American restaurant, New England restaurant, New Zealand restaurant, Chesapeake restaurant, Contemporary Louisiana restaurant … +11 more
- **Why grouped:** Small total; all comfort-food formats with the same site.
- **Photo basket:** lead = burger/ribs/plates, interior, bar. Slots: plate -> hero.
- **Palette bias:** Vibrant or TonalSpot. Ground: light.
- **Type bias:** T6 or T1.
- **Copy voice:** Generous and casual.
  - VI: {dish} và {side} / EN: {dish} and {side}
  - VI: Brunch cuối tuần / EN: Weekend brunch
  - VI: Mở {hours} / EN: Open {hours}
- **Extra slot:** none
- **Menu shape:** By course. Prices: Menu photo or app.
- **Pairs with personalities:** street, cosy, lively
- **Reference:** reasoned (no live site read)

## 35. Southeast Asian regional (Indonesian, Malay, Filipino, Singaporean, Burmese)  (`southeast-asian`)
- **No-site total:** 104 (DN 3 / HCM 18 / BKK 63 / LON 20), top score 7.29. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (30):** Burmese restaurant (28), Singaporean restaurant (28), Filipino restaurant (23), Malaysian restaurant (15), Indonesian restaurant (10), Javanese restaurant, Padang restaurant, Ayam penyet restaurant, Bakso restaurant, Balinese restaurant, Batak restaurant, Betawi restaurant … +18 more
- **Why grouped:** Indonesian regional rows are numerous but tiny; Singapore/Malaysia near-duplicates.
- **Photo basket:** lead = dish close-ups, street stall, interior. Slots: dish -> hero; stall -> about.
- **Palette bias:** Vibrant or TonalSpot. Ground: light.
- **Type bias:** T6 or T1.
- **Copy voice:** Flavour and place.
  - VI: {dish} kiểu {region} / EN: {dish}, {region} style
  - VI: Mở {hours} / EN: Open {hours}
  - VI: Giao hàng {area} / EN: Delivery {area}
- **Extra slot:** none
- **Menu shape:** By dish type. Prices: App or board.
- **Pairs with personalities:** street, lively, cosy
- **Reference:** reasoned (no live site read)

## 36. Kebab and shawarma (doner, gyro, durum, kofta)  (`kebab-shawarma`)
- **No-site total:** 99 (DN 0 / HCM 3 / BKK 23 / LON 73), top score 13.07. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (7):** Doner kebab restaurant (99), Cig kofte restaurant, Kofta restaurant, Durum restaurant, Gyro restaurant, Sfiha restaurant, Shawarma restaurant
- **Why grouped:** Delivery-first, counter-led; skewer-and-wrap.
- **Photo basket:** lead = wraps and spits, counter, packaging. Slots: wrap -> hero; spit -> about.
- **Palette bias:** Vibrant or Rainbow. Ground: light.
- **Type bias:** T6.
- **Copy voice:** Fast and hungry.
  - VI: {dish} {price} / EN: {dish} {price}
  - VI: Giao nhanh {area} / EN: Fast delivery {area}
  - VI: Mở đến {close} / EN: Open until {close}
- **Extra slot:** Delivery-first order buttons.
- **Menu shape:** By wrap/plate then sides. Prices: Delivery app or board.
- **Pairs with personalities:** street, lively, playful
- **Reference:** reasoned (no live site read)

## 37. African restaurant  (`african`)
- **No-site total:** 51 (DN 1 / HCM 1 / BKK 3 / LON 46), top score 6.53. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (7):** African restaurant (36), Ethiopian restaurant (15), Cape Verdean restaurant, East African restaurant, Eritrean restaurant, Seychelles restaurant, West African restaurant
- **Why grouped:** Small and varied: West, East, Ethiopian, Cape Verdean.
- **Photo basket:** lead = stews and injera, interior, people. Slots: plate -> hero.
- **Palette bias:** Expressive or TonalSpot. Ground: warm.
- **Type bias:** T1 or T4.
- **Copy voice:** Warm and communal.
  - VI: {dish} theo công thức {region} / EN: {dish}, {region} recipe
  - VI: Đặt nhóm {phone} / EN: Groups: {phone}
  - VI: Mở {hours} / EN: Open {hours}
- **Extra slot:** none
- **Menu shape:** By dish type and sharing platters. Prices: Menu photo.
- **Pairs with personalities:** cosy, lively, calm
- **Reference:** reasoned (no live site read)

## 38. Hotpot (hot pot, steamboat, shabu, sukiyaki)  (`hotpot`)
- **No-site total:** 0 (DN 0 / HCM 0 / BKK 0 / LON 0), top score 6.01. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (7):** Hot pot restaurant, Chanko restaurant, Offal pot cooking restaurant, Shabu-shabu restaurant, Steamboat restaurant, Sukiyaki and Shabu Shabu restaurant, Sukiyaki restaurant
- **Why grouped:** By-the-pot with broth + items; zero no-site in the four cities as matched, but a distinct site shape.
- **Photo basket:** lead = pot with steam, ingredient platters, group table. Slots: pot -> hero; platters -> cards.
- **Palette bias:** Vibrant or Rainbow. Ground: dark.
- **Type bias:** T6 or T2.
- **Copy voice:** Bubbling and shared.
  - VI: Nồi lẩu {broth} cho {n_people} người / EN: {broth} pot for {n_people}
  - VI: Chọn nước dùng, chọn nhúng / EN: Choose a broth, choose your dips
  - VI: Đặt bàn {phone} / EN: Reserve on {phone}
- **Extra slot:** By-the-pot builder (broth + items), if the menu has the structure.
- **Menu shape:** By broth then items/platters then sauces. Prices: Board photo; prices by pot/platter.
- **Pairs with personalities:** lively, street, cosy
- **Reference:** hotpot chain (reachable 7 Oct) <https://www.haidilao.com>

## 39. Izakaya and yakitori (incl. kushiyaki, kushikatsu)  (`izakaya-yakitori`)
- **No-site total:** 0 (DN 0 / HCM 0 / BKK 0 / LON 0), top score 5.8. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (5):** Izakaya restaurant, Modern izakaya restaurant, Kushiage and kushikatsu restaurant, Kushiyaki restaurant, Yakitori restaurant
- **Why grouped:** Small plates and drinks, dark rooms, group nights.
- **Photo basket:** lead = skewers, interior (lantern), drinks. Slots: skewers -> hero.
- **Palette bias:** Fidelity or Vibrant on dark. Ground: dark.
- **Type bias:** T2 or T6.
- **Copy voice:** Late and sociable.
  - VI: Xiên nướng {price}/xiên / EN: Skewers {price} each
  - VI: Đồ uống đi kèm / EN: Drinks to match
  - VI: Mở đến {close} / EN: Open until {close}
- **Extra slot:** Happy hour/events if data.
- **Menu shape:** By skewer/plate, then drinks. Prices: Board photo.
- **Pairs with personalities:** lively, street, premium
- **Reference:** reasoned (no live site read)

## –. Not a menu business (misrouted by INDEX.csv)  (`not-menu`)
- **No-site total:** 0 (DN 0 / HCM 0 / BKK 0 / LON 0), top score 7.89. Source: Overture 2026-09-23.1, counted 7 Oct 2026.
- **Rows (10):** Electrolysis hair removal service, Laser hair removal service, Weight loss service, Beautician, Hair removal service, Karaoke equipment rental service, Hairdresser, Eyebrow bar, Indoor golf course, Frozen food store
- **Why grouped:** Ten rows tagged "Menu" in INDEX.csv that are services or retail: hair removal, weight loss, beautician, hairdresser, eyebrow bar, karaoke equipment rental, indoor golf, frozen food. Route them to services + booking (or retail). Zero no-site count anyway.
- **Photo basket:** lead = n/a. Slots: route to booking skins.
- **Palette bias:** n/a Ground: n/a.
- **Type bias:** n/a
- **Copy voice:** n/a
- **Extra slot:** n/a
- **Menu shape:** n/a Prices: n/a
- **Pairs with personalities:** n/a
- **Reference:** reasoned (no live site read)
