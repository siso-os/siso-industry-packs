"""Research pack: fetch real café and restaurant sites and extract each one's sitemap and section outline (free, no model).
Writes _data/siso-agency/industries/pack/<slug>.json plus pack/summary.csv. A reader then distils the slots.
Usage: uv run -q --with requests --with beautifulsoup4 python 10_site_pack.py"""
import json, re, pathlib, urllib.parse, csv, requests
from bs4 import BeautifulSoup
OUT = pathlib.Path.home()/'SISO_Workspace/_data/siso-agency/industries/pack'; OUT.mkdir(parents=True, exist_ok=True)
SITES = [  # (url, why it's in the pack)
 ('https://www.ateliercrenn.com', 'BentoBox, fine dining'), ('https://www.saffysla.com', 'BentoBox, casual'),
 ('https://www.dadospizza.com', 'BentoBox, pizza'), ('https://www.thefriendlytoast.com', 'Popmenu, brunch group'),
 ('https://cyclonoodles.com', 'Owner.com, noodles'), ('https://kumascorner.com', 'platform, burger bar'),
 ('https://www.dishoom.com', 'brand-led restaurant group'), ('https://tartinebakery.com', 'bakery café'),
 ('https://www.monmouthcoffee.co.uk', 'independent coffee, London'), ('https://www.prufrockcoffee.com', 'independent café, London'),
 ('https://ozonecoffee.co.uk', 'café roaster'), ('https://www.ottolenghi.co.uk', 'restaurant and deli'),
 ('https://www.gailsbakery.com', 'bakery café chain'), ('https://bluebottlecoffee.com', 'café brand'),
 ('https://www.pizza4ps.com', 'Vietnam, best-known restaurant brand'), ('https://congcaphe.com', 'Vietnam, café chain'),
 ('https://madamelam.vn', 'Vietnam, restaurant'), ('https://www.humvegetarian.vn', 'Vietnam, restaurant'),
 ('https://runamcafe.com', 'Vietnam, café'), ('https://www.thedeckhouse.vn', 'Vietnam, restaurant'),
 ('https://www.noma.dk', 'world-class, design-led'), ('https://www.st-john.co.uk', 'classic restaurant, minimal'),
 ('https://www.blacksheeprestaurants.com', 'Hong Kong group'),
 ('https://cafe-89.pages.dev', 'ours: Café 89'), ('https://kikas-preview.pages.dev', 'ours: Kikas'),
]
UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15'}
DETECT = {
 'map_embed': r'google\.com/maps/embed|maps\.google|mapbox|leaflet', 'reservations': r'opentable|resy\.com|sevenrooms|exploretock|tablein|quandoo|thefork|reserve',
 'order_online': r'toasttab|doordash|ubereats|deliveroo|grab\.com|grabfood|shopeefood|order online|order now|chownow|olo\.com',
 'gift_cards': r'gift ?card|e-?gift|voucher', 'newsletter': r'newsletter|subscribe|sign ?up for', 'instagram': r'instagram\.com',
 'reviews': r'review|testimonial|tripadvisor|google reviews|★', 'events_private': r'private (dining|events|hire)|events|catering',
 'careers': r'careers|jobs|join (our|the) team|hiring', 'shop_merch': r'/shop|merch|store|buy beans|subscription',
 'language_switch': r'hreflang|lang-switch|language|tiếng việt|/vi/|/en/', 'carousel': r'swiper|slick|carousel|flickity|splide',
 'video_hero': r'<video', 'pdf_menu': r'\.pdf', 'schema_restaurant': r'"@type":\s*"(Restaurant|CafeOrCoffeeShop|Bakery|FoodEstablishment)"',
 'prices': r'(\$|£|€|₫|vnd|đ)\s?\d|\d[\d.,]*\s?(₫|đ|vnd|k\b)', 'hours': r'\b(mon|tue|wed|thu|fri|sat|sun)[a-z]*\b.{0,40}\d{1,2}[:.]?\d{0,2}\s?(am|pm|h)?',
}
def fetch(u):
    try:
        r = requests.get(u, headers=UA, timeout=20); return r.status_code, r.url, r.text
    except Exception as e: return 0, u, str(e)
def outline(html):
    s = BeautifulSoup(html, 'html.parser')
    for t in s(['script', 'style', 'noscript', 'svg']): t.decompose()
    body = s.body or s
    blocks = []
    for el in body.find_all(['header', 'section', 'footer', 'nav', 'article', 'aside'], recursive=True):
        if el.find_parent(['section', 'footer', 'header', 'article']): continue
        hs = [h.get_text(' ', strip=True)[:80] for h in el.find_all(['h1', 'h2', 'h3'])][:4]
        ctas = [a.get_text(' ', strip=True)[:30] for a in el.find_all(['a', 'button']) if a.get_text(strip=True)][:6]
        blocks.append({'tag': el.name, 'class': ' '.join(el.get('class', []))[:60], 'headings': hs, 'actions': ctas,
                       'imgs': len(el.find_all('img')), 'words': len(el.get_text(' ', strip=True).split())})
    return blocks[:25]
rows = []
for url, why in SITES:
    slug = re.sub(r'[^a-z0-9]+', '-', urllib.parse.urlparse(url).netloc.replace('www.', ''))[:40].strip('-')
    code, final, html = fetch(url)
    rec = {'url': url, 'final': final, 'why': why, 'status': code, 'bytes': len(html)}
    if code == 200:
        s = BeautifulSoup(html, 'html.parser')
        host = urllib.parse.urlparse(final).netloc
        nav = []
        for a in (s.find('nav') or s.find('header') or s).find_all('a', href=True):
            t = a.get_text(' ', strip=True)
            if t and len(t) < 40 and t not in [n['text'] for n in nav]: nav.append({'text': t, 'href': urllib.parse.urljoin(final, a['href'])})
        rec['nav'] = nav[:20]
        sm_code, _, sm = fetch(f'https://{host}/sitemap.xml')
        rec['sitemap'] = re.findall(r'<loc>(.*?)</loc>', sm)[:80] if sm_code == 200 else []
        low = html.lower()
        rec['features'] = {k: bool(re.search(v, low)) for k, v in DETECT.items()}
        rec['home'] = outline(html)
        rec['js_rendered'] = len(BeautifulSoup(html, 'html.parser').get_text(' ', strip=True).split()) < 150
        pages = {}
        for n in nav[:8]:
            if urllib.parse.urlparse(n['href']).netloc == host and n['href'].rstrip('/') != final.rstrip('/'):
                c, f, h = fetch(n['href'])
                if c == 200:
                    pages[n['text']] = {'url': f, 'outline': outline(h)[:12], 'features': [k for k, v in DETECT.items() if re.search(v, h.lower())]}
        rec['pages'] = pages
    (OUT/f'{slug}.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1))
    rows.append({'slug': slug, 'status': code, 'why': why, 'nav': len(rec.get('nav', [])), 'pages': len(rec.get('pages', {})),
                 'sitemap': len(rec.get('sitemap', [])), 'js': rec.get('js_rendered', ''), **rec.get('features', {})})
    print(slug, code, len(rec.get('pages', {})), 'pages', 'JS' if rec.get('js_rendered') else '', flush=True)
with open(OUT/'summary.csv', 'w', newline='') as f:
    keys = sorted({k for r in rows for k in r}, key=lambda k: list(rows[0]).index(k) if k in rows[0] else 99)
    w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(rows)
