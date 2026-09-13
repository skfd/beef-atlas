"""Fold the per-culture research files into the single file the web page fetches.

Runs under plain Python -- no Blender -- so the legend can be regenerated after a
wording fix without re-carving six cow models. The colours come from
blender/cuts.py, the same function that built the GLB materials.
"""

import glob
import io
import json
import os
import sys


def write(root):
    sys.path.insert(0, os.path.join(root, "blender"))
    import cuts as cutsmod

    # Anything the carve could not produce geometry for -- a rectangle that
    # clips away to nothing against the silhouette -- is marked, so the legend
    # can say so instead of offering an entry that highlights nothing.
    missing = {}
    report = os.path.join(root, "build", "build_report.json")
    if os.path.exists(report):
        for r in json.load(io.open(report, encoding="utf-8")):
            missing[r["culture"]] = set(r.get("missing", []))

    specs = []
    for f in sorted(glob.glob(os.path.join(root, "data", "cuts_*.json"))):
        spec = json.load(io.open(f, encoding="utf-8"))
        absent = missing.get(spec["id"], set())
        for idx, colour in enumerate(cutsmod.palette(len(spec["cuts"]))):
            spec["cuts"][idx]["colour"] = cutsmod.hex_colour(colour)
            if spec["cuts"][idx]["id"] in absent:
                spec["cuts"][idx]["absent"] = True
        specs.append(spec)

    # Biggest schemes last: the page opens on the first one, and the US primals
    # are the gentlest introduction to what the atlas is showing.
    order = {"us": 0, "uk": 1, "fr": 2, "br": 3, "kr": 4, "jp": 5}
    specs.sort(key=lambda s: order.get(s["id"], 99))

    out_dir = os.path.join(root, "web", "data")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "cultures.json")
    io.open(path, "w", encoding="utf-8").write(json.dumps(specs, indent=1, ensure_ascii=False))
    return path, specs


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path, specs = write(root)
    print(f"wrote {path}: {len(specs)} cultures, "
          f"{sum(len(s['cuts']) for s in specs)} cuts")
