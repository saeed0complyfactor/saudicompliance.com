"""Insights (articles) for saudicompliance.com.

Articles live in content/insights/<lang>/<slug>.md with a small front matter block:

    ---
    title: SEO title (<= 60 chars)
    h1: On-page headline, may contain <em>accent</em>
    description: Meta description (<= 155 chars)
    date: 2026-10-11
    updated: 2026-10-11
    hero: signing                      # image key in static/img
    service: @/licensing/payment-institution-licence/
    service_label: Payment institution licence support
    tags: SAMA, Payments
    ---

The body is a deliberately small Markdown subset: ## and ### headings, paragraphs,
"- " and "1. " lists, pipe tables, "> " callouts, **bold**, *italic*, [links](url).
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "content" / "insights"

UI = {
    "en": {"index_title": "Insights: Saudi Fintech Licensing & Compliance Guides",
           "index_desc": "Guides to SAMA and CMA licensing, AML/CFT, digital assets and market developments in Saudi Arabia, from Saudi Compliance.",
           "index_h1": "Guides for the <em>Saudi</em> licence path",
           "index_lede": "Plain-language guides to licensing, AML and regulatory change in Saudi Arabia, each one sourced to the regulator.",
           "label": "Insights", "read": "Read the guide", "min": "min read", "published": "Published", "updated": "Updated",
           "need": "Need help with this?", "by": "Saudi Compliance editorial team", "on_page": "On this page",
           "all": "All guides", "other_lang": "اقرأ بالعربية"},
    "ar": {"index_title": "رؤى: أدلة الترخيص والامتثال للتقنية المالية في السعودية",
           "index_desc": "أدلة حول تراخيص البنك المركزي السعودي وهيئة السوق المالية ومكافحة غسل الأموال والأصول الرقمية ومستجدات السوق في المملكة.",
           "index_h1": "أدلة لمسار <em>الترخيص</em> في المملكة",
           "index_lede": "أدلة واضحة حول الترخيص ومكافحة غسل الأموال والتغييرات التنظيمية في المملكة، وكل منها موثّق بمصادر الجهة الرقابية.",
           "label": "رؤى", "read": "اقرأ الدليل", "min": "دقائق قراءة", "published": "نُشر", "updated": "حُدّث",
           "need": "هل تحتاجون إلى مساعدة؟", "by": "فريق التحرير في سعودي كومبلاينس", "on_page": "في هذه الصفحة",
           "all": "جميع الأدلة", "other_lang": "Read in English"},
}


def parse(path):
    raw = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", raw, re.S)
    if not m:
        raise ValueError(f"{path}: missing front matter")
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    meta["slug"] = path.stem
    meta["body"] = m.group(2)
    words = len(re.findall(r"\w+", strip(meta["body"])))
    meta["minutes"] = max(3, round(words / 220))
    return meta


def strip(s):
    return re.sub(r"<[^>]+>", "", s)


def inline(s, lang):
    s = html.escape(s, quote=False)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: link(m.group(1), m.group(2), lang), s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?![*\w])", r"<em>\1</em>", s)
    return s


def link(text, url, lang):
    url = html.unescape(url)
    if url.startswith("@/"):
        url = f"/{lang}/" + url[2:]
    ext = url.startswith("http")
    attrs = ' rel="noopener" target="_blank"' if ext else ""
    return f'<a href="{html.escape(url, quote=True)}"{attrs}>{text}</a>'


def slugify(s):
    s = re.sub(r"<[^>]+>", "", s).lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.U)
    return re.sub(r"\s+", "-", s.strip())[:60] or "s"


def render(md, lang):
    """Return (html, toc[(id, text)])."""
    out, toc = [], []
    lines = md.strip().splitlines()
    i = 0
    used = set()
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            i += 1
            continue
        if ln.startswith("## ") or ln.startswith("### "):
            lvl = 2 if ln.startswith("## ") else 3
            text = ln[lvl + 1:].strip()
            hid = slugify(text) if lang == "en" else f"s{len(toc) + 1}"
            while hid in used:
                hid += "-2"
            used.add(hid)
            if lvl == 2:
                toc.append((hid, strip(inline(text, lang))))
            out.append(f'<h{lvl} id="{hid}">{inline(text, lang)}</h{lvl}>')
            i += 1
            continue
        if ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            head, body = rows[0], rows[1:]
            th = "".join(f'<th scope="col">{inline(c, lang)}</th>' for c in head)
            tb = "".join("<tr>" + "".join((f'<th scope="row">{inline(c, lang)}</th>' if j == 0 else f"<td>{inline(c, lang)}</td>") for j, c in enumerate(r)) + "</tr>" for r in body)
            out.append(f'<div class="tbl"><table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div>')
            continue
        if ln.startswith("> "):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i][1:].strip())
                i += 1
            paras = " ".join(buf).split("  ")
            title = ""
            first = paras[0]
            mt = re.match(r"\*\*(.+?)\*\*\s*(.*)", first)
            if mt:
                title, first = mt.group(1), mt.group(2)
                paras[0] = first
            t = f'<p class="callout-t">{inline(title, lang)}</p>' if title else ""
            out.append(f'<aside class="callout">{t}' + "".join(f"<p>{inline(p, lang)}</p>" for p in paras if p) + "</aside>")
            continue
        if re.match(r"^(- |\d+\. )", ln):
            ordered = bool(re.match(r"^\d+\. ", ln))
            items = []
            while i < len(lines) and re.match(r"^(- |\d+\. )", lines[i]):
                items.append(re.sub(r"^(- |\d+\. )", "", lines[i]).strip())
                i += 1
                while i < len(lines) and lines[i].startswith("   ") and lines[i].strip():
                    items[-1] += " " + lines[i].strip()
                    i += 1
            tag, cls = ("ol", "num") if ordered else ("ul", "sq")
            out.append(f'<{tag} class="{cls}">' + "".join(f"<li>{inline(x, lang)}</li>" for x in items) + f"</{tag}>")
            continue
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{2,3} |\||> |- |\d+\. )", lines[i]):
            buf.append(lines[i].strip())
            i += 1
        out.append(f"<p>{inline(' '.join(buf), lang)}</p>")
    return "\n".join(out), toc


def load(lang):
    d = SRC / lang
    if not d.exists():
        return []
    arts = [a for a in (parse(p) for p in sorted(d.glob("*.md"))) if a.get("draft", "").lower() != "true"]
    return sorted(arts, key=lambda a: a.get("date", ""), reverse=True)
