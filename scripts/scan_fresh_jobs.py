#!/usr/bin/env python3
"""
Scan Fresh Jobs Script
Queries verified corporate ATS boards (Greenhouse, Lever) for active engineering & security roles.
"""

import sys
import json
import urllib.request
import re

DEFAULT_BOARDS = [
    "coinbase", "affirm", "beyondfinance", "cloudflare", "datadog",
    "elastic", "newrelic", "okta", "pax8", "stripe", "twilio", "mongodb"
]

KEYWORDS = ["iam", "identity", "cloud security", "security engineer", "access management", "ciam"]

def check_greenhouse(board_name):
    url = f"https://api.greenhouse.io/v1/boards/{board_name}/jobs"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    matches = []
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())
            for job in data.get("jobs", []):
                title = job.get("title", "")
                title_lower = title.lower()
                if any(kw in title_lower for kw in KEYWORDS):
                    loc = job.get("location", {}).get("name", "Unknown")
                    matches.append({
                        "company": board_name.capitalize(),
                        "title": title,
                        "location": loc,
                        "url": job.get("absolute_url"),
                        "id": job.get("id"),
                        "portal": "Greenhouse"
                    })
    except Exception:
        pass
    return matches

def main():
    target_count = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    results = []
    for board in DEFAULT_BOARDS:
        matches = check_greenhouse(board)
        results.extend(matches)
        if len(results) >= target_count * 2:
            break

    print(json.dumps(results[:target_count], indent=2))

if __name__ == "__main__":
    main()
