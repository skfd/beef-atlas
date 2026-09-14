# Prior art for CarneAtlas: cross-language meat-cut references

> **Filed into `beef-atlas` after the fact — read [`README.md`](README.md) first.** This survey was
> commissioned as prior-art research on carneatlas.com and written **without knowing this project existed**.
> Two consequences: it covers pork, lamb and fish alongside beef, and where it says an anatomy-keyed
> cross-tradition cut map is unbuilt, **this repo is that map**. `README.md` reconciles the two and says
> what is actually new here.

Research date **2026-09-13**. Subject: https://carneatlas.com/ — "A reference for meat cuts across
languages and traditions", 64 beef / 40 pork / 13 lamb cuts + 39 fish species across 10 countries, with
a photo-ID feature, a daily puzzle, and Amazon affiliate links.

Six parallel research threads, several of which fanned out further. Per-thread raw notes sit beside this file;
everything here traces to a page someone actually fetched. **Unverified claims are marked as such** —
several agents caught themselves about to repeat a search-engine summary as fact, and those catches are
recorded rather than smoothed over.

---

## The short answer

**Yes — a great deal of prior art, and it is not where you would expect.**

The equivalence data CarneAtlas is built on **has been compiled repeatedly, well, and by institutions —
for decades.** ABIEC's Brazilian cut book carries a genuine **12-language aligned glossary**. A
nine-column table covering Argentina/Spain/Brazil/Chile/Portugal/USA-UK/France/Germany-Switzerland/Italy
has existed since **2003**. USDA's IMPS beef spec is **fully bilingual EN/ES across 183 numbered items**.
The EU runs a **legally mandated** system of fish trade names across 27 member states in 24 languages.
Howard Swatland — emeritus at **Guelph** — published *Meat Cuts and Muscle Foods: An International
Glossary* in 2000, with a **2023** edition listed. (Nobody in this survey read it — see Open Loops.)

What does *not* exist is a **consumer-facing, browsable, many-country mapper**. The data is locked in
unattributed PDFs, trade specs and national documents that do not cross-reference each other. That gap
is real. But it is no longer unoccupied: **three sites launched into it within roughly the last year**,
CarneAtlas among them, and all three are anonymous or LLC-fronted.

**The most useful single finding:** UNECE standardises cuts **by anatomy with stable numeric codes, and
publishes a five-language index against them** (EN/FR/RU/ES/ZH). That is the pivot key every name-first
resource lacks. Its companion **Retail Meat Cuts** standard maps retail names back to wholesale codes in
three languages — structurally the same layer CarneAtlas occupies, done officially in 2013/2016.

> ⚠️ **This corrects an earlier conclusion in this report's own research.** Three threads concluded UNECE
> was English-only, inferring it from a Stanford catalogue field after `unece.org` 403'd them. A fourth
> thread reached the documents through Wayback raw-asset URLs and read the multilingual index directly.
> **The primary source wins: UNECE is multilingual.** The corrected claim is throughout below.

---

## What CarneAtlas actually is

Worth establishing before comparing it to anything, because none of this is on the site.

| Fact | Evidence |
|---|---|
| Domain registered **2026-03-31T20:19:34Z** | Verisign RDAP |
| Cut pages `datePublished` **2026-04-01**, fish **04-02** | JSON-LD |
| Timestamps cluster **within seconds** (ribeye 18:26:19, onglet 18:26:28, picanha 18:26:41) | JSON-LD — bulk generation, not incremental writing |
| Daily puzzle at **#29 on 2026-09-13** | `/guess`; back-counts to ~2026-08-16, matching a site-wide `dateModified` sweep |
| **One** Wayback capture in the domain's life (`/pork`, 2026-06-10) | CDX `matchType=domain`; homepage never archived |
| **Zero** public discussion | HN Algolia `nbHits: 0`; Lobsters, Product Hunt, Reddit via PullPush, GitHub all empty |
| No `/about`, `/privacy`, `/terms`, `/contact`, `/ads.txt` | all 404; the 701-URL sitemap has no legal or sources page |
| Solo operator | "As an Amazon Associate **I** earn..." — first person singular |
| Affiliate clicks instrumented per page and placement | `/go/amazon?...&position=curated_gear&pageType=cut&pageSlug=ribeye&country=US`; tags `carneatlas-20` and `carneatlas02-21` |

