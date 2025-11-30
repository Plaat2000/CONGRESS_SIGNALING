"""Lightweight agent utilities for the OpenAI Responses API demo.

This module exposes a minimal tool surface so the model can fetch
"Congress signals" (i.e., notable trades around bill actions) from a
local SQLite database. If the database isn't populated, the agent
falls back to a small in-memory sample so the tool calls still return
useful structure for experimentation.
"""
from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any, Dict, List

# A few seed signals used when the local database has not been set up yet.
_DEFAULT_STRONG_TICKERS: List[Dict[str, Any]] = [
    {
        "ticker": "NVDA",
        "company_sector": "Technology",
        "signal_strength": 0.92,
        "rationale": "Clustered bipartisan buys ahead of AI funding bills and strong earnings momentum.",
    },
    {
        "ticker": "LMT",
        "company_sector": "Aerospace & Defense",
        "signal_strength": 0.87,
        "rationale": "Defense appropriations markup paired with fresh purchase disclosures from Armed Services members.",
    },
    {
        "ticker": "LLY",
        "company_sector": "Healthcare",
        "signal_strength": 0.83,
        "rationale": "Insider accumulation around drug pricing negotiations where health committee staff are active.",
    },
    {
        "ticker": "CAT",
        "company_sector": "Industrials",
        "signal_strength": 0.78,
        "rationale": "Heavy equipment stimulus amendments tracked by infrastructure subcommittee members buying shares.",
    },
    {
        "ticker": "NEE",
        "company_sector": "Utilities",
        "signal_strength": 0.75,
        "rationale": "Energy transition incentives aligning with clean-power procurement commentary in committee hearings.",
    },
]


class CongressSignalsAgent:
    """Simple helper that surfaces database-backed signals to the model."""

    def __init__(self, db_path: str | Path = "signals.db") -> None:
        self.db_path = Path(db_path)

    # -- Tool implementations -------------------------------------------------
    def top_signals(self, limit: int = 5) -> Dict[str, Any]:
        """Return the strongest-looking tickers based on suspicious trades.

        The method first attempts to pull aggregated trade / bill activity
        from the local SQLite database. If no rows are available, it falls
        back to a curated sample so the calling code always receives a
        structured response.
        """

        rows = self._query_top_signals(limit)
        if not rows:
            rows = _DEFAULT_STRONG_TICKERS[:limit]
        return {"signals": rows}

    def ticker_details(self, ticker: str, limit: int = 5) -> Dict[str, Any]:
        """Return recent suspicious trades and bill statuses for a ticker."""

        rows = self._query_ticker_details(ticker, limit)
        if not rows:
            rows = [
                {
                    "ticker": ticker.upper(),
                    "senator": "Sample Senator",
                    "trade_date": "(no local data)",
                    "transaction_type": "Purchase",
                    "bill_title": "Example bill touching the company's sector",
                    "status": "Draft",
                    "status_date": "(n/a)",
                    "days_diff": None,
                }
            ]
        return {"trades": rows}

    # -- Internal helpers -----------------------------------------------------
    def _connect(self) -> sqlite3.Connection | None:
        if not self.db_path.exists():
            return None
        try:
            return sqlite3.connect(self.db_path)
        except sqlite3.Error:
            return None

    def _query_top_signals(self, limit: int) -> List[Dict[str, Any]]:
        conn = self._connect()
        if conn is None:
            return []

        query = """
            SELECT
              ticker,
              company_sector,
              COUNT(*) AS trade_count,
              SUM(CASE WHEN transaction_type LIKE 'Purchase%' THEN 1 ELSE 0 END) AS buy_signals,
              MIN(ABS(days_diff)) AS nearest_event_days
            FROM suspicious_trades
            GROUP BY ticker, company_sector
            ORDER BY buy_signals DESC, trade_count DESC, nearest_event_days ASC
            LIMIT ?
        """
        try:
            cur = conn.cursor()
            cur.execute(query, (limit,))
            rows = cur.fetchall()
            return [
                {
                    "ticker": r[0],
                    "company_sector": r[1],
                    "signal_strength": min(1.0, 0.6 + 0.05 * r[2] + 0.1 * (r[3] or 0)),
                    "rationale": (
                        f"{r[2]} notable trades with {r[3]} buys; closest bill action {r[4]} days away"
                        if r[4] is not None
                        else f"{r[2]} notable trades with {r[3]} buys"
                    ),
                }
                for r in rows
            ]
        except sqlite3.Error:
            return []
        finally:
            conn.close()

    def _query_ticker_details(self, ticker: str, limit: int) -> List[Dict[str, Any]]:
        conn = self._connect()
        if conn is None:
            return []

        query = """
            SELECT
              senator,
              ticker,
              trade_date,
              transaction_type,
              bill_title,
              status,
              status_date,
              days_diff
            FROM suspicious_trades
            WHERE ticker = ?
            ORDER BY ABS(days_diff), trade_date DESC
            LIMIT ?
        """
        try:
            cur = conn.cursor()
            cur.execute(query, (ticker.upper(), limit))
            rows = cur.fetchall()
            return [
                {
                    "senator": r[0],
                    "ticker": r[1],
                    "trade_date": r[2],
                    "transaction_type": r[3],
                    "bill_title": r[4],
                    "status": r[5],
                    "status_date": r[6],
                    "days_diff": r[7],
                }
                for r in rows
            ]
        except sqlite3.Error:
            return []
        finally:
            conn.close()


# Tools exposed to the model for the new Responses API.
OPENAI_TOOLS: List[Dict[str, Any]] = [
    {
        "type": "function",
        "function": {
            "name": "top_signals",
            "description": "Return the strongest tickers based on suspicious trades and bill timing.",
            "parameters": {
                "type": "object",
                "properties": {
                    "limit": {
                        "type": "integer",
                        "description": "Number of tickers to return (default 5)",
                        "minimum": 1,
                        "default": 5,
                    }
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "ticker_details",
            "description": "Show recent suspicious trades and bill status changes for a specific ticker.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": "Ticker symbol to inspect",
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum rows to return (default 5)",
                        "minimum": 1,
                        "default": 5,
                    },
                },
                "required": ["ticker"],
            },
        },
    },
]


def dispatch_tool(agent: CongressSignalsAgent, name: str, args: Dict[str, Any]) -> Any:
    """Route a tool call from the model to the matching agent method."""

    method = getattr(agent, name, None)
    if method is None:
        raise ValueError(f"Unknown tool '{name}'")
    return method(**args)
