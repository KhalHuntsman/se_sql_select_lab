# STEP 1
import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

# STEP 2
df_first_five = pd.read_sql("""
SELECT employee_number, lastName
    FROM employees;
""", conn).head()

# STEP 3
df_five_reverse = pd.read_sql("""
SELECT lastName, employee_number
    FROM employees;
""", conn).head()

# STEP 4
df_alias = pd.read_sql("""
SELECT employee_number AS ID
    FROM employees;
""", conn).head()

# STEP 5
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
""", conn).head()

# STEP 6
df_name_length = pd.read_sql("""
SELECT length(lastName) AS name_length
    FROM employees;
""", conn).head()

# STEP 7
df_short_title = pd.read_sql("""
SELECT substr(jobTitle, 1,2) AS short_title
    FROM employees;
""", conn).head()

# STEP 8
sum_total_price = pd.read_sql("""
SELECT SUM(ROUND(priceEach * quantityOrdered, 0)) AS total_amount
FROM orderDetails;
""", conn).head()

# STEP 9
df_day_month_year = pd.read_sql("""
SELECT orderDate,
        strftime("%d", orderDate) AS day,
        strftime("%m", orderDate) AS month,
        strftime("%Y", orderDate) AS year
    FROM orderDetails;
""", conn).head()

conn.close()