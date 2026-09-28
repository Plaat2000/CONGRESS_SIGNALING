import sqlite3
from pathlib import Path
from tabulate import tabulate  # optional, but nice formatting

DB_PATH = Path("signals.db")

def main():
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute(
            """
            SELECT
              trade_id,
              senator,
              ticker,
              company_sector,
              trade_date,
              transaction_type,
              amount_low,
              amount_high,
              external_bill_id,
              bill_title,
              status,
              status_date,
              ROUND(days_diff, 1) AS days_diff
            FROM suspicious_trades
            ORDER BY ABS(days_diff), trade_date DESC
            LIMIT 50
            """
        )
        rows = cur.fetchall()
        headers = [d[0] for d in cur.description]
        if not rows:
            print("No suspicious trades found (with current data).")
        else:
            try:
                # pretty table if tabulate is installed
                print(tabulate(rows, headers=headers, tablefmt="grid"))
            except Exception:
                # fallback
                print(headers)
                for r in rows:
                    print(r)
    finally:
        conn.close()

if __name__ == "__main__":
    main()
