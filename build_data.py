"""Builds data.json for the Full Zip gallery.

Every value was read from the vendor's own product page (or the listing retailer's page) on CHECKED.
Anything the page did not state is left as None and shown as "not listed" on the site.
"""
import json

CHECKED = "2026-10-31"

H = []


def add(vendor, world, maker, product, url, price=None, currency="USD", price_note="", material=None, weight=None,
        weight_note="", fit=None, zipstyle="Zip-up", hood=None, pockets=None, sizes=None, made_in=None, notes="",
        source="vendor"):
    H.append(dict(vendor=vendor, world=world, maker=maker, product=product, url=url, price=price, currency=currency,
                  price_note=price_note, material=material, weight_oz=weight, weight_note=weight_note, fit=fit,
                  zip=zipstyle, hood=hood, pockets=pockets, sizes=sizes, made_in=made_in, notes=notes, source=source))


add("Ruby Coffee Roasters", "Coffee", "Roaster", "Burlap Bag Zip-Up Hoodie",
    "https://rubycoffeeroasters.com/products/burlap-bag-zip-up-hoodie", 50,
    material="52% cotton / 48% polyester", fit="Unisex, pre-shrunk", hood="Yes", pockets="Yes",
    sizes="S-2XL", made_in="Assembled in Nicaragua",
    notes="Inspired by coffee cherries and green-coffee burlap bags. Designed by K North Studios, printed by Ambient Inks.")
add("Heartbeat Hot Sauce Co.", "Hot sauce", "Hot sauce maker", "Poirier's Arch Hoodie",
    "https://www.heartbeathotsauce.com/collections/merchandise/products/poiriers-louisiana-style-arch-t-shirt", 60,
    currency="CAD", price_note="Canadian store", material="ATC Everyday Fleece (blend not listed)", sizes="S-2XL",
    notes="Screen printed on a zip-up fleece hoodie.")
add("Forty Weight Coffee Roasters", "Coffee", "Roaster", "Dark Blue Zip Hoodie",
    "https://www.fortyweightcoffee.com/apparel/dark-blue-zip-hoodie", 43,
    notes="Made on an Alternative Apparel blank. Artwork by Jeremiah Wolfe Clifford of Working Class Tattoo.")
add("Chud's BBQ", "BBQ", "Pit builder", "Welder Zip-Up Hoodie",
    "https://www.chudsbbq.com/products/pitmaster-zip-up-hoodie", 39.99, material="80% cotton / 20% polyester",
    sizes="S-4XL", notes="Merch from a bearded pit builder; warm zip-up with a hood.")
add("Mishimoto", "Auto parts", "Cooling and performance parts", "Embroidered Full-Zip Hoodie",
    "https://www.mishimoto.com/embroidered-full-zip-hoodie.html", 74.95,
    material="80% cotton / 20% polyester fleece blend, 100% cotton face", weight=7.4, weight_note="7.4 oz as listed",
    fit="Side-seamed", zipstyle="Full-zip", hood="Sueded jersey-lined, adjustable drawcord",
    pockets="Kangaroo pouch", made_in="Designed, printed and embroidered in the USA",
    notes="Embroidered M logo on the chest, silkscreen logo down the arm. 1x1 ribbed cuffs and waistband.")
add("Leatherman", "Tools & knives", "Multi-tool maker", "Vintage Zip Hoodie",
    "https://www.leatherman.com/products/vintage-zip-hoodie", 60,
    material="70% cotton / 30% polyester, 100% cotton face", fit="Oversized, unisex", zipstyle="Full-zip",
    hood="Yes", sizes="S-2XL", notes="Throwback logo styling.")
