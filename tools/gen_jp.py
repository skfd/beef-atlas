# -*- coding: utf-8 -*-
"""Build data/cuts_jp.json (Japanese / JMGA + yakiniku scheme) and sanity-check it."""
import json, itertools, io, os

data = {
  "culture": "Japan",
  "id": "jp",
  "flag": "JP",
  "blurb": "Japan breaks the carcass into thirteen wholesale 部分肉, eleven of which are the names allowed on a retail label, but what actually drives price is 霜降り — the intramuscular fat, or sashi, scored by the Japan Meat Grading Association as a yield grade A–C plus a meat-quality grade 1–5, so that A5 is the top box. Because the best beef is intensely fatty, cuts are trimmed and sized to be sliced paper-thin for sukiyaki and shabu-shabu or into bite squares for yakiniku, rather than into thick Western steaks. At the table nobody orders “chuck”: the working vocabulary is the yakiniku subcut names — karubi, harami, misuji, zabuton, ichibo — many of them 希少部位, rare cuts yielding only two or three kilos per animal.",
  "sources": [
    "https://ja.wikipedia.org/wiki/%E7%89%9B%E8%82%89",
    "https://ja.wikipedia.org/wiki/%E3%83%8F%E3%83%A9%E3%83%9F",
    "https://www.piif.jmtc.or.jp/ushibui/",
    "https://niku-miyabi.com/news/beef-part/",
    "https://oumiushi.com/about/japanese_beef",
    "https://niku-love.jp/beef-part/",
    "https://iso-labo.com/labo/beaf_parts.html",
    "https://js-dining.jp/column/yakiniku-bui-ichiran/"
  ],
  "cuts": []
}

C = data["cuts"]


def cut(i, name, native, rom, region, x, z, fw, desc, dishes):
    C.append({"id": i, "name": name, "native": native, "romanized": rom,
              "region": region, "x": x, "z": z, "full_width": fw,
              "description": desc, "dishes": dishes})


cut("neck", "Neck", "ネック", "nekku",
    "The neck, from the poll at x 0.80 forward-back to the point of shoulder at x 0.72, high on the topline.",
    [0.72, 0.82], [0.74, 0.94], True,
    "One of the thirteen official 部分肉 and the hardest-working muscle on the animal, so it is coarse-grained, almost free of sashi and firm, but very rich in collagen and beefy flavour. It is almost never sold as a steak cut — it goes to mince, stock and long-simmered dishes.",
    ["nikomi (stew)", "curry", "hamburg", "soup stock"])

cut("kata", "Chuck / shoulder clod (arm)", "カタ", "kata",
    "The shoulder clod and arm — the foreleg above the knee, from just ahead of the elbow at x 0.66 back to the point of shoulder at x 0.74, z 0.28 up to 0.54.",
    [0.66, 0.74], [0.28, 0.54], False,
    "The 部分肉 called カタ (also ウデ, arm) is a bundle of well-exercised muscles: lean, slightly tough, modestly marbled but loaded with gelatin and umami, and it carries the front shank below it. Sold thin-sliced for sukiyaki and as budget yakiniku, or cubed for stews; the rare cuts ミスジ, トウガラシ and クリミ are carved out of it.",
    ["nikomi (stew)", "sukiyaki", "yakiniku", "soup stock"])

cut("misuji", "Top blade / flat iron", "ミスジ", "misuji",
    "On the outside of the shoulder blade, under the scapula behind the point of shoulder, z 0.54–0.66.",
    [0.66, 0.74], [0.54, 0.66], False,
    "A 希少部位 from the カタ primal that lies flat against the shoulder blade and barely moves, so despite being shoulder meat it is tender and threaded with fine even sashi around the central sinew that gives it its name (three sinews). Only 2–3 kg per animal; grilled briefly over charcoal or served as rare-seared slices.",
    ["yakiniku", "steak", "tataki"])

cut("tougarashi", "Chuck tender / shoulder petite tender", "トウガラシ", "tougarashi",
    "In front of the shoulder blade at the point of shoulder, x 0.70–0.77, just below the neck line at z 0.66–0.74.",
    [0.70, 0.77], [0.66, 0.74], False,
    "Named for its chili-pepper shape, this cone of lean muscle sits on the front face of the scapula inside the カタ primal; it has very little sashi and a clean red-meat flavour with a slight chew. Prized as a lean yakiniku cut and for roast beef, and one of the 希少部位 sold only by specialist shops.",
    ["yakiniku", "roast beef", "steak"])

