#!/usr/bin/env python3
"""
Enumerate OFM agencies from:
1. UK Companies House (active companies with OFM-related names/SIC)
2. OpenCorporates (multi-jurisdiction search)
3. Job boards: OnlineJobs.ph, Indeed, Jooble, Swooped, Sirency
"""

import json
import subprocess
import time
import re
from datetime import datetime
from html.parser import HTMLParser
from urllib.parse import urljoin, quote

# Keywords to search for OFM agencies
KEYWORDS = [
    "onlyfans management",
    "onlyfans agency",
    "creator management",
    "model management",
    "onlyfans",
    "ofm agency",
    "content creator agency"
]

class CompaniesHouseParser(HTMLParser):
    """Parse Companies House search results."""
    def __init__(self):
        super().__init__()
        self.firms = []
        self.in_result = False
        self.current_firm = {}
        self.in_link = False
        self.in_status = False
        self.text_buffer = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "a" and "href" in attrs_dict and "/company/" in attrs_dict["href"]:
            self.in_link = True
            self.current_firm["url"] = urljoin("https://find-and-update.company-information.service.gov.uk", attrs_dict["href"])
            if "/company/" in attrs_dict["href"]:
                self.current_firm["company_number"] = attrs_dict["href"].split("/company/")[-1].rstrip("/")

    def handle_endtag(self, tag):
        if tag == "a":
            self.in_link = False
            if self.text_buffer.strip():
                if "name" not in self.current_firm:
                    self.current_firm["name"] = self.text_buffer.strip()
            self.text_buffer = ""

    def handle_data(self, data):
        if self.in_link or self.in_status:
            self.text_buffer += data

class OpenCorporatesParser(HTMLParser):
    """Parse OpenCorporates search results."""
    def __init__(self):
        super().__init__()
        self.firms = []
        self.current_firm = {}
        self.text_buffer = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "a" and "href" in attrs_dict and "/companies/" in attrs_dict["href"]:
            parts = attrs_dict["href"].split("/companies/")
            if len(parts) > 1:
                self.current_firm["url"] = urljoin("https://opencorporates.com", attrs_dict["href"])

    def handle_data(self, data):
        self.text_buffer += data.strip()
        if self.text_buffer and len(self.text_buffer) < 200:
            if "company" not in self.current_firm:
                self.current_firm["name"] = self.text_buffer

class JobBoardParser(HTMLParser):
    """Parse job board results for employer names."""
    def __init__(self, board_type="generic"):
        super().__init__()
        self.board_type = board_type
        self.jobs = []
        self.current_job = {}
        self.in_employer = False
        self.text_buffer = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if self.board_type == "onlinejobs":
            if tag == "a" and "class" in attrs_dict and "employer" in attrs_dict.get("class", ""):
                self.in_employer = True
        elif self.board_type == "indeed":
            if tag == "span" and "data-company-name" in attrs_dict:
                self.current_job["employer"] = attrs_dict["data-company-name"]
        elif self.board_type == "jooble":
            if tag == "span" and "class" in attrs_dict and "employer" in attrs_dict["class"]:
                self.in_employer = True

    def handle_data(self, data):
        if self.in_employer:
            self.text_buffer += data.strip()

    def handle_endtag(self, tag):
        if self.in_employer and tag == "a":
            if self.text_buffer:
                self.current_job["employer"] = self.text_buffer.strip()
                self.jobs.append(self.current_job)
                self.current_job = {}
            self.in_employer = False
            self.text_buffer = ""

def fetch_url(url, timeout=10):
    """Fetch URL using curl and return HTML content."""
    try:
        result = subprocess.run(
            ["curl", "-s", "-L", "-A", "Mozilla/5.0", "--max-time", str(timeout), url],
            capture_output=True,
            text=True,
            timeout=timeout + 2
        )
        if result.returncode == 0:
            return result.stdout
        return None
    except Exception as e:
        print(f"  Error fetching {url}: {e}", flush=True)
        return None

