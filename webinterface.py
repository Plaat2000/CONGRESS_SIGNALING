#!/usr/bin/env python3
"""Small read-only web interface for the congressional trading signals database."""

from __future__ import annotations

import html
import json
import sqlite3
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse


DB_PATH = Path(__file__).with_name("signals.db")
HOST = "127.0.0.1"
PORT = 8000


def fetch_trades(senator: str = "", ticker: str = "", limit: int = 100) -> list[dict]:
    query = "SELECT * FROM suspicious_trades WHERE 1=1"
    parameters: list[object] = []
    if senator:
        query += " AND senator LIKE ?"
        parameters.append(f"%{senator}%")
    if ticker:
        query += " AND ticker LIKE ?"
        parameters.append(f"%{ticker}%")
    query += " LIMIT ?"
    parameters.append(limit)

    with sqlite3.connect(DB_PATH) as connection:
        connection.row_factory = sqlite3.Row
        return [dict(row) for row in connection.execute(query, parameters)]


def page(trades: list[dict], senator: str, ticker: str) -> str:
    cards = []
    for trade in trades:
        cards.append(
            "<article class='card'>"
            f"<h2>{html.escape(str(trade['senator']))} · "
            f"{html.escape(str(trade['ticker']))}</h2>"
            f"<p><strong>Trade:</strong> {html.escape(str(trade['transaction_type']))} "
            f"on {html.escape(str(trade['trade_date']))}</p>"
            f"<p><strong>Amount:</strong> {trade['amount_low']} – {trade['amount_high']}</p>"
            f"<p><strong>Bill:</strong> {html.escape(str(trade['bill_title']))}</p>"
            f"<p><strong>Status:</strong> {html.escape(str(trade['status']))} "
            f"({html.escape(str(trade['status_date']))}); "
            f"<strong>Difference:</strong> {trade['days_diff']:.1f} days</p>"
            "</article>"
        )
    results = "".join(cards) or "<p>No matching signals found.</p>"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Congress Signaling</title>
  <style>
    body {{ font: 16px system-ui, sans-serif; max-width: 1000px; margin: 2rem auto; padding: 0 1rem; color: #17202a; background: #f5f7fa; }}
    form, .card {{ background: white; border: 1px solid #dce1e7; border-radius: 8px; padding: 1rem; margin: 1rem 0; }}
    form {{ display: flex; gap: .75rem; flex-wrap: wrap; }}
    input, button {{ padding: .6rem; font: inherit; }}
    button {{ cursor: pointer; background: #1769aa; color: white; border: 0; border-radius: 4px; }}
    .card h2 {{ margin-top: 0; }}
  </style>
</head>
<body>
  <h1>Congress Signaling</h1>
  <p>Read-only view of trades near bill-status changes.</p>
  <form method="get">
    <input name="senator" placeholder="Senator" value="{html.escape(senator)}">
    <input name="ticker" placeholder="Ticker" value="{html.escape(ticker)}">
    <button type="submit">Search</button>
  </form>
  <p>{len(trades)} signal(s)</p>
  {results}
</body>
</html>"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        values = parse_qs(parsed.query)
        senator = values.get("senator", [""])[0].strip()
        ticker = values.get("ticker", [""])[0].strip()
        try:
            limit = min(max(int(values.get("limit", ["100"])[0]), 1), 500)
            trades = fetch_trades(senator, ticker, limit)
        except (ValueError, sqlite3.Error) as error:
            self.send_error(500, f"Unable to read database: {error}")
            return

        if parsed.path == "/api/trades":
            self._send("application/json", json.dumps(trades, default=str))
        elif parsed.path in {"/", "/index.html"}:
            self._send("text/html; charset=utf-8", page(trades, senator, ticker))
        elif parsed.path == "/health":
            self._send("application/json", json.dumps({"status": "ok"}))
        else:
            self.send_error(404)

    def _send(self, content_type: str, content: str) -> None:
        body = content.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:
        return


def main() -> None:
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"Web interface running at http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping web interface.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
