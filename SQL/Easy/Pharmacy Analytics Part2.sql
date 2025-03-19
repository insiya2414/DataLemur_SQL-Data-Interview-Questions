SELECT 
  manufacturer, 
  COUNT(drug) AS drug_count,
  SUM(cogs - total_sales) AS total_loss
FROM pharmacy_sales
WHERE (cogs - total_sales) >=0
GROUP BY 1
ORDER BY 3 DESC;