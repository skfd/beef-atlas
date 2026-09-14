# Notes: fish species naming prior art

Baseline: **CarneAtlas has 39 fish species, per-country names across ~10 countries, and cites no source
on any fish page.** Numbers marked **(counted)** were counted by the agent from data it downloaded.

## 1. FishBase
https://www.fishbase.se/home/index.htm ("Main Data statistics as of **June 2026**")

**Provenance trap:** two live paths serve two different decades. `home/index.htm` -> June 2026;
`home.htm` -> **October 2015, 33,230 species**; `home/copyright.htm` is byte-identical to the June 2026
home page, **not** a copyright page. `https://fishbase.org/home.htm` returns **403** to curl.

| Figure | Value |
|---|---|
| Species | **36,761** (5,276 genera, 629 families, 84 orders, 10 classes) |
| Synonyms | 103,875 (95,951 + 7,924 misapplied) |
| **Common names** | **333,268 — for 30,302 species in 260 countries in 361 languages** |
| Reports in countries | 197,453 for 36,479 species in 303 countries |
| References used | 34,583 |
| Records total | ~3.3 million in ~200 tables |

Version string: "Froese, R. and D. Pauly. Editors. 2026. FishBase... **version (06/2026)**".
Updated daily internally, bimonthly on the website.

**Licence — CC BY-NC 4.0, confirmed not assumed.** Footer of `/search.php` links
`creativecommons.org/licenses/by-nc/4.0/` and states: *"You are welcome to include text, numbers and
maps from FishBase in your own web sites for non-commercial use, given that such inserts are clearly
identified as coming from FishBase, with a backward link... Photos and drawings belong to the indicated
persons or organizations and have their own copyright statements."*
**-> The NC clause matters for an Amazon-affiliate site.**

**Common names access:**
- Per-species HTML: `/ComNames/CommonNamesList.php?ID=236&GenusName=Salmo&SpeciesName=salar&...` —
  header reads **"n = 203"** for *Salmo salar*, with a "See Market names" link.
- **Per-species XML webservice, no key needed:**
  `https://www.fishbase.se/webservice/comnames/ComNamesXML.php?Genus=Salmo&Species=salar` ->
  `<status>Successful connection, 204 record(s) found.</status>`, each record
  `<comname>/<country>/<language>/<type>`. Counts disagree (203 vs 204) and the XML includes rows with
  an **empty `<comname>`**.
- Official "Download Section" is **documents and PowerPoints only** — **(counted: 33 download links,
  zero data dumps)**. `/api/` -> **403**. `fishbase.ropensci.org` -> unreachable. **No documented
  public REST API.**
- **The real bulk path: rfishbase parquet snapshots on Source Cooperative S3**, plain HTTPS, no R, no
  credentials. Bucket/prefix read from source (`rfishbase/R/fb_tbl.R` lines 95-96):
  `us-west-2.opendata.source.coop`, prefix `cboettig/fishbase/{sv}/`.
  - Versions **(counted)**: v19.04, v21.06, v23.01, v23.05, v24.07, **v25.04, v26.06** — note the last
    two **exist but are absent from the README's `available_releases()`**.
  - v26.06 parquet dir: **222 objects (counted)**, incl. `comnames.parquet` (10,260,470 bytes).
  - Downloaded and parsed `comnames.parquet` **(all counted)**: **333,253 rows, 36 columns; 372 distinct
    `Language` values; 262 distinct country codes; 30,302 distinct `SpecCode`.** Columns include
    `ComName, Transliteration, SpecCode, C_Code, Language, Script, UnicodeText, NameType, IsASFIS,
    PreferredName, TradeName, ComNamesRefNo, Misspelling, Size, Sex, Rank`.
  - `NameType` **(counted)**: Vernacular 297,882 / FAO 12,742 / AFS 8,558 / **Market 5,459** / FAO old
    5,004 / Aquarium 1,683 / vernacular 1,529 / AFS old 163. `TradeName=1` on 1,594 rows;
    `PreferredName=1` on 7,759; **`IsASFIS=1` on 0 rows**.
  - Depth per species **(counted)**: **median 4 names/species, max 534.** *Salmo salar* = **216 rows
    across 39 languages and 45 countries.**
  - Small drift snapshot vs live site: 333,253 vs 333,268 names; 372 vs 361 languages; 262 vs 260
    countries.
  - README caveat verbatim: *"rfishbase defaults to download the latest available snapshot; be aware
    that the most recent snapshot may be months behind the latest data on fishbase.org."* README
    **states no licence for the FishBase data itself.** Also serves SeaLifeBase.

