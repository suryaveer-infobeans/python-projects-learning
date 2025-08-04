# 🌦️ Weather Data Pipeline using Python and Snowflake

## 🚀 Objective

This project demonstrates a complete ETL (Extract-Transform-Load) data pipeline using **Python** and **Snowflake** to process raw weather report data and generate reporting-ready datasets.

---

## 🔍 Project Scope

### ✔️ 1. Data Ingestion

- Reads weather data from a **CSV file** (extensible to JSON/XML).
- Supports local file system and cloud sources (e.g., AWS S3).

### ✔️ 2. Data Processing with Python

- Cleans and transforms raw data using `pandas`.
- Handles nulls, missing values, and standardizes formats.
- Converts data into a structured format aligned with a reporting schema.

### ✔️ 3. Load into Snowflake

- Uses `snowflake-connector-python` and `snowflake.snowpark` to connect.
- Auto-creates the target table if it doesn’t exist.
- Loads transformed data using `write_pandas` or standard `INSERT` queries.
- Supports schema evolution and proper type casting (e.g., `DATE` fields).

### ✔️ 4. Reporting Layer

- Creates **views** in Snowflake to simplify analytical queries.
- Optional: Interactive dashboard built with **Plotly Dash** for visualizing weather trends.

### ✔️ 5. Automation & Logging *(Optional)*

- Supports scheduling with `cron` or Python’s `schedule` module.
- Includes structured logging and error handling for observability.

---

## 📁 Folder Structure

```bash
weather_pipeline_project/
├── config/
│   └── snowflake_config.py         # Snowflake connection config (uses .env)
├── data/
│   └── sample_weather_data.csv     # Sample raw weather data
├── etl/
│   └── weather_etl.py              # Main ETL script
├── dashboard/
│   └── app.py                      # Dash dashboard code
├── snowflake/
│   ├── create_schema.sql           # Schema creation SQL
│   ├── create_table.sql            # Table DDL
│   └── create_views.sql            # Reporting views
├── logs/
│   └── etl.log                     # ETL logs
├── .env                                # Environment variables (excluded in .gitignore)
├── requirements.txt                    # Python dependencies
└── README.md                       # Project documentation
```

---

## 🔧 Setup Instructions

### 1. 📦 Install Requirements

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. 🛠️ Set up `.env`

Create a `.env` file in the root directory:

```ini
SNOWFLAKE_ACCOUNT=your_account_id
SNOWFLAKE_USER=your_username
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_ROLE=SYSADMIN
SNOWFLAKE_WAREHOUSE=COMPUTE_WH
SNOWFLAKE_DATABASE=WEATHER_DB
SNOWFLAKE_SCHEMA=PUBLIC
```

### 3. 🏃‍♂️ Run ETL

```bash
python etl/weather_etl.py
```

### 4. 📊 Launch Dashboard

```bash
python dashboard/app.py
```

Open in browser: [http://localhost:8050](http://localhost:8050)

---

## 📈 Example Output

- **Table:** `WEATHER_DATA`
- **Views:** `vw_daily_temperature`, `vw_average_humidity`, etc.
- **Dashboard:** Interactive graphs showing weather trends by station and date.

---



