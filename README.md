# 🚀 PySpark 7-Day Data Engineering Practice

A structured, hands-on PySpark learning path — from fundamentals to production-ready ETL pipelines.

## 📅 7-Day Roadmap

| Day | Topic | Folder |
|-----|-------|--------|
| 1 | Spark Fundamentals, Architecture, SparkSession, DataFrames, Schemas, Read/Write | `day1_fundamentals/` |
| 2 | Transformations — select, filter, withColumn, when, nulls, string/date functions | `day2_transformations/` |
| 3 | Aggregations, groupBy, Joins, Union, Spark SQL | `day3_aggregations_joins/` |
| 4 | Window Functions — row_number, rank, lag, lead, running totals, top-N | `day4_window_functions/` |
| 5 | Performance — partitions, shuffle, repartition, coalesce, cache, broadcast, skew | `day5_performance/` |
| 6 | Real-World ETL — CSV/JSON/Parquet, partitioned data, incremental processing | `day6_etl_pipeline/` |
| 7 | Capstone Project, Revision, Mock Interview | `day7_project/` |

## 🗂️ Project Structure

```
pyspark-practice/
├── day1_fundamentals/
│   ├── 01_spark_basics.py
│   ├── 02_dataframes_schemas.py
│   ├── 03_read_write.py
│   └── exercises.py
├── day2_transformations/
│   ├── 01_select_filter.py
│   ├── 02_withcolumn_when.py
│   ├── 03_null_handling.py
│   ├── 04_string_date_functions.py
│   └── exercises.py
├── day3_aggregations_joins/
│   ├── 01_groupby_agg.py
│   ├── 02_joins.py
│   ├── 03_union_spark_sql.py
│   └── exercises.py
├── day4_window_functions/
│   ├── 01_row_number_rank.py
│   ├── 02_lag_lead.py
│   ├── 03_running_totals_topn.py
│   └── exercises.py
├── day5_performance/
│   ├── 01_partitions_shuffle.py
│   ├── 02_cache_persist.py
│   ├── 03_broadcast_joins.py
│   ├── 04_data_skew.py
│   └── exercises.py
├── day6_etl_pipeline/
│   ├── 01_read_formats.py
│   ├── 02_transformations.py
│   ├── 03_incremental_processing.py
│   ├── etl_pipeline.py
│   └── exercises.py
├── day7_project/
│   ├── capstone_project.py
│   ├── mock_interview.md
│   └── revision_notes.md
├── data/
│   ├── customers.csv
│   ├── orders.csv
│   ├── transactions.csv
│   └── products.csv
├── utils/
│   └── spark_session.py
├── .gitignore
├── requirements.txt
└── README.md
```

## 🛠️ Setup

### Prerequisites
- Python 3.8+
- Java 8 or 11 (required by Spark)

### Installation
```bash
pip install -r requirements.txt
```

### Running Scripts
```bash
python day1_fundamentals/01_spark_basics.py
```

## 📊 Practice Datasets

| Dataset | Description | Use Cases |
|---------|-------------|-----------|
| `customers.csv` | Customer master data | Joins, filtering, null handling |
| `orders.csv` | E-commerce orders | Aggregations, window functions |
| `transactions.csv` | Banking transactions | ETL, fraud detection scenarios |
| `products.csv` | Product catalog | Joins, transformations |

## 🎯 Learning Approach

- **Concept** → **Syntax** → **Example** → **Exercise** → **Review**
- Real-world scenarios: E-commerce, Banking, Retail
- SQL → PySpark conversions
- Debug broken code exercises
- Interview questions daily

## 👤 Author
- **obulreddy** — [GitHub](https://github.com/Obulreddy0)
