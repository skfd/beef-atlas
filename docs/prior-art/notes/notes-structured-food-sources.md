# Notes: other structured/open food sources (Wiktionary, OFF, USDA, Wikibooks, FoodSubs, AGROVOC)

All figures from pages/files the agent fetched. Unfetched marked UNVERIFIED.

## 1. Wiktionary — the closest existing thing, done ad hoc
https://en.wiktionary.org · **Licence CC BY-SA 4.0**, verified verbatim from the siteinfo API
`rightsinfo` (MediaWiki 1.47.0-wmf.19).

Counted from wikitext (`action=parse&prop=wikitext`), top-level `* Language:` lines inside each
`{{trans-top}}...{{trans-bottom}}` block:

| Entry | Sense | Languages | Last revision |
|---|---|---|---|
| brisket | "chest of an animal" | **14** | 2026-07-17 |
| brisket | "cut of meat" | **23** lines / 24 distinct `t` codes | — |
| sirloin | "cut of beef" | **19** lines / 18 codes | 2026-08-24 |
| tenderloin | "tenderest part of a loin" | **18** | — |
| chuck | "meat from the shoulder" | **11** (1 of 7 trans blocks) | — |
| flank steak | single sense | **9** | 2025-10-31 |
| rump steak | — | **6** | — |
| picanha | — | **6** | — |
| skirt steak | — | **3** (French, Korean, Russian) | — |
| short rib | — | **2** (Bulgarian, Maori) | — |

**The tail falls off a cliff.** The four famous cuts get 11-23 languages; `short rib` gets two.
Idiosyncratic: brisket's cut sense includes Southern Altai, Norman (`{{qualifier|Jersey}}`) and Volapuek
but not Dutch regional variants; chuck's includes Ancient Greek and Maori.

**Category size:** `Category:en:Cuts of meat` = **72** pages. Non-English equivalents near-empty:
**fr: 1, es: 3, de: 1, it: 14, pt: 11**. So the multilingual content exists **only as English-entry
translation tables — there is no reverse direction.** The Spanish entries `vacio` and `entrana` both
exist but carry **no beef-cut sense at all**.

**Regional variants — partially, ad hoc, via the `{{q}}` qualifier, used inconsistently.** Verbatim from
`flank steak`:
```
* Portuguese: {{t|pt|fraldinha|f}} {{q|Brazil}}, {{t+|pt|vazio|m}} {{q|Brazil: Rio Grande do Sul}}
* Spanish: {{t|es|sobrebarriga}}, {{t+|es|matambre}}
```
**Portuguese gets country and even *state* granularity; the Spanish line dumps a Colombian term and an
Argentine term side by side with no region marks at all. That one snippet is the structural gap in the
whole field.**

**Machine-readable extractions, both verified live:**
- **Wiktextract** https://github.com/tatuylonen/wiktextract — 1,264 stars, created 2018-10-29, last push
  **2026-09-04**, licence field `NOASSERTION`.
- **kaikki.org** https://kaikki.org/dictionary/rawdata.html — current English extract from the
  **enwiktionary dump dated 2026-09-02**; raw Wiktextract JSONL **23.1 GB** (2.7 GB gz). Other editions
  built: Chinese, Czech, Dutch, French, German. Per-word pages work:
  https://kaikki.org/dictionary/English/meaning/b/br/brisket.html offers a `brisket.jsonl` download.
- **DBnary** https://kaiko.getalp.org/about-dbnary/ — extracts from **27 Wiktionary language editions**;
  dataset **CC BY-SA 3.0 Unported**, software MIT; evolves **twice a month**; SPARQL endpoint;
  ontolex/lemon RDF since July 2017. **Note: "July/August 2026 extracts have been retracted."**

## 2. Open Food Facts — a French nutrition import, not a multilingual vocabulary
Real taxonomy path (the obvious one 404s):
https://raw.githubusercontent.com/openfoodfacts/openfoodfacts-server/main/taxonomies/**food**/categories.txt
— **3,614,222 bytes, 126,498 lines, 14,843 blocks.** Last commit touching it **2026-09-09**.

**210 distinct line-leading language prefixes** — 181 two-letter, 26 three-letter (`ang`, `arz`, `ast`,
`bar`, `yue`, `lmo`, `lad`, `csb`, `fur`, `jbo`...), plus `xx` (467 lines) as OFF's cross-language code.
Lines per prefix: **fr 10,650 · en 9,209 · hr 5,260 · nl 4,712 · it 3,739 · de 3,629 · es 3,563 ·
lt 2,377 · fi 1,837 · bg 1,394**. **French leads English — this file is French-first.**

