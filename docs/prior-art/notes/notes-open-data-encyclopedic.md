# Notes: encyclopedic and open-data prior art (meat cuts)

Every number below was read off a page or API response the agent fetched. Fetch date 2026-09-13.
Unfetched items marked UNVERIFIED.

## 1. Wikipedia — "Cut of beef"
https://en.wikipedia.org/wiki/Cut_of_beef (pageid 5453492)

**Coverage:** 21 sections, of which **17 are country/region naming sections** covering ~22 countries —
American/Canadian, Argentine, Brazilian, a *merged* Irish/British/Australian/South African/NZ section
(five countries treated as one system), Colombian, Chinese, Dutch, Finnish, French, German, Croatian,
Italian, Korean, Polish, Portuguese, Russian, Turkish, plus a UNECE section.

**Cross-language equivalence tables: ZERO.** Wikitable markup `{|` occurs **0 times** in all 24,030
characters of wikitext. The article is per-country prose definition lists (`; term : gloss`). No
structure maps a cut across countries. No other en-wiki article tabulates cuts across countries.

**Quality:** carries `{{Refimprove}}`, 1 `{{citation needed}}`, and only **15 `<ref>` tags for 22
countries**. Country sections cited to `rodiziodirectory.com`, `alimentipedia.it`, `clovegarden.com`,
`livestrong.com`, and **a bare JPEG** (`ipcva.com.ar/files/Cortes%20Blanco.jpg`). **Not a reliable
reference work.**

**Diagrams:** 19 images, ~12 substantive. Country diagrams for **10 of 22 covered countries**. Licences
on those 12: CC BY-SA 3.0 x6, PD x3, CC0 x2, CC BY 3.0 x1 — **all reusable**. 8 SVG / 4 PNG. Several
old (France 2010, US 2012, Brazil/Portugal 2013).

**Interlanguage versions: 14** (de, eu, fa, fr, it, ko, nl, pcd, pt, ru, sv, uk, vi, zh) — **and the 14
is badly inflated:**
- `zh` is a **19-character redirect** to a section of another article — no article
- `nl` (Runderlap, 1,173 chars) is about **one cut**, a mis-linked interwiki
- `sv` 1,740 · `uk` 2,701 · `pcd` (Picard) 2,941 chars — stubs
- `vi` is the **largest at 42,197 chars**, bigger than English, giving Vietnamese names for US cuts
- `de` 12,975 · `it` 8,103 · `pt` 7,240 · `fr` 4,644

**`de`, `fr`, `it`, `pt` all have 0 tables too.** German is organised by anatomy, not country, with 2
refs. French covers 9 countries, Italian 8, Portuguese only 2.

**There is no Spanish article at all** — es.wikipedia has `Carne de vacuno`, `Matambre (corte de
carne)`, `Filete (carne roja)`, but no cuts-of-beef article. **The single most striking gap, since
Spanish has the richest cut-name divergence.**

**Article-level depth is Anglocentric:** `Template:Cuts of beef` links **34 existing mainspace
articles** and **33 are English/US cut names**. Only **Picanha** is non-Anglo.

**Siblings:**
- **Cut of pork** — 11,361 chars, 24 refs, **0 tables**, revised 2026-08-28. Organised **by anatomy,
  not country**. Only regional content: one subsection "Iberian variants: presa and pluma". 6 interwikis.
- **Lamb and mutton** — 62 refs, revised 2026-09-08. Cuts section has only **3 country groupings**. Its
  one table is **sheep meat production tonnage**, not nomenclature.

Licence CC BY-SA 4.0; full MediaWiki API but the naming data is unstructured prose.

**vs CarneAtlas:** Wikipedia wins on beef country breadth (22 vs ~10) but has **no cross-country
mapping whatsoever**, no Spanish article, and cites blogs. For **pork and lamb it barely attempts
per-country naming at all.**

### Wikimedia Commons
**`Category:Beef cuts diagrams` does not exist.** The real ones:

