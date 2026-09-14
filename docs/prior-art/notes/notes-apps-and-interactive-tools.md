# Notes: meat-cut apps and interactive web tools

> Source report used second-person framing ("your core premise") as if CarneAtlas were ours. It is
> not — it is the site under research. Framing stripped; facts retained.

**Fetch-resistance findings worth reusing:** Google Play pages **defeat WebFetch entirely** (JS payload
truncates before any data) but yield cleanly to `curl` with a browser UA plus regex — that workaround
produced every Play update-date, rating and description below. Apple pages fetch fine.
`beefitswhatsfordinner.com` and `bordbia.ie` return **403 to WebFetch but 200 to curl**.
`elearn.canadabeef.ca` fails TLS handshake outright.

## Photo-ID / AI identifiers — all new, all tiny
- **MeatGrader** https://play.google.com/store/apps/details?id=com.meatgrader.app ·
  https://apps.apple.com/us/app/meatgrader/id6758238890 · https://meatgrader.com/ — both stores.
  **The closest thing to the CarneAtlas concept that exists.** Claims "Regional cut names (US, Brazil,
  Argentina, Japan, Korea, and more)", an "Interactive beef cut diagram", and "Available in 10
  languages" — but **both store Information sections declare Languages: English only**, so the
  10-language claim is marketing, not shipped localisation. Core loop: photo -> 0-100 quality score.
  Play: updated Jul 20 2026, **100+ downloads, no rating**. iOS v1.1.25, "not enough ratings".
  Free / Pro $1.99mo / Producer Pro $19.99mo. Actively maintained, zero traction.
- **Seared: Meat Identifier AI** https://apps.apple.com/us/app/seared-meat-identifier-ai/id6757457110
  — Format Partners LLC. 50+ cuts from a photo, marbling, USDA grade estimate. **English only. No
  regional/country cut names.** v1.4 Jul 20; 5.0 from **1 rating**; free + IAP to $59.99 lifetime.
- **Steak ID : Steak Identifier** https://play.google.com/store/apps/details?id=com.tlt.androidapps.steak
  — claims 50+ cuts from a photo. English only, US names. Updated Mar 21 2026; **100+ downloads, no
  rating**. *(verified via curl; WebFetch truncates Play pages)*
- **ButcherIQ** https://www.meatidentifier.com/ — photo -> BUY / CONSIDER / PASS across beef, pork,
  chicken, lamb, turkey. No countries/languages stated.

## Cross-country / multilingual cut references — the thin part of the market
- **Meat translator** / "Traductor de Carne"
  https://play.google.com/store/apps/details?id=com.jpr.meattranslator — **the only live cross-country
  cut-name app found.** ES/EN/PT UI, but only **three countries: Argentina, Mexico, USA.** Offline,
  free, no IAP. Updated Jan 10 2026; **4.0 stars, 91 reviews, 10K+ downloads.** Maintained, very thin.
- **BeefCuts3D — Steak Guide** https://apps.apple.com/us/app/beef-cuts-3d/id1535823789 — iOS only;
  **the Android build (`com.Delikatessenschmiede.BeefCuts`) is now a hard 404 on Play.** Uli Niklaus /
  Metzgerhandwerk Bayern. **English + German only.** Real 3D rotatable carcass, "Steak Finder" wizard,
  and explicitly "common names and **synonyms**" per cut. Beef + pork. (A "52 cuts" figure appears in
  search summaries — **unconfirmed** on the store page.) **v2.0 shipped ~3 days ago**; prior v1.9 was
  2023-06-15 — a 3-year gap then a full relaunch. $4.99. 4.0 from 1 rating.
- **Ask The Butcher** https://apps.apple.com/ca/app/ask-the-butcher/id506886493 — Australian, English +
  German. **v2.1, Apr 30 2013. Dead** — Apple shows "the developer of this app needs to update it".
- **DELISTED — five relevant non-English apps return a genuine Play 404 on every locale tried**
  (en_US, en_CA, en_GB, de_DE, es_AR, pt_BR): `jozhu.vacamugequiz` (Portuguese beef-cut **quiz**),
  `ar.com.megaingenieria.ipcva.nomenclador` (**official Argentine IPCVA cut nomenclator**),
  `ar.com.megaingenieria.ipcva.lacarnenoshacefuertes` (IPCVA learning game), `air.ExpertoEnCarnes`,
  and the BeefCuts3D Android build.

## English-only cut glossaries — the established, mostly stale tier
- **Meat Cuts** (Meat & Livestock Australia) https://apps.apple.com/us/app/meat-cuts/id904537057 ·
  https://play.google.com/store/apps/details?id=com.mla.meatcuts — beef, lamb, veal, goat. Australian
  names, English only. Notable: **suggests an alternate cut** for the one you looked up. iOS v4.0.4
  Nov 6 2023; Play Oct 28 2023, **3.5, 456 reviews, 100K+ downloads — the highest-install cut
  reference found, ~3 years stale.**
