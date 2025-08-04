import os
from dotenv import load_dotenv
from snowflake.snowpark import Session

# Load env vars
load_dotenv()

# Snowpark config
connection_parameters = {
    "account": os.getenv("SNOWFLAKE_ACCOUNT"),
    "user": os.getenv("SNOWFLAKE_USER"),
    "password": os.getenv("SNOWFLAKE_PASSWORD"),
    "role": os.getenv("SNOWFLAKE_ROLE"),
    "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
    "database": os.getenv("SNOWFLAKE_DATABASE"),
    "schema": os.getenv("SNOWFLAKE_SCHEMA"),
}

# Create session
try:
    session = Session.builder.configs(connection_parameters).create()
    print("✅ Snowpark session created")

    # Sample query
    df = session.sql("SELECT CURRENT_TIMESTAMP()").collect()
    print(df)

except Exception as e:
    print(f"❌ Snowpark connection failed: {e}")
