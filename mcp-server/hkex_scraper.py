"""HKEX News disclosure scraper. Free public access."""
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def search_disclosures(stock_code, category="announcements", since=None, limit=5):
    """Search HKEX News for disclosures. Returns list of announcements."""
    try:
        url = "https://www1.hkexnews.hk/search/titlesearch.xhtml"
        params = {"stockCode": stock_code, "category": category}
        resp = requests.get(
            url,
            params=params,
            timeout=30,
            headers={"User-Agent": "FintechResearch/1.0"},
        )
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        results = []
        rows = (
            soup.select("table.table-responsive tbody tr")
            if soup.select("table.table-responsive tbody tr")
            else []
        )
        for row in rows[:limit]:
            cols = row.find_all("td")
            if len(cols) >= 3:
                date_text = cols[0].get_text(strip=True)
                title = cols[1].get_text(strip=True)
                pdf_link = cols[1].find("a", href=True)
                pdf_url = pdf_link["href"] if pdf_link else ""
                if pdf_url and not pdf_url.startswith("http"):
                    pdf_url = "https://www1.hkexnews.hk" + pdf_url
                if since and date_text < since:
                    continue
                results.append(
                    {
                        "date": date_text,
                        "title": title,
                        "category": category,
                        "pdf_url": pdf_url,
                        "stock_code": stock_code,
                    }
                )
        time.sleep(2)  # Rate limit
        return {"announcements": results, "count": len(results)}
    except Exception as e:
        # Fallback to mock
        return _mock_disclosures(stock_code, limit)


def _mock_disclosures(stock_code, limit):
    """Return mock disclosure data for offline testing."""
    mocks = {
        "0700": [
            {
                "date": "2025-05-14",
                "title": "Quarterly Results Announcement",
                "category": "announcements",
                "pdf_url": "",
                "stock_code": "0700",
            },
            {
                "date": "2025-04-02",
                "title": "Connected Transaction",
                "category": "announcements",
                "pdf_url": "",
                "stock_code": "0700",
            },
            {
                "date": "2025-03-19",
                "title": "Annual Report 2024",
                "category": "reports",
                "pdf_url": "",
                "stock_code": "0700",
            },
        ],
        "9988": [
            {
                "date": "2025-05-10",
                "title": "Quarterly Results Announcement",
                "category": "announcements",
                "pdf_url": "",
                "stock_code": "9988",
            },
            {
                "date": "2025-04-15",
                "title": "Share Buyback Update",
                "category": "announcements",
                "pdf_url": "",
                "stock_code": "9988",
            },
            {
                "date": "2025-03-28",
                "title": "Annual Report 2024",
                "category": "reports",
                "pdf_url": "",
                "stock_code": "9988",
            },
        ],
        "3690": [
            {
                "date": "2025-05-12",
                "title": "Quarterly Results Announcement",
                "category": "announcements",
                "pdf_url": "",
                "stock_code": "3690",
            },
            {
                "date": "2025-03-25",
                "title": "Annual Report 2024",
                "category": "reports",
                "pdf_url": "",
                "stock_code": "3690",
            },
        ],
    }
    return {
        "announcements": mocks.get(stock_code, [])[:limit],
        "count": len(mocks.get(stock_code, [])),
        "mock": True,
    }
