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

---

# Round 2: subject-in-the-name candidates

Round 1's shortlist was register-first — Latin, neuroimaging, borrowed trade words. The owner has
since steered the opposite way: **the name must carry the subject** (beef / cow / meat / butchery,
so a cold reader knows what it is about) and the register must be **plain everyday words**,
specifically the *phrasebook / vocabulary / translation between cultures* idea — because the project
is a **translation between butchery traditions** rather than a map. The seed phrases were
*"Cross-culture Beef Cuts"* and *"Cow Meat Vocabulary"*. Academic and jargon words are out, which
retires Round 1's top three rather than competing with them.

Fifteen candidates, every availability claim traced to a fetch made on **2026-09-14**. Round 1's
candidates were not re-checked.

## The top three, given the steer

**1. Beef Phrasebook.** The steer, executed literally. Subject in the first word, register in the
second, and "phrasebook" is the only word in the list that already means *the thing this project
does* — you hold it up at a counter in a country whose words you do not have. **Every check came
back free**: all four TLDs unregistered, `skfd/beef-phrasebook` and `skfd/beefphrasebook` free, the
bare GitHub username free, nothing on either storefront, and no book, band, restaurant or product of
that name surfaced in nine searches. Its problem is stated below and it is real but survivable.

**2. Beef Vocabulary.** The closest thing on the list to the owner's own seed, *"Cow Meat
Vocabulary"* — same two ideas, one word shorter. Also a clean sweep: four TLDs free, GitHub free,
storefronts clear, and the only exact-title page anywhere is a classroom worksheet PDF. It is
flatter than *Phrasebook* — a vocabulary is a list, a phrasebook is a thing you carry — but it is
the safest plain-words option.

**3. Same Cow.** The plainest words available and the thesis in two syllables: *one animal, seven
ways, the same cow every time*. It keeps the subject, it is impossible to misspell, and the README's
own first line is already an argument for it. It is third rather than first because `samecow.com` is
registered (dead, but held), because it is a fragment rather than a name, and because it abandons
the phrasebook register the owner asked for.

Runners-up worth keeping: **Butcher's Phrasebook** — perfect register, entirely free, but
`butchershandbook.com` is a live site doing this exact concept under a name one word away, and it
says *butcher* where the project says *beef*. And **Beef Glossary** — free everywhere, but it is a
page heading rather than a product name (see below).

## A structural finding, as in round 1

**Eleven of the fifteen swept all four TLDs *and* both GitHub slots.** That is not luck and it is not
a sign these names are better than round 1's — it is that **multi-word compounds are cheap and
single dictionary words are not**. Round 1 fought `parcellation.com`, `chine.org` and `coregister.com`
because it was proposing single words that somebody had already bought. Every compound here
(`beefphrasebook`, `cutsintranslation`, `meatvocabulary`) is unregistered for the same reason nobody
registered it: it is long. **Availability has stopped being the discriminator in round 2.** What
separates these candidates is entirely the second axis:

**Does the name survive being searched for?** Three failure modes showed up, and each one killed a
different family:

- **Dictionary capture.** *Beef in Translation*, *Beef Translated* and *Cuts in Translation* all lose
  their own results page to Collins, Cambridge, WordReference and Linguee. A name that literally
  describes a dictionary lookup competes with actual dictionaries and loses.
- **Page-heading capture.** *Beef Glossary* and *Meat Vocabulary* are not owned by anyone — they are
  used as a *heading* by roughly eleven and seven distinct organisations respectively. A name that is
  already a common page title is unsearchable even though it is unclaimed.
- **Subject-word capture.** *Cut Phrasebook*, *Cut Vocabulary*, *Cuts in Translation*, *One Beast*,
  *Same Beast* and *Cross-Cut* carry no beef/cow/meat/butchery word at all, which **fails the owner's
  first constraint outright** regardless of how clean they check out. They are reported in full but
  cannot be recommended.

