# Notes: direct competitors, photo-ID apps, daily-game slot

All items below were fetched and verified by the agent unless marked otherwise.

## Direct competitors — same product concept

**Cutranslator** | https://cutranslator.com/
A working country-to-country beef cut *name translator*. Maps regional names onto "26 canonical
cuts—spanning all eight USDA primals". Source/destination country pickers, plus reverse lookup at
`/what-is/<local-name>` — e.g. https://cutranslator.com/what-is/nyretap correctly returns Danish
*nyretap* -> hanger steak and lists *onglet* (FR), *Nierenzapfen* (DE), *sagari* (JP).
Self-description inconsistent: one page says "2144 routes" over 190+ regions "Afghanistan through
Zimbabwe", another says "89 source countries / 134 destinations".
Operator "Albor Digital LLC", footer "(c) 2026". **No photos, no photo-ID, no game.**
Quality caveat: an A-to-Z list of 190+ countries including many with no distinct beef-naming
tradition, plus thin templating, reads as programmatic SEO rather than researched butchery. A
guessed Afghanistan URL 404'd, so exotic pairs are unverified.

**Meat My Nation** | https://meatmynation.com/
Explicitly a cross-country name-equivalence browser plus recipes/traditions, community-contribution
model. 8 countries on the homepage (Argentina, Australia, Brazil, France, Japan, Mexico, UK, US).
**Currently hollow**: `/cuts` states "18 cuts documented (demo data)" — 15 beef, 2 pork, 1 lamb — and
the site labels itself "Phase 1 MVP", "Demo data — not authoritative reference material", with
"Pro tools, API access, and educational packs — coming in future phases". (c) 2026. `/about` is 404.

**beefcuts.org** | https://beefcuts.org/
Search-result title: "Beef Cut Translations: Brazil, Argentina & Costa Rica". **Fetch failed — TLS
is broken**: the certificate presented is for `*.b-cdn.net`, not the domain; `www` does not resolve.
That is itself a maintenance signal. Content claims unverified.

## Photo-ID apps — not an empty field, and one overlaps CarneAtlas directly

**MeatGrader** — the single closest competitor to CarneAtlas' whole package.
https://meatgrader.com/ | https://apps.apple.com/us/app/meatgrader/id6758238890
iOS + Android. Photo -> quality score; "identifies the cut, then scores marbling". Store listing
advertises **"Regional cut names (US, Brazil, Argentina, Japan, Korea, and more)"** plus an
**"Interactive beef cut diagram"** with regional diagrams for EU/UK, Japanese, Korean, Australian,
Argentine, Canadian and Brazilian cuts. Marketing site claims "10 languages and regional cut names
from Buenos Aires to Tokyo."
Store facts verbatim: "Version 1.1.25 Jul 20", Seller "Johalf Farina", Languages "English",
free with IAP (Pro $1.99 / Producer Pro $19.99mo / $190yr); **rating count NOT FOUND** (no ratings).
**Discrepancy: site claims 10 languages, App Store lists English only.** Very new solo-dev app, no
traction — but aiming at exactly CarneAtlas' pairing of photo-ID plus multi-country naming.

**Seared: Meat Identifier AI** / **ButcherIQ** — one operator, two brands.
https://apps.apple.com/us/app/seared-meat-identifier-ai/id6757457110 | https://www.meatidentifier.com/
Photo-ID of 50+ cuts, marbling and USDA grade estimate, cooking guides. Verbatim: "Version 1.4
Jul 20", "5.0 out of 5 / 1 Ratings", English, "(c) 2026 Format Partners LLC", free with IAP
$2.99/wk–$59.99 lifetime. US/USDA-centric, **no cross-country naming**.

**Butchr** | https://apps.apple.com/us/app/butchr/id6758029766
Photo -> USDA grade estimate, marbling, freshness, cooking recs. Verbatim: "Version 1.0.2 Feb 11",
"5.0 out of 5 / 5 Ratings", English, Seller "Abhinav Sehgal", free. US-only, no multilingual names.

**Steak ID : Steak Identifier** | https://play.google.com/store/apps/details?id=com.tlt.androidapps.steak
Search result describes photo ID of 50+ steak cuts. **Fetch failed** — Google Play truncates before
metadata renders (tried twice). Ratings, installs, multilingual status unverified. **search-only**

## Interactive diagram apps

**BeefCuts3D – Steak Guide** | https://apps.apple.com/us/app/beef-cuts-3d/id1535823789
Rotatable, zoomable 3D beef and pork anatomy; select cuts on the model or via searchable list;
"Steak Finder" recommends by cooking method, time and budget. **Covers two naming conventions:
English and German** — the only app besides MeatGrader with cross-country naming. Verbatim:
"Version 2.0 3d ago", "4.0 out of 5 / 1 Ratings", Languages "English and German", Seller "Uli
Niklaus", $4.99. Actively maintained (v2.0 three days ago, updates back to 2023), almost no users.

**MeatVault** | https://apps.apple.com/us/app/meatvault/id6759194672
Freezer inventory tracker with a preloaded cut database — **not relevant** to name equivalence.

## The daily puzzle — the one genuinely empty slot
Checked https://listdle.com/, an index of daily Wordle-likes. Its food games: **Tastedle** (guess a
dish's country of origin), **Guess The Menu**, **Scrandle** (stadium food), **Nutrition Factdle**.
Also **Foodle** (word game, many clone domains) and https://dailydishgame.com/ (guess recipes from
ingredient clues). **No game about meat cuts or butchery appears in the index**, and none of the food
games touch cut names.

## Layered verdict on the consumer web
- **Static pairwise charts: well served.** US<->UK<->AU, US<->Brazil, French->English all have good
  pages (see notes-english-cross-country.md).
- **Interactive name translation: occupied, but weakly.** Cutranslator is the one real incumbent and
  does the core job. Breadth looks programmatic rather than researched; no imagery at all — which is
  exactly where a photo-and-diagram site beats it.
- **Photo-ID: more crowded than you'd expect.** Four AI photo apps, all 2026-vintage, all
  solo-developer, all with single-digit rating counts. Only **MeatGrader** combines photo-ID with
  regional cut names; only **BeefCuts3D** otherwise does multi-country naming (EN/DE).
- **Daily puzzle about cuts: nobody.** Confirmed absent from the main daily-games index.

So the *combination* — free web, ~10 countries, photo-ID, daily puzzle — is unoccupied. But every
component except the puzzle now has at least one incumbent, and **MeatGrader and Cutranslator are
the two to watch**.

Coverage caveat: WebSearch is US-only, so non-English findings are systematically thin.
