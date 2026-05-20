"""FRED API client. Free official API from Federal Reserve Bank of St. Louis."""
import os
import requests

FRED_BASE = "https://api.stlouisfed.org/fred/series/observations"


def get_series(series_id, start_date=None, end_date=None, limit=100):
    """Fetch FRED series data."""
    try:
        api_key = os.environ.get("FRED_API_KEY", "")
        if not api_key:
            return _mock_series(series_id)
        params = {
            "series_id": series_id,
            "api_key": api_key,
            "file_type": "json",
            "sort_order": "desc",
            "limit": limit,
        }
        if start_date:
            params["observation_start"] = start_date
        resp = requests.get(FRED_BASE, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        observations = [
            {"date": o["date"], "value": o["value"]}
            for o in data.get("observations", [])
            if o["value"] != "."
        ]
        return {
            "series_id": series_id,
            "series_name": _series_name(series_id),
            "units": _series_units(series_id),
            "frequency": _series_freq(series_id),
            "data": observations,
        }
    except Exception:
        return _mock_series(series_id)


def _series_name(sid):
    names = {
        "DGS10": "10-Year Treasury",
        "DGS2": "2-Year Treasury",
        "FEDFUNDS": "Fed Funds Rate",
        "DXY": "US Dollar Index",
        "USDCNH": "USD/CNH",
        "UNRATE": "Unemployment Rate",
        "CPIAUCSL": "CPI",
    }
    return names.get(sid, sid)


def _series_units(sid):
    return (
        "%"
        if sid in ("DGS10", "DGS2", "FEDFUNDS", "UNRATE")
        else "index"
        if sid == "DXY"
        else "USD"
    )


def _series_freq(sid):
    return "daily" if sid in ("DGS10", "DGS2", "DXY", "USDCNH") else "monthly"


def _mock_series(series_id):
    """Return mock FRED data for offline testing."""
    import random
    from datetime import date, timedelta

    today = date.today()
    data = []
    for i in range(30):
        d = today - timedelta(days=i * 7)
        base = {
            "DGS10": 4.3,
            "DGS2": 4.0,
            "FEDFUNDS": 5.25,
            "UNRATE": 4.1,
            "CPIAUCSL": 310.0,
            "DXY": 104.0,
        }.get(series_id, 100)
        data.append(
            {
                "date": d.strftime("%Y-%m-%d"),
                "value": str(round(base + random.uniform(-0.2, 0.2), 2)),
            }
        )
    return {
        "series_id": series_id,
        "series_name": _series_name(series_id),
        "units": _series_units(series_id),
        "frequency": _series_freq(series_id),
        "data": data,
        "mock": True,
    }
