import sqlite3

import pandas as pd

conn = sqlite3.connect("employees.db")

query = """
select dept, avg(salary) as avg_salary
from employees
group by dept
having avg(salary) > 50000;
"""

print(pd.read_sql_query(query,conn))
conn.close()

# problem 1 
# find departments that have more than one employee

query1 = """
select id , dept,name
from employees
group by dept
having count(*) > 1; 
"""
print(pd.read_sql_query(query1,conn))
conn.close()

# problem 2
# find departments where the highest salary is above 70000

query2 = """
select * from employees
where salary>70000;
"""
# print(pd.read_sql_query(query2,conn))
# conn.close()

# problem3 
# for each department, show the department name , employee count ,and average salary , sorted by average salary frm highest to lowest

