-- SELECT * FROM transactions;

WITH three_days_cte AS(
SELECT user_id, transaction_date,
DENSE_RANK() OVER(
PARTITION BY user_id ORDER BY transaction_date) AS num_user
FROM transactions
)

SELECT user_id
FROM three_days_cte
WHERE num_user= 3;
____________________________________________________________________________________________________________________________________
WITH consecutive_purchases AS (
    SELECT 
        user_id, 
        transaction_date,
        LEAD(transaction_date, 1) OVER (PARTITION BY user_id ORDER BY transaction_date) AS next_day_1,
        LEAD(transaction_date, 2) OVER (PARTITION BY user_id ORDER BY transaction_date) AS next_day_2
    FROM transactions
)
SELECT DISTINCT user_id
FROM consecutive_purchases
WHERE 
    next_day_1 = transaction_date + INTERVAL '1 day'
    AND next_day_2 = transaction_date + INTERVAL '2 days'
ORDER BY user_id;
