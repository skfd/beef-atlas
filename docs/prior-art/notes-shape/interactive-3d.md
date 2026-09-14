# Shape thread 4 — interactive 3D / clickable-cut tools

**Summary.** Genuine WebGL 3D beef-cut viewers do exist, and the existing repo notes badly
under-describe them: **every 3D viewer on the open web is Japanese or Japanese-derived**, and the
two that matter were missed entirely. (3D outside the web is Western — BeefCuts3D is a German
native-iOS app, and the only Western 3D meshes are dormant Sketchfab uploads.)
**Toyonishi Farm's 牛肉3D部位解説** (`toyonishifarm.co.jp/prt_detail.php?c=…`) is a
real three.js r92 + OrbitControls + ColladaLoader viewer covering **95 parts** of one whole cow —
muscle cuts, **organs and bones shown inside a translucent carcass** — but one tradition (Japanese,
with English gloss names) and **no raycaster, so you cannot click the model**; you pick from a text
list. **"Beef Atlas | 3D Cuts Guide"** (iOS + a free web build at
`beefatlas.kittichoteshane.workers.dev`, shipped 2026-08-19 — note the *name collision* with this
project) is a tap-selectable GLB cow whose own catalog JSON declares `layer.skin / layer.skeleton /
layer.carcass / layer.cuts`, an isolation behaviour that "fade[s] skin and non-selected cuts to
reveal deep anatomy", **three partition views over one mesh** (Steakhouse 17 cuts / Yakiniku 39 /
Butcher 72), EN/JA/TH, and **62 typed cross-system relationships** across five `relationshipType`
values, each carrying a `terminologyConfidence`. Its geometry is explicitly
`reference.toyonishi.beef-viewer` — a modified Toyonishi-derived GLB. So three of this atlas's four
features have each been done in 3D somewhere, and *two* products have done several at once. What
nobody has done: **more than two or three partitions, none of them national traditions** (steakhouse
/ yakiniku / butcher are registers, not countries — no US-vs-UK-vs-France-vs-Russia-vs-Brazil-vs-
Korea on one animal anywhere), and **nobody quantifies overlap as a percentage** — the state of the
art is a five-value qualitative label. **Every Western national marketing-board cut tool is 2D** —
live DOM probes returned `canvas:0, webgl:false` on all of them: the US Checkoff benchmark is still
a 10-hotspot HTML image map, AHDB's "virtual" carcass is photographs with zero canvas elements,
Australian Beef and Certified Angus Beef are SVG/tile grids, and Nebraska's Bovine Myology — the
best anatomy-to-cut resource alive — is a 16-frame photographic turntable. GitHub has **zero**
open-source 3D beef-cut viewers across five queries, and Google Play **zero** 3D cut apps across
twelve locale/query combinations.

All checks below were run 2026-09-13/14. Method: `curl` with a desktop UA + grep for
`usemap|<area|<canvas|three|babylon|.glb|.gltf|model-viewer|sketchfab`, and for JS-heavy pages the
in-app browser running a DOM probe (`canvas` count, live `getContext('webgl')`, `THREE.REVISION`,
`svg path` count) plus `read_network_requests` for mesh files. Measured numbers are quoted; anything
not fetched is marked UNPROVEN.

---

## Grading table

