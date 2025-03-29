SELECT 
ROUND(100.0 * COUNT(*) FILTER (WHERE call_category= 'n/a'OR call_category IS NULL)/ COUNT(*),1)
FROM callers;
_____________________________________________________________________________________________________________________________________

WITH uncategorised_call_cte AS (
SELECT
COUNT(policy_holder_id) AS total_policy_holders,
COUNT(policy_holder_id) FILTER (WHERE call_category= 'n/a' OR call_category IS NULL) AS policy_holders_na
FROM callers)

SELECT ROUND(100.0 * policy_holders_na/(total_policy_holders),1) 
AS uncategorised_call_pct
FROM uncategorised_call_cte;