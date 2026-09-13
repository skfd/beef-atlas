"""Check every data/cuts_*.json before it is carved.

    python tools/check_data.py

The research files are hand-authored, one per tradition, and a bad one fails
late and quietly: a missing key throws inside Blender twenty minutes into a
build, and a rectangle outside the silhouette carves to nothing and simply
disappears from the model. This catches all of that in a second.

Overlapping rectangles are reported but are not an error -- blender/cuts.py
resolves them deliberately, giving a contested cell to the smaller rectangle so
a named subcut wins against the primal it sits inside.
"""

import glob
import io
import json
import os
import sys

REQUIRED = ["id", "name", "native", "region", "x", "z", "full_width",
            "description", "dishes"]

# Where the mesh actually is, from blender/cow.py's PROFILE. A rectangle wholly
# outside this has nothing to carve against.
MESH_X = (-0.01, 0.99)
MESH_Z = (0.00, 0.94)


def check_file(path):
    problems, notes = [], []
    name = os.path.basename(path)
    try:
        spec = json.load(io.open(path, encoding="utf-8"))
    except Exception as e:
        return [f"{name}: will not parse: {e}"], []

    for key in ("culture", "id", "blurb", "cuts"):
        if not spec.get(key):
            problems.append(f"{name}: missing top-level '{key}'")
    cuts = spec.get("cuts") or []

    seen = set()
    for cut in cuts:
        cid = cut.get("id", "<no id>")
        for key in REQUIRED:
            if key not in cut:
                problems.append(f"{name}/{cid}: missing '{key}'")
        if cid in seen:
            problems.append(f"{name}: duplicate id '{cid}'")
        seen.add(cid)

        for axis, span, mesh in (("x", cut.get("x"), MESH_X), ("z", cut.get("z"), MESH_Z)):
            if not (isinstance(span, list) and len(span) == 2):
                problems.append(f"{name}/{cid}: {axis} is not a pair")
                continue
            lo, hi = sorted(span)
            if hi - lo < 1e-4:
                problems.append(f"{name}/{cid}: {axis} span is empty ({span})")
            if hi <= mesh[0] or lo >= mesh[1]:
                problems.append(f"{name}/{cid}: {axis} {span} is entirely off the mesh "
                                f"({mesh[0]}..{mesh[1]}) and would carve to nothing")

    overlaps = 0
    for i, a in enumerate(cuts):
        for b in cuts[i + 1:]:
            try:
                ox = min(max(a["x"]), max(b["x"])) - max(min(a["x"]), min(b["x"]))
                oz = min(max(a["z"]), max(b["z"])) - max(min(a["z"]), min(b["z"]))
            except Exception:
                continue
            if ox > 1e-6 and oz > 1e-6:
                overlaps += 1
    if overlaps:
        notes.append(f"{name}: {overlaps} overlapping rectangle pair(s) "
                     f"-- resolved by the partition, smallest wins")

    notes.append(f"{name}: {len(cuts)} cuts, {len(spec.get('sources') or [])} sources")
    return problems, notes


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    files = sorted(glob.glob(os.path.join(root, "data", "cuts_*.json")))
    if not files:
        print("no data/cuts_*.json found")
        return 1
    all_problems = []
    for f in files:
        problems, notes = check_file(f)
        all_problems += problems
        for n in notes:
            print("  " + n)
    if all_problems:
        print("\nPROBLEMS")
        for p in all_problems:
            print("  " + p)
        return 1
    print("\nall data files OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
