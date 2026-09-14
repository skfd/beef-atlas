# Notes: English-language cross-country cut guides

## Tier 2 — Substantial cross-country data (the actually useful prior art)

**"BEEF CUTS" multilingual comparison table** (hosted by Lexicool)
index https://www.lexicool.com/dictionary.asp?ID=GZ2XS26441 ->
PDF https://static.lexicool.com/dictionary/GZ2XS26441.pdf
**The single richest dataset found**, and Lexicool's metadata badly undersells it. Lexicool calls it
"Beef Cuts Glossary (DE-EN-ES-FR-IT-PT), 40 entries"; the actual PDF is a 3-page grid with **nine
country columns** — Argentina, Spain, Brazil, Chile, Portugal, USA/UK, France, Germany/Switzerland,
Italy — and roughly 200 term cells. **Latin-America-heavy, which is rare.**
Stale but not dead: PDF internals say Title "BEEF CUTS", created 5 Sep 2003 (Acrobat Distiller
5.0.5 / PDFMaker for Word). **No author, publisher or copyright string anywhere in the file** —
provenance unknown, so it is unattributable as a source. Still serving over HTTPS.
*verified: fetched, text extracted locally with pdftotext*

**Swatland, "History and Language of International Meat Cutting"**
https://meatscience.org/docs/default-source/publications-resources/rmc/2012/26_swatland_r2.pdf
AMSA International Lectureship paper, **Howard J. Swatland (Emeritus, University of Guelph)**, 2012,
7 pages. The best *scholarly* treatment of exactly this problem, covering country pairs nobody else
does. Five tables:
- T1: US primal names vs ten British/Scottish sources (England 1816, 1876, 2000; West of England,
  Liverpool, NE England, Manchester, Midlands, London, Edinburgh) **with a concordance score per cut**
- T2: US -> Caribbean
- T3: US <-> Mexico / Japan / Korea beef
- T4: US <-> Mexico pork
- T5: US <-> Russia / Netherlands / Chile

Also explains *why* names diverge — e.g. sirloin/surlonge means anterior in UK+France but posterior
in US+Australia. Notes that "traditional patterns of meat cutting and the names of meat cuts are
disappearing right now" under EU standardisation. Fixed 2012 conference paper, not maintained, URL
live. *verified: fetched, text extracted locally*

**Aussie Beef & Lamb "Beef Cut Guide"**
https://www.foodservice.aussiebeefandlamb.com/siteassets/cuts-charts-pdfs/aussie-beef-cut-guide.pdf
Industry-published **bilateral AU<->US chart**: every cut listed twice, Australian HAM name + code
next to the US NAMP name + number. Topside 2000 / Topside Untrimmed 168A; Cube Roll 2243 / Ribeye
Roll 112; Rump Cap 2091 / Sirloin Cap 184D; Flap Meat 2206 / Bavette-Flap 185-A. ~35 cuts over 10
primals. **The codified, authoritative version of the AU/US mapping that food blogs do badly.**
MLA foodservice asset, no visible date, live. Companion lamb chart at
https://www.foodservice.aussiebeefandlamb.com/siteassets/lamb/the-aussie-lamb-difference.pdf
("LAMB CUT GUIDE AUSTRALIAN & US", search-result title only). *verified: fetched*

**AUS-MEAT "Handbook of Australian Meat" (HAM) app**
https://www.ausmeat.com.au/handbook-of-australian-meat-app/
Codified Australian naming for beef, veal, sheepmeat, goat, with descriptions, images and 3D assets.
Critically, the page confirms the bridge between the two codified systems: **"The HAM cut codes and
the UNECE international cut codes are the same, hence the app applies across international borders."**
Actively maintained — footer "Version: v2.3.2 (prod)", "(c) Copyright AUS-MEAT Limited 2026". No cut
count or price on the page. *verified: fetched*

