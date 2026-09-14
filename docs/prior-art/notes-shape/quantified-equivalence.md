# Quantified partial equivalence between cutting systems — prior art

**Summary.** Almost nobody has done this. The one real methodological ancestor, **Swatland (2012)**,
is confirmed and its metric is now known exactly — and it is *not* what this project computes.
Swatland's "cut match" is a **name-anchored binary indicator summed over sources**: for each US primal
and each of ten British/Scottish cutting charts, score **1 if a cut of the *same name* overlaps in
location, 0 otherwise**, then sum to an integer 0–10. Gradation comes only from *aggregating over
sources*, never from measuring how much of one cut lies inside another; and the score is undefined
whenever the two systems use different words, which is exactly the case the project's percentages
exist to handle. His other four tables (US↔Caribbean/Mexico/Japan/Korea/Russia/Netherlands/Chile) carry
**no numbers at all** — he says the listed cuts have "a major overlap" but "seldom share identical
outlines" and leaves it there. Everything else found is binary by construction: the
**AUS-MEAT HAM per-cut PDFs** assert one-to-one crosswalks to NAMP/NZ MSG/AHECC and demonstrably lose
information doing it (HAM 2240 *and* 2243 both → NAMP 112); the **Trypuz et al. (2016)** UNECE ontology
is *reported* to be SKOS plus a "prepared from" partonomy, with no cross-standard alignment layer —
**but its abstract is paywalled and elided, so everything about its contents is UNPROVEN hearsay from
search summaries**; the largest cross-country cut table ever published,
**Huerta-Leidenz (2013)** for USMEF (42–52 US cuts × 35+ countries), carries an explicit author
disclaimer that it does **not** present anatomical equivalence. No paper in meat science was found that
computes a Dice/Jaccard/overlap coefficient between two partitions of the same carcass.
**Verdict: this project's overlap percentages have an ancestor in *intent* (Swatland) and none in
*method*.**

**Side question settled (§4.1): AUS-MEAT HAM item numbers ARE UNECE item numbers** — 1643 Brisket,
2012 Inside Cap, 2240 Cube Roll all match, and both systems obey "bone-in starts with 1, boneless with
2". HAM is a **superset**: it adds sub-variants (2140/2143 Striploin, 2240/2243 Cube Roll) that UNECE's
one-code-per-cut index lacks. The confusingly labelled "UNECE Species Code" field on the per-cut PDFs
is a *separate* field holding `0010` = beef on every cut; it is not a cut code and does not contradict
the identity.

---

## 1. Swatland (2012) — the one true ancestor. RUN TO GROUND.

**Citation.** Swatland, H. J. 2012. "History and Language of International Meat Cutting."
*Proceedings of the 65th Annual Reciprocal Meat Conference*, American Meat Science Association.
AMSA International Lectureship presentation. 7 pp.
PDF: https://meatscience.org/docs/default-source/publications-resources/rmc/2012/26_swatland_r2.pdf
*verified: downloaded with curl, text extracted locally with pdftotext.*

**DOI: none.** CrossRef bibliographic query for the title returns only unrelated Swatland items
(`https://api.crossref.org/works?query.bibliographic=History+and+Language+of+International+Meat+Cutting+Swatland`
→ *Meat Research in Argentina* 10.1016/j.meatsci.2007.10.010, etc.). AMSA RMC proceedings are not
DOI-registered. **The meatscience.org URL is the citation.** *verified: CrossRef API fetched.*

Author affiliation as printed: "Howard J. Swatland, Ph.D., Emeritus Professor, University of Guelph,
33 Robinson Avenue, Guelph, Ontario N1H2Y8, Canada. swatland@uoguelph.ca"

### 1.1 How the score is defined — verbatim

> "Let us ignore small anatomical differences in how the cuts are made, and look only at the names
> for the primal cuts (Table 1). The cutting charts used are those shown by Swatland (2004, Figures
> 57 - 64, 66, and 229). **If a US cut overlapped with a British cut of the same name, it scored 1,
> with 0 for a mismatch by location.** In Table 1, the cut match shows the degree of concordance"

And on the limits he himself flags:

> "There is no concordance for shank, but this simply may be a difference in English usage; if we
> substitute shin for shank, the score is a perfect 10."

> "The declining source match (5, 3, 2) might be due to chance, but also it may be showing the
> divergence with time between the United States and Britain."

### 1.2 What the metric actually is

- **Unit of comparison:** the *name* of a primal cut, checked against *location on the carcass*.
  Not muscles, not mass, not geometry, not volume.
- **Atom:** strictly **binary** — 1/0 per (US primal × British source) cell.
- **Gradation:** only by **summation over sources**. "Cut match" = row sum, 0–10 (10 British sources).
  "Source match" = column sum, 0–9 (9 US primals).
- **Size:** **9 US primal cuts × 10 British/Scottish sources = 90 binary cells.** Two systems
  (US vs Britain), one species (beef), primal level only.
- **Fatal restriction for this project's purpose:** the indicator is **conditional on name identity**.
  A cut that occupies 70% of the same anatomy under a *different* name scores 0, identically to a cut
  sharing nothing. The score measures *linguistic* survival of a name across cutting traditions, and
  he says so — the section that follows Table 1 is headed "LINGUISTIC SURVIVAL." It is a
  **philology metric, not a geometry metric.**

### 1.3 Table 1 reconstructed (pdftotext jumbles the columns; this grid is arithmetically verified)

Sources: (A) England 1816; (B) England 1876; (C) England 2000; (D) West of England; (E) Liverpool;
(F) Northeast England; (G) Manchester; (H) English Midlands; (I) London; (J) Edinburgh.

| US primal | A | B | C | D | E | F | G | H | I | J | **Cut match** | Archaic | Possible origin |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sirloin | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** | Surloine | Surlonge (Old French) |
| Loin    | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | **2** | Loyne | Lumbus (Latin) |
| Rib     | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | **10** | Ribb | Rif (Norse) |
| Chuck   | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | **4** | Chock | [?]oche (Old French) — glyph garbled in extraction |
| Round   | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | **4** | Rounde | Rotundus (Latin) |
| Flank   | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | **8** | Flanc | Hlanke (Frankish) |
| Plate   | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | **1** | Plater | Platus (Greek) |
| Brisket | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | **10** | Brusket | Brjósk (Norse) |
| Shank   | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** | Sceanca | Schenken (German) |
| **Source match** | **5** | **3** | **2** | **4** | **4** | **5** | **3** | **4** | **5** | **4** | 39 | | |

