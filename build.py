"""Build saudicompliance.com into ./site from content_en.py / content_ar.py.

    python build.py

Output is plain static HTML (pretty URLs: /en/licensing/ -> site/en/licensing/index.html).
"""
import html
import importlib
import json
import re
import shutil

import insights as INS
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "site"
STATIC = ROOT / "static"

# ---------------------------------------------------------------------------
# Switches: fill these in as the real details arrive.
# ---------------------------------------------------------------------------
DOMAIN = "https://saudicompliance.com"
EMAIL = "info@saudicompliance.com"          # needs a mailbox once the domain is registered
PHONE_DISPLAY = ""                           # e.g. "+966 11 000 0000" (Riyadh office), empty hides it
PHONE_TEL = ""
WHATSAPP = ""                                # digits only, e.g. "9665XXXXXXXX"; empty hides the button
STREET_ADDRESS = ""                          # Riyadh office street address; empty shows city only
WEB3FORMS_KEY = "cbe536ca-6b46-40cb-b5d6-71ec02ef63d2"  # same public key as AML Canada (ComplyFactor inbox)
GA4_ID = ""
PARENT = {"name": "ComplyFactor", "url": "https://complyfactor.com"}
SHOW_PLACEHOLDERS = False                    # True shows a marked note listing missing address/CR/phone (for review builds)

def has_page(lang, slug):
    if slug in ('', 'contact', 'insights') or slug in getattr(C[lang], 'LEGAL', {}):
        return True
    if slug.startswith('insights/'):
        return (INS.SRC / lang / (slug.split('/', 1)[1] + '.md')).exists()
    return any(p['slug'] == slug for p in C[lang].PAGES)


LANGS = [l for l in ("en", "ar") if (ROOT / f"content_{l}.py").exists()]
HREFLANG = {"en": "en", "ar": "ar-SA"}

C = {lang: importlib.import_module(f"content_{lang}") for lang in LANGS}
# Extra page modules: pages_<lang>_<topic>.py each define PAGES = [...] in the same block schema.
for _lang in LANGS:
    for _f in sorted(ROOT.glob(f"pages_{_lang}_*.py")):
        _m = importlib.import_module(_f.stem)
        _slugs = {p["slug"] for p in _m.PAGES}
        C[_lang].PAGES = [p for p in C[_lang].PAGES if p["slug"] not in _slugs] + list(_m.PAGES)

# ---------------------------------------------------------------------------
# Icons: one stroke family, 24px grid, 1.5 stroke.
# ---------------------------------------------------------------------------
ICONS = {
    "arrow": '<path d="M7 17 17 7M8 7h9v9"/>',
    "chev-l": '<path d="m15 18-6-6 6-6"/>',
    "chev-r": '<path d="m9 18 6-6-6-6"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "check": '<path d="m5 12.5 4.2 4L19 7"/>',
    "minus": '<path d="M6 12h12"/>',
    "menu": '<path d="M4 8h16M4 16h16"/>',
    "close": '<path d="m6 6 12 12M18 6 6 18"/>',
    "building": '<path d="M4 21V5a1 1 0 0 1 1-1h9a1 1 0 0 1 1 1v16M15 9h4a1 1 0 0 1 1 1v11M3 21h18M8 8h3M8 12h3M8 16h3"/>',
    "pin": '<path d="M12 21s7-6.1 7-11.5A7 7 0 0 0 5 9.5C5 14.9 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3Z"/>',
    "languages": '<path d="M4 6h9M8.5 4v2c0 4-2 7-5 8.5M6 10c1 2 3 3.6 5.5 4.5M13 20l4-9 4 9M14.4 17h5.2"/>',
    "scale": '<path d="M12 4v16M7 20h10M5 7h14M5 7l-3 6a3 3 0 0 0 6 0L5 7ZM19 7l-3 6a3 3 0 0 0 6 0l-3-6Z"/>',
    "clipboard": '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4h6v3H9zM9 12l2 2 4-4"/>',
    "doc": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8l-5-5Z"/><path d="M14 3v5h5M9 13h6M9 17h4"/>',
    "shield": '<path d="M12 3 5 6v6c0 4.4 3 7.6 7 9 4-1.4 7-4.6 7-9V6l-7-3Z"/><path d="m9 12 2 2 4-4"/>',
}