cut("kata-rosu", "Chuck roll / chuck eye", "カタロース", "kata-rosu",
    "The upper back over the shoulder, from the fifth-rib line at x 0.58 forward to the neck at x 0.72, along the topline z 0.74–0.92.",
    [0.58, 0.72], [0.74, 0.92], True,
    "An official 部分肉 that continues the loin muscle forward over the shoulder: fine-grained, generously marbled and full-flavoured, though with more connective tissue running through it than the rib loin. It is the classic sukiyaki and shabu-shabu cut because it slices thin beautifully and costs less than サーロイン.",
    ["sukiyaki", "shabu-shabu", "yakiniku", "steak"])

cut("zabuton", "Chuck flap / Denver steak", "ザブトン", "zabuton",
    "The rib-side underside of the chuck roll, hanging below the topline at z 0.66–0.74 between x 0.57 and 0.64.",
    [0.57, 0.64], [0.66, 0.74], False,
    "Also called ハネシタ (under the wing), this square slab — hence cushion — is cut from the rib end of the カタロース and is among the most heavily marbled muscles on the animal, only 4–5 kg per head. Grilled for seconds a side at the yakiniku table so the sashi just melts.",
    ["yakiniku", "sukiyaki", "shabu-shabu"])

cut("rib-rosu", "Rib loin / ribeye", "リブロース", "ribu-rosu",
    "The back between the fifth rib at x 0.57 and the last rib at x 0.46, from just under the spine at z 0.72 to the topline at z 0.92.",
    [0.46, 0.57], [0.72, 0.92], True,
    "One of the three premium 部分肉 and the part of the loin that marbles most readily, with the finest grain and the deepest fat flavour; the eye is ringed by the リブキャップ and マキ. Cut thick for steak, or shaved for the most luxurious sukiyaki and shabu-shabu.",
    ["steak", "sukiyaki", "shabu-shabu", "roast beef", "yakiniku"])

cut("sirloin", "Sirloin (short loin and sirloin)", "サーロイン", "saroin",
    "The back from the last rib at x 0.46 rearward to the hip at x 0.30, along the topline z 0.76–0.92.",
    [0.30, 0.46], [0.76, 0.92], True,
    "The Japanese サーロイン covers what Anglo butchery splits into short loin and sirloin, and is regarded as the finest-textured, sweetest meat on the carcass; the muscle does almost no work, so heavy sashi sits in a fine even web. The one cut Japan does treat as a thick steak, though it is shaved for sukiyaki just as often.",
    ["steak", "sukiyaki", "shabu-shabu", "roast beef"])

cut("hire", "Fillet / tenderloin", "ヒレ", "hire",
    "Inside the body under the lumbar spine, running from the hip at about x 0.26 forward toward the last rib, z 0.64–0.76.",
    [0.26, 0.40], [0.64, 0.76], True,
    "A 部分肉 that hangs beneath the backbone and bears no load at all, making it the most tender and the leanest of the prime cuts — only about 3% of the carcass, with the thick middle sold as シャトーブリアン. Cooked fast and rare as steak or crumbed as ヒレカツ; too lean for long heat.",
    ["steak", "chateaubriand", "katsu", "roast beef"])

cut("katabara", "Brisket / chuck rib (front plate)", "カタバラ", "katabara",
    "The front of the belly and chest, from the fifth-rib line at x 0.56 forward to the brisket behind the elbow at x 0.66, z 0.44–0.66.",
    [0.56, 0.66], [0.44, 0.66], True,
    "The forward half of the ばら, layered red meat and fat over the first six ribs, coarse-grained and rich; the ブリスケ and the famously fatty 三角バラ, sold as 特上カルビ, both come from here. Simmered for nikujaga and curry, or cut into premium kalbi squares.",
    ["yakiniku", "nikujaga", "curry", "nikomi (stew)"])

cut("karubi", "Short rib (kalbi)", "カルビ", "karubi",
    "The rib-cage section of the belly, x 0.44–0.56 between the last rib and the mid ribs, z 0.44–0.58.",
    [0.44, 0.56], [0.44, 0.58], True,
    "Not a butchery term but the yakiniku word, from Korean galbi (rib), for the fatty meat on and between the rib bones of the ばら primal: sweet, juicy and streaked with fat. The default order at any yakiniku restaurant, grilled in bite-sized squares; the strip prised from between the bones is 中落ちカルビ.",
    ["yakiniku", "kalbi", "sukiyaki"])

