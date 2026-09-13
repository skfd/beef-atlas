# -*- coding: utf-8 -*-
"""Generate data/cuts_fr.json — the French decoupe scheme — and validate it."""
import json, io, itertools

C = []


def cut(cid, name, native, region, x, z, fw, desc, dishes):
    C.append({"id": cid, "name": name, "native": native, "region": region,
              "x": x, "z": z, "full_width": fw, "description": desc, "dishes": dishes})


# ---- hindquarter: top slab ----
cut("queue", "Oxtail", "Queue",
    "Tail base, on the midline just behind and above the rump at x 0.00-0.06, rising from z 0.82 to 0.96.",
    [0.00, 0.06], [0.82, 0.96], False,
    "The tail's own musculature, worked constantly to swat flies and bound up with bone and cartilage. Pure collagen and bone: strictly a bouillir/mijoter cut given a long, gentle simmer until the gelatine dissolves.",
    ["queue de b\u0153uf en hochepot", "pot-au-feu", "daube de queue de b\u0153uf", "parmentier de queue de b\u0153uf"])

cut("rumsteck", "Rump", "Rumsteck",
    "The top slab over the hip and pin bone, x 0.06-0.30, z 0.74-0.92 \u2014 from the tail base forward to just short of the lumbar vertebrae.",
    [0.06, 0.30], [0.74, 0.92], True,
    "A large, lean, close-grained muscle group capping the pelvis, only moderately worked, so it is tender without being soft. A premi\u00e8re cat\u00e9gorie griller/r\u00f4tir cut, taken as thick pav\u00e9s or roasted whole.",
    ["rumsteck grill\u00e9", "brochettes de b\u0153uf", "fondue bourguignonne", "rosbif"])

cut("aiguillette-baronne", "Sirloin tip / tri-tip", "Aiguillette baronne",
    "A long conical piece at the front-lower tip of the rumsteck, between the rump and the noix, x 0.22-0.30, z 0.62-0.74.",
    [0.22, 0.30], [0.62, 0.74], True,
    "A tapering, needle-shaped muscle at the junction of the back and the hind limb, moderately worked and well flavoured, weighing 800 g to 1.2 kg. Versatile: sliced thin to griller, barded and tied to r\u00f4tir, or braised whole in a cocotte.",
    ["aiguillette baronne r\u00f4tie", "b\u0153uf \u00e0 la ficelle", "aiguillette brais\u00e9e aux carottes"])

cut("araignee", "Spider steak", "Araign\u00e9e",
    "A small irregular muscle lining the inside of the hip-joint socket, x 0.14-0.21, z 0.62-0.72 \u2014 directly over the hip joint at x 0.16.",
    [0.14, 0.21], [0.62, 0.72], False,
    "An internal muscle lining the hip socket, barely worked and richly marbled; the veined membrane over it looks like a spider's web, hence the name. Only two per carcass and a famous morceau du boucher \u2014 denerved, then grilled or pan-seared fast and served saignant.",
    ["araign\u00e9e grill\u00e9e", "araign\u00e9e \u00e0 l'\u00e9chalote", "araign\u00e9e po\u00eal\u00e9e au beurre"])

# ---- hind leg / thigh, tiled rear to front ----
cut("rond-de-gite", "Eye of round", "Rond de g\u00eete",
    "The hindmost muscle of the thigh, behind the femur, x 0.00-0.07, z 0.34-0.66.",
    [0.00, 0.07], [0.34, 0.66], True,
    "Also called the semelle ('shoe sole'), a cylindrical, extremely lean and fine-grained muscle at the very back of the leg with almost no fat. Tender enough to eat raw in tartare or carpaccio, but cooked it tightens quickly, so it is otherwise braised or mijot\u00e9.",
    ["carpaccio de b\u0153uf", "tartare", "b\u0153uf mode", "b\u0153uf brais\u00e9"])

cut("gite-a-la-noix", "Silverside", "G\u00eete \u00e0 la noix",
    "The middle-rear of the thigh, x 0.07-0.14, z 0.34-0.64, wrapping the back of the femur ahead of the rond de g\u00eete.",
    [0.07, 0.14], [0.34, 0.64], True,
    "A long muscle of the rear thigh with short fibres and a fine grain, lean and reasonably tender for a leg muscle. Cut into steaks to griller or barded and tied to r\u00f4tir; the firmer end goes to braiser.",
    ["r\u00f4ti de g\u00eete \u00e0 la noix", "b\u0153uf \u00e0 la mode", "steak de g\u00eete", "b\u0153uf brais\u00e9 aux carottes"])