def icon(name, cls="ic"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


LOGO_ICON = (ROOT / "static" / "logo-icon.svg").read_text(encoding="utf-8") if (ROOT / "static" / "logo-icon.svg").exists() else ""


def esc(s):
    return html.escape(s, quote=True)


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def L(s, lang):
    return s.replace("@/", f"/{lang}/").replace("{EMAIL}", EMAIL)


def page_url(lang, slug=""):
    return f"/{lang}/" + (f"{slug}/" if slug else "")


def find_page(lang, key):
    for p in C[lang].PAGES:
        if p["slug"] == key or p["slug"].endswith("/" + key):
            return p
    return None


# ---------------------------------------------------------------------------
# Shared chrome
# ---------------------------------------------------------------------------

def arrow_btn(label, href, cls="btn"):
    return (f'<a class="{cls}" href="{href}"><span class="btn-label">{label}</span>'
            f'<span class="btn-tile" aria-hidden="true"><span class="btn-arr">{icon("arrow")}</span>'
            f'<span class="btn-arr btn-arr-2">{icon("arrow")}</span></span></a>')


def split_h(text, tag="h2", cls=""):
    """Heading animated word by word. Text may contain <em>."""
    return f'<{tag} class="split {cls}" data-split>{text}</{tag}>'


def head(lang, title, desc, slug, jsonld):
    c = C[lang]
    have = [l for l in LANGS if has_page(l, slug)]
    alt = ""
    if len(have) > 1:
        alt = "".join(f'<link rel="alternate" hreflang="{HREFLANG[l]}" href="{DOMAIN}{page_url(l, slug)}">' for l in have)
        alt += f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}{page_url("en", slug)}">'
    ga = ""
    if GA4_ID:
        ga = (f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>'
              f"<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','{GA4_ID}');</script>")
    font = "readex-arabic" if lang == "ar" else "outfit-latin"
    return f"""<!doctype html>
<html lang="{HREFLANG[lang]}" dir="{c.DIR}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{DOMAIN}{page_url(lang, slug)}">
{alt}
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{DOMAIN}{page_url(lang, slug)}">
<meta property="og:image" content="{DOMAIN}/static/img/og.jpg">
<meta property="og:locale" content="{'ar_SA' if lang == 'ar' else 'en_US'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0E1A19">
<link rel="icon" href="/static/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/static/fonts/{font}.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/static/fonts/outfit-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/static/css/site.css">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>
{ga}
</head>
"""


def brand(lang):
    c = C[lang]
    return (f'<a class="brand" href="{page_url(lang)}" aria-label="{esc(c.UI["brand"])}, {esc(c.UI["brand_sub"])}">'
            f'<span class="brand-mark">{LOGO_ICON}</span>'
            f'<span class="brand-text"><span class="brand-name">{c.UI["brand"]}</span>'
            f'<span class="brand-sub">{c.UI["brand_sub"]}</span></span></a>')


def nav(lang, slug):
    c, ui = C[lang], C[lang].UI
    other = "ar" if lang == "en" else "en"
    twin = page_url(other, slug)
    if other in LANGS and not has_page(other, slug):
        twin = page_url(other, "insights" if slug.startswith("insights/") else "")
    links = "".join(f'<a href="{L(h, lang)}"{" aria-current=\"page\"" if L(h, lang) == page_url(lang, slug) else ""}>{t}</a>' for t, h in ui["nav"])
    return f"""<a class="skip" href="#main">{ui['skip']}</a>
<header class="nav" data-nav>
  <div class="wrap nav-in">
    {brand(lang)}
    <nav class="nav-links" aria-label="Primary">{links}</nav>
    <div class="nav-end">
      <a class="lang" href="{twin}" hreflang="{HREFLANG[other]}" lang="{HREFLANG[other]}">{ui['lang_switch']}</a>
      <a class="nav-cta" href="{L(ui['cta_href'], lang)}">{ui['cta']}</a>
      <button class="burger" type="button" aria-expanded="false" aria-controls="menu" data-burger><span class="sr">{ui['menu']}</span>{icon('menu')}</button>
    </div>
  </div>
  <div class="menu" id="menu" hidden>
    <div class="wrap">
      <nav aria-label="Mobile">{links}<a href="{twin}" lang="{HREFLANG[other]}">{ui['lang_switch']}</a></nav>
      {arrow_btn(ui['cta'], L(ui['cta_href'], lang))}
    </div>
  </div>
</header>
"""


def footer(lang):
    ui = C[lang].UI
    cols = "".join(
        f'<div class="f-col"><h2 class="f-h">{h}</h2><ul>' + "".join(f'<li><a href="{L(u, lang)}">{t}</a></li>' for t, u in items) + "</ul></div>"
        for h, items in ui["footer_cols"])
    contact = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
    if PHONE_DISPLAY:
        contact += f'<a href="tel:{PHONE_TEL}" dir="ltr">{PHONE_DISPLAY}</a>'
    addr = f"{STREET_ADDRESS}, {ui['office']}" if STREET_ADDRESS else ui["office"]
    ph = placeholder_html() if SHOW_PLACEHOLDERS else ""
    return f"""<footer class="footer">
  <div class="wrap">
    <div class="f-top">
      <div class="f-about">{brand(lang)}<p>{ui['footer_blurb']}</p>
        <address>{esc(addr)}<br>{contact}{ph}</address></div>
      {cols}
    </div>
    <div class="f-bottom"><p>{ui['parent_line']}</p><p>© <span data-year>2026</span> Saudi Compliance. {ui['rights']}</p></div>
  </div>
  <p class="f-word" aria-hidden="true">Saudi Compliance</p>
</footer>
{'<a class="wa" href="https://wa.me/' + WHATSAPP + '" aria-label="WhatsApp">WhatsApp</a>' if WHATSAPP else ''}
<script src="/static/js/site.js" defer></script>
</body>
</html>
"""


def placeholder_html():
    missing = []
    if not STREET_ADDRESS:
        missing.append("Riyadh street address")
    missing.append("CR number")
    if not PHONE_DISPLAY:
        missing.append("phone")
    if not WHATSAPP:
        missing.append("WhatsApp")
    return f'<span class="ph" dir="ltr" lang="en">[To add before launch: {", ".join(missing)}]</span>'


def img(name, alt, cls="", sizes="100vw", eager=False):
    return (f'<img class="{cls}" src="/static/img/{name}.webp" alt="{esc(alt)}" '
            f'{"fetchpriority=\"high\"" if eager else "loading=\"lazy\""} decoding="async">')


