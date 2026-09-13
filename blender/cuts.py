"""Turn each culture's list of cut rectangles into a clean partition of the cow.

The research data gives every cut a rectangle in the side view: an x range along
the body and a z range up it. Two things are wrong with using those rectangles
directly as boolean cutters. They leave gaps -- meat belonging to no cut, which
would simply vanish from the model -- and they overlap, which would carve the same
volume twice. Neither is a flaw in the data; a butchery chart is drawn by hand and
the schemes genuinely disagree about where a boundary sits.

So the rectangles are resolved into a partition first:

  1. every rectangle edge becomes a grid line, giving a grid of cells whose
     boundaries are exactly the boundaries the data asked for;
  2. each cell goes to the smallest rectangle containing its centre, so a named
     subcut (misuji, chadolbagi, araignee) wins against the primal it sits in
     rather than being buried by it;
  3. a cell inside no rectangle goes to the nearest one, so the legs, the head
     and any gap between two primals end up somewhere instead of nowhere;
  4. the cells of each cut are merged back into as few rectangles as possible,
     because each one costs a boolean against the whole cow.

The result tiles the animal exactly once, which is what makes the "every cut,
exploded" view and the per-cut raycasting in the web page work.
"""

import colorsys


def palette(n):
    """n colours that stay apart from each other, on a warm butcher-chart bias.

    Lives here rather than in build.py so the web legend can be regenerated with
    plain Python: the swatch beside a cut name has to be the same colour Blender
    baked into that cut's material, and two copies of this would drift.
    """
    colours = []
    for i in range(n):
        h = (0.035 + i * 0.6180339887) % 1.0
        s = 0.40 + 0.18 * ((i * 3) % 4) / 3.0
        v = 0.92 - 0.20 * ((i * 5) % 3) / 2.0
        colours.append(colorsys.hsv_to_rgb(h, s, v) + (1.0,))
    return colours


def hex_colour(rgba):
    return "#%02x%02x%02x" % tuple(max(0, min(255, round(c * 255))) for c in rgba[:3])


# The grid is clipped to this box. It is a little larger than the mesh, so a
# rectangle that over-extends past the silhouette simply gets clipped by the cow.
BOUNDS = (-0.10, 1.10, -0.05, 1.25)   # x0, x1, z0, z1
# z reaches well past the withers because an imported animal may carry its head
# above 1.0; anything outside the grid would simply not be carved and vanish.


def _rect(cut):
    x0, x1 = sorted(cut["x"])
    z0, z1 = sorted(cut["z"])
    bx0, bx1, bz0, bz1 = BOUNDS
    return (max(x0, bx0), min(x1, bx1), max(z0, bz0), min(z1, bz1))


# Horizontal distance counts for much more than vertical when deciding which cut
# an unclaimed cell belongs to. A strip of belly hanging below the flank is flank;
# straight-line distance would hand it to whichever shank happened to be nearest
# diagonally, which is how an imported cow with a deeper barrel ended up with its
# udder coloured as hind shank.
X_WEIGHT = 3.0


def _point_rect_distance(px, pz, r):
    x0, x1, z0, z1 = r
    dx = max(x0 - px, 0.0, px - x1) * X_WEIGHT
    dz = max(z0 - pz, 0.0, pz - z1)
    return (dx * dx + dz * dz) ** 0.5


def _edges(values, lo, hi, epsilon=1e-6):
    out = sorted({lo, hi} | {v for v in values if lo < v < hi})
    merged = [out[0]]
    for v in out[1:]:
        if v - merged[-1] > epsilon:
            merged.append(v)
    return merged


def _merge_cells(cells, xs, zs):
    """Greedily merge a set of (i, j) grid cells into as few rectangles as possible."""
    remaining = set(cells)
    rects = []
    for j in range(len(zs) - 1):
        for i in range(len(xs) - 1):
            if (i, j) not in remaining:
                continue
            # run right as far as the cut continues
            i_end = i
            while (i_end + 1, j) in remaining:
                i_end += 1
            # then run up, but only while the whole span is still ours
            j_end = j
            while all((k, j_end + 1) in remaining for k in range(i, i_end + 1)):
                j_end += 1
            for jj in range(j, j_end + 1):
                for ii in range(i, i_end + 1):
                    remaining.discard((ii, jj))
            rects.append((xs[i], xs[i_end + 1], zs[j], zs[j_end + 1]))
    return rects


def partition(cuts):
    """Map cut id -> list of (x0, x1, z0, z1) boxes that tile BOUNDS exactly once."""
    bx0, bx1, bz0, bz1 = BOUNDS
    rects = {c["id"]: _rect(c) for c in cuts}
    areas = {k: (r[1] - r[0]) * (r[3] - r[2]) for k, r in rects.items()}

    xs = _edges([v for r in rects.values() for v in r[:2]], bx0, bx1)
    zs = _edges([v for r in rects.values() for v in r[2:]], bz0, bz1)

    owned = {k: set() for k in rects}
    orphans = 0
    for i in range(len(xs) - 1):
        cx = (xs[i] + xs[i + 1]) / 2.0
        for j in range(len(zs) - 1):
            cz = (zs[j] + zs[j + 1]) / 2.0
            inside = [k for k, r in rects.items()
                      if r[0] <= cx <= r[1] and r[2] <= cz <= r[3]]
            if inside:
                owner = min(inside, key=lambda k: (areas[k], k))
            else:
                orphans += 1
                owner = min(rects, key=lambda k: (_point_rect_distance(cx, cz, rects[k]), k))
            owned[owner].add((i, j))

    # A cut whose rectangle is completely covered by smaller ones wins no cells
    # at all, and would then appear in the legend with nothing to click. Give it
    # back the cell at its own centre, taken from whichever neighbour can most
    # afford to lose one.
    starved = []
    for k, r in rects.items():
        if owned[k]:
            continue
        cx, cz = (r[0] + r[1]) / 2.0, (r[2] + r[3]) / 2.0
        i = max(n for n in range(len(xs) - 1) if xs[n] <= cx) if cx >= xs[0] else 0
        j = max(n for n in range(len(zs) - 1) if zs[n] <= cz) if cz >= zs[0] else 0
        i, j = min(i, len(xs) - 2), min(j, len(zs) - 2)
        donor = next((d for d in owned if (i, j) in owned[d]), None)
        if donor is None or len(owned[donor]) < 2:
            continue
        owned[donor].discard((i, j))
        owned[k].add((i, j))
        starved.append(k)

    boxes = {k: _merge_cells(v, xs, zs) for k, v in owned.items() if v}
    stats = {
        "starved_cuts_given_their_centre": sorted(starved),
        "grid": (len(xs) - 1, len(zs) - 1),
        "cells": (len(xs) - 1) * (len(zs) - 1),
        "orphan_cells": orphans,
        "boxes": sum(len(v) for v in boxes.values()),
        "cuts_with_no_cells": sorted(k for k in rects if k not in boxes),
    }
    return boxes, stats
