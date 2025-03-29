WITH user_activity AS (
  SELECT user_id,
         EXTRACT(MONTH FROM event_date) AS event_month
  FROM user_actions
  WHERE event_date >= '2022-06-01' AND event_date < '2022-08-01'  -- Only considering June and July
  GROUP BY user_id, event_month
)

SELECT 7 AS month, 
COUNT(DISTINCT ua1.user_id) AS monthly_active_users
FROM user_activity ua1
JOIN user_activity ua2
  ON ua1.user_id = ua2.user_id  
  AND ua1.event_month = 6  
  AND ua2.event_month = 7  