cut("tende-de-tranche", "Topside", "Tende de tranche",
    "The large muscle on the inner face of the thigh, x 0.14-0.21, z 0.38-0.62 \u2014 the medial side of the leg between hock and hip.",
    [0.14, 0.21], [0.38, 0.62], True,
    "The biggest piece of the thigh, on the inner face where the muscles do least work, so the meat is naturally tender and very lean. It hides the two prized morceaux du boucher \u2014 the small round poire (500-600 g) and the long flat merlan (800 g-1 kg) \u2014 and the whole group is griller/r\u00f4tir meat.",
    ["bifteck", "poire et merlan grill\u00e9s", "fondue bourguignonne", "r\u00f4ti de tende de tranche", "escalopes de b\u0153uf"])

cut("tranche-grasse", "Thick flank / knuckle", "Tranche grasse",
    "The front of the thigh over the stifle, x 0.21-0.29, z 0.36-0.60, ahead of the femur.",
    [0.21, 0.29], [0.36, 0.60], True,
    "The quadriceps group at the front of the leg, broken down by the trade into plat de tranche, rond de tranche and mouvant; well used in walking, so firmer and more sinewy than the tende de tranche. Sliced thin it grills, but most of it is braiser/mijoter meat.",
    ["b\u0153uf bourguignon", "paupiettes de b\u0153uf", "bifteck", "daube proven\u00e7ale"])

cut("gite-arriere", "Hind shank", "G\u00eete (jarret arri\u00e8re)",
    "The rear shank below the hock, x 0.03-0.13, z 0.06-0.34; the hock sits at z 0.28.",
    [0.03, 0.13], [0.06, 0.34], True,
    "The lower hind leg \u2014 hard-working muscles laced with tendon and collagen around the shank bone and its marrow. Emphatically a bouillir/mijoter cut: hours of gentle wet heat turn the collagen to gelatine and give the broth its body.",
    ["pot-au-feu", "osso-buco de b\u0153uf", "g\u00eete en gel\u00e9e", "bouillon de b\u0153uf"])

# ---- loin ----
cut("faux-filet", "Sirloin / strip loin", "Faux-filet (contre-filet)",
    "The long back muscle above the lumbar and last thoracic vertebrae, x 0.30-0.46, z 0.80-0.94, between the rumsteck and the ribs.",
    [0.30, 0.46], [0.80, 0.94], True,
    "The longissimus dorsi running along the top of the spine, a postural muscle that is barely worked and carries a firm cap of fat. A premi\u00e8re cat\u00e9gorie griller/r\u00f4tir cut with more chew and more flavour than the filet.",
    ["entrec\u00f4te faux-filet grill\u00e9e", "pav\u00e9 de faux-filet", "rosbif", "contre-filet sauce b\u00e9arnaise"])

cut("filet", "Tenderloin", "Filet",
    "Tucked inside the carcass underneath the lumbar spine, x 0.30-0.46, z 0.70-0.80, directly beneath the faux-filet.",
    [0.30, 0.46], [0.70, 0.80], False,
    "The psoas major, slung under the backbone where it never bears weight, which makes it the most tender and least fatty muscle on the animal. The top of the premi\u00e8re cat\u00e9gorie: grill or roast it quickly, usually barded because it has no fat of its own.",
    ["tournedos Rossini", "filet de b\u0153uf en cro\u00fbte", "chateaubriand", "filet mignon", "b\u0153uf Wellington"])

cut("bavette-d-aloyau", "Flank steak (loin end)", "Bavette d'aloyau",
    "The upper flank flap where the abdominal wall meets the loin, x 0.30-0.40, z 0.56-0.70, just below the filet and behind the last rib.",
    [0.30, 0.40], [0.56, 0.70], False,
    "A flat sheet of abdominal muscle with long, coarse, clearly visible fibres and a deep beefy taste. A deuxi\u00e8me cat\u00e9gorie griller cut treated like a first: seared hard, served saignant and always sliced across the grain.",
    ["bavette \u00e0 l'\u00e9chalote", "bavette grill\u00e9e", "bavette au poivre"])

cut("bavette-de-flanchet", "Flank steak (flank end)", "Bavette de flanchet",
    "The rear-lower flank in front of the thigh, x 0.29-0.36, z 0.44-0.56, below the bavette d'aloyau.",
    [0.29, 0.36], [0.44, 0.56], False,
    "The rearmost part of the abdominal wall, coarser and more sinewy than the bavette d'aloyau and streaked with connective tissue. Cheaper, and a deuxi\u00e8me/troisi\u00e8me cat\u00e9gorie piece: grilled fast if trimmed well, otherwise mijot\u00e9.",
    ["bavette grill\u00e9e", "b\u0153uf en daube", "bavette marin\u00e9e"])

