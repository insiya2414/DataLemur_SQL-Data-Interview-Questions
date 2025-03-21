SELECT 
a.age_bucket,
ROUND(100.0* SUM(act.time_spent) FILTER (WHERE act.activity_type = 'send')/SUM(act.time_spent),2) AS send_perc, 
ROUND(100.0* SUM(act.time_spent) FILTER (WHERE act.activity_type = 'open')/SUM(act.time_spent),2) AS open_perc
FROM activities AS act 
INNER JOIN 
age_breakdown AS a 
ON act.user_id = a.user_id
WHERE activity_type IN ('open', 'send')
GROUP BY a.age_bucket;