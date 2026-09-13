# Can the atlas be rebuilt on muscles? Mostly yes.

The question this table was built to answer: **is there enough published information to
define each cut by the muscles it contains and where along them it stops, or would we be
guessing?**

The answer, for all 153 cuts in seven traditions, measured rather than estimated:

| tradition | cuts | muscles sourced | bounds sourced | **carvable** | no muscle named |
|---|---:|---:|---:|---:|---:|
| Japan | 24 | 22 (91%) | 21 (87%) | **21** | 1 |
| Korea | 25 | 22 (88%) | 23 (92%) | **22** | 1 |
| Brazil | 24 | 20 (83%) | 20 (83%) | **17** | 2 |
| United States | 11 | 9 (81%) | 11 (100%) | **9** | 0 |
| France | 29 | 21 (72%) | 24 (82%) | **18** | 0 |
| Russia | 23 | 10 (43%) | 16 (69%) | **9** | 0 |
| United Kingdom | 17 | 11 (64%) | 6 (35%) | **6** | 0 |
| **total** | **153** | | | **102 — 66%** | 5 |

*Sourced* means graded `standard` or `trade`, which the checker only allows with a
verbatim quote behind it. *Carvable* is the strict test: the muscle list **and** the
boundaries are both sourced **and** the cut names at least one muscle the model has.

**Two thirds of the atlas could be rebuilt on muscles today.** The remaining third is
not a research dead end; see below.

## What the exercise actually proved

**The blocker was never knowledge, it was retrieval.** Every one of the seven traditions
has a national or international standard that defines its cuts properly. The difference
between a tradition scoring 92% and one scoring 35% is almost entirely whether that
standard can be pulled down as text:

| | |
|---|---|
| **Japan** | JMGA 部分肉取引規格 — full 別表1 as HTML at `jmga.or.jp/standard/beef-partial/` |
| **Korea** | 식약처고시 제2019-113호 [별표 3] — reachable through `law.go.kr`'s non-JS sibling endpoints, as print images |
| **Russia** | ГОСТ 31797-2012 and 7595-79 — full text at `base.garant.ru` and a narod.ru mirror |
| **United States** | IMPS Series 100 — 403 everywhere; recovered only because an earlier pass had cached the PDF to a temp directory |
| **France** | UNECE bovine standard — 403 at source, readable through translation-memory parallel segments |
| **Brazil** | ABIEC's cuts book — 18 MB, over the fetch limit, needs `curl` + `pdftotext` |
| **United Kingdom** | AHDB — the only one with **no** boundary spec to find at all |

The US is the sharpest example. It went from the worst-bounded tradition in the table to
**11 of 11 boundaries at `standard`** on the strength of one recovered PDF, without a
single new fact being discovered. Nothing about American butchery was unclear; the
document was just hard to fetch.

## The two weak traditions have opposite problems

**Russia** is 69% bounded and 43% muscled. ГОСТ defines отрубы by vertebra and rib with
great precision and mostly declines to name muscles — and it uses none of the kitchen
names (оковалок, кострец, огузок, щуп), so every retail cut needs a trade bridge that
ГОСТ does not provide. It is also the only tradition with real **disagreement**: five
cuts are `contested`, because wholesale catalogues and retail usage genuinely sell
different things under the same word.

**The United Kingdom** is the mirror image: 64% muscled and only 35% bounded. AHDB names
muscles well — it titles a page *Clod Flat Muscle (Brachialis)* — and publishes no
boundary specification at all. Some British cuts appear to be documented nowhere: AHDB
has a Latin name for the feather, the spider and the pavé, and **nothing whatsoever for
thick rib, top rib or leg-of-mutton cut.**

Those gaps are complementary, which points at the cheapest way to finish: both
traditions' cuts have UNECE or IMPS equivalents, and a cross-walk would supply Russia's
muscles and Britain's boundaries without new primary research.

## Where the information genuinely runs out

Five cuts name no muscle the model has, and each is a different kind of honest failure:

- **língua** (BR) and **タン** (JP) — the tongue. No standard describes its musculature,
  and the atlas models no lingual muscle at all.
- **matambre** (BR) — it is entirely *M. cutaneus trunci*, which the model lacks.
- **테ール** (JP) — JMGA has no tail item; it leaves with the offal.
- **araignée** (FR) — still unbroken after two research passes. Every source describes
  where it is and none names the muscle. It is the obturator internus, and no publication
  will say so.

And a shape of answer that recurs across traditions: **many cuts are bone-defined on
purpose.** 갈비 and its sub-cuts are rib spans. 차돌박이 is "ribs 1 to 7, about 15 cm
wide". Завиток is "along the line of the costal cartilages from the 8th rib to the 13th".
Oxtail and 꼬리 are vertebrae. That is not missing information — it is the correct
definition, and the schema records it as a boundary with no muscle list.

## What the model would need

Every one of the 49 modelled muscles is referenced by at least one cut, so nothing in the
anatomy is wasted. Against that, the table asks for **79 muscles the model does not
have, 216 times**. Twelve of them would close most of the gap:

| references | muscle | what it unlocks |
|---:|---|---|
| 12 | *M. cutaneus trunci* | all of Brazilian **matambre**, Japanese **カッパ** |
| 12 | *M. flexor digitorum profundus* | the shanks, every tradition |
| 11 | *M. flexor digitorum superficialis* | shanks; Japanese **センボン**, Korean **아롱사태** |
| 8 | *M. pectineus* | the inside round, named by CFIA and ГОСТ |
| 7 | *M. gluteus profundus* | the rump in every tradition |
| 7 | *M. iliacus* | half of the tenderloin; Japanese **テート** |
| 7 | *M. sartorius* | the French **merlan** — the only gap with a cut name of its own |
| 7 | *M. brachialis* | AHDB's **clod flat**, Korean **상박살** |
| 7 | *M. extensor digitorum communis* | the foreshanks |
| 6 | *M. gluteus accessorius* | Japanese **ネクタイ** |
| 6 | *M. flexor carpi ulnaris* | the foreshanks |
| 5 | *M. coracobrachialis* | ГОСТ's клювовидноплечевая |

Plus a lingual group, which is a different modelling problem — the tongue is not a
skeletal muscle with an origin and an insertion.

## What this does not settle

The table says *which* muscles and *between which bones*. It does not say **where along
a rib** — Japan's JMGA separates かたばら from かたロース about a third of the way down
the rib, running along the ribs rather than across them, and `from`/`to` cannot express
that. ザブトン and 三角バラ come out with identical bounds. That affects a handful of
cuts and is recorded in SCHEMA.md rather than patched over.

It also leaves three of the atlas's own rectangles contradicted by their national
standards, recorded in the relevant `dispute` fields and deliberately not applied,
because changing them means recarving models:

- **リブロース is ribs 7–10**, not the 5th rib to the last rib.
- **サーロイン starts at rib 11** and runs to the sacrum — three ribs longer than a US
  striploin, and it contains no tenderloin at all, because JMGA pulls ヒレ out whole
  before the loin is divided.
- **カメノコ is a シンタマ muscle**, not a ソトモモ one.
