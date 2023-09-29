import datetime as dt
import json
import time
import requests

MY_GEO_POS = {
    "lat": 41.981651,
    "lng": 2.823610
}

parameters = MY_GEO_POS
parameters["formatted"] = 0

#response = requests.get(url="http://api.open-notify.org/iss-now.json")
response = requests.get(url="https://api.sunrise-sunset.org/json")

response.raise_for_status()

if response.ok :
    print(json.dumps(response.json(), indent=1))
    print(f"the current time is: {dt.datetime.now()}")
else:
    raise Exception(f"Request ended to an error: {response.status_code} - {response.reason}")