**Verification:** the 1/0 rows above are **as extracted from the PDF**, not reconstructed to fit. The
check is that they validate against the independently printed margins: the printed cut-match column
(0,2,10,4,4,8,1,10,0) and the printed source-match row (5,3,2,4,4,5,3,4,5,4) both sum to **39**, and
**every one of the ten column sums computed from these extracted rows reproduces the printed
source-match value exactly.** That is strong evidence the row extraction was not scrambled by
pdftotext. *(It is not a uniqueness proof — a 0/1 matrix with given margins is generally not unique —
so the claim is "the extracted rows reproduce all ten printed column sums", not "this is the only
possible grid".)*

### 1.4 Tables 2–5 — no numbers whatsoever

The author's own statement of what those tables mean, verbatim, and the single most important sentence
in this thread:

> "The tables show the international names for primal cuts with **a major overlap** with the US cuts,
> which, as one would expect, **seldom share identical outlines**; reference to the source material may
> help (Swatland, 2004)."

So he *recognises partial overlap as the central phenomenon* and explicitly declines to quantify it.

- **Table 2** — US value-added cuts → **anatomy (muscle names)** → Caribbean name. This is the only
  table that is muscle-keyed. E.g. `Santa Fe / Gracilis / Cañada`; `Tucson / Semimembranosus / Cañada`;
  `Denver / Serratus ventralis / Falda de morrillo o tapa de cogote`;
  `Delmonico / Longissimus dorsi, mutifidus dorsi, spinalis dorsi and complexus / Filetillo`.
  Note **four US cuts all map to Caribbean "Cañada"** — many-to-one, unquantified.
- **Table 3** — US ↔ Mexico / Japan / Korea, beef, 9 primals. Partiality is expressed in *prose
  qualifiers inside the cell*, not numerically: `Sirloin / Cadera / Ranichi / Suldo, anterior`;
  `Loin / Lomo, posterior / Roin / Chaekeut`; `Round, hip / Pierna / Sotomomo, lateral + Uchimomo,
  medial / Suldo, posterior + udun`; `Plate / Pecho, anterior / Tomobara / Kalbi, dorsal`;
  `Brisket / Tapa de pecho / Katabara / Kalbi, ventral`.
  **The "+" and the "anterior/posterior/lateral/medial/proximal/distal" tags are the closest thing in
  the literature to a partial-overlap notation — and they are ordinal at best, not numeric.**
- **Table 4** — US ↔ Mexico / Japan / Korea, **pork**, 6 primals. `Shoulder / Cabeza de lomo /
  Kata + Ude / Abdari, Kalbi + Moksim`. Two cells are `--` (no equivalent).
- **Table 5** — US ↔ Russia / Netherlands / Chile, beef, 9 primals. `Sirloin / Tazobedrennaya,
  proximal / Dikke lende / Punta de ganso + Asiento`; `Round, hip / Tazobedrennaya, distal / Stomp /
  Pollo ganso, posta negra + posta rosado`; `Chuck / Scheynaya + Lopatochnaya / Schouder / Choclillo +
  paleta`. Growth figures quoted are **trade volumes, not equivalence** (Russia +82% to 48 k t;
  Netherlands +27% to 15 k; Chile +166% to 4 k; USMEF 2012, Dec 2011 data).

### 1.5 His own stated plan — relevant to this project's positioning

> "I think now is the time to dump the contents of my book into a Wikipedia type of website, check the
> content, improve the graphics, and let it develop as a community effort. I am not so sure it should
> be a public effort--some members of the general public have some strange views about meat cutting,
> while a minority are downright hostile. Thus, a secure server and a responsible committee of
> contributors and reviewers would produce the best result."

**No evidence was found that this website was ever built.** (See §2.3.) The project therefore occupies
a slot its most qualified predecessor publicly identified in 2012 and never filled.

Also worth recording, his framing of *why* this matters to science rather than trade:

> "the root cause is almost always that the authors do not know the name of their source meat cut and,
> hence, cannot identify the muscles contained in it. ... Do you really think you could publish a paper
> in a geology journal if you forgot where you found your rocks?"

---

## 2. *Meat Cuts and Muscle Foods: An International Glossary* — bibliographically pinned, text still unread

### 2.1 Editions (verified)

| Ed. | Year | Publisher | Pages | ISBN-10 / ISBN-13 | Source |
|---|---|---|---|---|---|
| 1st | 2000 | Nottingham University Press | 250 | 1897676301 | OpenLibrary OL6891899M, LCCN 00559946, LC TX373 .S83 2000 |
| 2nd | 2004 | Nottingham University Press | vii + 258 | 1904761151 / 9781904761150 | OpenLibrary OL17623433M, OCLC 56444546, Dewey 664.9029 |
| 2nd (reissue) | 2023 | Nottingham University Press | 266 | 9781789182903 | WebSearch of AbeBooks/Amazon/thegreatbritishbookshop listings |

- OpenLibrary API (`https://openlibrary.org/api/books?bibkeys=ISBN:1904761151,ISBN:1897676301&format=json&jscmd=data`)
  *verified: fetched.* Notes on the 2004 record: "Previous ed.: 2000. Includes bibliographical
  references (p. 241-258)." Subtitle recorded as "[an international glossary]" — **in brackets, i.e.
  supplied by the cataloguer, not on the title page.**
- The **2023 ISBN 9781789182903 is in the 978-1-7891-82 block (5m Books / 5m Publishing)**, consistent
  with a reissue of the 2nd edition under the imprint that absorbed Nottingham University Press.
  *UNPROVEN:* no publisher page for the 2023 printing was fetched; the year, page count and ISBN come
  from **WebSearch result summaries of retail listings only** and the retail listings themselves were
  not opened. Treat "2023 edition" as **a reprint of the 2nd edition, not a third edition** — the
  small page-count gap and the identical blurb both point that way, but it is not proved.

### 2.2 Structure — the decisive point, from the publisher's blurb

> "Wholesale and retail meat cuts are described and **cross-referenced** - many being clearly
> illustrated and labelled - **so that the reader may start with a country, or with the name of a
> specific meat cut to find the country of origin.**"

> "For this second edition, information for ten countries has been added or expanded, bringing the
> total to **51**. Languages added including Urdu, Yoruba, Ibo and Hausa, plus many extra names in
> Arabic and Latin-American Spanish."

> "Cutting patterns for beef, pork, lamb, game, poultry and fish are featured, plus a number of
> invertebrates such as crabs, lobsters, shrimp, squid and scallop that also produce striated muscle."

**This is a bidirectional name↔country index, not a comparison matrix and not a scoring scheme.**
51 countries is more than any other single source found anywhere in this survey.

### 2.3 Accessible text — a partial win

- **Google Books** id `9yGrqlv8ZfgC`, 2004 ed., **"No eBook available; no preview shown"**. No TOC, no
  "Common terms and phrases". https://books.google.com/books/about/Meat_Cuts_and_Muscle_Foods.html?id=9yGrqlv8ZfgC
  *verified: fetched (via the books.google.ca redirect).*
- **archive.org: zero results.** `https://archive.org/advancedsearch.php?q=title%3A%28%22meat+cuts+and+muscle+foods%22%29&output=json`
  → `numFound: 0`. **No lending copy exists.** *verified: fetched.*
- **Google Books API and OpenLibrary full-text: not available** (`books.googleapis.com` returned HTTP 429
  quota-exhausted for this environment; recorded so a later run knows to retry).
- **`swatland.net` does not resolve** (curl: connection never established, for both http and https).
- **`uoguelph.ca/~swatland/` → 404. `animalbiosciences.uoguelph.ca/~swatland/` exists but 403s to curl.**
- ✅ **BUT: the whole Guelph directory is in the Wayback Machine with an open directory listing.**
  https://web.archive.org/web/20180724191641id_/http://animalbiosciences.uoguelph.ca/~swatland/
  *verified: fetched.* It holds ~80 files: `ch1.htm`…`ch9_2.htm` (a full textbook), `b4a-z.htm`,
  `Final.html`, `INTRO.html`, `Lectures.html`, figure GIFs, and `HTML10234.tgz` (**4.2 GB**, not fetched).
  Enumerated via the CDX API:
  `https://web.archive.org/cdx/search/cdx?url=animalbiosciences.uoguelph.ca/~swatland/*&output=json`

#### `b4a-z.htm` — an A–Z glossary, free, full text, 199 KB
https://web.archive.org/web/20190814181918id_/http://animalbiosciences.uoguelph.ca/~swatland/b4a-z.htm
*verified: downloaded and parsed locally.* File date **1998-11-02**; `<META Generator="Microsoft Word 97">`.

**This is the only Swatland glossary text anybody on this project has read.** But be precise about what
it is and is not:
- **332 headwords**, running ABDUCTOR POLLICIS LONGUS → YELLOWTAIL FLOUNDER.
- Composition is roughly: **veterinary muscle anatomy** (~150 entries: BICEPS FEMORIS, SEMIMEMBRANOSUS,
  SERRATUS VENTRALIS THORACIS…), **fish and shellfish species** (~100: ANCHOVY, DUNGENESS CRAB,
  LUMPFISH…), and only **~50 meat-cut entries**, overwhelmingly North American
  (ARMBONE CHUCK, BOTTOM ROUND, CHICAGO ROUND, DIAMOND ROUND, NEW YORK ROUND, SHORT HIP OF BEEF,
  SQUARE CUT CHUCK OF BEEF, TRIANGLE OF BEEF, WING OF BEEF, SWISS STEAKS, LONDON BROIL) with a thin
  French seam (BIFTEK DE CONTRE FILET, CUISSE, FLANC, JARRET AVANT, JUMEAU, LONGE, POITRINE,
  POINT DE POITRINE, LANGOUSTE).
- **It is a predecessor/fragment, NOT the 51-country glossary.** It is dated two years before the 1st
  edition, has no Asian, Slavic, Arabic or African material at all, and covers a handful of countries
  rather than 51.
- **But its *scope* matches the book's blurb closely** — "beef, pork, lamb, game, poultry and fish
  ... plus a number of invertebrates such as crabs, lobsters, shrimp, squid and scallop" is an exact
  description of what this file contains, and the 1998 date sits two years before the 2000 edition.
  **Plausibly an early draft of the book. UNPROVEN** — nothing in the file names the book.

**How it handles equivalence — binary, and anchored on muscles.** Three verbatim entries:

> **BIFTEK DE CONTRE FILET** — "In ® North America, steaks of ® beef longissimus dorsi."

> **CANADIAN MEAT CUTS** — "® North American meat cuts." (and **US MEAT CUTS** likewise redirects)

> **AITCH BONE** — "Trade name for ® pubis + ® ischium."

The `®` glyph is a cross-reference arrow. **Equivalence is asserted as a redirect (A = B) or as a
muscle list. There is no score, no percentage, no hedge, nowhere in the file.**

The richest entry, **NORTH AMERICAN BEEF CUTS**, is the closest he comes to the project's subject —
and it is a *cutting procedure narrated against skeletal landmarks*, with Canadian French names in
parentheses, e.g.:

> "The round (ronde) is separated from the rump (croupe) about 1 cm distal to the ischium, terminating
> the separation just after passing through the head of the ® femur. The rump is separated from the
> sirloin (surlonge) from between sacral vertebrae 4 and 5 to a point just ventral to the acetabulum
> of the pelvis. The sirloin is separated from the short loin (longe) with a cut perpendicular to the
> vertebral column, passing between lumbar vertebrae 5 and 6."

**This is prior art for feature 1/3 (cuts defined by named skeletal landmarks and muscles), not for
feature 2.** It is also a usable free source of landmark-level cut boundary definitions.

**Not yet examined** (all HTTP 200 in Wayback): `Final.html` (130 KB, 2006), `INTRO.html`,
`Lectures.html`, `10234I04.htm`, `Sik.htm`, `ch1.htm`–`ch9_2.htm`, `HTML10234/`. A follow-up pass on
`ch2.htm` (168 KB) and `ch3_0.htm` is the obvious next move if more Swatland text is wanted.

---

## 3. Trypuz, Kulicki et al. (2016) — UNECE bovine ontology. **ABSTRACT UNVERIFIED.**

**Citation.** Trypuz, R., Kulicki, P., Grądzki, P., Trójczak, R., Wierzbicki, J. 2016.
"Machine-Understandable and Processable Representation of UNECE Standards for Meat. Bovine Meat —
Carcases and Cuts Case Study." *Metadata and Semantics Research* (MTSR 2016), CCIS, Springer.
**DOI 10.1007/978-3-319-49157-8_12**. DBLP key `conf/mtsr/TrypuzKGTW16`; MAG 2548202195;
S2 CorpusId 11506319; S2 paperId `13c302250d0ad429a968f238e736971ec187d00e`.
*verified: Semantic Scholar Graph API fetched —
`https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/978-3-319-49157-8_12?fields=...`*

**BLOCKED / PAYWALLED — mark all content claims UNPROVEN:**
- Semantic Scholar returns `"abstract": null` and `openAccessPdf.status: "CLOSED"` with an explicit
  note: *"the following paper fields have been elided by the publisher: {'abstract'}"*.
- `link.springer.com/chapter/10.1007/978-3-319-49157-8_12` **303-redirects to `idp.springer.com/authorize`**
  (an auth wall). Not followed.
- ResearchGate copy is a "Request PDF" stub.
- **No preprint, no repository copy, no ontology file, and no live SPARQL endpoint URL was located.**

**What is claimed about it comes only from WebSearch result summaries, not from a fetched abstract.**
Recorded as hearsay, flagged as such: SKOS as the representation basis; "a limited number of
ontological object properties extending SKOS ... to represent relations among beef cuts **such as the
relation of being prepared from**"; a web app to browse the standard and a SPARQL endpoint; a stated
ambition to cover all 16 UNECE meat standards and link into Schema.org and the GS1 vocabulary.

**Answer to the brief's question — "did they formalise the UNECE cutting lines in a way that supports
comparison?" — on the evidence available: NO, and probably not by design.**
1. It represents **one** standard (UNECE bovine). Comparison requires two.
2. The only relation reported is **`prepared from`** — a **partonomy within one standard**. *(An
   illustrative instance of that relation, taken from the AUS-MEAT PDF rather than from Trypuz: "Cube
   Roll is prepared from a Forequarter (item 1063)". The example is real; that Trypuz encodes this
   particular pair is not verified.)* A partonomy is a mereology, not an alignment.
   SKOS's cross-scheme predicates (`skos:closeMatch`, `skos:broadMatch`, `skos:relatedMatch`) — which
   are the natural place a cross-standard mapping would live — are **not mentioned in any summary**.
3. SKOS mapping properties are in any case **unweighted**: `closeMatch` has no "how close" slot. Even
   if they had used them, the result would be binary/ordinal, never 91%.
4. **On multilingual naming — do NOT assume it is handled.** No fetched source says so. The UNECE
   bovine standard's own §5.1 multilingual index (EN/FR/RU/ES/ZH) would make `skos:prefLabel`/`altLabel`
   with `@lang` tags trivial, and SKOS is built for exactly that — but **that is inference, not evidence.**
   **UNPROVEN.**

**Adjacent, and fully open:** Kulicki, P., Trypuz, R., Wierzbicki, J. 2012. "Towards beef production and
consumption ontology and its application." *Proc. FedCSIS 2012*, pp. 483–488. ISBN 978-83-60810-51-4.
https://annals-csis.org/proceedings/2012/pliks/287.pdf — *verified: downloaded, extracted.*
**This is a different ontology** (the *ProOptiBeef* project's farm-to-fork ontology for a Polish beef
research programme, feeding a semantic search engine called **Oxpecker**) and it **does not cover
cut nomenclature** — grep for `UNECE|cut|SKOS|multiling` returns one incidental hit
("multilingual settings" as a motivation) and nothing on cutting systems. Useful only as evidence
that this group's interest in meat ontology predates and surrounds the 2016 UNECE paper.
Later work by the same two authors is in an entirely different domain (Trypuz, Kulicki, Sopek 2024,
ontology of the SAE J3016 autonomous-driving standard, *Semantic Web*, doi 10.3233/SW-243578) —
**they appear to have moved on; no continuation of the UNECE meat project was found.**

---

## 4. IMPS ↔ UNECE ↔ HAM harmonisation — binary by construction, and lossy

### 4.1 SETTLED: **HAM item numbers DO match UNECE item numbers (3/3 checked). The PDF field labelled "UNECE" is a separate thing — the species code.**

Two distinct questions were conflated in earlier notes; both are now answered, and they have
*opposite* answers.

**(a) Is the "UNECE" field on the per-cut PDF a cut code? NO — it is the species code.**
The per-cut PDFs at `https://www.ausmeat.com.au/cutcodes/<NNNN>.pdf` are free, unauthenticated and
unlinked. Seven were fetched and the text extracted. **Field labels read exactly:**

| HAM No | Product | UNECE field label | UNECE value | N.A.M.P. | N.Z.M.S.G. |
|---|---|---|---|---|---|
| 1643 | BRISKET (bone-in, 13 ribs) | "U. N. Coding" | **0010** | — | — |
| 2000 | TOPSIDE | "U. N. Coding" | **0010** | 168 | 1200 |
| 2012 | INSIDE CAP (alt: Topside Cap) | "U. N. Coding" | **0010** | 169B | — |
| 2140 | STRIPLOIN (3 ribs) | "UNECE Species Code" | **0010** | 180 | 1620 |
| 2143 | STRIPLOIN (2 ribs) | "UNECE Species Code" | **0010** | 180 | — |
| 2240 | CUBE ROLL (5 ribs) | "U. N. Coding" | **0010** | 112 | 2240 |
| 2243 | CUBE ROLL (7 ribs) | "UNECE Species Code" | **0010** | 112 | 2240 |

*verified: all seven PDFs downloaded with curl and extracted with pdftotext.*
The value is `0010` on **every** beef cut; per the standards-thread notes UNECE species code
**10 = beef**. So the field carries species, and the PDFs contain **no UNECE cut-number field**.

**(b) Is the H.A.M. No itself a UNECE item number? YES, on every case checkable — 3/3.**
Cross-checking the H.A.M. numbers against the UNECE 2023 bovine multilingual index recorded in the
standards notes:

| Number | UNECE 2023 index | AUS-MEAT HAM PDF | Match? |
|---|---|---|---|
| **1643** | Brisket | **BRISKET**, "BONE IN BEEF" | ✅ |
| **2012** | Inside cap (*Dessus* / *Tapa de nalga*) | **INSIDE CAP**, alt. Topside Cap | ✅ |
| **2240** | Cube Roll | **CUBE ROLL**, alt. Rib Eye Roll | ✅ |

**The structural rule matches too.** UNECE states "codes for bone-in cuts start with 1 and codes for
boneless cuts with 2". The AUS-MEAT PDFs obey it exactly: 1643 Brisket is stamped "BONE IN BEEF",
1063 Forequarter is the bone-in source item, and 2000/2012/2140/2240 are all stamped "BONELESS BEEF".

**Conclusion: AUS-MEAT's claim is substantially right.** *"The HAM cut codes and the UNECE international
cut codes are the same, hence the app applies across international borders"*
(https://www.ausmeat.com.au/handbook-of-australian-meat-app/) — **supported, with one refinement: HAM
shares the UNECE base numbering and then adds sub-variants UNECE does not have.** HAM 2140 *and* 2143
are both Striploin (3-rib vs 2-rib); HAM 2240 *and* 2243 are both Cube Roll (5-rib vs 7-rib); the
"Related Items" field on 2240 lists 2241/2242/2243/2244. UNECE's 89-item index carries one code per
cut. So **HAM ⊇ UNECE at the numbering level** — a superset, not a divergence.

**Correction to earlier notes:** the standards-thread caution ("the PDFs list UNECE Species Code as a
separate field — so treat the earlier 'HAM codes == UNECE codes' quote with care") was right *about the
field* and wrong *about the implication*. The separate species field does not undermine the identity
claim; the H.A.M. number is itself the UNECE item number.

### 4.2 The crosswalk that does exist is **binary and demonstrably lossy** — the cleanest negative found

**HAM 2240 (Cube Roll, "5" ribs, caudal edge of 4th rib to 13th) → NAMP 112.**
**HAM 2243 (Cube Roll, "7" ribs, same muscle description, lip retained) → NAMP 112.**
**Both also → N.Z.M.S.G. 2240.**

Two Australian cuts that differ in rib count and in whether *M. iliocostalis* ("the Lip") is retained
collapse onto **one** American number and **one** New Zealand number. The crosswalk records
`2240 → 112` and `2243 → 112` as equally true. **There is no field anywhere in the format capable of
saying that 2240 and 2243 stand in different relations to 112.**

This is exactly the information the project's overlap percentages are designed to carry, and it is
exactly what the industry standard throws away. **Record this as the concrete demonstration that the
official crosswalks assert binary identity and lose partiality.**

Also present on these PDFs and useful for feature 3: muscle-level definitions
("consists of the M. longissimus dorsi and associated muscles underlying the dorsal aspect of the ribs
(caudal edge of the 4th rib to the 13th inclusive)"), "Related Items" lists (2240→2241/2242/2243/2244 —
a sibling-variant graph), "Points Requiring Specification", and foodservice synonyms
(2140 Striploin: Entrecote / New York Steak).

### 4.3 Trade/customs classification — explicit negative, not worth further fetching

Customs nomenclature is **binary by construction**: a consignment is classified under exactly one code.
The standards-thread notes already establish the substance —
- **WCO HS / EU Combined Nomenclature ch. 02** reaches only bone-in primals, with rib- and
  vertebra-precise legal definitions, and **collapses all boneless beef to one line per heading**.
  No retail-cut granularity, therefore no partial-correspondence problem to solve.
- **Reg. (EU) 2016/1240 Annex III Part IV** gives 13 `INT nn` beef cuts across 24 languages — a real
  multilingual coded list, but each `INT nn` is defined by its own seam-and-bone instruction and is
  **not mapped to IMPS, UNECE or HAM at all**.
- The CN EN/FR divergence recorded in those notes (EN "crop and chuck and blade cuts" / "brisket cut"
  vs FR « découpes ... dites "australiennes" » at the same code 0202 30 50) shows the legal instruments
  are willing to let *names* diverge wildly under a shared code — which is only possible **because the
  code, not the name, carries the definition.** That is the opposite of grading name equivalence.
- **AHECC** (Australian export codes, on every HAM PDF) resolves multiple distinct HAM cuts to the same
  `0201.30.13` / `0202.30.13` pair — i.e. all boneless chilled/frozen beef. Maximum collapse.

**No published crosswalk with any notion of partial correspondence was found. Explicit negative.**

---

## 5. Huerta-Leidenz (2013), USMEF — the largest cut-name matrix ever published, with an author's disclaimer that settles the question

**Citation (the guide's own recommended form, verbatim):**
> "Huerta-Leidenz, N. 2013. Guía de nomenclatura internacional de cortes de carne de res para EE.UU. y
> diferentes países objetivo de la U.S. Meat Export Federation. pp 20. U.S. Meat Export Federation.
> Ciudad de México, México."

Author: **Nelson Huerta-Leidenz**, Director de Servicios Técnicos de USMEF para Latinoamérica.
© USMEF 2013. Print run **30,000 copies**. 20 pp (the PDF is 11 sheets, spreads).

**Live URL 404s**; retrieved from the Wayback Machine:
https://web.archive.org/web/2020id_/https://www.northernbeef.com/wp-content/uploads/2018/05/1063.GUI%CC%81A_beef-cuts_espan%CC%83ol_09oct13.pdf
*verified: downloaded via Wayback and extracted with pdftotext (1.49 MB, 11 pp).*
An **English companion** is archived too (`.../1064.GUIDE_beef-cuts_inglés_09oct13.pdf`, snapshots
2023-07-27 and 2024-02-27, `application/pdf`, 200) — **not fetched.**

### 5.1 Scale and structure

> "La guía que ahora se presenta a su consideración, comprende el listado de **42 a 52 cortes
> estadounidenses con sus equivalentes en más de 35 países** de Latinoamérica, Europa, Asia, Oceanía
> y el Mundo Árabe."

Layout: **rows = US cut name + IMPS/NAMP item number; columns = countries; cells = one or more local
names**, split into `CORTES SIN HUESO` / `CORTES CON HUESO` blocks and grouped into regional tables:
- Central America & Caribbean: Costa Rica, Cuba, El Salvador, Guatemala, Honduras, México, Nicaragua,
  Puerto Rico, República Dominicana (+ Panamá)
- South America: Argentina, Bolivia, Brasil, Colombia, Chile, Ecuador, Paraguay, Perú, Uruguay, Venezuela
- Europe: Alemania, España, Francia, Inglaterra, Italia, Portugal, Rusia
- Asia/Oceania/Arab: Mundo Árabe, China–Taiwan, Indonesia, Australia
- Canada **deliberately excluded**: "su nomenclatura de cortes de carne bovina es prácticamente
  idéntica a la de Estados Unidos."
- A final table of *"términos elegantes"* — marketing coinages proposed for modern US cuts in Spanish
  (from an NCBA 2005 initiative).

Sample row (bone-in, IMPS 109/109E, Rib bone-in Ribeye Roll) across South America:
`Lomo Entero/Delmonico con hueso · Lomo de res con hueso · Lomo Rollizo con hueso · Lomo Grande con
hueso · Costilla Cargada Completa · Sobre Lomo/Asado de Costilla con hueso · Lomo de Costillón con
hueso · Grillada/Lomo/FM con hueso` — **multiple synonyms per cell, no ranking, no weight, no hedge.**

The only qualification anywhere in the tables is a footnote repeated on every page —
"El músculo subescapular se derivaría cuando se convierte un 116A Chuck roll a PSO 3" — i.e. a
preparation note, not a degree of correspondence.

### 5.2 THE DISCLAIMER — the most important sentence in this whole thread

> "Sin embargo, al reconocer la variación dentro y entre países para la nomenclatura y estilos de
> preparación de cortes, hacemos la salvedad de que el glosario contenido en esta publicación,
> **no persigue presentar -mucho menos institucionalizar- equivalencias anatómicas o comerciales.**
> En cambio, la misma puede servir como lo que es, una guía para que el lector descubra
> **las similitudes** entre las piezas cárnicas estadounidenses de hoy, con aquellas de otros países
> con los que existe o se pretende un intercambio comercial."

*(The person who assembled the largest cross-country cut-name table in existence, for the body with the
strongest commercial incentive to make it authoritative, explicitly refuses to claim it represents
anatomical equivalence — and offers it as a prompt for the reader to notice "similarities".)*

And on the state of the field:

> "La industria de la carne a nivel mundial aún confronta la falta de un sistema consensuado de
> estandarización de términos o códigos para definir y describir productos cárnicos..."

> "Este es el producto de un proyecto sin fin, a medida que empezamos a penetrar más países a nivel
> mundial, iremos descubriendo las diferencias entre modalidades de corte para poder establecer las
> equivalencias debidas."

He also cites the concept **«relaciones de equivalencia» (Michel, 1997)** as the theoretical frame for
name-pair equivalence. *(Michel 1997 not chased — worth a look if the project wants a citable theory
of "equivalence relation" between cut names.)*

### 5.3 Leads harvested from its bibliography (none fetched — all UNPROVEN)

- **NAMP. 2011. "Nomenclatura de res y cerdo en países seleccionados de América Latina (Cómo utilizar su
  guía para compradores de carne)"**, in *The Meat Buyer's Guide — Guía para Compradores de Carne*,
  sect. beef/carne de res, **7th bilingual ed.** — the direct predecessor Huerta-Leidenz expanded.
- **Yakoo, M., Araujo, F., Sainz, R., Rocha, G. 1998. "Comparação entre cortes comerciais de carne
  bovina no Brasil, Austrália e nos Estados Unidos."** *Beef Point*,
  `beefpoint.com.br/radares-tecnicos/qualidade-da-carne/comparacao-entre-cortes-comerciais-de-carne-bovina-no-brasil-australia-e-nos-estados-unidos-7115/`
  — **an explicit three-country cut comparison, 1998. Worth chasing; not fetched.**
- **Jones, S. L., Burson, D. E., Calkins, C. R. 2001. "Bovine Myology and Muscle Profiling"** — the
  muscle-anatomy reference underlying feature 3.
- **INAC (Uruguay), *Manual de Cortes Bovinos para Abasto* (107 pp) and *Manual de Cortes de Carnes
  Bovina y Ovina / Handbook of Uruguayan Meat* (108 pp)**, `inac.gub.uy`.
- **SENASA / Secretariat for Agriculture, Argentina, *Glossary of Main Export Cuts from Argentina***
  (64 pp) — surfaced in search at
  `https://www.magyp.gob.ar/sitio/areas/bovinos/informacion_interes/informes/_archivos//000018_Nomencladores/000000-%20Presentaci%C3%B3n%20glosario%20de%20cortes%20bovinos,%20porcinos%20y%20ovinos.pdf`
- **AUS-MEAT Handbook 7th ed. CD-ROM** at `ausmeat.com.au/custom-content/cdrom/Handbook-7th-edition/English/`
- **USMEF *Manual Para Carne Internacional*** in English, Japanese, Korean, Mandarin and Spanish
  (late 1990s), and the **USMEF Bilingual Labeling Manual** covering 11 countries. Neither located.
- **Guaporé, *Dicionário de Cortes Bovinos***, `guapore.com/cortes-dicionario.htm`.

---

## 6. Calderón Alonso et al. (2021) — cut equivalence *plus* numbers, but the numbers are yield

**Citation.** Calderón Alonso, A. C., Romo Valdez, A. M., Barreras Bojórquez, L. G., Ríos Rincón, F. G.
2021. "Equivalencia de la nomenclatura y rendimiento de cortes primarios de la canal bovina en el
noroeste de México." *NACAMEH* **15**(1): 30–45. Received 25/05/2021, accepted 01/07/2021.
DOI printed in the PDF as literally `https://doi.org/PENDIENTE` — **no DOI was ever assigned.**
Open access PDF: https://dialnet.unirioja.es/descarga/articulo/8017603.pdf
*verified: downloaded, extracted (16 pp).*

**What it does.** Tables 1–4 give **US ↔ México ↔ Noroeste de México** equivalences for basic and
primal cuts, **keyed by IMPS and NAMP numbers**, built by reconciling NAMP (2011), SAGARPA (2013),
Huerta-Leidenz (2013) and IMPS-USDA (2014). Tables 5–7 give **commercial yield as % of carcass**.

Sample of Table 3 as extracted (hindquarter):
`Gooseneck / IMPS 171 / NAMP 170A / Pulpa blanca / MX 101 / Pulpa larga` ·
`Peeled Knuckle / 168 / 168 / Pulpa negra / 103 / Pulpa negra` ·
`Bottom sirloin / 157 / NA / Tapa de aguayón / — / Chambarete` ·
`Outside skirt / — / — / Fajitas / No aplica / Arrachera`.
Note the `NA` / `—` / `No aplica` cells: **absence of an equivalent is recorded; degree of equivalence
is not.** *(Caveat: the column alignment of this table is scrambled by pdftotext, so individual
row pairings above should be re-read off the PDF before being quoted as fact.)*

**Verdict on this paper.** The **equivalence is binary** (a three-column synonym table). The
**quantities are yields** — forequarter 38.23%, hindquarter 29.59%, other carcass components 31.72%;
highest-value cuts 20.23%; "cortes valiosos" 55.12% (CV 6.97%), bone 12.49%, trimmed fat 9.45%.
**Those percentages are fractions of a carcass, not fractions of another country's cut.**
It is the closest thing found to "a peer-reviewed paper that puts numbers next to a cross-country cut
mapping" — and the numbers answer a completely different question.

It also reports the **cutting-line difference itself**, which is the real source of partial overlap:
Mexican/Venezuelan tradition quarters at the **5th intercostal space**, US practice at the **12th**
— hence the Mexican `chuletón`, from which `lomo` and `rib eye` come out as one piece, and hence
`suadero` and `diezmillo`. That is a qualitative statement of exactly what a percentage would quantify.

**The 2014 Venezuelan paper is identified through this one** (see §7).

---

## 7. The 2014 Venezuelan paper — IDENTIFIED

Semantic Scholar paperId `14cee89716f570662b60e6211021f1fe7c6d15d7`.
**The S2 Graph API returned HTTP 429 (rate-limited) on three attempts and the S2 web page fetched
empty, so the paperId↔title link is NOT confirmed at the API level.** But the title is unmistakable
and matches the brief's description exactly:

> **Montero, [et al.] 2014. "Deshuese y variación del rendimiento carnicero de canales bovinas en
> Venezuela: descripción anatómica del proceso y nomenclatura de cortes equivalente a los
> correspondientes norteamericanos" / "Fabrication and variation of the cut-out yield of beef carcasses
> in Venezuela: anatomical description of the process and equivalency of cut nomenclature to North
> American counterparts."**

- ResearchGate record (Request PDF, not fetched):
  https://www.researchgate.net/publication/260364557_Deshuese_y_variacion_del_rendimiento_carnicero_de_canales_bovinas_en_Venezuela_descripcion_anatomica_del_proceso_y_nomenclatura_de_cortes_equivalente_a_los_correspondientes_norteamericanos_Fabrication
- **Cited four times in Calderón Alonso et al. (2021)** as "Montero y col. (2014)", alongside
  "Huerta-Leidenz y col. (2014)" — *verified from the fetched Dialnet PDF*, which is what pins the
  identification.

**What it does, per its own title and per the 2021 paper's descriptions of it:** the same shape as §6 —
**anatomical description of the fabrication process + a name-equivalence table to North American cuts +
yield variation.** Quoted in the 2021 paper as observing that "la estandarización de la nomenclatura y
la codificación de cortes **no existen en la inmensa mayoría de los países latinoamericanos**", and as
comparing Mexican and Venezuelan carcass-cutting technique (quartering at the 5th intercostal space).

**Full text not obtained; venue, exact author list and DOI UNVERIFIED.** On the evidence, it is a
name-equivalence + yield paper of the §6 type, i.e. **binary equivalence with mass-based numbers**,
not a graded-overlap paper. The Huerta-Leidenz connection (Venezuelan meat scientist, USMEF Latin
America, §5) makes this a coherent single research lineage: **Huerta-Leidenz → Montero 2014 →
Calderón Alonso 2021**, all doing IMPS-keyed Spanish-language cut mapping, none of them grading it.

---

## 8. Lhuissier (2002) — cut names as contested administrative artefacts. FULL CITATION OBTAINED.

**Lhuissier, Anne. 2002. "Cuts and Classification: The Use of Nomenclatures as a Tool for the Reform of
the Meat Trade in France, 1850–1880." *Food and Foodways* 10(4): 183–208.
DOI 10.1080/07409710216028.** Published November 2002.
*verified: CrossRef API —
`https://api.crossref.org/works?query.title=Cuts%20and%20classification%20nomenclatures%20reform%20meat%20trade%20France`
returned the record with title, journal, volume 10, issue 4, pages 183-208, date 2002-11.*

**Full text NOT obtained. Its argument is UNPROVEN.**
- Taylor & Francis article page not fetched (paywall expected).
- **HAL returns zero results**:
  `https://api.archives-ouvertes.fr/search/?q=Lhuissier AND title_t:(cuts classification)` → `numFound: 0`.
  Despite Lhuissier being an INRA/INRAE sociologist, this 2002 article is not self-archived there.
- Her 2002 EHESS doctoral thesis is a **different work**: *"Réforme sociale et alimentation populaire
  (1850-1914): pour une sociologie des pratiques alimentaires"* (from a WebSearch summary only —
  **UNPROVEN**, no catalogue record fetched).

**What can be said without the text:** the title alone establishes the frame the brief wants — cut
nomenclatures as **instruments of trade reform** in a specific political struggle (the Paris butchery
trade, 1850–1880), i.e. **cut boundaries as administrative artefacts produced by contest, not as
natural kinds.** That is the correct intellectual framing for why partitions differ and why a
percentage rather than an equals-sign is the honest representation. **But do not quote an argument from
this paper until someone reads it.** Supporting context surfaced but not fetched: Lhuissier also
published on Paris retail butchery display, 1860–1960 (https://www.academia.edu/40600690/ and
researchgate 336733777), and there is a related *Revue d'histoire moderne et contemporaine* 2004
article on meat-market stabilisation in France, 18th–20th c.
(https://shs.cairn.info/revue-d-histoire-moderne-et-contemporaine-2004-3-page-121).

---

## 9. A similarity/overlap/Dice/Jaccard score between two anatomical partitions, in meat science

### **EXPLICIT NEGATIVE. Nothing found.**

Searched for set-similarity metrics applied to carcass partitions. What comes back is a
**different literature entirely**: tissue composition of primals, genetic correlation of primal yields,
DXA/camera-vision prediction of carcass composition, nutritional comparison between primals. Sampled:
- "Influence of Production Factors on Beef Primal Tissue Composition" https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8871317/
- "Relationship between body size traits and carcass traits with primal cuts yields in Hanwoo steers" https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7888490/
- "Estimation of Genetic Correlations of Primal Cut Yields with Carcass Traits in Hanwoo Beef Cattle" https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8614487/
- "Carcass and Primal Composition Predictions Using Camera Vision Systems (CVS) and DXA" https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8158109/

**All of these quantify *what is inside one cut*. None quantifies *how much of cut A is inside cut B*.**
*(These were surfaced as search results and not individually fetched — but the negative is about the
absence of a metric, and the search returned no candidate worth fetching.)*

One tangential-but-real observation surfaced in that search, worth keeping because it states the
project's premise in the literature's own voice: that **the division of half-carcasses into primals
varies somewhat from country to country, and the division of primals into retail cuts varies much more
so between countries.** *(Attributed in a search summary to the ScienceDirect "Primal Cut" topic page,
https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/primal-cut —
**not fetched, so treat as unattributed until confirmed.**)*

### Muscle profiling — the right substrate, the wrong question

**Von Seggern, D. D., Calkins, C. R., Johnson, D. D., Brickler, J. E., Gwartney, B. L. 2005.
"Muscle profiling: Characterizing the muscles of the beef chuck and round." *Meat Science*.**
https://www.sciencedirect.com/science/article/abs/pii/S0309174005001269
RMC version: https://meatscience.org/docs/default-source/publications-resources/rmc/2005/muscle-profiling---characterizing-the-muscles-of-the-beef-chuck-and-round(3).pdf
*(Neither fetched — described from search summaries. Details below are therefore UNPROVEN.)*
**39 muscles dissected from 142 carcasses**, each characterised for colour, moisture, proximate
composition, emulsion capacity, pH, collagen, heme-iron and Warner-Bratzler shear. Produced the
**flat iron, chuck eye steak and Denver cut**.

**This is the methodological ancestor of feature 3 (cuts keyed to named muscles), not of feature 2.**
It decomposes *one* system into muscles; it never compares two systems. But it matters for feature 2
indirectly: **it establishes muscle as the accepted common substrate in meat science**, which is the
natural denominator for any overlap metric someone might eventually define.
Pair it with **Jones, Burson & Calkins 2001, "Bovine Myology and Muscle Profiling"** (from the USMEF
bibliography, §5.3) and with **Tucker, H. Q., Voegeli, M. M., Wellington, G. H. 1952,
*A Cross-sectional Muscle Nomenclature of the Beef Carcass*, Michigan State College Press,
East Lansing** — which Swatland calls the field's solution to exactly this problem:

> "The international meat science community found a way around this problem by adopting muscle names as
> the basis for communication; the breakthrough publication making veterinary anatomy accessible to meat
> scientists was Tucker, Voegeli, and Wellington's *A Cross-sectional Muscle Nomenclature of the Beef
> Carcass*"

**That sentence is the strongest available argument for this project's architecture:** the discipline's
own accepted answer to cross-system incommensurability is *reduce to muscles* — and once both partitions
are expressed over a shared muscle set, an overlap coefficient is the obvious next step that nobody took.

---

## 10. Consolidated answers to the brief's four questions

| Source | Binary or graded? | Metric | Computed over | Cuts × systems |
|---|---|---|---|---|
| **Swatland 2012 T1** | **Graded 0–10, but only by summing binary cells** | "cut match" = Σ of 1-if-same-named-cut-overlaps-in-location | **names + location.** Not muscles, mass or geometry | 9 primals × 10 British sources (2 systems) |
| Swatland 2012 T2 | Binary | none | muscle names | ~11 US cuts × Caribbean |
| Swatland 2012 T3–T5 | Binary + prose qualifiers (`anterior`, `+`) | none — "major overlap", "seldom identical outlines" | names | 9 beef / 6 pork primals × 6 countries |
| Swatland *Glossary* (2000/04/23) | Binary (cross-reference redirect) | none | names ↔ country; some muscle lists | 51 countries, cut count unknown |
| Trypuz et al. 2016 | Binary (SKOS) — **UNPROVEN** | none reported | `prepared from` partonomy *within* UNECE | 1 standard, 0 comparisons |
| AUS-MEAT HAM PDFs | **Binary, and lossy** (2240 & 2243 → NAMP 112) | none | item numbers | ~4 code systems, 1:1 asserted |
| Huerta-Leidenz 2013 | Binary, **with equivalence explicitly disclaimed** | none | names, IMPS-keyed | **42–52 cuts × 35+ countries** |
| Calderón Alonso 2021 | Binary equivalence; **numbers = carcass yield %** | % of carcass weight | mass | ~30 cuts × 3 (US/MX/NW-MX) |
| Montero et al. 2014 | Same shape (**text unobtained**) | yield | mass | VE ↔ US |
| WCO HS / EU CN / INT nn | Binary by construction | none | legal definitions | primals only |
| Von Seggern 2005 | n/a — not a comparison | composition/shear per muscle | 39 muscles × 142 carcasses | 1 system |

---

## 11. Verdict

**This project's overlap percentages have an ancestor in intent and none in method.**

- **Swatland (2012) is the only person who ever published a per-cut number expressing how well two
  cutting systems agree.** That legitimises the *idea* of scoring concordance cut-by-cut, and gives the
  project a citable, named, peer-presented predecessor at the AMSA International Lectureship. But his
  number is a **count of name survivals across ten British charts**, it requires the two cuts to
  **share a name**, and it is **blind to how much anatomy they share**. `Rib = 10` and `Sirloin = 0`
  are statements about English vocabulary, not about the carcass. A project claiming
  "US short loin is 91% Russian тонкий край" is computing something Swatland's method
  **cannot express and was not built to express** — his own Russian table (T5) carries no numbers at all.
- **The field knows partial overlap is the real phenomenon and has consistently refused to quantify it.**
  Swatland: cuts "seldom share identical outlines." Huerta-Leidenz, with 35+ countries and USMEF behind
  him: the glossary "no persigue presentar ... equivalencias anatómicas o comerciales." AUS-MEAT's
  format has no slot for it. UNECE's ontology models parthood inside one standard and alignment across
  none. **The gap is not an oversight — it is a repeatedly, explicitly declined problem.**
- **Nothing in meat science computes a set-similarity coefficient between two partitions of one carcass.**
  Searched and not found. The nearest neighbours quantify composition *within* a cut (Von Seggern),
  or mass *as a fraction of the carcass* (Calderón Alonso, Montero) — both are different denominators.
- **The substrate the project needs is the one the discipline already agreed on.** Muscle nomenclature
  has been meat science's lingua franca since Tucker et al. (1952), Swatland says so explicitly, and
  every serious source here — IMPS line drawings with Latin names, Korean 별표 3 seaming specs, AUS-MEAT
  "M. longissimus dorsi ... 4th rib to the 13th", Swatland's Table 2 and his `b4a-z` entries —
  defines cuts over muscles and skeletal landmarks. **Expressing both partitions over a shared muscle
  set and taking an overlap coefficient is the obvious unclaimed step**, and the honest framing for the
  project is: *the substrate is standard, the scoring is not — and no published work has done it.*
- **Novelty assessment: feature 2 is, as far as this search can establish, genuinely unprecedented.**
  That is a real claim to make, but it must be made carefully: the strongest counter-evidence is
  **Swatland's book itself, whose 258 pages nobody has read** (§2.3 — no preview, no lending copy,
  print only). If the book contains a graded scheme, this verdict is wrong. **Getting a physical or
  library copy of the 2004/2023 edition is the single highest-value remaining action on this thread.**

---

## 12. Failures, blocks and explicit negatives

**Blocked / paywalled:**
- `link.springer.com/chapter/10.1007/978-3-319-49157-8_12` — **303 → `idp.springer.com/authorize`.**
  Abstract elided by publisher in Semantic Scholar too. **Trypuz 2016 content is UNPROVEN throughout.**
- `books.googleapis.com` — HTTP 429, daily quota exhausted for this environment. Google Books HTML
  used instead; it shows **no preview** for the Glossary.
- `api.semanticscholar.org` — HTTP 429 on three attempts for the Venezuelan paperId.
  `semanticscholar.org/paper/14cee...` fetched **empty**. Paper identified by other means (§7).
- `northernbeef.com` live PDF — **404** (it returns an HTML 404 page at a `.pdf` URL: check `file`
  output, never the extension). Wayback copy ✅ worked. `dialnet.unirioja.es` PDF ✅ worked.
- `animalbiosciences.uoguelph.ca/~swatland/` — **403** live; **Wayback works.**
- `swatland.net` / `www.swatland.net` — **does not resolve** (curl: no connection, http and https).
  `uoguelph.ca/~swatland/` — **404**.
- `archives-ouvertes.fr` — **0 results** for Lhuissier. Not self-archived.
- `archive.org` — **0 results** for the Glossary. No lending copy.

**Explicit negatives (searched, genuinely absent):**
- No DOI for Swatland (2012). AMSA RMC proceedings are not DOI-registered.
- No DOI for Calderón Alonso et al. (2021) — the PDF prints `https://doi.org/PENDIENTE`.
- No released ontology file, no live SPARQL endpoint URL, and no successor paper for the UNECE bovine
  ontology. The same authors' 2024 work is on autonomous-driving standards.
- No published IMPS↔UNECE↔HAM crosswalk expressing **partial** correspondence, anywhere.
- No meat-science paper computing Dice/Jaccard/overlap between two carcass partitions.
- No evidence Swatland's proposed "Wikipedia type of website" for international meat cuts was built.

**Not chased (deliberate, listed so a later pass can pick them up):**
`Final.html` / `ch2.htm` / `ch3_0.htm` and the rest of the archived Guelph textbook;
the **English** USMEF guide (`1064.GUIDE_beef-cuts_inglés_09oct13.pdf`, archived, 200);
Yakoo et al. 1998 Brazil/Australia/US comparison; NAMP 2011 Latin America nomenclature section;
INAC Uruguay manuals; SENASA Argentina export-cut glossary; Michel (1997) on "relaciones de
equivalencia"; Swatland 2010a *Meat Sci* 86:80–85 (possible peer-reviewed sibling of the 2012 paper);
Montero et al. 2014 full text; Lhuissier 2002 full text.
