-- senators & committees
CREATE TABLE senator (
    senator_id SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    party TEXT,
    state TEXT,
    external_id TEXT UNIQUE  -- e.g. bioguide id if you add it later
);

CREATE TABLE committee (
    committee_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    chamber TEXT,            -- 'Senate' / 'House'
    code TEXT UNIQUE         -- committee code from senate.gov
);

CREATE TABLE senator_committee (
    senator_id INT REFERENCES senator(senator_id),
    committee_id INT REFERENCES committee(committee_id),
    role TEXT,               -- Chair, Ranking Member, Member
    start_date DATE,
    end_date DATE,
    PRIMARY KEY (senator_id, committee_id, start_date)
);

-- companies & prices
CREATE TABLE company (
    company_id SERIAL PRIMARY KEY,
    ticker TEXT UNIQUE NOT NULL,
    name TEXT,
    sector TEXT,
    industry TEXT
);

CREATE TABLE price_history (
    company_id INT REFERENCES company(company_id),
    trade_date DATE,
    close NUMERIC(18,4),
    volume BIGINT,
    market_cap NUMERIC(20,2),
    PRIMARY KEY (company_id, trade_date)
);

-- bills & status
CREATE TABLE bill (
    bill_id SERIAL PRIMARY KEY,
    external_bill_id TEXT UNIQUE NOT NULL,  -- e.g. 'S.123-118'
    title TEXT,
    summary TEXT,
    chamber TEXT,
    congress INT,
    introduced_date DATE,
    sector TEXT  -- your classification of which sector it hits
);

CREATE TABLE bill_status_history (
    bill_status_id SERIAL PRIMARY KEY,
    bill_id INT REFERENCES bill(bill_id),
    status TEXT,             -- 'Introduced', 'Reported by Committee', etc.
    status_date DATE,
    raw_source TEXT          -- URL or source label
);

CREATE TABLE bill_committee (
    bill_id INT REFERENCES bill(bill_id),
    committee_id INT REFERENCES committee(committee_id),
    PRIMARY KEY (bill_id, committee_id)
);

CREATE TABLE bill_sponsor (
    bill_id INT REFERENCES bill(bill_id),
    senator_id INT REFERENCES senator(senator_id),
    role TEXT,               -- 'Sponsor', 'Co-Sponsor'
    PRIMARY KEY (bill_id, senator_id)
);

-- lobbying
CREATE TABLE lobbying_filing (
    filing_id SERIAL PRIMARY KEY,
    client_name TEXT,
    registrant_name TEXT,
    period_start DATE,
    period_end DATE,
    amount NUMERIC(18,2),
    source_url TEXT
);

CREATE TABLE lobbying_issue (
    lobbying_issue_id SERIAL PRIMARY KEY,
    filing_id INT REFERENCES lobbying_filing(filing_id),
    issue_code TEXT,
    description TEXT,
    referenced_bill_external_id TEXT  -- join to bill.external_bill_id when possible
);

-- senator trades
CREATE TABLE senator_trade (
    trade_id SERIAL PRIMARY KEY,
    senator_id INT REFERENCES senator(senator_id),
    company_id INT REFERENCES company(company_id),
    trade_date DATE,
    transaction_type TEXT,    -- 'Buy' / 'Sell'
    amount_low NUMERIC(18,2),
    amount_high NUMERIC(18,2),
    source TEXT,              -- 'CapitolTrades', etc.
    source_url TEXT
);

-- generic “societal events” if you add macro/news later
CREATE TABLE societal_event (
    event_id SERIAL PRIMARY KEY,
    event_date DATE,
    category TEXT,            -- 'Macro', 'News', 'SocialTrend'
    description TEXT,
    metadata JSONB
);
