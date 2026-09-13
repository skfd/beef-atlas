"""Validate the cut composition table, and report how much of it is actually sourced.

    python tools/check_composition.py [--verbose]

The table claims, for each of the 153 cuts, which muscles it contains and where along
them it starts and stops. Two kinds of thing can go wrong. One is mechanical: a muscle
id that is not in the model, a boundary naming a bone that does not exist, a `portion`
with nothing saying where it stops. The other is the one that matters -- an entry that
asserts a muscle with nothing behind it. So `standard` and `trade` grades are required
to carry a verbatim quote, `inferred` and `contested` to say what the reasoning or the
disagreement was, and the coverage table at the end is the real output: it is what
decides whether a tradition can be rebuilt on muscles or has to stay rectangles.
"""

import glob
import io
import json
import os
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GRADES = ("standard", "trade", "inferred", "contested")
ROLES = ("defining", "major", "minor", "trace")
EXTENTS = ("whole", "portion")
# A boundary is a bone, a seam with the neighbouring muscle, or the muscle's own end.
LITERAL_BOUNDS = ("seam", "origin", "insertion")


def ids_of(path, key="parts"):
    return {p["id"] for p in json.load(io.open(path, encoding="utf-8"))[key]}


def check_cut(cut, muscles, bones, problems, where):
    cid = cut.get("id", "<no id>")
    tag = f"{where}/{cid}"

    grade = cut.get("evidence")
    if grade not in GRADES:
        problems.append(f"{tag}: evidence {grade!r} is not one of {GRADES}")
    bgrade = cut.get("bounds_evidence")
    if bgrade is not None and bgrade not in GRADES:
        problems.append(f"{tag}: bounds_evidence {bgrade!r} is not one of {GRADES}")
    if not isinstance(cut.get("bone_in"), bool):
        problems.append(f"{tag}: bone_in must be true or false")

    entries = cut.get("muscles", [])
    if not isinstance(entries, list):
        problems.append(f"{tag}: muscles must be a list")
        entries = []
    for m in entries:
        mid = m.get("id")
        if mid not in muscles:
            problems.append(f"{tag}: {mid!r} is not a modelled muscle "
                            f"(put it in `unmodelled`)")
        if m.get("role") not in ROLES:
            problems.append(f"{tag}: {mid} role {m.get('role')!r} is not one of {ROLES}")
        extent = m.get("extent")
        if extent not in EXTENTS:
            problems.append(f"{tag}: {mid} extent {extent!r} is not one of {EXTENTS}")
        for end in ("from", "to"):
            v = m.get(end)
            if extent == "portion" and v is None:
                problems.append(f"{tag}: {mid} is a portion but has no {end!r} -- "
                                f"a muscle shared with the next cut needs both ends")
            elif extent == "whole" and v is not None:
                problems.append(f"{tag}: {mid} takes the whole muscle but names a {end}")
            elif v is not None and v not in bones and v not in LITERAL_BOUNDS:
                problems.append(f"{tag}: {mid} {end}={v!r} is neither a bone in the "
                                f"model nor one of {LITERAL_BOUNDS}")

    for u in cut.get("unmodelled", []):
        if not u.get("latin"):
            problems.append(f"{tag}: an unmodelled entry has no latin name")
        if not u.get("where"):
            problems.append(f"{tag}: unmodelled {u.get('latin')!r} has no `where` -- "
                            f"that line is the spec for adding it to the model")

    sources = cut.get("sources", [])
    quoted = [s for s in sources if (s.get("quote") or "").strip()]
    # A source marked `unverified` is one tools/verify_quotes.py could not check against
    # the page -- blocked at the origin and absent from the Wayback Machine. It may well
    # be right, but a grade resting only on unre-readable text is exactly the thing this
    # table promises not to do, so it does not count towards one.
    checkable = [s for s in quoted if not s.get("unverified")]
    if grade in ("standard", "trade"):
        if not quoted:
            problems.append(f"{tag}: graded {grade} with no verbatim quote behind it")
        elif not checkable:
            problems.append(f"{tag}: graded {grade} only on sources that cannot be "
                            f"re-read -- run tools/verify_quotes.py")
        for s in sources:
            if not s.get("url"):
                problems.append(f"{tag}: a source has a quote but no url")
    if grade == "inferred" and not (cut.get("dispute") or "").strip():
        problems.append(f"{tag}: inferred, but `dispute` does not say from what")
    if grade == "contested":
        if not (cut.get("dispute") or "").strip():
            problems.append(f"{tag}: contested, but `dispute` does not say by whom")
        if len(sources) < 2:
            problems.append(f"{tag}: contested with {len(sources)} source(s) -- "
                            f"a disagreement needs both sides")
    if grade in ("standard", "trade") and not entries and not cut.get("unmodelled"):
        problems.append(f"{tag}: graded {grade} but names no muscle at all")


