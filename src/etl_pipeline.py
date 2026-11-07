
import logging
from pathlib import Path

import pandas as pd


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

RAW_FILE = Path("data/raw/yellow_tripdata_2025-01.parquet")

PROCESSED_FILE = Path(
    "data/processed/yellow_tripdata_2025-01_cleaned.parquet"
)

LOG_FILE = Path("docs/etl_pipeline.log")


# --------------------------------------------------
# LOGGING CONFIGURATION
# --------------------------------------------------

LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


# --------------------------------------------------
# EXTRACT
# --------------------------------------------------

def extract_data(file_path):
    logger.info("Starting data extraction")

    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    df = pd.read_parquet(file_path)

    logger.info("Extracted %s records", len(df))

    return df


# --------------------------------------------------
# VALIDATE
# --------------------------------------------------

def validate_data(df):
    logger.info("Starting data validation")

    required_columns = [
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime",
        "trip_distance",
        "fare_amount",
        "total_amount"
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    logger.info("Required columns validation successful")


# --------------------------------------------------
# TRANSFORM
# --------------------------------------------------

def transform_data(df):
    logger.info("Starting data transformation")

    initial_records = len(df)

    # Remove exact duplicate records
    df = df.drop_duplicates()

    duplicates_removed = initial_records - len(df)

    logger.info("Duplicates removed: %s", duplicates_removed)

    # Calculate trip duration in minutes
    df["trip_duration_minutes"] = (
        df["tpep_dropoff_datetime"]
        - df["tpep_pickup_datetime"]
    ).dt.total_seconds() / 60

    # Identify invalid trip records
    invalid_duration = df["trip_duration_minutes"] <= 0
    invalid_distance = df["trip_distance"] < 0

    invalid_records = invalid_duration | invalid_distance

    rejected_records = invalid_records.sum()

    # Remove invalid records
    df = df.loc[~invalid_records].copy()

    logger.info("Invalid records removed: %s", rejected_records)
    logger.info("Records after transformation: %s", len(df))

    return df


# --------------------------------------------------
# LOAD
# --------------------------------------------------

def load_data(df, output_path):
    logger.info("Starting data loading")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_parquet(output_path, index=False)

    logger.info("Processed data saved to %s", output_path)
    logger.info("Loaded %s records", len(df))


# --------------------------------------------------
# MAIN PIPELINE
# --------------------------------------------------

def run_pipeline():
    logger.info("========== ETL PIPELINE STARTED ==========")

    df = extract_data(RAW_FILE)

    validate_data(df)

    df = transform_data(df)

    load_data(df, PROCESSED_FILE)

    logger.info("========== ETL PIPELINE COMPLETED ==========")


if __name__ == "__main__":
    run_pipeline()