**Cut-level entries exist but are a French import.** Verbatim:
```
< en: Beef front quarter
en: Beef flank steak
fr: Bavette d'aloyau de boeuf, Bavette d'aloyau
hr: Goveđi odrezak s boka
ja: 牛フランク
agribalyse_food_code:en: 6212
ciqual_food_code:en: 6212
```
Every cut-level entry carries a CIQUAL/AGRIBALYSE code — bulk-imported from the French food-composition
database. Which is why `entrecote` (7 lines), `bavette` (5), `onglet` (4) and `rumsteck` (7) all appear,
while **`brisket` appears 0 times in the whole file.**

**Language depth on meat entries:** across all **156** blocks whose `en:` line starts Beef/Pork/Lamb —
min 1, **median 2**, mean 4.0, max 21 — and **the rich ones are generic parents, not cuts** (`Pork, Pork
meat, swine, swine meat` 21; `Beef, Beef meat` 19; `Beef steaks` 13). The file carries **4,220**
`wikidata:en:` links.

API verified live: `/api/v2/search?categories_tags_en=beef-flank-steak` returns **count 259**.
Dumps generated **nightly** with 14-day deltas (JSONL, MongoDB, CSV ~9 GB raw, Parquet on Hugging Face,
experimental RDF). **Licence: database ODbL, contents DbCL, images CC BY-SA** — **legally mineable.**

## 3. USDA
### FoodData Central — monolingual, and the proof is funny
https://fdc.nal.usda.gov · **Licence CC0 1.0 / public domain** (verified by grep on fetched HTML).
**Not multilingual at all.** Cadence: Foundation Foods twice annually (April & October); SR Legacy
"Final update was in 2018"; FNDDS every 2 years; Branded monthly. Homepage marker "April 2026".
API verified live with `DEMO_KEY`:

| query | totalHits | top results |
|---|---|---|
| brisket | **245** | "Beef, brisket" (FNDDS), "Beef, brisket, whole, separable lean only..." (SR Legacy) |
| sirloin | **513** | "Beef, top sirloin steak, raw" (Foundation) |
| bavette | **6** | **all pasta brands — "ARTISAN PASTA, LEMON BAVETTE"** |
| entrecote | **0** | — |

**`bavette` returning pasta and `entrecote` returning nothing is the clearest possible proof** that FDC
indexes cut names only as English nutrition-record descriptions. A composition database, not a
nomenclature.

### IMPS — the real find, and it IS bilingual
https://www.ams.usda.gov/grades-standards/imps (403 to WebFetch; fetched with curl + browser UA). Lists
**11 series** (100 Beef, 200 Lamb & Mutton, 300 Veal & Calf, 400 Pork, 500/600 cured, 700 variety meats,
800 sausage, 11 Goat), nine "Draft ... 2020" PDFs, `Lamb_IMPS200Series_2022.pdf`,
`Veal_IMPS300Series_2022.pdf`, **and a section headed "USDA IMPS are now available in Spanish" with 5
Spanish editions.**

| | English | Spanish |
|---|---|---|
| File | `IMPS_100_Fresh_Beef[1].pdf` | `IMPS_100_Fresh_Beef_Spanish[1].pdf` |
| Size | 1,787,865 B | 957,194 B |
| Pages | **71** | **71** |
| Effective date | "EFFECTIVE: **November 2014**" | "VIGENTE DESDE **marzo 2015**" |
| Distinct numbered items | **183** (100-194) | **181** matches for `Pieza n.o NNN` |

