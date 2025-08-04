import os
from dotenv import load_dotenv
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
from snowflake.snowpark import Session

# Load environment variables
load_dotenv()

# Snowflake connection parameters
connection_parameters = {
    "account": os.getenv("SNOWFLAKE_ACCOUNT"),
    "user": os.getenv("SNOWFLAKE_USER"),
    "password": os.getenv("SNOWFLAKE_PASSWORD"),
    "role": os.getenv("SNOWFLAKE_ROLE"),
    "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
    "database": os.getenv("SNOWFLAKE_DATABASE"),
    "schema": os.getenv("SNOWFLAKE_SCHEMA")
}

# Create Snowflake session
session = Session.builder.configs(connection_parameters).create()

# Load data from Snowflake
df = session.table("WEATHER_DATA").to_pandas()

# Close session
session.close()

# Create plot
fig = px.line(df, x='DATE', y='TEMPERATURE_C', color='STATION_ID')

# Dash app
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Weather Report Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
