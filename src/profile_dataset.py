
import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/raw/yellow_tripdata_2025-01.parquet")

# Load dataset
df = pd.read_parquet(DATA_PATH)

print("\n========== DATA PROFILE ==========")

# 1. Dataset overview
print("\nTotal Records:", len(df))
print("Total Columns:", len(df.columns))

# 2. Missing values analysis
print("\n========== MISSING VALUES ==========")

missing = df.isnull().sum()
missing_percentage = (missing / len(df)) * 100

missing_report = pd.DataFrame({
    "Missing_Count": missing,
    "Missing_Percentage": missing_percentage
})

print(missing_report[missing_report["Missing_Count"] > 0])

# 3. Duplicate records
print("\n========== DUPLICATE RECORDS ==========")
print("Duplicate Rows:", df.duplicated().sum())

# 4. Trip distance validation
print("\n========== TRIP DISTANCE ==========")
print("Zero Distance:", (df["trip_distance"] == 0).sum())
print("Negative Distance:", (df["trip_distance"] < 0).sum())

# 5. Fare validation
print("\n========== FARE VALIDATION ==========")
print("Zero Fare:", (df["fare_amount"] == 0).sum())
print("Negative Fare:", (df["fare_amount"] < 0).sum())

# 6. Trip duration calculation
print("\n========== TRIP DURATION ==========")

df["trip_duration_minutes"] = (
    df["tpep_dropoff_datetime"] -
    df["tpep_pickup_datetime"]
).dt.total_seconds() / 60

print("Negative Duration:", (df["trip_duration_minutes"] < 0).sum())
print("Zero Duration:", (df["trip_duration_minutes"] == 0).sum())

print("\n========== COMPLETED ==========")
