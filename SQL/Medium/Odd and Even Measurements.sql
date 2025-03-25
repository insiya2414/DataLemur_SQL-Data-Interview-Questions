WITH odd_even_cte AS(
SELECT measurement_value, 
  CAST(measurement_time AS DATE) AS measurement_day,
  EXTRACT(DAY FROM measurement_time) AS measurement_date,
  DENSE_RANK() OVER (
  PARTITION BY EXTRACT(DAY FROM measurement_time) ORDER BY measurement_time) AS ranking
FROM measurements)

SELECT 
    measurement_day,
    SUM(CASE WHEN ranking % 2 = 1 THEN measurement_value ELSE 0 END) AS odd_sum,
    SUM(CASE WHEN ranking % 2 = 0 THEN measurement_value ELSE 0 END) AS even_sum
FROM odd_even_cte
GROUP BY measurement_day
ORDER BY 2,3 ASC;
