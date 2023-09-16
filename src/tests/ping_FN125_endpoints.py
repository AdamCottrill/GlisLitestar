import requests
from pprint import pprint

domain = "http://127.0.0.1:8000"

prj_cd = "LEA_IA17_097"
sam = "4009"
eff = "114"
spc = "081"
grp = "00"
fish = "5555"


root_url = "http://127.0.0.1:8000/api/fn125/"
url = f"{root_url}{prj_cd}/{sam}/{eff}/{spc}/{grp}/{fish}/"
print("root url = ", root_url)
print("detail url = ", url)

# item list:
print("Checking our item list...")
response = requests.get(url)
print(response)
assert response.status_code == 200

# create a new fish_tag_id item:

data = {
    "prj_cd": prj_cd,
    "sam": sam,
    "eff": eff,
    "spc": spc,
    "grp": grp,
    "fish": fish,
    "flen": 140,
    "tlen": 146,
    "girth": 12,
    "rwt": 36,
    "eviswt": 33,
    "sex": "2",
    "mat": "1",
    "gon": "10",
    "gonwt": 4.9,
    "clipc": "1",
    "clipa": None,
    "nodc": None,
    "noda": None,
    "tissue": "0",
    "agest": "1",
    "fate": "K",
    "fdsam": "0",
    "stom_contents_wt": 3,
    "comment5": "Test ping comment.",
}

print("creating new fn125 object...")
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
    "flen": 141,
    "tlen": 150,
    "girth": 14,
    "rwt": 42,
    "eviswt": 40,
    "sex": "1",
    "mat": "2",
    "gon": "40",
    "gonwt": 7.8,
    "clipc": "F",
    "clipa": "F",
    "nodc": "F212",
    "noda": "F212",
    "tissue": "8",
    "agest": "1",
    "fate": "K",
    "fdsam": "0",
    "stom_contents_wt": 2,
    "comment5": "Replaced with a PUT request.",
}

print("Update whole object with PUT request ...")
response = requests.put(url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 200


print("updating an existing  fn125_tag object with agea=12...")
response = requests.patch(
    url, json={"tissue": "14A", "comment5": "Updated via a PATCH request"}
)
print(response)
pprint(response.json())
assert response.status_code == 200

print("Deleting our new  fn125 object...")
response = requests.delete(url)
print(response)
assert response.status_code == 204
