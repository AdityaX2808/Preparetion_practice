-- SQLite
select * from employees_ties;

--  SQL 1: Rank every employee within their department by salary (highest first), using RANK()

select id , name ,dept,
salary,
dense_rank() over(PARTITION BY dept ORDER BY salary DESC) as salary_rank
from employees_ties;

--2: Highest-paid employee in each department, using a CTE and ROW_NUMBER()
with ranked_employees as(
    SELECT
    id,
    name, 
    dept,
    salary,
    ROW_NUMBER() OVER(PARTITION BY dept ORDER BY salary desc,id) as rank_employ
    from employees_ties
)

select id,
name,
dept,
salary,
rank_employ
from ranked_employees
where rank_employ = 1; 


-- SQL 3: Second highest salary overall, using DENSE_RANK()
with salary_ranked as (
    SELECT id ,  name , dept, salary,
    dense_rank()over (order by salary desc,id) as salary_rank
    from employees_ties)
    select * from salary_ranked
    where salary_rank = 2

-- -- SQL 4 (tie experiment): On employees_ties, show name, dept, salary plus
-- ROW_NUMBER(), RANK() and DENSE_RANK() side by side, partitioned by dept

SELECT
    id,
    name,
    dept,
    salary,
    ROW_NUMBER() OVER (
        PARTITION BY dept ORDER BY salary DESC
    ) AS row_num,
    RANK() OVER (
        PARTITION BY dept ORDER BY salary DESC
    ) AS salary_rank,
    DENSE_RANK() OVER (
        PARTITION BY dept ORDER BY salary DESC
    ) AS dense_salary_rank
FROM employees_ties;