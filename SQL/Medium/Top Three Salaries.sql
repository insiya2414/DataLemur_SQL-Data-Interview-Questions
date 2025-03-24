WITH high_earners_cte AS(
    SELECT d.department_name, e.name, e.salary,
    DENSE_RANK () OVER (
    PARTITION BY d.department_id ORDER BY e.salary DESC 
    ) AS high_salary
    FROM employee AS e
    INNER JOIN department AS d
    ON e.department_id = d.department_id)

SELECT department_name, name, salary
FROM high_earners_cte
WHERE high_salary <= 3
ORDER BY department_name ASC,salary DESC, name ASC;
