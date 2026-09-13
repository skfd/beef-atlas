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
| 0.52 | belly line — bottom of the barrel                |
| 0.70 | mid-barrel — the upper/lower primal split        |
| 0.90 | topline / back                                   |
| 1.00 | top of the withers                               |

Y: the barrel is about +/-0.17 wide; a box spanning y -0.5..0.5 takes the full width.

A cut is `boxes: [[x0,y0,z0, x1,y1,z1], ...]` — a union, so irregular shapes are
built from two or three boxes. Boxes are clipped against the cow mesh, so it is safe
(and normal) to over-extend a box past the silhouette.
