"""Check that every quote in the composition table is actually on the page it cites.

    python tools/verify_quotes.py [us fr uk ...] [--refetch]

The whole table rests on one rule: a cut graded `standard` or `trade` carries verbatim
text from a source. The rule is worth nothing unchecked, and it is very easy to break by
accident -- the fetch tool most of this was researched with runs a summarising model over
the page, which paraphrases, merges adjacent sentences and translates out of the source
language, silently and plausibly. Quotes that were never on the page are the one failure
this table exists to prevent.

So: fetch each cited URL with curl, reduce it to plain text, and require the quote to be
a literal substring after whitespace normalisation. Sources that cannot be fetched live
-- the USDA specifications, the Beef Checkoff table -- are checked against the verbatim
extracts committed alongside the data instead, which is why those extracts exist.

Pages are cached under build/quotecheck/ so a re-run is free; pass --refetch to ignore it.
"""

import glob
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time
from html import unescape
from collections import defaultdict
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "build", "quotecheck")

# Standards no fetcher can reach, and the committed text that stands in for them. These
# are checked against the *whole* extracted document, not the curated excerpt, so a quote
# is verified against everything the source says rather than against what a previous pass
# chose to keep.
LOCAL = (
    ("IMPS_100", "sources/imps100.txt"),
    ("LSimps700", "sources/imps700.txt"),
    ("ams.usda.gov", "sources/imps100.txt"),
    # law.go.kr serves this appendix as page images, never as text.
    ("admRulSeq=2100000184120", "sources/kr-byl3.txt"),
    ("bylSeq=2026095", "sources/kr-byl3.txt"),
    ("paffa.org", "calkins-table.md"),
    ("agrireseau.net", "calkins-table.md"),
)

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")


