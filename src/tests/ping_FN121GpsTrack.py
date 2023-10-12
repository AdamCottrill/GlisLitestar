import sys
from datetime import datetime
from pprint import pprint

import requests

domain = "http://127.0.0.1:8000"

prj_cd = "LEA_IA17_097"
sam = "4001"
trackid = sys.argv[1]

root_url = "http://127.0.0.1:8000/api/fn121_gps_tracks"

url = f"{root_url}/{prj_cd}/{sam}/{trackid}"
print("root url = ", root_url)
print("detail url = ", url)

# item list:
print("Checking our item list...")
response = requests.get(root_url)
print(response)
assert response.status_code == 200

# create a new Fn121 GPS track item:
data = {
    "prj_cd": prj_cd,
    "sam": sam,
    "trackid": trackid,
    "dd_lat": 45.5,
    "dd_lon": -81.5,
    "sidep": 12.0,
    "timestamp": datetime.now().isoformat(),
    "comment": "comment created with a post",
}


print("creating new gear_eff_process_type object...")
response = requests.post(root_url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 201

print("fetch the details of the object we just created:")
response = requests.get(url)
print(response)
assert response.status_code == 200


data = {
    "prj_cd": prj_cd,
    "sam": sam,
    "trackid": trackid,
    "dd_lat": 44.9,
    "dd_lon": -80.2,
    "sidep": 15.5,
    "timestamp": datetime.now().isoformat(),
    "comment": "comment created with a put",
}

print("Update whole object with PUT request ...")
response = requests.put(url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 200

print("Deleting our new  gear_eff_process_type object...")
response = requests.delete(url)
print(response)
assert response.status_code == 204
