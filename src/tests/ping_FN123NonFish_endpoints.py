import requests
from pprint import pprint

domain = "http://127.0.0.1:8000"

prj_cd = "LEA_IA17_097"
sam = "4009"
eff = "032"
taxon = "12354"


root_url = "http://127.0.0.1:8000/api/fn123_nonfish/"
url = f"{root_url}{prj_cd}/{sam}/{eff}/{taxon}/"
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
    "taxon": taxon,
    "catcnt": 11,
    "mortcnt": 1,
    "comment3": "Created with a POST request.",
}

print("creating new fn123_nonfish object...")
response = requests.post(root_url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 201


data = {
    "prj_cd": prj_cd,
    "sam": sam,
    "eff": eff,
    "taxon": taxon,
    "catcnt": 31,
    "mortcnt": 3,
    "comment3": "Updated with a PUT Request",
}

print("Update whole object with PUT request ...")
response = requests.put(url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 200


print("updating an existing  fn123_nonfish object with CATCNT=12...")
response = requests.patch(
    url, json={"catcnt": 42, "comment3": "Updated via a PATCH request"}
)
print(response)
pprint(response.json())
assert response.status_code == 200

print("Deleting our new  fn123_nonfish object...")
response = requests.delete(url)
print(response)
assert response.status_code == 204
