"""
Day 1 — Topic 1: Spark Basics & SparkSession
=============================================
Learn: What is Spark, creating SparkSession, first DataFrame
"""

import sys
sys.path.insert(0, "..")
from utils.spark_session import get_spark


# ============================================================
# 1. Create a SparkSession
# ============================================================
spark = get_spark("Day1_Spark_Basics")

# Check Spark version
print(f"Spark Version: {spark.version}")
print(f"App Name: {spark.sparkContext.appName}")
print(f"Master: {spark.sparkContext.master}")


# ============================================================
# 2. Create your first DataFrame from a Python list
# ============================================================
data = [
    (1, "Rahul", "Engineering", 75000),
    (2, "Priya", "Marketing", 65000),
    (3, "Amit", "Engineering", 80000),
    (4, "Sneha", "HR", 60000),
    (5, "Vikram", "Marketing", 70000),
]
columns = ["emp_id", "name", "department", "salary"]

df = spark.createDataFrame(data, columns)

# Show the DataFrame
print("\n--- Employee DataFrame ---")
df.show()

# Print the schema (column names + data types)
print("--- Schema ---")
df.printSchema()

# Count rows
print(f"Total rows: {df.count()}")


# ============================================================
# 3. Read CSV file into DataFrame
# ============================================================
customers_df = (
    spark.read
    .option("header", "true")        # First row is header
    .option("inferSchema", "true")   # Auto-detect data types
    .csv("../data/customers.csv")
)

print("\n--- Customers DataFrame ---")
customers_df.show()
customers_df.printSchema()


# ============================================================
# EXERCISES — Try these yourself!
# ============================================================
# Exercise 1: Create a DataFrame of 5 products (id, name, price)
#             and display it with .show()

# Exercise 2: Read orders.csv and print its schema and row count

# Exercise 3: Read transactions.csv, show the first 5 rows only


# Stop SparkSession when done
spark.stop()