| Tool | 3D? | Traditions on one animal | Anatomy under the cuts? | Live / last update | Free? |
|---|---|---|---|---|---|
| Toyonishi 牛肉3D部位解説 | **Real 3D** (three.js r92dev, WebGL canvas 724×700, ColladaLoader) | 1 (JP) + EN gloss name per cut | **Yes** — organs + bones rendered inside translucent body | Live | Free |
| Beef Atlas (kittichoteshane) | **Real 3D** (GLB served, 12,857 verts / 24,224 tris, 46 selectable entities; tap-to-select **declared, not observed rendering**) | **3 views** (Steakhouse/Yakiniku/Butcher) — registers, not countries | **Yes** — declared `layer.skeleton`, skin at opacity 0.16 | iOS v1.0 2026-08-20; web live; **no Android** | Free |
| BeefCuts3D (Uli Niklaus) | **Real 3D** (store copy: "Rotate and zoom the models") | 1 partition, **EN + DE names** | "Explore muscles, primal cuts and individual cuts" | v2.0 2026-09-10 | $4.99 |
| 全国食肉学校 FMA 3D contents | **Real 3D** (23 Sketchfab models) | 1 (JP) | Carcass/primal scans, no muscle layer | Live | Free |
| Sketchfab `UNLMeats` | **Real 3D** (24 IMPS subprimal scans) | 1 (US/IMPS) | No | 2017–2018 | Free |
| Nebraska Bovine Myology | **No** — 16-photo turntable | 1 (US/IMPS) | **Yes, best in class** — 119 muscles, 35 bones, cross-sections, layer-by-layer peel | Live | Free |
| Beef It's What's For Dinner | **No** — HTML image map | 1 (US) | No | Live | Free |
| AHDB Virtual Beef & Lamb | **No** — photographs, 0 canvas | 1 (UK); grading not cuts | No | Live, ©2026 | Free |
| Canada Beef carcass | **No** — SVG/HTML | 1 (CA), EN/FR **labels** | No | Live | Free |
| Australian Beef (MLA) | **No** — inline-SVG clickable carcass (236 paths, canvas 0) | 1 (AU) | No | Live | Free |
| Australian Butchers Guild | **No** — 17-hotspot image map | 1 (AU) | No | Live | Free |

---

## 1. Toyonishi Farm — 牛肉3D部位解説 ("Beef 3D part commentary") — THE 3D INCUMBENT

- https://toyonishifarm.co.jp/prt_detail.php?c=strip_loin (one page per cut)
- Standalone build: https://toyonishi-store.com/beef3d/index.html?part=suet
- Agency credit: http://nzambi.com/pf_detail.php?id=126 (スタジオザンビ / Studio Zambi)

**3D: proven, not inferred.** Browser probe returned `{canvas:1, sizes:["724x700"], webgl:true,
three:true, threeRev:"92dev"}`. Scripts served: `tools/three/three.min.js`,
`tools/three/OrbitControls.js`, `tools/three/Detector.js`, `tools/three/ColladaLoader.js`.
On-screen instruction: 「指先で360°視点を変えて動かすことができます」.
OrbitControls config read from the inline script: `enableRotate:true`, `enableZoom:true`,
`enablePan:false`, `enableDamping:true`.

**Scope: 95 distinct parts** (counted from `prt_detail.php?c=` links in the sidebar). The taxonomy
is the full Japanese trade hierarchy — 正肉 split マエ / ロイン / モモ / バラ, then 内臓 (offal:
タン, ホホ, ハラミ, サガリ, ハツ, レバー, ヒゾウ, フワ, ミノ, ハチノス, センマイ, ギアラ,
ショウチョウ, シマチョウ, モウチョウ, チョクチョウ, ヤン, テール, ウルテ, アキレス, メンブレン,
マメ, コブクロ, シビレ, ノドスジ), then 正肉・内臓以外 (鬼スジ, ケンネ脂, ゲンコツ).

**Anatomy under a translucent hide: YES.** Screenshotted directly. `?c=liver` renders the full
viscera set (rumen, intestines, liver, lungs, heart) inside a ghosted body; `?c=femur` (ゲンコツ)
renders the femur inside the same ghosted body. This is the exact visual idiom of this project's
feature 3, already shipped, in 3D.

**Traditions: one.** Japanese partition only. Each cut page prints an English gloss
(`英名：Strip loin、Sir-loin`) — **label translation, not a second partition**. It also names the
constituent muscles in prose (`主な筋肉／主に胸最長筋・背半棘筋` = longissimus thoracis +
semispinalis dorsi) but does not render muscles as selectable geometry.

**Two real limitations, both verified:**
1. **No click-on-model.** `grep -c 'aycaster'` over the page = **0**; zero click/mousedown handlers
   bound to `#canvas_main`. Selection is from the left-hand HTML list only. Rotate/zoom is all the
   mesh does.
2. **Not one scene — 95 pre-baked scenes.** The inline script loads
   `./src/dae/<partname>.dae` (verified 200 for `strip_loin`, `liver`, `femur`, `tongue`,
   `tenderloin`). A whole-cow `./src/cow_all.dae` exists (873,355 bytes, **1 geometry, 3 nodes** —
   one merged mesh) but its loader block is **commented out** in the shipped source. So there is no
   runtime selection model at all; each cut is a separate whole-carcass file with that part
   pre-coloured.

