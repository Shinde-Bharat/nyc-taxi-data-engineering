
import logging
from pathlib import Path

import duckdb


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

INPUT_FILE = Path(
    "data/processed/yellow_tripdata_2025-01_cleaned.parquet"
)

OUTPUT_FILE = Path(
    "data/processed/yellow_tripdata_2025-01_deduplicated.parquet"
)

DB_FILE = Path("data/processed/deduplication.duckdb")


# --------------------------------------------------
# LOGGING
# --------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


# --------------------------------------------------
# GLOBAL DEDUPLICATION
# --------------------------------------------------

def run_deduplication():

    logger.info("========== GLOBAL DEDUPLICATION STARTED ==========")

    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    connection = duckdb.connect(str(DB_FILE))

    try:
        connection.execute("SET memory_limit = '1GB'")
        connection.execute("SET threads = 2")

        input_records = connection.execute(
            f"""
            SELECT COUNT(*)
            FROM read_parquet('{INPUT_FILE.as_posix()}')
            """
        ).fetchone()[0]

        logger.info("Input records: %s", input_records)

        connection.execute(
            f"""
            COPY (
                SELECT DISTINCT *
                FROM read_parquet('{INPUT_FILE.as_posix()}')
            )
            TO '{OUTPUT_FILE.as_posix()}'
            (FORMAT PARQUET, COMPRESSION ZSTD)
            """
        )

        output_records = connection.execute(
            f"""
            SELECT COUNT(*)
            FROM read_parquet('{OUTPUT_FILE.as_posix()}')
            """
        ).fetchone()[0]

        duplicates_removed = input_records - output_records

        logger.info("Duplicates removed globally: %s", duplicates_removed)
        logger.info("Output records: %s", output_records)
        logger.info("Output file: %s", OUTPUT_FILE)

        logger.info("========== GLOBAL DEDUPLICATION COMPLETED ==========")

    finally:
        connection.close()


if __name__ == "__main__":
    run_deduplication()
