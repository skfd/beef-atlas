# Notes: official / industry standards prior art

**Method:** `unece.org` is completely closed to automated fetching — Cloudflare 403s **both** WebFetch and
curl with a browser UA, and the archived copy of one landing page had itself captured a Cloudflare block
page. All UNECE material here came via **Wayback `id_` raw-asset URLs**. Two PDFs are stored truncated at
exactly 1,048,576 bytes, which is why the chicken standard's internals are unverified. Everything else
fetched from primary sites.

> **THIS THREAD OVERTURNS AN EARLIER FINDING.** Three other threads concluded UNECE is "English only",
> based on Stanford SearchWorks' catalogue record for the 2004 bovine edition. That was an inference from
> a catalogue field. This thread read the documents themselves and found a **five-language index**. The
> primary source wins.

## The short version
What CarneAtlas does informally — one cut, many national names — **already exists officially**, and the
trick that makes those systems work is **a number used as the language-independent key**. Four official
systems do exactly that:
- **UNECE** item codes with an **EN/FR/RU/ES/ZH** index, now aligned to WCO HS codes
- **USDA IMPS**, whose Spanish editions keep **identical item numbers**
- **URMIS**, with EN/ES retail name lists behind the same 4-digit numbers
- **Canada Pork's CPI codes**, stable across a **7-language** brochure set

**AUS-MEAT HAM** numbers survive intact into a full Japanese translation, but MLA disclaims it as
unofficial. The EU went furthest of anyone for exactly one species: **Reg. (EU) 2026/343** puts poultry
cut names in **23 languages in a single legal table**.

CarneAtlas has the photos and the country breadth and **no codes at all** — both its gap and its niche.

## 1. UNECE meat standards (WP.7) — multilingual after all
https://unece.org/trade/wp7/Meat-Standards

**Scope: 16 standards, not 4** — Bovine (ECE/TRADE/326), Ovine (308), Porcine (369), Chicken (355), plus
Veal, Caprine, Deer, Duck, Goose, Horse, Llama/Alpaca (368), Rabbit, Turkey (358), Processed Poultry Meat,
Edible Meat Co-products and **Retail Meat Cuts**. Porcine acknowledgements credit Australia, Bolivia,
Brazil, China, EU, France, Italy, Netherlands, New Zealand, Poland, Russia, US, Uruguay and GS1.

**MULTILINGUAL: YES — the single most important finding in the whole survey.** Each species standard
readable has a section **"5.1 Multilingual index of products"** with columns
**English / French / Russian / Spanish / Chinese**, keyed by item number. Verified in **Bovine 2007,
Bovine 2023 and Ovine 2012**. (In Porcine Rev.3 2018 it is still a bracketed placeholder and that edition
is English-only.) From the 2023 bovine text:
> item **1643 Brisket** = *Poitrine sans plat de côtes* / Грудино-реберный отруб / *Pecho* /
> 胸肉, 前胸肉, 胸肋肉

Whole standards are also published as **parallel EN/FR/RU PDFs**.

**Coded cuts: yes — the most developed scheme anywhere.** Two layers:
- **4-digit product/cut code, per species.** Bovine: "codes for bone-in cuts start with 1 and codes for
  boneless cuts with 2" — 1643 Brisket, 2240 Cube Roll, 2012 Inside cap. Porcine 4013 Leg Long Cut; ovine
  4800 Leg. **Codes are NOT global** — porcine 4013 and ovine 4800 are both 4xxx — so only the full code
  plus species disambiguates.
- **20-digit, 14-field "UNECE Code for Purchaser Requirements."** Worked porcine example
  `30401300111011122150` = porcine (30) + Leg Long Cut (4013) + chilled + hog/barrow + indoors +
  conventional feed + specified slaughter + specified post-slaughter + 0-5 mm fat + industry-standard
  quality + specified weight range + vacuum-packed + conformity not specified.
  Species codes: 10 beef, 11 veal, 20 deer, 30 porcine, 40 ovine, 50 caprine, 60 llama, 61 alpaca,
  70 chicken, 71 turkey, 72 duck, 73 goose, 74 rabbit, 80 equine, 90 co-products, 91 retail cuts.
- **Machine-readable:** the code holds **GS1 Application Identifier (7002)**, used with a GTIN in GS1-128
  barcodes.
- The **2023 bovine revision adds WCO Harmonized System alignment** — each index item carries its 6-digit
  HS code (0201 10/20/30 fresh-chilled, 0202 10/20/30 frozen).

