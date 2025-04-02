WITH company_cte AS (
    SELECT 
        e.department_id, 
        TO_CHAR(s.payment_date, 'MM-YYYY') AS payment_date,
        s.amount
    FROM employee AS e
    INNER JOIN salary AS s
        ON e.employee_id = s.employee_id
    WHERE TO_CHAR(s.payment_date, 'MM-YYYY') = '03-2024'  -- Filtering for March 2024
),
department_avg AS (
    SELECT 
        department_id, 
        payment_date, 
        AVG(amount) AS dept_avg_salary
    FROM company_cte
    GROUP BY department_id, payment_date
),
company_avg AS (
    SELECT 
        payment_date, 
        AVG(amount) AS company_avg_salary
    FROM company_cte
    GROUP BY payment_date
)
SELECT 
    d.department_id,
    d.payment_date,
    CASE 
        WHEN d.dept_avg_salary > c.company_avg_salary THEN 'higher'
        WHEN d.dept_avg_salary < c.company_avg_salary THEN 'lower'
        ELSE 'same'
    END AS comparison
FROM department_avg d
JOIN company_avg c
    ON d.payment_date = c.payment_date
ORDER BY d.department_id;




