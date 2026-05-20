"""SEC EDGAR API client. Free official API for US equities only."""
import requests
import json
import os

SEC_BASE = "https://www.sec.gov/cgi-bin/browse-edgar"
CIK_PATH = os.path.join(os.path.dirname(__file__), "mock_data", "us_tickers.json")


def get_company_tickers():
    """Load ticker->CIK mapping from local cache."""
    try:
        with open(CIK_PATH) as f:
            return json.load(f)
    except Exception:
        return {}


def search_filings(ticker, form_types=None, limit=5):
    """Search SEC EDGAR filings. US equities only."""
    try:
        form_types = form_types or ["10-K", "10-Q", "8-K"]
        tickers = get_company_tickers()
        cik = tickers.get(ticker.upper(), {}).get("cik")
        if not cik:
            return _mock_filings(ticker, limit)
        headers = {"User-Agent": "FintechResearch/1.0 (contact@example.com)"}
        results = []
        for ft in form_types:
            params = {
                "action": "getcompany",
                "CIK": cik.zfill(10),
                "type": ft,
                "dateb": "",
                "owner": "exclude",
                "count": str(limit),
                "output": "atom",
            }
            resp = requests.get(SEC_BASE, params=params, headers=headers, timeout=30)
            if resp.status_code == 200:
                # Parse atom XML
                import xml.etree.ElementTree as ET

                root = ET.fromstring(resp.content)
                ns = {"atom": "http://www.w3.org/2005/Atom"}
                for entry in root.findall("atom:entry", ns)[:limit]:
                    title = entry.findtext("atom:title", "", ns)
                    updated = entry.findtext("atom:updated", "", ns)
                    link_el = entry.find("atom:link", ns)
                    href = link_el.get("href", "") if link_el is not None else ""
                    results.append(
                        {
                            "accession_number": "",
                            "form_type": ft,
                            "filing_date": updated[:10],
                            "description": title,
                            "url": href,
                        }
                    )
        return {"filings": results[:limit]}
    except Exception:
        return _mock_filings(ticker, limit)


def _mock_filings(ticker, limit):
    return {
        "filings": [
            {
                "accession_number": "mock-001",
                "form_type": "10-K",
                "filing_date": "2025-02-15",
                "description": f"Annual report for {ticker}",
                "url": "",
                "mock": True,
            }
        ],
        "mock": True,
    }