| Category | Files | Subcats |
|---|---|---|
| Cuts of beef | 75 | 26 |
| **Cuts of beef diagrams** | **31** | 0 |
| **Cuts of beef by country** | 0 | **26 countries** |
| Cuts of pork | 76 | 19 |
| Cuts of pork by country | 0 | **13 countries** |
| Cuts of lamb | 28 | 7 |
| Cuts of lamb by country | 0 | **3 countries** |

26 beef countries: Argentina, Austria, Bangladesh, Brazil, China, Colombia, Czech Republic, France,
Germany, Greece, Hungary, Israel, Italy, Japan, Korea, Netherlands, Norway, Philippines, Poland,
Portugal, Russia, Shenzhen, Spain, Turkey, UK, US, Arab World. **Very uneven** — Korea 54 files, US 33,
Shenzhen 27, UK 18, Germany 12, but Spain/Poland/Russia/Turkey/Portugal/Netherlands 1 each.

**All 31 files in `Cuts of beef diagrams` enumerated:** PD 12 · CC BY-SA 4.0 6 · CC BY-SA 3.0 6 ·
CC BY-SA 2.0 2 · "No restrictions" 2 · CC BY 2.0 2 · CC0 1. **All 31 freely reusable.**

## 2. Wikidata — shallow and structurally unable to do the job
Endpoint https://query.wikidata.org/sparql via GET with `format=json`; all queries ran.

Class items: `Q2051651` cut of beef · `Q139960435` cut of meat · `Q6418247` primal cut. Confirmed
`ASK { wd:Q6418247 wdt:P279* wd:Q139960435 }` -> true. **There is no class item for "cut of pork" or
"cut of lamb".**

- `?i wdt:P31/wdt:P279* wd:Q2051651` -> **8 instances**
- `?i wdt:P279* wd:Q2051651` -> **54**. So cuts are modelled as **subclasses, not instances**.
- `Q139960435` tree: 96 subclasses, 13 instances. `Q6418247`: 95.
- Label depth across the 54: **max 49, median 6, min 1** — but **the top of the list is dishes, not
  cuts** (steak tartare 49, beef tenderloin 43, beefsteak 39, Chateaubriand 32) leaking in via `P279*`.
  Genuine cuts sit lower: brisket 31, rump steak 29, T-bone 27, chuck steak 27, flank 24, sirloin 24.
  **A typical real cut carries fewer than 6 labels.** Six items have a single label and no English label.

**THE STRUCTURAL FINDING** — `total 54 · withCountry (P17) 2 · withImage (P18) 32 · withAnatomy (P927)
0`. Wikidata labels are per-**language**, not per-**country**. Verified example: `Q2165995` flank steak
has Spanish label **"arrachera"** (Mexican) with alias **"vacio"** (Argentine), jumbled in one
undifferentiated Spanish bucket. **Nothing can say "arrachera in Mexico, vacio in Argentina."**
Portuguese similarly lumps "Bife do Vazio" with aliases Vazio and Pacu. And mappings are unreliable:
`Q6501598` sirloin steak has es=`solomillo` (**which is tenderloin, not sirloin**), fr=`Faux-filet`,
pt=`Contrafile`, it=`Lombo`. **Cuts don't map 1:1 across butchery traditions, and flat labels silently
assert that they do.**

**Lexemes** (the technically correct home for per-language names). Counted: Lexemes with a sense
(`P5137`) pointing at any item in the cut-of-meat subclass tree — **80 lexemes across 19 languages**:
Swedish 13 · Bokmal 11 · English 9 · Danish 7 · Italian 7 · Nynorsk 5 · German 5 · Russian 4 ·
Spanish 3 · **Sumerian 3** · Japanese 3 · French 2 · Hebrew 2 · Dagbanli 1 · Latin 1 · Southern Min 1 ·
Hindko 1 · Korean 1 · Finnish 1.
**Nordic languages are 36 of 80 — nearly half. Spanish has 3. There are as many Sumerian cut lexemes as
Spanish ones, and more than French.** Hobbyist effort concentrated in Scandinavia, not a resource.

