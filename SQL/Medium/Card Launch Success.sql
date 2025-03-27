WITH cards_cte AS (
SELECT card_name, issued_amount, issue_month, issue_year,
DENSE_RANK() OVER(
PARTITION BY card_name ORDER BY issue_year, issue_month) AS ranking
FROM monthly_cards_issued)

SELECT card_name, issued_amount
FROM cards_cte
WHERE ranking = 1
ORDER BY 2 DESC;

____________________________________________________________________________________________________________________________________

-- DataLemur Solution:
WITH card_launch AS (
  SELECT 
    card_name,
    issued_amount,
    MAKE_DATE(issue_year, issue_month, 1) AS issue_date,
    MIN(MAKE_DATE(issue_year, issue_month, 1)) OVER (
      PARTITION BY card_name) AS launch_date
  FROM monthly_cards_issued
)

SELECT 
  card_name, 
  issued_amount
FROM card_launch
WHERE issue_date = launch_date
ORDER BY issued_amount DESC;