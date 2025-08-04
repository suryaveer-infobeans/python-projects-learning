CREATE TABLE IF NOT EXISTS weather_schema.weather_data (
    station_id STRING,
    date DATE,
    temperature_c FLOAT,
    humidity INT,
    wind_speed_kmph FLOAT,
    condition STRING
);
