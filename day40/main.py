import json
import requests

SHEETY_ENDPOINT = "https://api.sheety.co/bdafefbddd18fe84def04c4e480d1586/flightClub/users"

THE_TOKEN = "TheSecretT0k3nTheSecretT0k3nTheSecretT0k3nTheSecretT0k3n" # this is not correct in pro projects

f_name = input("Welcome to the flight club, give me your name:\n")

f_surname = input("Now your Lastname:\n")

f_email = input("Now your Email:\n")

user = {}

user["user"] = {
    "a": f_name, 
    "b": f_surname,
    "c": f_email
}

header = {
    "Authorization": f"Bearer {THE_TOKEN}"
}

response = requests.post(SHEETY_ENDPOINT, headers=header, json=user)

r_body = response.json()

print(r_body)