(The 183/181 gap is likely the agent's regex missing two, not a content gap.) **Load-bearing evidence
that it is a genuine parallel nomenclature, not a translated cover page:**
> EN: `Item No. 115A - Beef Chuck, Blade Portion, Boneless`
> ES: `Pieza n.o 115A - Espaldilla, Porción de la Paleta, Deshuesada`

Spanish anatomical vocabulary is fully present in the ES edition (Lomo 141 occurrences, Costilla 66,
Falda 20, Pecho 20, Paleta 19) and English fully absent from it (Chuck 0, Brisket 0), and vice versa.

**URMIS** (Uniform Retail Meat Identity Standards): no mention anywhere on the IMPS page — **UNVERIFIED,
not located.** **IMPS licence: page states none — UNVERIFIED** (the agent declined to infer
public-domain status from "US government work").

**vs CarneAtlas:** IMPS is the single strongest piece of prior art for *authoritative* cut naming — 183
numbered beef items, bilingual EN/ES, the reference the US trade actually uses. But two languages,
11-year-old PDFs, no machine-readable form, and it is a **procurement spec**: it tells a buyer what to
order, not what a shopper in Buenos Aires calls that muscle.

## 4. Wikibooks Cookbook — prose, no overlap
Licence CC BY-SA 4.0 (verified via siteinfo).
- **Cookbook:Beef** — last revision **2025-06-29**. `== Cuts ==` section: **8 American primals** in
  prose. Notes "In continental Europe, cuts tend to derive from individual muscles... In the UK and
  North America, some cuts may consist of multiple muscle groups." British and Dutch cuts appear **only
  as image files** — **no non-English cut names in the wikitext.** (A rendered-page summary suggested
  otherwise; the wikitext does not support it.)
- **Cookbook:Pork** — last revision **2025-08-26**, 3,832 chars. 4 primals, **16** bulleted sub-cuts.
  English only.
- **Cookbook:Lamb** redirects to **Cookbook:Lamb and Mutton** (last revision **2025-07-01**, 14,363
  chars) — the best of the three: a `== Cuts ==` **wikitable** with 19 row separators and ~21 named
  subprimals across Primal cut / Definition / Flavor-Texture / Description / Use / Subprimal columns.
  Still English only.
- **`Cookbook:Cuts of beef`, `Cookbook:Butchery`, `Cookbook:Cuts of meat` — all MISSING.**

## 5. Cook's Thesaurus / foodsubs.com — ALIVE, rebuilt, and legally untouchable
**Status: LIVE.** `http://foodsubs.com/` -> 301 -> `https://foodsubs.com/` -> 200, a modern site with
Google Tag Manager, footer "**© 2026 Foodsubs.com**". **Old flat URLs are dead** (`/Beef.html` -> 404);
content moved to `/groups/meats/beef/...` and `/ingredients/...`.

Counts from live navigation: Meats **352** · Beef **59** · Beef Chuck 16 · Beef Loin Cuts 16 · Beef Rib
Cuts 5 · Beef Round Cuts 11 · Breast & Flank 5 · Misc 6 · Veal 24 · Variety Meats 23 · Lamb 21 · Pork
**29** · Game 21 · Poultry 16 · Cured Meats 142.

**Multilingual depth for cuts: NONE.** The "Also known as:" field is English-only US trade synonyms with
no language labels:
- `beef top blade steak` -> "book steak, butler steak, flat iron steak, lifter steak, petite steak, top
  blade steak, top chuck steak"
- `beef 7-bone pot roast` -> "7-bone pot roast, 7-bone roast, center cut pot roast, chuck roast center cut"

Item pages also carry a scientific name (`Bos taurus`), nutrition per 100g, and substitution ratios.
Non-meat entries **do** carry transliterated foreign synonyms — `bok choy` -> "baak choi, bai cai, pak
choi, taisai, pok choi..." with a "Cuisine: Chinese" field — but still untagged by language. **So the
site's reputation for foreign synonyms holds for produce and cheese, not for beef cuts.**

**Licence: ALL RIGHTS RESERVED.** Verbatim from https://foodsubs.com/terms-and-conditions:
> "All content included on this site is and shall continue to be the property of Foodsubs.com... **Any
> copying, redistribution, use or publication by you of any such content or any part of the Site is
> prohibited**"
> "...a limited, revocable, nonexclusive license to use this site solely for your own personal use and
> **not for republication, distribution, assignment, sublicense, sale, preparation of derivative works,
> or other use**."
California law; copyright agent Margaret Alden.

Wayback CDX confirms the new-structure beef pages are preserved through at least **2025-08-21** (query
capped at 25 rows). Whether the pre-rebuild `Beef.html` pages are preserved: **UNVERIFIED**.

**vs CarneAtlas:** structurally the closest competitor — a browsable cut hierarchy with synonym lists,
**59 beef items against CarneAtlas's 64** — but monolingual and licensed so restrictively that not a
line can be reused.

## 6. AGROVOC (FAO) — 26 languages deep, ~60 cuts shallow
https://agrovoc.fao.org · SKOSMOS REST API verified working.
**The decisive result: searching `brisket` -> 0 results; `sirloin*` -> 0 results.** It has `beef`
(c_861) and `meat cuts` (c_4672). The `meat cuts` concept has **26 prefLabel languages** (ar, cs, de, en,
es, fa, fr, hi, hu, it, ja, ka, ko, lo, ms, pl, pt, **pt-BR**, ro, ru, sk, sr, sw, th, tr, zh — note
`pt` "peça de carne" vs `pt-BR` "corte de carne", **the one place a regional split appears**), created
1981-01-09, modified 2025-07-18. Its narrower concepts are exactly **seven**, all generic:

| Concept | English | prefLabel languages |
|---|---|---|
| c_11912 | joints (meat) | 22 |
| c_7380 | steaks | 25 |
| c_7047 | shoulders | 24 |
| c_4421 | loins | 23 |
| c_4254 | legs (meat) | 22 |
| c_2897 | fillets | 26 |
| c_1587 | chops | 23 |

**None has any narrower concept.** The thesaurus declares 42 languages overall. **Licence UNVERIFIED** —
`/browse/agrovoc/en/about` 404s, no licence statement found on any fetched page.

**vs CarneAtlas:** AGROVOC is 22-26 languages deep and about 60 cuts *shallow*. **It stops exactly one
level above where CarneAtlas's entire dataset lives.** Best possible upstream vocabulary to align
top-level categories to; useless as a source of cut names.

## 7. Wikidata per-item labels (complements the SPARQL findings in notes-open-data-encyclopedic.md)
**Licence CC0** (verified verbatim from siteinfo rightsinfo).

| Item | Labels | Alias languages | Sitelinks |
|---|---|---|---|
| brisket Q1324342 | **31** | 7 | 22 |
| chuck steak Q1365996 | **27** | 4 | 15 |
| sirloin steak Q6501598 | **24** | 3 | 19 |

Q1365996's labels include `fr: paleron`, `pt: acém`, `pl: Karkówka`, `sv: högrev`, `da: højreb`,
`fi: etuselkä`, `cs: hovězí krk`, `ca: filet de llonzes i coll` — genuinely useful, CC0, API-accessible
per item. But the item set is **bounded by Wikipedia notability**: `Category:Cuts of beef` = **48**
pages, `Category:Cuts of pork` = **20**. **No structural region field** — you get `paleron` for French
with no way to say whether that is the Paris butcher's term or the Quebecois one. (WDQS SPARQL returned
**429: "Aggressively rate-limiting to 1 req / min - this rule was created during active wdqs outage"**,
so no aggregate class count from this thread.)

