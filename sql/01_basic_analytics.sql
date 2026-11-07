
-- 1. Total taxi trips
SELECT COUNT(*) AS total_trips
FROM read_parquet('data/processed/yellow_tripdata_2025-01_cleaned.parquet');

-- 2. Total revenue
SELECT ROUND(SUM(total_amount), 2) AS total_revenue
FROM read_parquet('data/processed/yellow_tripdata_2025-01_cleaned.parquet');

-- 3. Average trip distance
SELECT ROUND(AVG(trip_distance), 2) AS average_distance
FROM read_parquet('data/processed/yellow_tripdata_2025-01_cleaned.parquet');

-- 4. Revenue by payment type
SELECT payment_type,
       COUNT(*) AS total_trips,
       ROUND(SUM(total_amount), 2) AS revenue
FROM read_parquet('data/processed/yellow_tripdata_2025-01_cleaned.parquet')
GROUP BY payment_type
ORDER BY revenue DESC;

-- 5. Top 10 pickup locations
SELECT PULocationID,
       COUNT(*) AS total_pickups
FROM read_parquet('data/processed/yellow_tripdata_2025-01_cleaned.parquet')
GROUP BY PULocationID
ORDER BY total_pickups DESC
LIMIT 10;