CC0, excellent plumbing (SPARQL, REST, dumps). **Best plumbing, worst content.**

## 3. UNECE meat standards — the most important resource, and the actionable finding
Verified: *Bovine meat: carcases and cuts: UNECE standard*, ed. 2004, **ECE/TRADE/326**, ISBN
9789211168853, vi+58pp, Sales No. E.03.II.E.58 — via Stanford SearchWorks
https://searchworks.stanford.edu/view/5793124. Catalogue language: **English**.

UNVERIFIED: unece.org returns **HTTP 403 (Cloudflare)** to every attempt, as does digitallibrary.un.org
and a reader proxy. French and Russian editions **unverified**. Sibling standards appeared as search
URLs whose content was never fetched — Porcine (ECE/TRADE/369, 2006; Rev.3 2018), Ovine (2006, ISBN
9789211168860), Caprine (2007), Chicken (ECE/TRADE/355 Rev.1, 2013). **Titles real, details unverified.**

**BUT the codification is available machine-readable and free.** The Odoo Community Association ships
it:
`https://raw.githubusercontent.com/OCA/community-data-files/13.0/product_meat_unece/data/unece_code_list.xml`
— 44,963 bytes, downloaded and parsed: **169 records, 169 codes, 164 names**, with **16 species/product
headers**: 10 Bovine (Beef) · 11 Bovine (Veal) · 20 Deer · 30 Porcine · 40 Ovine · 50 Caprine ·
60 Llama · 61 Alpaca · 70 Chicken · 71 Turkey · 72 Duck · 73 Goose · 74 Rabbit · 80 Equine (Horse) ·
90 Edible meat co-products · 91 Retail meat cuts. Cuts carry numeric codes (1643 Brisket, 1650 Brisket
point end bone-in, 1660 Brisket navel end...).
Licence **AGPL-3**. Multilingual depth **thin** — `i18n/` holds only `fr.po` and the `.pot` template,
i.e. **French only**. Last commit touching it 2023-09-03; **exists only on branch 13.0, absent from
14.0-19.0, so effectively abandoned.**

**vs CarneAtlas:** UNECE covers **16 species groups** including deer, llama, alpaca, horse, rabbit, goat
and four poultry. More usefully: **it standardises cuts by anatomy with stable numeric codes — exactly
the pivot key CarneAtlas lacks.** Mapping each cut to a UNECE code would let names in any country hang
off an anatomy-anchored identifier, and **no encyclopedic source does this.**

## 4. OFAJ/DFJW bilingual butchery glossary — the closest true analogue
https://www.ofaj.org/sites/default/files/media/boucherie-metzgerhandwerk.pdf (verified HTTP 200, live)
*Glossaire/Glossar: Boucherie / Metzgerhandwerk*, Office franco-allemand pour la Jeunesse. **149 pages**,
PDF created 2003-07-04. **Bidirectional FR->DE and DE->FR.** Text extracted: 84,085 chars;
**~680 gender-marked French headwords** (agent's own regex measurement, not the "800+ terms" a search
summary claimed).

Real cross-language cut mapping with synonym sets: *aiguillette baronne* -> `Hueftdeckel, Tafelspitze,
"Buergermeisterstueck", "Pfaffenstueck"`. Explanatory equivalences rather than word swaps: *tende de
tranche* -> "entspricht: runde Nuss [Rind]"; *hampe* -> "Frankreich: Rindersteak aus der Querrippe".
It is a **whole-trade** glossary (slaughter, tools, even *allocation de chomage*), so cut terms are a
subset.

