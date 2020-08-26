import requests
import json
import argparse
from datetime import datetime, timezone

parser = argparse.ArgumentParser()
parser.add_argument("credential", help="JSON file which is storing id/pass at Fleep", type=str)
args = parser.parse_args()
with open(args.credential) as f:
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

now_dt = datetime.now(timezone.utc)
import pickle
pickle_file = "/tmp/last_alert.pt"
import os
last_run_file = os.path.isfile(pickle_file)
first_run = False
dt_gap = None 

if last_run_file:
    last_run_dt = pickle.load(open(pickle_file, "rb"))
    dt_gap = now_dt - last_run_dt
else:
    pickle.dump(now_dt, open(pickle_file, "wb"))
    first_run = True


#TODO Better logic
if  first_run or dt_gap.days > 0:

    time_stamp = format(now_dt.astimezone().isoformat())
    MESSAGE = time_stamp + ": The host is dead"
    CONV_ID = "219f033c-87a0-44ab-9602-7802b57cb701"
    
    r = requests.post(HOST + "/api/message/send/" + CONV_ID, cookies = {"token_id": TOKEN}, headers = {"Content-Type": "application/json"},
            data = json.dumps({"message": MESSAGE,"ticket": TICKET}))
    print(r)
    
    pickle.dump(now_dt, open(pickle_file, "wb"))
else:
    print("Last alert is in a day. Keep silent")


