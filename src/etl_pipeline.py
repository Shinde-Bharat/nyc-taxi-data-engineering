
import logging
from pathlib import Path

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

RAW_FILE = Path("data/raw/yellow_tripdata_2025-01.parquet")
PROCESSED_FILE = Path(
    "data/processed/yellow_tripdata_2025-01_cleaned.parquet"
)
LOG_FILE = Path("docs/etl_pipeline.log")

BATCH_SIZE = 100_000


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
    ],
    force=True,
)

logger = logging.getLogger(__name__)


# --------------------------------------------------
# VALIDATE
# --------------------------------------------------

def validate_columns(columns):
    required_columns = [
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime",
        "trip_distance",
        "fare_amount",
        "total_amount",
    ]

    missing_columns = [
        column for column in required_columns
        if column not in columns
    ]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    logger.info("Required columns validation successful")


# --------------------------------------------------
# TRANSFORM
# --------------------------------------------------

def transform_data(df):
    initial_records = len(df)

    # Remove duplicates within the current batch
    df = df.drop_duplicates()

    duplicates_removed = initial_records - len(df)

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

    return df, duplicates_removed, rejected_records


# --------------------------------------------------
# MAIN PIPELINE
# --------------------------------------------------

def run_pipeline():
    logger.info("========== ETL PIPELINE STARTED ==========")

    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {RAW_FILE}")

    parquet_file = pq.ParquetFile(RAW_FILE)

    validate_columns(parquet_file.schema.names)

    PROCESSED_FILE.parent.mkdir(parents=True, exist_ok=True)

    total_input = 0
    total_output = 0
    total_duplicates = 0
    total_rejected = 0

    writer = None

    try:
        for batch_number, batch in enumerate(
            parquet_file.iter_batches(batch_size=BATCH_SIZE),
            start=1,
        ):
            df = batch.to_pandas()

            total_input += len(df)

            df, duplicates, rejected = transform_data(df)

            total_duplicates += duplicates
            total_rejected += rejected
            total_output += len(df)

            if not df.empty:
                table = pa.Table.from_pandas(df, preserve_index=False)

                if writer is None:
                    writer = pq.ParquetWriter(
                        PROCESSED_FILE,
                        table.schema,
                    )
                else:
                    table = table.cast(writer.schema, safe=False)

                writer.write_table(table)

            logger.info(
                "Batch %s | Input: %s | Output: %s",
                batch_number,
                len(batch),
                len(df),
            )

            del df
            del batch

    finally:
        if writer is not None:
            writer.close()

    logger.info("Input records: %s", total_input)
    logger.info("Duplicates removed: %s", total_duplicates)
    logger.info("Invalid records removed: %s", total_rejected)
    logger.info("Output records: %s", total_output)
    logger.info("Processed data saved to %s", PROCESSED_FILE)

    logger.info("========== ETL PIPELINE COMPLETED ==========")


if __name__ == "__main__":
    run_pipeline()
