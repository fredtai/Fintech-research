"""SQLite cache layer with TTL support."""
import json
import sqlite3
from datetime import datetime, timedelta
from contextlib import contextmanager


class Cache:
    """SQLite-based cache with TTL, WAL mode, and table per data type."""

    def __init__(self, db_path="cache.db"):
        self.db_path = db_path
        with self._connect() as conn:
            # WAL mode for better concurrency
            conn.execute("PRAGMA journal_mode=WAL;")
            conn.execute("PRAGMA synchronous=NORMAL;")
            self._create_tables(conn)

    @contextmanager
    def _connect(self):
        conn = sqlite3.connect(self.db_path, check_same_thread=False)
        try:
            yield conn
        finally:
            conn.close()

    def _create_tables(self, conn):
        conn.execute("""
            CREATE TABLE IF NOT EXISTS cache (
                key TEXT PRIMARY KEY,
                data TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                expires_at TIMESTAMP
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS fundamentals (
                ticker TEXT PRIMARY KEY,
                data TEXT,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS price_history (
                ticker TEXT,
                date TEXT,
                open REAL,
                high REAL,
                low REAL,
                close REAL,
                volume INTEGER,
                PRIMARY KEY (ticker, date)
            )
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_price_ticker ON price_history(ticker);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_cache_expires ON cache(expires_at);")
        conn.commit()

    def get(self, key):
        """Return dict or None (checks TTL, expired returns None)."""
        try:
            with self._connect() as conn:
                cur = conn.execute(
                    "SELECT data, expires_at FROM cache WHERE key = ?",
                    (key,),
                )
                row = cur.fetchone()
                if not row:
                    return None
                data_json, expires_at = row
                if expires_at and datetime.now() > datetime.fromisoformat(expires_at):
                    conn.execute("DELETE FROM cache WHERE key = ?", (key,))
                    conn.commit()
                    return None
                return json.loads(data_json)
        except Exception:
            return None

    def set(self, key, data, ttl_seconds=3600):
        """JSON-serialize and store with TTL."""
        try:
            expires = (datetime.now() + timedelta(seconds=ttl_seconds)).isoformat()
            data_json = json.dumps(data, default=str)
            with self._connect() as conn:
                conn.execute(
                    """INSERT INTO cache (key, data, expires_at)
                       VALUES (?, ?, ?)
                       ON CONFLICT(key) DO UPDATE SET
                         data=excluded.data,
                         created_at=CURRENT_TIMESTAMP,
                         expires_at=excluded.expires_at""",
                    (key, data_json, expires),
                )
                conn.commit()
        except Exception:
            pass

    def get_fundamentals(self, ticker):
        """Return dict or None."""
        try:
            with self._connect() as conn:
                cur = conn.execute(
                    "SELECT data FROM fundamentals WHERE ticker = ?",
                    (ticker,),
                )
                row = cur.fetchone()
                if row:
                    return json.loads(row[0])
                return None
        except Exception:
            return None

    def set_fundamentals(self, ticker, data):
        """Store fundamentals JSON blob."""
        try:
            data_json = json.dumps(data, default=str)
            with self._connect() as conn:
                conn.execute(
                    """INSERT INTO fundamentals (ticker, data, updated_at)
                       VALUES (?, ?, CURRENT_TIMESTAMP)
                       ON CONFLICT(ticker) DO UPDATE SET
                         data=excluded.data,
                         updated_at=CURRENT_TIMESTAMP""",
                    (ticker, data_json),
                )
                conn.commit()
        except Exception:
            pass

    def get_price_history(self, ticker):
        """Return list of dicts or None."""
        try:
            with self._connect() as conn:
                conn.row_factory = sqlite3.Row
                cur = conn.execute(
                    """SELECT date, open, high, low, close, volume
                       FROM price_history WHERE ticker = ?
                       ORDER BY date DESC LIMIT 100""",
                    (ticker,),
                )
                rows = cur.fetchall()
                if rows:
                    return [dict(r) for r in rows]
                return None
        except Exception:
            return None

    def set_price_history(self, ticker, rows_list):
        """Store OHLCV rows. rows_list = [{date, open, high, low, close, volume}]."""
        try:
            with self._connect() as conn:
                for row in rows_list:
                    conn.execute(
                        """INSERT INTO price_history
                           (ticker, date, open, high, low, close, volume)
                           VALUES (?, ?, ?, ?, ?, ?, ?)
                           ON CONFLICT(ticker, date) DO UPDATE SET
                             open=excluded.open,
                             high=excluded.high,
                             low=excluded.low,
                             close=excluded.close,
                             volume=excluded.volume""",
                        (
                            ticker,
                            row["date"],
                            row["open"],
                            row["high"],
                            row["low"],
                            row["close"],
                            row["volume"],
                        ),
                    )
                conn.commit()
        except Exception:
            pass

    def clear_expired(self):
        """Delete expired cache entries."""
        try:
            with self._connect() as conn:
                conn.execute(
                    "DELETE FROM cache WHERE expires_at < ?",
                    (datetime.now().isoformat(),),
                )
                conn.commit()
        except Exception:
            pass