cut("flanchet", "Flank / plate", "Flanchet",
    "The abdominal wall under the loin, x 0.36-0.46, z 0.44-0.56, between the last rib and the hind leg.",
    [0.36, 0.46], [0.44, 0.56], False,
    "Built from the layered muscles of the abdomen alternating with membrane and fat \u2014 it holds the animal's belly up, and is tough and gristly for it. A troisi\u00e8me cat\u00e9gorie bouillir/mijoter cut, usually rolled and tied for the pot.",
    ["pot-au-feu", "flanchet en cocotte", "b\u0153uf gros sel"])

cut("onglet", "Hanger steak", "Onglet",
    "The pillars of the diaphragm hanging under the lumbar spine at the last rib, x 0.40-0.46, z 0.56-0.68.",
    [0.40, 0.46], [0.56, 0.68], False,
    "The crura of the diaphragm, a breathing muscle that works constantly but bears no load, giving long coarse fibres, a central sinew and an almost offal-rich flavour. The archetypal morceau du boucher \u2014 grilled very fast and eaten saignant, never past it.",
    ["onglet \u00e0 l'\u00e9chalote", "onglet grill\u00e9", "onglet sauce au poivre"])

cut("hampe", "Skirt steak", "Hampe",
    "The muscular skirt of the diaphragm along the inside of the lower ribs, x 0.48-0.56, z 0.54-0.64.",
    [0.48, 0.56], [0.54, 0.64], False,
    "The outer fleshy part of the diaphragm separating thorax from abdomen, in long visible bands that give a deliberate resistance to the tooth. Another morceau du boucher: membrane stripped, grilled or pan-seared very hot, served rare.",
    ["hampe grill\u00e9e", "hampe \u00e0 l'\u00e9chalote", "hampe po\u00eal\u00e9e persillade"])

# ---- ribs ----
cut("entrecote", "Rib steak / prime rib", "C\u00f4tes, entrec\u00f4tes",
    "The upper rib cage, x 0.46-0.56, z 0.80-0.94, spanning the ribs between the last rib at x 0.46 and the fifth rib at x 0.56.",
    [0.46, 0.56], [0.80, 0.94], True,
    "The continuation of the long back muscle over the ribs, generously marbled because the muscle does little work and stores fat between its fibres. Premi\u00e8re cat\u00e9gorie griller/r\u00f4tir: on the bone it is a c\u00f4te de b\u0153uf, boned out it is the entrec\u00f4te.",
    ["c\u00f4te de b\u0153uf grill\u00e9e", "entrec\u00f4te marchand de vin", "entrec\u00f4te bordelaise", "entrec\u00f4te frites"])

cut("plat-de-cotes", "Short rib / rib plate", "Plat de c\u00f4tes",
    "The lower half of the rib cage down toward the rib ends, x 0.46-0.56, z 0.64-0.80, beneath the entrec\u00f4te.",
    [0.46, 0.56], [0.64, 0.80], True,
    "The flat muscle and fat lying along the lower rib bones, layered and coarse-grained with plenty of connective tissue. A classic troisi\u00e8me cat\u00e9gorie bouillir cut \u2014 the piece that gives a pot-au-feu its flavour \u2014 sold with or without the bone.",
    ["pot-au-feu", "pot\u00e9e", "b\u0153uf bourguignon", "plat de c\u00f4tes au gros sel"])

cut("basses-cotes", "Chuck rib / blade end", "Basses c\u00f4tes",
    "The first five ribs, high on the back just behind and above the shoulder blade, x 0.56-0.66, z 0.84-0.94.",
    [0.56, 0.66], [0.84, 0.94], True,
    "Where the back muscle runs out over the forward ribs and breaks into several smaller, well-marbled muscles divided by seams of fat. Dual-purpose: in thin steaks it is a griller cut, in chunks it is one of the best mijoter cuts on the animal.",
    ["basses c\u00f4tes grill\u00e9es", "b\u0153uf bourguignon", "carbonade flamande", "daube"])

