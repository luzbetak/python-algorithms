SELECT employee_name, employee.department_id, salary
FROM  employee
JOIN
   (
      SELECT department_id, AVG(salary) AS average
      FROM employee
      GROUP BY department_id
   ) AS a

ON employee.department_id = a.department_id
WHERE  employee.salary > a.average