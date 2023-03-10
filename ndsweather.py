# ndsweather.py

import os
import json
import weatherkit

# Load the credentials from wherever you store them securely
# team_id = os.environ.get('APPLE_TEAM_ID')
# key_id = os.environ.get('APPLE_KEY_ID')
# service_id = os.environ.get('APPLE_SERVICE_ID')
# private_key = os.environ.get('APPLE_PRIVATE_KEY')

keyfile = open("AuthKey_84FS6668BX.p8", "r")
keystring = keyfile.read()

team_id = "7QAM3LGSSC"
key_id = "84FS6668BX"
service_id = "com.neherdata.weather"
private_key = keystring

# Instantiate the WeatherKit object
wk_client = weatherkit.WeatherKit(team_id, service_id, private_key, key_id)

# Include any/all of the datasets we want to pull in the list
datasets = [
    "forecastHourly",
    "forecastDaily",
    "currentWeather",
    "forecastNextHour",
]

# Fetch the API
forecasts = wk_client.fetch(datasets, 40.308392, -74.069771, "US", "US/Eastern")
secretariat = wk_client.fetch(datasets, 40.308392, -74.069771, "US", "US/Eastern")

# There is a convenience method for converting the forecast response object to JSON
forecasts_json = forecasts.as_json()

print(forecasts_json)
