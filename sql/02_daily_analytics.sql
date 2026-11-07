
SELECT
    CAST(tpep_pickup_datetime AS DATE) AS trip_date,
    COUNT(*) AS total_trips,
    ROUND(SUM(total_amount), 2) AS daily_revenue,
    ROUND(AVG(fare_amount), 2) AS avg_fare,
    ROUND(AVG(trip_distance), 2) AS avg_distance,
    ROUND(AVG(trip_duration_minutes), 2) AS avg_duration_minutes,
    ROUND(AVG(tip_amount), 2) AS avg_tip
FROM read_parquet(
    'data/processed/yellow_tripdata_2025-01_cleaned.parquet'
)
GROUP BY trip_date
ORDER BY trip_date;
