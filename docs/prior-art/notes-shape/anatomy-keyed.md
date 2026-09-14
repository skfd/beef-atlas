# Prior art, feature 3: anatomy-keyed cut references

*Thread: who has systematically answered "which muscles are in this cut" / "which cut does this muscle
land in". Research date 2026-09-13. Every number below was measured off a file or page actually
fetched; the command is named where it matters. Negative results are stated as such.*

## Summary — the one thing that matters

**UNL Bovine Myology (`bovine.unl.edu`) is live, and it ships the muscle→cut mapping as a public JSON
file: `https://bovine.unl.edu/muscles.json`, 1,390,225 bytes, 119 muscles, of which 91 carry a
`retail_cuts` string — 355 muscle→cut pairs over 85 distinct US retail cut names, plus origin /
insertion / action / innervation / blood supply per muscle and 39 muscles with full lab chemistry from
the Beef Checkoff muscle-profiling program.** It also carries 143 cross-section/dissection layers with
**1,830 muscle polygons and 323 bone polygons** as 2D pixel-space image maps. That is the closest thing
in existence to feature 3, and it is *further along than expected*: it is not a table in a PDF, it is a
queryable dataset with per-muscle anatomy. What it is **not**: it is **one tradition** (US retail /
URMIS names, IMPS subprimals), it has **no shared coordinate frame** (polygons are per-photo pixel
coordinates; the cross-section reference is a prose string like `"Round A - F"`), the cut side is a
**flat comma-separated string, not a keyed relation**, and its **interactive 3D is dead** — the old
`/bovine3D` Shockwave section (`3did.dcr`, "3D Rotation" and "3D Muscle ID") served content **2004 to
2011**, 404'd from 2012, and today `https://bovine.unl.edu/bovine3D` still returns **404**. Second finding, and it closes an open loop from the
earlier round: **the French Meat Academy SKOS thesaurus has been located** — it is `MEAT-T` on
AgroPortal, 1,505 concepts, Etalab 2.0 — and it is **not** anatomy-keyed: a search of it for
`longissimus` returns **0 concepts**.

---

## 1. UNL Bovine Myology — `https://bovine.unl.edu/` — **LIVE, the main hit**

Citation the site itself asks for (from `https://bovine.unl.edu/about`):

> Jones, S.J., Guru, A., Singh, V., Carpenter, B., Calkins, C.R., and Johnson, D. 2004. Bovine Myology
> and Muscle Profiling. Available: https://bovine.unl.edu

Funding and partners named on `/about`: **Beef Checkoff** (muscle profiling data), NCBA, Cattlemen's
Beef Board, **USDA AMS** (Bucky Gwartney), Univ. of Florida (Dwain Johnson), and UNL's **DEAL Lab**
(Distributed Environments for Active Learning) for the software. Contact today is Ty Schmidt, UNL
Animal Science.

### 1.1 The data is a public JSON file

Found by watching the browser's network tab on `/muscle-descriptions` — the pages are client-rendered
and `curl` of the HTML returns nothing useful, but the page fetches:

- `https://bovine.unl.edu/muscles.json` → **200, 1,390,225 bytes, application/json**

(`bones.json` and `subprimals.json` do **not** exist — both 404. Subprimal and cross-section data is
inlined into the page HTML as `var subprimals = [...]` / `var crosssection = {...}` instead.)

**Measured contents of `muscles.json` — a JSON array of 119 objects.** Fields:
`id, number, name, common_name, origin, insertion, action, innervation, blood_supply, retail_cuts,
group, primal, image, ExprMositure, Colo_L, ColorA, ColorB, emulsnCap, Tot_HemIron, TotaCollagen,
Moisture, Ash, Protein, Fat, pH, SensTendDry, SensTend_Moist, SensTend_EvaluDry, SensTendEval_Moist,
SenJuciness_Dry, SensJuici_Moist, Sens_FlavDry, SensFlavMoist, SensConn_Dry, Sens_Conn_Moist,
Sh_ForDry, She_For_Moist, appearsInCrossec, imageFileName, dairy_cow_mean, beef_cow_mean, created_at,
updated_at, profile, profile_data`

Non-empty counts (measured over all 119):

| field | non-empty | note |
|---|---|---|
| `name` (scientific) | **119** | e.g. `Adductor`, `Longissimus`, `Semimembranosus` |
| `origin` / `insertion` | **119 / 119** | full veterinary-anatomy prose |
| `action` | 118 | |
| `innervation` | 115 | |
| `blood_supply` | 114 | |
| `group` | 115 | 10 values: Abdomen, Cutaneous, Dorsal, Lumbar, Neck, Pelvic, Shoulder, Tail, Thoracic, Thorax |
| `primal` | 105 | free text, multi-valued as a string, e.g. `"Chuck, Rib, Loin"` |
| **`retail_cuts`** | **91** | **the feature-3 field** |
| `common_name` | 50 | e.g. `Adductor` → `"Inside round"` |
| `appearsInCrossec` | 81 | prose, e.g. `"Round A - F"` |
| `image` | 49 | `/images/muscles/36.jpg` |
| `pH` (i.e. lab chemistry) | **39** | matches Von Seggern et al.'s 39-muscle chuck/round study |
| `Sh_ForDry` (Warner-Bratzler) | 37 | |
| `SensTendDry` (sensory panel) | 24 | |
| `profile` (profiling dict) | **21** | 23 measured variables per carcass profile |

**The muscle→cut mapping, measured.** Splitting `retail_cuts` on commas and newlines:

- **355 muscle→cut pairs**
- **85 distinct retail cut names** (all US; URMIS/BIC-style, e.g. `Beef Chuck Arm Steak`,
  `Beef Round Top Round Roast`, `Beef Loin Tenderloin Steak`)
