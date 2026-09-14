# Research method and confidence

**What to trust in this survey, and what not to.** Filed into `beef-atlas` at `docs/prior-art/`.

Research date **2026-09-13**. Started from a bare prompt: *"i found this https://carneatlas.com/ are there
any other prior art? let's research"*. No further steering was given, so the scope taken was the plain
reading — **other cross-language / cross-tradition meat-cut references** — plus a short section on the
format (reference corpus + daily game + affiliate links).

## What is here

| File | Lines | What it is |
|---|---|---|
| **`landscape.md`** | 424 | **Read this one.** The synthesis: short answer, a 22-row comparison matrix, five tiers of prior art, the three direct competitors, what is actually unoccupied, and the findings that would break a naive data model. |
| `notes-standards-and-industry.md` | 393 | UNECE, IMPS, URMIS, AUS-MEAT/HAM, Canada (CFIA/Canada Pork/Canada Beef), AHDB, EU regulations, Codex, Japan (JMGA/MAFF), Korea (MFDS). |
| `notes-non-english.md` | 287 | ES / PT / FR / DE / IT. ABIEC's 12-language glossary, the nine-column table, Weidefleisch, Italian name collisions. |
| `notes-fish-naming.md` | 265 | FishBase, FAO ASFIS, FishFinder, EU Reg. 1379/2013 national designation lists. |
| `notes-open-data-encyclopedic.md` | 257 | Wikipedia, Wikidata (incl. SPARQL queries and results), FoodOn, LanguaL, OFAJ glossary, academic literature. |
| `notes-structured-food-sources.md` | 254 | Wiktionary, Open Food Facts, USDA FoodData Central + IMPS, Wikibooks, FoodSubs, AGROVOC. |
| `notes-english-cross-country.md` | 210 | Lexicool 2003 PDF, Swatland 2012, Aussie Beef chart, expat blogs and the demand signals in their comment threads. |
| `notes-apps-and-interactive-tools.md` | 159 | Measured app-store metadata, the clickable-cow benchmarks, confirmed absence of any daily cut puzzle. |
| `notes-the-site-itself.md` | 128 | CarneAtlas provenance: RDAP, JSON-LD timestamps, Wayback, sourcing behaviour per page type, zero social footprint. |
| `notes-competitors-and-apps.md` | 93 | Cutranslator, Meat My Nation, MeatGrader, BeefCuts3D. |
| `notes-format-analogues.md` | 47 | TasteAtlas, VIVC, corpus-plus-daily-game precedents, the Heardle shutdown. |

The notes are raw per-thread output, deliberately kept rather than collapsed — they carry the URLs,
measured counts and negative results that `landscape.md` compresses. **If you need to re-verify a number, it
is in the notes with the URL it came from.**

## The answer, in five lines

1. **Extensive prior art exists**, and the equivalence data has been compiled repeatedly by institutions
   since at least 2003 — it is just locked in PDFs, trade specs and national documents that do not
   cross-reference each other.
2. **UNECE is the spine**: cuts standardised by anatomy with stable numeric codes **and a five-language
   index** (EN/FR/RU/ES/ZH), plus a Retail Meat Cuts standard that bridges retail names to wholesale codes.
3. **CarneAtlas is five months old, bulk-generated, anonymous, and has zero inbound footprint** — but its
   corpus is real and its meat-cut sourcing is honest. Its fish section is indefensible.
4. **Three sites launched into this niche in roughly the last year** (CarneAtlas, Cutranslator, Meat My
   Nation); none has traction, and one runs on demo data.
5. **The genuinely unbuilt thing is narrow**: a *country*-keyed (not language-keyed) browsable map. A daily
   puzzle about cuts is the one clear empty slot.

## Read this before trusting anything

**One claim in this research was overturned mid-flight, and the correction pattern matters more than the
fact.** Three threads concluded UNECE was English-only — each inferring it from a Stanford catalogue field
after `unece.org` returned Cloudflare 403s. A fourth thread reached the documents via Wayback raw-asset
URLs and read a five-language index directly. **The report now says UNECE is multilingual, with the
correction flagged inline rather than quietly swapped.**

