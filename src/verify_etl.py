
import pandas as pd
from pathlib import Path

RAW_FILE = Path("data/raw/yellow_tripdata_2025-01.parquet")

PROCESSED_FILE = Path(
    "data/processed/yellow_tripdata_2025-01_cleaned.parquet"
)

# Check output file
if not PROCESSED_FILE.exists():
    raise FileNotFoundError("Processed dataset not found!")

# Read raw and processed datasets
raw_df = pd.read_parquet(RAW_FILE)
processed_df = pd.read_parquet(PROCESSED_FILE)

print("\n========== ETL VERIFICATION ==========")

print("Raw Records:", len(raw_df))
print("Processed Records:", len(processed_df))
print("Records Removed:", len(raw_df) - len(processed_df))

print("\nProcessed Dataset Shape:", processed_df.shape)

print("\nDuplicate Records:",
      processed_df.duplicated().sum())

print("\nInvalid Trip Duration:",
      (processed_df["trip_duration_minutes"] <= 0).sum())

print("\nNegative Trip Distance:",
      (processed_df["trip_distance"] < 0).sum())

print("\nOutput File Size:",
      round(PROCESSED_FILE.stat().st_size / (1024 * 1024), 2),
      "MB")

print("\n========== VERIFICATION COMPLETED ==========")
