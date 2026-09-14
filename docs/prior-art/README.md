# Prior art

Who else has tried to map one cut across several butchery traditions, how far they got, and what is
left. Research date **2026-09-13**; six parallel threads, everything traceable to a fetched page.

Read [`landscape.md`](landscape.md) for the survey. [`research-method.md`](research-method.md) says which
findings are solid and which rest on a blocked fetch. [`notes/`](notes/) is the raw per-thread output,
kept so every number stays traceable to the URL it came from.

## Read this first: what is new here, and what is not

**This atlas already uses most of the primary sources the survey found.** A grep of `data/` counts IMPS
160×, ABIEC 128×, AHDB 150×, JMGA 87×, UNECE 48×, GOST 34×, plus Interbev and AUS-MEAT. So the survey is
**not** news on the standards axis — treat those sections as confirmation and provenance, not discovery.

What the survey actually adds:

### 1. Nobody else has built what this repo has built
The survey's original conclusion was that an anatomy-keyed cross-tradition cut map was unbuilt. **That was
written without knowing this project existed, and this project is that thing** — 153 cuts across seven
traditions in one coordinate frame, over 115 named anatomical parts, with muscle-overlap percentages
between traditions. Nothing in the survey does the last part at all. The closest anyone comes:

| | What they do | Where they stop |
|---|---|---|
| **UNECE** | anatomy-defined cuts, numeric codes, **5-language index** (EN/FR/RU/ES/ZH) | prose and cutting lines; no muscle model, no overlap, PDFs behind Cloudflare |
| **AUS-MEAT HAM** | per-cut PDFs cross-walking HAM + UNECE + NAMP + NZ MSG + AHECC, with photos | one tradition; a crosswalk table, not a shared frame |
| **Swatland 2012** | US vs ten British/Scottish sources **with per-cut concordance scores** | a printed table; the only prior work that quantified partial equivalence at all |
| **Weidefleisch** | ~60 cuts keyed by code across de/at/ch/us/uk/fr/it | flat name register, no anatomy |
| **carneatlas.com** | ~10 countries, per-cut name tables, photo-ID, daily puzzle | names only, no codes, no anatomy; fish section unsourced |

**Swatland's concordance scores are the one piece of genuine methodological prior art** for what this repo
computes. Worth reading before defending the overlap percentages to anyone.

### 2. Two UNECE facts worth having
- Its species standards carry a **"Multilingual index of products"** in **English / French / Russian /
  Spanish / Chinese**, keyed by item number — verified in Bovine 2007, Bovine 2023, Ovine 2012. The 2023
  bovine index holds **89 item codes** and adds **WCO Harmonized System alignment**.
- The separate **UNECE Standard for Retail Meat Cuts** (2013/2016, EN/FR/RU, with photographs) maps retail
  names back to wholesale item numbers — *"Ribeye Steak, Boneless — UNECE source No. 2240 Cube Roll"*. If
  this atlas ever wants a retail layer above the primal layer, that mapping already exists.

Both required Wayback raw-asset URLs; `unece.org` 403s all automated fetching.

### 3. The expansion candidates, ranked by how ready the source data is
The atlas covers US, UK, France, Russia, Brazil, Korea, Japan. The survey found well-sourced material for
traditions it does **not** cover:

1. **Spanish-speaking traditions — the biggest gap and the best-sourced.** A **nine-column table**
   (Argentina, Spain, Brazil, Chile, Portugal, USA/UK, France, Germany/Switzerland, Italy) exists twice, as
   a 2003 Lexicool PDF and Argentina's **MAGyP** ministry glossary (2007). **IPCVA** publishes ~80 Argentine
   cuts. **SAG Chile** is the one country in the survey whose cut names are **fixed by law** — 33 cuts under
   NCh 1596, a closed official list. Mexico has no institutional source, but a distributor's blog does
   ~50 cuts across four Mexican regions.
   ⚠️ Before relying on either copy of the nine-column table: **they share an identical column set in the
   same order and may be one document.** Diff them.