## 8. UNECE — UNVERIFIED, Cloudflare-blocked on every route
`unece.org/trade/wp7/meat-standards` 403, `unece.org/sites/default/files/2024-03/Bovine_326Rev2E_2016.pdf`
403, `www.unece.org/fileadmin/DAM/trade/agr/standard/meat/e/Bovine_2004_e_Publication.pdf` 403,
`digitallibrary.un.org/record/527063` returned **202 with 0 bytes**. WebSearch surfaced these as leads
only — snippet claims (a 2015 revision; a 2023 edition in English/French/Russian) are **search-result
text that could not be confirmed. Worth a retry from a real browser.**

## Bottom line
**No free resource models per-country name variation *within* a language as structured data.**
- **Wiktionary** does it ad hoc and inconsistently — `{{q|Brazil}}` and `{{q|Brazil: Rio Grande do Sul}}`
  on one line, then `sobrebarriga, matambre` unmarked on the next — across only 72 English cut entries.
- **IMPS** is the only official bilingual cut nomenclature (183 numbered beef items, EN + ES, 2014/2015),
  but two languages in static PDFs.
- **Wikidata** gives 24-31 CC0 labels per cut but only for the ~48 cuts Wikipedia deems notable, with no
  region dimension.
- **AGROVOC** is 22-26 languages deep but stops at `steaks`/`chops`/`loins`.
- **Open Food Facts** has ~24 cut nodes at a median of 2 languages, all French imports.
- **FoodData Central** is monolingual; `bavette` returns pasta.
- **FoodSubs** has the right shape (59 beef items, synonym lists) but is English-only and **explicitly
  forbids derivative works**.
- **Wikibooks** is prose.

**Legally mineable:** OFF (ODbL) for French/Croatian/Japanese terms, Wikidata (CC0) for 20+ labels on the
notable cuts, Wiktionary/DBnary (CC BY-SA). **FoodSubs must not be copied from.**
