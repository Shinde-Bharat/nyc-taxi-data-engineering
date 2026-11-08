
from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator


def start_pipeline():
    print("NYC Taxi ETL Pipeline Started!")


def finish_pipeline():
    print("NYC Taxi ETL Pipeline Completed!")


with DAG(
    dag_id="nyc_taxi_etl_pipeline",
    description="NYC Taxi Data Engineering Pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["nyc-taxi", "data-engineering"],
) as dag:

    start = PythonOperator(
        task_id="start_pipeline",
        python_callable=start_pipeline,
    )

    finish = PythonOperator(
        task_id="finish_pipeline",
        python_callable=finish_pipeline,
    )

    start >> finish
