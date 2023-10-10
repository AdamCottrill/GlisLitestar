import requests
import sys
from pprint import pprint

domain = "http://127.0.0.1:8000"

prj_cd = "LEA_IA17_097"
subspace = "146"
metres_up = 4
metres_across = sys.argv[1]


root_url = "http://127.0.0.1:8000/api/stream_dimensions/"
url = f"{root_url}{prj_cd}/{subspace}/{metres_up}/{metres_across}"
print("root url = ", root_url)
print("detail url = ", url)

# item list:
print("Checking our item list...")
response = requests.get(url)
print(response)
assert response.status_code == 200

# create a new Stream Dimension item:

data = {
    "prj_cd": prj_cd,
    "subspace": subspace,
    "metres_up": metres_up,
    "metres_across": metres_across,
    "width": 12.1,
    "depth": 5,
    "velocity": 0.9,
    "comment": "created with a POST",
}

print("creating new stream dimension object...")
response = requests.post(root_url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 201


data = {
    "prj_cd": prj_cd,
    "subspace": subspace,
    "metres_up": metres_up,
    "metres_across": metres_across,
    "width": 15.1,
    "depth": 0.5,
    "velocity": 0.1,
    "comment": "updated with a PUT",
}

print("Update whole object with PUT request ...")
response = requests.put(url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 200


print("Deleting our new  stream dimension object...")
response = requests.delete(url)
print(response)
assert response.status_code == 204