def cta_band(lang):
    h = C[lang].HOME
    ui = C[lang].UI
    return f"""<section class="cta-band dark" aria-labelledby="cta-h">
  <canvas class="wave" data-wave="cta" aria-hidden="true"></canvas>
  <div class="wrap cta-in">
    <h2 id="cta-h" class="split display-2" data-split>{"<br>".join(h['cta_h2'])}</h2>
    <p class="lede">{h['cta_lede']}</p>
    {arrow_btn(ui['cta'], L(ui['cta_href'], lang))}
  </div>
</section>"""


# ---------------------------------------------------------------------------
# JSON-LD
# ---------------------------------------------------------------------------

def org_ld(lang):
    ui = C[lang].UI
    org = {
        "@type": ["ProfessionalService", "Organization"],
        "@id": f"{DOMAIN}/#org",
        "name": "Saudi Compliance",
        "alternateName": "سعودي كومبلاينس",
        "url": DOMAIN,
        "logo": f"{DOMAIN}/static/logo-icon.png",
        "image": f"{DOMAIN}/static/img/og.jpg",
        "description": strip_tags(C[lang].HOME["description"]),
        "email": EMAIL,
        "areaServed": {"@type": "Country", "name": "Saudi Arabia"},
        "knowsLanguage": ["en", "ar"],
        "address": {"@type": "PostalAddress", "addressLocality": "Riyadh", "addressCountry": "SA",
                    **({"streetAddress": STREET_ADDRESS} if STREET_ADDRESS else {})},
        "parentOrganization": {"@type": "Organization", "name": PARENT["name"], "url": PARENT["url"]},
        "knowsAbout": ["SAMA payment institution licence", "CMA FinTech Experimental Permit", "AML/CFT compliance",
                       "Saudi Personal Data Protection Law", "BNPL licensing", "Open banking licensing"],
    }
    if PHONE_TEL:
        org["telephone"] = PHONE_TEL
    return org


def crumbs_ld(lang, trail):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": strip_tags(n), "item": f"{DOMAIN}{u}"} for i, (n, u) in enumerate(trail)]}


# ---------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------