def norm(s, tight=False):
    """Comparison form: punctuation-normalised, and optionally whitespace-free.

    `tight` exists because stripping HTML leaves spaces where the tags were, and the
    standards like to italicise every Latin muscle name -- so a page that reads
    "le pectineus, l'adductor" comes out of detag() as "le pectineus , l' adductor".
    Dropping whitespace entirely makes the two compare equal. For a quote of any real
    length that cannot produce a false match."""
    s = re.sub(r"[   ]", " ", s)
    s = s.replace("‘", "'").replace("’", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("‐", "-").replace("‑", "-").replace("–", "-")
    s = s.replace("—", "-").replace("−", "-")
    s = re.sub(r"\s+", " ", s).strip()
    return s.replace(" ", "") if tight else s


def detag(html):
    html = re.sub(r"(?is)<(script|style|noscript).*?</>", " ", html)
    html = re.sub(r"(?s)<!--.*?-->", " ", html)
    html = re.sub(r"(?s)<[^>]+>", " ", html)
    # After the tags, the entities: AHDB writes every dash as &ndash; and every elision
    # as &hellip;, so a page left un-unescaped disagrees with its own quotes.
    return unescape(html)


# A refusal is not a short page: a Cloudflare block comes back as a kilobyte of
# challenge script, comfortably over any length threshold, and would otherwise be
# read as "the page exists and the quote is not on it".
BLOCK = ("403 Forbidden", "Access denied", "Just a moment", "challenge-platform",
         "Attention Required", "Request unsuccessful", "429 Too Many Requests")


def blocked(text):
    head = text[:3000]
    return len(text.strip()) < 400 or any(b in head for b in BLOCK)


def fetch(url, refetch=False):
    host = urlparse(url).netloc
    for key, rel in LOCAL:
        if key in url:
            path = os.path.join(ROOT, "data", "composition", rel)
            if os.path.exists(path):
                return io.open(path, encoding="utf-8").read(), "local"
    os.makedirs(CACHE, exist_ok=True)
    dest = os.path.join(CACHE, hashlib.sha1(url.encode()).hexdigest() + ".txt")
    if os.path.exists(dest) and not refetch:
        return io.open(dest, encoding="utf-8", errors="replace").read(), "cache"
    raw = subprocess.run(
        ["curl", "-sL", "--max-time", "45", "-A", UA, url],
        capture_output=True).stdout
    text = None
    for enc in ("utf-8", "windows-1251", "cp1252", "euc-kr", "shift_jis"):
        try:
            cand = raw.decode(enc)
        except (UnicodeDecodeError, LookupError):
            continue
        # windows-1251 pages decode as utf-8 garbage rather than failing; prefer the
        # candidate that produces the fewest replacement-ish sequences.
        if text is None or cand.count("�") < text.count("�"):
            text = cand
        if enc == "utf-8" and "�" not in cand:
            break
    if raw[:5] == b"%PDF-":
        # A PDF stripped of "tags" is binary noise that matches nothing; run the same
        # extractor the research passes used instead.
        tmp = dest[:-4] + ".pdf"
        open(tmp, "wb").write(raw)
        subprocess.run(["pdftotext", "-enc", "UTF-8", tmp, dest], capture_output=True)
        text = io.open(dest, encoding="utf-8", errors="replace").read()             if os.path.exists(dest) else ""
        os.remove(tmp)
        return text, "fetched"
    text = detag(text or "")
    if blocked(text) and "web.archive.org" not in url:
        # Several of these sites answer a scripted request with 403 and a human one with
        # the page. The Wayback Machine is not a second opinion -- it is the same page,
        # captured -- so a quote confirmed there is confirmed. Ask it which capture
        # exists rather than guessing a date, and give it room: it answers 429 to a
        # burst, and a 429 read as an empty page would look like a bad quote.
        snap = ""
        for attempt in range(3):
            time.sleep(6 * attempt)
            probe = subprocess.run(
                ["curl", "-s", "--max-time", "30",
                 "http://archive.org/wayback/available?url=" + url.split("://", 1)[-1]],
                capture_output=True).stdout.decode("utf-8", "replace")
            if "429" in probe[:200]:
                continue
            try:
                closest = json.loads(probe)["archived_snapshots"].get("closest", {})
            except (ValueError, KeyError):
                break
            if not closest.get("url"):
                break
            time.sleep(3)
            snap, _ = fetch(closest["url"], refetch)
            break
        if len(snap.strip()) >= 400:
            text = snap
    io.open(dest, "w", encoding="utf-8").write(text)
    return text, "fetched"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    refetch = "--refetch" in sys.argv
    ids = args or [os.path.basename(f)[5:-5]
                   for f in sorted(glob.glob(os.path.join(ROOT, "data", "cuts_*.json")))]

    last_hit = defaultdict(float)
    total = ok = bad = unreach = 0
    failures = []
    for tid in ids:
        path = os.path.join(ROOT, "data", "composition", f"{tid}.json")
        if not os.path.exists(path):
            continue
        doc = json.load(io.open(path, encoding="utf-8"))
        for cut in doc["cuts"]:
            if cut.get("evidence") not in ("standard", "trade") and \
               cut.get("bounds_evidence") not in ("standard", "trade"):
                continue
            for src in cut.get("sources", []):
                q = (src.get("quote") or "").strip()
                url = src.get("url", "")
                if not q or not url:
                    continue
                total += 1
                host = urlparse(url).netloc
                wait = 3.0 - (time.time() - last_hit[host])
                if wait > 0 and not any(k in url for k, _ in LOCAL):
                    time.sleep(wait)
                page, how = fetch(url, refetch)
                last_hit[host] = time.time()
                if how != "local" and blocked(page):
                    unreach += 1
                    failures.append((tid, cut["id"], "UNREACHABLE", url, q[:70]))
                    continue
                # A quote may elide with an ellipsis; each side must then be on the page.
                parts = [f for f in re.split(r"\s*(?:…|\.\.\.)\s*", q) if len(f) > 12]
                if all(norm(f, tight=True) in norm(page, tight=True) for f in parts or [q]):
                    ok += 1
                else:
                    bad += 1
                    failures.append((tid, cut["id"], "NOT ON PAGE", url, q[:70]))
        print(f"  {tid}: checked", flush=True)

    print(f"\n{ok}/{total} quotes verified as literal substrings "
          f"({bad} not on the page, {unreach} pages unreachable)")
    for tid, cid, why, url, q in failures:
        print(f"  [{why}] {tid}/{cid}\n      {url}\n      {q}…")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