2. **Germany / Austria / Switzerland — three traditions, not one.** The divergence is institutional:
   Germany follows DLG rules, Austria the **Wiener Teilung** descending from Vienna's 1873
   Qualifikationstabelle. `Hüftdeckel` (DE) = `Tafelspitz` (AT); the forequarter is *Bug* in Vienna but
   *Laffe* in Swiss German. **Weidefleisch's code-keyed register** already tabulates de/at/ch/us/uk/fr/it.
3. **Canada — bilingual and legally binding.** The **CFIA Meat Cuts Manual** is a single EN/FR document with
   names paired inline, and CFIA states they *must* be used on labels. Note Québécois French is a **third
   French naming dialect** built on American calques that no France-based source cross-references — relevant
   to the existing `cuts_fr.json`. **Canada Pork's CPI codes** are stable across a seven-language brochure
   set (EN FR ES JA KO ZH VI).
4. **Australia** — AUS-MEAT HAM, with free unlinked per-cut PDFs at `ausmeat.com.au/cutcodes/<NNNN>.pdf`
   carrying photos and the four-way code crosswalk.
5. **Italy** — see the warning below before attempting it.

### 4. One finding that bears on the data model
**A name→cut lookup is not a function, and Italy proves it.** *Cappello del prete* is only the terminal part
of the dorsal muscle in Turin but the whole muscle in Sciacca; *osso buco* is inner thigh in Milan and rear
hock in Sciacca; *fesa* is outer thigh in Bari and inner thigh in Sciacca. Sources also contradict each
other, and the unit of variation is arguably the **city**, not the region. Any Italian data needs a
per-claim source field. (The reported invariant: *filetto* means the same everywhere.)

Related, and already implicit in this atlas's percentages: **cuts are not coextensive across traditions**,
because the carcasses are not split the same way — US at the 12th/13th rib, Brazilian at the 5th/6th. The
only consumer source found that models this honestly grades each match **high / approximate / variable**
rather than asserting equality. Lhuissier (2002) makes the historical case that cut names are **contested
administrative artefacts, not natural kinds**.

### 5. Two folklore numbers, one wrong
- **Korea does not have ~120 named beef cuts.** The MFDS notice (고시 제2019-113호) 별표 1 footer reads
  `10개 부위 / 39개 부위 / 7개 부위 / 25개 부위` — **beef 10 primals + 39 sub-cuts = 49**; pork 7 + 25 = 32.
  Stable since 2015. Consistent with this repo's Korean transcription.
- **Japan's official list is small:** JMGA's beef partial-meat standard has **13** cuts, the retail quality
  standard **11** labels, pork **5**. The one Japanese source with real cut codes,
  **食肉標準商品コード**, reaches ザブトン-and-offal granularity with 5-digit IDs — and dates from **March 2002**.

### 6. Where the atlas could align outward
- **UNECE item codes** are the obvious stable external key; **GS1 Application Identifier (7002)** carries
  them in barcodes.
- **Wikidata is CC0 and gives 24–31 labels on notable cuts** — but it **structurally cannot express
  per-country naming** (country property on 2 of 54 items, 0 with an anatomical location, Mexican
  *arrachera* and Argentine *vacío* jumbled in one Spanish bucket). **This atlas could contribute what
  Wikidata lacks.**
- **FoodOn** has 409 beef classes and **zero non-English labels**. **Commons' 31 beef-cut diagrams are all
  freely reusable.** **Spanish Wikipedia has no cuts-of-beef article at all.**
- Do **not** copy from FoodSubs/Cook's Thesaurus — its terms explicitly forbid derivative works.

## Scope note
The survey was commissioned as prior-art research on **carneatlas.com**, a small anonymous site, so
`landscape.md` is framed around that site and covers **pork, lamb and fish** alongside beef. The fish
material (FishBase, FAO ASFIS, EU commercial designations) is out of scope for this atlas and kept only
because it is the clearest worked example of how far a naming dataset can be taken.
