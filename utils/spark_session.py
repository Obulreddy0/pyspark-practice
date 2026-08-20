"""
Reusable SparkSession factory for all practice scripts.
Usage:
    from utils.spark_session import get_spark

    spark = get_spark("Day1_Basics")
"""

from pyspark.sql import SparkSession


def get_spark(app_name: str = "PySpark_Practice") -> SparkSession:
    """Create or get a SparkSession configured for local practice."""
    spark = (
        SparkSession.builder
        .appName(app_name)
        .master("local[*]")              # Use all available local cores
        .config("spark.sql.shuffle.partitions", "8")   # Reduce for local mode
        .config("spark.driver.memory", "2g")
        .config("spark.sql.legacy.timeParserPolicy", "LEGACY")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")   # Reduce noisy logs
    return spark