So: **five and a half months old, bulk-generated, anonymous, with no inbound footprint at all.** Roughly
117 cuts plus 39 fish species is a real corpus, and it is indexed and crawlable — but nobody has linked to it.

**It is better than a content farm, and it does cite sources — unevenly.** Cut pages carry a `citation`
array in JSON-LD and a rendered Sources block: ribeye cites Wikipedia + **USDA AMS IMPS Series 100** +
**NAMI Meat Buyer's Guide**; picanha cites **ABCZ**; onglet cites **Larousse Gastronomique**. Wikipedia is
always first. The names-by-country tables carry genuinely specific local knowledge ("Italy: boneless
ribeye is sold under the French loanword; bone-in is *costata*"), and the anatomical prose is correct
(rib cap = spinalis dorsi on the longissimus dorsi).

**Fish pages carry zero citations.** 4/4 sampled have no `citation` array, no Sources block, no
scientific binomial — tuna is labelled only with the family "Scombridae". **FishBase is not referenced
anywhere on the site.** That is the weak flank, and section 6 below quantifies how weak.

Two accuracy flags found in passing: the ribeye page gives the **UK** name as "Scotch fillet", which is
AU/NZ usage; and `/fish/robalo` is titled "Robalo in English: Snook", collapsing the European-Portuguese
sense (sea bass) with the Latin American one (snook).

---

## The comparison matrix

Beef cuts unless noted. "Countries" = distinct national naming systems actually enumerated.

| Resource | Cuts | Countries / languages | Cross-country mapping | Diagrams | Machine-readable | Licence | Last updated |
|---|---|---|---|---|---|---|---|
| **CarneAtlas** | 117 + 39 fish | 10 countries / 8 locales | **Yes — per-cut table** | borrowed from Commons | no | — | 2026-08 |
| **ABIEC Livro de Cortes** | ~36 coded | **12 languages**, + inline `(Chile: …)` on 72 rows | **Yes — aligned glossary** | yes | no (PDF) | n/s | frozen 2019/20 |
| **Lexicool / MAGyP nine-column** | ~40-50 | **9 country columns** (AR ES BR CL PT US-UK FR DE-CH IT) | **Yes — true matrix** | no | no (PDF) | **none — unattributable** | 2003 / 2007 |
| **Swatland, AMSA 2012** | varies | US vs **10 British/Scottish regional sources**, + Caribbean, MX, JP, KR, RU, NL, CL | **Yes — with per-cut concordance scores** | no | no (PDF) | free to read | 2012 |
| **Swatland, *International Glossary*** | unknown | "international" | **presumed — unread** | — | no (book) | paid | **2023 ed. listed** (ISBNs verified via OpenLibrary only) |
| **UNECE Bovine (ECE/TRADE/326)** | **89 item codes** (32 bone-in, 57 boneless) | **5 languages — EN/FR/RU/ES/ZH**, in a "Multilingual index of products" | **YES — one code, five names** | yes | GS1 AI (7002); OCA XML mirror | UN, free to reprint | **2023 rev. (adoption unverified)**; 16 standards in the family |
| **UNECE Retail Meat Cuts** | beef/pork/lamb/veal retail | **EN/FR/RU** | **YES — retail name → wholesale code** ("Ribeye Steak, Boneless — UNECE source No. 2240") | **photos** | no | UN, free | 2013/2016 |
| **USDA URMIS** | 4-digit retail nos. | **EN + ES name lists** | pairwise | yes | no | **lists login-gated** | 2014 ed. |
| **EU Reg. 2026/343 (poultry)** | poultry cuts | **23 languages, one legal table** | **YES — legally required name per language** | no | EUR-Lex | free | **OJ 17.2.2026** |
| **EU Reg. 2016/1240 Annex III** | **13 beef cuts, `INT nn`** | **24 languages** | **YES** | no | EUR-Lex | free | consolidated 2018 |
| **AUS-MEAT HAM per-cut PDFs** | beef/veal/sheep/goat | English | **best cross-walk found — HAM + UNECE + NAMP + NZ MSG + AHECC on one page** | **studio photos** | no | **free, unlinked** (`/cutcodes/NNNN.pdf`) | cut pages updated 2023 |
| **Canada Pork CPI codes** | C200–C235 | **7 languages** (EN FR ES JA KO ZH VI) | **YES — identical codes across languages** | yes | no | free | index 2026-03-03 |
| **CFIA Meat Cuts Manual** | 6 species | **EN/FR in one bilingual document** | **YES — names paired inline** | line drawings | no | free | 2019; rule page 2026-06-17 |
| **AHDB Meat Purchasing Guide** | **702 cuts** | English only | no | yes | no | free (Azure blob) | PDF 2025-10-08 |
| **Korea MFDS 고시 2019-113** | **49 beef (10+39), 32 pork** | Korean only | no | no | no | free | 2019-12-01 |
| **Japan 食肉標準商品コード** | 5-digit codes, offal included | Japanese only | no | no | no | free | **March 2002** |
| **USDA IMPS Series 100** | **183 numbered items** | **2 (EN + ES), genuinely parallel** | pairwise only | yes | no (PDF) | not stated | EN Nov 2014 / ES Mar 2015 |
| **AUS-MEAT HAM app** | beef/veal/sheep/goat | Australian | **HAM codes == UNECE codes** | yes + 3D | app | AUS-MEAT | v2.3.2, © 2026 |
| **Aussie Beef AU↔US chart** | ~35 | 2, **at code level** | **Yes — HAM no. beside NAMP no.** | yes | no (PDF) | MLA | undated, live |
| **Wikipedia "Cut of beef"** | — | **~22 countries** | **NO — `{|` occurs 0 times** | 10 countries' diagrams, **all reusable** | API, but prose | CC BY-SA 4.0 | 2026-08-25 |
| **Wikidata** | 54 in tree | median **6** labels/cut | **Cannot express it** — P17 on 2/54 | 32/54 | **excellent (SPARQL/CC0)** | CC0 | 2026-08 |
| **FoodOn** | **409 beef, 182 pork, 130 lamb** | **zero non-English labels** | no | no | yes (OWL) | CC BY | active |
| **AGROVOC `meat cuts`** | **7 narrower concepts** | **26 languages** | no — stops at "steaks"/"chops" | no | yes (SKOS API) | unverified | 2025-07-18 |
| **Wiktionary** | 72 EN entries | 2-23 langs/entry, **median low** | ad hoc `{{q}}` tags | no | **yes (Wiktextract/DBnary)** | CC BY-SA | 2026-09 dump |
| **FoodSubs / Cook's Thesaurus** | **59 beef** | **English only** | US trade synonyms only | no | no | **all rights reserved** | rebuilt, © 2026 |
| **Weidefleisch register** | ~60 coded | **de at ch us uk fr it** | **Yes — code-keyed register** | no | no (HTML) | n/s | unknowable |
| **Cutranslator** | 26 canonical | claims 89-190 regions | **Yes — interactive** | **none at all** | no | Albor Digital LLC | © 2026 |
| **Meat My Nation** | **18 ("demo data")** | 8 | intended | — | "API coming" | n/s | Phase 1 MVP |
| **EU Fish Commercial Names** | national lists | **27 states, 24 UI langs** | **Yes, legally mandated** | no | **"Coming soon…"** | n/s (UK: OGL v3.0) | DE 2026-09-04 |
| **FishBase** | — | **333,253 names / 372 langs / 262 countries / 30,302 species** | **Yes — has a country column** | photos | XML + S3 parquet | **CC BY-NC 4.0** | v06/2026 |
| **FAO ASFIS** | — | **13,965 species × 6 langs** | language-keyed, not country-keyed | no | **yes — 2 MB CSV** | ambiguous | ed. 2026.1 |

---

## The five tiers of prior art

### 1. Codified trade standards — accurate, coded, and sharing one spine
**UNECE** is the spine. AUS-MEAT states plainly that *"The HAM cut codes and the UNECE international cut
codes are the same, hence the app applies across international borders."* NAMP/IMPS numbers ride alongside
(the Aussie Beef chart prints HAM 2243 next to NAMP 112 for cube roll / ribeye roll; Canada Beef's tool
carries NAMP numbers too). AHDB's UK trade app catalogues **850+ cuts**.

**And the multilingual premise holds — this is the corrected finding.** Each readable species standard
carries a section **"5.1 Multilingual index of products"** with columns **English / French / Russian /
Spanish / Chinese**, keyed by item number. Verified in Bovine 2007, **Bovine 2023** and Ovine 2012:
> item **1643 Brisket** = *Poitrine sans plat de côtes* / Грудино-реберный отруб / *Pecho* / 胸肉, 前胸肉, 胸肋肉

Whole standards are published as parallel EN/FR/RU PDFs. (Porcine Rev.3 2018 is the exception — its index
is still a bracketed placeholder, English only.) The 2023 bovine index holds **89 item codes** — 32 bone-in
(1xxx), 57 boneless (2xxx) — against CarneAtlas's 64 beef cuts, and the 2023 revision adds **WCO
Harmonized System alignment**, each item carrying its 6-digit HS code. There is also a **20-digit,
14-field "Code for Purchaser Requirements"** that embeds species, cut, chill state, sex, housing, feed,
fat depth, weight range and packaging, and it carries **GS1 Application Identifier (7002)** for use with a
GTIN in GS1-128 barcodes.

**Its companion standard is the closest official analogue to CarneAtlas found anywhere.** The **UNECE
Standard for Retail Meat Cuts** (2013/2016, EN/FR/RU, free, with photographs) maps every retail cut back to
its wholesale item — *"Ribeye Steak, Boneless — UNECE source No. 2240 Cube Roll"*, *"Country Style ribs,
bone-in — No. 4140 Loin Long"*. **A retail-name ↔ wholesale-code bridge in three languages is precisely
the layer CarneAtlas occupies.**

Reaching any of this took work: `unece.org` **403s both WebFetch and curl with a browser UA**, and an
archived copy of one landing page had itself captured a Cloudflare block page. Everything above came via
**Wayback `id_` raw-asset URLs**. Two PDFs are stored truncated at exactly 1 MiB, which is why the Chicken
standard's internals stay unverified, as does formal adoption of the 2023 bovine revision.

A free machine-readable mirror also exists, though it is thinner than the PDFs: the Odoo Community
Association ships `product_meat_unece/data/unece_code_list.xml` —
**169 records, 16 species/product headers**, AGPL-3, `i18n/` holding only French, **abandoned on branch
13.0** and absent from 14.0-19.0.

⚠️ **Treat the HAM-equals-UNECE claim with care.** AUS-MEAT asserts the codes are the same, but its own
per-cut PDFs list UNECE Species Code as a *separate field* from the HAM number (2140 STRIPLOIN shows
"UNECE 0010" alongside NAMP 180 and NZ MSG 1620). Whether the cut numbers are literally identical is
**unverified**.

### 2. Export glossaries — where the real multilingual work was done
- **ABIEC's Brazilian Beef Cuts Book** is the best of anything found: a coded catalogue whose glossary is a
  true **12-language aligned table** (PT EN FR ES IT DE AR RU ZH KO JA FA), with rows like `B2111 Raquete
  / Oyster Blade / Paleron / Marucha / Copertina / Schaufelstück` — and it encodes *intra*-Spanish
  variation inline, **72 occurrences of "(Chile: …)"**. Frozen 2019/20. ABIEC's own page asks you to
  request it by email while two full copies sit openly on the same server.
- **The nine-column table** exists twice: Lexicool's undated 2003 PDF and Argentina's MAGyP glossary
  (source file "Glosario de cortes vacunos 2007.doc"). ⚠️ **Flagged inference:** both have an *identical
  nine-column country set in the same order*. The cells were not diffed. If they are the same underlying
  document, the count of independent multi-country tables drops by one. **Worth a diff before citing
  either.**
- **USDA IMPS is genuinely bilingual**, not a translated cover page: `Item No. 115A - Beef Chuck, Blade
  Portion, Boneless` ↔ `Pieza n.o 115A - Espaldilla, Porción de la Paleta, Deshuesada`, 71 pages each,
  183 numbered items, and the Spanish edition contains zero occurrences of "Chuck" or "Brisket" while
  carrying Lomo 141×, Costilla 66×.
- **OFAJ's 149-page FR↔DE butchery glossary (2003)** is the closest true analogue in spirit — real
  synonym sets (*aiguillette baronne* → `Hüftdeckel, Tafelspitze, "Bürgermeisterstück"`) and explanatory
  rather than word-swap equivalences. **And its preface names CarneAtlas's exact niche as the reason it
  stopped:** a more precise description *"supposerait l'étude détaillée de trop nombreuses appellations
  régionales, voire locales, qui sortiraient du cadre de ce glossaire."*

### 3. Encyclopedic and open data — broad labels, no country axis
Three findings, each independently verified, that together define the gap:

1. **Wikipedia has no cross-country equivalence tables.** `{|` occurs **0 times** in all 24,030 characters
   of "Cut of beef" wikitext — it is per-country prose definition lists. Same for the German, French,
   Italian and Portuguese articles. It covers ~22 countries with only **15 `<ref>` tags**, citing
   `livestrong.com`, `clovegarden.com` and **a bare JPEG**. **There is no Spanish article at all** —
   the language with the richest cut-name divergence. And of the 34 articles in `Template:Cuts of beef`,
   **33 are English/US names**; only Picanha is not.
2. **Wikidata structurally cannot express per-country naming.** Of 54 items in the cut-of-beef tree,
   **P17 (country) appears on 2, P927 (anatomical location) on 0.** Labels are per-*language*, not
   per-*country*: `Q2165995` flank steak has the Spanish label **"arrachera"** (Mexican) with alias
   **"vacío"** (Argentine) in one undifferentiated bucket. Nothing can say which is which. And the
   mappings are wrong in places — `Q6501598` sirloin steak has es=`solomillo`, **which is tenderloin.**
   The Lexeme layer, the technically correct home, holds **80 lexemes across 19 languages of which Nordic
   languages are 36 — and there are as many Sumerian cut lexemes (3) as Spanish ones, and more than
   French (2).**
3. **FoodOn, the best structured meat-cut vocabulary in existence, has zero non-English `rdfs:label`s** —
   409 beef, 182 pork, 130 lamb English classes, 134 IMPS cross-references, and ~180 non-English
   *synonyms* across ~83,000 labels.

Two near-misses worth knowing: **AGROVOC** has `meat cuts` in **26 languages** but exactly **seven
narrower concepts** (steaks, chops, loins, legs, shoulders, fillets, joints), none with children — it
stops one level above where cut data lives. **Cook's Thesaurus / foodsubs.com is alive and rebuilt**, with
**59 beef items** in the right shape, but English-only for meat and its terms **explicitly forbid
"preparation of derivative works"**.

**Legally mineable:** Wikidata (CC0, 24-31 labels on notable cuts), Open Food Facts (ODbL — French-first,
`brisket` appears 0 times but `entrecôte` 7 times), Wiktionary/DBnary (CC BY-SA), Commons diagrams (**all
31 files in `Cuts of beef diagrams` verified reusable**). **Not** FoodSubs.

### 4. National single-country references — the common case
Excellent within one naming system, structurally incapable of crossing: IPCVA (~80 Argentine cuts, ES/EN/ZH),
INAC Uruguay, **SAG Chile (33 cuts fixed by law under NCh 1596** — the only closed official list found),
PROVACUNO, Interbev/la-viande.fr, Embrapa, AMA Austria, Proviande Switzerland, Bord Bia ("Your Guide to
**12** Beef Cuts", and not interactive despite appearances).

The clickable-cow benchmarks live here. The US Checkoff's is **literally a 1990s HTML image map** —
`<img usemap>` with 10 `<area shape="poly">` hotspots over 9 primals, no SVG, no zoom. **Canada Beef's is
better and bilingual**: inline SVG, 9 sections, NAMP numbers, real technical descriptions, EN/FR toggle.

### 5. Consumer explainers — and the demand signal
Dozens of one-country expat posts. Two are worth naming for what they prove rather than what they contain:
- **"Separated by a Common Language" (2009)** frames the problem better than anything else found: *"It's
  not that the cuts of beef have different names in the two places, it's that they are different cuts of
  meat."* 62 comments.
- **A 24 January 2011 hobby blog post is still the state of the art for US↔Germany** — 65 comments running
  through **September 2024**, author still replying. **The loudest unmet-demand signal in the survey.**

One design idea stands out from this tier: **Carnes de Luxe grades each match as high / approximate /
variable** rather than asserting 1:1 equality. It is the only source found that models uncertainty.

---

## The three direct competitors

| | CarneAtlas | Cutranslator | Meat My Nation |
|---|---|---|---|
| Shape | reference + photo-ID + daily game | interactive translator | community equivalence browser |
| Corpus | **117 cuts + 39 fish, real** | 26 canonical cuts | **18 cuts, self-labelled "demo data"** |
| Reach claimed | 10 countries / 8 locales | "2144 routes", 190+ regions — *also* "89 source countries" | 8 countries |
| Imagery | Commons photos + diagrams | **none at all** | — |
| Attribution | none | "Albor Digital LLC" | none; `/about` 404s |
| Weakness | anonymous, fish unsourced | breadth reads **programmatic, not researched** — a guessed Afghanistan URL 404'd | **hollow**; "Phase 1 MVP" |

Also **MeatGrader** (iOS + Android), the only product pairing photo-ID with regional cut names — store
listing advertises "Regional cut names (US, Brazil, Argentina, Japan, Korea, and more)" and "10
languages", but **both stores declare Languages: English only**, and it has **100+ downloads, no
ratings**. And **BeefCuts3D**, a real 3D rotatable carcass with EN/DE synonyms, **$4.99, v2.0 shipped
three days before this research, 1 rating.**

The pattern across all of them: **the idea is being attempted repeatedly, by solo operators, and nobody
has traction.** MLA's Meat Cuts app is the install leader at 100K downloads — and has not been touched
since 2023. Five non-English cut apps return hard Play 404s, **including the official IPCVA nomenclator.**

---

## What is genuinely unoccupied

1. **A daily puzzle about cuts.** Verified absent from listdle.com's index. The only cut quizzes in
   existence are a **2017 Sporcle page (9,064 plays)** and a PurposeGames set (6,193 plays), both
   US-only, English, static, UGC. The one mobile attempt, Portuguese `jozhu.vacamugequiz`, **is delisted.**
   The daily-food-game genre is otherwise all word games.
2. **~~An anatomy-keyed cross-country name map~~ — withdrawn.** I claimed this; the standards thread
   disproved it. **UNECE already joins codes to five languages**, and its Retail Meat Cuts standard already
   bridges retail names to wholesale codes in three. What remains genuinely unbuilt is narrower: a
   **country-keyed** map (UNECE is *language*-keyed — it cannot say Mexico vs Argentina within Spanish),
   covering the ~10 consumer markets CarneAtlas targets, in a browsable interactive form rather than PDFs
   on a Cloudflare-walled UN site. Weidefleisch's de/at/ch/us/uk/fr/it register over ~60 cuts and
   **AUS-MEAT's per-cut PDFs** (HAM + UNECE + NAMP + NZ MSG + AHECC on one page, with studio photos, free
   at unlinked `/cutcodes/NNNN.pdf` URLs) are how close the trade has come.
3. **A downloadable country-keyed trade-name dataset.** For fish this is nearly built and then stops: the
   EU's consolidated system's open-data page says ***"Coming soon…"***. For red meat, **URMIS's EN/ES name
   lists are login-gated** with no openly downloadable full list.
4. **Pork and lamb.** Afterthoughts almost everywhere, **despite diverging more than beef across
   borders.** Wikipedia's "Cut of pork" is organised by anatomy with one regional subsection; there is no
   Wikidata class item for cut of pork or cut of lamb at all; Japan's official pork standard has **5 cuts**.
5. **Anything at all for the species UNECE covers and nobody else does** — deer, llama, alpaca, horse,
   rabbit, goat, and four kinds of poultry.

**Not unoccupied:** photo-ID (four apps), interactive name translation (Cutranslator), single-country
clickable diagrams (every beef board), the raw equivalence data (compiled repeatedly since 2003), and
**coded multilingual cut nomenclature — which UNECE has been doing since at least 2004.**

### The EU already did this properly — for exactly one species
**Commission Delegated Regulation (EU) 2026/343** (6 Oct 2025, OJ 17.2.2026, repealing Reg. 543/2008 whose
validity ended 2026-03-08) puts poultry carcase and cut names in **23 language columns — every EU official
language except Irish — in one legal table**, with cuts defined anatomically by bone and weight ratio, and
Art. 3(1) making the name in each language the **legally required food name**. EN "breast fillet" carries
**four French synonyms**. Nothing equivalent exists for beef, pork or lamb: Reg. 1308/2013 Annex VII says
sales descriptions *"may be supplemented by"* a cut name — optional, undefined, left to trade. The only
coded EU red-meat cut list is **13 beef cuts with `INT nn` codes buried in the intervention-deboning annex
of Reg. 2016/1240**, which is nonetheless a real 13-cut × 24-language nomenclature.

**And Codex Alimentarius has no cut nomenclature at all** — in CXC 58-2005 every instance of "cut" is a
verb, the Committee on Meat Hygiene is adjourned *sine die*, and the Processed Meat committee is abolished.
**UNECE is the only global body doing this.**

---

## Fish is the weakest flank, by orders of magnitude

CarneAtlas: **39 species, unsourced, no binomials.** Against:

- **FishBase: 36,761 species, 333,253 common-name records, 372 languages, 262 countries** — counted from
  the v26.06 parquet snapshot, downloaded and parsed. **~777× the species count.** *Salmo salar* alone
  carries **216 names across 39 languages and 45 countries** — more name variation than CarneAtlas's
  entire 39 × 10 grid. Free per-species XML API, no key. **CC BY-NC 4.0 — the NC clause matters for an
  affiliate-monetized site.**
- **FAO ASFIS: 13,965 species items × 6 languages**, one permanent 3-alpha code each, in a **2 MB CSV at
  one URL**. Fill rates counted: EN 73.6%, FR 41.8%, ES 35.2%, ZH 19.3%, AR 14.9%, RU 4.3%.
- **EU Regulation 1379/2013 Article 37** requires every member state to publish accepted commercial
  designations *"in the official language or languages of the Member State"* plus *"any other name or
  names that are accepted or permitted locally or regionally"* — **exactly CarneAtlas's data model, as
  law.** Germany's list is on its **117th amendment (Stand 04.09.2026)** with 974 designations; Ireland
  has 542 English + 415 Irish; the UK's is **HTML tables under OGL v3.0**.

**And the regulation names FishBase and FAO ASFIS as the scientific-name authorities.** The two resources
that dwarf CarneAtlas's fish section are written into EU law — and the site cites neither.

---

## Findings that would change a data model

Three, all from primary sources, all cheap to get wrong:

1. **A name→cut lookup is not a function.** In Italy, *cappello del prete* means only the terminal part of
   the dorsal muscle in Turin but the whole muscle in Sciacca; *osso buco* is inner thigh in Milan and
   rear hock in Sciacca; *fesa* is outer thigh in Bari and inner thigh in Sciacca. **A naive many-to-one
   schema will silently return wrong answers.**
2. **Sources contradict each other, and the unit of variation may be the city, not the region.** Carne
   Genuina puts *rotolo di coscia* in Milan where Wikipedia puts *Magatello*. Any such dataset needs a
   **per-claim source field**. (Reported invariant: *filetto* means the same everywhere.)
3. **Cuts are not coextensive across traditions, so equivalence is an approximation.** US carcasses split
   at the **12th/13th rib**, Brazilian at the **5th/6th**. Swatland explains sirloin/*surlonge* means
   anterior in the UK and France but posterior in the US and Australia. Lhuissier (2002) establishes cut
   names as **contested administrative artefacts, not natural kinds**. Carnes de Luxe's high/approximate/
   variable grading is the right response.

A fourth, and the cleanest proof of point 3 anywhere: **the same legal code carries a different naming
metaphor in different languages of the same instrument.** In the EU's Combined Nomenclature, code
0202 30 50's English text reads "crop and chuck and blade cuts" and "brisket cut"; the French text of the
same code reads « découpes de quartiers avant dites **"australiennes"** » and « découpe de poitrine dite
**"australienne"** ». Same code, same anatomy, and one language names it by butchery while the other names
it by country of origin — inside one binding document.

**And the strongest one-line justification for a site like CarneAtlas comes from URMIS itself**, explaining
why it was founded in 1973: *"well over 1,000 different names had been given to the then 315 retail cuts of
beef, pork, veal, and lamb."*

### Two folklore numbers, checked
- **Korea does not have ~120 named beef cuts.** The MFDS notice (고시 제2019-113호) footer row of 별표 1
  reads `10개 부위 / 39개 부위 / 7개 부위 / 25개 부위` — **beef 10 primals + 39 sub-cuts = 49 official
  names; pork 7 + 25 = 32.** The same counts appear in the 2015 version, so it is stable. The *direction*
  of the folklore is right — 49 legally mandated Korean names against Japan's 13 JMGA primals — but **120
  is not a number this instrument produces, and no primary source for it was found.**
- **Japan's official list is small and named, not numbered:** JMGA's beef partial-meat standard has exactly
  **13** cuts, the retail quality standard **11** labels, and the pork standard **5**. The one Japanese
  source with real cut codes, 食肉標準商品コード, reaches ザブトン-and-offal granularity with 5-digit IDs —
  and dates from **March 2002**.

Also worth correcting: **France does not have the regional naming variation one would assume.** Every
source was checked for it and none found. What France has is a **two-register split** — traditional
butcher names versus simplified supermarket labels imposed by a July 2014 decree, artisanal butchers
exempted, contested in the Senate in 2015 — **and no source publishes a crosswalk between the two
registers.** That missing crosswalk is the real French gap. Meanwhile **Germany vs Austria vs Switzerland
is real and institutional**: Germany follows DLG rules, Austria the *Wiener Teilung* descending from
Vienna's 1873 Qualifikationstabelle. `Hüftdeckel` (DE) = `Tafelspitz` (AT); the forequarter is *Bug* in
Vienna but *Laffe* in Swiss German.

---

## Method notes for anyone re-running this

- **unece.org returns 403 to everything** — three agents, multiple routes, curl with browser UA, the UN
  digital library. The OCA XML mirror is the way in.
- **Google Play defeats WebFetch entirely** (JS truncates before data) but yields to `curl` + browser UA.
  Apple pages fetch fine. `beefitswhatsfordinner.com` and `bordbia.ie`: **403 to WebFetch, 200 to curl.**
- **reddit.com and seriouseats.com are blocked** to this user agent, so **forum demand is genuinely
  unmeasured** — the one real hole in this survey.
- **PDFs must be downloaded and text-extracted, not fetched.** The Lexicool, Swatland, ABIEC, IMPS and
  German BLE findings exist only because agents ran `pdftotext` locally.
- **WebSearch's US-only bias did not bite** on non-English queries — ES/PT/FR/DE/IT query strings have no
  English homographs, so native domains surfaced anyway. What limited coverage was **fetch failures and
  data trapped in images** (Austrian tables as PNG, Italian regional dictionary as image tables, Spanish
  tables JS-loaded).
- **Dates are mostly worthless.** Auto-renewing "© 2026" with no real revision date is the norm; across
  the entire Italian set exactly one item showed a verifiable recent revision.
- **Stale official documentation is a trap.** FAO's own catalogue still describes ASFIS v2020.1 (13,420
  items, EN/FR/ES only) for a file that now has 13,965 items and six languages; `ASFIS_Structure.pdf`
  carries 2008 filesystem paths and documents field names that no longer exist.

---

## Open loops

- **Diff the Lexicool 2003 PDF against the MAGyP 2007 glossary** — same nine columns, same order. One
  document or two?
- **The French Meat Academy SKOS thesaurus** (1,519 concepts, bilingual FR/EN definitions), described in a
  *Meat Science* paper at https://www.sciencedirect.com/science/article/abs/pii/S0309174022001176 —
  **would be the best structured prior art if the file can be found.** Paywalled abstract; SKOS file not
  located. Related and openly licensed: the **Thésaurus de la viande**, https://doi.org/10.15454/pb5qxc
  (Kombolo et al. 2022, 1500+ concepts, one category is *découpe*) — **French only**.
- **Swatland, *Meat Cuts and Muscle Foods: An International Glossary*, 2023 edition** — the most relevant
  published work in existence, and nobody read it. Guelph author; possibly in the local library system.
- **Trypuz et al. (2016)**, "Machine-Understandable and Processable Representation of UNECE Standards for
  Meat" (https://doi.org/10.1007/978-3-319-49157-8_12) — paywalled; **do not assume it handles
  multilingual naming.**
- A 2014 Venezuelan paper whose title is precisely a Spanish↔North-American cut-name mapping, with **no
  DOI, no venue, no authors** (Semantic Scholar paperId `14cee89716f570662b60e6211021f1fe7c6d15d7`).
- The **CMA 13-language "Meat Cuts — European" glossary** — ProZ 403s on every attempt and publisher CMA
  was dissolved. Probably dead.
- **Formal adoption of the 2023 UNECE bovine revision** (ECE/CTCS/WP.7/2023/24) — the document says it was
  "submitted to the Working Party for adoption" at the 78th session, Nov 2023. Unconfirmed.
- **The UNECE Chicken standard's internals** — both Wayback copies are truncated at exactly 1 MiB. Same
  problem blocks Bovine Rev.2 2016.
- **Whether HAM cut numbers and UNECE cut codes are literally identical.** AUS-MEAT says yes; its own PDFs
  list them as separate fields. Worth settling, because it decides whether one crosswalk or two is needed.
- **The full URMIS code list and its Spanish lists** — login-gated, no subscription price found. The freely
  available AMSA/NCBA secondary source (agrilife.org 4hmeat guide, 68pp) reproduces the numbers with photos.
- **The origin of the "120 Korean cuts" figure** — not traced to any source.
- The `unece.org` Cloudflare wall is worth one manual attempt from a real browser; everything in section 1
  came through Wayback.
