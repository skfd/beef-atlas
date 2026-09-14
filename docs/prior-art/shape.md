# Prior art for *this* shape

The [first round](landscape.md) asked who else lists cut names across languages. It was seeded with a
competitor's website, and it answered that question well. This round asks the narrower and more useful
one: **who else has built the thing in this repo**, seeded with the repo itself.

Research date **2026-09-13**; five parallel threads, raw output in [`notes-shape/`](notes-shape/).

## The shape, stated exactly

Four features. They are independent — most prior art has one or two, and the interesting question is
always which.

1. **One animal, many partitions, one shared frame.** Every cut in every tradition is authored against
   [`FRAME.md`](../../data/FRAME.md), not against a per-country chart, so the same region of the animal
   carries the same numbers everywhere. 153 cuts, 7 traditions.
2. **Quantified overlap between partitions.** The US short loin is *91%* Russian тонкий край, *82%* the
   British sirloin. A number, not a label.
3. **Cuts keyed to named anatomy.** 115 named bones, muscles and organs in the same frame, plus a per-cut
   muscle composition table sourced to regulatory standards with verbatim quotes
   ([`data/composition/`](../../data/composition/)).
4. **Interactive 3D web delivery.** Click the model, peel muscle layers, cut away the near side, explode.

### One correction to make before claiming anything

**The published percentages are areal, in two dimensions.** `FRAME.md` describes cuts as unions of 3D
boxes, but no cut in any of the seven files has a `boxes` key — the authored unit is a single `x`/`z`
rectangle in the sagittal plane plus a `full_width` flag, and [`web/app.js:217`](../../web/app.js)
intersects those rectangles. The box unions are *derived* at build time by
[`blender/cuts.py:111`](../../blender/cuts.py) so that overlapping claims tile cleanly, and the mesh only
clips the silhouette.

`full_width` does not change that, which is worth stating because the field's name suggests otherwise:
nothing geometric reads it. [`blender/build.py:56`](../../blender/build.py) hardcodes `y_half=0.6` and
`carve()` is handed only `(x0, x1, z0, z1)`, so **every cut is carved the full width of the animal
regardless**. The flag's only consumer is [`web/app.js:394`](../../web/app.js), where it prints a note
telling the reader that this particular cut is a thin sheet in life and the slab is "whereabouts, not the
shape of the cut". It is an honesty label in the UI, not a parameter.

So the atlas is, underneath, a **2D areal partition problem** — which is lucky, because it means the
geographic literature in §3 applies literally rather than by analogy.

(`FRAME.md` should be fixed to say so; that is a separate change.)

## The verdict, one row per feature

| | closest prior art | how far it got |
|---|---|---|
| **1. many partitions, one frame** | "3D Beef Cuts Guide — Steak, Yakiniku & Butcher Atlas" (2026) | three partitions over one mesh — but they are *registers within Japan/the West*, not national traditions |
| **2. quantified overlap** | — | **nothing.** Swatland counts name survival; the largest published table explicitly declines the claim |
| **3. anatomy-keyed cuts** | UNL Bovine Myology (2004) | 119 muscles → 85–92 US retail cuts, as a delimited string; one tradition; no shared frame |
| **4. interactive 3D + anatomy** | Toyonishi Farm 牛肉3D部位解説 | 95 parts of a Japanese carcass in three.js, viscera inside a translucent body — but not clickable, and one tradition |

**Features 1, 3 and 4 are each anticipated. Feature 2 is not, and the reason it is not is the most
interesting thing this round found.**

## 1. Feature 2 is empty, and not by accident

The field knows partial overlap is the real phenomenon, has known it for decades, and has repeatedly
declined to put a number on it.

**Swatland's concordance score is a philology metric, not a geometry one.** Round 1 called it "the only
prior work that quantified partial equivalence at all." That is wrong and this file supersedes it. The
2012 AMSA paper defines it in its own words:

> If a US cut overlapped with a British cut of the same name, it scored 1, with 0 for a mismatch by
> location.

It is a binary indicator summed over sources — 9 US primals × 10 British/Scottish charts, row sums 0–10
(Rib 10, Brisket 10, Flank 8, Chuck 4, Round 4, Loin 2, Plate 1, Sirloin 0, Shank 0). The thread
reconstructed the grid and **all ten column sums reproduce the printed margins**, so the numbers are
sound — they just measure something else. The score requires the two cuts to **share a name**: a cut
occupying 70% of the same anatomy under a different name scores 0, identically to one sharing nothing at
all. The section after the table is headed *"Linguistic survival."* His other four tables — Mexico, Japan,
Korea, Russia, the Netherlands, Chile, the Caribbean — carry **no numbers**; he writes that those cuts have
"a major overlap" but "seldom share identical outlines", and stops.

