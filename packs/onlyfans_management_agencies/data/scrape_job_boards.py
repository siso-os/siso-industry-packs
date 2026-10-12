#!/usr/bin/env python3
"""
Enhanced job board scraping for OFM agencies.
Fetches HTML and extracts employer/company names from job listings.
"""

import json
import subprocess
import time
import re
from urllib.parse import quote

def fetch_url(url, timeout=10):
    """Fetch URL using curl."""
    try:
        result = subprocess.run(
            ["curl", "-s", "-L", "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
             "--max-time", str(timeout), url],
            capture_output=True,
            text=True,
            timeout=timeout + 2
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout
        return None
    except Exception as e:
        return None

def scrape_sirency_jobs():
    """Scrape Sirency OnlyFans Manager Jobs page."""
    employers = {}
    url = "https://www.sirency.com/onlyfans-manager-jobs"

    print("  Scraping Sirency jobs page...", flush=True)
    html = fetch_url(url, timeout=15)

    if html is None or not html.strip():
        return employers

    # Look for job listings with company/agency info
    # Sirency job board should have job cards with company info

    # Pattern 1: job listings that have company names in job cards
    job_pattern = r'<div[^>]*class="[^"]*job[^"]*"[^>]*>([^<]*<[^>]*>)*?([A-Z][A-Za-z\s&,\.]+?)(?:\s*<|(?:Job|Position|Opportunity))'

    # Pattern 2: company names in links that point to company pages
    company_pattern = r'<a[^>]*href="[^"]*company[^"]*"[^>]*>([A-Z][^<]{2,100})</a>'

    for match in re.finditer(company_pattern, html):
        company = match.group(1).strip()
        # Filter out common non-company text
        if (company and
            len(company) > 3 and
            not any(x in company.lower() for x in ["click", "view", "more", "apply", "contact", "social"])):
            employers[company] = employers.get(company, 0) + 1

    # Also look for company names in specific markup patterns
    # Look for text between job title and "Apply" or similar CTAs
    detailed_pattern = r'<h[2-3][^>]*>([^<]+)</h[2-3]>\s*<p[^>]*>([^<]+)</p>'
    for match in re.finditer(detailed_pattern, html):
        title = match.group(1).strip()
        company = match.group(2).strip()

        if (company and
            len(company) > 3 and
            not any(x in company.lower() for x in ["job", "onlyfans", "chatter"]) and
            not any(x in title.lower() for x in ["apply", "view all"])):
            employers[company] = employers.get(company, 0) + 1

    return employers

def scrape_indeed_onlyfans():
    """Scrape Indeed for OnlyFans jobs."""
    employers = {}

    print("  Scraping Indeed for OnlyFans jobs...", flush=True)

    for location in ["", "&l=United+Kingdom", "&l=United+States"]:
        url = f"https://www.indeed.com/jobs?q=onlyfans{location}"
        html = fetch_url(url, timeout=15)

        if html is None or not html.strip():
            continue

        # Extract job listing sections
        # Indeed uses specific classes for company names
        company_patterns = [
            r'<span[^>]*data-company-name="([^"]+)"',
            r'<a[^>]*class="[^"]*company[^"]*"[^>]*>([^<]+)</a>',
            r'<div[^>]*data-testid="company-name"[^>]*>([^<]+)</div>',
            r'<span[^>]*class="[^"]*companyName[^"]*"[^>]*>([^<]+)</span>'
        ]

        for pattern in company_patterns:
            for match in re.finditer(pattern, html):
                company = match.group(1).strip()
                if company and len(company) > 2:
                    employers[company] = employers.get(company, 0) + 1

        time.sleep(1)

    return employers

def scrape_jooble_onlyfans():
    """Scrape Jooble for OnlyFans positions."""
    employers = {}

    print("  Scraping Jooble for OnlyFans positions...", flush=True)

    url = "https://jooble.org/jobs-onlyfans"
    html = fetch_url(url, timeout=15)

    if html is None or not html.strip():
        return employers

    # Jooble job card patterns
    patterns = [
        r'<a[^>]*class="[^"]*company[^"]*"[^>]*title="([^"]+)"',
        r'<span[^>]*class="[^"]*company[^"]*"[^>]*>([^<]+)</span>',
        r'<div[^>]*class="[^"]*company-link[^"]*"[^>]*>([^<]+)</div>'
    ]

    for pattern in patterns:
        for match in re.finditer(pattern, html):
            company = match.group(1).strip()
            if company and len(company) > 2:
                employers[company] = employers.get(company, 0) + 1

    return employers

def scrape_onlinejobs_ph_ofm():
    """Scrape OnlineJobs.ph for OnlyFans/OFM positions."""
    employers = {}

    print("  Scraping OnlineJobs.ph for OFM roles...", flush=True)

    keywords = [
        "OnlyFans manager",
        "OnlyFans chatter",
        "OnlyFans account manager",
        "content creator management",
        "OFM manager"
    ]

    for kw in keywords:
        url = f"https://www.onlinejobs.ph/jobseekers/jobsearch?jobkeyword={quote(kw)}"
        html = fetch_url(url, timeout=15)

        if html is None or not html.strip():
            continue

        # OnlineJobs.ph employer listing patterns
        patterns = [
            r'<h3[^>]*class="[^"]*employer[^"]*"[^>]*>([^<]+)</h3>',
            r'<div[^>]*class="[^"]*company-name[^"]*"[^>]*>([^<]+)</div>',
            r'<span[^>]*data-employer="([^"]+)"'
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, html):
                employer = match.group(1).strip()
                if employer and len(employer) > 2:
                    employers[employer] = employers.get(employer, 0) + 1

        time.sleep(0.5)

    return employers

def scrape_swooped():
    """Scrape Swooped job board."""
    employers = {}

    print("  Scraping Swooped for OFM jobs...", flush=True)

    url = "https://swooped.co/jobs?keywords=OnlyFans"
    html = fetch_url(url, timeout=15)

    if html is None or not html.strip():
        return employers

    # Swooped patterns for employer/company info
    patterns = [
        r'<div[^>]*data-company="([^"]+)"',
        r'<span[^>]*class="[^"]*employer[^"]*"[^>]*>([^<]+)</span>',
        r'<h3[^>]*>([A-Z][^<]{3,100})</h3>\s*<p[^>]*class="[^"]*company[^"]*"'
    ]

    for pattern in patterns:
        for match in re.finditer(pattern, html):
            employer = match.group(1).strip()
            if employer and len(employer) > 2:
                employers[employer] = employers.get(employer, 0) + 1

    return employers

def main():
    """Main job board scraping."""
    all_job_employers = {}

    print("Scraping job boards for OFM agencies...\n", flush=True)

    sirency = scrape_sirency_jobs()
    all_job_employers["sirency"] = sirency

    indeed = scrape_indeed_onlyfans()
    all_job_employers["indeed"] = indeed

    jooble = scrape_jooble_onlyfans()
    all_job_employers["jooble"] = jooble

    onlinejobs = scrape_onlinejobs_ph_ofm()
    all_job_employers["onlinejobs"] = onlinejobs

    swooped = scrape_swooped()
    all_job_employers["swooped"] = swooped

    print(f"\nResults:")
    print(f"  Sirency: {len(sirency)} employers")
    print(f"  Indeed: {len(indeed)} employers")
    print(f"  Jooble: {len(jooble)} employers")
    print(f"  OnlineJobs.ph: {len(onlinejobs)} employers")
    print(f"  Swooped: {len(swooped)} employers")

    # Write to temp JSON for verification
    with open("/tmp/job_employers.json", "w") as f:
        for board, employers in all_job_employers.items():
            for emp, count in sorted(employers.items(), key=lambda x: x[1], reverse=True)[:10]:
                f.write(json.dumps({"board": board, "employer": emp, "posts": count}) + "\n")

    print(f"\nTop employers saved to /tmp/job_employers.json", flush=True)

if __name__ == "__main__":
    main()