**Free:** yes. "All material may be freely quoted or reprinted, but acknowledgement is requested." Print
carries UN Sales No. E.03.II.E.59, ISBN 978-92-1-116886-0.

**Last updated:** Bovine — **ECE/CTCS/WP.7/2023/24, 4 Sep 2023**, EN/FR/RU, listed first on the catalogue;
the document says it is "submitted to the Working Party for adoption" (78th session, Nov 2023) and
**adoption is unverified**. Earlier bovine: Rev.2, labelled by UNECE "(Revised 2015 version)", published
2016; Rev.1 2014; Rev.1 2012; 2007 EN/FR/RU; 2004 EN/FR/RU. Ovine Rev.1 "2012 edition", published 2013,
EN/FR. Porcine Rev.3 2018 EN only. Chicken 2013 EN/FR and 2007 EN/FR/RU. Standards reviewed three years
after publication.

**Size: 89 item codes** in the 2023 bovine multilingual index (32 bone-in, 57 boneless) — agent's own count
from the extracted index pages; the document states no total. (`2012` confirmed a real code — "Inside cap
/ Dessus / Tapa de nalga", HS 020130 — so 89 stands.) CarneAtlas lists 64 beef cuts.

### 1b. UNECE Standard for Retail Meat Cuts — the closest official analogue of all
https://unece.org/sites/default/files/2024-03/Retail_Meat_Cuts_2016_E.pdf (+ `_F`, `RetailMeatCuts-2016_R`)
"2013/2016 edition", 2016. Beef, pork, lamb, veal **retail** cuts, **EN/FR/RU**, free. Adopted as
ECE/TRADE/C/WP.7/2013/5 (69th session, Nov 2013); lamb and veal photos and descriptions added at the 72nd
session (Nov 2016) per ECE/CTCS/WP.7/2016/31.

**Every retail cut maps back to its wholesale item:**
> "Ribeye Steak, Boneless — **UNECE source No. 2240** Cube Roll"
> "Ribeye Steak, Bone in — No. 1604 Ribs prepared"
> "Country Style ribs, bone-in — No. 4140 Loin Long"

**That retail-name ↔ wholesale-code bridge, in three languages, is exactly CarneAtlas's layer.**

## 2. USDA IMPS and the NAMI/NAMP Meat Buyer's Guide
**IMPS** https://www.ams.usda.gov/grades-standards/imps — 11 documents. Dates read off the PDFs: General
Requirements (June 1996), QA Provisions (June 1997), **100 Fresh Beef / 200 Fresh Lamb and Mutton / 300
Fresh Veal and Calf / 400 Fresh Pork — all effective November 2014**, 500 cured pork (1992), 600 cured
beef (June 1993), 700 Variety Meats (June 1993), 800 Sausage (Nov 1992), Series 11 Fresh Goat (Oct 2001).
**Multilingual: partly** — Spanish editions of the fresh series only, keeping **identical item numbers**
(1100 Cubed Steak / 1100 Bistec Suavizado; 1103 Rib, Rib Steak, Bone-In / 1103 Espaldar, Bistec de
Espaldar, Con Hueso). **Coded: yes** (112 Ribeye Roll; 109D Roast-Ready Cover Off Short Cut Export Style;
402K Eye of Round; 716 Beef Tongue Short Cut; goat 11-2-00). **Free**, public domain. Illustrations are
**anatomical line drawings with Latin muscle names — no photographs.** Drafts stamped "DRAFT 9-30-2020"
plus two 2022-named lamb/veal files sit unfinalized while the live fresh series remain 2014.

**The Meat Buyer's Guide, 10th edition** — Meat Institute with AMSA.
https://www.meatinstitute.org/Meat_Buyers_Guide. Beef, pork, veal, lamb, processed, poultry; US;
**English only**; numbered — "summarizes USDA's IMPS" with "updated item numbers".
**PAID: $80 regular / $70 educational**, print only, currently out of stock. **10th edition announced
15 May 2026, ships 1 June 2026**; first published 1961. **The closest commercial prior art on the photo
axis** — a professionally photographed catalogue keyed to IMPS numbers — but $80, print, English, one
country.

## 3. AUS-MEAT and MLA
**Handbook of Australian Meat (HAM), 8th ed.** — AUS-MEAT Limited (AMPC/MLA joint venture).
**Free per-cut PDFs at `https://www.ausmeat.com.au/cutcodes/<NNNN>.pdf`** — publicly reachable but
**unlinked and unindexed**; `/cutcodes/` itself 404s. Australia/NZ; beef, veal, sheepmeat, goatmeat.
**Multilingual: no** — what it translates is *code systems*.
**Coded: yes, and it is the best cross-walk found anywhere.** Each cut PDF carries the **H.A.M. No** plus
**UNECE, NAMP, NZ MSG and AHECC** numbers and foodservice synonyms:
> **2140 STRIPLOIN** = UNECE 0010, NAMP 180, NZ MSG 1620, AHECC 0202.30.13/0201.30.13,
> a.k.a. Entrecote / New York Steak / Porterhouse Steak / Sirloin Steak (issued 2001, updated 07-Jun-2023)

Also 2000 TOPSIDE (NAMP 168, NZ MSG 1200) and 4621 RAM CARCASE. **The PDFs include studio photographs**
plus a carcase-location diagram. **Free/paid split:** print Handbook A$159.50 inc GST, but the **HAM app
is free** (iOS v3.0.2 2025-11-03; Play "Updated Aug 19, 2026") and the per-cut PDFs are free and
unauthenticated; the "Cut Code Search & Translation" tool sits behind free registration.

**MLA.** Consumer material has no codes (australianbeef.com.au/cooking/beef-cuts/, Meat Cuts app). Trade
material carries HAM numbers: the MSA Beef Primal & Sub-Primal Cuts poster ("Released: March 2018" —
TOPSIDE 2000, STRIPLOIN 2143, CUBE ROLL 2243, TENDERLOIN 2150, OYSTER BLADE 2303), and the **Aussie Beef
Cut Guide, an explicit HAM↔NAMP cross-reference**
https://www.foodservice.aussiebeefandlamb.com/contentassets/e1535f16c7494fc1b0fe37c4515bea3f/aussie-beef-cut-guide-2025.pdf
(created 2025-09-05; Striploin 2143 = Striploin 180, Cube Roll 2243 = Ribeye Roll 112).
**Multilingual: yes, verified** — Aussie Meat Academy https://www.aussiemeatacademy.com/en/cuts has a
working switcher for EN, AR, ID, JA, KO, MS, TH, VI (though "Cuts" there is a video tag, not a
catalogue); and MLA Japan's trade page https://www.aussiebeef.jp/b2b/ links a free **172-page Japanese
translation of HAM 8th edition with the HAM numbers intact** — ストリップロイン 2140, チャック 2260,
ランプ 2090, アイラウンド 2040, オイスターブレード 2303.
**MLA's own disclaimer inside it is the most telling sentence in this survey:** *"it is not an official
translation."* (That PDF sits behind an expiring third-party flipbook URL — not a stable citation.)

## 4. Canada (English/French)
**CFIA Meat Cuts Manual — the binding retail nomenclature (UMCNS / SNUCV).**
https://inspection.canada.ca/en/food-labels/labelling/industry/meat-and-poultry-products/meat-cuts
Beef, horse, lamb, pork, poultry, veal — each with a cut diagram, a skeletal diagram with Latin bone
names, cut descriptions, variety meats and a modifier list — plus a separate **ostrich** page whose table
runs **Latin muscle → EN → FR** (*iliofemoralis externus* → oyster → *sot l'y laisse*).
**Multilingual: yes, genuinely** — the PDF is a **single bilingual document** with names paired inline
(`4.1 Chuck/Bloc d'épaule`, `5.2.1.1 Porterhouse/Aloyau, gros filet`, `5.3.2.3 Eye of round/Noix de
ronde`). **Coded: no** — numbering is document outline, not item IDs. **Free.** Modified 2019-06-10 /
2019-08-12; bilingual 39-page beef PDF created 2019-07-16; GC Publications record **A104-471/2019-PDF**.
CFIA states the names **"must be used in labelling all beef, veal, pork, lamb, and poultry meat cuts"**,
coined names violating s.5(1) *Food and Drugs Act* and s.6(1) *Safe Food for Canadians Act*.

**CFIA Wholesale Meat Specifications Document (WMSD / DSVG)** — numbered, but **the numbers are
American.** 100 beef / 200 lamb / 300 veal / 400 pork. The page itself states the names, specifications
and item numbers are "identical to that found in the Institutional Purchase Specifications (IMPS)
documents ... USDA-AMS and the Meat Buyer's Guide ... North American Meat Institute."

**The rule tying both to law:** inspection.canada.ca meat-and-poultry-products page, section "Meat cut
nomenclature" (`#s1c2`) — **date modified 2026-06-17**, the freshest Canadian page found; assigns retail
names to the Meat Cuts Manual and wholesale names to the WMSD, exempting stewing beef, kebab, fondue,
small-piece meat, hip minute steaks and ground meat.

**Canada Pork "Pork Cuts & Specs" — the only Canadian-origin code scheme, and the most multilingual
source in the survey.** https://canadapork.com/canadian-advantage/pork-cuts-specs/ (FR at `/fr/...`).
**CPI codes** C200 Loin Bone-In, C201 Loin Boneless, C205 Short Cut Back Boneless, C210 Rib Rack Nine
Bone Frenched, C227 Tenderloin, C229 Rib Cap, C235 Sirloin — and **the French page carries the identical
C200-C235 codes with translated names** (*Filet*, *Longe avec os*, *Surlonge*). https://canadapork.com/tools/
groups brochures under **English, French, Spanish, Japanese, Korean, Chinese and Vietnamese**. Free; index
modified 2026-03-03. **Structurally the closest prior art of all** — browsable primal→sub-primal
catalogue, multilingual, per-cut identifier stable across languages — but one species, one country,
export-buyer framing.

**Canada Beef.** https://canadabeef.ca/cuts-by-colour/ (modified 2024-05-08) — consumer primal→cut
browsing with cooking method and tenderness; **no French** (`lang="en-US"`, no hreflang; `boeufcanada.ca`
does not resolve); no codes. Its Retail Merchandising Guide poster **does** map IMPS numbers to Canadian
retail names (167A Sirloin Tip Peeled → Quick Roast / Rotisserie / Oven Roast / Fast-Fry Steak /
Marinating Steak; also 171C, 171B, 184, 185A, 107, 124A).

**Beef Cattle Research Council** — grading and yield only (Canada Prime / A / AA / AAA, B1-B4, D1-D4, E;
yield 1-5); no cut chart, and the declared `/fr/` alternates serve English bodies.

**AAFC — nothing found.** The other cut-nomenclature records on publications.gc.ca are the **withdrawn**
CGSB standards *Beef cuts* **32.44-92** and *Lamb cuts* **32.48-92** (Dec 1992, converted to GCS 2014,
**withdrawn April 2020**), which did carry numbers — "Cut 114 – Shoulder Clod", "Cut 114A (1114R) –
Shoulder Clod, Roast Ready" — free at
https://publications.gc.ca/collections/collection_2017/ongc-cgsb/P29-5-032-044-1992-eng.pdf, with
separate FR editions. Historical only.

## 5. US checkoff explorers, and URMIS
**Beef. It's What's For Dinner. — Cuts.** https://www.beefitswhatsfordinner.com/cuts
**Multilingual: no** (`lang="en"`, no hreflang); Spanish exists only as PDF posters — genuinely useful
data, rendering cuts as *Aguayón, Arrachera, Diezmillo, Chuletón, Cuete, Empuje*.
**Coded: yes, two systems** in an "Industry Ids" box — **IMPS/NAMP** (Ribeye Steak 1112A, Flat Iron 1114D
PSO 1, Brisket Flat Half 120A) and "UPC" numbers that are **URMIS retail numbers** (Flat Iron 1166,
Brisket Flat Half 1622, Chuck Arm Steak 1050/1056). **Free**, including high-res photo downloads.
Actively maintained (© 2026 Cattlemen's Beef Board / NCBA), though the PDF posters lag the site (the file
named `Beef-Retail-Cuts-Chart-2018.pdf` is internally the 2021 artwork).
**Size: 154 entries** per the site's own AJAX endpoint, ~11 being primal/category overviews, so
**≈143 real cuts.** Per cut: aliases, description, industry IDs, photos, parent primal, cooking methods,
nutrition with USDA NDB number, recipes. **The closest single-species analogue** — but one country, one
language, and it carries the codes CarneAtlas omits.

**URMIS — Uniform Retail Meat Identity Standards** (established 1973 by ICMISC).
https://www.meattrack.com/urmis/ · US retail; beef, pork, lamb, veal.
**Multilingual: yes by design** — the nav exposes English **and Español** name lists for beef and pork
(lamb and veal English-only). **Coded: yes — 4-digit retail numbers, historically paired per USDA grade:**
Chuck Arm Pot Roast bone-in **1048** (Select) / **1863** (Choice); bone-in steak 1050/1865; boneless roast
1049/1864; boneless steak 1056/1871; Top Blade boneless 1144/1959; Flat Iron **1166/1981**. Distinct from
IMPS/NAMP (wholesale). **Free/paid: mixed** — narrative pages open, but **every actual name/code list
redirects to `login.php`**; no openly downloadable full list exists. Editions **1973, 1995, 2003, 2014**;
the 2014 overhaul followed 2012 NCBA / National Pork Board research, ran through USDA AMS and FSIS, kept
UPCs unchanged, set a 3-line/26-character label format citing 9 CFR 317.344.

**THE BEST ONE-LINE ARGUMENT FOR A SITE LIKE CARNEATLAS COMES FROM URMIS ITSELF:**
> "well over 1,000 different names had been given to the then 315 retail cuts of beef, pork, veal, and lamb."

Free secondary source reproducing URMIS numbers with photos:
https://agrilife.org/4hmeat/files/2018/01/Guide-To-ID-Meat-Cuts.pdf (68pp, AMSA / NCBA / National Pork
Board / American Lamb Board, 2013-14).

**Pork — National Pork Board.** https://pork.org/cuts/ is **not** a cut database: 12-13 broad category
pages, English only, **no codes**, free. The only real chart is the "Purchasing Pork" poster (~30 cuts,
© 2019, print code #03341 3/19) and it has **no stable URL** — the address printed on the poster,
`pork.org/purchasingpork`, now redirects to a checkoff facts page with no chart. On the 2013 renaming: the
*new names* are live at https://pork.org/cuts/pork-chops/ (Porterhouse, Ribeye, Sirloin, New York and
blade pork chops), but **no fetched page states the year 2013** or ties the renaming to URMIS by name.

## 6. UK — the AHDB Meat Purchasing Guide
https://ahdb.org.uk/mpg · PDF
https://projectblue.blob.core.windows.net/media/Default/Trade/MPG/MPG(9th-edition)_251008_WEB.pdf (122pp).
Beef, veal, lamb, mutton, pork; GB trade. **Multilingual: no** — no non-English text in the document, and
no translated URLs in the 14,227-URL sitemap.
**Coded: yes, but primal-scoped, not globally unique.** `Topside B001` = Topside; `Topside B016` = Topside
without *gracilis*; `Topside B018` = Main Topside Muscle (*semimembranosus*) — **while `Fore Rib B018` =
Tomahawk Steak.** Lamb L###, veal V###, mutton M###; **pork uses a separate bare 4-digit series** (1003
Forequarter bone-in, 1005 Shoulder round, 1029 Boston Butt bone-in rind on; ranges 1xxx-8xxx).
**Free** (public Azure blob, no auth). PDF created 2025-10-08, sitemap `lastmod` for `/mpg` 2025-10-31.
**Size: the cover states "over 700 ... cuts" and counting the extracted text gives 702** — **by far the
deepest single-country catalogue found.**
Cutting specs are a web layer: per-cut records at e.g. ahdb.org.uk/trade/beef/steaks-daubes-and-ribs/tomahawk-steak
(`Code: Fore Rib B018`), browsable via `ahdb.org.uk/mpgmeattype/{beef,lamb,mutton,pork,veal}`. Only the
PDF is demonstrably current; the web pages' sitemap dates are 2019. **No EBLEX/BPEX branding survives.**

