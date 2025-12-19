# STEP 1
# --------------------------------------------------
# Import required libraries:
# - sqlite3 for connecting to the SQLite database
# - pandas for executing SQL queries and storing results as DataFrames
import sqlite3
import pandas as pd

# Establish a connection to the SQLite database file
conn = sqlite3.connect('data.sqlite')


# STEP 2
# --------------------------------------------------
# Select the employee number and last name for all employees.
# This demonstrates a basic SELECT statement and column selection.
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName
    FROM employees;
""", conn)


# STEP 3
# --------------------------------------------------
# Select the same two columns as Step 2, but in reverse order.
# This shows that column order in SELECT determines output column order,
# not the underlying table structure.
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber
    FROM employees;
""", conn)


# STEP 4
# --------------------------------------------------
# Select the employee number and rename the column using an alias.
# AS allows us to change how the column name appears in the result set.
df_alias = pd.read_sql("""
    SELECT employeeNumber AS ID
    FROM employees;
""", conn)


# STEP 5
# --------------------------------------------------
# Classify employees as "Executive" or "Not Executive" based on job title.
# CASE acts like an if/else statement in SQL.
# The computed result is given an alias called 'role'.
df_executive = pd.read_sql("""
    SELECT firstName, lastName, jobTitle,
           CASE
             WHEN jobTitle = "President"
               OR jobTitle = "VP Sales"
               OR jobTitle = "VP Marketing"
             THEN "Executive"
             ELSE "Not Executive"
           END AS role
    FROM employees;
""", conn)


# STEP 6
# --------------------------------------------------
# Calculate the length of each employee's last name.
# LENGTH() is a SQLite string function that returns character count.
df_name_length = pd.read_sql("""
    SELECT length(lastName) AS name_length
    FROM employees;
""", conn)


# STEP 7
# --------------------------------------------------
# Extract the first two characters from each job title.
# SUBSTR(string, start, length) is used for substring extraction.
df_short_title = pd.read_sql("""
    SELECT substr(jobTitle, 1, 2) AS short_title
    FROM employees;
""", conn)


# STEP 8
# --------------------------------------------------
# Calculate the total price per order line by multiplying priceEach
# by quantityOrdered, then rounding to the nearest whole number.
# The resulting column is summed in pandas to produce a single total.
sum_total_price = pd.read_sql("""
    SELECT ROUND(priceEach * quantityOrdered, 0) AS total_price
    FROM orderDetails;
""", conn).sum()


# STEP 9
# --------------------------------------------------
# Break an order date into day, month, and year components.
# STRFTIME() extracts parts of a date in SQLite.
# A JOIN is required because orderDate lives in the orders table,
# while orderDetails ensures we only include valid order rows.
df_day_month_year = pd.read_sql("""
    SELECT o.orderDate,
           strftime('%d', o.orderDate) AS day,
           strftime('%m', o.orderDate) AS month,
           strftime('%Y', o.orderDate) AS year
    FROM orders o
    JOIN orderDetails od
      ON o.orderNumber = od.orderNumber;
""", conn)


# --------------------------------------------------
# Close the database connection once all queries are complete
conn.close()
