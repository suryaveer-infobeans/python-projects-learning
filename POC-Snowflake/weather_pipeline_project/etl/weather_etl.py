import logging
import pandas as pd
from snowflake.snowpark import Session
from snowflake.snowpark.exceptions import SnowparkSQLException
# from config.snowflake_config import SNOWFLAKE_CONN_PARAMS
import importlib.util
import sys
import os

# Load Snowflake config dynamically
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../config/snowflake_config.py'))
spec = importlib.util.spec_from_file_location("snowflake_config", config_path)
snowflake_config = importlib.util.module_from_spec(spec)
spec.loader.exec_module(snowflake_config)

SNOWFLAKE_CONN_PARAMS = snowflake_config.SNOWFLAKE_CONN_PARAMS

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_snowflake_session():
    try:
        session = Session.builder.configs(SNOWFLAKE_CONN_PARAMS).create()
        logger.info("✅ Snowflake session created")
        return session
    except Exception as e:
        logger.error(f"❌ Failed to create Snowflake session: {e}")
        raise


def load_weather_data_to_snowflake(session, csv_path):
    try:
        df = pd.read_csv(csv_path)

        df.columns = [c.strip().upper() for c in df.columns]

        df['DATE'] = pd.to_datetime(df['DATE'], errors='coerce')

        df = df.dropna(subset=['DATE'])

        df['DATE'] = df['DATE'].dt.date

        df = df.reset_index(drop=True)

        # Load to Snowflake
        session.write_pandas(df, table_name="WEATHER_DATA", auto_create_table=False)
        logger.info("✅ Data loaded successfully into Snowflake")

    except Exception as e:
        logger.error(f"❌ ETL failed: {e}")
        raise


def main():
    csv_path = os.path.join(os.path.dirname(__file__), "../data/weather_report.csv")
    session = create_snowflake_session()
    load_weather_data_to_snowflake(session, csv_path)
    session.close()


if __name__ == "__main__":
    main()