**Quality Standard Mark: not a nomenclature, and dead.** Eating-quality assurance scheme set up 2004,
~2,500 members mostly independent butchers, closed to new members Oct 2021, **closed entirely 31 March
2022.** No cut codes or definitions.

**No UK statutory cut naming.** The Products Containing Meat etc. (England) Regulations 2014
(SI 2014/3001) Schedule 1 reserves only **processed** names — Burger, Economy Burger, Hamburger, Chopped X,
Corned X, Luncheon meat, Sausage, Meat pie, Pasty, Bridie, Scottish pie — each with minimum meat content;
**no anatomical cut name is reserved.** The general rule is only "label your food with a name that
represents the food honestly". **UK cut nomenclature is AHDB's voluntary trade reference, not law.**

## 7. EU and Codex
**(a) Carcase classification — grades only, no cut names.** Reg. (EU) No 1308/2013 (CMO) **Annex IV**
"Union scales for the classification of carcasses". Beef categories Z/A/B/C/D/E, conformation
**S, E, U, R, O, P**, fat cover **1-5** (hence EUROP/SEUROP; the Art. 7 reference quality is **R3**); pig
S-P by estimated lean-meat percentage; sheep A/B. The only anatomy is *presentation* and the conformation
regions "round, back, shoulder". Free; consolidated **2026-08-18**. Implementing acts agree: Delegated Reg.
(EU) 2017/1182 (its only cut words are the pig reference-dissection "four major cuts (shoulder, loin, ham
and belly)") and Implementing Reg. (EU) 2017/1184. **Orthogonal to a cut atlas.**

