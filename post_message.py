import requests
import json

with open("auth.json") as f:
    auth_data = json.load(f)

HOST = "https://fleep.io"

#TODO error handling
r = requests.post(HOST + "/api/account/login",
    json=auth_data)
print(r)

TICKET = r.json()["ticket"]
TOKEN  = r.cookies["token_id"]

print(r.json())
print(TICKET)
print(TOKEN)

CONV_ID = "219f033c-87a0-44ab-9602-7802b57cb701"
MESSAGE = "The host is dead"

r = requests.post(HOST + "/api/message/send/" + CONV_ID, cookies = {"token_id": TOKEN}, headers = {"Content-Type": "application/json"},
        data = json.dumps({"message": MESSAGE,"ticket": TICKET}))
print(r)
