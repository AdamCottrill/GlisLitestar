import requests
import sys
from pprint import pprint

domain = "http://127.0.0.1:8000"

prj_cd = "LEA_IA17_097"
sam = "4009"
eff = "032"
spc = sys.argv[1]
grp = "00"


root_url = "http://127.0.0.1:8000/api/fn123/"
url = f"{root_url}{prj_cd}/{sam}/{eff}/{spc}/{grp}/"
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
    "catcnt": 60,
    "biocnt": 15,
    "catwt": 1.694,
    "subcnt": 3,
    "subwt": 0.33,
    "comment3": "Created with a POST request.",
}

print("creating new fn123 object...")
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
    "catcnt": 77,
    "biocnt": 19,
    "catwt": 3.241,
    "subcnt": 7,
    "subwt": 0.77,
    "comment3": "Updated with a PUT Request",
}

print("Update whole object with PUT request ...")
response = requests.put(url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 200


# print("updating an existing  fn123 object with CATCNT=12...")
# response = requests.patch(
#     url, json={"catcnt": 12, "comment3": "Updated via a PATCH request"}
# )
# print(response)
# pprint(response.json())
# assert response.status_code == 200

print("Deleting our new  fn123 object...")
response = requests.delete(url)
print(response)
assert response.status_code == 204
