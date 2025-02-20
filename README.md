# Queensland Renewable Energy Forecasting Project

## Project Goal
This project aims to forecast solar and wind energy generation in Queensland using weather forecast data. Results from various machine learning and time series models are explored.

## Power BI Dashboard
An interactive dashboard visualising energy generation forecasts can be accessed here:
[Renewable Energy Dashboard](https://app.powerbi.com/view?r=eyJrIjoiNDEyNGVkYjgtM2UzZC00NzdjLWFhYjgtYmY4MmEyN2ZjZjI4IiwidCI6IjRkZjFmMjIxLTQwNzMtNDM4Ni1hYjMxLWRlYTMzMWFhMGY0NCJ9)

## Data Pipeline
The project utilises an automated data pipeline to gather real-time and historical data from multiple sources:

1. **Weather Forecast Data**: Obtained from Open-Meteo, including solar irradiance, wind speed, and other meteorological variables.
2. **Historic Energy Generation**: Retrieved from OpenElectricity, providing past solar and wind energy production data.
3. **Historic Weather Data**: Collected from NASA POWER, offering long-term weather trends for model training.

## Predictive Models
Three predictive models were developed to forecast energy generation:

- **Linear Regression (LR)**: A baseline statistical model capturing relationships between weather features and energy output.
- **Gradient Boosting (XGBoost)**: A machine learning model that utilises decision trees to capture more complex, non-linear relationships.
- **SARIMA (Seasonal AutoRegressive Integrated Moving Average)**: A time-series model capturing seasonality and temporal trends in energy production.

## Dashboard Overview
The Power BI dashboard provides real-time and historical insights into Queensland's renewable energy generation:

- **Energy Generation Forecast**: Comparison of model predictions against actual recorded energy generation.
- **Monthly Trends**: Historical trends in renewable energy production over time.
- **Current Generation**: Live updates on solar and wind power output.
- **Fuel Mix**: Breakdown of energy generation by source (coal, gas, solar, wind).
- **Renewable Share**: Proportion of renewable vs. non-renewable energy in the current grid mix.

## Future Improvements
- Inclusion of rooftop solar generation. This is a large contributor to renewable energy generation in Queensland.
- Integration of additional weather variables for enhanced model accuracy.
- Development of hourly forecasts.
- Expansion of the dashboard to include regional breakdowns and more granular insights.

