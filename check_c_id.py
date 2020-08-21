import requests
import json

with open("auth.json") as f:
    auth_data = json.load(f)

#TODO error handling
r = requests.post("https://fleep.io/api/account/login",
    json=auth_data)
print(r)

TICKET = r.json()["ticket"]
TOKEN  = r.cookies["token_id"]

print(r.json())
print(TICKET)
print(TOKEN)

r = requests.post("https://fleep.io/api/conversation/list", cookies={"token_id":TOKEN}, json={"ticket": TICKET})
print(r)

my_j = r.json()
for c in range(len(my_j['conversations'])):
    print("------")
    print(my_j['conversations'][c]['topic'])
    print(my_j['conversations'][c]['conversation_id'])


