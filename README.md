# Lab 06

## Create the database

   * Run the command in your terminal: `psql`
   * Then run the SQL command: `create database company;`
   * Check if the database was created: `\l`
   * Press `q` to close the scrolling screen
   * Exit PostgreSQL: `\q`

## Import the SQL file

Run the command in the terminal:

```
cd ~
git clone git@github.com:GENBUS760/Lab06.git
cd Lab06
psql company < indexes.sql
```

Then check if the tables were imported:

   * Run the command in your terminal: `psql`
   * Select the database you created: `\c company`
   * List all tables: `\dt`
   * Then run the SQL command: `select * from employees;`
   * Quit PostgreSQL: `\q`

## Update the database with Python

   * Install the psycopg library: `pip install psycopg`
   * Read and run the Python script `indexes.py`
   * Modify the Python script to insert your name into the `employees` table. See the Python script for details.
   * Run the Python script again: `python indexes.py`

## Add the subsidiary ID column (after the company merger)

   * Try yourself: import `subsidiary.sql` into the `company` database.
   * Try running the query from lecture to get all employees with subsidiary ID = 20.
   * How much faster/slower is the above query then the query to get all employees with ID = 123? Add `explain analyze` just before your query above to measure performance.
   * Try yourself: create an index on the subsidiary ID column.
   * Compare the speeds of the two queries above after adding this index.