---

## 2. "Beef Atlas | 3D Cuts Guide" — THE CLOSEST COMPETITOR, AND A NAME COLLISION

- iOS: https://apps.apple.com/us/app/beef-atlas-3d-cuts-guide/id6796940694
- **Free web build (no login): https://beefatlas.kittichoteshane.workers.dev/**
- Seller Kittichote Kamalapirat, bundle `com.kittishane.beefatlas`, v1.0, released **2026-08-19**,
  updated 2026-08-20, **Free**, 2.97 MB, listed language EN, **0 ratings in every storefront
  checked** (us/jp/kr/br/fr/de/gb/ru/au).

**3D: proven.** Network trace on the web build: `GET /atlas/beef-atlas.glb → 200`
`Content-Type: model/gltf-binary`, plus `/atlas/atlas-catalog.json` (235,362 B) and
`/atlas/anatomy-metadata.json` (101,662 B). Probe: `{canvas:1, webgl:true}`. Store copy: "Tap
selectable regions on a 3D beef anatomy model", "Extract a selected cut for an isolated 3D view".

**It is built on Toyonishi.** Both JSON files state it outright:
`geometryReference.id = "reference.toyonishi.beef-viewer"`,
`productionTopology: "toyonishiDetailed"`,
note: *"This is the only anatomy topology in the project. Modified Toyonishi-derived GLB"*.
13 of its `sources` are Toyonishi cut pages plus MAFF's 牛肉・牛内臓の部位図鑑, JMI's glossary,
two yakiniku restaurant guides, and the NCBA 2021 foodservice/retail charts.

**Multiple partitions on one mesh: YES — three views, measured in the live app.**
Counts read off the running page:
- Steakhouse — **17 cuts** (Ribeye, NY Strip, Filet Mignon, T-Bone, Porterhouse, Cowboy, Tomahawk,
  Top Sirloin, Flat Iron, Hanger, Skirt, Flank, Tri-Tip, Chateaubriand, Short Ribs, Chuck Eye,
  Brisket)
- Yakiniku — **39 cuts** in 8 groups (Karubi/Rōsu menu families, Kata-Rōsu, Zabuton, Misuji,
  Sankaku-Bara, Kainomi, Harami, Sagari, Ichibo, Shinshin, Kamenoko, Tomosankaku, …)
- Butcher — **72 cuts**, hierarchical with parent regions and "Includes smaller cuts" children
- Catalog internals: 48 `cutConcepts`, 94 `anatomicalInstances` (left/right pairs → 47 distinct),
  62 `terms` (ja 40 / en 21 / th 1), 144 `localizations`, 55 `geometryMappings`,
  `expectedSelectableCutCodes: 44`, `statistics.selectableEntities: 46`,
  mesh 12,857 vertices / 24,224 triangles.
- **BUT the three views are registers, not countries.** `restaurantSystems: ["steakhouse",
  "yakiniku"]` — plus a butcher/trade base. `supportedLocales: ["en","ja","th"]`. There is no
  UK, French, Russian, Brazilian or Korean partition.

**Anatomy under a translucent hide: YES, declared.**
`layers: [{layer.skin, defaultVisible:true, defaultOpacity:0.16}, {layer.skeleton,
defaultVisible:false}, {layer.carcass}, {layer.cuts}]` and
`interaction.isolationBehavior: "Optionally fade skin and non-selected cuts to reveal deep
anatomy."` Skeleton exists as a layer but ships hidden by default; no named individual bones or
muscles found in the entity list (all 94 entities are `cut.*`).

**Cross-partition overlap: qualitative, NOT quantified.** 62 `relationships`, each
`{termId, targets[{conceptId, role}], relationshipType, terminologyConfidence, rationale,
sourceIds}`. **Measured histograms over all 62:**
- `relationshipType`: **exact 41, derived 12, approximate 5, broader 2, restaurantDependent 2**
- `terminologyConfidence`: **verified 53, supported 8, provisional 1**
- target `role`: core 57, component 14 — and 58 of 62 relationships point at exactly one concept
  (one points at 6, one at 3, two at 2), so even the many-to-many cases are rare.

