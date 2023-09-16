import requests
from pprint import pprint

domain = "http://127.0.0.1:8000"

prj_cd = "LEA_IA17_097"
sam = "4009"
eff = "114"
spc = "081"
grp = "00"
fish = "54"
fish_tag_id = 17


root_url = "http://127.0.0.1:8000/api/fn125_tag/"
url = f"{root_url}{prj_cd}/{sam}/{eff}/{spc}/{grp}/{fish}/{fish_tag_id}/"
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
    "fish_tag_id": fish_tag_id,
    "tagid": "60-02-29",
    "tagdoc": "67125",
    "tagstat": "C",
    "cwtseq": 333333,
    "comment_tag": "TEST",
}

print("creating new fn125_tag object...")
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
    "fish_tag_id": fish_tag_id,
    "tagid": "63-01-57",
    "tagdoc": "63144",
    "tagstat": "A",
    "cwtseq": 12345,
    "comment_tag": "Test PUT Request",
}

print("Update whole object with PUT request ...")
response = requests.put(url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 200


print("updating an existing  fn125_tag object with agea=12...")
response = requests.patch(
    url, json={"tagid": "65982", "comment_tag": "something more informative"}
)
print(response)
pprint(response.json())
assert response.status_code == 200

print("Deleting our new  fn125_tag object...")
response = requests.delete(url)
print(response)
assert response.status_code == 204