- cuts per muscle: min 1, max 18, mean **3.9** (355 pairs / 91 muscles)
- most-shared cuts: `Beef Chuck Arm Steak` (20 muscles), `Beef Chuck Arm Pot Roast` (19),
  `Beef Chuck Arm Pot Roast Boneless` (15), `Beef Chuck Arm Steak Boneless` (15),
  `Beef Chuck 7-Bone Steak` (14), `Shank Cross Cuts` (13), `Beef Rib Roast` (12)
- 79 muscles carry both `retail_cuts` and `appearsInCrossec`

Example record (muscle id 36):

```
"name": "Adductor", "common_name": "Inside round", "group": "Pelvic", "primal": "Round",
"retail_cuts": "Beef Round Steak, Beef Round Steak Boneless, Beef Round Top Round Steak,
                Beef Round Top Round Roast",
"appearsInCrossec": "Round A - F"
```

**Caveat that matters:** `retail_cuts` is a **flat string**, not a foreign key. Some entries have
embedded `\r\n` separators (`"Beef Chuck 7-Bone Pot Roast\r\nBeef Chuck 7-Bone Steak"`), so the
distinct-name count moves between 85 and 92 depending on how you split. There is no cut table for
retail cuts anywhere on the site — the 197 subprimals (below) are a *separate* list, keyed to IMPS, and
`retail_cuts` does **not** reference them. So the relation exists as text, not as data.

### 1.2 Subprimals — 197 of them, IMPS text, verbatim

Inlined on `https://bovine.unl.edu/subprimals` as `var primals` / `var subprimals` (a 143,670-char
inline `<script>`; extracted with a JSON `raw_decode`).

- **7 primals**: Brisket/Foreshank, Round, Chuck, Flank, Plate, Loin, Rib
- **197 subprimals**; 144 carry an `item_number` (`"Item No. 118"`, `"Similar to Item No. 114"`);
  195 carry a `description`
- The descriptions are **verbatim IMPS specification text**, e.g. item 118 Beef Brisket:
  *"This item includes the anterior end of the sternum bones, the deep pectoral, and the (web)
  superficial pectoral muscle…"* — muscles named **in prose**, not as a list
- `/about` confirms: *"The Institutional Meat Purchase Specifications were used as a reference in
  making these cuts."*
- **Photography**: 44 subprimals have image sets — 39 of exactly **16 images** (the 22.5°-per-frame
  rotation table described on `/about`), 2 of 13, 2 of 15, 1 of 17. The remaining **153 have zero
  images**. So the 360° rotation viewer covers roughly a fifth of the subprimals.

Note: this is the **reverse direction of feature 3 and it is only prose.** A subprimal record does not
carry a muscle list; you have to read the IMPS paragraph. The mapping is machine-readable in the
muscle→cut direction only.

### 1.3 Cross-sections and dissection layers — the closest thing to layer peeling

11 cross-section sets (`/cross-sections/1` … `/11`; 12+ return HTTP 500). Each page inlines
`var crosssection` with a `layers` array; each layer carries a base64 JPEG `photo`, a base64
`illustration`, and **arrays of `{muscle_id, coords}` and `{bone_id, coords}` polygons** in image
pixel space.

| id | name | layers | muscle polygon refs | distinct muscles |
|---|---|---|---|---|
| 1 | Brisket | 8 | 42 | 6 |
| 2 | Chuck | 17 | 313 | 37 |
| 3 | Flank | 3 | 10 | 4 |
| 4 | Foreshank | 4 | 32 | 10 |
| 5 | Loin | 18 | 167 | 26 |
| 6 | Plate | 5 | 131 | 8 |
| 7 | Rib | 13 | 168 | 18 |
| 8 | Round | 16 | 157 | 26 |
| 9 | Rump | 3 | 24 | 12 |
| 10 | **Lateral Fore Section** | 29 | 475 | 39 |
| 11 | **Lateral Hind Section** | 27 | 311 | 34 |

**Totals: 143 layers, 1,830 muscle polygons, 323 bone polygons, 143 photos + 143 illustrations,
95 distinct muscle ids referenced.**

Sets 10 and 11 are the important ones for shape: they are a **serial dissection**, one muscle removed
per layer, layer names literally reading `"Omotransversarius removed"`, `"Triceps brachii - lateral,
Triceps brachii - medial, Triceps brachii - long removed"`, `"Semimembranosus removed"`. This is
**layer peeling done photographically in 2004** — the same idea as this repo's feature 4, executed on a
real carcass instead of geometry. From `/about`:

> *"After each individual muscle was removed the carcass was photographed."*

Two 750-lb carcasses were used: one sliced into 1-inch cross-sections, one dissected laterally.

**Why it is not a coordinate frame:** the `coords` are 2D polylines in the pixel space of each
individual photograph (`"201,140 206,141 206,160 …"`). There is no registration between layers, between
cross-sections, or to any carcass-wide axis system. Cut boundaries are not in that space at all — only
muscles and bones are outlined.

### 1.4 Bones

`var bones` on each cross-section page: bone records with `name, skeletal_division (Axial /
Appendicular), description, location, articulation, number, common_name, appearsincrossec`.
34 illustrated bone ids are referenced across the cross-sections. `appearsincrossec` is again prose:
`"Ribs (1-5) - Chuck Arm A-F; Rib 7- Rib C; Rib 8 - Rib E; …"`.

### 1.5 The 3D is gone — measured

- Current nav (rendered): About, Muscles, Muscle Descriptions, Cross-Sections, Subprimal Descriptions,
  Muscle Profiling, Bones, Bone Descriptions, Skeleton, Fabrication Videos, Glossary. **No 3D item.**
