#!/usr/bin/env python3
"""
Scan Fresh Jobs Script
Queries public Greenhouse job boards for active roles whose titles match keywords.

Usage:
    python3 scan_fresh_jobs.py [count] [--keywords "a,b"] [--boards "x,y"]
"""

import argparse
import json
import sys
import urllib.request

DEFAULT_BOARDS = [
    "coinbase", "affirm", "beyondfinance", "cloudflare", "datadog",
    "elastic", "newrelic", "okta", "pax8", "stripe", "twilio", "mongodb"
]

DEFAULT_KEYWORDS = ["iam", "identity", "cloud security", "security engineer", "access management", "ciam"]


def split_csv(value):
    return [item.strip() for item in value.split(",") if item.strip()]


def check_greenhouse(board_name, keywords):
    url = f"https://api.greenhouse.io/v1/boards/{board_name}/jobs"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    matches = []
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode())
    for job in data.get("jobs", []):
        title = job.get("title", "")
        title_lower = title.lower()
        if any(kw in title_lower for kw in keywords):
            loc = job.get("location", {}).get("name", "Unknown")
            matches.append({
                "company": board_name.capitalize(),
                "title": title,
                "location": loc,
                "url": job.get("absolute_url"),
                "id": job.get("id"),
                "updated_at": job.get("updated_at"),
                "portal": "Greenhouse"
            })
    return matches


def main():
    parser = argparse.ArgumentParser(description="Scan Greenhouse boards for matching job titles.")
    parser.add_argument("count", nargs="?", type=int, default=10, help="max results to print (default 10)")
    parser.add_argument("--keywords", help="comma-separated title keywords (case-insensitive)")
    parser.add_argument("--boards", help="comma-separated Greenhouse board tokens")
    args = parser.parse_args()

    keywords = [kw.lower() for kw in split_csv(args.keywords)] if args.keywords else DEFAULT_KEYWORDS
    boards = split_csv(args.boards) if args.boards else DEFAULT_BOARDS

    results = []
    failed = []
    for board in boards:
        try:
            results.extend(check_greenhouse(board, keywords))
        except Exception as exc:
            failed.append(f"{board}: {exc}")
        if len(results) >= args.count * 2:
            break

    if failed:
        print("Boards that could not be scanned:\n  " + "\n  ".join(failed), file=sys.stderr)

    print(json.dumps(results[:args.count], indent=2))


if __name__ == "__main__":
    main()