**vs CarneAtlas:** ComNames alone holds **333,253 name records in 372 languages across 262 countries for
30,302 species** — roughly **777x the species count**. ***Salmo salar* by itself (216 names, 39
languages, 45 countries) carries more name variation than CarneAtlas's entire 39-species x 10-country
grid.** And FishBase has a **country column**, which is the axis CarneAtlas claims as its own.

## 2. FAO ASFIS List of Species for Fishery Statistics Purposes
Data: https://www.fao.org/fishery/static/ASFIS/ASFIS_sp.zip

**The landing page is unreadable — UNVERIFIED.** `fao.org/fishery/collection/asfis/en` returns HTTP 200
/ 70,550 bytes but the body is a multilingual "page not found" shell; the whole `/fishery/` site is a
client-rendered Qwik app. Its content API returns **401 with `WWW-Authenticate: Bearer`**. So **no figure
below comes from FAO's own description** — all from the data file or other fetched PDFs.

**Download works:** HTTP 200, `application/zip`, **2,007,548 bytes**, entries dated **2026-07-09**.
Contains `ASFIS_sp_2026.1.xlsx` (1,546,351 B) and `ASFIS_sp_2026.1.csv` (1,822,794 B). Edition confirmed
from `docProps/core.xml`: created 2026-07-08, modified 2026-07-09. Prior edition `ASFIS_sp_2024.zip`
also live (13,567 rows); `ASFIS.zip` and `ASFIS_sp_Feb_2025.zip` are **404**.

**Contents, by parsing the CSV (counted): 13,965 data rows, 14 columns.**

| Column | Non-empty | % |
|---|---|---|
| `Alpha3_Code` | 13,965 (13,965 unique, 0 dupes) | 100 |
| `Scientific_Name` / `Taxonomic_Code` / `Order or higher taxa` | 13,965 | 100 |
| `Family` | 13,853 | 99.2 |
| `ISSCAAP_Group ` *(header has a trailing space)* | 13,747 | 98.4 |
| **`English_name`** | **10,283** | **73.6** |
| **`French_name`** | **5,833** | **41.8** |
| **`Spanish_name`** | **4,917** | **35.2** |
| **`Chinese_name`** | **2,698** | **19.3** |
| **`Arabic_name`** | **2,075** | **14.9** |
| **`Russian_name`** | **598** | **4.3** |

**Six name languages, all genuinely populated but very unevenly.** Sample row:
`SAL | Salmo salar | Atlantic salmon | Saumon de l'Atlantique | Salmon del Atlantico | (AR blank) |
大西洋鲑 | Лосось атлантический (=семга) | Linnaeus 1758 | SALMONIDAE`. `FishStat_Data = YES` on 4,065 rows.

**The 3-alpha code system:** the **"Inter-Agency 3-Alpha Code"**, developed by the **CWP** (Coordinating
Working Party on Fishery Statistics), assigned by FAO. From ASFIS Reference Series No. 15 (Garibaldi &
Busilacchi, 2002, 258pp),
https://openknowledge.fao.org/server/api/core/bitstreams/e98c60e0-1d51-4b60-9564-5be4c922566c/content:
*"Once a 3-alpha identifier has been assigned to a species item it is not changed and thus it is a
permanent reference to a species item. Codes for species items which have been cancelled... are not
reused but are considered as 'dead codes'."* and *"Only FAO-FIDI, being the manager of the list, can
create or modify codes."* It identifies a **"species item"**, not necessarily a species — categories
exist at genus, family or higher level; subspecies excluded. Per `ASFIS_Structure.pdf`: *"Only in few
cases the three letters of the 3-alpha code are related to the scientific or English name... In all the
other cases the 3 letters are assigned at random."*