- `https://bovine.unl.edu/bovine3D` → **HTTP 404** today.
- Wayback CDX (`http://web.archive.org/cdx/search/cdx?url=bovine.unl.edu/bovine3D*&…`, 1,127 rows)
  shows the old section: mimetypes **168 × `application/x-shockwave-flash`, 4 × `application/x-director`**,
  271 GIF, 187 JPEG, 154 TIFF, 210 HTML.
  The Director/Shockwave files are `bovine3D/eng/3did.dcr`, `bovine3D/animations/3did.dcr`,
  `bovine3D/animations/3did.dir`, `bovine3D/eng/3D_progbar.dcr`.
- **When it died, measured** (`awk '{print substr($1,1,4), $3}' cdx-b3d.txt | sort | uniq -c`):
  HTTP-200 captures run **2004 → 2011-08-12** (748 of them in 2010 alone); from **2012 onward every
  capture is 404**, and from 2021 they are 301 redirects. **`/bovine3D` served content 2004–2011 and
  was gone by 2012.** (A 2015 `.swf` hit elsewhere in the Wayback index —
  `animations/subprimals/130.swf` — is *not* under `/bovine3D`; the subprimal rotation Flash outlived
  the 3D section.)
- The archived index (`http://web.archive.org/web/2007id_/http://bovine.unl.edu/bovine3D/eng/index.jsp`)
  lists a nav that the live site no longer has: *Introduction, Development, **3D Rotation**, **3D Muscle
  ID**, Fabrication Videos, Skeleton, Cross-sections, Lateral Views, Sub-primals, Bone Descriptions,
  Muscle Descriptions, Muscle Profiling Database, Graphs/Charts, Glossary, Credits.*
- Earliest capture of the domain **2002-03-28**; `/bovine3D` captures run 2004 → ~2015; latest domain
  capture 2025-03-31. Legacy JSP ids (`ShowSubPrimal.jsp?primal_id=965938774`) match the `legacy_id`
  values still present in today's `subprimals` JSON — same database, re-platformed.
- **Conclusion: `bovine.unl.edu` was interactive-3D from 2004 to 2011 via Shockwave 3D; the section
  404'd from 2012 and is absent from the rebuild (current DB records are stamped `2020-11-16`). The
  live site is 2D photos, image-map polygons, and tables.**

### 1.6 The 3D paper

`https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/1186107.1186134` returns:

> **"A novel way to study muscle anatomy of the beef animal"** — Vishal Singh, Ashu Guru, Bucky
> Gwartney, Steven J. Jones. **SIGGRAPH, 2004.** DBLP `conf/siggraph/SinghGGJ04`.
> `openAccessPdf: {"url": "", "status": "CLOSED"}`.

**UNPROVEN / BLOCKED:** `https://dl.acm.org/doi/pdf/10.1145/1186107.1186134` → **403**, and
`https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1101&context=rangebeefcowsymp` → **403**
(both to `curl` with a browser UA). I did **not** read the paper. The method description quoted in
search-engine snippets (CT scan at 7 mm increments, per-slice outlining, surface rendering, reassembly
in NewTek Lightwave 3D) is **not verified against the primary source** and should not be repeated as
fact. A separate ResearchGate item, *"The 3D bovine and porcine myology system"*, was **seen only as a
search result** and is likewise unverified.

### 1.7 Licence

**No licence statement found.** `/about` gives a citation request and a credits list; the site footer
is the standard UNL framework footer (`Copyright 2026`, UNL Web Developer Network). The
`muscles.json` endpoint serves without auth but carries no licence. **Treat as all-rights-reserved
unless UNL says otherwise.**

### 1.8 Known broken bits (recorded, not inferred)

- `https://bovine.unl.edu/muscles` renders only a heading: no XHR fires, no muscle content. The
  *Muscle Descriptions* page is the one that loads `muscles.json`.
- `https://bovine.unl.edu/sitemap.xml` → 404. `/muscles/1`, `/bones/1` → 404 (no per-entity routes).
- `/cross-sections/12` and above → HTTP 500.

---

## 2. UNL Porcine Myology — `https://porcine.unl.edu/` — **LIVE, but no cut mapping**

Same platform, same nav. `porcine.unl.edu/muscles.json` → **404**; instead
`https://porcine.unl.edu/muscle-descriptions` (152,779 bytes) inlines `var muscles`.

- **110 muscles.** Fields: `name, common_name, group, origin, insertion, innervation, blood_supply,
  action, notes, id`.
- Non-empty: name 110, origin 110, insertion 110, action 109, innervation 107, blood_supply 106,
  group 108, common_name 46, notes 2.
- **There is no `retail_cuts` field, no `primal`, no `appearsInCrossec`, no profiling data.**
  Feature 3 is absent for pork.
- Data-quality tell: porcine muscle #1 `Adductor` has `common_name: "Inside round"` — a **beef** retail
  term — and origin/insertion prose identical to the bovine record. The pork records appear to be
  cloned from the bovine ones.
- Print ancestor, cited on the bovine `/about` reference list: **Jones, S.J. and Burson, D.E.,
  *Porcine Myology*, National Pork Producers Council, Des Moines, IA, 2000.** Not fetched.

**`https://porcine.unl.edu/about`, read** — it is richer than the muscle table suggests and names a
second print ancestor:

> *"The cross-sectional views follow the design of the porcine myology publication of **R.G. Kauffman
> and L.E. St Clair in Bulletin 715 "Porcine Myology" published in 1965 by the University of Illinois
> College of Agriculture Agricultural Experiment Station**."*

- Two 180-lb carcasses. Cross-sections labelled **A through DDD** (body) and **EEE through VVV**
  (thoracic limb) — a far finer slice series than the bovine site's 11 sets.
- A **six-layer lateral dissection**, with the muscles removed at each layer listed by name in prose
  (layer 5 alone removes 17 named muscles). Same layer-peeling idea as bovine sets 10/11.
