import csv
import sqlite3
from pathlib import Path

DB_PATH = Path("signals.db")
DATA_DIR = Path("data")

def get_or_create(conn, table, key_col, key_val, extra_cols=None):
    cur = conn.cursor()
    cur.execute(f"SELECT id FROM {table} WHERE {key_col} = ?", (key_val,))
    row = cur.fetchone()
    if row:
        return row[0]
    cols = [key_col]
    vals = [key_val]
    placeholders = ["?"]
    if extra_cols:
        for col, val in extra_cols.items():
            cols.append(col)
            vals.append(val)
            placeholders.append("?")
    sql = f"INSERT INTO {table} ({', '.join(cols)}) VALUES ({', '.join(placeholders)})"
    cur.execute(sql, vals)
    conn.commit()
    return cur.lastrowid

def ingest_companies(conn):
    path = DATA_DIR / "companies.csv"
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            get_or_create(
                conn,
                "company",
                "ticker",
                row["ticker"].strip(),
                {
                    "name": row.get("name", "").strip() or None,
                    "sector": row.get("sector", "").strip() or None,
                    "industry": row.get("industry", "").strip() or None,
                },
            )
    print("Loaded companies")

def ingest_bills(conn):
    # bills.csv
    bills_path = DATA_DIR / "bills.csv"
    with bills_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            get_or_create(
                conn,
                "bill",
                "external_bill_id",
                row["external_bill_id"].strip(),
                {
                    "title": row.get("title", "").strip() or None,
                    "sector": row.get("sector", "").strip() or None,
                },
            )
    print("Loaded bills")

    # bill_status.csv
    status_path = DATA_DIR / "bill_status.csv"
    with status_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cur = conn.cursor()
        for row in reader:
            external_id = row["external_bill_id"].strip()
            cur.execute("SELECT id FROM bill WHERE external_bill_id = ?", (external_id,))
            bill_row = cur.fetchone()
            if not bill_row:
                print(f"WARNING: status references unknown bill {external_id}, skipping")
                continue
            bill_id = bill_row[0]
            cur.execute(
                """
                INSERT INTO bill_status (bill_id, status, status_date)
                VALUES (?, ?, ?)
                """,
                (
                    bill_id,
                    row.get("status", "").strip() or None,
                    row.get("status_date", "").strip() or None,
                ),
            )
        conn.commit()
    print("Loaded bill statuses")

def ingest_trades(conn):
    path = DATA_DIR / "trades.csv"
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cur = conn.cursor()
        for row in reader:
            senator_name = row["senator"].strip()
            ticker = row["ticker"].strip()
            trade_date = row["trade_date"].strip()
            tx_type = row["transaction_type"].strip()
            amount_low = row.get("amount_low") or None
            amount_high = row.get("amount_high") or None

            senator_id = get_or_create(conn, "senator", "full_name", senator_name)
            company_id = get_or_create(conn, "company", "ticker", ticker)

            cur.execute(
                """
                INSERT INTO senator_trade (
                    senator_id, company_id, trade_date,
                    transaction_type, amount_low, amount_high
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    senator_id,
                    company_id,
                    trade_date,
                    tx_type,
                    float(amount_low) if amount_low else None,
                    float(amount_high) if amount_high else None,
                ),
            )
        conn.commit()
    print("Loaded trades")

def main():
    conn = sqlite3.connect(DB_PATH)
    try:
        ingest_companies(conn)
        ingest_bills(conn)
        ingest_trades(conn)
    finally:
        conn.close()

if __name__ == "__main__":
    main()
