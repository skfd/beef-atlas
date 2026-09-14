# The same cow, cut seven ways

*What the Beef Atlas data says about how the United States, the United Kingdom, France,
Russia, Brazil, Korea and Japan disagree about a carcass — and where they don't.*

Every cut in this project is a rectangle in one shared frame: `x` runs from tail to nose,
`z` from the ground to the withers. Because all seven traditions are drawn on the same
animal, they can be measured against each other. When this piece says the American short
loin is "82% the British sirloin", it means 82% of the American rectangle is covered by
the British one.

> **What the percentages are and aren't.** They are overlap of rectangles in a side-view
> projection, not anatomy. They capture front-to-back and top-to-bottom disagreement
> well, and they are blind to left-to-right: muscles that differ by depth rather than
> position — British topside versus silverside, French *poire* versus *merlan* — are
> flattened onto the same patch. Where a low number is an artifact of that, this piece
> says so. Treat them as a measure of *where on the animal*, not of butchery equivalence.

### The measure has a name

It is not homemade. Dividing the shared area by the area of the cut you started from is
the **non-symmetric conditional overlap** *P(i|j) = |rᵢ ∩ rⱼ| / |rⱼ|* defined by
[Bohland, Bokil, Allen & Mitra (2009)](https://doi.org/10.1371/journal.pone.0007200) for
the *brain atlas concordance problem* — comparing several schemes that carve one brain
into differently-named regions, by registering them all into one coordinate frame and
"discounting the names of regions and instead comparing their definitions as spatial
entities". Geographers compute the identical quantity when they translate one set of
boundaries into another and call it an **allocation factor**, or an areal weight, under
the heading of *areal interpolation*. The measure here is area, so that method applies
literally rather than by analogy.

Bohland's reason for preferring it to the symmetric coefficients — Dice, Jaccard — is
the reason it is right here too: those reach 1 only when two regions are *identically*
defined, whereas this one reaches 1 on a pure subset. France cuts 29 pieces where
America cuts 11, so most French cuts are *refinements* of American ones rather than
rivals to them, and a symmetric index would report near-total disagreement where the
truth is clean containment.

**It runs in one direction only, and the direction is part of the number.** *P(i|j)* and
*P(j|i)* are different quantities: a small cut wholly inside a large one is 100% of
itself and a fraction of the other. Every percentage below is stated as *how much of the
first cut is covered by the second*, and where both directions matter — §2's British
false friend is the case — both are given.

---

## 1. The short version

Beef traditions agree about the middle of the animal and disagree about its ends. The
loin and rib — the expensive strip running along the back — are named nearly identically
everywhere. The shoulder and the hind leg are where cuisines part company, and they part
company in proportion to how much slow cooking and thin-slicing they do.

The crudest measure is how big an average cut is:

| Tradition | Cuts | Mean cut size | Smallest | Largest |
|---|---:|---:|---:|---:|
| United States | 11 | 0.040 | 0.020 | 0.103 |
| United Kingdom | 17 | 0.033 | 0.006 | 0.076 |
| Brazil | 24 | 0.018 | 0.008 | 0.036 |
| Russia | 23 | 0.017 | 0.006 | 0.042 |
| Korea | 25 | 0.016 | 0.004 | 0.048 |
| Japan | 24 | 0.016 | 0.005 | 0.029 |
| France | 29 | 0.015 | 0.006 | 0.048 |

*(Area in frame units; the whole animal is roughly 1 × 1.)*

The average French cut is **2.7 times smaller** than the average American one. That is the
whole story in one number, and everything below is the texture of it.

---

## 2. The British false friend

**This is the single most useful fact in the atlas, and it catches people constantly.**

British cut names sit *one primal forward* of American ones:

| You say | They mean | Overlap |
|---|---|---:|
| American **short loin** | British **sirloin** | 82% |
| American **sirloin** | British **rump** | 82% |

A British "sirloin steak" is cut from what an American butcher calls the short loin — the
same muscle that yields a New York strip. A British "rump steak" is what an American menu
calls sirloin. The confirmation runs in both directions at the same 82%, which is about as
clean as this data gets.

It goes further: the British *sirloin* runs forward over the last three ribs as the **wing
rib**, so the British **fore rib** is only the five ribs ahead of that, rather than the
whole American rib primal.

The British scheme is also the one that most resembles the American in spirit — large
roasting joints, a small number of them — while using almost none of the same words.

## 3. Where everyone agrees: the loin and the rib

Put an American primal down and ask what covers it elsewhere:

| American primal | UK | France | Russia | Brazil | Korea | Japan |
|---|---|---|---|---|---|---|
| **Rib** | Fore rib 64% | Côtes/entrecôtes 55% | Толстый край 64% | Contrafilé 55% | 꽃등심 82% | リブロース **91%** |
| **Short loin** | Sirloin 82% | Faux-filet 55% | Тонкий край **91%** | Contrafilé 55% | 채끝 64% | サーロイン 73% |
| **Sirloin** | Rump 82% | Rumsteck 55% | Оковалок 78% | Alcatra 70% | 채끝 45% | サーロイン 31% |

Japanese リブロース covers the American rib primal at **91%**, and Russian **тонкий край**
covers the American short loin at exactly the same figure — the closest correspondences in
the whole atlas, across two of the largest cultural distances in it. *Тонкий край* means
literally "thin edge", named for the shape of the muscle rather than for a place on the
animal, and it still lands on the same beef as a New York strip.

This is not a coincidence of naming. The loin and rib are the muscles along the spine that
carry weight but barely move, so they are tender everywhere, expensive everywhere, and
cooked fast everywhere. There is only one sensible way to take them off a carcass, and
every tradition found it.

## 4. Where they diverge: the shoulder

The shoulder is the opposite case. It is a knot of hard-working muscles of wildly different
texture, and what you do with it depends entirely on how you cook.

Count the cuts each tradition places in each band of the body:

| Body zone | US | UK | FR | RU | BR | KR | JP |
|---|---:|---:|---:|---:|---:|---:|---:|
| Hind leg & round (x 0.00–0.24) | 4 | 5 | **9** | 8 | 8 | 5 | 6 |
| Sirloin (0.24–0.36) | 2 | 6 | 6 | 3 | 5 | 5 | 7 |
| Loin (0.36–0.46) | 2 | 3 | 5 | 5 | 3 | 6 | 7 |
| Rib (0.46–0.56) | 2 | 3 | 4 | 5 | 5 | 5 | 3 |
| **Shoulder & chuck (0.56–0.72)** | **3** | 5 | 8 | 7 | 8 | **11** | 7 |
| Neck (0.72–0.80) | 2 | 2 | 1 | 3 | 3 | 3 | 4 |

Korea names **eleven** cuts where the United States names three. Spelled out:

- **United States** — Chuck, Brisket, Fore Shank.
- **Korea** — 갈비 (short rib), 갈비살 (rib finger meat), 등심 (loin, reaching forward),
  살치살 (chuck flap tail), 앞다리 (foreleg), 부채살 (top blade), 양지 (brisket/plate),
  차돌박이 (brisket point, sliced paper-thin), 앞사태 (foreshank), 제비추리 (the *longus
  colli* under the neck bones), 목심 (neck/chuck roll).
- **France** — Basses côtes, Gros bout de poitrine, Paleron, Macreuse à bifteck, Jumeau à
  bifteck, Jumeau à pot-au-feu, Macreuse à pot-au-feu, Gîte avant.
- **Japan** — カタ, ミスジ, トウガラシ, カタロース, ザブトン, リブロース, カタバラ.

Notice what France does there: it names the *same* region twice — *macreuse à bifteck* and
*macreuse à pot-au-feu*, *jumeau à bifteck* and *jumeau à pot-au-feu*. The French scheme
splits by **how you will cook it**, grill versus stew, and builds that into the name. No
other tradition here does that.

The consequence is that the American **chuck** has no good counterpart anywhere: its best
match in any of the other six is only **54%** (the British *neck and clod*). It is not
that the others disagree about where the shoulder is. It is that nobody else is willing to
call that much meat one thing.

## 5. Where they diverge: the hind leg

The American **round** is the most parochial cut in the atlas — nothing anywhere covers
more than **34%** of it. Everyone else takes the hind leg apart by muscle:

- **UK** — silverside, topside, thick flank, leg, plus rump above.
- **France** — nine named morceaux in the same span: rond de gîte, gîte à la noix, tende de
  tranche, tranche grasse, araignée, aiguillette baronne, rumsteck, gîte, queue.
- **Brazil** — picanha, alcatra, patinho, coxão mole, coxão duro, lagarto, ossobuco, rabo.
- **Japan** — ランプ, イチボ, ウチモモ, ソトモモ, スネ, テール.

Part of that 34% is the projection artifact: topside and silverside are the inside and the
outside of the same leg, and a side view cannot separate them, so the atlas tiles them
front-to-back instead. But the direction is real. Only the American and (to a lesser
extent) Korean schemes treat the hind leg as a single large block to be roasted or ground;
everyone else treats it as a drawer of individually named muscles.

**Brazil's picanha** is the sharpest case. It is the rump cap — a triangle of muscle under
a thick fat cap that most traditions bury inside a larger round or rump cut and sell as
nothing in particular. Brazil made it the prestige cut of the national cuisine.

## 6. Russia grades where everyone else only names

Every other tradition here answers the question *what is this cut*. The Russian retail
standard, **ГОСТ 7595-79**, also answers *what is it worth*. It divides a side into eleven
**сортовые отрубы** and assigns each one of three **сорта** by the ratio of muscle to
connective tissue:

| Sort | Отрубы | Share of the carcass |
|---|---|---:|
| **1-й сорт** | тазобедренный, поясничный, спинной, лопаточный, плечевой, грудной | ~88% |
| **2-й сорт** | шейный, пашина | ~7% |
| **3-й сорт** | зарез, передняя голяшка, задняя голяшка | ~5% |

That is a third axis of organisation, alongside France's grading by cooking method and
Japan's by marbling — and unlike either, it is a **price** grade written into a state
standard. The US and UK schemes grade nothing at the cut level at all.

Underneath the standard sits an older kitchen vocabulary the GOST never names —
*оковалок*, *кострец*, *огузок* and its two faces *щуп* and *ссек*, *глазной мускул*,
*завиток*, *челышко*, *покромка*. Russian cooks use those words; the standard uses the
eleven отрубы. Both are in the atlas, each subcut carrying the sort of the отруб it falls
inside.

Two placements are worth flagging. The GOST's spinal/lumbar boundary falls between ribs
**11 and 12**, two ribs ahead of the last-rib line most other traditions quarter on. And
*зарез* is only the first two neck vertebrae — the atlas of the neck, which is a far
smaller and lower-value cut than "neck" implies anywhere else.

## 7. The diaphragm is the tell

The clearest single diagnostic of a cuisine's relationship to beef is whether it bothers to
name the diaphragm and the belly sheets — thin, strongly-grained, intensely beefy muscles
that are superb grilled fast and sliced across the grain, and mediocre at everything else.

| Tradition | Named diaphragm/skirt/sheet cuts |
|---|---|
| **France** | Bavette d'aloyau, Bavette de flanchet, **Onglet**, **Hampe** — four |
| **Japan** | カイノミ, **ハラミ**, **サガリ** — three |
| **Korea** | 토시살, **안창살**, 갈비 — three |
| **Brazil** | Fraldinha — one |
| **Russia** | Диафрагма, Завиток, Пашина — three, but the diaphragm leaves with the offal |
| **UK** | Thin flank — a region, not the muscle |
| **US** | folded into short plate and flank — none named separately at primal level |

France distinguishes *onglet* (the hanger, hanging free off the last rib) from *hampe* (the
skirt, the muscular part of the diaphragm) and knows they eat differently. Japan makes the
same distinction — ハラミ is the rib-side sheet, サガリ the lumbar crus — and both are
classified as offal under Japanese law despite eating like red meat. Korea splits 안창살
(the diaphragm sheet) from 토시살 (the pillar muscle that works it).

Russia is the interesting middle case: *диафрагма* is named, and *завиток* and *пашина*
are distinguished from each other along the belly, but the diaphragm is classed with the
offal rather than sold as steak — the same legal quirk Japan has, reached from a completely
different culinary direction.

Cuisines that cook thin slices over fire name these muscles. Cuisines that roast joints
don't. That is the rule, and it has almost no exceptions in this data.

## 8. The genuinely unique

Two cuts in the atlas have no meaningful counterpart anywhere, and both are Brazilian:

- **Cupim** (best match 33%) — the fatty hump of zebu (Nelore, *Bos indicus*) cattle, which
  sits on top of the withers. It is not that other traditions cut the hump differently;
  most of them raise cattle that do not have one. *The atlas cow is a European type, so
  cupim's shape marks the spot but the hump itself is missing — the page says so when you
  select it.*
- **Rabo** (19%) — oxtail, which the UK (*oxtail*), Korea (꼬리) and Japan (テール) also
  name, but placed differently enough in the frame that the overlap stays low.

## 9. So why?

Three different optimisation targets, visible in the geometry:

**The United States optimises for large, uniform grilling steaks.** Eight big primals,
worked outward from the spine, quartered between the 12th and 13th ribs. The rib and loin
are only about a quarter of the carcass but carry the ribeye, strip, T-bone, porterhouse
and tenderloin; the hard-working shoulder, leg and belly are boned out for roasts, barbecue
and ground beef. Fewer names, bigger pieces, more of the animal sold as an undifferentiated
block. Britain does the same thing with different words and a slightly finer hand.

**Korea and Japan optimise for the tabletop grill.** When the cooking method is "thin slices
over heat in front of the diner", the relevant unit is a *muscle with a consistent texture*,
not a saw cut through bone. So both name many small muscles — 차돌박이, 살치살, 부채살,
ミスジ, ザブトン, トウガラシ — and the names that diners actually use are these subcuts,
not the official primals. Japan layers a second axis on top: the price is set by marbling
(霜降り, graded 1–5) more than by which cut it is, which is why "A5" is a thing you order.

**France optimises for a taxonomy of cooking method.** Twenty-nine morceaux, followed by
muscle seams rather than sawn through bone, and graded *griller* / *braiser* / *bouillir* —
with the cooking method built into the name where two halves of one muscle group behave
differently. It is the most granular scheme here and the only one whose categories are
verbs.

**Brazil optimises for churrasco and the fat cap**, which is why a cut most traditions
discard into a larger one — picanha — is the one on the sign outside.

**Russia optimises for pricing a whole carcass fairly.** Eleven отрубы and three sorts is
not a cook's taxonomy, it is a shop's: it answers what a given piece should cost, in a
system where that had to be written down centrally. The cook's vocabulary survived
alongside it rather than being replaced by it.

---

*Data and sources: each tradition's `sources` array in `data/cuts_*.json`, and the
**About & sources** panel in the [atlas itself](https://skfd.github.io/beef-atlas/). The
backbone is Wikipedia's "Cut of beef" and its per-country counterparts, with USDA IMPS
Series 100, AHDB, la-viande.fr, ГОСТ 7595-79, scotconsultoria, 축산물품질평가원 and the
Japan Meat Grading Association behind the individual schemes. Every figure in this piece is
computed from the atlas data, not quoted from a source.*