- Funded through the **Pork Checkoff / National Pork Board**; built by UNL Animal Science (Steven
  Jones), IANR Media and the Raikes School (Ashu Guru, Brady Sullivan, **Derek Von Seggern**, Ethan
  Johnson); *"Muscle Profiling Data Furnished By"* Dong Ahn, Steven Lonergan and Ken Prusa (Iowa
  State) — i.e. the Buege et al. pork data of §6.1.
- **But none of that profiling data, and no cut field, is exposed in the `var muscles` payload.** The
  pork site is the beef site's skeleton with the meat-industry layer left out.

`ovine.unl.edu`, `lamb.unl.edu`, `bovine3d.unl.edu` — **all fail to resolve** (curl exit 000). No lamb
equivalent at UNL.

---

## 3. The French Meat Academy SKOS thesaurus — **FOUND. Open loop from the earlier round closed.**

The earlier survey (`landscape.md` "Open Loops", `research-method.md`) recorded this as *"the SKOS file
could not be located… would be the single best structured prior art if the file can be found."*
It is:

- **AgroPortal `MEAT-T`** — `https://agroportal.eu/ontologies/MEAT-T`
  (the old `agroportal.lirmm.fr` host now 302s to `agroportal.eu`)
- Title **Meat Thesaurus (MEAT-T)**, format SKOS
- **Metrics as AgroPortal reports them: 2 classes, 1,505 individuals (= SKOS concepts), 0 properties**
- Last submission **2022-02-13**
- URI `http://opendata.inrae.fr/ThViande/MeatThesaurus`; concept URIs `…/ThViande/C853`
- Description: *"derived and adapted from the Dictionnaire de la viande, Académie de la viande
  (France). Publisher, Autres voix, 2012. ISBN 2918237086"*; terms and definitions in **French and
  English**
- DOI **`10.15454/PB5QXC`**, resolving to Recherche Data Gouv (INRAE Dataverse),
  `https://entrepot.recherche.data.gouv.fr/citation?persistentId=doi:10.15454/PB5QXC`
- **Licence: `etalab 2.0`** (`https://spdx.org/licenses/etalab-2.0.html`) — i.e. **open**
- Authors on the Dataverse record include **Kombolo, Moise** and **Hocquette, Jean-François** (INRAE);
  contact `vocabulaires-ouverts@inrae.fr`; published 2022-02-22, last updated 2025-08-11

**Concept-count discrepancy, stated rather than smoothed:** the brief says 1,519; the *Meat Science*
paper abstract as surfaced in search says **1,567**; AgroPortal's deposited submission measures
**1,505**. Three numbers, one resource. AgroPortal's is the one I measured directly.

### 3.1 Getting the file — partially blocked

- The **Dataverse record contains zero files.** `https://entrepot.recherche.data.gouv.fr/api/datasets/
  :persistentId/?persistentId=doi:10.15454/PB5QXC` returns `"files": []`, and
  `…/api/datasets/125094/versions/:latest/files` returns `{"status":"OK","data":[]}`. It is a
  metadata-only record pointing at AgroPortal.
- The AgroPortal REST API requires a key: `https://data.agroportal.eu/ontologies/MEAT-T/metrics`
  → **401**, *"You must provide an API Key… obtained by logging in"*. I did not create an account.
- `http://opendata.inrae.fr/ThViande/C707` → **does not resolve** (curl 000).
- The INRAE Skosmos instance `https://consultation.vocabulaires-ouverts.inrae.fr/rest/v1/vocabularies`
  lists only **three** vocabularies — `disciplines-scientifiques`, `thematiques-numeriques`,
  `thesaurus-inrae`. **The meat thesaurus is not there.**
- **Status: the resource is located, identified and openly licensed; the raw SKOS file is behind a free
  AgroPortal account. Downloading it is a five-minute job for a human with a login.**

### 3.2 And it does not do feature 3 — measured

AgroPortal's search is server-rendered, so it can be queried without a key:
`https://agroportal.eu/search?q=<term>&ontologies=MEAT-T&pagesize=150`, counting distinct
`ThViande/C\d+` ids in the returned HTML.

| query | MEAT-T concepts matched | what came back |
|---|---|---|
| `longissimus` | **0** | — |
| `anatomie` | **0** | — |
| `morceau` | **0** | — |
| `muscle` | 4 | *conversion of muscle into meat*, *lean meat percentage*, *muscle contraction* — **no named muscles** |
| `faux-filet` | 18 | tenderloin of beef/pork/veal, chump, contrafilet, shortloin tip, lamb loin chop … |
| `découpe` | 8 | Forequarter, Hindquarter, *pièce de découpe*, primal pork cuts, secondary pork cuts |
| `bavette` | 4 | flank steak, loin skirt, skirt for pot-au-feu |
| `rumsteck` | 2 | rump cap |

