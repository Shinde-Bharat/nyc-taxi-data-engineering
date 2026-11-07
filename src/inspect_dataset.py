
import pandas as pd
from pathlib import Path

# Define dataset path
DATA_PATH = Path("data/raw/yellow_tripdata_2025-01.parquet")

# Check whether the file exists
if not DATA_PATH.exists():
    raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

# Read the dataset
df = pd.read_parquet(DATA_PATH)

# Display basic information
print("\n--- FIRST 5 RECORDS ---")
print(df.head())

print("\n--- DATASET SHAPE ---")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())