def build_home(lang):
    c, h, ui = C[lang], C[lang].HOME, C[lang].UI
    ld = {"@context": "https://schema.org", "@graph": [org_ld(lang), {
        "@type": "WebSite", "@id": f"{DOMAIN}/#site", "url": DOMAIN, "name": "Saudi Compliance",
        "inLanguage": HREFLANG[lang], "publisher": {"@id": f"{DOMAIN}/#org"}}]}

    marquee = "".join(f'<li>{m}</li>' for m in h["marquee"])
    stmt = "".join(
        (f'<span class="num" data-count="{t}">{t}</span>' if kind == "count" else esc(t)) for t, kind in h["statement"])
    words = "".join(f"<li>{w}</li>" for w in h["words"])
    svc = "".join(f"""<li class="svc">
        <a href="{L(u, lang)}">
          <span class="svc-img">{img(im, '')}</span>
          <span class="svc-body"><span class="svc-t">{t}</span><span class="svc-d">{d}</span></span>
          <span class="svc-go" aria-hidden="true">{icon('arrow')}</span>
        </a></li>""" for im, t, d, u in h["services"])
    principles = "".join(f'<li><h3>{t}</h3><p>{d}</p></li>' for t, d in h["principles"])
    lic = "".join(f"""<li class="lic">
        <a href="{L(u, lang)}">
          <span class="lic-img">{img(im, '')}</span>
          <span class="tag">{tag}</span>
          <span class="lic-t">{t}</span>
          <span class="lic-f">{f}</span>
        </a></li>""" for im, tag, t, f, u in h["licences"])
    steps_nav = "".join(f'<li><a href="#step-{i}" data-step-link="{i}">{s[1]}</a></li>' for i, s in enumerate(h["steps"]))
    steps = "".join(f"""<article class="step" id="step-{i}" data-step="{i}">
        <div class="step-img">{img(im, '')}</div>
        <h3><a href="{L(ui['stage_links'][i], lang)}">{t}</a></h3><p>{d}</p>
      </article>""" for i, (im, t, d) in enumerate(h["steps"]))
    why = "".join(f'<li class="float-card" style="--i:{i}"><h3>{t}</h3><p>{d}</p></li>'
                  for i, (ic, t, d) in enumerate(h["why_cards"]))
    them_t, them = h["compare"]["them"]
    us_t, us_sub, us = h["compare"]["us"]
    them_li = "".join(f"<li>{icon('minus')}<span>{x}</span></li>" for x in them)
    us_li = "".join(f"<li>{icon('check')}<span>{x}</span></li>" for x in us)
    nums = "".join(f'<li><span class="big" data-count="{n}">{n}</span><span class="nl">{l}</span><span class="ns">{s}</span></li>'
                   for n, l, s in h["numbers"])
    faq = "".join(f'<details class="qa"><summary><span>{q}</span>{icon("plus")}</summary><div class="qa-a"><p>{L(a, lang)}</p></div></details>'
                  for q, a in h["faq"])
    hc_img, hc_t, hc_d = h["hero_card"]

    body = f"""<body class="home">
{nav(lang, '')}
<main id="main">
<section class="hero dark" aria-labelledby="hero-h">
  <canvas class="wave" data-wave="hero" aria-hidden="true"></canvas>
  <div class="wrap hero-in">
    <h1 id="hero-h" class="split display-1" data-split data-split-now>{"<br>".join(h['h1'])}</h1>
    <div class="hero-foot">
      <div class="hero-copy rise" style="--d:.55s">
        <p class="lede">{h['lede']}</p>
        <div class="btn-row">{arrow_btn(ui['cta'], L(ui['cta_href'], lang))}
          <a class="link-arrow" href="{L(h['secondary_cta'][1], lang)}">{h['secondary_cta'][0]} {icon('arrow')}</a></div>
      </div>
      <figure class="hero-card rise" style="--d:.8s">{img(hc_img, '', eager=True)}<figcaption><strong>{hc_t}</strong><span>{hc_d}</span></figcaption></figure>
    </div>
  </div>
</section>

<section class="band dark" aria-label="Frameworks">
  <div class="marquee" data-marquee><ul>{marquee}</ul></div>
</section>

<section class="statement paper">
  <div class="wrap stmt-in">
    <p class="stmt" data-fill>{stmt}</p>
    <div class="stmt-foot">
      {arrow_btn(h['statement_cta'][0], L(h['statement_cta'][1], lang), 'btn btn-ghost')}
      <p class="src">{h['statement_source']}</p>
    </div>
  </div>
</section>

<section class="words paper-2" aria-hidden="true">
  <div class="marquee marquee-big" data-marquee><ul>{words}</ul></div>
</section>

<section class="services paper" aria-labelledby="svc-h">
  <div class="wrap">
    <div class="sec-head">
      {split_h(h['services_h2'], 'h2', 'display-2').replace('<h2 ', '<h2 id="svc-h" ', 1)}
      <div class="car-ctrl"><button type="button" data-car="-1" aria-label="{ui['prev']}">{icon('chev-l')}</button><button type="button" data-car="1" aria-label="{ui['next']}">{icon('chev-r')}</button></div>
    </div>
  </div>
  <ul class="carousel" data-carousel>{svc}</ul>
  <div class="wrap sec-foot"><p>{h['services_foot']}</p><span class="rule"></span><a class="link-arrow" href="{L(h['services_all'][1], lang)}">{h['services_all'][0]} {icon('arrow')}</a></div>
</section>

<section class="principles dark" aria-labelledby="pr-h">
  <div class="wrap">
    <div class="pr-head">{split_h(h['principles_h2'], 'h2', 'display-2').replace('<h2 ', '<h2 id="pr-h" ', 1)}<p class="lede">{h['principles_lede']}</p></div>
    <ol class="pr-list">{principles}</ol>
    <figure class="wide"><div class="wide-img" data-parallax>{img(h['wide_img'], '')}</div></figure>
  </div>
</section>

<section class="licences paper" aria-labelledby="lic-h">
  <div class="wrap">
    {split_h(h['licences_h2'], 'h2', 'display-2 center').replace('<h2 ', '<h2 id="lic-h" ', 1)}
    <ul class="lic-grid">{lic}</ul>
    <div class="center-row">{arrow_btn(h['licences_all'][0], L(h['licences_all'][1], lang), 'btn btn-ghost')}</div>
  </div>
</section>

<section class="steps paper" aria-labelledby="st-h">
  <div class="wrap">
    <div class="st-head">{split_h(h['steps_h2'], 'h2', 'display-2').replace('<h2 ', '<h2 id="st-h" ', 1)}<p class="lede">{h['steps_lede']}</p></div>
    <div class="st-grid">
      <ol class="st-nav" data-step-nav>{steps_nav}</ol>
      <div class="st-panels"><span class="st-thread" aria-hidden="true"><span data-thread></span></span>{steps}</div>
    </div>
  </div>
</section>

<section class="why paper-2" aria-labelledby="why-h" data-float>
  <div class="why-sticky">
    <div class="why-center">
      {split_h(h['why_h2'], 'h2', 'display-2 center').replace('<h2 ', '<h2 id="why-h" ', 1)}
      <p class="lede">{h['why_lede']}</p>
      {arrow_btn(ui['cta'], L(ui['cta_href'], lang))}
    </div>
  </div>
  <ul class="float-cards">{why}</ul>
</section>

<section class="compare dark" aria-labelledby="cmp-h">
  <div class="wrap">
    {split_h(h['compare_h2'], 'h2', 'display-2 center').replace('<h2 ', '<h2 id="cmp-h" ', 1)}
    <div class="cmp">
      <div class="cmp-them"><h3>{them_t}</h3><ul>{them_li}</ul></div>
      <div class="cmp-us"><h3>{us_t}</h3><p>{us_sub}</p><ul>{us_li}</ul></div>
    </div>
    <h2 class="nums-h display-3">{h['numbers_h2']}</h2>
    <ul class="nums">{nums}</ul>
  </div>
</section>

<section class="faq paper" aria-labelledby="faq-h">
  <div class="wrap faq-in">
    {split_h(ui['faq_title'], 'h2', 'display-2').replace('<h2 ', '<h2 id="faq-h" ', 1)}
    <div class="qa-list">{faq}</div>
  </div>
</section>
{cta_band(lang)}
</main>
"""
    faq_ld = None  # FAQ rich results retired (May 2026); the Q&A stays as on-page content only.
    write(lang, "", head(lang, h["title"], h["description"], "", ld) + body + footer(lang))


