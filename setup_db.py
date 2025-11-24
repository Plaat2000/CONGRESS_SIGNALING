import sqlite3
from pathlib import Path

DB_PATH = Path("signals.db")

SCHEMA_SQL = """
DROP TABLE IF EXISTS senator;
DROP TABLE IF EXISTS company;
DROP TABLE IF EXISTS bill;
DROP TABLE IF EXISTS bill_status;
DROP TABLE IF EXISTS senator_trade;
DROP VIEW IF EXISTS suspicious_trades;

CREATE TABLE senator (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT UNIQUE
);

CREATE TABLE company (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT UNIQUE,
    name TEXT,
    sector TEXT,
    industry TEXT
);

CREATE TABLE bill (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    external_bill_id TEXT UNIQUE,
    title TEXT,
    sector TEXT
);

CREATE TABLE bill_status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_id INTEGER,
    status TEXT,
    status_date TEXT, -- ISO date string
    FOREIGN KEY (bill_id) REFERENCES bill(id)
);

CREATE TABLE senator_trade (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    senator_id INTEGER,
    company_id INTEGER,
    trade_date TEXT, -- ISO date string
    transaction_type TEXT,
    amount_low REAL,
    amount_high REAL,
    FOREIGN KEY (senator_id) REFERENCES senator(id),
    FOREIGN KEY (company_id) REFERENCES company(id)
);

CREATE VIEW suspicious_trades AS
SELECT
    st.id AS trade_id,
    s.full_name AS senator,
    c.ticker,
    c.sector AS company_sector,
    st.trade_date,
    st.transaction_type,
    st.amount_low,
    st.amount_high,
    b.external_bill_id,
    b.title AS bill_title,
    b.sector AS bill_sector,
    bs.status,
    bs.status_date,
    (julianday(st.trade_date) - julianday(bs.status_date)) AS days_diff
FROM senator_trade st
JOIN senator s ON s.id = st.senator_id
JOIN company c ON c.id = st.company_id
JOIN bill b ON b.sector = c.sector
JOIN bill_status bs ON bs.bill_id = b.id
WHERE ABS(julianday(st.trade_date) - julianday(bs.status_date)) <= 5
ORDER BY ABS(julianday(st.trade_date) - julianday(bs.status_date)), st.trade_date DESC;
"""

def main():
    if DB_PATH.exists():
        DB_PATH.unlink()
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.executescript(SCHEMA_SQL)
        conn.commit()
        print("Database and schema created at", DB_PATH)
    finally:
        conn.close()

if __name__ == "__main__":
    main()
