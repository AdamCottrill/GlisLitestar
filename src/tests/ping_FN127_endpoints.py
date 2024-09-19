import requests
import sys
from pprint import pprint

domain = "http://127.0.0.1:8000"
prj_cd = "LEA_IA17_097"
sam = "4052"
eff = "032"
spc = "331"
grp = "00"
fish = "39750"
ageid = int(sys.argv[1])
#ageid = 34


root_url = "http://127.0.0.1:8000/api/fn127/"
url = f"{root_url}{prj_cd}/{sam}/{eff}/{spc}/{grp}/{fish}/{ageid}/"
print("root url = ", root_url)
print("detail url = ", url)

# item list:
print("Checking our item list...")
response = requests.get(url)
print(response)
assert response.status_code == 200

# create a new ageid item:

data = {
    "prj_cd": prj_cd,
    "sam": sam,
    "eff": eff,
    "spc": spc,
    "grp": grp,
    "fish": fish,
    "ageid": ageid,
    "preferred": 0,
    "agea": 2,
    "agemt": "111PD",
    "edge": "+",
    "conf": 9,
    "nca": 2,
    "agestrm": 1,
    "agelake": 0,
    "spawnchkcnt": 0,
    "age_fail": "",
    "comment7": "Test comment.",
}

print("creating new fn127 object...")
print("POSTing to", root_url)
response = requests.post(root_url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 201


data = {
    "prj_cd": prj_cd,
    "sam": sam,
    "eff": eff,
    "spc": spc,
    "grp": grp,
    "fish": fish,
    "ageid": ageid,
    "preferred": 1,
    "agea": 2,
    "agemt": "111PD",
    "edge": None,
    "conf": None,
    "nca": None,
    "agestrm": None,
    "agelake": None,
    "spawnchkcnt": None,
    "age_fail": None,
    "comment7": "Replaced with a PUT request.",
}

print("Update whole object with PUT request ...")
response = requests.put(url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 200


# print("updating an existing  fn127 object with agea=12...")
# response = requests.patch(
#     url, json={"agea": 22, "comment7": "something more informative"}
# )
# print(response)
# pprint(response.json())
# assert response.status_code == 200

print("Deleting our new  fn127 object...")
response = requests.delete(url)
print(response)
assert response.status_code == 204