The one candidate where availability still decided it is **Cross-Cut** — the only name in round 2
with **all four TLDs registered**, and the pun is taken several times over. (It is not unique across
both rounds: bare **Concordance** matched it, `.com`/`.org`/`.dev`/`.app` all 200, and was cut before
round 1's table for exactly that reason. Cross-Cut is the only such name to reach a table.)

## The table

`.com` / `.org` / `.dev` / `.app` — **F** = unregistered (RDAP 404), **T** = registered (RDAP 200).
GitHub column is `skfd/<slug>` repo / bare `github.com/<slug>` user-or-org. **Subj** = does the name
carry beef / cow / meat / butchery, the owner's first constraint.

| # | Name | Subj | .com | .org | .dev | .app | GitHub repo / user | App Store | Play | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Beef Phrasebook** | **yes** | **F** | **F** | **F** | **F** | **free** / **free** | clear | clear | **Strong** — clean sweep, register exactly as steered |
| 2 | **Beef Vocabulary** | **yes** | **F** | **F** | **F** | **F** | **free** / **free** | clear | clear | **Strong** — clean sweep, closest to the owner's own seed |
| 3 | **Same Cow** | **yes** | T | **F** | **F** | **F** | **free** / **free** | clear | clear | **Strong** — plainest words, thesis exactly; `.com` held and dead |
| 4 | **Butcher's Phrasebook** | **yes** | **F** | **F** | **F** | **F** | **free** / **free** | clear | clear | **Viable** — `butchershandbook.com` is one word away, in this niche |
| 5 | **Meat Phrasebook** | **yes** | **F** | **F** | **F** | **F** | **free** / **free** | clear | clear | **Viable** — clean, but promises pork and lamb too |
| 6 | **Beef Glossary** | **yes** | **F** | **F** | **F** | **F** | **free** / **free** | clear | clear | **Marginal** — ~11 orgs use it as a page heading |
| 7 | **Beef in Translation** | **yes** | **F** | **F** | **F** | **F** | **free** / **free** | clear | clear | **Marginal** — its own SERP belongs to dictionaries |
| 8 | **Beef Translated** | **yes** | **F** | **F** | **F** | **F** | **free** / **free** | clear | clear | **Marginal** — two live blog posts are near-identical headlines |
| 9 | **Cuts in Translation** | no | **F** | **F** | **F** | **F** | **free** / **free** | clear | clear | **Viable-but-off-steer** — no subject word |
| 10 | **Cut Phrasebook** | no | **F** | **F** | **F** | **F** | **free** / **free** | clear | clear | **Weak** — parses as *phrases to cut out* |
| 11 | **Cut Vocabulary** | no | **F** | **F** | **F** | **F** | **free** / **free** | clear | clear | **Weak** — drowned by the dictionary entry for "cut" |
| 12 | **Meat Vocabulary** | **yes** | **F** | **F** | **F** | **F** | **free** / **free** | clear | clear | **Reject** — an ESL category label used by 7+ orgs |
| 13 | **One Beast** | no | T | **F** | **F** | **F** | **free** / *taken* | clear | clear | **Reject** — "whole beast" already means whole-animal butchery |
| 14 | **Same Beast** | no | T | **F** | **F** | **F** | **free** / *taken* | clear | clear | **Reject** — `.com` is a live site; an EP and a Kobe Bryant idiom |
| 15 | **Cross-Cut** | no | T | T | T | T | **free** / *taken* | clear | **app titled `CrossCut`** | **Reject** — the only all-four-registered name in round 2 |

---

## Method, and the two traps round 1 warned about

Both traps were avoided by using round 1's corrected endpoints, and both controls are reported
alongside the results rather than assumed.

- **`.com`** — `https://rdap.verisign.com/com/v1/domain/<NAME>.COM`.
  Control `GOOGLE.COM` → **200**, run at the start *and* end of the batch. 404 = unregistered.
- **`.org`** — `https://rdap.publicinterestregistry.org/rdap/domain/<name>.org`.
  Control `wikipedia.org` → **200**, start and end.
- **`.dev` / `.app`** — `https://pubapi.registry.google/rdap/domain/<name>.<tld>`, **not**
  `www.registry.google`, which round 1 found returns an HTML 404 even for registered domains.
  Controls `web.dev` → **200** and `cash.app` → **200**, re-run before **every** batch of seven and
  again at the end — four control pairs per run, **eight** across the two runs, all 200. Requests were throttled at
  `sleep 8`. **No 429 was seen in either run**, so no result here is a rate-limit artefact.
  `rdap.org` was not used at all.
- **GitHub** — `gh api repos/skfd/<slug>` and `gh api users/<slug>` under an authenticated token
  (5,000/hr, so no throttling), 404 = free. Controls: `repos/skfd/beef-atlas` → **200** and
  `users/skfd` → **200**, confirming the 404s are real absences rather than a broken call. Both slug
  forms were checked for every multi-word name — hyphenated (`beef-phrasebook`) and flat
  (`beefphrasebook`) — for repos *and* for usernames, 60 checks. Plus `gh search repos "<name>"`.
- **App Store** — `https://itunes.apple.com/search?term=<q>&entity=software&limit=15&country=us`,
  read as JSON. As in round 1 this is a fuzzy search: a `resultCount` of 15 means fifteen loose
  matches, not a collision. Only an exact `trackName` counts.
- **Google Play** — `curl` with a Chrome UA against
  `https://play.google.com/store/search?q=<q>&c=apps&hl=en&gl=us`. Every fetch returned
  **HTTP 200, ~1.2 MB, 29–50 real app cards, and no consent interstitial**, so these are results and
  not blocks. **Improvement on round 1's method:** rather than grepping the whole blob for the phrase
  — which matches the *echoed query* in `og:title`, `twitter:title`, `<title>` and two `ds:`
  request payloads, six times per page — app card titles were extracted from the `DdYX5` span class
  and compared normalized. That is what caught `CrossCut` and confirmed the other fourteen.
- **Live-page check on every registered domain.** RDAP says *registered*; it does not say *used*.
  Each `T` was fetched and its final URL and `<title>` recorded, and `nslookup … 8.8.8.8` run
  alongside. This resolved two things RDAP alone would have got wrong — see `crosscut.dev` below.

**One conflict resolved rather than papered over:** `crosscut.dev` returns RDAP **200**
(registered) but `nslookup crosscut.dev 8.8.8.8` returns **`Non-existent domain`** and HTTPS returns
**000**. The domain is registered at the registry and never delegated. It is reported as **T**
(registered, and therefore not available to take) — RDAP is the authority on availability, DNS only
on use.

**Not checked, same as round 1:** no trademark registers (USPTO, EUIPO, WIPO) — nothing here is a
clearance opinion; storefront checks are **US-only** (`country=us`, `gl=us&hl=en`) and first page
only; social handles were not checked. New this round: the collision searches were run through a
backend that **did not honour exact-phrase quoting** — it returned `beef AND phrasebook` rather than
`"beef phrasebook"`. A negative is therefore weaker than a quoted negative: it means *no exact-title
owner surfaced*, not *none exists*. Every candidate below states which queries were actually run.

---

## 1. Beef Phrasebook

**Register:** plain words, subject first. Slug `beef-phrasebook` / `beefphrasebook`.

**Domains.** All four unregistered: `beefphrasebook.com` → **404** (Verisign), `.org` → **404**
(PIR), `.dev` → **404**, `.app` → **404** (both Google RDAP, controls 200).

**GitHub.** `repos/skfd/beef-phrasebook` → **404** (free). `repos/skfd/beefphrasebook` → **404**
(free). `users/beef-phrasebook` → **404** (free). `users/beefphrasebook` → **404** (free).
`gh search repos "beef phrasebook"` → **empty result**.

**App Store.** `term=beef+phrasebook` → `resultCount 15`, a fuzzy split between beef businesses
(*Western Beef*, *Roast Perfect* by Certified Angus Beef, *Omaha Steaks*, *CattleFax*) and
language apps (*Learn Italian – Phrasebook*, *SpeakEasy Italian Phrasebook*). **No `trackName` is
this name.**

**Google Play.** 200, 1.30 MB, **50** app cards, no consent wall. All six occurrences of the string
were verified as the echoed query (`og:title`, `twitter:title`, `<title id="main-title">`, two `ds:`
request payloads, one `data-p` attribute). **No card title contains it.** Nearest cards are
*Beef R Us*, *You Want Beef?*, *French phrasebook*, *Beef Bae*. **Clear.**

**General collision.** No exact-title book, film, band, shop or app surfaced across nine queries,
including three restricted to amazon.com / goodreads.com / books.google.com. Nearest published works
are [*Beef: Webster's Quotations, Facts and Phrases*](https://www.amazon.com/Beef-Websters-Quotations-Facts-Phrases/dp/B001Q91Z58)
(an auto-generated Icon Group corpus, conceptually adjacent, not a competitor) and
[*The Beef Book*](https://www.amazon.com/Beef-Book-Fundamentals-Trade-Ranch/dp/0990995909).
The food-phrasebook slot is genuinely empty: **no result found** for `"steak phrasebook"`,
`"chef's phrasebook"`, `"cook's phrasebook"` or `"kitchen phrasebook"` either. Cooking reference
books use *Companion* ([Food Lover's Companion](https://en.wikipedia.org/wiki/Food_Lover's_Companion)),
*Guide* or *Glossary* instead — which is either the gap this name fills or a hint that the metaphor
has been tried and does not sell.

**The obvious problem.** Two, and they are the same problem twice. **"Beef" means a feud**, and
pairing it with "phrasebook" actively invites that reading — *a phrasebook of beefs* is a funnier
book than the one this is. And the query is **pre-owned by language learning**: searching it returns
Memrise's "How to say beef in Korean", "How to say beef in Chinese" and
[Phrase Finder's beef idioms](https://www.phrases.org.uk/phrase-thesaurus/beef), so the project
competes with Memrise for its own brand name on day one. Secondarily, "phrasebook" is a commoditised
app category — [Lonely Planet is the world's largest phrasebook publisher](https://www.goodreads.com/series/357934-lonely-planet-phrasebooks)
and there are several generic *Phrasebook* apps on both stores — so the word buys recognition but no
distinctiveness.

## 2. Beef Vocabulary

**Register:** plain words; the owner's own seed, shortened. Slug `beef-vocabulary` / `beefvocabulary`.

**Domains.** All four unregistered: `.com` **404**, `.org` **404**, `.dev` **404**, `.app` **404**.

**GitHub.** `repos/skfd/beef-vocabulary` → **404**. `repos/skfd/beefvocabulary` → **404**.
`users/beef-vocabulary` → **404**. `users/beefvocabulary` → **404**. All free.
`gh search repos "beef vocabulary"` → **empty result**.

**App Store.** `term=beef+vocabulary` → `resultCount 15`, a fuzzy split between vocabulary trainers
(*Vocabulary.com*, *WordUp*, *Exam Vocabulary Builder*) and beef businesses (*Beef News and Markets*,
*Performance Beef*, *All About Beef* by the American Farm Bureau Foundation). **None is named this.**

**Google Play.** 200, 1.25 MB, 30 cards, no consent wall, **no card title contains the phrase.**
**Clear.**

**General collision.** The only exact-title page found in four queries is a classroom worksheet:
[*Beef Vocabulary* (PDF), Ag in the Classroom](https://www.agintheclassroom.org/media/5qziiomm/beef-vocabulary.pdf).
No book, band, restaurant, app or product. Unusually for this family, the **meat industry does not
use this wording** — it says *glossary* and *terms*, not *vocabulary* — so the phrase is not a
crowded page heading the way *Beef Glossary* is.

**The obvious problem.** It **leaks into the ESL cluster it does not own**. Every "meat vocabulary"
teaching page ([Cambridge's *Cuts of meat* topic list](https://dictionary.cambridge.org/us/topics/food/cuts-of-meat/),
[Woodward English](https://www.woodwardenglish.com/lesson/meat-english-vocabulary/),
[EnglishClub](https://www.englishclub.com/vocabulary/food-meats.php)) has a beef section, so the
name inherits language-learning noise without being a language-learning product. And the word is
**flatter than the idea**: a vocabulary is a list of words, which undersells a page whose whole point
is that the words are drawn on the same animal in one coordinate frame. *Phrasebook* implies you
carry it somewhere; *vocabulary* implies you memorise it.

## 3. Same Cow

**Register:** plainest possible; the thesis as a two-word sentence fragment.

**Domains.** `samecow.com` → **200** (registered) — but `nslookup samecow.com 8.8.8.8` returns the
name with **no A record** and HTTPS returns **000**: held and dead, not in use. `.org` → **404**
(free), `.dev` → **404** (free), `.app` → **404** (free).

**GitHub.** `repos/skfd/same-cow` → **404**. `repos/skfd/samecow` → **404**. `users/same-cow` →
**404**. `users/samecow` → **404**. All free — **and unlike its two "beast" siblings, the bare
username is available.** `gh search repos "same cow"` → **empty result**.

**App Store.** `term=same+cow` → `resultCount 12`, all cow games and milking toys (*Tiny Cow*,
*Milk The Cow*, *Cow Evolution*, *Cow Launcher*). **None is named this.**

**Google Play.** 200, 1.21 MB, 30 cards, no consent wall, **no card title contains the phrase.**
**Clear.**

**General collision.** No band, book, film, restaurant, shop, podcast or software product of this
name found across three queries. The nearest thing to an owner is a **slogan, not a name**: the
Vermont nonprofit [World Cow](https://www.worldcow.earth/) uses "We're all spots on the same cow" as
its tagline, and it is the top semantic hit for the exact phrase. Also live but harmless: a
Spanish-language *La Vaca* [TikTok trend page](https://www.tiktok.com/discover/te-cow-the-cow-the-same-cow).
Butcher-shop queries returned only unrelated businesses (*Cow Palace Butcher Shop*, *The Cowshed*).

**The obvious problem.** It is a **fragment, not a name** — "same cow" begs "same as what?", which is
the same objection that sank *Coextensive* in round 1, in plainer clothes. It carries the subject but
not the *activity*: nothing in it says butchery, comparison, or reference, so a cold reader knows it
is about a cow and nothing more. It is also **unsearchable as two of the commonest words in
English**, `.com` is held by someone who is not using it, and — the quiet one — the World Cow slogan
means the first person to say the phrase out loud in a pitch may get "like the nonprofit?" back.

## 4. Butcher's Phrasebook

**Register:** the steer, in the trade's own voice. Slugs `butchers-phrasebook` / `butchersphrasebook`
(apostrophe dropped).

**Domains.** All four unregistered: `.com` **404**, `.org` **404**, `.dev` **404**, `.app` **404**.

**GitHub.** `repos/skfd/butchers-phrasebook` → **404**. `repos/skfd/butchersphrasebook` → **404**.
`users/butchers-phrasebook` → **404**. `users/butchersphrasebook` → **404**. All free.
`gh search repos "butchers phrasebook"` → **empty result**.

**App Store.** `term=butchers+phrasebook` → `resultCount 13`, all dictionaries and language
phrasebooks (*Learn French Phrasebook Pro*, *Brazilian Phrasebook*, Farlex *Dictionary.*), plus one
unrelated food app, *The Fat Butcher*. **None is named this.**

**Google Play.** 200, 1.18 MB, 30 cards, no consent wall, **no card title contains the phrase.**
**Clear.**

**General collision.** No exact-title owner. But the adjacency is the sharpest in round 2:
**[The Butcher's Handbook](https://butchershandbook.com/) is a live, active site occupying this
project's exact concept under a name one word away** — its pages include
["Butchery Glossary — A-Z Butcher's Dictionary"](https://butchershandbook.com/glossary/),
["Butchering Terms Glossary: 110+ Essential Butcher Terms Explained (2026)"](https://butchershandbook.com/guides/butchering-terms-glossary/)
and ["Butcher Shop Slang: Decode 50+ Butcher Terms & Phrases"](https://butchershandbook.com/guides/butcher-shop-slang/).
Round 1 already cited this site as a source for the word *chine*. Also in the neighbourhood:
[*The Butcher's Book* by Hendrik Dierendonck](https://www.amazon.com/Butchers-Book-Hendrik-Dierendonck/dp/9463887946),
[*The Butchers Manual*](https://www.amazon.com/Butchers-Manual-Compendium-Practical-Information/dp/1447449762),
and [*The Gourmet Butcher's Guide to Meat*](https://www.amazon.com/Gourmet-Butchers-Guide-Meat-Professionally/dp/1603584684).

**The obvious problem.** **It reads as a knock-off of `butchershandbook.com`** — *Butcher's
Phrasebook* against *The Butcher's Handbook* is one consonant cluster apart, in the same niche, and
the two will be confused in citation and recall permanently. Second: the name says **butcher, not
beef** — the project is beef-only across seven traditions, and "butcher" promises pork, lamb and
poultry as well. Third, the possessive costs a slug decision every time it is written
(`butchers-` vs `butcher-s-`) and the apostrophe cannot survive into a domain. And "Butcher" carries
heavy unrelated fame — Jim Butcher the novelist, Joyce Carol Oates's *Butcher*, Billy Butcher from
*The Boys*.

## 5. Meat Phrasebook

**Register:** the steer, one level broader.

**Domains.** All four unregistered: `.com` **404**, `.org` **404**, `.dev` **404**, `.app` **404**.

**GitHub.** `repos/skfd/meat-phrasebook` → **404**. `repos/skfd/meatphrasebook` → **404**.
`users/meat-phrasebook` → **404**. `users/meatphrasebook` → **404**. All free.
`gh search repos "meat phrasebook"` → **empty result**.

**App Store.** `term=meat+phrasebook` → `resultCount 15`, all meat commerce and thermometers
(*MEATER®*, *The MeatStick*, *Meat N' Bone*, *TenderCuts*, *La Carniceria Meat Market*). **None is
named this.**

**Google Play.** 200, 1.17 MB, 30 cards, no consent wall, **no card title contains the phrase.**
**Clear.**

**General collision.** No exact-title owner across four queries. One genuine near-miss is worth
knowing because it is *this project as a book*:
[*VOCABULARIO DE LA CARNE (Español-Inglés): Meat Vocabulary (English-Spanish)* by Xavier Balp](https://www.amazon.com/VOCABULARIO-CARNE-Espa%C3%B1ol-Ingl%C3%A9s-Vocabulary-English-Spanish/dp/B0DH4YXTCL)
— 1,300+ bilingual meat terms. It is literally a meat phrasebook, just not titled one. Adjacent
reference works: [*The Meat Buyer's Guide*](https://www.amazon.com/Buyers-Guide-North-American-Processors/dp/1935593005),
[LaFrieda's *Meat: Everything You Need to Know*](https://www.amazon.com/Meat-Everything-You-Need-Know/dp/1476725993),
[*The Everyday Meat Guide*](https://www.amazon.com/Everyday-Meat-Guide-Neighborhood-Butchers/dp/1452142882).

**The obvious problem.** **Scope.** The atlas is 153 cuts of **beef** on one bovine carcass, and the
README's first line is "One animal". *Meat Phrasebook* promises pork, lamb, poultry and game, so the
name writes a cheque the project does not cash — and if it ever did add a second species the frame,
not the name, is what would have to change. It also inherits the same Memrise/Phrase-Finder
language-learning drag as *Beef Phrasebook* without the compensating specificity.

## 6. Beef Glossary

**Register:** plain, and the driest option that still carries the subject.

**Domains.** All four unregistered: `.com` **404**, `.org` **404**, `.dev` **404**, `.app` **404**.

**GitHub.** `repos/skfd/beef-glossary` → **404**. `repos/skfd/beefglossary` → **404**.
`users/beef-glossary` → **404**. `users/beefglossary` → **404**. All free.
`gh search repos "beef glossary"` → **empty result**.

**App Store.** `term=beef+glossary` → `resultCount 14`, all cattle-industry and steakhouse apps
(*Beef News and Markets*, *GENEX Beef*, *CattleFax*, *LongHorn Steakhouse*, *Beef Cow BCS*). **None
is named this.**

**Google Play.** 200, 1.22 MB, 30 cards, no consent wall, **no card title contains the phrase.**
**Clear.**

**General collision.** No owner — and that is the finding rather than the reassurance. One site uses
the exact title as a page heading ([AkoVet, *Beef Glossary*](https://akovet.org/for-animal-owners/beef-cattle/beef-glossary-of-terms/))
and **roughly ten more use a near-identical heading**, split across two unrelated senses. *Cattle
production and genetics:* [MU Extension, *Beef Production Glossary*](https://extension.missouri.edu/publications/g2030),
[eXtension *Beef Cattle Glossary*](https://beef-cattle.extension.org/beef-cattle-glossary/),
[*Glossary of Beef Terms*, Beef Runner](https://beefrunner.com/2011/12/01/glossary-of-beef-terms/),
[U. Arkansas FSA-3112](https://www.uaex.uada.edu/publications/PDF/FSA-3112.pdf),
[UT *Cattle and Beef Market Definitions*](https://utia.tennessee.edu/publications/wp-content/uploads/sites/269/2023/10/W801.pdf),
[Rodeo Houston](https://www.rodeohouston.com/wp-content/uploads/2023/08/H-Calf-Glossary-of-Terms.pdf).
*Cuts and cooking:* [VitalChoice, *Beef Terms: A Glossary*](https://www.vitalchoice.com/articles/cooking-tips/beef-terms),
[*The Delicious Glossary of All Things Beef*](https://beefitarian.com/the-delicious-glossary-of-all-things-beef/),
[The Nibble](https://www.thenibble.com/reviews/main/meats/beef/glossary.asp).

**The obvious problem.** **It is a page type, not a product name.** Eleven organisations already
publish something called a beef glossary, so the name announces the atlas as one more entry in a
genre it is trying to replace — and the genre is *alphabetical lists of terms*, which is the exact
thing this project argues is insufficient. It is also **split down the middle by "beef"**: half the
existing glossaries are about *cattle breeding and market terms*, not cuts, so the name does not even
disambiguate which beef subject it means.

## 7. Beef in Translation

**Register:** plain, and the steer's "translation between cultures" idea stated outright.

**Domains.** All four unregistered: `.com` **404**, `.org` **404**, `.dev` **404**, `.app` **404**.

**GitHub.** `repos/skfd/beef-in-translation` → **404**. `repos/skfd/beefintranslation` → **404**.
`users/beef-in-translation` → **404**. `users/beefintranslation` → **404**. All free.
`gh search repos "beef in translation"` → **empty result**.

**App Store.** `term=beef+in+translation` → `resultCount 15`, all translation utilities (*Google
Translate*, *Naver Papago*, *Talk & Translate*) plus one stray *Beef News and Markets*. **None is
named this.**

**Google Play.** 200, 1.25 MB, 30 cards, no consent wall, **no card title contains the phrase.**
**Clear.**

**General collision.** No exact-title owner found in three queries — but the negative is unusually
weak here, because **8 of 8 results on the quoted phrase were dictionary entries**:
Collins English-Italian *BEEF*, [Cambridge *BEEF*](https://dictionary.cambridge.org/),
[SpanishDictionary.com](https://www.spanishdict.com/translate/beef), Translate.How. The
*"X in Translation"* formula is occupied in food by one strong incumbent —
**[Eating In Translation](https://www.eatingintranslation.com/)**, Dave Cook's NYC food site running
since 2005 with work published in the New York Times — plus scattered one-offs
([Tasty's *Lost In Translation* series](https://www.buzzfeed.com/amandaeedelman/lost-in-translation-trailer-tasty),
[The Splendid Table](https://www.splendidtable.org/story/2016/07/22/lost-in-translation),
[*Food and translation* in *The Translator*](https://www.tandfonline.com/doi/full/10.1080/13556509.2015.1110934)).
On the **rap-beef** risk: checked, and on the *exact quoted phrase* it did not materialise —
dictionaries dominate, not hip-hop. Slang only takes over once the phrasing loosens
("beef explained" → [Billboard's Drake/Kendrick timeline](https://www.billboard.com/lists/drake-kendrick-lamar-beef-timeline/)).

**The obvious problem.** **A name that describes a dictionary lookup has to outrank dictionaries**,
and it will not — Collins, Cambridge, WordReference and Linguee own the phrase's results page today.
Behind that sits the formula problem: *X in Translation* is a *Lost in Translation* riff, which reads
as a magazine-column title rather than a reference work, and it is one word from Dave Cook's
twenty-year-old food property. And the slang sense is only ever one sloppy query away.

## 8. Beef Translated

**Register:** plain, the same idea in the active voice.

**Domains.** All four unregistered: `.com` **404**, `.org` **404**, `.dev` **404**, `.app` **404**.

**GitHub.** `repos/skfd/beef-translated` → **404**. `repos/skfd/beeftranslated` → **404**.
`users/beef-translated` → **404**. `users/beeftranslated` → **404**. All free.
`gh search repos "beef translated"` → **empty result**.

**App Store.** `term=beef+translated` → `resultCount 15`, all translation utilities. **None is named
this.**

**Google Play.** 200, 1.21 MB, 30 cards, no consent wall, **no card title contains the phrase.**
**Clear.**

**General collision.** No exact-title owner — but **two live blog posts are all but this name as a
headline**, both doing a slice of exactly what the atlas does:
["Italian Beef Cuts, Translated" (Casa Mia Tours)](https://casamiatours.com/italian-beef-cuts-translated/)
and ["French Beef Cuts Translated" (Days on the Claise)](https://daysontheclaise.blogspot.com/2020/03/french-beef-cuts-translated.html).
And the wider niche is busier than round 1 assumed — **[beefcuts.org](https://beefcuts.org/) is an
entire domain translating beef cut names between Brazil, Argentina and Costa Rica**, plus
[G. J. Honour's American-to-British translation](https://gjhonour.com/blogs/family-butcher/translation-of-american-to-british-beef-cuts),
[Grasspunk's French cut translations](https://grasspunk.com/french-beef-cut-translations/),
[an Ask MetaFilter thread](https://ask.metafilter.com/104492/), and
[a German butcher-shop cheat sheet](https://www.noordinaryhomestead.com/butcher-shop-cheet-sheet-auf-deutsch/).
*(This is prior art for the **project**, not just the name — worth folding into `shape.md`
independently of whatever the atlas ends up called.)*

**The obvious problem.** **The name is already the headline of the blog-post genre it would be
competing with.** A dozen "<Country> beef cuts, translated" posts exist; naming the atlas *Beef
Translated* files it among them rather than above them, and every query the name most resembles
returns one of those posts or a dictionary. It is also **grammatically a past participle** — it
describes a completed action performed on beef, so it reads as a finished document rather than a
thing you open and turn around.

## 9. Cuts in Translation

**Register:** plain, the mechanism named. **Fails the subject test** — no beef/cow/meat word.

**Domains.** All four unregistered: `.com` **404**, `.org` **404**, `.dev` **404**, `.app` **404**.

**GitHub.** `repos/skfd/cuts-in-translation` → **404**. `repos/skfd/cutsintranslation` → **404**.
`users/cuts-in-translation` → **404**. `users/cutsintranslation` → **404**. All free.
`gh search repos "cuts in translation"` → **empty result**.

**App Store.** `term=cuts+in+translation` → `resultCount 15`, all translation utilities. **None is
named this.**

**Google Play.** 200, 1.26 MB, 30 cards, no consent wall, **no card title contains the phrase.**
**Clear.**

**General collision.** **No result found** for any book, film, band, restaurant, podcast, paper or
exhibition with this exact title, across two queries. The results page is instead split between
dictionaries (Collins *CUT*, LEO, Cambridge) and film-editing explainers (Backstage's *Types of Cuts
in Film*, [Adobe on cuts in film](https://www.adobe.com/creativecloud/video/post-production/cuts-in-film/cross-cut.html)).
Of the three translation-family names this is the most distinctive — no incumbent and no slang sense.

**The obvious problem.** **"Cuts" reads as film cuts and record tracks before it reads as meat.**
Without a beef word adjacent, the name is about editing, and it lands in a results page owned by
Adobe and Backstage. That is the owner's first constraint failing outright: someone seeing it cold
does not know what it is about. It also inherits the *Lost in Translation* formula and sits beside
*Eating In Translation*.

## 10. Cut Phrasebook

**Register:** the steer, minus the subject. **Fails the subject test.**

**Domains.** All four unregistered: `.com` **404**, `.org` **404**, `.dev` **404**, `.app` **404**.

**GitHub.** `repos/skfd/cut-phrasebook` → **404**. `repos/skfd/cutphrasebook` → **404**.
`users/cut-phrasebook` → **404**. `users/cutphrasebook` → **404**. All free.
`gh search repos "cut phrasebook"` → **empty result**.

**App Store.** `term=cut+phrasebook` → `resultCount 13`, all dictionaries and travel phrasebooks
(*Travel Phrasebook | Translator* by Bravolol, *Google Translate*, *Phrasebook – over 30 languages*
by Jourist). **None is named this.**

**Google Play.** 200, 1.18 MB, 30 cards, no consent wall, **no card title contains the phrase.**
**Clear.**

**General collision.** No exact-title owner. The instructive hits are a **collision of parsing rather
than of ownership**: the bookstore pass returned
[*Words And Phrases To Cut Out And Collage*](https://www.amazon.com/Words-Phrases-Cut-Collage-Inspirational/dp/B0C4MRXBDV)
and [*1000 Cut-Out Inspirational Phrase Strips*](https://www.amazon.com/Cut-Out-Inspirational-Phrase-Strips-Ready/dp/B0H7R2KBDY),
i.e. craft supplies. Organic results for bare "cut" were entirely idiom and dictionary content.

**The obvious problem.** **It parses backwards.** English reads *cut phrasebook* as "a phrasebook you
cut out", not "a phrasebook of cuts" — the craft-supply books above are what the phrase already
means in the wild. On top of that it has **no meat signal at all** and collides with film editing,
haircuts and *The Cut*. It is free because nobody wants it.

## 11. Cut Vocabulary

**Register:** plain, minus the subject. **Fails the subject test.**

**Domains.** All four unregistered: `.com` **404**, `.org` **404**, `.dev` **404**, `.app` **404**.

**GitHub.** `repos/skfd/cut-vocabulary` → **404**. `repos/skfd/cutvocabulary` → **404**.
`users/cut-vocabulary` → **404**. `users/cutvocabulary` → **404**. All free.
`gh search repos "cut vocabulary"` → **empty result**.

**App Store.** `term=cut+vocabulary` → `resultCount 15`, **every single result a vocabulary
trainer** — *Vocabulary.com*, *WordUp*, *Vocabulary Builder by Magoosh*, *Vocabuo*, *VividVocab*,
*Flexi*. Not a collision on the name, but the densest category noise of any candidate in round 2.

**Google Play.** 200, 1.26 MB, 30 cards, no consent wall, **no card title contains the phrase.**
**Clear.**

**General collision.** No page titled this appeared in any of three queries — no band, album, film,
app or product. The bare-name search returned **only definitions of the word "cut"**:
[Vocabulary.com's entry for *cut*](https://www.vocabulary.com/dictionary/cut),
[Merriam-Webster's *CUT* thesaurus page](https://www.merriam-webster.com/thesaurus/cut),
[a Vocabulary.com word list](https://www.vocabulary.com/lists/33390). ESL material on this topic
exists but is titled *Cuts of Meat*, not *Cut Vocabulary*
([Cambridge](https://dictionary.cambridge.org/us/topics/food/cuts-of-meat/),
[LanGeek](https://langeek.co/en/vocab/subcategory/1718/word-list),
[islcollective](https://en.islcollective.com/english-esl-worksheets/vocabulary/food/meat-cuts/114880)).

**The obvious problem.** **Both words are dictionary magnets, so the name is two decoys in a row.**
"Vocabulary" fetches Vocabulary.com and a wall of vocabulary-builder apps; "cut" fetches the
dictionary entry for *cut*. Nobody holds it and nobody could rank for it. And, as with the other
cut-family names, it says nothing about beef — film cut, pay cut, haircut all come first.

## 12. Meat Vocabulary — Reject

**Register:** plain, subject present.

**Availability is completely clean.** `.com` **404**, `.org` **404**, `.dev` **404**, `.app` **404**.
`repos/skfd/meat-vocabulary` → **404**, `repos/skfd/meatvocabulary` → **404**,
`users/meat-vocabulary` → **404**, `users/meatvocabulary` → **404** — all free.
`gh search repos "meat vocabulary"` → **empty**. App Store `term=meat+vocabulary` → `resultCount 15`,
a fuzzy mix of meat commerce and vocabulary trainers, **none named this**. Google Play 200, 1.25 MB,
30 cards, no consent wall, **no card title contains the phrase**. Nothing blocks it.

**The obvious problem.** Availability is not the issue. **The phrase is already an ESL category
label**, used as a page title or heading by at least seven distinct organisations:
[Quizlet *Meat Vocabulary Flashcards*](https://quizlet.com/17052323/meat-vocabulary-flash-cards/),
[Promova *Meat Vocabulary: A Chef's Guide to Meat Terminology in English*](https://promova.com/english-vocabulary/meat-and-poultry-vocabulary),
[The English Alley](https://theenglishalley.com/m/vocabulary/shops/meat.html),
[Bespeaking](https://bespeaking.com/meat-vocabulary-to-know-easy-english/),
[Woodward English](https://www.woodwardenglish.com/lesson/meat-english-vocabulary/),
[LanguageGuide](https://www.languageguide.org/english/vocabulary/meat/),
[EnglishClub](https://www.englishclub.com/vocabulary/food-meats.php),
[Grammar Monster](https://www.grammar-monster.com/vocabulary/ESL-vocabulary-food-meat.htm).
Notably, **zero butchery-industry sites use it** — the phrase belongs entirely to English teaching.
Adopting it would file a seven-tradition butchery atlas under "learn food words in English", which is
the wrong shelf in a way no amount of front-page copy fixes. It also carries the same all-species
scope error as *Meat Phrasebook*.

## 13. One Beast — Reject

**Register:** plain, evocative. **Fails the subject test** — "beast" is not a beef word.

**Domains.** `onebeast.com` → **200** (registered). Fetched: it serves a 114-byte
`window.location.href="/lander"` redirect stub, i.e. a **parked domain on a reseller lander**, not a
real site. `.org` → **404** (free), `.dev` → **404** (free), `.app` → **404** (free).

**GitHub.** `repos/skfd/one-beast` → **404** (free), `repos/skfd/onebeast` → **404** (free),
`users/one-beast` → **404** (free) — but `users/onebeast` → **200**, **the bare username is taken**
(a dormant User account created 2010-09-17, 0 public repos, 2 followers). `gh search repos "one
beast"` → small unrelated hits only, top is `TyrusRC/chimera` at 3 stars matching on its description
"Many backends, one beast".

**App Store.** `term=one+beast` → `resultCount 14`, all games and fitness (*Beast Bumpers*, *I Am
Your Beast*, *World Beast War*, *Beast Mode Soccer+*). **None is named this.**

**Google Play.** 200, 1.29 MB, 30 cards, no consent wall, **no card title contains the phrase.**
**Clear.**

**The obvious problem.** **"Whole beast" is already the established phrase for whole-animal
butchery**, so *One Beast* reads as a derivative of it rather than as a name:
[*Whole Beast Butchery: The Complete Visual Guide to Beef, Lamb, and Pork* by Ryan Farr](https://www.amazon.com/Whole-Beast-Butchery-Complete-Visual/dp/1452100594),
[Beast and Cleaver](https://www.exploretock.com/beastandcleaver/) in Seattle,
[BEAST Butcher & Block](https://www.tripadvisor.com/Restaurant_Review-g44881-d17625116-Reviews-BEAST_Butcher_Block-Saint_Louis_Missouri.html)
in St. Louis. Secondarily, "beast" does not say beef — it says lamb, pig or *Bloodborne*
([*Great One Beast*](https://bloodborne.wiki.fextralife.com/Great+One+Beast) is a real drag on the
exact phrase) — and it sits inside a dense fitness-and-supplement "Beast" trademark thicket
([Eddie Hall's BEAST™](https://beast.co.uk/), [Beast Sports Nutrition](https://beastsports.com/)).
The taken GitHub username forecloses ever making it an org.

## 14. Same Beast — Reject

**Register:** plain. **Fails the subject test.**

**Domains.** `samebeast.com` → **200** (registered) — and unlike its siblings it is **a live site**:
309 KB, `<title>PP77 ✦ Pocketplane Dengan Identitas Digital Lebih Compact</title>`, an
Indonesian-language commercial page. Not parked, not dormant, and not something to inherit a domain
next to. `.org` → **404** (free), `.dev` → **404** (free), `.app` → **404** (free).

**GitHub.** `repos/skfd/same-beast` → **404** (free), `repos/skfd/samebeast` → **404** (free),
`users/same-beast` → **404** (free) — but `users/samebeast` → **200**, **taken** (User, created
2022-01-04, 1 public repo). `gh search repos "same beast"` → one 0-star hit,
`mlynek003/DifferentAnimal`, whose description is the idiom below.

**App Store.** `term=same+beast` → `resultCount 3` (*MoneyLion*, *Among Beast!*, *Cash App*) —
the thinnest result set in round 2. **None is named this.**

**Google Play.** 200, 1.26 MB, 30 cards, no consent wall, **no card title contains the phrase.**
**Clear.**

**The obvious problem.** Three owners, none of them this project. A recording artist holds the exact
title — [*Same Beast* EP by Caxxianne](https://music.apple.com/tr/album/same-beast-ep/1640512416),
four tracks — with [Odezy Da Beast's *Different Animal, Same Beast*](https://www.deezer.com/en/album/478267705)
behind it. The **`.com` is a live Indonesian commercial site**. And culturally the phrase is
pre-owned: *"different animal, same beast"* is [a well-known Kobe Bryant line](https://x.com/kobebryant/status/942795811540295680)
with its own explainer traffic, so every search for the name lands in sports motivation. Building
beef SEO against a basketball meme is a losing start, and the GitHub username is gone as well.

## 15. Cross-Cut — Reject

**Register:** the wildcard. A real butchery term that puns on cross-cultural — and **the only
candidate in round 2 with all four TLDs registered** (round 1's bare *Concordance* was the same, and
was cut before reaching the table). **Fails the subject test** too.

**The pun is real, and confirmed.** *Cross-cut chuck* is genuine current trade usage: the whole
shoulder removed from the forequarter is the cross-cut chuck (~100 lb, ~23% of the carcass) per
[Chefs Resources' chuck primal guide](https://www.chefs-resources.com/types-of-meat/beef/cuts-of-beef/beef-chuck-roast/),
alongside IMPS/NAMP chuck series 113–116
([chuck steak names and IMPS numbers](https://www.chefs-resources.com/types-of-meat/beef/cuts-of-beef/chuck-steak-varieties-and-alternate-names/)).
The Beef Checkoff itself lists a [**Shank Cross-Cut**](https://www.beefitswhatsfordinner.com/cuts/cut/2491/shank-cross-cut)
as a named cut. *(Caveat, recorded as unchecked: the USDA AMS IMPS Series 100 PDF was **not** opened,
so whether "cross-cut chuck" is a literal IMPS item heading rather than trade vernacular alongside
IMPS-numbered items is unverified.)*

**Domains — all four registered, and three are in active use.**
`crosscut.com` → RDAP **200**; fetched with `curl -L`, it **redirects to `https://www.cascadepbs.org/articles/`**
(the final URL was recorded; the individual hop status codes were not)
(`<title>Articles | Cascade PBS</title>`) — the 18-year Seattle nonprofit newsroom
[Crosscut.com](https://en.wikipedia.org/wiki/Crosscut.com), merged into KCTS-TV in 2015, rebranded to
[Cascade PBS in 2024](https://www.cascadepbs.org/news/2024/01/crosscut-and-cascade-pbs-say-bye-seattle-center-hello-first-hill/),
newsroom [shut in September 2025](https://www.cascadepbs.org/all/2025/09/the-new-path-forward-for-the-cascade-pbs-newsroom/)
after CPB funding cuts ([Washington State Standard](https://washingtonstatestandard.com/2025/09/24/last-words-what-washington-is-losing-with-the-demise-of-crosscut/)).
The brand is vacating, but the domain is **actively redirected**, the [@crosscut Instagram](https://www.instagram.com/crosscut/)
is live, and [a *Crosscut* podcast feed](https://podcasts.apple.com/us/podcast/crosscut/id1011469236) is still up.
`crosscut.org` → RDAP **200**; fetched, it **redirects to `crosscutmt.org`**,
`<title>Crosscut Mountain Sports Center</title>` — a Bozeman, Montana nonprofit.
`crosscut.dev` → RDAP **200** (registered) but `nslookup` returns **`Non-existent domain`** and HTTPS
returns **000**: registered, never delegated.
`crosscut.app` → RDAP **200**; fetched, it serves the same 114-byte `/lander` parking stub as
`onebeast.com`.

**GitHub.** `repos/skfd/cross-cut` → **404** (free), `repos/skfd/crosscut` → **404** (free),
`users/cross-cut` → **404** (free) — but `users/crosscut` → **200**, **taken** (`Crosscut`, User,
created 2009-08-12). Worse, **a repo is literally named `crosscut`**:
[`hannobraun/crosscut`](https://github.com/hannobraun/crosscut), 18 stars, "An experimental project
to create an interactive programming language" — the same failure mode round 1 rejected *Balgol* for,
in English. And `gh search repos crosscut` is topped by
[`keeper013/CrossCutterN`](https://github.com/keeper013/CrossCutterN) (79 stars) plus a run of
microservices repos, because **"cross-cutting concern" is standard aspect-oriented-programming
jargon** — which is precisely the audience a GitHub repo is read by.

**App Store.** `term=crosscut` → `resultCount 12`; `term=cross+cut` → `resultCount 15`. No app is
*titled* Cross-Cut, but two nearby owners appear: *Crosscut Cam* (Photo & Video) and, more
pointedly, **`CrossCut Games, Inc.`** as a *seller* of two titles (*Moldvay's Labyrinth*).

**Google Play — the only storefront hit in round 2.** 200, 1.21 MB, 30 cards, no consent wall, and a
card **titled exactly `CrossCut`**, published by **The Seven Fifty Limited Partnership**. The
hyphenated query `cross-cut` returns the same app. This is the one exact-title storefront collision
found across all fifteen candidates.

**What that app is — because the task asked whether the pun was taken by woodworking or film
editing, and the answer is neither.** Its listing was fetched:
`play.google.com/store/apps/details?id=cross.cut.app` → **200**, category **Tools**, description
opening *"Calculate Your Real Take-Home Pay! When receiving cross-border payments, hidden fees and
bad exchange rates always eat into your earnings…"* — a **cross-border payment payout calculator**
for freelancers on Payoneer, PayPal and Wise. So the pun has been claimed by a **third** sense nobody
listed: the *cut* a payment processor takes on a *cross*-border transfer. Woodworking and film
editing dominate the *search results* (saw sleds and Adobe's parallel-editing glossary), but the
literal storefront name was taken by fintech. That the same two words land on a butchery term, a saw,
an editing technique, an AOP concept and a remittance fee is itself the argument against the name.

**The obvious problem.** **Everything is taken.** Four registered TLDs, the GitHub username, a GitHub
repo of that exact name, an exact-title Play app, an App Store developer, a Seattle news archive, a
Montana nonprofit, [Crosscut Ventures](https://crosscut.vc/) (an LA VC with >$300M deployed), and at
least one [recording artist](https://www.discogs.com/artist/495023-Crosscut). Against that, the pun
has to compete with two dominant everyday senses — the
[crosscut saw](https://en.wikipedia.org/wiki/Crosscut_saw) and sled, which own commercial search, and
[cross-cutting](https://en.wikipedia.org/wiki/Cross-cutting) in film, which owns explainer search —
plus AOP jargon in the one place a repo lives. Hyphenation buys nothing: search engines treat
*Cross-Cut*, *Crosscut* and *Cross Cut* as one token. And [Shotcut](https://www.shotcut.org/), a
popular open-source video editor, is one syllable away. The food lane is genuinely empty — **no**
restaurant, steakhouse or butcher of this name was found — but that is the only lane that is.
The pun was worth asking about; the answer is that it was taken long ago, several times over.
