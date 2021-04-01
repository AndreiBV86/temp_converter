--CREATE TABLE students (
--
--    first_name TEXT,
--    last_name TEXT,
--    age INTEGER
--
--);
--
--CREATE TABLE employees (
--
--    first_name TEXT,
--    last_name TEXT,
--    age INTEGER
--
--);
--
--SELECT * FROM students;

INSERT INTO employees (first_name, last_name, age) VALUES ("Ivan", "Ivanov", 25);
INSERT INTO employees (first_name, last_name, age) VALUES ("Petr", "Petrov", 27);
INSERT INTO employees (first_name, last_name, age) VALUES ("Olga", "Sidorova", 22);
INSERT INTO employees (first_name, last_name, age) VALUES ("Inna", "Zaharova", 29);
INSERT INTO employees (first_name, last_name, age) VALUES ("Ivan", "Ivanov", 25);
INSERT INTO employees (first_name, last_name, age) VALUES ("Petr", "Petrov", 27);
INSERT INTO employees (first_name, last_name, age) VALUES ("Olga", "Sidorova", 22);
INSERT INTO employees (first_name, last_name, age) VALUES ("Inna", "Zaharova", 29);

SELECT first_name, age FROM employees WHERE first_name IS "Ivan";

SELECT last_name, age FROM employees WHERE last_name IS NOT "Ivanov";

SELECT last_name, age FROM employees WHERE last_name IS NOT "Ivanov" AND age IS NOT 22;

SELECT last_name, age FROM employees WHERE age <= 25;

SELECT first_name, age FROM employees WHERE first_name LIKE "I%";

SELECT * FROM employees WHERE first_name LIKE "%a" OR age IS 25;

SELECT * FROM employees WHERE last_name LIKE "%ro%";

UPDATE employees SET first_name="Oleg" WHERE first_name=" Ivan";

DELETE FROM employees WHERE age IS 27;


