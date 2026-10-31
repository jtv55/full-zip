"""Outside check: every material/weight/zip claim in data.json must appear in the live product page.

Fetches each page and confirms the fiber percentages, oz/gsm weight and zip wording are literally on it.
Prints any mismatch. Run: python verify.py
"""
import json, re, sys
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding="utf-8")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
data = json.load(open("data.json", encoding="utf-8"))


def check(h):
    try:
        r = requests.get(h["url"], headers={"User-Agent": UA}, timeout=15)
    except Exception as e:
        return h["id"], h["product"], ["unreachable"]
    if r.status_code != 200:
        return h["id"], h["product"], [f"http {r.status_code}"]
    html = r.text
    text = " ".join(BeautifulSoup(html, "html.parser").get_text(" ", strip=True).split()).lower()
    text += " " + html.lower()
    probs = []
    if h.get("material"):
        for pct, fib in re.findall(r"(\d+)%\s*(?:[a-z\-]+ )?(cotton|polyester|nylon|spandex|elastane|wool|rayon|viscose|acrylic|hemp|merino)", h["material"].lower()):
            if not re.search(rf"{pct}\s?(?:%|percent)[^<>]{{0,40}}{fib[:4]}", text) and not re.search(rf"{pct}\s?(?:%|percent)-?\s?{fib[:4]}", text):
                probs.append(f"material {pct}% {fib} not found")
    m = re.search(r"([\d.]+) (?:oz|gsm)", h.get("weight_note") or "")
    if m and m.group(1) not in text:
        probs.append(f"weight {m.group(1)} not found")
    if not re.search(r"zip", text):
        probs.append("no 'zip' on page")
    return h["id"], h["product"], probs


with ThreadPoolExecutor(8) as ex:
    res = list(ex.map(check, data))
bad = [r for r in res if r[2]]
for i, p, probs in bad:
    print(i, p[:50], "->", "; ".join(probs))
print(f"{len(data) - len(bad)} of {len(data)} pass")