- **Nose to Tail: Cuts of Meat** https://play.google.com/store/apps/details?id=com.socketsoftware.nosetotail
  · https://nosetotailapp.com/ — **200+ cuts across cow, chicken, lamb, pig** (80+ beef free, 120+
  behind one IAP). **Interactive butcher's diagram plus an "X-ray" feature**, hand-drawn illustrations,
  browse-by-cooking-method. English only, mixed US/UK names. Updated Aug 19 2024; **4.2, 299 reviews,
  50K+ downloads.** Semi-dormant (Aug 2024 = Google's target-SDK deadline, a compliance push).
- **Meat Purchasing Guide** (AHDB, UK) https://play.google.com/store/apps/details?id=uk.org.ahdb.meatpurchasingguide
  — **850+ beef/veal/lamb/mutton/pork cuts** with cutting specs, product codes, carcase classification.
  UK only. B2B trade reference. **Updated Feb 24 2026**; 4.5 stars; only 50+ downloads.
- **MyMeatUp** (Meat Institute, US) — v2.0.0, **Oct 2017. Abandoned.**
- **BEEFabulous** (California Beef Council) — v1.2.0, **May 2019. Abandoned.**
- **BEEFoodservice** (California Beef Council) — NAMP/IMPS ordering numbers, cutting videos, two
  training courses. Play updated Aug 18 2025, 4.5, 500+ downloads. Maintained.
- **Schweizer Fleisch / Viande Suisse** https://play.google.com/store/apps/details?id=com.appswithlove.ent.academy
  — Swiss; 56 preparation techniques, "Nose to Tail" off-cuts special. Updated Aug 19 2024, no rating,
  **100K+ downloads.** Semi-dormant.
- **CutRite** — wild game (deer, elk), custom "meat maps". **Updated Jul 23 2026**, 4.3, 500+ downloads.
- Noise, not relevant: Top Cut (AU B2B ordering), Meat Rank (rate cuts eaten at restaurants, Argentine
  names), plus a dozen butcher delivery apps.

## Interactive web tools
- **Beef. It's What's For Dinner — Cuts** (US Beef Checkoff / NCBA)
  https://www.beefitswhatsfordinner.com/cuts — **the benchmark, and genuinely a clickable cow.** HTML
  read directly: a real `<img usemap="#image-map-primal-cut">` over
  `PrimalCuts_LtGray_Transparent.png` with **10 `<area shape="poly">` hotspots covering 9 primals** —
  chuck, rib, loin, sirloin, round, brisket, flank, short plate, shank (x2) — each linking to
  `/cuts/cut/<id>/<slug>`. Toggle between primal and ingredient cuts, six curated collections, cut
  search. **US-only, English, no language switcher.** Implementation is a **1990s HTML image map, not
  SVG** — no zoom, no hover detail, no mobile-friendly hit targets. `/butchercounter.aspx` is the
  legacy name for the same tool. *(verified via curl; WebFetch 403s)*
- **Canada Beef — Interactive Beef Carcass** https://canadabeef.ca/carcass/ — "Click on a Primal Cut to
  view Sub-Primal Cuts", **9 sections** (HIP, SIRLOIN, LOIN, RIB, CHUCK, FLANK, PLATE, BRISKET, GROUND
  BEEF & VARIETY MEATS). Each sub-primal carries a **NAMP number**, a real technical butchering
  description, cooking methods and applications (Ponderosa Hip #166B and Eye of Round #171C read in
  full). **Inline SVG.** Site has a **Francais toggle, so EN/FR. Arguably better data than the US
  tool.**
- **Simply Beef & Lamb — Beef Cuts** (AHDB, UK) https://www.simplybeefandlamb.co.uk/cuts/beef-cuts/ —
  clickable carcass, ~40+ British cuts by section, British names like silverside and bistro rump.
  UK-only, English. (c)2026, maintained.
- **AHDB Virtual Beef & Lamb** https://virtualbeefandlamb.ahdb.org.uk — virtual livestock viewed from
  every angle as conformation and fat class change, with a Carcase cuts section and yield data, offline
  mode. **A grading/selection trainer for farmers, not a cut-name glossary** — no cross-country naming.
- **cuttingmeat.com** https://cuttingmeat.com/ — "Explore all 9 primal cuts of beef on our interactive
  diagram." Victor Mondial, self-described master butcher. US-only, English. Independent
  content/affiliate site — a direct analogue of the CarneAtlas monetization model, minus the languages.
- **Half a Cow Club — Beef Cuts Chart** https://halfacowclub.com/guides/beef-cuts-chart — tappable
  8-primal diagram with **yield percentages** (Chuck 26%, Round 22%, Rib 9%, Sirloin 9%, Short Loin 8%,
  Plate 6%, Brisket 5%, Flank 3%) and a cut-sheet builder. US-only. SEO content marketing for a
  bulk-beef broker.