Verbatim examples:
- `relationship.ribeye.exact` → `relationshipType:"exact"`, `terminologyConfidence:"verified"`
- `relationship.rosu.broader` → targets chuck_roll + ribeye + striploin, `"broader"`, `"supported"`
- `relationship.san_nok.approximate` → Thai สันนอก → striploin, `"approximate"`, `"provisional"`
- `relationship.ribeye_steak.derived` → role `"component"`, `"derived"`, `"verified"`

So: **five relationship types and three confidence grades — no percentages, no volume, no
geometry-derived overlap.** Two-thirds of the relations are plain `exact`; only 9 of 62 express any
imprecision at all. The app's own store text concedes it "identifies approximate and
restaurant-dependent relationships instead of presenting uncertain mappings as exact."

**Android: does not exist.** `play.google.com/store/apps/details?id=com.kittishane.beefatlas`
returns **HTTP 404** ("We're sorry… not found"). iOS + web only, so no download band is available;
iOS exposes only `userRatingCount`, which is 0 everywhere.

**Caveat:** in the in-app browser the GLB fetched 200 but the canvas rendered blank/white across
several waits; the App Store screenshots (`iphone-01-atlas.jpg`, `iphone-02-ribeye.jpg`) show the
rendered cow. Treat "the web build visibly renders the cow on ordinary hardware" as **UNPROVEN**;
everything else here is from the shipped data files and the live DOM.

---

## 3. BeefCuts3D — correcting the existing notes

https://apps.apple.com/us/app/beef-cuts-3d/id1535823789 — iTunes lookup API, verbatim:
`version 2.0`, `currentVersionReleaseDate 2026-09-10T21:48:53Z` (so "3 days ago" in the old notes
= **10 Sep 2026**), `releaseDate 2020-10-15`, `languageCodesISO2A ["EN","DE"]`, `price 4.99`,
`fileSizeBytes 764,305,408` (**729 MB** — consistent with real 3D assets), seller Uli Niklaus,
genres Food & Drink + Education, min iOS 15.0.

**Correction to `notes-apps-and-interactive-tools.md` and `notes-competitors-and-apps.md`:** both
say "4.0 from 1 rating". That is the **US** storefront only. Per-storefront `userRatingCount`:
**de 37**, br 4, us 1, au 1, and 0 in jp/kr/fr/gb/ru. So it has ~44 ratings worldwide, essentially
all German — a German-market app, not a dead one.

**Description evidence on the three questions** (full text captured):
- 3D: "Rotate and zoom the models… Select a piece on the animal or in the list to see its position,
  then open the detail view for a closer look from every angle." → real 3D, and it **does** support
  select-on-model, which Toyonishi does not.
- Anatomy: "Explore **muscles**, primal cuts and individual cuts", "Discover pork anatomy and cuts
  as well as beef in one interactive meat atlas". One screenshot is literally named
  `01-muscles-1320x2868.png`. So a muscle layer exists. Whether bones/organs do is UNPROVEN.
- Traditions: **one partition, two languages.** "common names and **synonyms**" + "English and
  German" — label translation. Two species (beef + pork), not two cutting systems.

---

## 4. 全国食肉学校 (Federal Meat Academy, Japan) — 3D teaching models

