# The cow frame

Every cut is a set of axis-aligned boxes in one normalized frame. The same frame is
used by every culture, so the same region of the animal is the same numbers everywhere.

Axes (right-handed, cow faces +X):

    x  0.00 = rear of the buttock / tail base   ->  1.00 = tip of the nose
    y -0.50 = left flank  ->  +0.50 = right flank   (0 = spine plane, body is symmetric)
    z  0.00 = ground under the hoof             ->  1.00 = top of the withers

Side view, nose to the right:

                            withers          poll
      z=1.00  .                 _____________
      z=0.90  |   TOPLINE  ____/             \___
              |           /                      \__  head
      z=0.70  |  - - - - - - - - - - - - - - - - -  \   <- upper/lower primal split
      z=0.52  |  BELLY    \______________________/
              |            |  |            |  |
      z=0.28  |  knee/hock +  +            +  +
              |            |  |            |  |
      z=0.00  +------------+--+------------+--+---------- ground
               0.00   0.16  0.24      0.46   0.62   0.80   1.00
               tail   hip   hook    last rib  elbow  poll   nose

X landmarks

| x    | landmark                                        |
|------|--------------------------------------------------|
| 0.00 | rear of round / tail base                        |
| 0.08 | pin bone (aitch bone)                            |
| 0.16 | hip joint                                        |
| 0.24 | hook bone — round / sirloin boundary             |
| 0.36 | sirloin / short loin boundary                    |
| 0.46 | last rib — loin / rib boundary                   |
| 0.56 | 5th rib — rib / chuck boundary                   |
| 0.62 | elbow, front leg attachment                      |
| 0.72 | point of shoulder — chuck / neck boundary        |
| 0.80 | poll — neck / head boundary                      |
| 1.00 | nose                                             |

Z landmarks

| z    | landmark                                        |
|------|--------------------------------------------------|
| 0.00 | hoof / ground                                    |
| 0.28 | knee (front) and hock (rear)                     |
| 0.49 | belly line — bottom of the barrel                |
| 0.69 | mid-barrel — the upper/lower primal split        |
| 0.89 | topline / back                                   |
| 0.93 | top of the withers, the high point of the mesh   |

The z table above is what the mesh as built actually measures; the cut data was
written against a nominal 0.52 / 0.70 / 0.90 / 1.00, which is within a couple of
percent everywhere and is absorbed by the clipping described below.

Y: the barrel is about +/-0.17 wide. Nothing you author sets y — see below.

## What a cut actually is

One rectangle in this side view:

    "x": [0.36, 0.46], "z": [0.62, 0.92], "full_width": true

That is the whole geometry. There is no y in the data and no list of boxes: every cut
is carved the full width of the animal, and `blender/build.py` hardcodes the cutter's
half-width rather than reading anything from the file. `tools/check_data.py` requires
`x`, `z` and `full_width` on every cut and will reject anything else.

`full_width` is therefore **not a geometric switch**. Setting it `false` carves exactly
the same slab; all it does is make `web/app.js` print a note in the panel saying that
this cut is a thin sheet of muscle in life, so the reader should take the slab as
whereabouts rather than as the shape of the cut. It is an honesty label. Use it for
sheets — flank, skirt, the abdominal wall — and leave it `true` for blocks.

Rectangles from different cuts in the same tradition may overlap, and normally do at
the seams. `blender/cuts.py` resolves that before anything is carved: `partition()`
lays every rectangle's edges down as a grid, works out which cut owns each cell, and
merges the cells back into a union of boxes that tiles the tradition exactly once. So
the box unions are **derived**, never authored — if you go looking for a `boxes` key in
`data/cuts_*.json` you will not find one.

Those derived boxes are then intersected with the cow mesh, so it is safe (and normal)
to over-extend a rectangle past the silhouette: a cut that reaches below the belly line
or past the nose simply comes back clipped to the animal. A cut whose rectangle misses
the animal altogether carves nothing, and the page says so rather than showing an empty
slot.

One consequence worth knowing when you read the percentages: because the geometry is a
rectangle in x and z and the y extent is constant, **the overlap between two cuts is an
area in this side view**, not a volume. See [`docs/differences.md`](../docs/differences.md).
