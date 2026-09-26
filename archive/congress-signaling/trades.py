import csv
from datetime import datetime
from db.models import SessionLocal, Senator, Company, SenatorTrade

TRADES_CSV_PATH = "data/capitoltrades_sample.csv"


def ingest_trades():
    db = SessionLocal()
    try:
        with open(TRADES_CSV_PATH, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                full_name = row["politician"]
                ticker = row["ticker"]
                trade_date = datetime.strptime(row["transaction_date"], "%Y-%m-%d").date()
                tx_type = row["transaction"]
                amount_low = float(row["amount_low"]) if row["amount_low"] else None
                amount_high = float(row["amount_high"]) if row["amount_high"] else None

                senator = db.query(Senator).filter_by(full_name=full_name).one_or_none()
                if not senator:
                    senator = Senator(full_name=full_name)
                    db.add(senator)
                    db.flush()

                company = db.query(Company).filter_by(ticker=ticker).one_or_none()
                if not company:
                    company = Company(ticker=ticker)
                    db.add(company)
                    db.flush()

                trade = SenatorTrade(
                    senator_id=senator.senator_id,
                    company_id=company.company_id,
                    trade_date=trade_date,
                    transaction_type=tx_type,
                    amount_low=amount_low,
                    amount_high=amount_high,
                    source="CapitolTrades",
                    source_url=row.get("source_url"),
                )
                db.add(trade)
        db.commit()
    finally:
        db.close()


if __name__ == "__main__":
    ingest_trades()
