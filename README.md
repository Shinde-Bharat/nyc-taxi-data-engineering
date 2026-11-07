
# 🚖 NYC Taxi Data Engineering Pipeline

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white"/>
  <img src="https://img.shields.io/badge/DuckDB-FFF000?style=for-the-badge&logo=duckdb&logoColor=black"/>
  <img src="https://img.shields.io/badge/Parquet-50ABF1?style=for-the-badge&logo=apache&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
</p>

## 📌 Project Overview

An end-to-end **Data Engineering project** built using NYC Yellow Taxi trip data for January 2025.

This project demonstrates data ingestion, profiling, cleaning, validation, SQL analytics, and distributed data processing using Python, Pandas, PySpark, and DuckDB.

## 🎯 Project Objectives

- 📥 Ingest NYC Taxi trip data in Parquet format.
- 🔍 Perform data inspection and profiling.
- 🧹 Clean and validate millions of trip records.
- 🐼 Build a Pandas ETL pipeline.
- ⚡ Implement distributed processing using PySpark.
- 🦆 Perform analytical queries using DuckDB SQL.
- ✅ Validate Pandas and PySpark transformation results.
- ☁️ Extend the pipeline with cloud storage and orchestration.

## 📊 Dataset

| Property | Details |
|---|---|
| 🚕 Dataset | NYC Yellow Taxi Trip Records |
| 📅 Period | January 2025 |
| 📦 Format | Parquet |
| 📈 Raw Records | 3,475,226 |
| 🧹 Cleaned Records | 3,473,175 |
| 🌐 Source | NYC Taxi & Limousine Commission |

🔗 [Official NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Pipeline development |
| 🐼 Pandas | Data cleaning and transformation |
| ⚡ PySpark | Distributed data processing |
| 🦆 DuckDB | SQL analytics |
| 🗂️ Parquet | Columnar data storage |
| 🔧 Git | Version control |
| 🐙 GitHub | Code hosting and collaboration |

## 🏗️ Pipeline Architecture

```text
              🚕 NYC TLC Dataset
                      |
                      ▼
               📥 Data Ingestion
                      |
                      ▼
             🔍 Data Inspection
                      |
                      ▼
              📊 Data Profiling
                      |
                      ▼
             🐼 Pandas ETL
                      |
                      ▼
           🧹 Cleaning & Validation
                      |
                      ▼
             🗂️ Processed Parquet
                 /          \
                ▼            ▼
        🦆 DuckDB SQL    ⚡ PySpark
          Analytics       Processing
                \            /
                 ▼          ▼
              ✅ ETL Validation
```

## 📂 Project Structure

```text
nyc-taxi-data-engineering/
│
├── 📁 data/
│   ├── raw/
│   └── processed/
│
├── 📁 docs/
│
├── 📁 notebooks/
│
├── 📁 sql/
│   ├── 01_basic_analytics.sql
│   └── 02_daily_analytics.sql
│
├── 📁 src/
│   ├── inspect_dataset.py
│   ├── profile_dataset.py
│   ├── etl_pipeline.py
│   ├── verify_etl.py
│   ├── run_sql.py
│   ├── run_daily_analytics.py
│   ├── pyspark_etl.py
│   ├── compare_etl.py
│   └── test_spark.py
│
├── 📄 .gitignore
└── 📄 README.md
```

## ⚙️ Data Engineering Workflow

### 1️⃣ Data Inspection
- Read Parquet dataset.
- Inspect schema and data types.
- Analyze missing values.
- Understand dataset structure.

### 2️⃣ Data Profiling
- Identify duplicate records.
- Detect invalid trip distances.
- Analyze fare amounts.
- Investigate trip duration anomalies.

### 3️⃣ Pandas ETL Pipeline
- Validate required columns.
- Remove duplicate records.
- Calculate trip duration.
- Remove invalid trip durations.
- Filter negative trip distances.
- Export cleaned data to Parquet.

### 4️⃣ SQL Analytics with DuckDB
- 💰 Total trip revenue.
- 🚕 Total trips.
- 📏 Average trip distance.
- 💳 Revenue by payment type.
- 📍 Top pickup locations.
- 📅 Daily trip and revenue analysis.

### 5️⃣ PySpark Processing
- Read raw Parquet data.
- Apply transformations.
- Calculate trip duration.
- Remove duplicate records.
- Filter invalid records.

### 6️⃣ ETL Validation
Compared processed record counts between Pandas and PySpark.

| Processing Engine | Records |
|---|---:|
| 🐼 Pandas | 3,473,175 |
| ⚡ PySpark | 3,473,175 |

✅ Both implementations produced matching record counts.

## 🚀 Getting Started

### 📥 Clone Repository

```bash
git clone https://github.com/Shinde-Bharat/nyc-taxi-data-engineering.git
cd nyc-taxi-data-engineering
```

### 🐍 Create Virtual Environment

```bash
python -m venv .venv
```

Activate on Windows:

```cmd
.venv\Scripts\activate
```

### 📦 Install Dependencies

```bash
pip install pandas pyarrow duckdb pyspark
```

### 📊 Download Dataset

Download January 2025 Yellow Taxi data:

🔗 https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-01.parquet

Place it inside:

```text
data/raw/
```

### ▶️ Run Pipeline

```bash
python src/inspect_dataset.py
python src/profile_dataset.py
python src/etl_pipeline.py
python src/verify_etl.py
python src/run_sql.py
python src/run_daily_analytics.py
python src/pyspark_etl.py
python src/compare_etl.py
```

## 📌 Project Progress

- [x] 📥 Data ingestion
- [x] 🔍 Data inspection
- [x] 📊 Data profiling
- [x] 🐼 Pandas ETL
- [x] ✅ ETL validation
- [x] 🦆 DuckDB SQL analytics
- [x] 📅 Daily analytics
- [x] ⚡ PySpark transformations
- [x] 🔄 Pandas vs PySpark comparison
- [x] 🐙 GitHub repository
- [ ] 🌬️ Apache Airflow orchestration
- [ ] ☁️ AWS S3 integration
- [ ] 📈 Power BI dashboard

## 🔮 Future Enhancements

- 🌬️ Automate workflows using Apache Airflow.
- ☁️ Store processed data in AWS S3.
- 🔎 Implement cloud-based analytical queries.
- 📊 Build interactive Power BI dashboards.
- 🏭 Develop a production-style data pipeline.

## 👨‍💻 Author

**Bharat Shinde**

🔗 GitHub: [@Shinde-Bharat](https://github.com/Shinde-Bharat)

---

<p align="center">
  ⭐ If you find this project interesting, consider giving it a star!
</p>