- **Bord Bia (Irish Food Board) — Beef Cuts** https://www.bordbia.ie/meat/cuts/beef-cuts/ — **not
  interactive.** Title is literally "Your Guide to **12** Beef Cuts"; HTML grepped, no clickable
  diagram, no image map. Ireland, English. *(verified via curl; WebFetch 403s)*
- **IPCVA / Argentine Beef** https://argentinebeef.org.ar/en — site is **trilingual ES/EN/ZH** with a
  "Names of cuts" / "Handbook of Argentine beef" section — **the only official non-English
  multi-language cut-naming resource still live.** Appears to be a downloadable handbook rather than an
  interactive tool (handbook itself not opened).
- Static cross-country references: https://prydebutchery.com.au/global-guide-to-beef-cuts/ (USA/UK/
  Australia only, ~40 cuts, no search or interactivity), plus
  https://en.wikipedia.org/wiki/Cut_of_beef and the Wikimedia Commons SVG set (e.g.
  `File:Beef_cuts_Brazil.svg`) — **the de-facto free multi-country diagram source everyone traces from.**
- Search-only, not fetched: meatcutguide.com/guides/beef-cuts-chart/, christensenranch.com/cuts-of-beef/,
  pafarmlink.org/resource/pfl-meat-cutting-diagrams/, **wagyuinternational.com/cuts.php (Japanese +
  English names, dishes by country — worth a look for Japan data)**, easyanddelish.com/meat-cuts-beef/.

## The two differentiator questions, answered
**(a) Photo-ID of a cut — YES, it exists, four times over**, but every one is a 2025/26 startup with
essentially no users. Steak ID's own store text: "SteakID instantly identifies any beef cut from a
simple photo... Identifies 50+ popular steak cuts". MeatGrader's: "Photograph your beef cut and get
results in seconds. MeatGrader identifies the cut." So photo-ID is **not** unclaimed — but the combined
installed base of all four is roughly 200 Android downloads plus two apps with one rating each.
**Only MeatGrader pairs photo-ID with regional cut names, and it declares English-only in both stores.
Nobody has combined photo-ID with a genuine multi-country name map.**

**(b) A game/quiz/puzzle about cuts — effectively NO, and certainly no daily puzzle.** What exists:
two amateur one-off web quizzes — https://www.purposegames.com/game/beef-cuts-of-meat-game
(click-the-diagram, 11 questions, 6,193 plays, user account) and
https://www.sporcle.com/games/WhyAmIDoingThis/us-cuts-of-beef (picture-click, 13 US cuts, forced
order, 9,064 plays, last updated **Feb 16 2017**). Both UGC parked on general quiz platforms, English,
US-only, single static quiz. Search-only leads: Quizlet flashcard sets, Quizalize, quiz-maker.com, a
trivia page at hindquarter.ca. **On mobile: zero live cut quiz apps** — the one that existed, the
Portuguese `jozhu.vacamugequiz`, is now a 404. Seared has "COMPETITIVE RANKED GRILLING... compete on
the global leaderboard", which gamifies *grilling*, not cut names. **A daily meat-cut puzzle does not
exist; the daily-food-puzzle genre is all word games** (Foodle, Phoodle, Daily Dish, Tastele).

## Landscape read
**Wide but uniformly shallow, split cleanly in two with nothing bridging the gap.** On one side,
well-funded but nationally siloed beef-board tools — the US Checkoff's clickable cow, Canada Beef's
bilingual carcass, AHDB's UK carcass and 850-cut trade guide — each excellent within one country's
naming system and each **structurally incapable of telling you that a UK silverside is a US bottom
round**; the US benchmark is still literally an HTML image map with nine hotspots. On the other side, a
dozen abandoned single-country glossary apps (MyMeatUp untouched since 2017, BEEFabulous since 2019,
MLA's Meat Cuts — the install leader at 100K — since 2023) plus a fresh crop of 2026 AI photo-ID apps
with a combined few hundred downloads.

**The cross-country name-mapping job is served today by exactly one 10K-download Android app covering
three countries, one app's unlocalised marketing claim, a Sydney butcher's static HTML table covering
USA/UK/Australia, and Wikipedia.** That is close to empty for ~10 countries. Photo-ID is real but no
longer novel — table stakes rather than a headline. **The daily puzzle is the genuinely unoccupied
ground.**

## Query hygiene
19 searches. **Five returned nothing usable** — German `Fleischteile Rindfleisch` (only delivery apps
and two unrelated Wikipedia articles), Japan/Korea interactive diagrams (**no such tool exists**; all
static guides and Pinterest), Brazil/Argentina IPCVA interactive, the daily-puzzle query (confirmed an
absence), and the grilling/BBQ + meat-thermometer-app family (**zero app-store results — that
hypothesis is dead**). Three more were half junk, drowned in butcher delivery apps.