# ---- belly / brisket ----
cut("tendron", "Rib tips / short plate", "Tendron, milieu de poitrine",
    "The mid-breast over the rib cartilages and sternum, x 0.46-0.58, z 0.44-0.54.",
    [0.46, 0.58], [0.44, 0.54], True,
    "Alternating layers of muscle, fat and the soft cartilage of the rib ends, taken from the floor of the chest. A troisi\u00e8me cat\u00e9gorie mijoter cut whose cartilage melts to gelatine over long cooking; sliced very thin it can also be grilled.",
    ["tendron de b\u0153uf en cocotte", "pot-au-feu", "tendron brais\u00e9", "tendron au barbecue"])

cut("gros-bout-de-poitrine", "Brisket", "Gros bout de poitrine",
    "The front of the breast below and between the forelegs, x 0.58-0.72, z 0.44-0.56, ahead of the elbow at x 0.62.",
    [0.58, 0.72], [0.44, 0.56], True,
    "Three pectoral muscles slung under the shoulder that carry much of the animal's forward weight with no collarbone to help, so they are dense, fatty and full of collagen. A bouillir/mijoter cut, and the traditional piece for salting.",
    ["pot-au-feu", "b\u0153uf gros sel", "poitrine sal\u00e9e", "pot\u00e9e auvergnate"])

# ---- shoulder ----
cut("paleron", "Flat iron / blade", "Paleron",
    "Flat on the outer face of the shoulder blade, upper-rear shoulder near the neck, x 0.56-0.66, z 0.66-0.84.",
    [0.56, 0.66], [0.66, 0.84], True,
    "A flat, regular muscle lying against the scapula, split lengthwise by a tough central sheet of gristle that melts into gelatine. The braiser cut par excellence \u2014 over two hours of wet heat \u2014 though the two half-fillets either side of the nerve also make tender grilling steaks.",
    ["b\u0153uf bourguignon", "carbonade flamande", "daube", "pot-au-feu", "paleron brais\u00e9"])

cut("macreuse-a-bifteck", "Chuck tender / shoulder steak", "Macreuse \u00e0 bifteck",
    "The forward upper shoulder toward the point of shoulder, x 0.66-0.72, z 0.66-0.88.",
    [0.66, 0.72], [0.66, 0.88], True,
    "The upper part of the big shoulder mass on the foreleg, moderately worked, lean and fairly firm but with a fine, even grain. A deuxi\u00e8me cat\u00e9gorie griller cut \u2014 thin steaks, brochettes, or barded and roasted.",
    ["bifteck de macreuse", "brochettes", "macreuse grill\u00e9e", "r\u00f4ti de macreuse"])

cut("jumeau-a-bifteck", "Chuck eye / shoulder twin", "Jumeau \u00e0 bifteck",
    "Below the shoulder blade on the outer shoulder, x 0.56-0.65, z 0.56-0.66.",
    [0.56, 0.65], [0.56, 0.66], True,
    "A long muscle with short fibres lying under the blade, called the 'twin' because it runs alongside its tougher counterpart. The tenderer of the pair and a griller cut: quick steaks or escalopes.",
    ["jumeau grill\u00e9", "escalopes de b\u0153uf", "brochettes", "bifteck sauce \u00e9chalote"])

cut("jumeau-a-pot-au-feu", "Chuck (stewing twin)", "Jumeau \u00e0 pot-au-feu",
    "The deeper, lower half of the twin pair toward the point of shoulder, x 0.65-0.72, z 0.56-0.66.",
    [0.65, 0.72], [0.56, 0.66], True,
    "The firmer twin, heavily worked and shot through with connective tissue, so it turns unctuous and gelatinous once broken down. Strictly mijoter/bouillir: rago\u00fbts, daubes and the pot itself.",
    ["pot-au-feu", "b\u0153uf bourguignon", "daube", "rago\u00fbt de b\u0153uf"])

cut("macreuse-a-pot-au-feu", "Shoulder clod", "Macreuse \u00e0 pot-au-feu",
    "The muscle mass wrapping the humerus on the foreleg above the shank, x 0.58-0.70, z 0.30-0.44.",
    [0.58, 0.70], [0.30, 0.44], True,
    "A big block of muscle on the front limb, worked at every stride and dense with sinew. Firmer than the macreuse \u00e0 bifteck and a troisi\u00e8me cat\u00e9gorie bouillir cut that needs long, slow simmering to turn tender.",
    ["pot-au-feu", "b\u0153uf mode", "rago\u00fbt", "bouillon"])