add("Zero Tolerance Knives", "Tools & knives", "Knife maker", "Zip-Up Hoodie, Gray",
    "https://mygoodknife.com/en/shop/t-shirt-zero-tolerance-zip-up-hoodie-gray-zt18xl-/", 35.16, currency="EUR",
    price_note="Price from the European retailer MyGoodKnife", material="Cotton / polyester (blend not listed)",
    zipstyle="Zipper on the front", hood="Nylon hood cord", pockets="Two hand pockets", source="retailer",
    notes="ZT logo on the front. ZT is a division of Kai USA.")
add("Technoblade (Mr. Technodad)", "Creators", "YouTuber merch", "One Of Us Zip Up Hoodie (Black)",
    "https://technoblade.com/products/one-of-us-zip-up-hoodie-black", 64, material="80% cotton / 20% polyester",
    hood="Jersey-lined", pockets="Split pouch pocket", sizes="S-3XL",
    notes="Embroidered and screen-printed left chest, printed right sleeve, custom woven hem tag.")
add("Stone Creek Coffee", "Coffee", "Roaster", "Coffee Line Zip-Up Hoodie",
    "https://www.stonecreekcoffee.com/products/coffee-line-zip-up-hoodie", 35, price_note="From $35 (first listed size)",
    material="60% recycled cotton / 40% post-consumer recycled polyester (District Re-Fleece)",
    fit="Unisex, side-seamed", zipstyle="Full-zip (metal YKK)", hood="Recycled natural-color drawcords",
    pockets="2x1 rib-knit pocket opening", sizes="XS-3XL", made_in="Made in India, printed in Milwaukee, WI",
    notes="Artwork from the roaster's coffee labels (Voyager, Ring of Fire, Green Dragon and others). Certified B Corp.")
add("Equator Coffees", "Coffee", "Roaster", "Equator in Motion Zip Hoodie",
    "https://www.equatorcoffees.com/collections/apparel/products/equator-in-motion-zip-hoodie", 55, sizes="XS-2XL",
    notes="Collaboration with Marin County brand Katemi; back print.")
add("ECM", "Coffee", "Espresso machine maker", "Grey Logo Zip-Up Hoodie",
    "https://www.wholelattelove.com/products/ecm-grey-logo-zip-up-hoodie", 80, source="retailer",
    price_note="Sold by Whole Latte Love", notes="Grey, ECM logo on the left chest.")
add("Boston Dynamics", "Tech", "Robotics company", "Robot Full Zip Hoodie",
    "https://shop.bostondynamics.com/products/robot-full-zip-hoodie",
    material="50% cotton (up to 7.7% reclaimed) / 50% polyester, Champion brand", weight=9, weight_note="9 oz as listed",
    zipstyle="Full zip", hood="Two-ply, dyed-to-match drawcord", pockets="Front pouch pocket", sizes="S-3XL",
    notes="Rib-knit waistband and cuffs, coverstitching throughout, set-in sleeves. Price not shown on the page I read.")
add("Chainlink", "Tech", "Blockchain oracle network", "Perfect Weight Full-Zip Hoodie",
    "https://shop.chain.link/shop/35937-75854-district-perfect-weight-full-zip-hoodie",
    material="Cotton fleece (District Perfect Weight; blend not listed)", weight=8.26,
    weight_note="8.26 oz as listed", zipstyle="Full-zip",
    hood="Jersey-lined, dyed-to-match drawcords with metal tips",
    notes="Swag store. The price on the page is unclear, so check the store.")
add("Museum of Science, Boston", "Museums", "Science museum", "Dino Zip-Up Hooded Sweatshirt",
    "https://shop.mos.org/products/museum-of-science-dino-zip-up-hooded-sweatshirt", 75, material="100% cotton",
    fit="Adult, unisex", sizes="S-3XL", notes="Illustrated dinosaur embellishments, color Deep dive.")
add("American Museum of Natural History", "Museums", "Natural history museum",
    "Eco-Friendly Adult Deep Blue Elephant Zip Hoodie",
    "https://shop.amnh.org/products/eco-friendly-adult-deep-blue-amnh-ny-elephant-zip-hoodie", 70,
    material="100% cotton, fair-labor certified", hood="Drawstring", pockets="Front pockets", sizes="S-2XL",
    notes="Museum logo and elephant silhouettes on the front, 'New York' lettering on one sleeve.")
