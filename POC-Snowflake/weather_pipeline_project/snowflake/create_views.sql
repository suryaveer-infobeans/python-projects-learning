CREATE OR REPLACE VIEW weather_schema.avg_temp_by_date AS
SELECT date, AVG(temperature_c) AS avg_temp
FROM weather_schema.weather_data
GROUP BY date;
