-- DROP TABLE IF EXISTS employee;
DROP TABLE employee;
CREATE TABLE IF NOT EXISTS employee (
	employee_id INTEGER,
	employee_name TEXT,
	department_id INTEGER,
	salary DECIMAL
);

INSERT INTO employee VALUES(1, 'Joseph',   100, 160000);
INSERT INTO employee VALUES(2, 'Kevin',    100, 175000);
INSERT INTO employee VALUES(3, 'Thomas',   200, 150000);
INSERT INTO employee VALUES(4, 'Stefan',   200, 135000);
INSERT INTO employee VALUES(5, 'Jay',      300, 180000);
INSERT INTO employee VALUES(6, 'Luzbetak', 300, 155000);

CREATE UNIQUE INDEX index_name ON employee(employee_id);


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