# ---------------------------------------------------------------------------
# Inner pages
# ---------------------------------------------------------------------------

def render_block(b, lang, idx):
    bid = f"s{idx}"
    h2 = f'<h2 id="{bid}" class="split" data-split>{b["h2"]}</h2>' if b.get("h2") else ""
    t = b["type"]
    if t == "prose":
        return f'<section class="blk">{h2}' + "".join(f"<p>{L(p, lang)}</p>" for p in b["body"]) + "</section>"
    if t == "list":
        return f'<section class="blk">{h2}<ul class="sq">' + "".join(f"<li>{L(i, lang)}</li>" for i in b["items"]) + "</ul></section>"
    if t == "steps":
        return (f'<section class="blk">{h2}<ol class="stepped">' +
                "".join(f'<li><h3>{a}</h3><p>{L(d, lang)}</p></li>' for a, d in b["items"]) + "</ol></section>")
    if t == "table":
        th = "".join(f'<th scope="col">{x}</th>' for x in b["head"])
        rows = "".join("<tr>" + "".join((f'<th scope="row">{L(x, lang)}</th>' if j == 0 else f"<td>{L(x, lang)}</td>") for j, x in enumerate(r)) + "</tr>" for r in b["rows"])
        note = f'<p class="note">{b["note"]}</p>' if b.get("note") else ""
        return f'<section class="blk">{h2}<div class="tbl"><table><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table></div>{note}</section>'
    if t == "callout":
        return f'<aside class="callout"><p class="callout-t">{b["title"]}</p><p>{L(b["body"], lang)}</p></aside>'
    if t == "faq":
        return (f'<section class="blk">{h2}<div class="qa-list">' +
                "".join(f'<details class="qa"><summary><span>{q}</span>{icon("plus")}</summary><div class="qa-a"><p>{L(a, lang)}</p></div></details>' for q, a in b["items"]) +
                "</div></section>")
    if t == "cards":
        return (f'<section class="blk">{h2}<ul class="mini-cards">' +
                "".join(f'<li><a href="{L(u, lang)}"><span class="mc-img">{img(im, "")}</span><span class="mc-t">{tt}</span><span class="mc-d">{d}</span></a></li>' for im, tt, d, u in b["items"]) +
                "</ul></section>")
    raise ValueError(t)


def tracker(lang, stage):
    if stage is None:
        return ""
    ui = C[lang].UI
    items = "".join(
        f'<li class="{"on" if i == stage else ("done" if i < stage else "")}"><a href="{L(u, lang)}"{" aria-current=\"step\"" if i == stage else ""}><span class="tr-dot"></span>{s}</a></li>'
        for i, (s, u) in enumerate(zip(ui["stages"], ui["stage_links"])))
    return f'<nav class="tracker" aria-label="{ui["stage_label"]}"><div class="wrap"><ol>{items}</ol></div></nav>'


def inner_hero(lang, h1, lede, hero_img, trail, cta=True):
    ui = C[lang].UI
    crumbs = "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in trail[:-1]) + f'<li aria-current="page">{strip_tags(trail[-1][0])}</li>'
    return f"""<section class="hero hero-inner dark">
  <canvas class="wave" data-wave="inner" aria-hidden="true"></canvas>
  <div class="wrap hi-in">
    <div class="hi-copy">
      <ol class="crumbs">{crumbs}</ol>
      <h1 class="split display-1b" data-split data-split-now>{h1}</h1>
      <p class="lede rise" style="--d:.5s">{lede}</p>
      {('<div class="rise" style="--d:.7s">' + arrow_btn(ui['cta'], L(ui['cta_href'], lang)) + '</div>') if cta else ''}
    </div>
    {f'<figure class="hi-img clip-in">{img(hero_img, "", eager=True)}</figure>' if hero_img else ''}
  </div>
</section>"""