**Two stale-documentation traps:**
- `ASFIS_Structure.pdf` (27,138 B, 5pp) carries footers reading
  `file:///T|/FIES/ASFIS_fin/ASFIS_Web/asfis_st.asp ... [26/03/2008 16:27:38]`. It documents field names
  `3A_CODE` / `Stats_data` (actual: `Alpha3_Code` / `FishStat_Data`) and **only EN/FR/ES name fields — no
  Arabic, Chinese or Russian. Do not cite it as describing the current file.**
- FAO's data catalogue still says "**13 420 species items**" and "about one third... have also a French
  and Spanish name" — that is **version 2020.1**, understates the current file by 545 items, and omits
  AR/ZH/RU entirely.

**Licence — attribution-required but genuinely ambiguous across FAO's own pages:**
1. **CC BY 4.0** per FAO's statistical-database terms — but Annex 1 names "Fisheries and Aquaculture
   (FishStat)" and **not ASFIS**, and the same terms add *"Datasets shall not be used for or in
   conjunction with the promotion of a commercial enterprise."*
2. **`"license_id": "CC-3.0-IGO"`, `"isopen": false`** per the CKAN API — and **that identifier does not
   resolve**; the licence list contains only `CC-BY-3.0-IGO`, `CC-BY-SA-3.0-IGO`, `CC-BY-NC-SA-3.0-IGO`.
3. No licence file ships inside the zip.

**Cadence:** annual. FishStat release calendar final row: *"ASFIS List of Species... | July 2026 | |
May 2027"*. The CWP handbook's "March-April" claim is stale against observed releases of Jul 2026 and
Nov 2024.

**vs CarneAtlas:** the canonical machine-readable naming table — **13,965 species items x 6 languages,
one permanent 3-alpha code each, a 2 MB CSV refreshed annually.** ~358x the species count. **But note it
is *language*-keyed, not *country*-keyed**, so it does not model "Portugal vs Brazil" the way CarneAtlas
claims to.

## 3. FAO FishFinder
https://www.fao.org/fishery/fishfinder/en — **site not fetchable, same empty JS shell. UNVERIFIED.**
Everything below from PDFs and repository metadata that were fetched.

From the FishFinder leaflet (1,207,082 B, 2pp, internal stamp `06/07/2011`), verbatim: *"In forty years
FAO FishFinder has produced over **200 identification guides**... and has compiled a unique and
important archive of more than **40 000 scientific illustrations** as well as distribution maps,
taxonomic descriptions, biological and fisheries information on over **8 000 species**."* Also *"So far,
**158 volumes** have been published"*.

Coverage: regional Species Identification Sheets, worldwide Species Catalogues by taxon, per-country
Field Guides (Angola, Cambodian Mekong, Gulf of Guinea, Kuwait/Saudi/Bahrain/Qatar/UAE, Madagascar,
Morocco, Mozambique, Namibia, Pakistan, Senegal, Somalia, Sri Lanka, Tanzania, Kenya...), waterproof
pocket ID cards.

**Multilingual at whole-publication level, not as parallel data fields** — evidenced by the series
titles ("Pacifico Centro Oriental", "Mediterranee et Mer Noire", "Hakes of the world (En & Sp)").
Individual guides carry local vernacular names plus an English FAO name.

**Machine-readable: no.** PDF and print only. One 32-page guide downloaded (8,009,739 B) yielded **zero
extractable text** (image-only scan). The openknowledge search API returns **403**, so the catalogue
cannot even be enumerated programmatically.

**Licence: non-commercial** — DSpace metadata gives `dc.rights.license = "CC BY NC SA 3.0 IGO"`. Older
items stricter: the Kenya pocket guide states *"Reproduction for resale or other commercial purposes,
including educational purposes, may incur fees."*

