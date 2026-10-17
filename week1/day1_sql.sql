-- SQLite
select
dept as department_name,
count(id) as employee_count,
avg(salary) as average_salary
from employees
group by dept
order by avg(salary) desc;

select dept as department_name,
sum(salary) as total_salary
from employees
GROUP BY dept
having sum(salary) between 100000 and 150000;