add("Natural History Museum of Los Angeles", "Museums", "Natural history museum", "Zip-Up Hooded Sweatshirt",
    "https://shop.nhm.org/products/natural-history-museum-zip-up-hooded-sweatshirt", 64, sizes="S-3XL",
    notes="Dinosaurs on the front, footprints down the sleeve.")
add("Skulls Unlimited", "Museums", "Osteology museum and supplier", "Museum of Osteology 'Keeper of Curiosity' Zip Hoodie",
    "https://www.skullsunlimited.com/products/museum-of-osteology-keeper-of-curiosity-zip-hoodie", 59.99,
    fit="Unisex sizing", sizes="S-3XL", notes="Black, museum logo on the front, American-traditional Sir Indiana Bones on the back.")
add("Museum of Peace & Quiet", "Museums", "Art space and shop", "Museum Zip-Up Hoodie, Black",
    "https://feature.com/products/museum-of-peace-and-quiet-museum-zip-up-hoodie-black", 96, material="100% cotton",
    zipstyle="Full zipper", hood="Hooded neckline, ribbed trims", pockets="Front pockets", sizes="SM-XL",
    made_in="Made in USA", source="retailer", price_note="Sold by Feature", notes="Embroidered 'Museum' graphics on the front.")
add("The Broad", "Museums", "Contemporary art museum", "Celebration Zip Hoodie",
    "https://shop.thebroad.org/products/celebration-zip-hoodie", 96, material="100% combed cotton", sizes="S-2XL",
    made_in="Imported", notes="Supervsn x The Broad Juneteenth collaboration; architectural graphic across the back.")
add("Aquarium Co-Op", "Aquariums", "Aquarium supply store", "Classic Mbu Puffer Hoodie",
    "https://www.aquariumcoop.com/products/classic-mbu-puffer-hoodie", 39.99, material="50% cotton / 50% polyester fleece",
    zipstyle="Zip-up (sturdy metal zipper)", hood="Black drawcord", pockets="Two front pockets", sizes="S-5XL",
    notes="Mbu puffer on the back with 'Edmonds, Washington'; logo on the left chest.")
add("Society for Scholarly Publishing", "Science & learning", "Professional society",
    "It's a Good Day to Do Science Full-Zip Hoodie", "https://ssp.org/product/its-a-good-day-to-do-science-full-zip-hoodie/",
    42.95, material="50% cotton / 50% polyester, medium-heavy fleece", weight=8, weight_note="8 oz/yd2 as listed",
    fit="Tubular, seam-free body", zipstyle="Full metal zipper", hood="Adjustable, self-colored drawstring",
    pockets="Spacious front pockets", notes="Care: machine wash warm, tumble dry medium.")
add("Drennan", "Fishing", "Tackle brand", "Full Zip Hoody",
    "https://www.anglingdirect.co.uk/drennan-full-zip-hoody", currency="GBP", price_note="Sold by Angling Direct (UK)",
    material="Anti-pill fabric", zipstyle="Full zip (YKK)", hood="Blue-lined, drawstrings",
    pockets="Hand-warmer pouch pocket", sizes="M-XXL", source="retailer",
    notes="Navy and aqua. Cuffed wrists to keep wind out.")
add("Drennan", "Fishing", "Tackle brand", "Specialist Zipped Hoodie",
    "https://www.anglingdirect.co.uk/drennan-specialist-zipped-hoodie", currency="GBP", price_note="Sold by Angling Direct (UK)",
    zipstyle="Full zip", source="retailer", notes="In Drennan's Specialist green. Price and fabric not captured.")