Latest FishFinder-tagged publication verified is **2023**; a confirmed recent item is the mesopelagic
fishes guide, **2020**, 346pp, ISBN 978-92-5-133094-4, DOI https://doi.org/10.4060/cb0365en, 552 species.
**But the headline programme statistics are from 2011 and still in circulation — treat as 15 years old.**

**vs CarneAtlas:** not really comparable — a book/plate library for *identifying* fish, not a names
dataset. **The one resource here that is worse than CarneAtlas as structured data, because none of it is
data at all.**

## 4. EU commercial designations — the closest and most direct prior art
### 4a. The legal requirement — VERIFIED verbatim
Regulation **(EU) No 1379/2013** of 11 December 2013, fetched in full (293,856 B) from
https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32013R1379. **Article 37 "Commercial
designation", verbatim:**
> **1.** ...Member States shall draw up and publish a list of the commercial designations accepted in
> their territory, together with their scientific names. The list shall indicate:
> **(a)** the scientific name for each species, in accordance with the **FishBase Information System or
> the ASFIS database of the Food and Agriculture Organization (FAO)**, where relevant;
> **(b)** the commercial designation: **(i)** the name of the species in the official language or
> languages of the Member State concerned; **(ii)** where applicable, any other name or names that are
> accepted or permitted locally or regionally.
> **3.** Any changes... shall be **notified forthwith to the Commission**.

**The premise holds in full, including the notification duty. And the regulation names FishBase and FAO
ASFIS by name as the scientific-name authorities — the two resources above are written into EU law.**

### 4b. The Commission's consolidated system
**Fish Commercial Names Information System — https://fish-commercial-names.ec.europa.eu**
The DG MARE page states verbatim: *"The Commission has set up an information system gathering all the
commercial designations recognised in the EU... **This tool is not the official source** of information
on the commercial designations accepted in the member states: **only the national lists provided below
are the authoritative source.**"* That page links **27 member-state national lists** plus a UK entry
**(counted)**.
- Covers **27 member states (counted)**; UI served in **24 EU languages (counted)**.
- **Search by: Commercial designation, Scientific name, FAO 3-alpha code, Combined Nomenclature.**
  Per-country views filterable **by that country's official languages** — Ireland offers English and
  Irish.
- **Machine-readable: NOT YET.** The open-data page states the data *"can be accessed for free, in an
  open machine-readable format, with an open attribution license that also allows for a commercial
  reuse"* — followed immediately by ***"Coming soon..."***. No download, no API today.
  `/fish-names/advanced-search_en` returns **404**. Per-species detail pages are **bot-gated** (curl and
  WebFetch both got "Security check / Verify you are a human") — contents UNVERIFIED.
- **Ireland, counted via the site's own pager** (20 rows/page): **English 542 designations; Irish (ga)
  415.** Pager arithmetic, not a downloaded file. Listing shows synonym resolution inline — `Arched
  razor shell -> Ensis arcuatus synonym for Ensis magnus` — and family-level entries.

### 4c. Germany — BLE, a real national list, fetched and parsed
*"Verzeichnis der Handelsbezeichnungen fuer Erzeugnisse der Fischerei und Aquakultur
(deutsch-lateinisch)"* — page `Erscheinungsdatum: **07.09.2026**`, flagged *"Nicht barrierefrei"*.
PDF: **207,100 bytes, 28 pages (counted)**. Header: **"117. Aenderung — Stand: 04.09.2026"** (117th
amendment). Two columns only: `Handelsbezeichnung | Wissenschaftlicher Name`.
**Counted by parsing extracted text: 1,204 designation/scientific-name pair lines -> 974 distinct German
commercial designations against 854 distinct scientific-name strings** (includes `spp.` and family-level
entries, and a hybrid `Heterobranchus longifilis X Clarias gariepinus`).
**Multiple permitted German names per species are common:** `Coregonus lavaretus` -> Blaufelchen,
Gangfisch, Grosse Maraene, Kilch, Sandfelchen, Silberkarpfen (**6**); `Pandalus borealis` -> six names;
`Salmo salar` -> Atlantischer Lachs, Lachs, Salm, Wildlachs (**4**).
PDF only, extracts cleanly with `pdftotext -layout`. **Licence: none stated.** Covers fishery **and
aquaculture** — shellfish and crustaceans included. **No FAO 3-alpha code.**

