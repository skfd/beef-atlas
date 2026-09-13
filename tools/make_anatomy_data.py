"""Fold the anatomy research files into the single file the web page fetches.

Same shape as make_web_data.py, and the same reason: the page should make one fetch
and read prose that can be corrected without rebuilding a cow.

The one thing this adds is where each part *actually ended up*. The panel text is
authored; the geometry is not trusted to match it. build_anatomy.py measures the
bounding box of every part after it has been carved and clipped and writes it into
build/anatomy_report.json, and that measurement is what the page uses to line a
muscle up against the cut rectangles. An authored "this is in the short loin" would
be a second copy of the truth, free to drift from the model the moment either moved.
"""

import io
import json
import os

SYSTEMS = ("skeleton", "muscle", "viscera")

# Mirrors anatomy.SYSTEM_COLOUR. A part that authored no colour still needs one in
# the legend swatch, and a row of identical red dots against the bones would be a
# lie about which system you are looking at.
FALLBACK = {"skeleton": "#e5ded0", "muscle": "#9a2b27", "viscera": "#af6768"}


def write(root):
    measured = {}
    report = os.path.join(root, "build", "anatomy_report.json")
    if os.path.exists(report):
        for r in json.load(io.open(report, encoding="utf-8")).get("detail", []):
            measured[r["id"]] = r

    parts, missing = [], []
    for system in SYSTEMS:
        path = os.path.join(root, "data", "anatomy", f"{system}.json")
        if not os.path.exists(path):
            continue
        doc = json.load(io.open(path, encoding="utf-8"))
        for part in doc["parts"]:
            m = measured.get(part["id"])
            if not m:
                # In the data but not in the model: the page must not offer a
                # legend entry that highlights nothing.
                missing.append(part["id"])
                continue
            lo, hi = m["bbox"]
            parts.append({
                "id": part["id"],
                "name": part.get("name", part["id"]),
                "latin": part.get("latin", ""),
                "system": part.get("system", system),
                "group": part.get("group", ""),
                "depth": int(part.get("depth", 0)),
                "colour": part.get("colour") or FALLBACK.get(
                    part.get("system", system), "#9a2b27"),
                "blurb": part.get("blurb", ""),
                "beef": part.get("beef", ""),
                "x": [lo[0], hi[0]],
                "y": [lo[1], hi[1]],
                "z": [lo[2], hi[2]],
                "faces": m["faces"],
            })

    out = {"parts": parts, "missing": missing,
           "sources": sorted({u for system in SYSTEMS
                              for u in _sources(root, system)})}
    out_dir = os.path.join(root, "web", "data")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "anatomy.json")
    io.open(dest, "w", encoding="utf-8").write(
        json.dumps(out, indent=1, ensure_ascii=False))
    return dest, out


def _sources(root, system):
    path = os.path.join(root, "data", "anatomy", f"{system}.json")
    if not os.path.exists(path):
        return []
    return json.load(io.open(path, encoding="utf-8")).get("sources", [])


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dest, out = write(root)
    by_system = {}
    for p in out["parts"]:
        by_system[p["system"]] = by_system.get(p["system"], 0) + 1
    print(f"wrote {dest}: {len(out['parts'])} parts " +
          ", ".join(f"{k} {v}" for k, v in sorted(by_system.items())))
    if out["missing"]:
        print("  not in the model: " + ", ".join(out["missing"]))
