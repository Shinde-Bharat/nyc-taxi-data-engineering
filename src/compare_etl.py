
import pandas as pd

from pyspark.sql import SparkSession

# Read Pandas ETL output

pandas_path = "data/processed/yellow_tripdata_2025-01_cleaned.parquet"

pandas_df = pd.read_parquet(pandas_path)

print("Pandas ETL Results")
print("Rows:", len(pandas_df))

# Start Spark
spark = (
    SparkSession.builder
    .appName("ETL-Comparison")
    .master("local[*]")
    .getOrCreate()
)

# Read raw data
raw_path = "data/raw/yellow_tripdata_2025-01.parquet"

spark_df = spark.read.parquet(raw_path)

# Apply same cleaning logic
from pyspark.sql.functions import unix_timestamp, col

spark_df = spark_df.withColumn(
    "trip_duration_minutes",
    (
        unix_timestamp(col("tpep_dropoff_datetime"))
        - unix_timestamp(col("tpep_pickup_datetime"))
    ) / 60
)

spark_df = spark_df.dropDuplicates()

spark_df = spark_df.filter(
    (col("trip_duration_minutes") > 0)
    & (col("trip_distance") >= 0)
)

print("\nPySpark ETL Results")
print("Rows:", spark_df.count())

spark.stop()