**(b) The one place the EU did CarneAtlas's job properly — poultry.**
**Commission Delegated Regulation (EU) 2026/343** of 6 October 2025, marketing standards for poultrymeat,
**repealing Reg. (EC) No 543/2008** — https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026R0343
*Currency correction worth flagging: 543/2008, the regulation usually cited here, ended validity
**2026-03-08**.*
Annex I has two tables — carcase names and **"Names of poultry cuts"** — laid out as **23 language
columns, every EU official language except Irish.** Verified row:
> EN "Chicken leg with a portion of the back" / FR "Cuisse de poulet avec une portion du dos" /
> DE "Hähnchenschenkel mit Rückenstück, Hühnerkeule mit Rückenstück" / BG "Пилешко бутче с част от гърба,
> прикрепен към него" / EL "Πόδι από κοτόπουλο με ένα κομμάτι της ράχης"

EN "breast fillet" carries **four French synonyms** ("filet de poitrine, blanc, filet, noix"). Cuts are
defined anatomically by bone and weight ratio ("the weight of the back does not exceed 25% of that of the
whole cut"), **named but not numbered**, and Art. 3(1) makes these names in every official language the
**legally required food name**. Published OJ L, 2026/343, 17.2.2026.
**The closest legal analogue to CarneAtlas that exists — and the EU did it for no other species.**

**(c) No general EU beef/pork cut nomenclature — but two narrow coded lists.**
- The statute says so itself: Reg. 1308/2013 Annex VII Part I, point III(2) — sales descriptions
  "**may be supplemented by** an indication of the name or designation of the pieces of meat or offal
  concerned." **Optional, undefined, left to trade.** (Annex VII *does* harmonise a multilingual table of
  **veal sales descriptions per country**: Belgium "veau / kalfsvlees / Kalbfleisch", Bulgaria "месо от
  малки телета", Spain "Ternera blanca", Greece "μοσχάρι γάλακτος", plus the reserved-term rule that
  veau/Kalb/ternera/veal/vitello/kalf/vitela/teletina may not be used above 12 months.)