Positive control passes (cut queries return plenty), so the zero on `longissimus` is real.
**MEAT-T is a bilingual cut-and-process terminology with definitions. It has cut concepts and it has no
muscle concepts, therefore it cannot relate the two.** It is excellent prior art for the *naming* layer
(feature 1's vocabulary), and none at all for feature 3.

*(The other INRAE hit, `thesaurus-inrae` on Skosmos, is a general research thesaurus — `beef cattle` is
a concept in it. Not a cut resource.)*

---

## 4. Print ancestors named by UNL's own reference list

From `https://bovine.unl.edu/about` — this is the bibliography the only real feature-3 resource was
built on, so it is worth recording verbatim in outline. **None of these were fetched; they are recorded
as leads, not as verified claims.**

- **Tucker, H.Q., Voegeli, M.M., and Wellington, G.H. *A Cross Sectional Muscle Nomenclature of the
  Beef Carcass*. Michigan State College Press, East Lansing, MI, 1952.** — on its title alone the
  oldest direct ancestor of feature 3 found in this thread. **Worth chasing.**
- Jones, S.J. and Burson, D.E. *Porcine Myology*. National Pork Producers Council, 2000.
- *The Meat Buyers Guide*, North American Meat Processors Association (NAMP, now NAMI), 1997.
- **Nomina Anatomica Veterinaria**, World Association of Veterinary Anatomists, 1994.
- Popesko, P. *Atlas of Topographical Anatomy of the Domestic Animals*, 2nd ed., vols 1–3, 1977.
- Getty, R. *Sisson and Grossman's The Anatomy of the Domestic Animals*, 5th ed., vols 1–2, 1975.
- Sisson, S. *The Anatomy of the Domestic Animals*, 4th ed., 1953.
- **Swatland, H.J. *Meat cuts and muscle foods*. Nottingham University Press, 2000.** — already an open
  loop in `landscape.md`; UNL cites it, which raises its priority.
- *Research in Motion — Muscle Profiling*. UNL and Univ. of Florida, NCBA, Denver, 2000.

Note what the list tells you: **the veterinary-anatomy side (NAV, Sisson/Getty, Popesko) and the
butchery side (Meat Buyers Guide, IMPS) are two separate literatures, and Bovine Myology is the place
they were joined.** That join is the thing this repo is also doing, and the fact that it took a
Checkoff-funded university program to do it once, for one country, is the strongest available evidence
for how rare it is.

---

## 5. The Calkins / Von Seggern muscle-profiling program — its other outputs

*(The project already uses the Calkins & Sullivan "Common Names for Beef Muscles" fact sheet —
`data/composition/calkins-table.md`. This section is deliberately about everything else the program
produced.)*

### 5.1 The paper

Crossref `https://api.crossref.org/works/10.1016/j.meatsci.2005.04.010`:

> **Von Seggern, D.D., Calkins, C.R., Johnson, D.D., Brickler, J.E., Gwartney, B.L.** "Muscle
> profiling: Characterizing the muscles of the beef chuck and round." ***Meat Science* 71 (2005)
> 39–51.** DOI `10.1016/j.meatsci.2005.04.010`.

Crossref carries no abstract for it and I did not read the full text (Elsevier). A Crossref
bibliographic search on `muscle profiling characterizing the muscles` returned exactly **one** paper in
this series — there is no visible companion "…of the beef loin/rib" paper. Adjacent Nebraska/Checkoff
outputs that surfaced: *"Effect of muscle location, fiber direction, and slice thickness on the
processing characteristics…"* (Meat Sci 2008, `10.1016/j.meatsci.2007.06.024`); *"Retail yields from
beef chuck and round subprimals…"* (J Anim Sci 2003, `10.2527/2003.8161482x`).

### 5.2 The Checkoff's own summary — 39 muscles, and the atlas is the delivery vehicle

`https://www.beefresearch.org/resources/product-quality/fact-sheets/muscle-profiling`, which links
`https://www.beefresearch.org/Media/BeefResearch/Docs/muscle-profiling-overview_10-28-2020-76.pdf`
(127,230 bytes, extracted with `pdftotext -layout`):

> *"Checkoff-funded research was conducted to profile the physical and chemical characteristics of **39
> beef muscles**…"*
> *"…the **infraspinatus**, or top blade muscle, is the second most tender muscle in the carcass if its
> inherent connective tissue is managed correctly. This knowledge resulted in the development of the
> successful beef Flat Iron Steak."*
> *"Individual muscle data is shared through an interactive Web site hosted by the University of
> Nebraska-Lincoln (http://bovine.unl.edu). This Web site … receives more than 2 million hits per year
> from users around the globe."*

**The count closes the loop: the fact sheet's 39 profiled muscles and the 39 muscles carrying a `pH`
value in `muscles.json` are the same number.** *Membership is not proven identical.* Von Seggern's
title says chuck and round; the 39 `pH` muscles carry `primal` strings of Chuck 17, Round 6,
`"Chuck, Rib"` 6, `"Round, Loin"` 5, plus single Loin / Brisket / three-primal entries. Predominantly
chuck and round, with edge muscles spanning into rib and loin — but I did not read the paper's muscle
list, so treat the set as *consistent with*, not *verified as*, Von Seggern's. The paper, the fact
sheet and `bovine.unl.edu` are three faces of one programme, and the website is the machine-readable
face.

### 5.3 …and the consumer-facing sibling drops the anatomy entirely

`https://www.beefitswhatsfordinner.com/cuts/cut/2851/flat-iron-steak` (same Checkoff funder, the
consumer cut database): the page says **"Top Blade"** 11 times and the word **"muscle" exactly once**;
**`infraspinatus` appears zero times.** The anatomy survives only in the research-side resource.

---

## 6. Pork and lamb

### 6.1 Pork muscle profiling — 25 muscles, no cut mapping

`https://meatscience.org/docs/default-source/publications-resources/rmc/2003/pork-muscle-profiling(3).pdf?sfvrsn=2`
(98,907 bytes, 2 pages; AMSA 56th Reciprocal Meat Conference 2003, pp. 51–52):

> **Buege, D.R.**, Sebranek, Doumit, Marple, Ahn, Huff-Lonergan, Lonergan, Fedler, Prusa, Helman,
> Meisinger. "Pork Muscle Profiling."
> *"…the chemical, physical and nutritional evaluation of **25 significant shoulder and ham muscles**…"*
> Iowa State + Michigan State + Wisconsin, funded by the **National Pork Board**. 64 carcasses.
> Muscles ≥ 0.5 lb evaluated for weight, dimensions, pH, sensory, tenderness, colour, water-holding,
> protein solubility, gel strength, pigment, collagen, nutrients.

This is muscle → **properties**, the pork analogue of Von Seggern. It is **not** muscle → cut.

Related pages fetched: `https://porkcheckoff.org/research/pork-muscle-profiling-study/` (200) and
`https://porkgateway.org/resource/pork-muscle-profiling-determining-the-properties-of-individual-ham-and-shoulder-muscles/`
(200).

### 6.2 Porcine Myology — see §2. 110 muscles, **no cut field**.

### 6.3 Lamb — nothing found

No `ovine.unl.edu`. No lamb muscle-profiling programme surfaced. The only lamb item in this thread is
Interbev's lamb cutting poster (§7), which carries no anatomical names.

---

## 7. France and other national muscle atlases

### 7.1 Interbev / Institut de l'Élevage cutting posters — muscle-level, but **not anatomy-keyed**

`https://www.interbev.fr/ressource/posters-de-decoupe-de-carcasses-de-boeuf-veau-agneau-cheval/`.
Eight PDFs, free: beef (avant `Poster2-BOEUF-AVANT.pdf` 546,832 B; arrière `Poster3-BOEUF-ARRIERE.pdf`
584,766 B), veal (2), lamb (1), horse (3). Interbev's own framing:

> *"…les demies carcasses sont découpées en pièces de gros, qui sont elles mêmes ensuite découpées et
> séparées en **muscles**. L'objectif … est triple : **localiser les différents muscles d'une
> carcasse**, identifier la diversité de muscles présents … et connaître la destination culinaire de
> chacun des morceaux."*

So the *intent* is feature 3. The execution is not: `pdftotext` over all three beef/lamb posters finds
**zero** occurrences of `longissimus|semitendinosus|semimembranosus|biceps femoris|infraspinatus|
psoas|gluteus|rectus` (poster word counts 101, 140, 83 — they are photo posters with labels). Every
label is a **French butcher name** — *araignée, merlan de cuisse, poire, rond de gîte, aiguillette
baronne, bavette d'aloyau* — which are single-muscle cuts but are not anatomical terms and carry no
Latin key. A French reader learns which lump of meat is which; nothing connects it to a muscle name.

`https://idele.fr/detail-article/posters-de-decoupe-de-carcasses-de-boeuf-veau-agneau` is behind a
"haphash" JS bot-check (5,349 B, no content) — **BLOCKED**, but the Interbev copy of the same
collaboration is open, so nothing is lost.

### 7.2 *Recueil des connaissances sur la qualité des viandes bovines* (Interbev CVL) — incidental only

`https://interbev-cvl.normabev.fr/_medias/CVLO/documents/recueil-des-connaissances-sur-la-qualite-des-viandes-bovines.pdf`
— 12,792,200 bytes, **89,602 words extracted**. Latin muscle names appear on **11 lines out of 10,000+**,
and every one is a figure legend or an aside, e.g. a chart key reading:

> *Longissimus dorsi : Faux-filet · Gluteus medius : Rumsteak · Semi tendinosus : Rond de Gîte ·
> Tensor fasciae latae : Bavette d'aloyau*

**Four equivalences in a graph legend.** That is the extent of systematic Latin↔French cut keying in a
90,000-word national reference on beef quality. A strong measured negative for France.

### 7.3 Japan — one hobbyist resource, and it is genuinely feature-3-shaped

`https://dolikyou.com/焼肉の解剖学｜焼肉の部位を獣医学生が解説/` (2021) — *"I pulled out the anatomy
textbook and looked up which muscle each yakiniku cut corresponds to."* Written by a veterinary
student. Measured: **30 `筋肉名：` (muscle-name) assignments**, grouped by the trade's four divisions
(まえ / ロイン / ともバラ / もも) plus organs, e.g. ザブトン → 僧帽筋 (trapezius), ミスジ → 棘下筋
(infraspinatus), トウガラシ → 棘上筋 (supraspinatus). **Nine downloadable PDFs**
(`焼肉部位-体幹.pdf`, `焼肉部位　後枝.pdf`, `部位一覧.pdf`, …).

Caveats: hobbyist, one tradition, static images, and the author flags his own uncertainty — several
entries carry `(?)` or `など` ("etc."), e.g. 菱形筋…板状筋(?)、半棘筋(?). Still, **this is the only
non-US resource found in this thread that actually assigns anatomical muscle names to a national cut
vocabulary**, and it took a vet student with a textbook to do it.

---

## 8. Veterinary nomenclature — the naming authority, and it contains no cuts

**Nomina Anatomica Veterinaria, 6th edition (2017)**, ICVGAN / World Association of Veterinary
Anatomists. **Free**: `http://www.wava-amav.org/downloads/nav_6_2017.zip` (1,899,237 B zip →
`NAV, 6th EDITION, 2017. Complete version.pdf`, 3,848,574 B, **178 pages**).

Measured on the `pdftotext -layout` extraction (53,080 words, 10,086 lines):

- **157 distinct `M. <name>` muscle terms** (an undercount — plural `Mm.` entries and indented
  sub-entries are not all captured by that pattern). There is a full `MYOLOGIA` section; `M. longissimus`
  appears with its lumborum / thoracis / cervicis / atlantis / capitis subdivisions.
- **`steak`, `brisket`, `sirloin`, `retail cut`, `butcher` — 0 occurrences, combined.**

**NAV is the name authority for one side of the join and says nothing whatsoever about the other.**
That is the structural gap feature 3 sits in: NAV names the muscles, IMPS/URMIS/BS/GOST name the cuts,
and nothing official relates them.

**Budras, *Bovine Anatomy: An Illustrated Text*** (2nd ed. 2011, Schlütersche, ISBN 9783899930528) —
**UNVERIFIED.** Only bookseller and publisher blurbs were reachable; they describe a topographical +
systems veterinary atlas (bones, joints, muscles, organs, vessels, nerves, lymph nodes per body part)
and **make no mention of meat cuts or butchery**. I did not see a table of contents. Treat "Budras does
not map cuts" as *likely but unproven*.

**Two targets from the brief that this thread did NOT clear — stated so nobody assumes otherwise:**

- **Gerrard & Mills** — **not searched.** No claim either way.
- **NAMI / AMI (formerly NAMP) muscle atlases and *The Meat Buyers Guide*** — **not fetched.** The 1997
  edition is cited in UNL's own reference list (§4), which makes the Meat Buyers Guide an *input* to
  Bovine Myology rather than a competitor to it; but whether any NAMI publication tabulates muscle→cut
  in its own right is **unverified and open**.
- **Swatland** is covered in `notes/notes-english-cross-country.md` and left there. UNL cites *Meat
  cuts and muscle foods* (2000) in its bibliography, which raises its priority as an open loop but adds
  no measured fact to this thread.

---

## 9. Muscle-keyed databases for meat animals — the UBERON/FMA analogue does not exist

- **UBERON** (`https://obofoundry.org/ontology/uberon.html`) is the multi-species anatomy ontology
  (~6,500+ classes) and does contain muscles species-neutrally. **It has no butchery layer**, and no
  resource was found that binds UBERON (or any OBO ontology) terms to meat cuts.
- **AGROVOC** `meat cuts` was already measured in the earlier round: 7 narrower concepts, stops at
  "steaks"/"chops" (`notes/notes-structured-food-sources.md`).
- **MEAT-T** — §3. Cuts, no muscles.
- **`bovine.unl.edu/muscles.json`** — §1. The *only* machine-readable muscle↔cut artefact found in this
  entire thread, and it is a flat string field in an unlicensed JSON on a university web server.

**No FMA/UBERON-equivalent muscle-keyed database exists for meat animals with a cut layer attached.**

**The human analogue does exist, which sharpens the contrast.** `https://lifesciencedb.jp/bp3d/`
(**BodyParts3D / Anatomography**, DBCLS Japan) was observed directly in the browser this session: it
serves per-structure 3D `.obj` models **keyed to FMA concept IDs**, with `obj2FMA` / `FMA2obj` lookups,
filters for Bone / Muscle / Vessel / Internal, and a "show only TA matches" toggle against
*Terminologia Anatomica*. Licence on the page: **CC BY-SA 2.1 Japan**. So *"named anatomy, in 3D,
keyed to a controlled vocabulary, openly licensed"* is a solved problem — **for humans**. For cattle
there is no FMA, no BodyParts3D, and no open 3D model keyed to NAV.

---

## 10. The 3D question, across the field

| resource | 3D? | interactive? | status |
|---|---|---|---|
| `bovine.unl.edu/bovine3D` (2004–~2015) | yes — Shockwave 3D (`3did.dcr`) | yes | **dead**, 404, Wayback only |
| `bovine.unl.edu` today | no | partly (image maps, 16-frame rotations on 44 of 197 subprimals) | live |
| `porcine.unl.edu` | no | tables only | live |
| Interbev/Idele posters | no | no (PDF) | live, free |
| MEAT-T | n/a | browsable via AgroPortal | live, Etalab 2.0 |
| NAV 6 | no | no (PDF) | live, free |

Two further 3D items appeared **as search results only and were not verified** — a ResearchGate item
*"The 3D bovine and porcine myology system"*, and a commercial *3D Bovine Anatomy* product from
Biosphera (`biosphera3d.com`). A Semantic Scholar lookup for the former returned **HTTP 429**
(rate-limited). **UNPROVEN.** Note also `S0309174018304510`, *"A CT-image based pig atlas model and its
potential applications in the meat industry"* (Meat Science) — surfaced in search, **abstract not
fetched**, but on its title it is the closest thing to a volumetric livestock-cut model and is worth a
follow-up in the feature-4 thread rather than this one.

---

## 11. What this narrows, and what it strengthens

**Narrows.** The claim "nobody has done anatomy-keyed cuts" is **too strong and should not be made**.
UNL Bovine Myology did exactly that, in 2004, with Checkoff money, and it is still serving the data as
JSON today: 119 muscles, 91 with cut lists, 355 muscle→cut pairs, 1,830 dissection polygons, full
origin/insertion/innervation prose. Anyone auditing this repo who knows the field will know that site.
It should be cited, engaged with, and credited — not discovered later.

**Strengthens.** Every axis of it stops one step short of this repo's shape:

1. **One tradition.** All 85 cut names are US retail. No UK, FR, RU, BR, KR, JP. The French
   equivalent (Interbev posters) has no anatomical names at all; the French thesaurus (MEAT-T) has
   cuts and **zero** muscle concepts; the only Japanese equivalent is a vet student's blog post with 30
   assignments and question marks on several. **Nobody has crossed traditions on the anatomy key.**
2. **No shared coordinate frame.** UNL's geometry is 2D polygons in per-photograph pixel space, with
   no registration between the 143 layers and no cut boundaries in that space at all. The
   cross-section reference is a prose string (`"Round A - F"`). This repo's normalised cow frame is
   exactly the thing UNL does not have, and it is what makes quantified overlap (feature 2) possible.
3. **Keyed at primal granularity; text at every finer granularity.** To be precise, because this is the
   sentence most likely to be quoted: the cross-section layers *do* carry a real foreign key —
   `{"muscle_id": 39, "coords": "…"}` resolves into `muscles.json`, and since each cross-section set is
   named for a primal, UNL genuinely has a **keyed primal→muscle relation** (Chuck 37 distinct muscles,
   Loin 26, Round 26, Lateral Fore 39, Lateral Hind 34). What is *not* keyed is everything below the
   primal: `retail_cuts` is a delimited **string** with no cut table behind it, subprimal→muscle exists
   only inside verbatim IMPS **paragraphs**, and `appearsInCrossec` is **prose** (`"Round A - F"`). The
   relation this repo needs — cut ↔ muscle, at cut granularity, as data — is exactly the one left as
   text.
4. **The 3D was real and is gone.** Shockwave killed it. Rebuilding it in WebGL is not a novel idea —
   it is a **2004 idea whose runtime died**, which is a much better framing than pretending it is new.
5. **Not open.** No licence on `bovine.unl.edu`. MEAT-T is Etalab 2.0 but needs an AgroPortal login and
   has no muscles. NAV is free but has no cuts.

The honest sentence is: ***the muscle→cut join has been done once, well, for one country, in 2004, by a
university programme that has since lost its 3D and left the cut side as prose; and no one has done it
across traditions, in a shared coordinate frame, or as data at cut granularity.***

---

## 12. Open loops for whoever picks this up

1. **Tucker, Voegeli & Wellington, *A Cross Sectional Muscle Nomenclature of the Beef Carcass*,
   Michigan State College Press, 1952.** Cited by UNL. Oldest identified ancestor. Not located online.
2. **Download the MEAT-T SKOS file.** Free AgroPortal account at `agroportal.eu/account`; Etalab 2.0
   once you have it. Worth doing for the FR/EN cut vocabulary even though it has no muscles.
3. **SIGGRAPH 2004 paper** `10.1145/1186107.1186134` — ACM 403s automated fetching. The method (CT
   scan → per-slice segmentation → Lightwave) is directly relevant to this repo's build pipeline and is
   currently only a search-engine summary.
4. **Wayback the dead 3D.** `bovine.unl.edu/bovine3D/eng/index.jsp` had "3D Rotation" and "3D Muscle
   ID". The `.dcr` files are archived; seeing what they actually did would settle how close 2004 got.
5. **`Meat Science` S0309174018304510** — CT-based pig atlas model. Feature-4 thread.
6. **Budras TOC** — confirm or kill the "no cuts" assumption.
7. **UNL licensing.** `muscles.json` is served openly with no licence. If any of it is to be compared
   against or cited quantitatively, ask Ty Schmidt (`ty.schmidt@unl.edu`).

---

## Appendix: fetch log — what worked, what did not

| URL | result |
|---|---|
| `https://bovine.unl.edu/muscles.json` | **200, 1,390,225 B** — the find |
| `https://bovine.unl.edu/{muscles,bones,muscle-descriptions,profiling,subprimals,cross-sections,about,glossary,skeleton}` | 200 |
| `https://bovine.unl.edu/cross-sections/1…11` | 200; **12+ → HTTP 500** |
| `https://bovine.unl.edu/{sitemap.xml,bovine3D,muscles/1,bones/1,bones.json,subprimals.json}` | **404** |
| `https://porcine.unl.edu/{,muscles,bones,muscle-descriptions,cross-sections,skeleton,about}` | 200; `muscles.json` 404 |
| `ovine.unl.edu`, `lamb.unl.edu`, `bovine3d.unl.edu` | **do not resolve** (curl 000) |
| `web.archive.org/cdx/…bovine.unl.edu/bovine3D*` | 200, **1,127 rows** |
| `https://agroportal.eu/ontologies/MEAT-T` | 200 (JS-rendered; read via browser) |
| `https://agroportal.eu/search?q=…&ontologies=MEAT-T` | 200, **server-rendered — usable without a key** |
| `https://data.agroportal.eu/ontologies/MEAT-T/{metrics,latest_submission}` | **401, API key required** |
| `https://entrepot.recherche.data.gouv.fr/api/datasets/…PB5QXC` | 200, but **`"files": []`** |
| `https://consultation.vocabulaires-ouverts.inrae.fr/rest/v1/vocabularies` | 200 — meat thesaurus **absent** |
| `http://opendata.inrae.fr/ThViande/C707` | **does not resolve** |
| `https://hal.inrae.fr/hal-03711007` | **blocked — Anubis proof-of-work bot wall** |
| `https://dl.acm.org/doi/pdf/10.1145/1186107.1186134` | **403** |
| `https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1101&context=rangebeefcowsymp` | **403** |
| `https://idele.fr/detail-article/posters-de-decoupe-…` | **blocked — "haphash" JS bot-check** |
| `https://api.semanticscholar.org/graph/v1/paper/search?…` | **429 rate-limited** on the 2nd call |
| `https://www.interbev.fr/wp-content/uploads/2017/06/Poster{2,3}-*.pdf` | 200, free |
| `http://www.wava-amav.org/downloads/nav_6_2017.zip` | 200, free, 1.9 MB |
| `https://meatscience.org/docs/…/pork-muscle-profiling(3).pdf` | 200, free |
| `https://www.beefresearch.org/Media/BeefResearch/Docs/muscle-profiling-overview_10-28-2020-76.pdf` | 200, free |
| `https://ramcountrymeats.colostate.edu/links/` | 200 — its entire meat-resources link list is **`bovine.unl.edu` + `porcine.unl.edu`** |

**Method note.** `bovine.unl.edu` is client-rendered: `curl` of the HTML returns the UNL framework
chrome and nothing else, and `WebFetch`-style summarisation would have reported "a page about muscles".
The data was found by loading `/muscle-descriptions` in a real browser and reading the **network tab**,
which exposed `muscles.json`. Every count above was then computed with `json.load` over the raw file,
not read off a page. The subprimal and cross-section data is *not* in any `.json` — it is inlined in
each page as a `var …= [...]` inside a multi-hundred-KB `<script>`, recovered with a JSON
`raw_decode` at the assignment offset.