cut("gite-avant", "Fore shank / shin", "G\u00eete avant (jarret)",
    "The foreleg below the knee, x 0.58-0.70, z 0.06-0.30; the knee sits at z 0.28.",
    [0.58, 0.70], [0.06, 0.30], True,
    "The shin of the front leg: lean muscle bundles wrapped in tendon around a marrow bone, about as hard-working as meat gets. A bouillir cut whose collagen is exactly what a good bouillon or a b\u0153uf en gel\u00e9e needs.",
    ["pot-au-feu", "jarret de b\u0153uf", "b\u0153uf en gel\u00e9e", "bouillon"])

cut("collier", "Neck / chuck", "Collier",
    "The neck, x 0.72-0.80, z 0.62-0.94, from the point of shoulder forward to the poll.",
    [0.72, 0.80], [0.62, 0.94], True,
    "The muscles of the encolure, holding up a very heavy head all day, which makes the meat coarse, gelatinous and deeply flavoured. A troisi\u00e8me cat\u00e9gorie mijoter cut \u2014 cheap, and one of the tastiest things in a long-cooked stew.",
    ["b\u0153uf bourguignon", "daube", "rago\u00fbt", "carbonade flamande", "pot-au-feu"])

cut("joue", "Cheek", "Joue (plat de joue)",
    "The cheek muscle on the side of the head, x 0.80-0.90, z 0.70-0.86, forward of the poll at x 0.80.",
    [0.80, 0.90], [0.70, 0.86], True,
    "The masseter, chewing cud for hours every day, so it is a dense mesh of muscle and collagen with almost no fat. Sold as an abat, it is braised or confit for several hours until it falls apart into a silky, sticky texture.",
    ["joue de b\u0153uf brais\u00e9e", "daube de joue au vin rouge", "joue de b\u0153uf confite", "carbonade"])

doc = {
    "culture": "France",
    "id": "fr",
    "flag": "FR",
    "blurb": (
        "The French d\u00e9coupe follows the seams between individual muscles rather than sawing straight "
        "across the bone, so one carcass yields some 29 named morceaux that each correspond to a muscle "
        "or a tight group of them \u2014 which is why the onglet, the araign\u00e9e and the merlan exist in France "
        "and have no clean English equivalent. Each morceau is then graded by the cooking it wants: "
        "griller and r\u00f4tir for the lightly worked premi\u00e8re cat\u00e9gorie, braiser and mijoter for the middle, "
        "bouillir for the collagen-heavy neck, shanks and breast. The finest seam cuts are so small and "
        "so fiddly to extract that butchers traditionally kept them back for themselves \u2014 the morceaux "
        "du boucher."
    ),
    "sources": [
        "https://fr.wikipedia.org/wiki/D%C3%A9coupe_du_b%C5%93uf",
        "https://en.wikipedia.org/wiki/Cut_of_beef",
        "https://fr.wikipedia.org/wiki/Paleron",
        "https://www.la-viande.fr/cuisine-achat/cuisiner-viande/cuisiner-boeuf/morceaux-boucher",
        "https://jeretiens.net/le-nom-des-morceaux-de-boeuf-decoupe-a-la-francaise/",
        "https://www.lesviandesdubourbonnais.fr/les-morceaux-du-boeuf/",
        "https://degustonfoin.fr/blogs/recettes-viande-bovine/les-morceaux-du-boeuf",
    ],
    "cuts": C,
}

out = r"C:\Users\kk\Code\beef-atlas\data\cuts_fr.json"
with io.open(out, "w", encoding="utf-8") as f:
    json.dump(doc, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", out, len(C), "cuts")

# ---- validation ----
def hit(a, b):
    return min(a[1], b[1]) - max(a[0], b[0]) > 1e-9

bad = 0
for p, q in itertools.combinations(C, 2):
    if hit(p["x"], q["x"]) and hit(p["z"], q["z"]):
        print("OVERLAP:", p["id"], p["x"], p["z"], "<->", q["id"], q["x"], q["z"])
        bad += 1
print("overlaps:", bad)

ids = [c["id"] for c in C]
assert len(ids) == len(set(ids)), "duplicate ids"

merged = []
for a, b in sorted(c["x"] for c in C):
    if merged and a <= merged[-1][1] + 1e-9:
        merged[-1][1] = max(merged[-1][1], b)
    else:
        merged.append([a, b])
print("x spans:", merged)
prev = 0.0
for a, b in merged:
    if a > prev + 1e-9:
        print("GAP in x:", round(prev, 3), "->", round(a, 3))
    prev = max(prev, b)
if prev < 0.80:
    print("GAP in x:", round(prev, 3), "-> 0.80")
