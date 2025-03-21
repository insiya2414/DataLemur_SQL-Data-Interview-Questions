WITH second_highest_employee AS(
SELECT employee_id, salary,
DENSE_RANK() OVER(
ORDER BY salary DESC) AS second_highest_salary_of_employee
FROM employee)

SELECT 
salary
FROM second_highest_employee
WHERE second_highest_salary_of_employee = 2