def build_inner(lang, p):
    c, ui = C[lang], C[lang].UI
    slug = p["slug"]
    trail = [(ui["home"], page_url(lang))]
    if "/" in slug:
        parent = find_page(lang, slug.split("/")[0])
        trail.append((strip_tags(parent["h1"]), page_url(lang, parent["slug"])))
    trail.append((p["h1"], page_url(lang, slug)))

    blocks = "".join(render_block(b, lang, i) for i, b in enumerate(p["blocks"]))
    toc = "".join(f'<li><a href="#s{i}" data-toc="s{i}">{strip_tags(b["h2"])}</a></li>' for i, b in enumerate(p["blocks"]) if b.get("h2"))
    sources = ""
    if p["sources"]:
        sources = (f'<section class="sources"><h2>{ui["sources"]}</h2><ul>' +
                   "".join(f'<li><a href="{u}" rel="noopener" target="_blank">{n}</a></li>' for n, u in p["sources"]) + "</ul></section>")
    meta = f'<p class="reviewed">{ui["reviewed"]}: {c.REVIEWED}</p><p class="disclaimer">{ui["disclaimer"]}</p>'
    rel_cards = ""
    for r in p.get("related", []):
        rp = find_page(lang, r)
        if not rp:
            continue
        rel_cards += (f'<li><a href="{page_url(lang, rp["slug"])}"><span class="mc-img">{img(rp["hero"], "")}</span>'
                      f'<span class="mc-t">{strip_tags(rp["h1"])}</span><span class="mc-d">{strip_tags(rp["lede"])[:120].rsplit(" ", 1)[0]}…</span></a></li>')
    related = f'<section class="related paper-2"><div class="wrap"><h2 class="display-3">{ui["related"]}</h2><ul class="mini-cards">{rel_cards}</ul></div></section>' if rel_cards else ""

    is_guide = slug.startswith("licensing/") or slug == "digital-assets"
    main_ld = {
        "@type": "Article" if is_guide else "Service",
        "name" if not is_guide else "headline": strip_tags(p["h1"]),
        "description": p["description"],
        "url": f"{DOMAIN}{page_url(lang, slug)}",
        "inLanguage": HREFLANG[lang],
    }
    if is_guide:
        main_ld.update({"dateModified": "2026-10-11", "publisher": {"@id": f"{DOMAIN}/#org"}, "author": {"@id": f"{DOMAIN}/#org"},
                        "image": f"{DOMAIN}/static/img/{p['hero']}.webp"})
    else:
        main_ld.update({"provider": {"@id": f"{DOMAIN}/#org"}, "areaServed": {"@type": "Country", "name": "Saudi Arabia"}})
    ld = {"@context": "https://schema.org", "@graph": [org_ld(lang), main_ld, crumbs_ld(lang, trail)]}

    body = f"""<body class="inner">
{nav(lang, slug)}
<main id="main">
{inner_hero(lang, p['h1'], p['lede'], p['hero'], trail)}
{tracker(lang, p['stage'])}
<div class="paper article-wrap">
  <div class="wrap art">
    <aside class="toc"><p class="toc-h">{ui['on_this_page']}</p><ol data-toc-list>{toc}</ol></aside>
    <article class="prose">{blocks}{sources}{meta}</article>
  </div>
</div>
{related}
{cta_band(lang)}
</main>
"""
    write(lang, slug, head(lang, p["title"], p["description"], slug, ld) + body + footer(lang))


def build_contact(lang):
    c, ui, k = C[lang], C[lang].UI, C[lang].CONTACT
    f = ui["form"]
    opts = "".join(f"<option>{o}</option>" for o in f["stage_opts"])
    steps = "".join(f"<li>{s}</li>" for s in k["aside"])
    trail = [(ui["home"], page_url(lang)), (k["h1"], page_url(lang, "contact"))]
    ld = {"@context": "https://schema.org", "@graph": [org_ld(lang), {"@type": "ContactPage", "url": f"{DOMAIN}{page_url(lang, 'contact')}"}, crumbs_ld(lang, trail)]}
    ptitle = c.LEGAL["privacy"]["title"]
    consent = re.sub(re.escape(ptitle), lambda m: f'<a href="{page_url(lang, "privacy")}">{m.group(0)}</a>', f["consent"], count=1, flags=re.I)
    wa = f'<a class="link-arrow" href="https://wa.me/{WHATSAPP}">WhatsApp {icon("arrow")}</a>' if WHATSAPP else ""
    body = f"""<body class="inner contact">
{nav(lang, 'contact')}
<main id="main">
{inner_hero(lang, k['h1'], k['lede'], None, trail, cta=False)}
<div class="paper article-wrap">
  <div class="wrap contact-grid">
    <form class="form" action="https://api.web3forms.com/submit" method="POST" data-form>
      <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
      <input type="hidden" name="subject" value="Saudi Compliance enquiry ({lang})">
      <input type="checkbox" name="botcheck" class="sr" tabindex="-1" autocomplete="off">
      <label><span>{f['name']}</span><input name="name" required autocomplete="name"></label>
      <label><span>{f['email']}</span><input name="email" type="email" required autocomplete="email" dir="ltr"></label>
      <label><span>{f['company']}</span><input name="company" autocomplete="organization"></label>
      <label><span>{f['stage']}</span><select name="stage">{opts}</select></label>
      <label class="full"><span>{f['message']}</span><textarea name="message" rows="5" required></textarea></label>
      <p class="consent full">{consent}</p>
      <div class="full form-end"><button class="btn" type="submit" data-sending="{f['sending']}"><span class="btn-label">{f['send']}</span><span class="btn-tile" aria-hidden="true"><span class="btn-arr">{icon('arrow')}</span><span class="btn-arr btn-arr-2">{icon('arrow')}</span></span></button>
        <p class="form-msg" role="status" data-ok="{esc(f['ok'])}" data-err="{esc(f['err'])} {EMAIL}"></p></div>
    </form>
    <aside class="contact-aside">
      <h2 class="display-3">{k['aside_h']}</h2>
      <ol class="stepped small">{steps}</ol>
      {placeholder_html() if SHOW_PLACEHOLDERS else ''}
      <p class="addr">{ui['office']}<br><a href="mailto:{EMAIL}">{EMAIL}</a>{'<br><a href="tel:' + PHONE_TEL + '" dir="ltr">' + PHONE_DISPLAY + '</a>' if PHONE_DISPLAY else ''}</p>
      {wa}
    </aside>
  </div>
</div>
</main>
"""
    write(lang, "contact", head(lang, k["title"], k["description"], "contact", ld) + body + footer(lang))