**The largest cross-country cut table ever published refuses the claim in its preface.** Huerta-Leidenz
(2013) for USMEF: 42–52 US cuts against 35+ countries, IMPS-keyed, 30,000 copies printed. The preface says
it *"no persigue presentar -mucho menos institucionalizar- equivalencias anatómicas o comerciales."* The
person with the biggest matrix and the strongest commercial reason to assert equivalence explicitly
declines to.

So feature 2 is not an empty niche nobody got to. It is a claim the field treats as not worth making —
which is a better thing to have an answer to. **The atlas's answer is that a percentage is exactly the
honest form of the claim**, because it is the form that cannot overstate: 64% says the Korean 채끝 is
mostly-but-not-the-same, and no name-equivalence table has a way to say that.

No meat-science paper computes Dice, Jaccard or any overlap coefficient between two carcass partitions.
Searched and absent — a null search, weaker than a blocked fetch, so grey literature may exist.

**And the consumer end of the genre does the same thing.** `beefcuts.org` — turned up while checking
names, and a good example because nothing about it is careless — is a nine-column table of American,
Brazilian, Argentine, Costa Rican, Mexican, French, Australian, Japanese and Italian cut names, with
notes in English and Spanish, titled *"Beef Cut Translations"*. Nine traditions, two languages of
commentary, real per-cut prose about what each is for. **Zero percent signs in the entire page**, and
no canvas, WebGL or model of any kind. It is the round-1 nine-column genre done well, and it stops
exactly where all of them stop. The domain currently returns a BunnyCDN "Domain suspended or not
configured" 403; the reading above is of the
[2025-03-26 capture](https://web.archive.org/web/20250326204452id_/https://beefcuts.org/).

## 2. Everything else is anticipated, and one of them ships this month

### The name is taken, and the product is close
**"Beef Atlas | 3D Cuts Guide"** — confirmed on the App Store,
[id6796940694](https://apps.apple.com/us/app/beef-atlas-3d-cuts-guide/id6796940694), developer Kittichote
Kamalapirat, free, too few ratings to display an average. The free web build is at
`beefatlas.kittichoteshane.workers.dev`, whose own page title is *"3D Beef Cuts Guide – Steak, Yakiniku &
Butcher Atlas"*. One GLB (12,857 verts, 46 selectable entities) carrying **three partitions over one
mesh** — Steakhouse 17 cuts, Yakiniku 39, Butcher 72 — in EN/JA/TH, with declared `skin` (opacity 0.16) /
`skeleton` / `carcass` / `cuts` layers and an isolation behaviour that fades the hide and unselected cuts
to reveal deep anatomy. That is features 1, 3 and 4 at once.

Two things keep it apart from this atlas, and both were re-measured here from its public
`/atlas/atlas-catalog.json` (235,362 bytes). Its partitions are **registers, not countries**:
`"restaurantSystems": ["steakhouse", "yakiniku"]`, exactly two, over 48 `cutConcepts` and 94
`anatomicalInstances`. And its 62 cross-system relationships are **qualitative labels** — `exact` 41,
`derived` 12, `approximate` 5, `broader` 2, `restaurantDependent` 2, confidence `verified` 53 /
`supported` 8 / `provisional` 1 — with, checked explicitly, **no numeric field anywhere in any of them**.
They also bind a *term* to a *concept* (`term.en.ribeye` → `concept.ribeye`), which is a terminology
assertion rather than a comparison of two regions.

On provenance, the same catalog says so itself, in a `geometryReference` block quoted here verbatim:

> `"id": "reference.toyonishi.beef-viewer"`, `"productionTopology": "toyonishiDetailed"` … "This is the
> only anatomy topology in the project. Modified Toyonishi-derived GLB/USDZ exports are approved for
> reviewed iOS and production web distribution."

Recorded because **this project will be asked whether its own cow is independently authored** — it is,
procedurally generated by [`blender/cow.py`](../../blender/cow.py). The developer's declaration that such
exports are "approved" is their claim, and nothing here disputes it.

### UNL did anatomy-keyed cuts in 2004, and shipped the data as JSON
`https://bovine.unl.edu` is live and further along than expected. **Fetched and counted directly**:
`bovine.unl.edu/muscles.json`, 1,390,225 bytes, **119 muscles**, 91 carrying a `retail_cuts` field —
**346 muscle→cut pairs over 92 distinct US retail cut names** when split on commas. Also 197 IMPS
subprimals with verbatim spec text, and 143 cross-section and dissection layers carrying 1,830 muscle
polygons and 323 bone polygons as 2D image maps, two of them serial dissections with layers named
*"Semimembranosus removed"*. Cite it as **Jones, Guru, Singh, Carpenter, Calkins & Johnson, 2004**, the
site's own requested citation. No licence statement anywhere.

**Do not say nobody has done anatomy-keyed cuts.** What survives, and is stronger for being precise: it is
**one tradition**; the cut↔muscle link is a **delimited string**, not a relation (the cross-section
`muscle_id` is a real foreign key, so they knew the difference); its geometry is per-photo pixel polygons
with **no shared frame** and no cut boundaries; and its interactive 3D was **Shockwave at `/bovine3D`,
served 2004→2011-08, 404 from 2012**. Rebuilding that in the browser is a 2004 idea whose runtime died,
not a new one.

Directly useful: **32 of this repo's 49 muscles match a UNL muscle name exactly**, so `muscles.json` is an
independent cross-check on the US half of [`data/composition/us.json`](../../data/composition/us.json) that
costs nothing to run.

### The French Meat Academy thesaurus is found — and does not do what we hoped
Round 1's best open loop, closed. It is **`MEAT-T` on AgroPortal** (`agroportal.eu/ontologies/MEAT-T`):
**1,505 concepts**, FR/EN, DOI `10.15454/PB5QXC`, licence **Etalab 2.0** — genuinely open. But searching it
for `longissimus` returns **0** concepts and `muscle` returns 4, none of them a named muscle, while
`faux-filet` returns 18. **It is cuts without anatomy.** The Recherche Data Gouv record holds zero files
and the API needs a free login, so the concept list is measured through AgroPortal's search, not a
download.

### Everything non-US, non-Japanese is a measured negative
Interbev/Idele cutting posters state the aim of *"localiser les différents muscles"* and contain **zero**
Latin muscle names. A 90,000-word Interbev quality reference has **four** muscle:cut equivalences, in a
chart legend. **NAV 6th ed.** (2017, free) has 157+ `M.` terms and zero occurrences of steak, brisket,
sirloin or butcher — the veterinary nomenclature and the trade nomenclature do not touch. Porcine Myology
has 110 muscles and no cut field. Japan's only equivalent is a vet student's 2021 blog with 30
assignments, several marked `(?)`. No Korean or Brazilian interactive tool exists.

### Industry puts cuts in a scanned frame — and publishes only weights
Anatomy-in-a-shared-frame is real and current, all from one research lineage. **Ho, Yu, Gangsei & Kongsro
(2019)**, *Meat Science* 148:1–4, `10.1016/j.meatsci.2018.09.011` — a parametric mesh from one pig CT,
**84 muscles and 121 bones in a single frame**, with "virtual meat cuts" named as a potential application.
**Ritchie & Ho (2025)**, `10.1080/00288233.2024.2305825` — a lamb atlas in Unity3D where a virtual knife
resects to *New Zealand* specifications and returns volume and weight per cut. **RoBUTCHER**
(`10.1016/j.atech.2023.100388`) registers a CT atlas to a live point cloud and generates **cutting
trajectories** — the only fetched sentence anywhere describing a cut as a *surface* in a scanned animal's
frame.

All three are paywalled or truncated, none publishes geometry, and all are single-tradition. There is **no
bovine Visible Human**: the Visible Animal Project is a dog.

## 3. The metric has a name, and two disciplines already own it

This is what the outside-meat thread was for, and it is the most immediately usable result.

**Bohland, Bokil, Allen & Mitra (2009), "The brain atlas concordance problem", PLoS ONE 4(9):e7200** is
this project's shape in another substance. One brain (Colin27, registered to MNI-305), **eight parcellation
schemes** applied to it (AAL 62 regions, CYTO 29, Harvard-Oxford 56, ICBM 49, LPBA40 29, T&G 65, TALc 68,
TALg 49), compared by spatial overlap *"discounting the names of regions and instead comparing their
definitions as spatial entities"* — which is precisely what this atlas does and precisely what Swatland
does not. Their framing question is this atlas's front page:

> what is the probability that a voxel is in Region X according to Method A if it is in Region Y according
> to Method B?

Their measure, Eq. 3, is **non-symmetric conditional overlap**:

    P(i|j) = |r_i ∩ r_j| / |r_j|

the proportion of region *r_j* contained within the bounds of *r_i* — **identical to
`overlapFraction(a, b) = area(a ∩ b) / area(a)`** in `web/app.js`. They prefer it to Dice and Jaccard for a
stated reason: those reach 1 only when two regions are *identically* defined, whereas P(i|j) reaches 1 on a
pure subset relationship — which is the right behaviour when France's 29 cuts are largely a refinement of
America's 11.

Geographers compute the same quantity routinely and call it an **allocation factor** (`afact` in Geocorr),
under the heading of **areal interpolation**; the **Modifiable Areal Unit Problem** (Openshaw 1984) splits
the *scale* effect from the *zoning* effect, which is exactly the France-cuts-smaller versus
Britain-shifted-forward distinction in [`differences.md`](../differences.md). The US Census Bureau ships the
complete pairwise tract intersection table as an 18 MB text file.

The third analogue is the closest in substance and the weakest in method: the *Language Sciences* 28(2–3)
2006 issue on **body-part terminology**, where speakers of different languages draw their language's
body-part terms **on the same six standard illustrations** — one shared frame, many cultures' partitions,
compared qualitatively and never scored.

**A cautionary note worth keeping.** Bohland published the full overlap matrix at `obart.info`. That domain
no longer resolves.

## What to do with this

1. **Name the metric.** One sentence in `differences.md`: this is the non-symmetric conditional overlap
   *P(i|j)* of Bohland et al. (2009), the standard measure for comparing two parcellations of one object;
   geographers call it an allocation factor. It costs nothing and moves the percentages from a homemade
   number to a cited one.
2. **Ship the matrix as data** — `data/overlap.csv`, **both directions per pair**, because the measure is
   non-symmetric and publishing one direction is the mistake that invites the Dice objection. Bohland's
   site going dark is the argument for putting it in the repo rather than only in the page.
3. **Cite UNL.** The README should say what came before, and UNL Bovine Myology is the honest ancestor of
   the anatomy layer. Then run `muscles.json` against `data/composition/us.json` — 32 muscle names already
   match.
4. **Correct round 1.** [`README.md`](README.md) calls Swatland "the only prior work that quantified partial
   equivalence"; §1 above shows he quantified name survival. Fix it rather than leave two files disagreeing.
5. **Decide about the name.** — **decided 2026-09-14: the project is now `Beef Phrasebook`.** Another live product is called *Beef Atlas* in this exact category, on the
   App Store and the web. It has no ratings yet and this repo is not on a storefront, so there is nothing
   forcing the issue — but the decision is cheaper now than after a launch. (A thread reported its release
   as 2026-08-19; the store page did not show me a date, so treat that as unconfirmed.)
6. **Consider Bohland's S-index**, `S = 1 − 4 Σ W_ij X_ij (1 − X_ij)`, which runs on numbers already
   computed and collapses 153×153 into a 7×7 table that does not penalise France for being a refinement.

## Confidence

Same rules as round 1: every number traceable to a fetched URL, and a negative resting on a blocked fetch
marked unproven rather than asserted.

**Verified by direct fetch in this session**, not taken from a thread: the competitor's App Store listing,
its web page title, and its catalog JSON — the two `restaurantSystems`, the 62 relationships and their
label counts, the absence of any numeric field in them, and the `geometryReference` provenance block.
Also `bovine.unl.edu/muscles.json`, with counts recomputed here: **346 pairs over 92 cut names**, against
the thread's 355/85. The gap is the delimiter — the field is comma-separated prose, and two readers split
it differently, which is exactly the point about it being a string rather than a relation.

**Unproven and marked so in the notes:** Trypuz et al. 2016 is hard-blocked (Springer 303s to an auth wall,
Semantic Scholar returns a null abstract) — **do not assume it handles multilingual naming or cutting-line
geometry**. The three CT-atlas papers are paywalled; their internals rest on abstracts. The competitor's
2026-08-19 release date rests on one thread's fetch. `unece.org` still 403s everything.

**Still unread, and still the one thing that could overturn §1:** Swatland, *Meat Cuts and Muscle Foods: An
International Glossary*, 258pp. No Google Books preview, zero archive.org copies. His archived Guelph site
yielded a free 332-headword glossary whose equivalences are redirects and muscle lists with no grading
anywhere — consistent with the verdict, not proof of it. A library copy remains the highest-value
outstanding action.

**Closed since round 1:** HAM item numbers **are** UNECE item numbers (1643 Brisket, 2012 Inside Cap, 2240
Cube Roll all match; both obey bone-in→1, boneless→2; HAM is a superset). The crosswalk is demonstrably
lossy — HAM 2240 and 2243 both map to NAMP 112 with no way to say they relate differently. Lhuissier is
*Food and Foodways* 10(4):183–208, doi `10.1080/07409710216028`.
