# 🌦️ Weather Data Engineering Pipeline

## Overview
This project is an end-to-end real-time data engineering pipeline that ingests live weather data using WeatherAPI, validates and cleans the data, stores it in a MySQL database, and performs analytics.

## Tech Stack
- Python
- WeatherAPI
- Pandas
- MySQL
- Matplotlib

## Pipeline Flow
WeatherAPI → Python Ingestion → Data Cleaning → MySQL → Analytics

## Features
- Real-time API ingestion
- Data validation & sanity checks
- Deduplication logic
- MySQL relational storage
- Analytical visualizations
- Production-ready structure

## How to Run
1. Clone repository
2. Create virtual environment
3. Install dependencies
4. Add `.env` file with API key and DB credentials
5. Run pipeline scripts

## Sample SQL Query
```sql
SELECT DATE(timestamp), AVG(temperature_c)
FROM weather_data
GROUP BY DATE(timestamp);
