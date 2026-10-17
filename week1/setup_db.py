import sqlite3

conn = sqlite3.connect("employees.db")

cur = conn.cursor()

cur.execute("drop table if exists employees")
cur.execute("""
    create table employees(
        id integer primary key,
        name text,
        dept text,
        salary integer
    )
""")

cur.executemany(
    "insert into employees values(? , ? , ?, ?)",
    [
        (1,"Asha","IT",60000),
        (2,"Ravi", "IT",80000),
        (3,"Meera","HR",50000),
        (4,"Kiran","HR",52000),
        (5,"Sana","Sales",55000),
    ],
)
conn.commit()
conn.close()