- **Commission Implementing Reg. (EU) 2016/1240, Annex III Part IV "Specifications for intervention
  deboning"** — **13 beef cuts with `INT nn` codes**, the only coded EU red-meat cut list:
  INT 11 shank / *jarret arrière*, 12 thick flank / *tranche grasse*, 13 topside / *tranche*,
  14 silverside / *semelle*, 15 fillet / *filet*, 16 rump / *rumsteck*, 17 striploin / *faux-filet*,
  18 flank / *flanchet*, 19 fore-rib, 21 shin / *jarret avant*, 22 shoulder / *épaule*, 23 brisket /
  *poitrine*, 24 forequarter / *avant* — each with a seam-and-bone cutting instruction. Free; consolidated
  2018-02-07. **A real 13-cut × 24-language beef nomenclature, buried in a procurement annex.**
- **Combined Nomenclature chapter 02** (CN 2026 = Annex I to Reg. (EEC) 2658/87 as replaced by Commission
  Implementing Reg. (EU) 2025/1926), applies from 2026-01-01, free, all languages. **It goes finer than
  HS-6 — but only to bone-in primals**, with rib- and vertebra-precise legal definitions in the Additional
  Notes: compensated quarters 0201 20 20, forequarters "minimum of four and maximum of 10 pairs of ribs",
  brisket 0202 30 50, hams "includes at most the last lumbar vertebra" 0203 12 11, bellies "commonly known
  as streaky" 0203 19 15, sheep chines/best ends 0204 22 30, legs 0204 22 50 "cut at the sixth lumbar
  vertebra just under the ilium". Boneless collapses to one line per heading — so ~25 primals across four
  species and **nothing at retail-cut level**: no sirloin steak, no bavette, no picanha.