add("Black Diamond", "Outdoor gear", "Climbing and ski gear maker", "Stacked Full-Zip Hoodie",
    "https://www.absolute-snow.co.uk/black-diamond-stacked-mens-full-zip-hoodie", 31.45, currency="GBP",
    price_note="Sold by Absolute Snow (UK); sale price", material="97% organic cotton / 3% elastane",
    weight_note="290 gsm as listed; garment 542 g", fit="Regular", zipstyle="Full zip", hood="Drawstring", source="retailer",
    notes="All-purpose layer for the mountain, overnights or travel.")
add("Railroad City (Pennsylvania Railroad K4 1361)", "Railroads", "Heritage railroad museum shop",
    "K4 1361 Core Fleece Full-Zip Sweatshirt", "https://shop.railroadcity.org/products/1361-Full-Zip-Sweatshirt-p794663076",
    39.99, material="Mid-weight heather-gray fleece (blend not listed)", zipstyle="Full-zip",
    notes="Steam locomotive branding on the left chest.")
add("Railroaders Memorial Museum", "Railroads", "Heritage railroad museum", "Core Fleece Full-Zip Sweatshirt (Embroidered)",
    "https://shop.railroadcity.org/products/RMM-Full-Zip-Sweatshirt-p794663079", 44.99,
    material="Mid-weight fleece (blend not listed)", zipstyle="Full-zip",
    notes="Embroidered PRR keystone logo on the left chest.")

import os
IMAGES = json.load(open("images.json")) if os.path.exists("images.json") else {}

from urllib.parse import urlparse

for i, h in enumerate(H, 1):
    h["image"] = IMAGES.get(str(i))
    h["_handle"] = urlparse(h["url"]).path.rstrip("/").split("/")[-1]
    h["_domain"] = ".".join(urlparse(h["url"]).netloc.split(".")[-2:])

if os.path.exists("harvested.json"):
    have = {(h["_domain"], h["_handle"]) for h in H}
    for h in json.load(open("harvested.json", encoding="utf-8")):
        if (h["domain"], h["handle"]) in have:
            continue
        have.add((h["domain"], h["handle"]))
        h["_handle"], h["_domain"] = h.pop("handle"), h.pop("domain")
        H.append(h)

import re


def short_sizes(s):
    if not s:
        return s
    t = s
    for a, b in [(r"triple extra[- ]large|xxx[- ]large|3x[- ]large", "3XL"), (r"double extra[- ]large|xx[- ]large|2x[- ]large", "2XL"),
                 (r"extra[- ]small|x[- ]small", "XS"), (r"extra[- ]large|x[- ]large", "XL"), (r"small", "S"), (r"medium", "M"), (r"large", "L")]:
        t = re.sub(a, b, t, flags=re.I)
    return t.upper().replace(" ", "")


WORLD_FIX = {"Outdoor gear": "Outdoors", "Aquariums": "Nature", "Science & learning": "Media", "Space": "Tech",
             "Hot sauce": "Food & drink", "BBQ": "Food & drink", "Spirits": "Beer & spirits", "Beer": "Beer & spirits",
             "Aviation": "Outdoors", "Creators": "Media"}
for i, h in enumerate(H, 1):
    h["id"] = i
    h["checked"] = CHECKED
    h["world"] = WORLD_FIX.get(h["world"], h["world"])
    if h.get("sizes") and len(h["sizes"]) > 9:
        h["sizes"] = short_sizes(h["sizes"])
    if h.get("sizes"):
        h["sizes"] = (h["sizes"].replace("X-Sl", "XS").replace("X-S", "XS").replace("3XLG", "3XL").replace("XLG", "XL")
                      .replace("XXXL", "3XL").replace("XXL", "2XL"))
        if h["sizes"].endswith("X"):
            h["sizes"] += "L"
        if h["sizes"] == "S-1":
            h["sizes"] = None
    h.pop("_handle", None); h.pop("_domain", None)

json.dump(H, open("data.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(len(H), "hoodies;", sum(1 for h in H if h["material"]), "list a material;", sum(1 for h in H if h["price"]), "list a price")