def main():
    verbose = "--verbose" in sys.argv
    muscles = ids_of(os.path.join(ROOT, "data", "anatomy", "muscle.json"))
    bones = ids_of(os.path.join(ROOT, "data", "anatomy", "skeleton.json"))

    problems = []
    rows, unmodelled = [], Counter()
    for cuts_path in sorted(glob.glob(os.path.join(ROOT, "data", "cuts_*.json"))):
        spec = json.load(io.open(cuts_path, encoding="utf-8"))
        want = [c["id"] for c in spec["cuts"]]
        comp_path = os.path.join(ROOT, "data", "composition", f"{spec['id']}.json")
        if not os.path.exists(comp_path):
            rows.append((spec["culture"], len(want), None, None))
            continue
        doc = json.load(io.open(comp_path, encoding="utf-8"))
        got = [c.get("id") for c in doc.get("cuts", [])]

        for cid in want:
            if got.count(cid) == 0:
                problems.append(f"{spec['id']}: {cid} is in the cut data and not here")
            elif got.count(cid) > 1:
                problems.append(f"{spec['id']}: {cid} appears {got.count(cid)} times")
        for cid in set(got) - set(want):
            problems.append(f"{spec['id']}: {cid!r} is not a cut in cuts_{spec['id']}.json")

        for cut in doc.get("cuts", []):
            check_cut(cut, muscles, bones, problems, spec["id"])
            for u in cut.get("unmodelled", []):
                unmodelled[u.get("latin", "?")] += 1

        ev = Counter(c.get("evidence") for c in doc["cuts"])
        bev = Counter(c.get("bounds_evidence") for c in doc["cuts"])
        rows.append((spec["culture"], len(want), ev, bev))

    print(f"{'tradition':<18}{'cuts':>5}  {'muscles: std/trade/inf/cont':<30}"
          f"{'bounds: std/trade/inf/cont':<30}")
    done = 0
    for culture, n, ev, bev in rows:
        if ev is None:
            print(f"{culture:<18}{n:>5}  {'-- not started --':<30}")
            continue
        done += 1
        f = lambda c: "/".join(str(c.get(g, 0)) for g in GRADES)  # noqa: E731
        sourced = ev.get("standard", 0) + ev.get("trade", 0)
        print(f"{culture:<18}{n:>5}  {f(ev):<12}{sourced * 100 // max(n, 1):>3}% sourced"
              f"{'':<4}{f(bev):<30}")

    if unmodelled:
        print("\nmuscles the table wants that the model does not have:")
        for latin, count in unmodelled.most_common(12):
            print(f"  {count:>3} cuts  {latin}")

    if verbose or problems:
        print()
        for p in problems[:60]:
            print("  " + p)
        if len(problems) > 60:
            print(f"  … and {len(problems) - 60} more")
    print(f"\n{len(rows) - done} of {len(rows)} traditions not started"
          if done < len(rows) else "")
    print("OK" if not problems else f"{len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
