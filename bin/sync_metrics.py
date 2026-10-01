#!/usr/bin/env python3
"""Generate _data/metrics.yml for the research-output charts.

Papers come from _data/publications.yml (itself generated from the CV by
sync_publications.py); citations come from OpenAlex, looked up by ORCID. Run
this after bin/sync_publications.py so the two stay in step:

    bin/sync_metrics.py
"""

import argparse
import datetime
import json
import pathlib
import re
import sys
import urllib.error
import urllib.request

import yaml

# OpenAlex has split the author identity across several records, and the ORCID
# endpoint resolves to a stub holding only three papers. So the works are pulled
# by explicit author id instead. Re-check this list with
#   https://api.openalex.org/authors?search=LaBollita
# after a sync looks light; "H. A. Labollita" (A5070896130) is a limnologist and
# is deliberately not in it.
AUTHOR_IDS = [
    "A5005667161",  # Harrison LaBollita, the main record
    "A5135665981",  # stub the ORCID resolves to
    "A5014780762",  # "H. LaBollita"
    "A5130913286",  # "H. LaBollita"
]

# OpenAlex asks for a contact address to put the request in its polite pool.
MAILTO = "harrisonlabollita@gmail.com"


def papers_by_year(publications):
    """Count published papers and preprints per year.

    A record with no journal URL is still under review, so it counts as a
    preprint. Records whose CV reference carries no year fall back to the year
    encoded in the arXiv identifier (2606.26243 -> 2026).
    """
    published, preprints = {}, {}

    for record in publications:
        year = record.get("year")
        if year is None:
            arxiv = record.get("arxiv") or ""
            match = re.search(r"/(\d{2})(\d{2})\.", arxiv)
            if not match:
                print(f"  ! entry {record['number']}: no year and no arXiv id, skipped",
                      file=sys.stderr)
                continue
            year = 2000 + int(match.group(1))
            if record.get("url"):
                print(f"  ! entry {record['number']}: published but the CV reference "
                      f"has no year; using the arXiv year {year}", file=sys.stderr)

        bucket = published if record.get("url") else preprints
        bucket[year] = bucket.get(year, 0) + 1

    return published, preprints


def fetch_works(author_ids):
    """Every OpenAlex work by those authors, deduplicated by work id.

    The author records overlap, so the same paper can come back more than once.
    """
    works, cursor = {}, "*"
    base = ("https://api.openalex.org/works"
            f"?filter=author.id:{'|'.join(author_ids)}"
            "&select=id,cited_by_count,counts_by_year&per-page=200"
            f"&mailto={MAILTO}")

    while cursor:
        try:
            with urllib.request.urlopen(f"{base}&cursor={cursor}", timeout=60) as response:
                payload = json.load(response)
        except (urllib.error.URLError, TimeoutError) as error:
            sys.exit(f"could not reach OpenAlex: {error}")

        for work in payload["results"]:
            works[work["id"]] = work
        cursor = payload["meta"].get("next_cursor")

    if not works:
        sys.exit(f"OpenAlex returned no works for {', '.join(author_ids)}")

    return list(works.values())


def citation_metrics(works):
    """Return (citations per year, lifetime citations, h-index)."""
    per_year = {}
    for work in works:
        for entry in work["counts_by_year"]:
            per_year[entry["year"]] = per_year.get(entry["year"], 0) + entry["cited_by_count"]

    counts = sorted((work["cited_by_count"] for work in works), reverse=True)
    h_index = sum(1 for rank, count in enumerate(counts, 1) if count >= rank)

    return per_year, sum(counts), h_index


def build_rows(published, preprints, citations):
    """One row per year, gaps filled with zeros, with running totals."""
    years = set(published) | set(preprints) | set(citations)
    if not years:
        sys.exit("no data to chart")

    rows = []
    papers_cum = preprints_cum = citations_cum = 0

    for year in range(min(years), max(years) + 1):
        papers_cum += published.get(year, 0)
        preprints_cum += preprints.get(year, 0)
        citations_cum += citations.get(year, 0)
        rows.append({
            "year": year,
            "papers": published.get(year, 0),
            "preprints": preprints.get(year, 0),
            "papers_cum": papers_cum,
            "preprints_cum": preprints_cum,
            "citations": citations.get(year, 0),
            "citations_cum": citations_cum,
        })

    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-p", "--publications", type=pathlib.Path,
                        default=pathlib.Path("_data/publications.yml"))
    parser.add_argument("-o", "--output", type=pathlib.Path,
                        default=pathlib.Path("_data/metrics.yml"))
    parser.add_argument("--authors", nargs="+", default=AUTHOR_IDS,
                        help="OpenAlex author ids to merge")
    args = parser.parse_args()

    publications = yaml.safe_load(args.publications.read_text(encoding="utf-8"))
    published, preprints = papers_by_year(publications)
    works = fetch_works(args.authors)
    citations, citations_total, h_index = citation_metrics(works)
    rows = build_rows(published, preprints, citations)

    lines = [
        "# Generated by bin/sync_metrics.py. Do not hand-edit.",
        f"# Papers: {args.publications}. Citations: OpenAlex ({', '.join(args.authors)}).",
        "",
        f"updated: {datetime.date.today().isoformat()}",
        f"citations_total: {citations_total}",
        f"h_index: {h_index}",
        "years:",
    ]
    for row in rows:
        lines.append(f"  - year: {row['year']}")
        for field in ("papers", "preprints", "papers_cum", "preprints_cum",
                      "citations", "citations_cum"):
            lines.append(f"    {field}: {row[field]}")
    lines.append("")

    args.output.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {len(rows)} years to {args.output} "
          f"({citations_total} citations, h-index {h_index})")


if __name__ == "__main__":
    main()
