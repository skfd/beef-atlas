# Notes: CarneAtlas itself — provenance, sourcing, footprint

## Public discussion: none exists
Primary negative finding. Searched via the platforms' own backends, not Google ranking:

| Surface | Result |
|---|---|
| HN (Algolia API, 4 query shapes incl. url-restricted) | `nbHits: 0` |
| Lobsters | "0 results for carneatlas" |
| Product Hunt (native search) | "No products found" |
| Reddit (PullPush index, submissions + comments) | empty |
| GitHub repo + code search (incl. authed `gh search`) | `total_count: 0` |

Weak negatives only: `site:`-restricted WebSearch (backend did not honour `site:` as a hard filter),
reddit.com direct fetch tool-blocked, Bluesky searchPosts 403. A low-engagement tweet could exist
unindexed, but HN/Lobsters/PH/PullPush are reliable. **No launch thread = no community-cited
alternatives to harvest.**

Also searched, nothing found: Indie Hackers, X/Twitter, Medium, Google News, YouTube, Facebook,
Mastodon, BetaList, Uneed, SideProjectors, Toolify, SimilarWeb.

## Naming hazard
- `"carne atlas"` as a phrase is already the Heinrich Boll Foundation's **Meat Atlas**
  (https://www.boell.de/en/meat-atlas)
- `carneatlas launch` -> Carne Group (fund services); `carneatlas review` -> Carnimeat (carnivore app)

## Provenance — hard facts
- **Domain registered 2026-03-31T20:19:34Z**, NameCheap, expiry 2029-03-31
  (Verisign RDAP: https://rdap.verisign.com/com/v1/domain/CARNEATLAS.COM)
- **Content `datePublished` = 2026-04-01 (cuts) / 2026-04-02 (fish)** — one to two days after
  registration, clustered within *seconds* (ribeye 18:26:19, onglet 18:26:28, picanha 18:26:41).
  Bulk generation, not incremental writing. Second batch 2026-04-27/28. Site-wide `dateModified`
  sweep 2026-08-14 and 2026-08-16.
- **Wayback: exactly one capture of the whole domain** — `20260610185042` of `/pork`. Homepage never
  archived. (CDX with matchType=domain; the `available` endpoint 429'd.)
- **No /about, /privacy, /terms, /contact, /humans.txt, /llms.txt, /.well-known/security.txt,
  /ads.txt** — all 404. Sitemap (701 URLs) has no about/legal/sources page.
- Footer names no person, no company, no year. Only ownership signal: "As an Amazon Associate I earn
  from qualifying purchases" — first person singular, a solo operator.
- Next.js App Router; images on Cloudinary.
- Amazon tags **`carneatlas-20`** (.com) and **`carneatlas02-21`** (.fr) — geo-localised. Clicks route
  through an internal redirector instrumented per page and per placement:
  `/go/amazon?target=...&productId=...&position=curated_gear&pageType=cut&pageSlug=ribeye&country=US`.
  `/go/` is Disallowed in robots.txt.

## Creator — inference only, not confirmed
Cloudinary cloud name in every image URL is `rogerpscott`
(`res.cloudinary.com/rogerpscott/image/upload/.../carneatlas/cuts/ribeye.jpg`). A GitHub login of
that exact name exists (created 2016, bio "Learning how to code!", 19 public repos: bootcamp
exercises, a 2025 `mancala`, a 2026-08 `residency-mexico-consulate-data`). **None of the 19 repos is
carneatlas.** This is a same-handle correlation between a Cloudinary cloud name and a GitHub login —
suggestive, not proof. No page exists on which carneatlas.com and a person's name appear together.

## Does it cite sources? Splits sharply by page type
**Cut pages (`/cut/<slug>`) — sourced.** 6/6 sampled carry a `citation` array in JSON-LD *and* a
rendered Sources block:
- ribeye -> Wikipedia *Rib eye steak*; **USDA AMS IMPS Series 100 — Fresh Beef**
  (https://www.ams.usda.gov/grades-standards/imps); **NAMI** *Meat Buyer's Guide*
- picanha -> Wikipedia; **ABCZ** (Assoc. Brasileira dos Criadores de Zebu)
- onglet -> Wikipedia *Hanger steak*; **Larousse Gastronomique** (`url: null`, book ref)
- carnitas -> Wikipedia; **Larousse de la Cocina Mexicana** (`url: null`)
- oxtail -> Wikipedia; USDA AMS IMPS
- galbi, tafelspitz -> **Wikipedia only**

Wikipedia is always first.

**Fish pages (`/fish/<slug>`) — unsourced.** 4/4 sampled (tuna, sardinha, turbot, huachinango) have
zero citations. **FishBase is not referenced anywhere on the site.** No scientific binomial either —
tuna is labelled only with the family "Scombridae". Only attribution is the photo credit.

**Primal pages, country pages, /identify** — no citations.

## What a cut page actually contains (/cut/ribeye, in order)
Title + primal breadcrumb (Beef - Rib) + cooking-method tags; Compare/Save/Share bar; inline
**"Buy Ribeye - Amazon"** affiliate card (labelled "Affiliate link"); "Also called" flag strip;
**Wikimedia Commons photo with full licence credit** (photos are borrowed, not original); ~60-word
description; **names-by-country table with a Notes column carrying genuinely specific local
knowledge** (Italy: "Boneless ribeye is sold under the French loanword; bone-in is 'costata'";
Germany: "Loanword used at retail; 'Hochrippe' refers to the whole bone-in rib roast"); a
"What to ask for / I'm shopping in <country>" widget; a "Source this cut" affiliate block; similar
cuts with per-pair prose that is anatomically correct (rib cap = spinalis dorsi on the longissimus
dorsi); substitutes-by-primal selector; cross-promo to the daily puzzle; one linked recipe; a
"Get this cut right" gear block (Thermapen ONE, Lodge cast iron) with price tier and justification;
newsletter signup ("Every Thursday", twice); more cuts in primal; Sources.

**Depth read: better than a content farm, short of authoritative.** Anatomical and nomenclature notes
are specific and mostly correct; cut-page sourcing is real and checkable. Against that: FAQPage
schema is template-filled, fish coverage entirely unsourced, everything published within ~48h of
domain purchase.

Two credibility flags (worth checking, not asserting):
- ribeye page gives the **UK** name as "Scotch fillet" — that is more typically AU/NZ usage
- `/fish/robalo` titled "Robalo in English: Snook", collapsing European-Portuguese (sea bass) with
  Latin American (snook); meanwhile `sea-bass` redirects to `/fish/loup-de-mer`

## Scale, from the sitemap (701 URLs)
**117 distinct cut pages** (64 beef + 40 pork + 13 lamb, matching the homepage claim exactly),
**39 fish species**, 10 country pages, 110 recipes, 117 cut-vs-cut and 75 fish-vs-fish comparison
pages, plus `/compare`, `/substitute`, `/gear`, `/identify` and 6 national-specialities pages.
A 60-URL sample of `/cut/` pages: none redirect, so all real distinct pages. Alias slugs do redirect
(`/cut/entrecote`, `/cut/ojo-de-bife` -> `/cut/ribeye`; `/fish/monkfish` -> `/fish/lotte`) — and the
canonical fish slug is often the non-English name. Minor inconsistency: `/identify` says "8 locales"
while the site presents 10 countries. The 10: US, UK, Mexico, Argentina, France, Spain, Portugal,
Brazil, Italy, Germany. Spain's country page alone shows "109 entries".

`/identify` is an AI visual identifier, up to four angles of one cut, free and account-free, hedged
in its own FAQ ("an AI visual assessment, not a definitive identification... For certainty, ask your
butcher").

## The daily puzzle
`/guess` — "Guess the Cut". **Puzzle #29 on 2026-09-13**, "five questions - a new board every day",
free, no sign-up. `Game` JSON-LD names three question types: name the cut, place it on the animal,
say which country calls it that. Sample rendered question: *"A butcher hands you Maminha. Which
country are you in?"* (Brazil / UK / Portugal / Spain). Per-animal boards at `/guess/beef|pork|lamb`.
Inference: #29 on Sep 13 back-counts to a first board around 2026-08-16, matching the site-wide
`dateModified` sweep of 2026-08-16 — so the puzzle looks like a mid-August addition, unconfirmed.

## Adjacent prior art surfaced incidentally (NOT community-cited)
- Anova thread asking for exactly this resource (2018-05-16):
  https://community.anovaculinary.com/t/butchery-anatomy-gastronomy-books-websites-for-better-understanding-various-cuts-and-muscles-along-with-their-culinary-quality/14608
  — answers named only books/video: *A Field Guide to Meat*, Time-Life *The Good Cook*, YouTube
  breakdowns. **No websites.** Telling.
- https://bbqnewsletter.substack.com/p/friday-find-a-visual-guide-to-the
- Spanish "Atlas Cortes de Carne de Res" PDF:
  https://pdfcoffee.com/atlas-cortes-de-carne-de-res-4-pdf-free.html
- https://www.beefitswhatsfordinner.com/cuts/cut-charts

**Net: indexed and crawlable with real content, but zero inbound social/editorial footprint.**
