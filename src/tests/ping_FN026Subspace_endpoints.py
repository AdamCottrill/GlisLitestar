import requests
import sys
from pprint import pprint

domain = "http://127.0.0.1:8000"

prj_cd = "LEA_IA17_097"
space = '04'
subspace = sys.argv[1]


root_url = f"{domain}/api/fn026_subspace/"
url = f"{root_url}{prj_cd}/{space}/{subspace}/"
print("root url = ", root_url)
print("detail url = ", url)

# item list:
print("Checking our item list...")
response = requests.get(root_url)
print(response)
assert response.status_code == 200


# create a new FN026SUBSPACE item:
data = {
    "prj_cd": prj_cd,
    "space": space,
    "subspace": subspace,
    "subspace_des": "created by POST",
    "dd_lat": 45.5,
    "dd_lon": -81.5,
    "sidep_lt": 50,
    "sidep_ge": 10,
    "grdep_lt": 50,
    "grdep_ge": 5,
    "subspace_wt": 0.5
}

print("creating new fn026subspace object...")
response = requests.post(root_url, json=data)
print(response)

pprint(response.json())
assert response.status_code == 201

data = {
    "prj_cd": prj_cd,
    "space": space,
    "subspace": subspace,
    "subspace_des": "updated with PUT",
    "dd_lat": 45.25,
    "dd_lon": -81.25,
}

print("Update whole object with PUT request ...")
response = requests.put(url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 200


print("Deleting our new  fn026subspace object...")
response = requests.delete(url)
print(response)
assert response.status_code == 204