def build_legal(lang, key):
    ui, d = C[lang].UI, C[lang].LEGAL[key]
    trail = [(ui["home"], page_url(lang)), (d["title"], page_url(lang, key))]
    secs = "".join(f'<section class="blk"><h2>{t}</h2><p>{L(b, lang)}</p></section>' for t, b in d["body"])
    ld = {"@context": "https://schema.org", "@graph": [org_ld(lang), crumbs_ld(lang, trail)]}
    body = f"""<body class="inner legal">
{nav(lang, key)}
<main id="main">
{inner_hero(lang, d['title'], f"{ui['reviewed']}: {C[lang].REVIEWED}", None, trail, cta=False)}
<div class="paper article-wrap"><div class="wrap art art-solo"><article class="prose">{secs}</article></div></div>
</main>
"""
    write(lang, key, head(lang, d["title"] + " | Saudi Compliance", d["description"], key, ld) + body + footer(lang))


def build_404():
    ui = C["en"].UI
    t, d, b = ui["not_found"]
    body = f"""<body class="inner">
{nav('en', '')}
<main id="main">
<section class="hero hero-inner dark nf"><canvas class="wave" data-wave="inner" aria-hidden="true"></canvas>
<div class="wrap hi-in"><div class="hi-copy"><h1 class="display-1b">{t}</h1><p class="lede">{d}</p>{arrow_btn(b, '/en/')}
<p class="lede" lang="ar" dir="rtl"><a href="/ar/">الصفحة الرئيسية بالعربية</a></p></div></div></section>
</main>
"""
    (OUT / "404.html").write_text(head("en", t + " | Saudi Compliance", d, "", {"@context": "https://schema.org", "@type": "WebPage"}).replace('<link rel="canonical"', '<meta name="robots" content="noindex"><link rel="canonical"') + body + footer("en"), encoding="utf-8")


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
URLS = []
ARTICLE_URLS = {}


def build_insights(lang):
    ui, iu = C[lang].UI, INS.UI[lang]
    arts = INS.load(lang)
    other = "ar" if lang == "en" else "en"
    other_slugs = {a["slug"] for a in INS.load(other)} if other in LANGS else set()
    # Index
    trail = [(ui["home"], page_url(lang)), (iu["label"], page_url(lang, "insights"))]
    cards = "".join(
        f'<li><a href="{page_url(lang, "insights/" + a["slug"])}"><span class="mc-img">{img(a.get("hero", "riyadh-aerial"), "")}</span>'
        f'<span class="mc-meta">{esc(a.get("tags", ""))} · {INS.minutes(a["minutes"], lang)}</span>'
        f'<span class="mc-t">{strip_tags(a.get("h1", a["title"]))}</span><span class="mc-d">{esc(a["description"])}</span></a></li>'
        for a in arts)
    ld = {"@context": "https://schema.org", "@graph": [org_ld(lang), {"@type": "CollectionPage", "name": iu["index_title"], "url": f"{DOMAIN}{page_url(lang, 'insights')}",
          "inLanguage": HREFLANG[lang], "hasPart": [{"@type": "Article", "headline": a["title"], "url": f"{DOMAIN}{page_url(lang, 'insights/' + a['slug'])}"} for a in arts]},
          crumbs_ld(lang, trail)]}
    body = f"""<body class="inner insights">
{nav(lang, 'insights')}
<main id="main">
{inner_hero(lang, iu['index_h1'], iu['index_lede'], 'riyadh-aerial', trail)}
<div class="paper article-wrap"><div class="wrap"><ul class="mini-cards ins-grid">{cards}</ul></div></div>
{cta_band(lang)}
</main>
"""
    write(lang, "insights", head(lang, iu["index_title"], iu["index_desc"], "insights", ld) + body + footer(lang))
    # Articles
    for a in arts:
        slug = "insights/" + a["slug"]
        html_body, toc = INS.render(a["body"], lang)
        h1 = a.get("h1", a["title"])
        trail = [(ui["home"], page_url(lang)), (iu["label"], page_url(lang, "insights")), (h1, page_url(lang, slug))]
        langs = [lang] + ([other] if a["slug"] in other_slugs else [])
        prev = ARTICLE_URLS.get(a["slug"], ([], ""))[0]
        ARTICLE_URLS[a["slug"]] = (sorted(set(prev + langs)), a.get("updated", a.get("date", "2026-10-11")))
        toc_html = "".join(f'<li><a href="#{i}" data-toc="{i}">{esc(t)}</a></li>' for i, t in toc)
        svc = a.get("service", "")
        cta = (f'<aside class="callout art-cta"><p class="callout-t">{iu["need"]}</p><p><a href="{L(svc, lang)}">{esc(a.get("service_label", ui["cta"]))}</a></p>'
               f'<p><a href="{L(ui["cta_href"], lang)}">{ui["cta"]}</a></p></aside>') if svc else ""
        alt = (f'<p class="alt-lang"><a href="{page_url(other, slug)}" lang="{HREFLANG[other]}" hreflang="{HREFLANG[other]}">{iu["other_lang"]}</a></p>'
               if other in langs else "")
        meta = (f'<p class="art-meta"><span>{iu["by"]}</span><span>{iu["published"]}: <time datetime="{a.get("date")}">{a.get("date")}</time></span>'
                f'<span>{iu["updated"]}: <time datetime="{a.get("updated", a.get("date"))}">{a.get("updated", a.get("date"))}</time></span><span>{INS.minutes(a["minutes"], lang)}</span></p>')
        art_ld = {"@type": "Article", "headline": a["title"], "description": a["description"], "inLanguage": HREFLANG[lang],
                  "datePublished": a.get("date"), "dateModified": a.get("updated", a.get("date")),
                  "image": f"{DOMAIN}/static/img/{a.get('hero', 'og')}.webp", "url": f"{DOMAIN}{page_url(lang, slug)}",
                  "author": {"@id": f"{DOMAIN}/#org"}, "publisher": {"@id": f"{DOMAIN}/#org"},
                  "mainEntityOfPage": f"{DOMAIN}{page_url(lang, slug)}"}
        ld = {"@context": "https://schema.org", "@graph": [org_ld(lang), art_ld, crumbs_ld(lang, trail)]}
        doc = head(lang, a["title"], a["description"], slug, ld)
        doc = doc.replace('<meta property="og:type" content="website">',
                          '<meta property="og:type" content="article">'
                          f'<meta property="article:published_time" content="{a.get("date")}">'
                          f'<meta property="article:modified_time" content="{a.get("updated", a.get("date"))}">', 1)
        if other not in langs:  # only one edition: hreflang must not point at a missing page
            doc = re.sub(r'<link rel="alternate" hreflang="[^"]+" href="[^"]+">', "", doc)
        body = f"""<body class="inner article">
{nav(lang, slug)}
<main id="main">
{inner_hero(lang, h1, a['description'], a.get('hero'), trail)}
<div class="paper article-wrap">
  <div class="wrap art">
    <aside class="toc"><p class="toc-h">{iu['on_page']}</p><ol data-toc-list>{toc_html}</ol></aside>
    <article class="prose post">{meta}{alt}{html_body}{cta}<p class="disclaimer">{ui['disclaimer']}</p></article>
  </div>
</div>
{cta_band(lang)}
</main>
"""
        write(lang, slug, doc + body + footer(lang))


