"""Filters the raw store-catalog harvest down to hoodies that belong on the site.

Reads harvest.json (written by the discovery script), drops clothing-brand and
retailer-resold items, dedupes, and writes harvested.json for build_data.py.
"""
import json, re, sys
from urllib.parse import urlparse

SRC = sys.argv[1]
DROP_VENDORS = {"Milwaukee Tool", "RevZilla", "Biketart", "Black Diamond"}
DROP_TITLE = re.compile(r"Alpinestars|Dainese|Troy Lee|Fox Head|Since 74", re.I)
RETAILERS = {"Pilot Mall", "Aspen Ski and Board", "J&P Cycles"}

raw = json.load(open(SRC, encoding="utf-8"))
out, seen = [], set()
for r in raw:
    for h in r["found"]:
        if h["vendor"] in DROP_VENDORS or DROP_TITLE.search(h["product"]):
            continue
        if h["price"] is None:
            continue
        key = (h["vendor"], re.sub(r"\W+", "", h["product"].lower()))
        handle = urlparse(h["url"]).path.rstrip("/").split("/")[-1]
        if key in seen:
            continue
        seen.add(key)
        h = {k: v for k, v in h.items() if not k.startswith("_") and k != "full_zip_in_text"}
        h["handle"] = handle
        h["domain"] = ".".join(urlparse(h["url"]).netloc.split(".")[-2:])
        if h["vendor"] in RETAILERS:
            h["source"] = "retailer"
            h["price_note"] = (h["price_note"] + " " if h["price_note"] else "") + "Sold by " + h["vendor"]
        out.append(h)
json.dump(out, open("harvested.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(len(out), "kept of", sum(len(r["found"]) for r in raw))
