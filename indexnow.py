"""Ping IndexNow (Bing, Yandex, Seznam, Naver...) with every URL in site/sitemap.xml.

Run after a deploy has finished:  python indexnow.py
"""
import json
import re
import urllib.request
from pathlib import Path

import build

ROOT = Path(__file__).parent
urls = re.findall(r"<loc>([^<]+)</loc>", (ROOT / "site" / "sitemap.xml").read_text(encoding="utf-8"))
host = build.DOMAIN.split("//", 1)[1]
body = {"host": host, "key": build.INDEXNOW_KEY, "keyLocation": f"{build.DOMAIN}/{build.INDEXNOW_KEY}.txt", "urlList": urls}
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=json.dumps(body).encode(),
                             headers={"Content-Type": "application/json; charset=utf-8"})
with urllib.request.urlopen(req, timeout=30) as r:
    print(r.status, len(urls), "URLs submitted")
