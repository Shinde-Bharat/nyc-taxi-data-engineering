
from datetime import datetime
import subprocess

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator


# --------------------------------------------------
# TASK 1: PANDAS ETL
# --------------------------------------------------

def run_pandas_etl():
    subprocess.run(
        ["python", "/opt/airflow/src/etl_pipeline.py"],
        check=True,
    )


# --------------------------------------------------
# TASK 2: GLOBAL DEDUPLICATION USING DUCKDB
# --------------------------------------------------

def run_global_deduplication():
    subprocess.run(
        ["python", "/opt/airflow/src/global_deduplication.py"],
        check=True,
    )


# --------------------------------------------------
# TASK 3: DATA VALIDATION
# --------------------------------------------------

def validate_data():
    subprocess.run(
        ["python", "/opt/airflow/src/verify_etl.py"],
        check=True,
    )


# --------------------------------------------------
# DAG CONFIGURATION
# --------------------------------------------------

with DAG(
    dag_id="nyc_taxi_etl_pipeline",
    description="NYC Taxi Data Engineering Pipeline with Pandas, DuckDB and Airflow",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["nyc-taxi", "data-engineering", "duckdb"],
) as dag:

    # Pandas ETL
    etl = PythonOperator(
        task_id="pandas_etl",
        python_callable=run_pandas_etl,
    )

    # Global deduplication
    deduplication = PythonOperator(
        task_id="global_deduplication",
        python_callable=run_global_deduplication,
    )

    # Validation
    validation = PythonOperator(
        task_id="validate_data",
        python_callable=validate_data,
    )

    # Task dependencies
    etl >> deduplication >> validation