**Its preface names the hard part verbatim:** cut descriptions are limited to primals following the
"Decoupe nationale (dite de Paris)" because *"Une description plus precise supposerait l'etude
detaillee de trop nombreuses appellations regionales, voire locales, qui sortiraient du cadre de ce
glossaire."* — a more precise description would require studying too many regional and local
appellations, beyond this glossary's scope. **The one resource that engaged the problem explicitly
declined it as too large.**

Siblings also live: `cuisine-kuche.pdf`, `charcutier-traiteur-fleischverarbeitung-feinkost.pdf`.
2 languages only, not machine-readable, **licence UNVERIFIED** (no ©/droits/Rechte statement found in
extracted text), **last updated 2003**. Wikipedia's *Cut of beef* external links point to an archived
copy of this file.

## 5. FoodOn — the strongest structured cut vocabulary, and effectively monolingual
https://foodon.org · https://obofoundry.org/ontology/foodon.html · paper
https://doi.org/10.1038/s41538-018-0032-6 (Dooley et al. 2018, *npj Science of Food*)

Measured by downloading `foodon.owl` (~40 MB) on 2026-09-13: **409 beef, 182 pork, 130 lamb, 85 veal,
5 mutton** English-labelled classes, with deep synonym sets (`beef top sirloin steak` carries 5 exact
synonyms), and **134 references to USDA IMPS** with `seeAlso` links to the IMPS 100-series PDF
(verified 200: `ams.usda.gov/sites/default/files/media/IMPS100SeriesDraft2020.pdf`).

**Multilingual depth: ZERO non-English `rdfs:label`s.** Across ~83,000 labels there are only ~180
non-English *synonyms* total (49 es, 30 fr, 25 it, 14 zh, 14 jp, 9 th, 8 ja, 7 ko, 6 ru, 5 pt...).
OWL, CC BY per OBO Foundry.

**The gap in one sentence: the best structured meat-cut vocabulary in existence has ~800 English cut
classes, is US-centric, and is essentially monolingual.**

## 6. LanguaL — the only genuinely multilingual food-descriptor thesaurus found
https://langual.org · DOI https://doi.org/10.13140/RG.2.2.13274.64964 (Moller & Ireland, 2017/2018)
**8 languages**: English, Czech, Danish, French, German, Italian, Portuguese, Spanish. Its facet
**C. PART OF PLANT OR ANIMAL** is where cuts would live, but **whether facet C reaches retail-cut
granularity was NOT verified.** langual.org states FoodOn is its successor; FoodOn carries 50
`langual:` cross-references. Peer-reviewed: https://doi.org/10.1038/ejcn.2010.209 and
https://doi.org/10.1016/j.profoo.2013.04.018

## 7. Thesaurus de la viande — French only, openly licensed
Kombolo, Hocquette, Landrieu, Richon, Aubin, Yon (2022), Recherche Data Gouv,
https://doi.org/10.15454/pb5qxc (landing page verified 200). **1500+ concepts with definitions, French
only**; one of its 12 categories is **decoupe**. Derived from the Academie de la Viande's *Dictionnaire
de la Viande* (2012) — underlying dictionary UNVERIFIED.

## 8. Academic literature
**Headline: there is no academic paper specifically on comparative multilingual meat-cut
nomenclature.** Ten query framings across Crossref, OpenAlex, DOAJ, Semantic Scholar and OpenLibrary
found none. (Semantic Scholar returned 429 on nearly every call; Springer and unece.org gated.)

**Most on-point scholarly article found:**
**Lhuissier (2002), "Cuts and Classification: The Use of Nomenclatures as A Tool for the Reform of the
Meat Trade in France, 1850-1880", *Food and Foodways* 10:183-208 —
https://doi.org/10.1080/07409710216028.** Establishes cut names as **contested administrative
artefacts, not natural kinds.**

