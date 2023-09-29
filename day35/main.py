
import requests
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


OPEN_WEATHER_MAP_API_KEY = "8e080ba1df23cda5a0e218cf79284c3b"
OPEN_WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

CITY= "Girona"

params = {
    "lat": 41.981651,
    "lon": 2.823610,
    "appid": OPEN_WEATHER_MAP_API_KEY,
}

# declaring twilio info to send SMS
account_sid = os.environ['AC843df5a9fe1d0f7ddb68272618d18432']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


# getting weather info
response = requests.get(OPEN_WEATHER_ENDPOINT, params=params)

if response.ok:
    json_body = response.json()
    weather = json_body["weather"][0]
    
    message = client.messages \
                    .create(
                        body=f"Hi Facundo! Today the weather will be: {weather}",
                        from_='+15017122661',
                        to='+15558675310'
                    )
    print(f"tyhe day will be: {weather['description']}")
else:
    print(f"Error: {response.status_code} - {response.reason}")

