import requests
import sys
from pprint import pprint
from datetime import time

domain = "http://127.0.0.1:8000"

prj_cd = "LEA_IA17_097"
mode = sys.argv[1]


root_url = "http://127.0.0.1:8000/api/fn028/"
url = f"{root_url}{prj_cd}/{mode}/"
print("root url = ", root_url)
print("detail url = ", url)

# item list:
print("Checking our item list...")
response = requests.get(url)
print(response)
assert response.status_code == 200

# create a new FN028 item:

data = {
    "prj_cd": prj_cd,
    "mode": mode,
    "mode_des": "created by POST",
    "gr": "GL01",
    "orient": "1",
    "gruse": 2,
    "effdur_ge": 0.1,
    "effdur_lt": 1.0,
    "efftm0_ge": "08:00",
    "efftm0_lt": "16:00",
}

print("creating new fn028 object...")
response = requests.post(root_url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 201


data = {
    "prj_cd": prj_cd,
    "mode": mode,
    "mode_des": "Updated with a PUT",
    "gr": "GL03",
    "orient": "3",
    "gruse": 3,
    "effdur_ge": 0.3,
    "effdur_lt": 3.0,
    "efftm0_ge": "07:30",
    "efftm0_lt": "15:30",
}

print("Update whole object with PUT request ...")
response = requests.put(url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 200


print("Deleting our new  fn028 object...")
response = requests.delete(url)
print(response)
assert response.status_code == 204
