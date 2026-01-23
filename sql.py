import sqlite3
conn = sqlite3.connect("sample-database.db")
cur = conn.cursor()
cur.execute("SELECT * FROM employees LIMIT 3")
ans = cur.fetchall()
for i in ans:
    print(i)

cur.close()
conn.close()

import sqlite3
from contextlib import closing

def get_connection(database_path):
    return closing(sqlite3.connect(database_path))

def create_employee(database_path, first_name, last_name, email, phone_number, employee_id, hire_date, job_id, salary, manager_id, department_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO employees (first_name, last_name, email, phone_number, employee_id, hire_date, job_id, salary, manager_id, department_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ? )", (first_name, last_name))
        connection.commit()
        return cursor.lastrowid


def get_employee(database_path, employee_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees WHERE id=?", (employee_id,))
        return cursor.fetchone()


def update_employee(database_path, employee_id, name=None, bio=None):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        if name:
            cursor.execute("UPDATE employees SET name=? WHERE id=?", (name, employee_id))
        if bio:
            cursor.execute("UPDATE employees SET bio=? WHERE id=?", (bio, employee_id))
        connection.commit()


def delete_employee(database_path, employee_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM employees WHERE id=?", (employee_id,))
        connection.commit()

