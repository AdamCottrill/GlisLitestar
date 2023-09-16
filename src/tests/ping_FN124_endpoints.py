import requests
from pprint import pprint

domain = "http://127.0.0.1:8000"

prj_cd = "LEA_IA17_097"
sam = "4009"
eff = "114"
spc = "081"
grp = "00"
siz = "150"


root_url = "http://127.0.0.1:8000/api/fn124/"
url = f"{root_url}{prj_cd}/{sam}/{eff}/{spc}/{grp}/{siz}/"
print("root url = ", root_url)
print("detail url = ", url)

# item list:
print("Checking our item list...")
response = requests.get(url)
print(response)
assert response.status_code == 200

# create a new siz_tag_id item:

data = {
    "prj_cd": prj_cd,
    "sam": sam,
    "eff": eff,
    "spc": spc,
    "grp": grp,
    "siz": siz,
    "sizcnt": 3,
    "comment4": "Test ping comment.",
}

print("creating new fn124 object...")
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
    "siz": siz,
    "sizcnt": 14,
    "comment4": "Replaced with a PUT request.",
}

print("Update whole object with PUT request ...")
response = requests.put(url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 200


print("updating an existing  fn124 object with agea=12...")
response = requests.patch(
    url, json={"sizcnt": 12, "comment4": "Updated via a PATCH request"}
)
print(response)
pprint(response.json())
assert response.status_code == 200

print("Deleting our new  fn124 object...")
response = requests.delete(url)
print(response)
assert response.status_code == 204
