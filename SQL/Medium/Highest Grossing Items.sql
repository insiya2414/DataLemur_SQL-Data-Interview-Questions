WITH spent_cte AS( SELECT category, product, 
    SUM(spend) AS total_spend,
    RANK () OVER(
    PARTITION BY category
    ORDER BY SUM(spend) DESC) AS high
    FROM product_spend
WHERE EXTRACT(YEAR FROM transaction_date) = 2022
GROUP BY product, category)

SELECT category, product, total_spend
FROM spent_cte
WHERE high <=2
ORDER BY category, high;