Generalise it: where these notes record a *negative* that rests on a blocked fetch rather than a read
document, treat it as unproven. The notes mark these. The known-weak ones:

- **`unece.org` 403s everything** (WebFetch and curl with a browser UA). Two Wayback PDFs are truncated at
  exactly 1 MiB, so the Chicken standard's internals and Bovine Rev.2 2016 stay unverified — as does formal
  adoption of the 2023 bovine revision.
- **reddit.com and seriouseats.com are blocked** to this user agent. **Forum demand is genuinely
  unmeasured** — the one real hole in the survey. Evidence of demand rests on blog comment counts instead.
- **URMIS's actual name/code lists are login-gated.** The freely available AMSA/NCBA secondary source
  (agrilife.org 4hmeat guide, 68pp) reproduces the numbers with photos.
- **Google Play defeats WebFetch** (JS truncates before metadata); `curl` + browser UA works. Apple pages
  are fine. This is saved as a memory (`web-research-fetch-resistance`) so future sessions don't rediscover it.
- **Dates on hobbyist sites are mostly worthless** — auto-renewing "© 2026" with no real revision date.

## The decision this is blocked on

I asked and it went unanswered, so it sits here. **The answer determines whether a second round is worth
running, and what it chases:**

1. **Build something** → the target is a country-keyed layer over UNECE codes. First loose ends: settle
   whether AUS-MEAT's HAM numbers really *are* UNECE numbers (AUS-MEAT claims so; its own per-cut PDFs list
   them as separate fields), and diff the Lexicool 2003 PDF against the MAGyP 2007 glossary — identical
   nine-column sets in the same order, possibly one document.
2. **Contribute to what exists** → Spanish Wikipedia has **no cuts-of-beef article at all**, and Wikidata
   **structurally cannot express per-country naming** (country property on 2 of 54 items). Both are open
   doors; Commons diagrams are all reusable.
3. **Just sizing up CarneAtlas** → done, stop here. Real corpus, honest on meat, unsourced on fish, less
   novel than it looks.

## Open loops, in rough order of value

- **Swatland, *Meat Cuts and Muscle Foods: An International Glossary*, 2023 ed.** — the most relevant
  published work in existence and **nobody read it**. Author is emeritus at **Guelph**; possibly reachable
  through the local library system. Only its ISBNs were verified.
- **The French Meat Academy SKOS thesaurus** (1,519 concepts, bilingual FR/EN definitions) — would be the
  best structured prior art if the file can be found. Described in a *Meat Science* paper; SKOS file not
  located.
- **Diff Lexicool 2003 vs MAGyP 2007** (see above) — decides whether there are seven or eight independent
  multi-country tables.
- **HAM vs UNECE code identity** — decides whether one crosswalk or two.
- **Trypuz et al. (2016)**, machine-readable representation of the UNECE bovine standard
  (doi 10.1007/978-3-319-49157-8_12) — paywalled; **do not assume it handles multilingual naming.**
- A 2014 Venezuelan paper whose title is exactly a Spanish↔North-American cut-name mapping, with **no DOI,
  no venue, no authors** (Semantic Scholar paperId `14cee89716f570662b60e6211021f1fe7c6d15d7`).
- **The origin of the "120 Korean cuts" figure** — not traced. The official count is **49 beef / 32 pork**;
  the folklore number has no primary source and would have been repeated if unchecked.
- One manual browser attempt at `unece.org` would close several unverified cells at once.

## Housekeeping

- This research now lives in `beef-atlas` at `docs/prior-art/`. It was produced in a scratch folder and
  filed here afterwards, so any path referring to `~/Code/cowork` in the notes is historical.
- A `reference` memory was written: `web-research-fetch-resistance` — the fetch-resistance patterns above
  are cross-project reusable and cost real time to discover.
