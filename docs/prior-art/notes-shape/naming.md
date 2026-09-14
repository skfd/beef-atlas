# Renaming the atlas: 10 candidates, checked

`Beef Atlas` collides with a live App Store product in the same category
([id6796940694](https://apps.apple.com/us/app/beef-atlas-3d-cuts-guide/id6796940694)) — see
[`shape.md` §2](../shape.md). This file is the replacement shortlist, with every availability
claim traced to a fetch made on **2026-09-13**.

## The top three

**1. Longissimus.** The one muscle that every tradition divides differently — it is the US short
loin, the British sirloin, Russian тонкий край, Korean 채끝, Japanese サーロイン, all at once. That
is the project's thesis compressed into one word, and it is the only candidate that reaches both
layers of the repo: the cut data *and* the 115-part anatomy model. Latin, dry, reference-register,
and it means something you can explain in four words ("the longest one"). `github.com/skfd/longissimus`
is free, the username is free, `.dev` and `.app` are unregistered, and neither storefront has
anything. Its problem is real and stated below.

**2. Cut Concordance.** The cleanest slate among the viable candidates — **every single check came
back free**: all four TLDs unregistered, GitHub repo and username free, nothing on either
storefront, no famous owner. (`Razrub` and `Balgol` match it on availability; both are rejected
below on other grounds.) It also names the actual mechanism with a citation behind it: Bohland et al.
(2009) is literally *"The brain atlas concordance problem"*, the paper `shape.md` §3 identifies as
this project's shape in another substance. The caveat is sharper than availability, and it is in
the section below.

**3. Parcellation.** The most *accurate* name available. Neuroimaging already uses it for exactly
this problem — one object, many rival schemes dividing it into regions that disagree — and it is in
the Bohland paper's subtitle (*"Quantitative Comparison of Anatomical Parcellations"*). Adopting the term of art moves the atlas from homemade to cited. `.org`, `.dev`
and `.app` free, GitHub entirely free, both storefronts clear.

Runner-up worth keeping in the drawer: **Coextensive** — precise, unclaimed on GitHub, zero App
Store results, but an adjective, and adjectives make poor mastheads.

## A structural finding that outranks availability

Three candidates are butchery terms borrowed from one of the seven traditions — 枝肉 (Japan),
разруб (Russia), 발골 (Korea). All three are correctly romanised and none is offensive. But **a
project whose entire thesis is that no tradition is the reference frame should not be named in one
tradition's language.** Naming it `Razrub` makes Russian the metalanguage for describing Russian,
Korean, Japanese, French, British, Brazilian and American butchery. That is a worse problem than
any domain being taken, and it is why all three sit low in the table despite `razrub` and `balgol`
having perfectly clean availability.

A second axis, from the linguistic check: `Balgol` and `Razrub` name a *violent operation*
(extract-bone, chop-apart), `Edaniku` names the *object*, `Longissimus` names a *part*, and
`Parcellation` / `Coextensive` / `Concordance` name the *method*. This atlas charts lines; it does
not swing a cleaver. The method and part registers fit; the operation register does not.

## The table

`.com` / `.org` / `.dev` / `.app` — **F** = unregistered (RDAP 404), **T** = registered (RDAP 200).
GitHub column is `skfd/<slug>` repo / bare `github.com/<slug>` user-or-org.

| # | Name | .com | .org | .dev | .app | GitHub repo / user | App Store | Play | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Longissimus** | T | T | **F** | **F** | **free** / **free** | clear | clear | **Strong** — best thesis fit, names one muscle |
| 2 | **Cut Concordance** | **F** | **F** | **F** | **F** | **free** / **free** | clear | clear | **Strong** — everything free; term already loaded in meat science |
| 3 | **Parcellation** | T | **F** | **F** | **F** | **free** / **free** | clear | clear | **Strong** — exactly right, forbidding |
| 4 | **Coextensive** | T | **F** | **F** | **F** | **free** / **free** | clear (0 results) | clear | **Viable** — precise, but an adjective |
| 5 | **Coregister** | T | **F** | **F** | **F** | **free** / **free** | clear | clear | **Viable** — names a preprocessing step, not an atlas |
| 6 | **Aitchbone** | T | **F** | **F** | **F** | **free** / *taken* | clear | clear | **Marginal** — an actual product on sale at UK butchers |
| 7 | **Razrub** (разруб) | **F** | **F** | **F** | **F** | **free** / **free** | clear | clear | **Reject** — picks one of seven traditions as metalanguage |
| 8 | **Balgol** (발골) | **F** | **F** | **F** | **F** | **free** / **free** | clear | clear | **Reject** — BALGOL is a 1960s programming language |
| 9 | **Edaniku** (枝肉) | T | **F** | **F** | **F** | **free** / **free** | clear | clear | **Reject** — a famous Japanese play about a meat plant owns it |
| 10 | **Chine** | T | T | **F** | **F** | **free** / *taken* | clear | clear | **Reject** — French for *China*; also a narrow existing butchery verb |

Also checked and cut before the table: **Concordance** (bare), **Seven Knives**, **Same Animal**,
**Shared Frame** — evidence in the last section.

---

## Method, and what makes a claim here trustworthy

Two endpoints were wrong on the first attempt and both were caught by controls, so the controls are
reported alongside the results.

- **`.com`** — `https://rdap.verisign.com/com/v1/domain/<NAME>.COM`.
  Control: `GOOGLE.COM` → **200**. 404 = unregistered.
- **`.org`** — `https://rdap.publicinterestregistry.org/rdap/domain/<name>.org`.
  Control: `wikipedia.org` → **200**.
- **`.dev` / `.app`** — `https://pubapi.registry.google/rdap/domain/<name>.<tld>`.
  Controls: `web.dev` → **200**, `cash.app` → **200**.
  **The obvious endpoint is wrong.** `https://www.registry.google/rdap/domain/web.dev` returns a
  **404 HTML error page** for a domain that is certainly registered — it would have reported every
  slug as free. `rdap.org` 302s to `pubapi.registry.google`, which is the real host. Google's RDAP
  also rate-limits to 429 after roughly ten requests, so those runs were throttled with `sleep 8`
  and the control was re-run at the end of each batch.
- **`rdap.org`** was abandoned after 11 requests — it returned **429** for everything after that,
  which is *unchecked*, not free. None of those 429s are reported as results.
- **GitHub** — `https://api.github.com/repos/skfd/<slug>` and `https://api.github.com/users/<slug>`
  (404 = free), plus `gh search repos <slug> --sort stars --limit 5`.
- **App Store** — `https://itunes.apple.com/search?term=<q>&entity=software&limit=15&country=us`,
  read as JSON for `trackName` / `primaryGenreName`. This is a fuzzy search, so a `resultCount` of
  13 means "13 loose matches", not a collision; what matters is whether any `trackName` *is* the
  name.
- **Google Play** — `curl` with a Chrome user agent against
  `https://play.google.com/store/search?q=<q>&c=apps&hl=en&gl=us`, checked for a consent
  interstitial before being believed. Every fetch returned a ~1 MB result blob with real app cards
  and **no** consent wall, so these are results rather than blocks.

One conflict was resolved rather than papered over: a web search surfaced `Balgol.com` as a live
site, but Verisign RDAP returns **404** and `nslookup balgol.com 8.8.8.8` returns **no A record**,
and `curl http://balgol.com/` returns **000** (no connection). The domain has lapsed and the search
index is stale. RDAP + DNS win.

---

## 1. Longissimus

**Register:** anatomical Latin. *Thesis + anatomy layer.*

**What it means.** Latin for "the longest one"
([Wikipedia](https://en.wikipedia.org/wiki/Longissimus)). It is the long back muscle, and it is the
muscle the seven traditions fight over: it forms the rib steak and, further back, the striploin
([buttonsoup.ca](https://buttonsoup.ca/know-your-steaks/),
[sousvideresources.com](https://sousvideresources.com/2019/05/14/sous-vide-not-all-new-yorks-are-created-equal-neither-are-rib-eyes-beef-longissmus-muscle/)).
It is also the default sample muscle of meat science —
[USDA on using it to predict carcass tenderness](https://www.ams.usda.gov/sites/default/files/media/Use_of_the_Longissimus_Muscle_to_Predict_Carcass_Tenderness%5B1%5D.pdf),
[a Hanwoo composition study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10001086/).

**Expert reading.** Bare "Longissimus" is normal usage — *musculus longissimus* is itself the Latin
head term, so nothing reads as missing. Modern veterinary nomenclature prefers *longissimus thoracis
et lumborum*; *longissimus dorsi* is the older form the meat trade kept. No homophone, no vulgarity,
no cross-language landmine.

**GitHub.** `https://api.github.com/repos/skfd/longissimus` → **404** (free).
`https://api.github.com/users/longissimus` → **404** (free).
`gh search repos longissimus --sort stars` → top hits are `CintiaAraujo-Zoo/EchoMetrics` (1 star,
ultrasound measurement of longissimus dorsi area) and a MATLAB IMF-estimation repo (1 star). **No
repo is named `longissimus`; nothing above 500 stars.**

**Domains.** `longissimus.com` → **200** (registered; live page title is *"longissimus.com is
parked"*). `longissimus.org` → **200** (registered). `longissimus.dev` → **404** (free).
`longissimus.app` → **404** (free).

**App Store.** `itunes.apple.com/search?term=longissimus&entity=software&limit=15&country=us` →
`resultCount 0`. Nothing at all.

**Google Play.** `play.google.com/store/search?q=longissimus&c=apps&hl=en&gl=us` → 200, ~1.24 MB,
30 app cards, no consent wall. The string "longissimus" appears **only in the echoed query** — not
in any title, description or package id. Results are generic posture/stretching apps. **Clear.**

**General collision.** Searches for `longissimus` and `longissimus beef` return the Wikipedia muscle
article, Physiopedia, TeachMeAnatomy, and a wall of meat-science papers
([PMC4092992](https://pmc.ncbi.nlm.nih.gov/articles/PMC4092992/),
[beefresearch.org](https://www.beefresearch.org/resources/product-quality/project-summaries/2001-2005/cataloging-beef-muscles)).
A supplementary search for `Longissimus restaurant OR butcher OR brand name` found **no business of
that name**. It is also a common Latin species epithet
([*Mecolaesthus longissimus*](https://en.wikipedia.org/wiki/Mecolaesthus_longissimus)).

**The obvious problem.** It names **one muscle out of 49**, so it promises a steak where the project
delivers a whole animal in seven partitions — and every search for it lands in anatomy literature
that has nothing to do with this page, which is a discoverability tax forever. Twelve letters, four
syllables, and the doubled `-ss-` is a spelling trap.

## 2. Cut Concordance

**Register:** dry reference work / the mechanism. Slug `cut-concordance` on GitHub,
`cutconcordance` for domains.

**GitHub.** `https://api.github.com/repos/skfd/cut-concordance` → **404** (free).
`https://api.github.com/repos/skfd/cutconcordance` → **404** (free).
`https://api.github.com/users/cutconcordance` → **404** (free).
`gh search repos cutconcordance` → **empty result**, no notable repos.

**Domains.** All four unregistered: `cutconcordance.com` → **404** (Verisign RDAP; `nslookup`
returns no A record), `.org` → **404**, `.dev` → **404**, `.app` → **404**. **The only *viable* candidate
with a clean sweep of all four TLDs *and* a free GitHub username** — `razrub` and `balgol` share the
sweep but are rejected on other grounds.

**App Store.** `term=cut+concordance` → `resultCount 2`, both Bible tools: *Strong's Concordance*
(Reference, Watchdis Group B.V) and *Bible and Strong's Concordance* (Book). Neither is this name.

**Google Play.** `q=cut%20concordance` → 200, ~1.24 MB, 30 cards, no consent wall. The phrase
appears only in the echoed query. **Clear.** Flagged as adjacent: the bare word "concordance" is
crowded with Bible-study apps, one titled exactly *"Concordance"*.

**General collision.** `cut concordance` returns a knot-theory paper on
[cut-diagrams](https://pith.science/paper/2603.26366), the
[`insongkim/concordance`](https://rdrr.io/github/insongkim/concordance/f/README.md) R package for
trade-code crosswalks, and Accuplacer cut-score tables. `cut concordance beef` returns only generic
cuts-of-beef pages — **no meat business uses it**.

**The obvious problem.** Not availability — it is that **"concordance" is already a word in this
exact literature, attached to the thing the project argues is wrong.** `shape.md` §1 spends its
longest section showing that Swatland's 2012 *concordance score* measures name survival rather than
geometry, and that a cut occupying 70% of the same anatomy under a different name scores zero.
Naming the atlas *Cut Concordance* invites precisely the confusion the writeup works to dispel. It
can be argued the other way — reclaiming the word and supplying the number it was missing — but
that is an argument you would have to make on the front page rather than a name that works
unattended. Secondarily: two words, and "concordance" drags Bible-index and medical-adherence
baggage.

## 3. Parcellation

**Register:** borrowed term of art / the mechanism.

**What it means.** Two live senses ([Wiktionary](https://en.wiktionary.org/wiki/parcellation)):
cadastral division of land into parcels, and the neuroimaging sense — "a map or annotation
associating spatial locations (e.g. voxels) with parcel identities". The second is a major term of
art: [*Nature Reviews Neuroscience*, "Imaging-based parcellations of the human
brain"](https://www.nature.com/articles/s41583-018-0071-7), and the paper `shape.md` builds §3 on,
[*The Brain Atlas Concordance Problem: Quantitative Comparison of Anatomical
Parcellations*](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2748707/). The field's own framing —
rival atlases parcelling one organ into regions that disagree — is a near-exact structural analogue
of what this repo does to a cow.

**GitHub.** `repos/skfd/parcellation` → **404** (free). `users/parcellation` → **404** (free).
`gh search repos parcellation` → top hits are `ieee820/BraTS2018-tumor-segmentation` (162 stars) and
`pykao/BraTS2018-tumor-segmentation` (112) — both match on the *description*, not the name. **No
repo is named `parcellation`; nothing above 500 stars.**

**Domains.** `parcellation.com` → **200** (registered; HTTP 200 with no `<title>`, i.e. blank or
parked). `parcellation.org` → **404** (free). `parcellation.dev` → **404** (free).
`parcellation.app` → **404** (free).

**App Store.** `term=parcellation` → `resultCount 13`, all parcel/land-mapping business apps
(*Land id®*, *Parceled Land Map*, *LandVision*, *Parcel Delivery 3D*). **None is named
Parcellation.**

**Google Play.** `q=parcellation` → 200, ~1.19 MB, 30 cards, no consent wall. Word appears only in
the echoed query; nearest are *Parcelles*, *Parcel Tracer*, *Parcele*. **Clear.**

**General collision.** `parcellation` returns Merriam-Webster, ScienceDirect, arXiv reviews and
[US patent 11694806](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11694806) on
grouping brain parcellation data — heavily owned by neuroimaging as a *field*, but by no single
product, company or film. `parcellation beef` returned **no meat product of this name**; the meat
space is empty.

**The obvious problem.** It is **neuroscience jargon**, so every search result is brain imaging and
a general reader cannot guess the meaning or the spelling. Worse, the land/logistics sense is live
in English and dominant in French planning usage, so a large share of readers will assume parcel
delivery. And it is a mass noun for a *process* — "Parcellation" names an activity, not a thing you
open in a browser.

## 4. Coextensive

**Register:** dry technical / the thesis, stated as a question. *Are these two cuts the same region?
No — 64% coextensive.*

**What it means.** "Equal or coincident in space, time, or scope"; having the same boundaries. From
Latin *co-* + *extendere*; [OED](https://www.oed.com/dictionary/coextensive_adj)'s earliest evidence
is 1771 in Burke ([Merriam-Webster](https://www.merriam-webster.com/dictionary/coextensive)). Used
chiefly in **legal and administrative-geography prose** — the stock examples are jurisdictional
("Todd County is coextensive with the Rosebud Sioux Reservation").

**GitHub.** `repos/skfd/coextensive` → **404** (free). `users/coextensive` → **404** (free).
`gh search repos coextensive` → **empty result**, no notable repos.

**Domains.** `coextensive.com` → **200** (registered; live title is *"coextensive.com — Moz DA 3
aged domain | ED.com"*, i.e. a domain reseller, not a real site). `.org` → **404** (free).
`.dev` → **404** (free). `.app` → **404** (free).

**App Store.** `term=coextensive` → `resultCount 0`. Nothing.

**Google Play.** `q=coextensive` → 200, ~1.21 MB, 30 cards, no consent wall. Word appears only in
the echoed query; nearest is *Coexistence*, a different word. **Clear.**

**General collision.** `coextensive` returns dictionary entries plus
[category-theory/universal-algebra papers on arXiv](https://arxiv.org/pdf/2104.12188). `coextensive
beef` returns dictionary entries and nothing else. **No product or organisation owns it.**

**The obvious problem.** It is an **adjective, and a relational one** — "coextensive" begs "with
what?", so it reads as a dangling fragment on a masthead. Five syllables of dictionary word in a
contract-drafting register, with no animal hook at all; a general reader will half-recognise it and
be unable to define it.

## 5. Coregister

**Register:** imaging mechanism. Literally what the repo does — two datasets brought into one
coordinate frame.

**GitHub.** `repos/skfd/coregister` → **404** (free). `users/coregister` → **404** (free).
`gh search repos coregister` → `almostdutch/Image-coregistration-translation-rotation` (9 stars),
`adolliou/euispice_coreg` (3). **No repo named `coregister`.** A supplementary search found no npm
or PyPI package of that name either, only substring repos
([AllenInstitute/em_coregistration](https://github.com/AllenInstitute/em_coregistration)).

**Domains.** `coregister.com` → **200** (registered; live title *"Registered & Protected by
Markmonitor"* — a corporate brand-protection holding, which means a company is actively defending
the string). `.org` → **404** (free). `.dev` → **404** (free). `.app` → **404** (free).

**App Store.** `term=coregister` → `resultCount 14`, all registration/sign-up utilities (*Namecheap*,
*Life Registration*, *Signup Kiosk*). **None is named Coregister.**

**Google Play.** `q=coregister` → 200, ~1.03 MB, 9 cards (thin but genuine, no consent wall). Word
appears only in the echoed query. **Clear.**

**General collision.** A standard verb in medical imaging and remote sensing, with
[US patent 5672877](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5672877) on
coregistration of multi-modality medical data and SPM/FSL tooling built around it
([Andy's Brain Book](https://andysbrainbook.readthedocs.io/en/latest/SPM/SPM_Short_Course/SPM_04_Preprocessing/03_SPM_Coregistration.html)).
No meat or food use at all. Worth noting the adjacent noise: **BeEF** is a well-known
browser-exploitation framework and `Beef.Core` a NuGet package, so `coregister beef` searches are
already polluted.

**The obvious problem.** It is a **verb naming a preprocessing step**, not a reference work — it
describes the boring part (aligning the data) rather than the interesting part (what the alignment
reveals). And it is indistinguishable from the noise of SPM/MRI/satellite tutorials. The MarkMonitor
lock on the `.com` also signals a corporate owner somewhere who cares about the string.

## 6. Aitchbone

**Register:** English butchery vocabulary, obscure and dry.

**GitHub.** `repos/skfd/aitchbone` → **404** (free). `https://api.github.com/users/aitchbone` →
**200** — **the username is taken.** `gh search repos aitchbone` → `j-yoshino/AitchboneAndTongue`
(0 stars, a game-jam entry). Nothing notable.

**Domains.** `aitchbone.com` → **200** (registered; the page is a *"Buy A Domain | Register Your
Domain Name"* reseller placeholder). `.org` → **404** (free). `.dev` → **404** (free). `.app` →
**404** (free).

**App Store.** `term=aitchbone` → `resultCount 0`. Nothing.

**Google Play.** `q=aitchbone` → 200, ~1.21 MB, 30 cards, no consent wall. Word appears only in the
echoed query; results are phonetic scatter (*AICHE*, *Barebone*, *Hattie B's*). **Clear.**

**General collision.** No famous unrelated owner — but the meat space is **actively occupied**. It
is a dictionary-listed common noun
([Merriam-Webster](https://www.merriam-webster.com/dictionary/aitchbone)) and a live retail product
at multiple named UK butchers:
[Calnan Brothers](https://calnanbrothers.co.uk/product/aitch-bone/),
[Grasmere Farm's 21-day dry-aged aitchbone joint](https://www.grasmere-farm.co.uk/shop/beef/21-day-dry-aged-aitchbone-joint-from-native-breed-beef/),
[Upper Unstead Farm](https://www.upperunsteadfarm.co.uk/products/aitch-bone-roast/),
plus recipes ([ckbk](https://app.ckbk.com/recipe/poor37139c06s001r001/aitchbone-of-beef)).

**The obvious problem.** **It is a cut of beef currently on sale**, so the name reads as a product
listing rather than a reference work, and it is permanently unsearchable — every result is a butcher
selling a joint. The spelling is also unguessable from the sound (`aitch` for the letter H), and the
GitHub username is already gone, which forecloses ever making it an org.

## 7. Razrub (разруб) — Reject

**Register:** Russian butchery vocabulary.

**What it means.** Masculine noun, two senses
([kartaslov](https://kartaslov.ru/значение-слова/разруб)): the *action* of cleaving apart, and the
*place or line along which* something was cut through. Morphology: prefix **раз-** ("asunder") +
root **-руб-**, from *рубить*, "to chop". `Разруб` is the nominative citation form; *схема
разрубА* is that noun in the genitive, so "Razrub" is grammatically correct rather than truncated,
and `razrub` is the standard transliteration.

**Confirmed as the charting term.** [meatinfo.ru's *Схема разруба
говядины*](https://meatinfo.ru/info/show?id=361),
[its cut-scheme category](https://meatinfo.ru/cutschemes/grp?cod=2340), and
[krascasing.ru's illustrated guide](https://www.krascasing.ru/blogs/tehnologii-i-instruktsii/razrub).
Register note: the everyday word is **разделка** (ru.wikipedia's article is *Разделка говяжьей
туши*); **разруб** is the narrower GOST/trade term — an asset for a technical atlas.

**Native-speaker reading.** Neutral technical, faintly blunt, **not brutal** — *рубить* is the
ordinary verb for chopping firewood, and in a butchery context a Russian reads GOST paperwork rather
than violence. Sense (2), "the line where something was cleft", actually flatters the product. In
Latin script an English eye catches "rub", accidentally food-adjacent and harmless.

**Availability is excellent.** `repos/skfd/razrub` → **404** (free). `users/razrub` → **404** (free).
`gh search repos razrub` → only `razrubat/razrubat` (0 stars) and `aerodame/RazRuBee` (0). All four
domains unregistered: `.com` **404** (confirmed by `nslookup` — no A record), `.org` **404**, `.dev`
**404**, `.app` **404**. App Store `term=razrub` → 14 fuzzy Arabic-language results, none named this.
Google Play `q=razrub` → 200, ~1.38 MB, **50** cards, no consent wall, word only in the echoed query.
**Clear everywhere.**

**The obvious problem.** Availability is not the issue — **the thesis is**. A project whose entire
argument is that no tradition is the reference frame cannot be named in one tradition's language
without making that tradition the metalanguage. Secondarily it is unreadable and unpronounceable to
non-Russian speakers, in Russian it is simply the common noun for "cut" rather than a name, and it
names the *operation* rather than the *map*.

## 8. Balgol (발골) — Reject

**Register:** Korean butchery vocabulary.

**What it means.** Hanja **拔骨** — 拔 "pull out" + 骨 "bone": 「식육 동물을 도살하여 뼈와 고기를
분리하는 일」, separating bone from flesh. Confirmed on the National Institute of Korean Language's
[우리말샘](https://opendict.korean.go.kr/search/searchResult?query=발골), field-labelled 농업, with
derived industry terms 발골햄, 기계발골육. Notably it returns **0 results** in the standard
dictionary [표준국어대사전](https://stdict.korean.go.kr/search/searchResult.do?searchKeyword=발골),
confirming it is genuine trade vocabulary rather than general lexicon. `balgol` is the correct
Revised Romanization.

**Native-speaker reading.** Neutral trade jargon, slightly gory-literal — a Korean reads
"extract-bone", live occupational vocabulary paired with 정형 (trimming) in
[trade press](https://www.chuksannews.co.kr/news/article.html?no=88832) and
[national reporting on 발골·정형사 labour shortages](https://www.nongmin.com/article/20260506500638).
No vulgar homophone was found.

**Availability is excellent.** `repos/skfd/balgol` → **404** (free). `users/balgol` → **404** (free).
All four domains unregistered: `.com` **404**, `.org` **404**, `.dev` **404**, `.app` **404** — and
the apparent counter-evidence was chased down: a search hit listed `Balgol.com` as live, but
`nslookup balgol.com 8.8.8.8` returns **no A record** and `curl http://balgol.com/` returns **000**.
The domain has lapsed; the index is stale. App Store `term=balgol` → 3 results, all Arabic *Baloot*
card games. Google Play `q=balgol` → 200, **1 card** ("Any Golf Score"), no consent wall — the
cleanest string of all 14.

**The obvious problem.** **BALGOL is a real programming language** — the Burroughs 220 dialect of
ALGOL-58 ([The Free Dictionary](https://encyclopedia2.thefreedictionary.com/BALGOL),
[ALGOL 58](https://en.wikipedia.org/wiki/ALGOL_58),
[a HathiTrust-catalogued BALGOL program](https://catalog.hathitrust.org/Record/100921811)). A
*software project* named BALGOL will be read as a compiler or language, which is the single worst
misreading available for a repo. On top of that it carries the same one-tradition-as-metalanguage
problem as Razrub, and 발골 names deboning specifically — a bloody manual operation — where the atlas
charts lines.

## 9. Edaniku (枝肉) — Reject

**Register:** Japanese butchery vocabulary.

**What it means.** 枝 "branch" + 肉 "meat"; reading えだにく, Hepburn `edaniku` (no macron, nothing to
get wrong). [Daijisen via kotobank](https://kotobank.jp/word/%E6%9E%9D%E8%82%89-36669):
「家畜の、頭部・内臓や四肢の先端を取り除いた部分の骨付きの肉」 — bone-in meat with head, viscera and
limb extremities removed. It is the standard trade word for a dressed carcass, tied directly to the
grading system ([meatbook.jp](https://meatbook.jp/edaniku/),
[zookan glossary](https://zookan.lin.gr.jp/kototen/nikuusi/n423.htm)). Register is wholesale/grading
jargon; Japanese consumers meet ロース/モモ/バラ instead. *(The commonly repeated "branch-shaped"
etymology could not be confirmed on any page actually fetched — recorded as **unchecked**.)*

**Native-speaker reading.** Neutral, mildly insider — the meat equivalent of "carcase weight". No
vulgarity, no pun. "Eda" is also a common Japanese surname element, so "Edaniku" can momentarily
read as a person's name (inference, unchecked).

**Availability.** `repos/skfd/edaniku` → **404** (free). `users/edaniku` → **404** (free).
`gh search repos edaniku` → **empty**. `.org` / `.dev` / `.app` all **404** (free). App Store
`term=edaniku` → 13 fuzzy Japanese results, none named this. Google Play `q=edaniku` → 200,
~1.23 MB, 30 cards, no consent wall, word only in the echoed query. **Clear.**

**The obvious problem.** **`edaniku.com` → 200, and the site is 舞台『エダニク』** — the official page
for Takuya Yokoyama's award-winning play *Edaniku*, set in a meat-processing plant
([Japan Foundation Performing Arts Network](https://performingarts.jpf.go.jp/E/play/1212/1.html),
[iaku](https://www.iaku.jp/backnumber/edaniku), [edaniku.com](https://edaniku.com/introduction.html)).
A well-known cultural work **on exactly this subject** already owns the name and the domain, which
is the same failure mode as `Beef Atlas` — quieter, but the same. Plus the one-tradition-as-
metalanguage objection, and the fact that it is a generic industry noun in the one country it comes
from.

## 10. Chine — Reject

**Register:** English butchery vocabulary. Included deliberately as the predictable reject, and it
failed for a reason worse than expected.

**What it means.** Butcher's glossary: chine bone = "The backbone or spinal column"; chining =
cutting through or removing the backbone so a rack can be portioned
([butchershandbook.com](https://butchershandbook.com/guides/butchering-terms-glossary/),
[Wiktionary](https://en.wiktionary.org/wiki/chine)). Pronounced /tʃaɪn/. English alone gives it
**four** live etymologies: backbone, a steep coastal ravine (Isle of Wight), an obsolete verb "to
crack", and a nautical sense — the sharp angle in a hull's cross-section, which boat people use
daily.

**The disqualifier.** **"Chine" is the French proper noun for China**
([Wiktionary](https://en.wiktionary.org/wiki/chine)), feminine, as in *encre de Chine*, *République
populaire de Chine*. **France is one of the seven traditions.** A French visitor lands on a beef
atlas whose name, capitalised as a product name, is the word "China" — a country that is not among
the seven. That reads as an error on the homepage, not as a clever pun. The name is not even stable
when spoken: EN /tʃaɪn/ "chyne" versus FR /ʃin/ "sheen".

**Availability (for completeness).** `repos/skfd/chine` → **404** (free), but
`https://api.github.com/users/chine` → **200**, **taken**. `chine.com` → **200** (registered),
`chine.org` → **200** (registered); `.dev` and `.app` → **404** (free). `gh search repos chine` →
the large hits (`1c7/chinese-independent-developer`, 61,418 stars;
`chinese-poetry/chinese-poetry`, 53,420) are **substring matches on "chinese"**, not the slug. App
Store `term=chine` → 13 results, all *Chime*/Chinese-learning fuzzy matches. Google Play `q=chine` →
200, ~1.08 MB, 13 cards, no consent wall: seven titles contain the substring, all via
"Chinese" (*HelloChinese*, *SuperChinese*, *Chineasy*, *Du Chinese*…), and the one package id
containing the bare word is `com.radiolight.chine`, titled *Radio China FM Online* — the French
sense, in the wild, on a storefront.

**Also.** Even setting France aside, butchers use it for **one specific operation on one bone**, so
it claims a narrow existing term for a whole-cow atlas.

---

## Also checked, and cut before the table

**Concordance (bare).** Rejected on availability, exactly as predicted. **All four TLDs registered**:
`.com` **200**, `.org` **200**, `.dev` **200**, `.app` **200**. `users/concordance` → **200**
(taken). Two established repos are literally named `concordance`:
[`concordancejs/concordance`](https://github.com/concordancejs/concordance) (211 stars, JS value
diffing) and [`jaymzh/concordance`](https://github.com/jaymzh/concordance) (206 stars, Harmony remote
control). Google Play carries an app titled exactly *"Concordance"* plus a stack of Strong's
Concordance Bible tools. `repos/skfd/concordance` is free, but that is the only thing that is.

**Seven Knives.** `.com`/`.org`/`.dev`/`.app` **all 404** (free) and `repos/skfd/sevenknives` free —
but `users/sevenknives` → **200** (taken; `sevenKnives/sevenKnives.github.io` exists). Worse, the
name is **taken by a recording artist** with a
[Discogs page](https://www.discogs.com/artist/6244680-Seven-Knives),
[Bandcamp](https://sevenknivesmusic.bandcamp.com/) and an
[official Facebook](https://www.facebook.com/SevenKnivesOfficial/), plus a separate album of that
title by Nechkin. And the adjacent collision is bad: **[Seven Beef](http://www.sevenbeef.com/knife-club/)**
is a real Seattle whole-animal steak restaurant with a members' *Knife Club* — close enough in
subject that the name looks derivative. Google Play is clear but sits one letter from the
*Seven Knights* game franchise. Separately, "seven" **locks a count the README explicitly invites
readers to extend** (`## Adding a tradition`), so the name expires the first time an eighth
tradition lands.

**Same Animal.** `sameanimal.com` → **200** (registered; resolves to an expired Squarespace site).
`.org`/`.dev`/`.app` free, GitHub repo and username free, Play clear. But **an existing recording
artist holds the exact name** across
[Apple Music](https://music.apple.com/us/artist/same-animal/1184840024),
[Spotify](https://open.spotify.com/artist/7bwzIMpVGU2HLyQ9OJiJb9) and
[SoundCloud](https://soundcloud.com/sameanimal). Two common words, unsearchable, and it says nothing
about butchery.

**Shared Frame.** `sharedframe.com` → **200** (registered; does not respond over HTTP).
`.org`/`.dev`/`.app` free, GitHub free. But the handles are held by a music project
([Bandcamp](https://sharedframe.bandcamp.com/), [X](https://twitter.com/sharedframe)), and the
killer is domain-semantic: **in cattle, "frame" already means frame score**
([MSU](https://www.canr.msu.edu/news/do-beef-cattle-frame-scores-need-updating)) **and "share"
already means a bulk beef share** ([Fox Hollow](https://foxhollow.com/blogs/blog/3-benefits-of-a-beef-share)),
so the name reads as a cattle-sizing tool or a meat-buying club. Google Play is clear but sits in a
dense photo-frame neighbourhood (*Frameo*, *PhotoShare Frame*, *Sharelife Frame*).

---

## What was not checked

- **Trademark registers** (USPTO, EUIPO, WIPO) were not searched. Everything above is domain,
  repository and storefront availability plus general web collision — it is not a clearance opinion.
- **Storefront checks are US-only** (`country=us`, `gl=us&hl=en`) and first page only. A Japanese or
  Korean storefront could hold something these queries never saw — relevant for `Edaniku` and
  `Balgol` in particular.
- **`rdap.org` 429 responses were discarded, not interpreted.** Every domain verdict here rests on a
  registry endpoint whose control domain returned 200 in the same batch.
- Three linguistic readings are flagged inference rather than sourced fact, and are marked as such
  in their sections: the 枝 "branch-shaped" etymology, the Russian violence connotation, and the
  Korean 발+골 "foot-goal" double-take.