def scrape_companies_house():
    """Scrape UK Companies House for OFM agencies."""
    firms = []
    blocked = []

    print("  Scraping Companies House...", flush=True)

    for keyword in KEYWORDS[:4]:  # Limit to first 4 keywords
        url = f"https://find-and-update.company-information.service.gov.uk/search/companies?q={quote(keyword)}&page=1"
        html = fetch_url(url, timeout=15)

        if html is None:
            blocked.append("companies_house")
            print(f"    Blocked/timeout on keyword: {keyword}", flush=True)
            continue

        if "Access Denied" in html or "403" in html or not html.strip():
            blocked.append("companies_house")
            print(f"    Blocked on keyword: {keyword}", flush=True)
            continue

        # Simple regex-based extraction since page structure varies
        company_pattern = r'<a[^>]*href="(/company/[^"]+)"[^>]*>([^<]+)</a>'
        for match in re.finditer(company_pattern, html):
            company_number = match.group(1).split("/company/")[-1].rstrip("/")
            name = match.group(2).strip()

            if name and len(name) > 2:
                firm = {
                    "name": name,
                    "source": "companies_house",
                    "jurisdiction": "UK",
                    "company_number": company_number,
                    "status": "active",  # CH only shows active by default
                    "incorporated": None,
                    "sic": None,
                    "posts_seen": 0,
                    "url": f"https://find-and-update.company-information.service.gov.uk/company/{company_number}",
                    "checked": "2026-10-11"
                }
                if firm not in firms:
                    firms.append(firm)

        time.sleep(1)  # Rate limit

    return firms, list(set(blocked))

def scrape_opencorporates():
    """Scrape OpenCorporates for OFM agencies."""
    firms = []
    blocked = []

    print("  Scraping OpenCorporates...", flush=True)

    url = f"https://opencorporates.com/companies?q=onlyfans&order=score"
    html = fetch_url(url, timeout=15)

    if html is None or "Access Denied" in html or not html.strip():
        blocked.append("opencorporates")
        print("    OpenCorporates blocked or timeout", flush=True)
        return firms, blocked

    # Extract company links and names
    company_pattern = r'<a[^>]*href="(/companies/[^"]+)"[^>]*>([^<]+)</a>'
    for match in re.finditer(company_pattern, html):
        name = match.group(2).strip()
        if "onlyfans" in name.lower() or "ofm" in name.lower() or "creator" in name.lower():
            url_path = match.group(1)
            firm = {
                "name": name,
                "source": "opencorporates",
                "jurisdiction": "unknown",
                "company_number": None,
                "status": "unknown",
                "incorporated": None,
                "sic": None,
                "posts_seen": 0,
                "url": f"https://opencorporates.com{url_path}",
                "checked": "2026-10-11"
            }
            if firm not in firms:
                firms.append(firm)

    return firms, blocked

def scrape_onlinejobs_ph():
    """Scrape OnlineJobs.ph for OFM job postings."""
    employers = {}

    print("  Scraping OnlineJobs.ph...", flush=True)

    for keyword in ["OnlyFans chatter", "OFM chatter", "OnlyFans manager", "content creator"]:
        url = f"https://www.onlinejobs.ph/jobseekers/jobsearch?jobkeyword={quote(keyword)}"
        html = fetch_url(url, timeout=15)

        if html is None or not html.strip():
            continue

        # Extract employer names from job listings
        employer_pattern = r'<div[^>]*class="[^"]*employer[^"]*"[^>]*>([^<]+)</div>'
        for match in re.finditer(employer_pattern, html):
            employer = match.group(1).strip()
            if employer and employer not in ["Anonymous", "Hidden", ""]:
                employers[employer] = employers.get(employer, 0) + 1

        time.sleep(1)

    return employers

def scrape_indeed():
    """Scrape Indeed for OFM jobs."""
    employers = {}

    print("  Scraping Indeed...", flush=True)

    # Try multiple country sites
    for country in ["ie", "co.uk", "ca"]:
        url = f"https://www.indeed.com/jobs?q=onlyfans&l="
        if country != "ie":
            url = f"https://www.indeed.{country}/jobs?q=onlyfans&l="

        html = fetch_url(url, timeout=15)

        if html is None or not html.strip():
            continue

        # Extract company names
        company_pattern = r'<span[^>]*data-company-name="([^"]+)"'
        for match in re.finditer(company_pattern, html):
            employer = match.group(1).strip()
            if employer:
                employers[employer] = employers.get(employer, 0) + 1

        time.sleep(1)

    return employers

def scrape_jooble():
    """Scrape Jooble for OFM jobs."""
    employers = {}

    print("  Scraping Jooble...", flush=True)

    url = "https://jooble.org/jobs-onlyfans"
    html = fetch_url(url, timeout=15)

    if html is None or not html.strip():
        return employers

    # Extract employer names from class patterns
    employer_pattern = r'<span[^>]*class="[^"]*company[^"]*"[^>]*>([^<]+)</span>'
    for match in re.finditer(employer_pattern, html):
        employer = match.group(1).strip()
        if employer:
            employers[employer] = employers.get(employer, 0) + 1

    return employers

