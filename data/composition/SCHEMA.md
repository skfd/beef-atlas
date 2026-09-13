# What a cut is made of

The atlas draws each cut as a rectangle in a side view. That is honest about roughly
*where* a cut is and says nothing about *what it is* — and a butcher does not think in
rectangles, they think in muscles and in where the saw crosses a rib.

This folder is the bridge: for every one of the 153 cuts, which muscles it contains and
where along them it starts and stops, with the source that says so.

It is **not** the geometry. Nothing here carves anything yet. The point of building the
table first is that it tells us which traditions can be rebuilt on muscles at all, and
which are documented so loosely that rectangles are the honest answer.

## Files

`data/composition/<id>.json`, one per tradition, keyed by the same cut `id` as
`data/cuts_<id>.json`. The cut files are not modified.

```json
{
  "culture": "United States",
  "id": "us",
  "sources": ["https://…"],
  "cuts": [ … ]
}
```

Every cut in `cuts_<id>.json` must appear here exactly once.

## A cut

```json
{
  "id": "short_loin",
  "muscles": [
    {"id": "longissimus", "role": "defining", "extent": "portion",
     "from": "rib-13", "to": "ilium",
     "note": "the last thoracic and all six lumbar segments; the same muscle is the rib eye in front of rib 13"},
    {"id": "psoas-major", "role": "major", "extent": "portion", "from": "rib-13", "to": "ilium"},
    {"id": "psoas-minor", "role": "minor", "extent": "whole"},
    {"id": "multifidus", "role": "trace", "extent": "portion"}
  ],
  "unmodelled": [
    {"latin": "M. iliocostalis lumborum", "role": "trace",
     "where": "lateral to the longissimus over the lumbar vertebrae"}
  ],
  "bone_in": true,
  "evidence": "standard",
  "bounds_evidence": "standard",
  "sources": [
    {"url": "https://…", "supports": ["muscles", "bounds"],
     "quote": "verbatim text from the page, not a paraphrase"}
  ],
  "dispute": null
}
```

### `muscles[]`

| Key | Meaning |
|---|---|
| `id` | **must** be one of the 49 ids in `data/anatomy/muscle.json`. Anything else goes in `unmodelled`. |
| `role` | `defining` — the cut essentially *is* this muscle · `major` — a substantial part of it · `minor` — present and named in specs · `trace` — anatomically there, nobody sells it that way |
| `extent` | `whole` — the cut takes the entire muscle · `portion` — it takes part of it |
| `from` / `to` | where the portion starts and stops. **Both are required whenever `extent` is `portion`**, and omitted when `whole`. Each is either a **bone id** from `data/anatomy/skeleton.json` — `rib-01`…`rib-13`, `lumbar-vertebrae`, `sacrum`, `ilium`, `ischium`, `scapula`, `humerus`, `carpus`, `femur`, `tarsus`, `sternum`, … — or one of three literals: `seam` (a natural seam with a neighbouring muscle), `origin`, `insertion` (the muscle's own end). |
| `seam` | `true` when the cut is released by seaming rather than sawn through bone |
| `note` | free text, and the right place to say "the same muscle is the rib eye in front of rib 13" |

**The bound lives on the muscle, not on the cut, and that is the whole point of this
table.** The rib eye, the strip loin and the chuck eye are one muscle — *longissimus* —
divided by a saw cut between the 12th and 13th ribs and another at the 5th. A list of
muscle names cannot tell them apart. `"from": "rib-06", "to": "rib-12"` can, and the
model has all thirteen rib pairs placed individually, so it is a boundary the geometry
could actually be carved against later.

A cut-level boundary could not express "longissimus from rib 6 to 12, but spinalis
whole", which is exactly the common case. Hence per-muscle.

### `unmodelled[]`

Muscles the cut genuinely contains that the atlas has not modelled. `latin` plus a
one-line `where` naming the modelled muscle it neighbours — that `where` is the spec for
whoever adds it to `muscle.json` later. This list is an output of the exercise, not a
failure of it.

### Evidence

Two axes, because they routinely differ: IMPS gives rib numbers and no muscle list,
UNL Bovine Myology gives muscles and no rib numbers.

| Grade | Means |
|---|---|
| `standard` | a government or international specification defines it — UNECE bovine standard, USDA IMPS, CFIA, a national 고시, JMGA |
| `trade` | an industry body or major trade source — AHDB, UNL Bovine Myology, the Beef Checkoff tenderness table, ABIEC, a national meat board |
| `inferred` | no source names it; derived from the cut's documented position plus anatomy. `dispute` must say what the reasoning was. |
| `contested` | sources name different muscles. `dispute` must list every candidate with its source. |

`evidence` grades the muscle list. `bounds_evidence` grades `from`/`to`. A cut with
standard muscles and inferred bounds is normal and the table should say so.

### `sources[]`

`quote` is **verbatim**, never a paraphrase, and is **mandatory** for any cut graded
`standard` or `trade` — the validator enforces it. `supports` says which part of the
entry the quote backs: `muscles`, `bounds`, or both.

For `inferred`, name the reasoning in `dispute`. For `contested`, list at least two
candidates with their sources. **"No source names a muscle for this cut" is a correct
and valuable answer** — several Korean and French cuts are defined by regulation in
terms of shape and position on purpose. Do not invent a Latin name to fill a field.

## Checking it

```sh
python tools/check_composition.py
```

Verifies that every cut is present exactly once, that muscle ids are real, that
`from`/`to` are real bone ids, that `portion` carries bounds, that `standard` and
`trade` entries carry a verbatim quote, and that `contested` lists more than one
candidate. It then prints the coverage table — what fraction of each tradition is
standard, trade, inferred or contested — which is the number that decides whether the
geometry can be rebuilt on muscles.

## Before you start researching

Read [`FINDINGS.md`](FINDINGS.md). It carries the correspondences already established
with verbatim quotes, and — just as useful — the list of sources that are hard-blocked,
so nobody spends thirty fetches rediscovering that `unece.org` returns 403.
