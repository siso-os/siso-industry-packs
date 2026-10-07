"""Research pack: fetch real salon and spa sites and extract each one's sitemap and section outline (free, no model).
Writes _data/siso-agency/industries/pack/<slug>.json plus pack/summary.csv. A reader then distils the slots.
Usage: uv run -q --with requests --with beautifulsoup4 python _fetch.py"""
import json, re, pathlib, urllib.parse, csv, requests
from bs4 import BeautifulSoup
OUT = pathlib.Path.home()/'SISO_Workspace/_data/siso-agency/industries/pack-salons'; OUT.mkdir(parents=True, exist_ok=True)
SITES = [  # (url, why it's in the pack)
 ('https://www.sassoon.com', 'London, hair, famous brand'), ('https://www.toniandguy.com', 'UK hair group'),
 ('https://www.hershesons.com', 'London, hair group'), ('https://www.bluntcut.com', 'London, hair independent'),
 ('https://www.blowdrybar.co.uk', 'London, blow-dry'), ('https://www.pallmallbarbers.com', 'London, barber, own booking'),
 ('https://www.murdocklondon.com', 'London, barber brand'), ('https://www.floydsbarbershop.com', 'US, barber chain'),
 ('https://www.nailsinc.com', 'London, nails'), ('https://www.lashlounge.com', 'US, lashes/brows chain'),
 ('https://www.massageenvy.com', 'US, massage chain'), ('https://www.elementsmassage.com', 'US, massage chain'),
 ('https://www.europeanwax.com', 'US, waxing chain'), ('https://www.greatclips.com', 'US, haircut chain, online check-in'),
 ('https://www.glossgenius.com', 'GlossGenius, platform'), ('https://www.fresha.com', 'Fresha, platform'),
 ('https://www.booksy.com', 'Booksy, platform'), ('https://www.vagaro.com', 'Vagaro, platform'),
 ('https://www.mindbodyonline.com', 'Mindbody, platform'), ('https://squareup.com/us/en/appointments', 'Square Appointments, platform'),
 ('https://www.sanctuary.com', 'spa, hotel'), ('https://www.heavenlyspa.com', 'US spa group'),
 ('https://letsrelaxspa.com', 'Bangkok, spa chain'), ('https://www.healthlandspa.com', 'Bangkok, spa chain'),
 ('https://www.asiaherbassociation.com', 'Bangkok, massage'), ('https://www.oasisspa.net', 'Bangkok, Oasis spa'),
 ('https://www.divanaspa.com', 'Bangkok, Divana spa'), ('https://bestspahoian.com', 'Hoi An, spa'),
 ('https://halohairbeautyhoian.vn', 'Hoi An, hair/beauty'), ('https://www.dahanspa.com', 'Hoi An, spa'),
 ('https://www.30shine.com', 'Vietnam, barber chain'), ('https://www.hairsalondanang.com', 'Da Nang, hair'),
 ('https://www.korigami.vn', 'Vietnam, hair'), ('https://www.pallmallbarbers.com/blog/', 'dup check'),
 ('https://www.mandarinoriental.com/en/bangkok/chao-phraya/wellbeing/spa', 'luxury hotel spa Bangkok'),
 ('https://www.fourseasons.com/danang/spa/', 'Da Nang luxury spa'), ('https://www.ryokan.vn', 'Vietnam spa guess'),
 ('https://www.hoianhairsalon.com', 'Hoi An hair guess'), ('https://hoianspa.vn', 'Hoi An spa'), ('https://www.bamboospa.vn','Vietnam spa'),
 ('https://spa.lotteHotel.com','x'),('https://www.tiemtocanhkhoa.com','Da Nang hair'),('https://salonhalo.vn','Halo salon'),
]
UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15'}
DETECT = {
 'booking_platform': r'fresha\.com|booksy|vagaro|glossgenius|squareup\.com/appointments|square\.site|treatwell|mindbody|mindbodyonline|setmore|acuityscheduling|schedulicity|phorest|timely|salonized|simplybook|calendly|opentable|zenoti|boulevard|meevo|rosy|bookwhen|cliniko|zalo\.me',
 'book_cta': r'book (now|online|an? appointment|your|a )|book now|đặt lịch|đặt hẹn|reserve|schedule',
 'price_list': r'(\$|£|€|₫|฿|vnd|thb|đ)\s?\d|\d[\d.,]*\s?(₫|đ|vnd|k\b|฿|baht)|price list|treatment menu|services? & prices',
 'staff': r'our (team|stylists|therapists|barbers|artists|technicians)|meet the|stylist|therapist|barber(s)?\b', 'before_after': r'before\s?(&|and|/)?\s?after|transformation',
 'gift_cards': r'gift ?card|e-?gift|voucher', 'memberships': r'membership|member(s)? (club|rates)|packages?|bundle|loyalty|rewards|course of',
 'deposit_policy': r'deposit|cancellation|no-?show|late fee|24 hours? notice|48 hours? notice',
 'chat_channel': r'zalo|whatsapp|wa\.me|line\.me|messenger|wechat|kakao', 'reviews': r'review|testimonial|tripadvisor|google reviews|★|trustpilot',
 'map_embed': r'google\.com/maps|maps\.google|mapbox|leaflet', 'hours': r'\b(mon|tue|wed|thu|fri|sat|sun)[a-z]*\b.{0,40}\d{1,2}[:.]?\d{0,2}\s?(am|pm|h)?',
 'language_switch': r'hreflang|lang-switch|tiếng việt|/vi/|/en/|/th/|/ko/|/zh/', 'instagram': r'instagram\.com', 'gallery': r'gallery|lookbook|our work|portfolio',
 'newsletter': r'newsletter|subscribe|sign ?up for', 'careers': r'careers|jobs|join (our|the) team|hiring|academy|training', 'shop_retail': r'/shop|/products|buy online|add to (cart|bag)',
 'carousel': r'swiper|slick|carousel|flickity|splide', 'video_hero': r'<video', 'schema_local': r'"@type":\s*"?(HairSalon|BeautySalon|NailSalon|DaySpa|HealthAndBeautyBusiness|LocalBusiness)',
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
def run(url, why):
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
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(8) as ex: list(ex.map(lambda t: run(*t), SITES))
with open(OUT/'summary.csv', 'w', newline='') as f:
    keys = sorted({k for r in rows for k in r}, key=lambda k: list(rows[0]).index(k) if k in rows[0] else 99)
    w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(rows)
