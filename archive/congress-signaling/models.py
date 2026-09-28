from sqlalchemy import (
    create_engine, Column, Integer, String, Date, Numeric, ForeignKey, BigInteger, Text
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

DATABASE_URL = "postgresql://congress:congress@localhost:5432/congress_signals"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
Base = declarative_base()


class Senator(Base):
    __tablename__ = "senator"
    senator_id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    party = Column(String)
    state = Column(String)
    external_id = Column(String, unique=True)


class Company(Base):
    __tablename__ = "company"
    company_id = Column(Integer, primary_key=True)
    ticker = Column(String, unique=True, nullable=False)
    name = Column(String)
    sector = Column(String)
    industry = Column(String)


class SenatorTrade(Base):
    __tablename__ = "senator_trade"
    trade_id = Column(Integer, primary_key=True)
    senator_id = Column(Integer, ForeignKey("senator.senator_id"))
    company_id = Column(Integer, ForeignKey("company.company_id"))
    trade_date = Column(Date)
    transaction_type = Column(String)
    amount_low = Column(Numeric(18, 2))
    amount_high = Column(Numeric(18, 2))
    source = Column(String)
    source_url = Column(Text)

    senator = relationship("Senator")
    company = relationship("Company")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