cut("tomobara", "Short plate / flank", "トモバラ", "tomobara",
    "The rear belly hanging below the barrel, x 0.32–0.44, from the belly line z 0.56 down to 0.44.",
    [0.32, 0.44], [0.44, 0.56], True,
    "The rear half of the ばら and an official 部分肉: thick alternating bands of lean and fat, coarse-grained but among the richest-tasting meat on the animal, and the source of ゲタ, ササニク and カイノミ. Thin-sliced for gyudon and nikomi, or grilled as kalbi.",
    ["yakiniku", "gyudon", "nikomi (stew)", "shabu-shabu"])

cut("kainomi", "Inside skirt / flap meat", "カイノミ", "kainomi",
    "The top rear corner of the short plate where it meets the flank and the tail of the fillet, x 0.32–0.40, z 0.56–0.64.",
    [0.32, 0.40], [0.56, 0.64], False,
    "A shellfish-shaped 希少部位 taken from the part of the トモバラ closest to the ヒレ, so it has the firm sweetness of red meat together with belly-cut marbling — about 2–3 kg per animal. Grilled quickly at the yakiniku table and priced as a premium cut.",
    ["yakiniku", "steak"])

cut("harami", "Skirt steak (diaphragm, rib side)", "ハラミ", "harami",
    "The rib-side sheet of the diaphragm, arching inside the body wall at the last ribs, x 0.44–0.56, z 0.58–0.72.",
    [0.44, 0.56], [0.58, 0.72], True,
    "Anatomically the diaphragm, so Japan classifies it as 内臓肉 (offal) even though it looks and eats like red meat — soft, juicy, coarse-fibred and leaner than kalbi. After karubi it is the most ordered thing at a yakiniku shop, and it anchors the harami teishoku.",
    ["yakiniku", "harami teishoku", "horumon"])

cut("sagari", "Hanging tender", "サガリ", "sagari",
    "The pillar of the diaphragm nearer the lumbar vertebrae, hanging inside the body cavity ahead of the kidneys at x 0.40–0.44, z 0.62–0.74.",
    [0.40, 0.44], [0.62, 0.74], True,
    "The crus of the diaphragm — the same organ as ハラミ but the small thick piece that hangs (下がる) from the spine, only a couple of kilos per animal and likewise sold as 内臓肉. Deeper-flavoured and slightly chewier than harami; a Kansai and Kyushu yakiniku favourite, and often lumped in with harami.",
    ["yakiniku", "horumon"])

cut("ranpu", "Rump", "ランプ", "ranpu",
    "The top of the hindquarter above the hip joint, behind the sirloin line, x 0.16–0.26, z 0.68–0.90.",
    [0.16, 0.26], [0.68, 0.90], False,
    "The upper part of the ランイチ 部分肉 (ランプ plus イチボ), sitting where the loin runs out over the hip: fine-grained, tender lean meat with a light even sashi and a concentrated beef flavour for a hindquarter cut. Served as steak, as thin yakiniku slices and in sukiyaki.",
    ["steak", "yakiniku", "sukiyaki", "roast beef"])

cut("ichibo", "Rump cap / picanha", "イチボ", "ichibo",
    "The rear cap of the rump over the aitch bone at the pin bone, x 0.04–0.16, z 0.62–0.86.",
    [0.04, 0.16], [0.62, 0.86], False,
    "The lower, rearmost muscle of the ランイチ, named after the H-shaped hip bone (H-bone) it caps; lean but carrying a fat cap and fine marbling, tender at the tail end and firmer toward the leg. Grilled as thick yakiniku slices or roasted whole.",
    ["yakiniku", "steak", "roast beef"])

cut("uchimomo", "Inside round / topside", "ウチモモ", "uchimomo",
    "The inner face of the hind leg, x 0.12–0.24 between the shank and the knuckle, z 0.26–0.62.",
    [0.12, 0.24], [0.26, 0.62], False,
    "An official 部分肉 and the single leanest large muscle on the carcass — a big uniform block of red meat, slightly coarse, with almost no sashi. Sliced thin for sukiyaki and shabu-shabu, roasted as roast beef, or served on lean yakiniku plates.",
    ["roast beef", "sukiyaki", "shabu-shabu", "steak"])

