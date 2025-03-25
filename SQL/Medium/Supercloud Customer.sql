WITH supercloud_cte AS (
    SELECT c.customer_id, p.product_category, c.product_id,
           DENSE_RANK() OVER (PARTITION BY c.customer_id ORDER BY c.product_id) AS ranking
    FROM customer_contracts AS c
    INNER JOIN products AS p
    ON c.product_id = p.product_id
)

SELECT customer_id
FROM supercloud_cte
WHERE product_category IN ('Analytics', 'Containers', 'Compute')
GROUP BY customer_id
HAVING COUNT(DISTINCT product_category) = 3;

