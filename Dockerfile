
FROM apache/airflow:3.4.0

RUN pip install --no-cache-dir duckdb==2.0.0
