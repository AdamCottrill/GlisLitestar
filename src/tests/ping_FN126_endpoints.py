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
food = int(sys.argv[1])


root_url = "http://127.0.0.1:8000/api/fn126/"
url = f"{root_url}{prj_cd}/{sam}/{eff}/{spc}/{grp}/{fish}/{food}/"
print("root url = ", root_url)
print("detail url = ", url)


## GET LIST

# item list:
print("Checking our item list...")
response = requests.get(url)
print(response)
assert response.status_code == 200

## POST Request

# create a new food item:
data = {
    "prj_cd": prj_cd,
    "sam": sam,
    "eff": eff,
    "spc": spc,
    "grp": grp,
    "fish": fish,
    "food": food,
    "taxon": "7123",
    "fdcnt": 4,
    "fdmes": "L",
    "fdval": 36,
    "lifestage": "50",
    "comment6": "Another test comment",
}

print("creating new fn126 object...")
response = requests.post(root_url, json=data)
assert response.status_code == 201
print(response)
pprint(response.json())


## PUT Request

data = {
    "prj_cd": prj_cd,
    "sam": sam,
    "eff": eff,
    "spc": spc,
    "grp": grp,
    "fish": fish,
    "food": food,
    "taxon": "7121",
    "fdcnt": 1,
    "fdmes": "L",
    "fdval": 36,
    "lifestage": "50",
    "comment6": "Replaced with a PUT request.",
}

print("Update whole object with PUT request ...")
response = requests.put(url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 200

# GET REQUEST

response = requests.get(url)
print(response)
pprint(response.json())
assert response.status_code == 200


# DELETE REQUEST

print("Deleting our new  fn126 object...")
response = requests.delete(url)
print(response)
assert response.status_code == 204
