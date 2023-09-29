import threading
import requests
from datetime import datetime
import smtplib
import math

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"
SMTP_ADDRESS = ".gmail.com"

MY_GEO_POS = {
    "lat": 41.981651,
    "lng": 2.823610
}

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_GEO_POS["lat"],
    "lng": MY_GEO_POS["lng"],
    "formatted": 0,
}

def check_iss_over_head():
    global iss_latitude, iss_longitude
    if MY_GEO_POS["lat"] -5 <= iss_latitude <= MY_GEO_POS["lat"] +5 and MY_GEO_POS["lng"] -5 <= iss_longitude <= MY_GEO_POS["lng"] +5:
        with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Watch out!! ISS is over you!!!!"
            )

def run_iss_check():
    global iss_latitude, iss_longitude
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    current_time = datetime.now()

    if current_time >= sunset or current_time <= sunrise:
        check_iss_over_head()

threading.Timer(60.0, run_iss_check).start()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



