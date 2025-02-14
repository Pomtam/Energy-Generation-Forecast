import requests
import pandas as pd
from io import StringIO

NASA_POWER_BASEURL = "https://power.larc.nasa.gov/api/temporal/{period}/point?"


# Fetch Functions

def fetch_weather_data(parameters, latitude, longitude, start_date, end_date, temporal="daily", format="csv", **kwargs):
    """
    Fetch weather data from NASA POWER API.
    
    :param parameters: Comma-separated string of parameters (e.g., "T2M,WSC")
    :param latitude: Latitude of the location
    :param longitude: Longitude of the location
    :param start_date: Start date in YYYYMMDD format
    :param end_date: End date in YYYYMMDD format
    :param temporal: Temporal resolution (daily, hourly, climatology)
    :param format: Response format (csv, json, etc.)
    :param kwargs: Additional query parameters
    :return: DataFrame with weather data
    """
    params = {
        "parameters": parameters,
        "community": "AG",
        "longitude": longitude,
        "latitude": latitude,
        "start": start_date,
        "end": end_date,
        "format": format
    }
    params.update(kwargs)  # Add any extra parameters

    response = requests.get(NASA_POWER_BASEURL.format(period=temporal), params=params)
    
    if response.status_code == 200:
        if format == "csv":
            # Parse CSV, skipping header metadata
            csv_data = response.text.split("-END HEADER-")[-1].strip()
            df = pd.read_csv(StringIO(csv_data))
            return df
        elif format == "json":
            return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Example usage
# if __name__ == "__main__":
#     df = fetch_weather_data(
#         parameters="T2M,WSC",
#         latitude=0,
#         longitude=0,
#         start_date="20170101",
#         end_date="20170201",
#         wind_surface="SeaIce",
#         wind_elevation=50
#     )
#     print(df.head())