# 🚀 PySpark 7-Day Data Engineering Practice.

A structured, hands-on PySpark learning path — from fundamentals to production-ready ETL pipelines.  
All practice is done in **Google Colab**.


## 📅 7-Day Roadmap

| Day | Topic |
|-----|-------|
| 1 | Spark Fundamentals, Architecture, SparkSession, DataFrames, Schemas, Read/Write |
| 2 | Transformations — select, filter, withColumn, when, nulls, string/date functions |
| 3 | Aggregations, groupBy, Joins, Union, Spark SQL |
| 4 | Window Functions — row_number, rank, lag, lead, running totals, top-N |
| 5 | Performance — partitions, shuffle, repartition, coalesce, cache, broadcast, skew |
| 6 | Real-World ETL — CSV/JSON/Parquet, partitioned data, incremental processing |
| 7 | Capstone Project, Revision, Mock Interview |

## 🛠️ Colab Setup

Paste this in the **first cell** of every Colab notebook:

```python
# Install PySpark
!pip install pyspark -q

# Clone this repo for data files
!git clone https://github.com/Obulreddy0/pyspark-practice.git

# Create SparkSession
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PySpark_Practice") \
    .master("local[*]") \
    .getOrCreate()

print(f"✅ Spark {spark.version} ready!")
```

## 📊 Practice Datasets

| Dataset | Description | Use Cases |
|---------|-------------|-----------|
| `customers.csv` | 15 rows — Customer master data (has nulls) | Joins, filtering, null handling |
| `orders.csv` | 25 rows — E-commerce orders | Aggregations, window functions |
| `transactions.csv` | 20 rows — Banking transactions | ETL, fraud detection scenarios |
| `products.csv` | 10 rows — Product catalog | Joins, transformations |

### Reading data in Colab:
```python
df = spark.read.option("header", "true").option("inferSchema", "true") \
    .csv("pyspark-practice/data/customers.csv")
df.show()
```

## 🎯 Learning Approach

- **Concept** → **Syntax** → **Example** → **Exercise** → **Review**
- Real-world scenarios: E-commerce, Banking, Retail
- SQL → PySpark conversions
- Debug broken code exercises
- Interview questions daily

## 👤 Author
- **obulreddy** — [GitHub](https://github.com/Obulreddy0)
