# 🌦️ Weather Data Pipeline using Python and Snowflake

## 🚀 Objective

This project demonstrates a complete ETL (Extract-Transform-Load) data pipeline using **Python** and **Snowflake** to process raw weather report data and generate reporting-ready datasets.

---

## 🔍 Project Scope

### ✔️ Data Ingestion
- Ingests weather data from a **CSV file** (extensible to JSON/XML).
- Supports local or cloud storage sources (S3, etc.).

### ✔️ Data Processing with Python
- Parses and cleans raw files using `pandas`.
- Removes nulls and standardizes formats.
- Converts data into a structured format aligned with reporting schema.

### ✔️ Load into Snowflake
- Uses `snowflake-connector-python` to connect.
- Creates table if not exists.
- Loads transformed data into Snowflake using `INSERT` queries (or can be upgraded to `COPY INTO`).

### ✔️ Reporting Layer
- Generates Snowflake **views** to support analytical queries.
- Optional: Includes a Plotly Dash dashboard to visualize data.

### ✔️ Automation (Optional)
- Can schedule the ETL pipeline using `cron` or `schedule`.
- Adds logging and error handling.

---

## 📁 Folder Structure

weather_pipeline_project/
├── data/
│ └── sample_weather_data.csv
├── etl/
│ └── weather_etl.py
├── config/
│ └── snowflake_config.py
├── snowflake/
│ ├── create_schema.sql
│ ├── create_table.sql
│ └── create_views.sql
├── dashboard/
│ └── app.py
├── logs/
│ └── etl.log
├── requirements.txt
└── README.md