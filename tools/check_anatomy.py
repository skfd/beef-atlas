"""Validate the anatomy data before Blender gets anywhere near it.

    python tools/check_anatomy.py

Blender takes tens of seconds to fail on a typo and reports it as a Python traceback
from inside a modifier. Everything checkable without a mesh is checked here instead:
the fields the page reads, the arguments each primitive takes, and whether the numbers
land inside the frame at all. The one thing this cannot check is whether a part is in
the *right* place -- that is what the cutaway renders and the `outside` figure in the
build are for.
"""

import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYSTEMS = ("skeleton", "muscle", "viscera")

# `system` is not required: load_specs fills it in from the filename.
REQUIRED = ("id", "name", "shape")
PRIMITIVES = {
    "tube": {"need": ("pts", "r"), "allow": ("flat", "ref", "seg", "samples", "cap", "name")},
    "fusiform": {"need": ("a", "b", "w"),
                 "allow": ("d", "bow", "ends", "bulge", "ref", "seg", "name")},
    "plate": {"need": ("poly", "y", "thick"), "allow": ("dome", "name")},
    "blob": {"need": ("lumps",), "allow": ("voxel", "smooth", "name")},
}

# Generous: a box round the animal plus room for a horn tip and a hoof. A number
# outside this is a typo, not a modelling choice.
BOUNDS = ((-0.08, 1.10), (-0.42, 0.42), (-0.05, 1.06))


def check_point(where, p, problems):
    if not isinstance(p, (list, tuple)) or len(p) < 3:
        problems.append(f"{where}: expected three numbers, got {p!r}")
        return
    for i in range(3):
        lo, hi = BOUNDS[i]
        if not isinstance(p[i], (int, float)):
            problems.append(f"{where}: {p[i]!r} is not a number")
        elif not (lo <= p[i] <= hi):
            problems.append(f"{where}: {'xyz'[i]}={p[i]} is outside the frame "
                            f"({lo}..{hi})")


def check_part(part, problems, seen):
    pid = part.get("id", "<no id>")
    for field in REQUIRED:
        if field not in part:
            problems.append(f"{pid}: missing {field!r}")
    if pid in seen:
        problems.append(f"{pid}: duplicate id")
    seen.add(pid)
    if not part.get("blurb"):
        problems.append(f"{pid}: no blurb -- the panel would show an empty paragraph")
    depth = part.get("depth", 0)
    if depth not in (0, 1, 2):
        problems.append(f"{pid}: depth {depth!r} is not 0, 1 or 2")
    colour = part.get("colour", "")
    if colour and not (colour.startswith("#") and len(colour) == 7):
        problems.append(f"{pid}: colour {colour!r} is not #rrggbb")

    for n, shape in enumerate(part.get("shape", [])):
        where = f"{pid} shape[{n}]"
        kind = shape.get("t")
        spec = PRIMITIVES.get(kind)
        if spec is None:
            problems.append(f"{where}: unknown primitive {kind!r}")
            continue
        for field in spec["need"]:
            if field not in shape:
                problems.append(f"{where}: {kind} needs {field!r}")
        for field in shape:
            if field != "t" and field not in spec["need"] and field not in spec["allow"]:
                problems.append(f"{where}: {kind} has no argument {field!r}")

        if kind == "tube" and "pts" in shape:
            pts = shape["pts"]
            if len(pts) < 2:
                problems.append(f"{where}: a tube needs at least two points")
            for i, p in enumerate(pts):
                check_point(f"{where} pts[{i}]", p, problems)
            r = shape.get("r")
            if isinstance(r, list) and len(r) != len(pts):
                problems.append(f"{where}: {len(r)} radii for {len(pts)} points")
        if kind == "fusiform":
            for field in ("a", "b"):
                if field in shape:
                    check_point(f"{where} {field}", shape[field], problems)
            for field in ("w", "d"):
                if field in shape and not (0 < shape[field] < 0.5):
                    problems.append(f"{where}: {field}={shape[field]} is not a "
                                    f"plausible half-width")
        if kind == "plate" and "poly" in shape:
            if len(shape["poly"]) < 3:
                problems.append(f"{where}: a plate needs at least three points")
            for i, p in enumerate(shape["poly"]):
                if not isinstance(p, (list, tuple)) or len(p) != 2:
                    problems.append(f"{where} poly[{i}]: expected an (x, z) pair")
                    continue
                check_point(f"{where} poly[{i}]", [p[0], 0.0, p[1]], problems)
        if kind == "blob":
            for i, lump in enumerate(shape.get("lumps", [])):
                if len(lump) not in (6, 9):
                    problems.append(f"{where} lumps[{i}]: expected 6 or 9 numbers, "
                                    f"got {len(lump)}")
                    continue
                check_point(f"{where} lumps[{i}] centre", lump[:3], problems)
                if any(r <= 0 for r in lump[3:6]):
                    problems.append(f"{where} lumps[{i}]: a radius is zero or negative")


def main():
    problems, seen, counts = [], set(), {}
    for system in SYSTEMS:
        path = os.path.join(ROOT, "data", "anatomy", f"{system}.json")
        if not os.path.exists(path):
            problems.append(f"{system}.json is missing")
            continue
        try:
            doc = json.load(io.open(path, encoding="utf-8"))
        except json.JSONDecodeError as e:
            problems.append(f"{system}.json is not valid JSON: {e}")
            continue
        if not doc.get("sources"):
            problems.append(f"{system}.json has no sources")
        parts = doc.get("parts", [])
        counts[system] = len(parts)
        for part in parts:
            if part.get("system", system) != system:
                problems.append(f"{part.get('id')}: system {part['system']!r} "
                                f"in {system}.json")
            part.setdefault("system", system)
            check_part(part, problems, seen)

    print(", ".join(f"{k} {v}" for k, v in sorted(counts.items())) +
          f" = {sum(counts.values())} parts")
    for p in problems:
        print("  " + p)
    print("OK" if not problems else f"{len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
