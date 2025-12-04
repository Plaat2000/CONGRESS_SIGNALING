-- trades within +/- 5 days of a bill status change
-- where the bill sector matches the company sector
CREATE OR REPLACE VIEW v_suspicious_trades AS
SELECT
    st.trade_id,
    s.full_name AS senator,
    c.ticker,
    c.sector AS company_sector,
    st.trade_date,
    st.transaction_type,
    b.external_bill_id,
    b.title AS bill_title,
    b.sector AS bill_sector,
    bsh.status,
    bsh.status_date,
    (st.trade_date - bsh.status_date) AS days_diff
FROM senator_trade st
JOIN senator s ON s.senator_id = st.senator_id
JOIN company c ON c.company_id = st.company_id
JOIN bill b ON b.sector = c.sector
JOIN bill_status_history bsh ON bsh.bill_id = b.bill_id
WHERE ABS(st.trade_date - bsh.status_date) <= 5
ORDER BY ABS(st.trade_date - bsh.status_date), st.trade_date DESC;