- **THE BEST EVIDENCE ANYWHERE THAT LEGAL CUT TERMS ARE NOT TRANSLATIONS OF ONE ANOTHER:** CN's EN "crop
  and chuck and blade cuts" and "brisket cut" (0202 30 50) appear in the French version as
  « découpes de quartiers avant dites **"australiennes"** » and « découpe de poitrine dite
  **"australienne"** ». **Same code, same anatomy, a completely different naming metaphor — inside one
  binding instrument.**

**(d) Codex Alimentarius — no cut nomenclature at all.** The only meat-hygiene code is **CXC 58-2005 Code
of Hygienic Practice for Meat** (PDF read: https://www.fao.org/input/download/standards/10196/CXP_058e.pdf,
52pp, EN/FR/ES/AR/ZH/RU). Its definitions cover Abattoir, Carcass ("The body of an animal after
dressing"), Dressing, Fresh meat; searching for `loin|brisket|sirloin|primal|nomenclature` returns nothing
and **every "cut" is a verb.** The **Codex Committee on Meat Hygiene is adjourned sine die** with one
standard to its name; the **Committee on Processed Meat and Poultry Products is abolished**.
**UNECE is the only global body doing multilingual coded cut nomenclature.**

## 8. Japan and Korea
**Japan — the official cut list exists, is named rather than numbered, and is small.**
- **JMGA 牛部分肉取引規格** (Beef Partial-Meat Trading Standard) https://www.jmga.or.jp/standard/beef-partial/
  — exactly **13** partial cuts: ネック, かた, かたロース, かたばら, ヒレ, リブロース, サーロイン,
  ともばら, うちもも, しんたま, らんいち, そともも, すね. **Only size is coded** (S/M/L by weight;
  サーロイン S <8.0 kg, M 8.0-10.5, L ≥10.5). Japanese only, free, page undated. Pork equivalent =
  **5 cuts** (6 if かた is subdivided).
- **食肉小売品質基準** (Meat Retail Quality Standard, MAFF notice)
  https://www.ajmic.or.jp/kumiai/2010pdf/p107-109.pdf — **11 retail beef labels** (6 for mixed slices),
  8 pork; last amended **2005-03-01**. **It already does CarneAtlas's job for imports:** 牛かたロース ⊃
  chuck roll; 牛サーロイン ⊃ striploin; 牛そともも ⊃ bottom (gooseneck) round, silverside.
- **The one Japanese source with numeric cut codes: 食肉標準商品コード 第2次バージョン** (Standard Meat
  Product Code, OFSI under a MAFF programme) https://www.ofsi.or.jp/file/task_edi/H13output/syoku_cv2.pdf
  — **5-digit code = 1-digit species + 3-digit 部位コード** (1 和牛, 2 国産牛, 3 輸入牛, 4 国産豚,
  5 輸入豚, 6 国産鶏, 7 輸入鶏). Beef: 310 ネック, 332 かたばら B（ブリスケット）,
  342 とうがらし（チャックテンダー）, 512 リブロース芯（リブアイロール）,
  622 ともさんかく（トライチップ）, 632 いちぼ（クーレット）, 644 しきんぼ（アイラウンド）;
  offal 821 タン, 826 ハラミ, 842 ハチノス. Free, Japanese only, **March 2002** — it reaches ザブトン-level
  and offal, i.e. CarneAtlas's granularity, but it is old and imageless.
- **Grading:** JMGA 牛枝肉取引規格 — yield A/B/C, quality 5-1, BMS 1-12, BCS 1-7, BFS 1-7; current scheme
  dates to **April 1988**; pork carcass standard revised **April 2022**. English and Chinese summaries
  exist but are **sold at ¥200**.
- **The most CarneAtlas-like Japanese government artifact:** MAFF's
  「牛、豚、鶏の部位を徹底解説！お肉丸わかり図鑑」 https://www.maff.go.jp/j/pr/aff/2009/spe1_02.html with a
  **bilingual JA/EN** beef poster (created 2020-09-08) — Neck, Rump, H-bone, Tenderloin, Chuck Flap Tail,
  Tri Tip, Chuck Tender, Brisket, Short Rib alongside ザブトン, トンビ, カイノミ, イチボ, ハラミ, ミノ,
  ハチノス. **Illustrated, named, diagram-numbered and bilingual — but one static PDF per species.**

**Korea — the strongest taxonomy anywhere, and the folklore number is wrong.**
- **소·돼지 식육의 표시방법 및 부위 구분기준** (MFDS notice on labelling and cut classification of beef and
  pork) https://www.mfds.go.kr/brd/m_211/view.do?seq=14389 — Korean only, free,
  **[시행 2019. 12. 1.] 고시 제2019-113호** (revision chain 1996 → 2019).
- **The real counts, read verbatim off the footer row of 별표 1 — `10개 부위 / 39개 부위 / 7개 부위 /
  25개 부위`** — i.e. **beef 10 대분할 + 39 소분할 = 49 official cut names; pork 7 + 25 = 32**, total 81.
  The same counts appear in the 2015 version, so the figure is stable. Beef 대분할: 안심, 등심, 채끝, 목심,
  앞다리, 우둔, 설도, 양지, 사태, 갈비; sample 소분할: 꽃등심살, 살치살, 부채살, 갈비덧살, 차돌박이,
  업진안살, 치마살, 아롱사태, 토시살, 안창살, 제비추리. 별표 3 gives per-cut seaming specs by named muscle
  **plus the anatomical term** (살치살 = 배쪽톱니근(복거근); 홍두깨살 = 반힘줄모양근(반건양근)).
- **Coded: no** — names only.
- **ON THE "120 CUTS" CLAIM: NOT SUPPORTED.** The figure appears nowhere in the notice; the official total
  is **49 beef / 32 pork**. The *direction* of the folklore is right — 49 legally mandated Korean beef
  names against Japan's 13 JMGA primals / 11 retail labels, or CarneAtlas's 64 beef cuts worldwide — but
  **120 is not a number this instrument produces, and no primary source for it was found.**
- **Grading:** 축산물 등급판정 세부기준 (MAFRA) — yield A/B/C, quality **1++, 1+, 1, 2, 3**;
  **[시행 2025. 2. 24.]**. Since 2019, 1++ beef must also print the marbling number.

**Korea is the best prior art on taxonomy, Japan's 食肉標準商品コード the best on stable identifiers, and
MAFF's poster the only government artifact that is illustrated, named and bilingual at once. None combines
photographs, cross-language equivalence and browsable per-cut records.**

## Could not verify
- **UNECE:** formal adoption of the 2023 bovine revision; internals of the **Chicken** standard (both
  Wayback copies truncated at exactly 1,048,576 bytes — same problem blocked Bovine Rev.2 2016);
  Cyrillic/Chinese glyphs in the Ovine 2012 index (columns confirmed from the header row); any live-site
  fetch of unece.org at all.
- **US:** printed dates on the 2022-named IMPS lamb/veal drafts; total cut counts for IMPS or the Meat
  Buyer's Guide; any item number printed inside the Guide's 10th edition; a Spanish Guide; whether Spanish
  IMPS exist for series 500-800; **the current full URMIS code list and its Spanish lists** (login-gated);
  the 2014 "Industry Guide for Meat Retailers"; the exact year of the pork retail renaming; a stable URL
  for the National Pork Board cut chart; the 154th beef entry (endpoint says 154, HTML yields 153).
- **Australia:** HAM 8th-edition year and ISBN from ausmeat.com.au itself (only from MLA Japan's translated
  colophon); total HAM cut count (no public index); whether the HAM app is multilingual; what the gated
  "Cut Code Search & Translation" tool does; **whether HAM numbers and UNECE cut codes are literally
  identical** (AUS-MEAT claims so; the PDFs list UNECE Species Code as a separate field — so treat the
  earlier "HAM codes == UNECE codes" quote with care); the Korean 호주식육편람 contents.
- **Canada:** Canadian Beef Information Gateway content (JS shell); whether CFIA diagrams are photos or
  line drawings; total cut counts in the Meat Cuts Manual or WMSD; what "CPI" expands to.
- **UK:** the "9th edition" designation (only in the filename — no edition statement, ISBN or year inside);
  whether any **BSI** standard on meat cuts exists (search pages are JS shells — neither found nor
  excluded); MPG print pricing.
- **EU / Codex:** whether a 2013 editorial amendment altered CXC 58-2005's definitions (Codex PDF host 403s
  with a JS challenge); contents of CXS 88/89/96/97/98-1981 and CXG 14-1991 (titles only); most CN 8-digit
  code↔name pairings had to come from the Additional Notes because the tariff table column-shifted on
  extraction.
- **Japan / Korea:** last-revision dates for both JMGA partial-meat standards (pages undated); **KAPE /
  ekape.or.kr content** (every content URL returned a JS shell or 404 — nothing is attributed to KAPE);
  JLIA and ALIC; whether a Korean notice later than 2019-113 exists (none visible, though Art. 10 mandates
  triennial review); any official English-language Korean cut list (none found); **the origin of the "120
  cuts" figure (not traced).**
