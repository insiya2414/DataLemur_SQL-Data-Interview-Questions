WITH repeated_payments AS (
    SELECT t1.transaction_id
    FROM transactions AS t1
    JOIN transactions AS t2
    ON t1.merchant_id = t2.merchant_id
    AND t1.credit_card_id = t2.credit_card_id
    AND t1.amount = t2.amount
    AND t1.transaction_id > t2.transaction_id  -- Ensure t1 happens after t2
    AND ABS(EXTRACT(EPOCH FROM (t1.transaction_timestamp - t2.transaction_timestamp))) <= 600
)

SELECT COUNT(DISTINCT transaction_id) AS payment_count
FROM repeated_payments;