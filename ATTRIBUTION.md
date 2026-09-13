# Attribution

## The cow model

The animal every tradition is carved from is:

> **“Cow”** by **nandakishor.irnv** — <https://sketchfab.com/3d-models/cow-14e616e26823472c809a03042a94b990>
> Licensed under **[Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/)**.

Obtained via the [Objaverse](https://objaverse.allenai.org/) mirror of Sketchfab
(object `14e616e26823472c809a03042a94b990`), which is what makes it fetchable without
a signed-in account.

It is used here **modified**: welded, re-oriented, scaled into the coordinate frame
in `data/FRAME.md`, voxel-remeshed into a watertight shell, decimated, and then cut
into pieces by `blender/build.py`. CC BY 4.0 permits this and requires that the
changes be indicated, which this paragraph does.

`assets/cow_source.glb` is the unmodified original as downloaded.
`assets/cow_normalized.blend` is the fitted version the build actually consumes.

## The cut data

Each `data/cuts_*.json` carries a `sources` array listing the URLs actually fetched
for that tradition. The backbone is Wikipedia’s “Cut of beef” and its per-country
counterparts, plus:

- **United States** — USDA IMPS Series 100, Beef Checkoff cut charts
- **United Kingdom** — AHDB / Simply Beef and Lamb
- **France** — fr.wikipedia *Découpe du bœuf*, la-viande.fr
- **Russia** — ГОСТ 7595-79 *Мясо. Разделка говядины для розничной торговли*
- **Brazil** — pt.wikipedia, scotconsultoria *mapa do boi*
- **Korea** — 축산물품질평가원, ko.wikipedia 소고기 부위
- **Japan** — 日本食肉格付協会, ja.wikipedia 牛肉

The same list is shown in the page under **About & sources**.

## This project

Code and data in this repository are the author’s own work. The cow model is not,
and stays under CC BY 4.0 as above.