**Closest prior art to a structured cut catalogue:**
**Trypuz, Kulicki, Gradzki, Trojczak, Wierzbicki (2016), "Machine-Understandable and Processable
Representation of UNECE Standards for Meat. Bovine Meat — Carcases and Cuts Case Study", *CCIS* —
https://doi.org/10.1007/978-3-319-49157-8_12.** Paywalled; description rests on the verified title, so
**do not assume it handles multilingual naming.**

**The single most relevant published work:**
**Swatland, H.J., *Meat Cuts and Muscle Foods: An International Glossary*, Nottingham University Press
— 2000 (ISBN 9781897676301), 2005 (9781904761150), 2023 (9781789182903).** OpenLibrary subjects:
"Terminology", "Meat cutting", "Meat cuts". Reception corroborated by a one-page review: Fisher (2001),
*Meat Science* 58:437, https://doi.org/10.1016/s0309-1740(01)00076-6 — cite as a review, not research.
**Note the 2023 edition — this is a living work, and the same author wrote the 2012 AMSA paper.**

Other books (ISBNs verified via OpenLibrary): *The Meat Buyer's Guide*, NAMP — 1976 (187815401X), 1990
(9781878154002), 1997 (0471716855), 2004 (9780471696254); *Encyclopedia of Meat Sciences*,
Devine/Dikeman/Jensen (2004), ISBN 9780124649729. *Handbook of Australian Meat* (AUS-MEAT) — **not
found on OpenLibrary; existence in catalogued form not asserted.**

Translation/terminology studies exist but are on food/menu culture-specific items, not cut names.
Best entry point: Chiaro & Rossato (2015), *The Translator* 21:237-243,
https://doi.org/10.1080/13556509.2015.1110934. **Directly useful as a design model:** Rebechi & Tagnin
(2020), "Brazilian cultural markers in translation: A model for a corpus-based glossary", *Research in
Corpus Linguistics* 8:65-85, https://doi.org/10.32714/ricl.08.01.05.
Meat science: Fisher (2007) EU beef carcass classification history,
https://doi.org/10.3920/978-90-8686-610-6_004; Savell, "Cutting and Boning | Traditional",
*Encyclopedia of Meat Sciences*, https://doi.org/10.1016/b978-0-12-384731-7.00147-1.

**UNVERIFIED but worth chasing manually:** *"Deshuese y variacion del rendimiento carnicero de canales
bovinas en Venezuela: ... nomenclatura de cortes equivalente a los correspondientes norteamericanos"*
(2014) — a real Semantic Scholar record (paperId `14cee89716f570662b60e6211021f1fe7c6d15d7`, MAG
2749631402) with **no DOI, no venue, no authors**. By title it is precisely a Spanish<->North-American
cut-name mapping.

## Still not covered
**Wiktionary translation tables, USDA FoodData Central, Open Food Facts, Wikibooks Cookbook, and Cook's
Thesaurus (foodsubs.com) were not verified — including whether foodsubs.com still exists.** Open
questions, not findings.

## Bottom line
**What outclasses CarneAtlas:** UNECE on species breadth (16 groups vs 3) and on having an
anatomy-anchored numeric key; Commons on free diagrams (26 beef countries, all 31 diagrams reusable);
FoodOn on English cut granularity (~800 classes); Wikipedia on beef country breadth (22 vs ~10).

**What nobody does — verified three ways:** (1) Wikipedia has **zero** cross-country equivalence tables
in English, German, French, Italian or Portuguese, and **no Spanish article at all**; (2) Wikidata's
model **cannot express per-country naming** — 2/54 items carry a country, 0/54 an anatomical location,
and Mexican "arrachera" sits undifferentiated beside Argentine "vacio"; (3) FoodOn, the best structured
vocabulary, has **zero non-English labels**. The one resource that engaged the problem, OFAJ's 2003
glossary, explicitly declined it as too large in scope.

**Strongest single recommendation from this thread:** adopt **UNECE numeric cut codes as the pivot
key** — the AGPL-3 XML at OCA (169 records, 16 species) gives the skeleton free, and no encyclopedic
source has done this mapping.