https://www.fma.ac.jp/3dcontents — page text: 「牛・豚などの枝肉や大分割を3Dで360度の角度から
見ることができます。実際に授業でも教材として使用しています。※外部サイトに遷移します」
("view beef/pork carcasses and primals in 3D from all 360°; actually used as teaching material in
class; links out to an external site").

Delivery is **23 outbound Sketchfab model links** harvested from the live DOM — slugs include
`ude-384011bd…` (ウデ, shoulder), `katarose-4f02721c…` (カタロース, chuck roll),
`rosehire-93f1723c…` (ロースヒレ, loin+tenderloin), `tomobara-7b64d36c…` (トモバラ, plate),
`momo-6bed45fc…` (モモ, round), plus ~18 hash-only slugs and one YouTube link
(https://youtu.be/hFaU5RI5X9Q). A vocational school publishing its primals as rotatable meshes —
**3D yes, one tradition (JP), no muscle/bone layer, no cross-country mapping.**

## 5. Sketchfab, measured

API sweep (`api.sketchfab.com/v3/search?type=models&q=…`) over `beef cuts`, `cow cuts`,
`beef carcass`, `butcher meat`, `meat cuts`: the field is overwhelmingly game props (cleavers, meat
hooks, horror butchers, PSX low-poly steaks). Only three clusters are real butchery reference:

- **`UNLMeats` / "UNLMeat Collections"** — https://sketchfab.com/UNLMeats — **24 models**,
  IMPS/NAMP-numbered beef subprimals with verbatim IMPS specification text as the description
  (e.g. *T.180, Beef Loin, Strip Loin, Split, Boneless*; *184-1, Beef Loin, Top Sirloin*;
  *119 E Brisket Boneless Deckle-on*; plus 107, 109, 109D, 112, 114E, 116B, 116D, 167A, 171C, 174,
  181, 191A, 207, 401A, 406, 412). **Separate meshes per cut, no shared carcass frame, no anatomy
  layer, US only, published 2017–2018, ~100–300 views each. Dormant.** This is the Nebraska group
  again (see §6).
- **`3dpadelt` — "Beef Half – Rinderhälfte – 3D Scan"** —
  https://sketchfab.com/3d-models/beef-half-rinderhalfte-3d-scan-6ac7ea9e92a246dda0806ce2b67684b4 —
  657 views, published 2025-12-19. A photogrammetry scan of a beef side. **No cut partition.**
- The FMA set in §4.

**Explicit negative: no Sketchfab model found that partitions one carcass into named cuts.**

## 6. Nebraska Bovine Myology — the anatomy benchmark, and it is 2D

https://bovine.unl.edu (sibling https://porcine.unl.edu, also live, 200).
Jones, Guru, Singh, Carpenter, Calkins & Johnson 2004, UNL Animal Science; contact now
Ty Schmidt. Sections: `/muscles`, `/muscle-descriptions`, `/cross-sections`, `/subprimals`,
`/bones`, `/bone-descriptions`, `/skeleton`, `/profiling`, `/fabrication-videos`, `/glossary`.

**Measured content** (embedded JSON + live DOM):
- **119 named muscles** in the Muscle Descriptions picker (Adductor → Vastus medialis), with a
  **Scientific Name / Common Name toggle**. (Counted from the live DOM: the picker's anchor list
  holds 204 links, of which 55 precede Adductor and 30 follow Vastus medialis as chrome/footer.)
- **35 bones** (`var bones = [...]`) each with `skeletal_division`, `description`, `location`,
  `articulation`, `common_name` ("Back strap", "Shoulder blade, blade bone, paddle bone") and
  **`appearsincrossec`** — e.g. Scapula → `"Chuck Blade G-Q"`, i.e. bones are keyed to cut
  cross-sections.
- **197 subprimals** across **7 primals** (`var primals` = Chuck, Rib, Loin, Round, Brisket/
  Foreshank, Plate, Flank), each carrying IMPS text and an `images[]` array.
- Each muscle page gives **Common Name and Wholesale Section**, e.g. Longissimus → Common Name
  "Ribeye, strip, Delmonico steak", Wholesale Section "Chuck, Rib, Loin". **That is cut-to-named-
  muscle keying, done in 2004.**

**3D: NO — and the About page says exactly how it was made.** DOM probe on `/muscle-descriptions`:
`{canvas:0, webgl:false, three:false, areas:0, usemap:0}`; one static JPEG per muscle
(`/images/muscles/17.jpg`). The site's own About text:
- Subprimals: *"photographed on a rotational table… These rotations involved **16 pictures, each
  rotating 22.5 degrees**"* → a 16-frame photographic turntable, not a mesh. (`spin` appears 23×
  in `/subprimals` markup, 9× in `/skeleton`.)
- Cross-sections: a 750 lb carcass sliced into **1-inch cross sections**, photographed, with
  diagrams colouring muscle red / bone pink / cartilage black.
- Lateral views: *"After each individual muscle was removed the carcass was photographed"* — i.e.
  **layer-by-layer muscle peeling already exists, photographically, per layer.**

So this project's "peel muscle layers" and "cutaway the near side" are both prior art in idiom —
executed as photography in 2004 rather than as geometry. US/IMPS only; no other tradition.

## 7. Western national boards — all 2D, all single-tradition

- **Beef. It's What's For Dinner** https://www.beefitswhatsfordinner.com/cuts — re-verified by curl
  2026-09-13: **still `1 usemap` + `10 <area>`**, zero canvas. The old note stands unchanged.
- **AHDB Virtual Beef & Lamb** https://virtualbeefandlamb.ahdb.org.uk — browser probe:
  `{canvas:0, webgl:false, svgPaths:0, three:false, babylon:false, imgs:6}`. Its own copy: *"The
  tool uses **images** and virtual livestock and carcases, to aid understanding of different
  classifications of fat and conformation"*. **Photographic grading trainer, not a cut atlas, not
  3D.** ©2026, maintained, offline mode offered. (Correction: the existing note's "viewed from
  every angle" should not be read as 3D.)
- **Canada Beef carcass** https://canadabeef.ca/carcass/ — 200, 4 `<path>`, no canvas/GLB. 2D.
- **Certified Angus Beef** https://www.certifiedangusbeef.com/en/cooking/cuts — **browser-probed**
  after render: `{canvas:0, webgl:false, three:false, areas:0, usemap:0, svgPaths:45, imgs:53}`.
  Its own copy: *"Discover Cuts by Primal. **Click on a primal tile** to see varieties of cuts."* —
  a grid of image tiles, not a diagram at all. **2D, US only.**
- **Australian Butchers Guild** https://www.australianbutchersguild.com.au/butchery/Beef-cuts-chart/
  — **`1 usemap` + `17 <area>`**: an image map with more hotspots than the US Checkoff's. 2D, AU.
- **Australian Beef (MLA)** — `/cuts/` is **404**; the live page is
  https://www.australianbeef.com.au/cooking/beef-cuts/. **Browser-probed** after render:
  `{canvas:0, webgl:false, three:false, areas:0, usemap:0, svgPaths:236, imgs:5}`. Its own copy:
  *"The primal cuts of the beef carcass… **Click on a cut below** to see information about the
  derived sub-cuts."* — an **inline-SVG clickable carcass** (the 236 paths), with carcase-percentage
  figures per primal ("two briskets per animal accounting for around **7.2% of the carcase**").
  **A good 2D tool, better than the US Checkoff's image map — but 2D, AU only.**
- **la-viande.fr** (Interbev) — homepage 200 (76 `<path>`, no canvas); `/sitemap.xml` returns
  **404** (no sitemap to enumerate), and guessed cut URLs `/decoupe-bovin` and
  `/decoupe-transformation/decoupe-bovins` both **404**. A French interactive cut tool remains
  **UNPROVEN** — three access routes tried, none reached one; not disproven.
- **carnebrasileira.com.br** — `curl` returned **HTTP 000** (connection failed). UNPROVEN.
- **ekapepia.com** (축산물품질평가원) 200 → `/v3/web/main.do`, 10,856 B, 0 `<path>`, no 3D signal;
  a guessed `/vi/meatPartInfo.do` redirects to `/v3/web/error.do`. **hanwooboard.or.kr** 200,
  2 `<path>`, no 3D signal; `/pages/hanwoo/part.html` 404. A Korean-language search
  (`소 부위 3D 인터랙티브 한우 부위별 그림 클릭`) returned only static guides and a
  blog-style reference to the official **한우 10 대분할 / 39 소분할** scheme
  (https://meat.8892-house.com/hanwoo-39-cuts/, 200). **No Korean interactive or 3D cut tool found.**
- **Brazil.** `carnebrasileira.com.br` and `www.carnebrasileira.com.br` both return **HTTP 000**
  (connection fails) — the domain appears dead. ABIEC's live site is https://abiec.com.br (200) and
  https://www.brazilianbeef.org.br (200); its cut reference is the **PDF** *Livro Brasileiro de
  Cortes Bovinos* (https://www.abiec.com.br/wp-content/uploads/ABIEC_LIVRO-DE-CORTES_COMPLETO.pdf),
  reported as covering 12 languages (PDF itself not opened — **UNPROVEN**). **No Brazilian
  interactive or 3D cut tool found.**

## 8. Open source — an emphatic negative

GitHub code search API, 5 queries: `beef cuts three.js` → **total_count 0**;
`meat cuts interactive 3d` → **0**; `beef carcass 3d viewer` → **0**; `cuts of beef webgl` → **0**;
`butcher webgl` → **1**, and that one is `KaiXGT2/ThePorkButcher_WebGL` ("The Pork Butcher | WebGL
Playable on browser", last push 2022-05-16) — **a game, not an atlas.**
There is no open-source interactive 3D meat-cut viewer.

## 9. App stores — 3D is nearly unoccupied

iTunes Search API across **us/jp/kr/br/fr/de/gb/ru/au**, terms `beef cuts` and `butcher`. Every
`*beef|meat|butcher|cut|steak|carne|肉|고기|viande|fleisch|мяс*` hit was enumerated. Findings:

- The **only two 3D cut apps that exist** are BeefCuts3D ($4.99, EN/DE, 2026-09-10) and Beef Atlas
  (Free, EN/JA/TH, 2026-08-20). Everything else is 2D reference, delivery, or games.
- `Handbook of Australian Meat` (AUS-MEAT) — https://apps.apple.com/au/app/handbook-of-australian-meat/id1577677255
  — 2025-11-03, free, 7 ratings, EN. **New to these notes**; the AUS-MEAT trade spec handbook. 2D
  reference, AU only (contents UNPROVEN, store metadata only).
- `Meat Cuts` (MLA) confirmed stale: 2023-11-06 across all storefronts; 8 ratings us, 12 au, 1 gb.
- `MyMeatUp` 2017-10-23 (44 ratings) and `Ask The Butcher` 2013-04-30 — both confirmed dead.
- **Non-English storefronts return no local cut-reference apps at all.** jp/kr/br/fr/ru queries
  surface the same English-language apps plus butcher-horror games. No Japanese, Korean, Brazilian,
  French or Russian national cut app exists on iOS.
- Note: **iOS exposes no download counts** — only `userRatingCount`. Play download bands were not
  re-swept in this thread (the existing notes cover them); Play-side 3D apps remain UNPROVEN beyond
  the already-recorded fact that BeefCuts3D's Android build 404s.

## 10. VR / AR / academic — two real systems, both single-tradition

- **Ritchie & Ho 2024, "Virtual reality-based meat cut planning for lamb carcasses"**, *New Zealand
  Journal of Agricultural Research* — DOI 10.1080/00288233.2024.2305825. tandfonline 403s to this
  agent; abstract retrieved verbatim via the Semantic Scholar API
  (`api.semanticscholar.org/graph/v1/paper/DOI:10.1080/00288233.2024.2305825`). Verbatim: *"A lamb
  carcass's **musculoskeletal model (or atlas)** is imported into an immersive virtual environment,
  created by a 3D VR engine (Unity3D). Virtual resection is performed by using a **virtual knife**
  operating on the virtual atlas **as per standard meat cut specifications of New Zealand**. The
  procedure yields **instant volume and weight information of each primary and retail meat cut**."*
  Hardware: Oculus Rift + hand motion sensor. **This is the closest thing found to quantified,
  geometry-derived cut measurement on a named-anatomy model** — but it is lamb, one tradition (NZ),
  a research prototype with no public build, and it computes volume/weight *per cut*, not **overlap
  between two traditions' cuts**. Nothing found suggests two cut specifications were ever run
  against the same atlas and compared.
- **Frontiers in Veterinary Science 2025, "Anatomy of meat cuts: integrating 3D scanning and virtual
  reality in veterinary education and training"** —
  https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2025.1680785/full
  (also PMC12590504). University of Sarajevo Veterinary Faculty. **12 beef cuts** scanned with an
  Einscan Pro 2X, published on Sketchfab, each with *"descriptive metadata including the name of the
  meat cut, the **constituent muscles** and the corresponding meat category, along with a diagram of
  its anatomical location"*; VR delivery via **Open Brush + HTC Vive Pro 2**, six cuts per station.
  Sketchfab account confirmed live: https://sketchfab.com/UNSA-VF — **24 models**, of which the meat
  cuts carry Bosnian names (*Ramstek cijeli*, *Cijeli But*, *Medaljon lažni biftek*, all published
  2025-04-17) and the rest are veterinary specimens (cow heart, kidneys, pig stomach, horse bones).
  **Separate scanned cut objects, no shared carcass frame, no partition of a whole animal, one
  tradition.**
- **Commercial VR butchery training: none found.** The only consumer product surfaced is
  *Butcher Simulator* on Steam (https://store.steampowered.com/app/3041780/Butcher_Simulator/) — a
  game, not a cut reference (store page not opened; **UNPROVEN** beyond the search listing).

## 11. Explicit negatives / not found

- **No tool anywhere shows two national traditions' cut boundaries on the same animal.** The only
  multi-partition product found (Beef Atlas) uses *registers* — steakhouse / yakiniku / butcher —
  not countries, and its own catalog lists exactly two `restaurantSystems`.
- **No tool anywhere quantifies overlap numerically.** The best that exists is a 4-value
  `relationshipType` × 3-value `terminologyConfidence` label.
- **No clickable 3D model with named muscles AND named bones AND multiple partitions.** Toyonishi
  has anatomy but one tradition and no click; Beef Atlas has click and partitions but its
  skeleton layer ships hidden and it names no individual muscles or bones; Nebraska has 119 muscles
  and 35 bones but is photographic and US-only.
- **Google Play: zero 3D beef-cut apps.** Twelve `curl`-with-browser-UA searches
  (`beef cuts 3d`, `meat cuts 3d anatomy`, `butcher 3d model cuts` × `hl=en/ja/ko/pt`,
  `gl=US/JP/KR/BR`), package ids extracted by regex. Across all twelve the only meat-cut result was
  `com.mla.meatcuts` (MLA, 2D, already in the notes); everything else was human-anatomy apps, 3D
  modelling tools, farm games and butcher-horror games. **No Android 3D cut viewer exists**, in any
  of the four locales.
- Adjacent-species 3D: only `porcine.unl.edu` (2D, same photographic idiom as bovine), BeefCuts3D's
  pork model, FMA's pork primal scans, and the Ritchie & Ho lamb VR prototype. **No 3D chicken or
  fish cut explorer found**; no adjacent-species tool shows more than one tradition either.
- `KaiXGT2/ThePorkButcher_WebGL` is the only WebGL butchery repo on GitHub and it is a game.

---

## Bottom line for the "unprecedented" claim

**Weakened on three of the four features, intact on the combination.**
- Feature 4 (interactive 3D, click a cut): **not unprecedented.** Toyonishi ships rotatable
  three.js; BeefCuts3D and Beef Atlas both ship select-on-model in 3D.
- Feature 3 (anatomy in the same frame under a translucent hide): **not unprecedented.** Toyonishi
  renders organs and bones inside a ghosted carcass today; Beef Atlas declares skin at opacity 0.16
  over a skeleton layer. What neither does is *name* 115 individual bones/muscles/organs as
  addressable entities — only Nebraska does that (119 muscles, 35 bones), and Nebraska is 2D.
- Feature 1 (many partitions in one shared frame): **partially anticipated.** Beef Atlas puts three
  partitions (17 / 39 / 72 cuts) over one GLB. But they are *registers* — steakhouse, yakiniku,
  butcher — drawn from essentially one US-plus-Japan vocabulary, and the catalog names exactly two
  `restaurantSystems`. **Seven national traditions on one frame remains unmatched, and 153 cuts is
  larger than any partition set found (Toyonishi 95, Beef Atlas butcher 72, Nebraska 197 subprimals
  but 2D and single-tradition).**
- Feature 2 (quantified overlap): **still unoccupied, and it is the sharpest differentiator.** The
  state of the art is Beef Atlas's five-value `relationshipType` (exact 41 / derived 12 /
  approximate 5 / broader 2 / restaurantDependent 2) crossed with a three-value
  `terminologyConfidence` — and 41 of the 62 are plain `exact`, i.e. the schema barely exercises its
  own imprecision. Ritchie & Ho compute real per-cut volumes and weights, but only within one
  specification. **Nobody publishes "US short loin is 91% Russian тонкий край".**

Two practical consequences worth flagging beyond the research question: the name **"Beef Atlas"
is already taken** by a free iOS + web product shipped 2026-08-19, and that product's geometry is
openly declared as **Toyonishi-derived** — a provenance question this project will be asked about
if it uses any similar asset.
