
import os
import sys

# Tell Spark to use our active virtual environment Python
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("NYC-Taxi-Data-Engineering")
    .master("local[*]")
    .getOrCreate()
)

print("Python Interpreter:", sys.executable)
print("Spark Version:", spark.version)

data = [
    ("Taxi A", 10.5),
    ("Taxi B", 15.2),
    ("Taxi C", 8.7),
]

df = spark.createDataFrame(
    data,
    ["taxi_name", "trip_distance"]
)

df.show()

print("Total trips:", df.count())

spark.stop()
