
import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession
from pyspark.sql.functions import unix_timestamp, col

# Create Spark session
spark = (
    SparkSession.builder
    .appName("NYC-Taxi-PySpark-ETL")
    .master("local[*]")
    .config("spark.hadoop.hadoop.security.authentication", "simple")
    .config("spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version", "2")
    .getOrCreate()
)
print("Spark Version:", spark.version)

# Read raw dataset
input_path = "data/raw/yellow_tripdata_2025-01.parquet"

df = spark.read.parquet(input_path)

print("Original Schema:")
df.printSchema()

print("Original Row Count:", df.count())

# Calculate trip duration
df = df.withColumn(
    "trip_duration_minutes",
    (
        unix_timestamp(col("tpep_dropoff_datetime"))
        - unix_timestamp(col("tpep_pickup_datetime"))
    ) / 60
)

# Remove duplicates
df = df.dropDuplicates()

# Remove invalid trips
df = df.filter(
    (col("trip_duration_minutes") > 0)
    & (col("trip_distance") >= 0)
)

print("Cleaned Row Count:", df.count())

# Save processed dataset
output_path = "data/processed/yellow_tripdata_2025-01_spark"

# df.write.mode("overwrite").parquet(output_path)

print("PySpark transformations completed!")

print("PySpark ETL Completed Successfully!")

spark.stop()