cut("sotomomo", "Outside round / silverside", "ソトモモ", "sotomomo",
    "The outer and rearmost face of the hind leg, x 0.00–0.12, z 0.24–0.62.",
    [0.00, 0.12], [0.24, 0.62], False,
    "The hardest-working muscles of the もも, so the grain is coarse, sinew runs through it and it is firm and very lean; it contains ハバキ and カメノコ. Best braised, stir-fried in thin strips or cured — rarely grilled as a steak.",
    ["nikomi (stew)", "stir-fry", "roast beef", "corned beef"])

cut("shintama", "Knuckle / thick flank", "シンタマ", "shintama",
    "The ball of muscle in front of the femur below the hip, x 0.24–0.32, z 0.44–0.62.",
    [0.24, 0.32], [0.44, 0.62], False,
    "A round 部分肉 of four muscles wrapped around the head of the femur — fine-grained, tender and lean for leg meat, and the source of the rare トモサンカク (ヒウチ) and シンシン. Used for roast beef, cutlets and lean yakiniku.",
    ["roast beef", "katsu", "yakiniku", "shabu-shabu"])

cut("shinshin", "Knuckle centre / centre of the ball tip", "シンシン", "shinshin",
    "The core of the knuckle, low on the front of the hind leg at x 0.24–0.32, z 0.30–0.44.",
    [0.24, 0.32], [0.30, 0.44], False,
    "Literally the core of the シンタマ, this 希少部位 is a small very fine-grained lean muscle with a faint even sashi — firm at first bite but silky once cooked, and only a few hundred grams per animal. Served as rare-seared yakiniku, roast beef or thin steak.",
    ["yakiniku", "roast beef", "steak", "tataki"])

cut("sune", "Shank / shin", "スネ", "sune",
    "The hind leg below the stifle, from the hock up to about z 0.24 at x 0.03–0.18; the foreleg equivalent (front shank) sits under the カタ.",
    [0.03, 0.18], [0.02, 0.24], False,
    "The official 部分肉 ともずね: almost fat-free, shot through with sinew and the toughest meat on the animal, but packed with gelatin and the most concentrated beef flavour. Long-simmered until the connective tissue melts, or trimmed into 牛すじ for oden and dote-yaki.",
    ["nikomi (stew)", "curry", "oden", "gyusuji"])

cut("tan", "Tongue", "タン", "tan",
    "The tongue, inside the head forward of the poll at x 0.84–0.96, z 0.74–0.84.",
    [0.84, 0.96], [0.74, 0.84], True,
    "Sold as 内臓肉 and graded along its length — タン元 at the root fatty and tender, タン中 balanced, タン先 at the tip lean and firm — with a springy crisp bite unlike any muscle cut. Thin-sliced 塩タン with lemon opens most yakiniku meals; the root end is stewed as tan shichu, a Sendai speciality.",
    ["yakiniku", "shio-tan", "tan shichu (stew)"])

cut("teru", "Oxtail", "テール", "teru",
    "The tail, from its base at the top of the rump, x 0.00–0.04, z 0.80–0.92.",
    [0.00, 0.04], [0.80, 0.92], True,
    "About 2 kg per animal of bony, sinewy, heavily gelatinous meat that is close to inedible without long cooking. Simmered for hours into テールスープ, a staple closing dish at yakiniku restaurants, or braised until the meat drops off the vertebrae.",
    ["tail soup", "nikomi (stew)", "yakiniku"])


def overlap(a, b):
    ox = min(a["x"][1], b["x"][1]) - max(a["x"][0], b["x"][0])
    oz = min(a["z"][1], b["z"][1]) - max(a["z"][0], b["z"][0])
    return ox > 1e-9 and oz > 1e-9


bad = [(a["id"], b["id"]) for a, b in itertools.combinations(C, 2) if overlap(a, b)]
print("cuts:", len(C))
print("overlapping pairs:", bad)
ids = [c["id"] for c in C]
assert len(set(ids)) == len(ids), "duplicate ids"

cov = sorted([list(c["x"]) for c in C])
merged = []
for s, e in cov:
    if merged and s <= merged[-1][1] + 1e-9:
        merged[-1][1] = max(merged[-1][1], e)
    else:
        merged.append([s, e])
print("x coverage:", merged)

out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "cuts_jp.json")
with io.open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", out)