### 4d. United Kingdom (retained law, not an EU member state)
https://www.gov.uk/government/publications/commercial-designations-of-fish-united-kingdom/commercial-designations-of-fish
`datePublished 2020-02-03`, `dateModified **2026-01-23**`.
**Counted from the HTML: 86 tables, 84 header rows, 491 data rows** in three sections (Marine fish /
Salmon and freshwater fish / Shellfish). **315 rows carry a scientific name (313 distinct)**; **174 are
cross-references** ("Alaska pollock – see entry for...") with no scientific name.
**90 of the 315 real entries bundle alternative designations with " or "** — `Alaska pollack or Alaska
pollock or Pacific pollack or Pacific pollock -> Gadus chalcogrammus/Theragra chalcogramma`;
`Angler(fish) or Monk(fish) -> Lophius americanus, L. budegassa, L. piscatorius`; `Bib or Pout or
Pouting or Pout whiting -> Trisopterus luscus`.
**Format: HTML tables — the most machine-readable national list found**, scrapeable without PDF
extraction. **Licence: Open Government Licence v3.0.** Includes shellfish. No FAO 3-alpha code.
France's DGCCRF list returned **403 — UNVERIFIED.**

**vs CarneAtlas:** **this is the closest and most direct prior art of anything in the whole survey.** The
Commission's system already does exactly what CarneAtlas does for fish — one species, its designation in
each country, in that country's own language(s) — across **27 member states and 24 interface
languages**, at national-list scale (Germany **974 designations / 854 scientific names**; Ireland **542
EN + 415 GA**; UK **315**). Legally mandated, refreshed continuously (DE 2026-09-04, UK 2026-01-23), and
free. Its one real gap: **the consolidated EU data is still not downloadable ("Coming soon...")**,
national lists are mostly unparsed PDFs, and coverage stops at commercially traded species inside the
EU/UK.

## Summary table

| Resource | Species | Multilingual depth | Machine-readable | Licence | Last updated |
|---|---|---|---|---|---|
| **FishBase** | 36,761 | 333,268 names / 361 langs / 260 countries | Per-species XML (no key); parquet bulk on S3 (v26.06); **no REST API** | **CC BY-NC 4.0** | version 06/2026 |
| **FAO ASFIS** | 13,965 items | 6 langs (EN 73.6%, FR 41.8%, ES 35.2%, ZH 19.3%, AR 14.9%, RU 4.3%) | **Yes** — CSV+XLSX zip, 2.0 MB, one URL | Ambiguous: CC BY 4.0 vs non-resolving "CC-3.0-IGO", `isopen: false` | ed. 2026.1, 9 Jul 2026 |
| **FAO FishFinder** | 8,000+ described (2011 figure) | Whole pubs in EN/FR/ES + local vernaculars | **No** — PDF/print, some image-only | CC BY-NC-SA 3.0 IGO | latest guide 2023; stats 2011 |
| **EU Fish Commercial Names** | 27 national lists | 24 UI langs, per-country official langs | **No — "Coming soon..."**; UK list is HTML | Not stated (UK: OGL v3.0) | DE 2026-09-04; UK 2026-01-23 |
| **CarneAtlas** | **39** | ~10 countries | — | — | — |

**Bottom line:** three of these are strictly and massively better on coverage, and two — FishBase and
ASFIS — are the authorities **EU law itself points at**. The only thing nobody has shipped is a
*downloadable, country-keyed* consolidated dataset of trade names: FishBase is language-keyed (has a
country column, but NC-licensed), ASFIS is language-keyed only, and the EU's country-keyed system has an
open-data page that says "Coming soon...".

**For the prior-art question: CarneAtlas's fish section is its weakest flank by a wide margin — 39
unsourced species against 36,761 in the resource EU law designates as authoritative.**
