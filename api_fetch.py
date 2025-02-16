import requests
import pandas as pd
from io import StringIO
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
SOLCAST_ID = os.getenv('SOLCAST_API_KEY')

NASA_POWER_BASEURL = "https://power.larc.nasa.gov/api/temporal/{period}/point?"
SOLCAST_BASEURL = "https://api.solcast.com.au/weather_sites/data/historic/radiation_and_weather?"


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





def fetch_solcast_data(latitude, longitude, start_date, end_date, duration="P1D", output_parameters="air_temp,dni,ghi", azimuth=None, tilt=None, array_type="fixed", format="json", token=SOLCAST_ID):
    """
    Fetch irradiance and weather forecast data from Solcast API.

    :param latitude: Latitude of the location
    :param longitude: Longitude of the location
    :param start_date: Start datetime for the historical data (YYYY-MM-DD)
    :param end_date: End datetime for the historical data
    :param duration: Duration of the historical data (e.g., "P1D")
    :param output_parameters: Parameters like "air_temp,dni,ghi"
    :param azimuth: Azimuth angle for PV system (optional)
    :param tilt: Tilt angle for PV system (optional)
    :param array_type: Type of PV array (fixed or horizontal_single_axis)
    :param format: Response format (json or csv)
    :param token: Bearer token for Solcast authorization
    :return: DataFrame or JSON with the requested data
    """
    headers = {
        "Authorization": f"Bearer {token}"
    }

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start": start_date,
        "end": end_date,
        # "duration": duration,
        "output_parameters": output_parameters,
        "format": format,
        "time_zone": "utc"  # Default to UTC
    }

    if azimuth is not None:
        params["azimuth"] = azimuth
    if tilt is not None:
        params["tilt"] = tilt
    if array_type is not None:
        params["array_type"] = array_type

    response = requests.get("https://api.solcast.com.au/data/historic/radiation_and_weather", headers=headers, params=params)

    if response.status_code == 200:
        if format == "json":
            return response.json()  # Returns the JSON response
        elif format == "csv":
            df = pd.read_csv(StringIO(response.text))  # Returns the data as a DataFrame
            return df
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