**UNECE Standard: Bovine Meat — Carcases and Cuts (ECE/TRADE/326)**
https://unece.org/trade/publications/bovine-meat-carcases-and-cuts |
PDF https://unece.org/sites/default/files/2024-03/Bovine_326Rev2E_2016.pdf
The international cut-code standard; AUS-MEAT confirms HAM codes are identical to it, so it is the
spine of any codified cross-country mapping. **But the "multilingual" premise does not hold up the
way you'd hope**: WebSearch prose claimed EN/FR/RU; the only third-party catalogue actually verified
(Stanford SearchWorks https://searchworks.stanford.edu/view/5793124) records the 2004 edition as
**English only**, vi+58pp, colour illustrations. Separate per-language documents at best, not one
side-by-side multilingual document. Sibling standards surfacing as real PDF links: veal
(VealMeatCarcasesCuts_2011E.pdf), ovine (Ovine_308Rev1E.pdf), caprine — all "E" for English.
*verified: **fetch failed** — unece.org returns 403 to every fetch and to curl with a browser UA, for
the index page, the publication page and both PDF paths. Language claim verified only via Stanford.*

**CloveGarden "Beef / Veal — Cuts by Chart"** | https://www.clovegarden.com/ingred/ab_cowc.html
US NAMP primals in depth (10+ primals with sub-cuts), and links out to separate **British, French (in
French), Argentine (in Spanish) and Australian** charts — one of the very few hobbyist sites
attempting four-plus countries. **Looks abandoned**: "(c)Andrew Grygus", page stamp "ab_cowc 2009",
early-2000s hand-rolled HTML, no revision since. Links resolved. *verified: fetched*

## Tier 3 — Expat / food-blog explainers (and demand signals)

**Separated by a Common Language — "buying meat"**
https://separatedbyacommonlanguage.blogspot.com/2009/12/buying-meat.html
Linguist's US<->UK treatment, beef/pork/chicken, both countries' diagrams. **Best framing of the core
problem found anywhere:** "It's not that the cuts of beef have different names in the two places,
it's that they are different cuts of meat." 7 Dec 2009, **62 comments** — a strong 15-year-old demand
signal. Blog long dormant. *verified: fetched*

**No Ordinary Homestead — "Butcher Shop Cheat Sheet Auf Deutsch"**
https://www.noordinaryhomestead.com/butcher-shop-cheet-sheet-auf-deutsch/
American-expat-in-Germany guide: two American-vs-German beef diagrams plus prose on brisket, T-bones,
flank, Schulter, Querrippe. Mostly prose, not a clean table. Pork companion at
https://www.noordinaryhomestead.com/auf-deutsch-pork-cuts/
Published 24 Jan 2011, **65 comments running 2011 through September 2024, author still replying.**
**The clearest evidence of sustained unmet demand in the whole survey** — a 2011 hobby post is still
the go-to answer for Germany. *verified: fetched*

**FrenchEntree — "French Cuts of Meat: Shopping at the Butchers in France"**
https://www.frenchentree.com/living-in-france/local-life/food-recipes/french-cuts-of-meat/
~50+ French cut names with English equivalents across beef, pork, lamb, poultry. Bulleted lists, not
a table. Well maintained for the genre: published 29 Jan 2013, **last updated 1 Apr 2024**, bylined
(Gemma Driver), commercial expat-media site. *verified: fetched*

**Pryde Butchery, Global Guide to Beef Cuts** | https://prydebutchery.com.au/global-guide-to-beef-cuts/
USA / UK / Australia, ~32+ cuts in three-column tables with notes on regional differences. Photos of
cuts, no diagrams. Published 12 Feb 2025, modified 2 Mar 2025, by owner David deMarco — **genuinely
authored by a butcher, well maintained. Best English pairwise chart found.** *verified: fetched*

**G. J. Honour Family Butcher, American to British Beef Cuts**
https://gjhonour.com/blogs/family-butcher/translation-of-american-to-british-beef-cuts
US->UK, ~25 cuts, two-column table plus carcass diagrams for both countries. Published 2 Jun 2025,
UK butcher. Solid, commercial (cuts link to product pages). *verified: fetched*

**Easy and Delish, Meat Cuts of Beef (US and Brazil)** | https://www.easyanddelish.com/meat-cuts-beef/
US + Brazil, 40+ cuts, chart plus prose by primal; site has a Portuguese version. Food blog,
"(c) 2026". **Best US<->Brazil consumer page found.** *verified: fetched*

**Grasspunk Farm, French Beef Cut Translations** | https://grasspunk.com/french-beef-cut-translations/
French->English/American, 20+ cuts, prose with links to la-viande.fr and Wikipedia; notes cuts that
differ across English-speaking countries. Article ~2013, but the farm owner answers reader questions
through at least Dec 2021 — dated, not abandoned. *verified: fetched*

**Euro Weekly News — British meat cut equivalents in Spain**
https://euroweeklynews.com/2026/07/16/feeling-lost-at-the-meat-counter-how-to-find-your-favourite-british-meat-cut-equivalents-in-spain/
~30+ UK->Spanish equivalents across beef, pork, lamb, chicken (ribeye->lomo alto, sirloin->lomo bajo,
pork tenderloin->solomillo de cerdo, belly->panceta). Prose. Usefully warns terminology varies
between northern and southern Spain. **Freshest item in the survey — 16 July 2026.** One-shot expat
newspaper content. *verified: fetched*

**MeatGrader — "British and European Beef Cuts"** | https://meatgrader.com/blog/british-and-european-beef-cuts
~20+ cuts: UK primals (shin, brisket, chuck, fore rib, sirloin, fillet, rump, topside, silverside,
thick flank) and French cuts (onglet, bavette d'aloyau, araignee, entrecote, faux-filet, merlan) with
inline US glosses ("Fore Rib (US: ribeye / standing rib roast)"; faux-filet = UK sirloin = US strip).
Also covers EUROP carcase classification. Content marketing for the MeatGrader app. *verified: fetched*

**Helvetic Kitchen — "Swiss Cuts of Pork"** | https://www.helvetickitchen.com/curiosities/swiss-cuts-of-pork
~10 Swiss pork primals as a consistent Swiss -> UK -> US triple. Valuable because **Switzerland and
pork are both near-absent elsewhere.** Honest caveat: "Not every single cut is directly translated."
Dated 8 February, year inferred 2018 from image metadata. Small personal blog. *verified: fetched*

**Vlees & Co — "Which Dutch meat cuts are comparable to international cuts?"**
https://vleesenco.nl/en/blog/premium-meat/which-dutch-meat-types-are-comparable-with-international-cuts/
15-20 Dutch cuts mapped against American, French, Argentine, Japanese, Irish and Scottish
equivalents, with one genuine comparison table. **Only consumer-facing Dutch resource found.**
Butcher-shop content marketing; **no publication date or copyright notice at all**, so freshness is
unassessable. *verified: fetched*

**Minerva Foods — "Behind the different names for beef"**
https://myminerva.minervafoods.com/en/behind-the-different-names-for-beef/
~15 cuts in a table mapping Brazilian names to US, Argentine, French and Texan names (contrafile/New
York, picanha, Denver, flat iron, short rib, brisket). Published 6 Aug 2026, updated 24 Aug 2026 —
current. But it is a beef **exporter's** marketing piece using foreign nomenclature to justify
premium pricing, so treat mappings as promotional. *verified: fetched*

## Tier 4 — Codified US-only references

**Chefs-Resources — Meat Buyer's Guide / IMPS PDFs**
https://www.chefs-resources.com/types-of-meat/beef/cuts-of-beef/meat-buyers-guide-pdf/
Free USDA IMPS for Fresh Beef PDF with NAMP/IMPS item numbers, descriptions, cut photos, plus offal
and veal specs and an IMPS weight-range table. **US-only, no international nomenclature.**
"Chefs Resources Inc (c) 2026", but a reader comment from November 2015 already flagged the PDF link
as outdated, so stated freshness is not trustworthy. *verified: fetched*

**NAMI/NAMP "The Meat Buyer's Guide", 8th ed.**
https://amazingribs.com/books-meat-and-butchering-meat-buyers-guide-meat-lamb-veal-pork-and-poultry/
Search results describe 295+ illustrated cuts with NAMP/IMPS numbers, and the 8th edition as "the
first universal meat-cut reference for the U.S., Canada and Mexico" — that trilateral scope is the
only reason it is cross-country relevant. NAMP merged into NAMI in 2015. Printed book, paid.
*verified: **search-only**, not fetched — confirm against a copy before relying on it*

## Notable near-misses
- **French Meat Academy "meat thesaurus"** — SKOS, 1,519 concepts, bilingual FR/EN definitions,
  described in a *Meat Science* paper at
  https://www.sciencedirect.com/science/article/abs/pii/S0309174022001176 — paywalled abstract,
  unfetched, and the published SKOS file could not be located. **Would be the single best structured
  prior art if it can be found.**
- **CMA "Meat Cuts — European" multilingual glossary** indexed at
  https://www.proz.com/translation-glossary-post/Arabic-to-Czech/12484 — sounds ideal (13 languages,
  beef/pork/veal/lamb) but ProZ **403**s on every attempt. Publisher CMA was dissolved years ago, so
  the target is likely dead.
- **INRAE open thesaurus** (https://consultation.vocabulaires-ouverts.inrae.fr/, EN/FR, last modified
  2022-04-26) covers livestock categories, **not cut names** — not useful.
- wagyuinternational.com/cuts.php — DNS timeout.

## Search-quality honesty note (from the agent)
17 WebSearch queries; **four substantially junk** (the Reddit-targeted query returned zero Reddit
results — 8 of 10 links were Wikipedia; the Ireland/Bord Bia/Canada query found no Irish or Canadian
resource at all; the multilingual-culinary-dictionary query returned generic cooking-terms pages; the
INRAE query returned French-for-beginners vocabulary sites). Two **hard-failed**: reddit.com and
seriouseats.com are blocked to this user agent, so **Reddit and Serious Eats went unsampled** — the
forum-demand side is genuinely unmeasured. Of ~30 fetches, failures: unece.org (403 on four URLs,
including curl with a browser UA), proz.com (403), meatmynation.com/about (404),
wagyuinternational.com (DNS timeout). **Three PDFs returned as binary to WebFetch and were extracted
locally with pdftotext — the Lexicool and Swatland findings exist only because of that**, so PDF
items are worth extracting rather than trusting a fetch summary. WebSearch is US-only, so UK,
Australian and Irish domains are under-sampled.

## Shape of the English landscape
**A barbell with nothing in the middle.** At one end, codified trade standards (UNECE, AUS-MEAT HAM,
NAMP/IMPS) that are accurate, code-based and share a numbering spine, but are monolingual-per-
document, paywalled or 403-walled, and written for exporters not shoppers. At the other end, dozens
of one-country blog posts written for expats. The only things attempting the actual middle — a
browsable many-country name mapper — are **CarneAtlas, Meat My Nation and Cutranslator**, all
anonymous or LLC-fronted, all launched within roughly the last year, one openly running on demo data.
The niche is contested but not held.

Coverage is extremely lopsided by country pair:
- **US<->UK is saturated** (and best explained by a 2009 linguistics blog)
- **US<->Australia is the only pair with a proper code-level industry chart**
- **France is over-served** by hobbyists (FrenchEntree, MeatGrader, Your Guardian Chef, Third Culture
  Mama, Grasspunk)
- **Germany rests on a single 2011 blog post still collecting comments in 2024** — the loudest
  unmet-demand signal in the survey
- Genuinely thin or absent: **Ireland, Canada, Poland, the Nordics** (nothing found); Switzerland and
  the Netherlands (one hobbyist page each); **Japan and Korea** (drowned in wagyu marketing, with
  Swatland's 2012 table the only real name mapping); Spain/Latin America, where the two best datasets
  are an unattributed 2003 PDF and a July 2026 expat newspaper column
- **Pork and lamb are afterthoughts almost everywhere despite diverging *more* than beef across
  borders**