def write(lang, slug, doc):
    p = OUT / lang / slug / "index.html" if slug else OUT / lang / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(doc, encoding="utf-8")
    if not slug.startswith("insights/"):
        URLS.append((lang, slug))


def root_files():
    # Root: language chooser that sends visitors to their language.
    (OUT / "index.html").write_text(f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>Saudi Compliance</title>
<link rel="canonical" href="{DOMAIN}/en/">
<link rel="alternate" hreflang="en" href="{DOMAIN}/en/"><link rel="alternate" hreflang="ar-SA" href="{DOMAIN}/ar/"><link rel="alternate" hreflang="x-default" href="{DOMAIN}/">
<script>location.replace((navigator.language||'').toLowerCase().startsWith('ar')?'/ar/':'/en/')</script>
<style>body{{margin:0;min-height:100vh;display:grid;place-items:center;background:#0E1A19;color:#EEF3EF;font:18px system-ui}}a{{color:#BFEF4C;margin:0 1em}}</style></head>
<body><p><a href="/en/">English</a><a href="/ar/" lang="ar">العربية</a></p></body></html>""", encoding="utf-8")

    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for lang_, slug in URLS:
        have = [l for l in LANGS if has_page(l, slug)]
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{HREFLANG[l]}" href="{DOMAIN}{page_url(l, slug)}"/>' for l in have) if len(have) > 1 else ""
        sm.append(f"<url><loc>{DOMAIN}{page_url(lang_, slug)}</loc><lastmod>2026-10-11</lastmod>{alts}</url>")
    for slug, (langs, mod) in ARTICLE_URLS.items():
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{HREFLANG[l]}" href="{DOMAIN}{page_url(l, "insights/" + slug)}"/>' for l in langs) if len(langs) > 1 else ""
        for l in langs:
            sm.append(f"<url><loc>{DOMAIN}{page_url(l, 'insights/' + slug)}</loc><lastmod>{mod}</lastmod>{alts}</url>")
    sm.append("</urlset>")
    (OUT / "sitemap.xml").write_text("\n".join(sm), encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n", encoding="utf-8")

    en = C["en"]
    lines = ["# Saudi Compliance", "", "> " + strip_tags(en.HOME["description"]), "",
             "Regulatory compliance advisory in Riyadh for fintechs: incorporation, SAMA and CMA licensing, MLRO and AML programmes, ongoing compliance, independent review. A ComplyFactor company.", "",
             "## Pages"]
    for p in en.PAGES:
        lines.append(f"- [{strip_tags(p['h1'])}]({DOMAIN}{page_url('en', p['slug'])}): {p['description']}")
    arts = INS.load("en")
    if arts:
        lines += ["", "## Guides"] + [f"- [{a['title']}]({DOMAIN}{page_url('en', 'insights/' + a['slug'])}): {a['description']}" for a in arts]
    lines += ["", f"Arabic edition: {DOMAIN}/ar/", f"Contact: {EMAIL}"]
    (OUT / "llms.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    (OUT / "CNAME").write_text(DOMAIN.split("//", 1)[1] + chr(10), encoding="utf-8")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(STATIC, OUT / "static")
    for lang in LANGS:
        build_home(lang)
        for p in C[lang].PAGES:
            build_inner(lang, p)
        build_contact(lang)
        for key in C[lang].LEGAL:
            build_legal(lang, key)
        build_insights(lang)
    build_404()
    root_files()
    n = sum(1 for _ in OUT.rglob("index.html"))
    print(f"built {n} pages into {OUT}")


if __name__ == "__main__":
    main()