def scrape_swooped():
    """Scrape Swooped job board."""
    employers = {}

    print("  Scraping Swooped...", flush=True)

    url = "https://swooped.co/jobs?keywords=OnlyFans"
    html = fetch_url(url, timeout=15)

    if html is None or not html.strip():
        return employers

    # Extract company/hiring manager info
    employer_pattern = r'<div[^>]*class="[^"]*company-name[^"]*"[^>]*>([^<]+)</div>'
    for match in re.finditer(employer_pattern, html):
        employer = match.group(1).strip()
        if employer:
            employers[employer] = employers.get(employer, 0) + 1

    return employers

def scrape_sirency():
    """Scrape Sirency job board."""
    employers = {}

    print("  Scraping Sirency...", flush=True)

    url = "https://www.sirency.com/onlyfans-manager-jobs"
    html = fetch_url(url, timeout=15)

    if html is None or not html.strip():
        return employers

    # Extract company listings
    company_pattern = r'<h[2-4][^>]*>([^<]+)</h[2-4]>'
    for match in re.finditer(company_pattern, html):
        company = match.group(1).strip()
        if company and len(company) > 2:
            employers[company] = employers.get(company, 0) + 1

    return employers

def main():
    """Main enumeration routine."""
    all_firms = []
    all_blocked = set()
    job_board_employers = {}

    print("Starting OFM agency enumeration from registries and job boards...", flush=True)

    # Registry scraping
    print("\n1. Company Registries", flush=True)
    ch_firms, ch_blocked = scrape_companies_house()
    all_firms.extend(ch_firms)
    all_blocked.update(ch_blocked)

    oc_firms, oc_blocked = scrape_opencorporates()
    all_firms.extend(oc_firms)
    all_blocked.update(oc_blocked)

    print(f"   Found {len(ch_firms)} Companies House firms")
    print(f"   Found {len(oc_firms)} OpenCorporates firms")

    # Job board scraping
    print("\n2. Job Boards", flush=True)

    onlinejobs = scrape_onlinejobs_ph()
    job_board_employers["onlinejobs"] = onlinejobs

    indeed = scrape_indeed()
    job_board_employers["indeed"] = indeed

    jooble = scrape_jooble()
    job_board_employers["jooble"] = jooble

    swooped = scrape_swooped()
    job_board_employers["swooped"] = swooped

    sirency = scrape_sirency()
    job_board_employers["sirency"] = sirency

    print(f"   OnlineJobs.ph: {len(onlinejobs)} unique employers")
    print(f"   Indeed: {len(indeed)} unique employers")
    print(f"   Jooble: {len(jooble)} unique employers")
    print(f"   Swooped: {len(swooped)} unique employers")
    print(f"   Sirency: {len(sirency)} unique employers")

    # Convert job board employers to firm records
    anonymous_posts = 0
    for board, employers in job_board_employers.items():
        for employer, count in employers.items():
            if employer.lower() in ["anonymous", "hidden", "", "undisclosed"]:
                anonymous_posts += count
            else:
                # Check if already in firms
                existing = next((f for f in all_firms if f["name"].lower() == employer.lower()), None)
                if existing:
                    existing["posts_seen"] += count
                    existing["source"] += f"|{board}"
                else:
                    firm = {
                        "name": employer,
                        "source": board,
                        "jurisdiction": None,
                        "company_number": None,
                        "status": None,
                        "incorporated": None,
                        "sic": None,
                        "posts_seen": count,
                        "url": None,
                        "checked": "2026-10-11"
                    }
                    all_firms.append(firm)

    # Write output
    output_file = "/Users/shaansisodia/SISO_Workspace/Great_Library_of_SISO/works/siso-industry-packs/packs/onlyfans_management_agencies/data/ocean_registry_jobs.jsonl"

    with open(output_file, "w") as f:
        for firm in all_firms:
            f.write(json.dumps(firm) + "\n")

        # Write summary
        summary = {
            "summary": True,
            "anonymous_posts": anonymous_posts,
            "blocked": list(all_blocked),
            "total_firms": len(all_firms),
            "registry_firms": len([f for f in all_firms if f["source"] in ["companies_house", "opencorporates"]]),
            "registry_active": len([f for f in all_firms if f["source"] in ["companies_house", "opencorporates"] and f["status"] == "active"]),
            "job_board_employers": len([f for f in all_firms if f["source"] not in ["companies_house", "opencorporates"]]),
            "sources": list(set([f["source"] for f in all_firms]))
        }
        f.write(json.dumps(summary) + "\n")

    print(f"\nResults written to {output_file}", flush=True)
    print(f"Total firms: {len(all_firms)}", flush=True)
    print(f"Registry firms (active): {len([f for f in all_firms if f['source'] in ['companies_house', 'opencorporates'] and f['status'] == 'active'])}", flush=True)
    print(f"Anonymous job posts: {anonymous_posts}", flush=True)
    print(f"Blocked sources: {list(all_blocked)}", flush=True)

if __name__ == "__main__":
    main()
