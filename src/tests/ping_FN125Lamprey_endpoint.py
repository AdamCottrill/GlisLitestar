import requests
from pprint import pprint

domain = "http://127.0.0.1:8000"

prj_cd = "LEA_IA17_097"
sam = "4009"
eff = "114"
spc = "081"
grp = "00"
fish = "54"
lamid = 4


root_url = "http://127.0.0.1:8000/api/fn125_lamprey/"
url = f"{root_url}{prj_cd}/{sam}/{eff}/{spc}/{grp}/{fish}/{lamid}/"
print("root url = ", root_url)
print("detail url = ", url)

# item list:
print("Checking our item list...")
response = requests.get(url)
print(response)
assert response.status_code == 200

# create a new lamid item:

data = {
    "prj_cd": prj_cd,
    "sam": sam,
    "eff": eff,
    "spc": spc,
    "grp": grp,
    "fish": fish,
    "lamid": lamid,
    "xlam": None,
    "lamijc_type": "0",
    "lamijc_size": 34,
    "comment_lam": "POST request.",
}

print("creating new fn125_lamprey object...")
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
    "lamid": lamid,
    "xlam": None,
    "lamijc_type": "A3",
    "lamijc_size": None,
    "comment_lam": "Test PUT Request",
}

print("Update whole object with PUT request ...")
response = requests.put(url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 200


print("updating an existing  fn125_lamprey object with agea=12...")
response = requests.patch(
    url, json={"lamijc_type": "A1", "comment_lam": "something more informative"}
)
print(response)
pprint(response.json())
assert response.status_code == 200

print("Deleting our new  fn125_lamprey object...")
response = requests.delete(url)
print(response)
assert response.status_code == 204
