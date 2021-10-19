#!/usr/bin/env python

import psycopg

# open a connection (make sure to close it later)
conn = psycopg.connect("dbname=company user=gb760")

# create a cursor
cur = conn.cursor()

# execute a SQL command
query = """
select employee_id, first_name, last_name from employees;
"""
cur.execute(query)

# retrieve results
for row in cur:
    print(row)

# Try yourself: set your firstname and lastname for
# all employees whose employee ID = 123
#
# Use the UPDATE sql command

# Check if the above query worked
print("Testing if employee ID = 123 exists...")

query = """
select employee_id, first_name, last_name from employees
where employee_id = 123;
"""
cur.execute(query)

for row in cur:
    print(row)
