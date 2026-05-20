"""News aggregation: NewsAPI + RSS feeds. Free tier."""
import os
import requests

try:
    import feedparser

    HAS_FEEDPARSER = True
except ImportError:
    HAS_FEEDPARSER = False


def get_news(query, source="newsapi", limit=5):
    """Get news with sentiment scoring."""
    try:
        if source == "newsapi":
            return _newsapi(query, limit)
        elif source == "rss":
            return _rss_feeds(query, limit)
        else:
            return _mock_news(query, limit)
    except Exception:
        return _mock_news(query, limit)


def _newsapi(query, limit):
    key = os.environ.get("NEWS_API_KEY", "")
    if not key:
        return _mock_news(query, limit)
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "sortBy": "publishedAt",
        "pageSize": limit,
        "apiKey": key,
    }
    resp = requests.get(url, params=params, timeout=30)
    resp.raise_for_status()
    articles = resp.json().get("articles", [])
    return {
        "articles": [
            {
                "title": a["title"],
                "source": a["source"]["name"],
                "published_at": a["publishedAt"],
                "url": a["url"],
                "sentiment_score": _sentiment(
                    a["title"] + " " + (a.get("description", "") or "")
                ),
            }
            for a in articles[:limit]
        ]
    }


def _rss_feeds(query, limit):
    if not HAS_FEEDPARSER:
        return _mock_news(query, limit)
    feeds = [
        "http://www.aastocks.com/en/rss/news.xml",
        "https://www.finet.hk/rss/news",
    ]
    articles = []
    for feed_url in feeds:
        try:
            fp = feedparser.parse(feed_url)
            for entry in fp.entries[:limit]:
                articles.append(
                    {
                        "title": entry.title,
                        "source": feed_url.split("/")[2],
                        "published_at": entry.get("published", ""),
                        "url": entry.link,
                        "sentiment_score": _sentiment(entry.title),
                    }
                )
        except Exception:
            continue
    return {"articles": articles[:limit]}


def _sentiment(text):
    """Simple keyword sentiment: -1 to +1."""
    positive = [
        "surge",
        "gain",
        "rise",
        "bull",
        "strong",
        "beat",
        "growth",
        "rally",
        "outperform",
        "upgrade",
        "boost",
        "jump",
    ]
    negative = [
        "fall",
        "drop",
        "bear",
        "weak",
        "miss",
        "decline",
        "crash",
        "sell",
        "downgrade",
        "plunge",
        "slump",
        "loss",
    ]
    text_lower = text.lower()
    pos = sum(1 for w in positive if w in text_lower)
    neg = sum(1 for w in negative if w in text_lower)
    total = pos + neg
    return round((pos - neg) / total, 2) if total > 0 else 0.0


def _mock_news(query, limit):
    return {
        "articles": [
            {
                "title": f"Mock news for {query}",
                "source": "Mock",
                "published_at": "2025-05-01T00:00:00Z",
                "url": "",
                "sentiment_score": 0.0,
                "mock": True,
            }
        ],
        "mock": True,
    }
