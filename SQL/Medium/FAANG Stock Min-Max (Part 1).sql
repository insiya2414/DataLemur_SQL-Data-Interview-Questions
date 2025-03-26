WITH MonthlyOpenPrices AS (
    SELECT 
        ticker,
        TO_CHAR(date, 'Mon-YYYY') AS month_year,        
        open,
        RANK() OVER (PARTITION BY ticker ORDER BY open DESC) AS high_rank,
        RANK() OVER (PARTITION BY ticker ORDER BY open ASC) AS low_rank
    FROM stock_prices
)
SELECT 
    h.ticker,
    h.month_year AS highest_mth,
    h.open AS highest_open,
    l.month_year AS lowest_mth,
    l.open AS lowest_open
FROM MonthlyOpenPrices h
JOIN MonthlyOpenPrices l ON h.ticker = l.ticker
WHERE h.high_rank = 1 AND l.low_rank = 1
ORDER BY h.ticker;

