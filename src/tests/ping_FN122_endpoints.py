import requests
from pprint import pprint

domain = "http://127.0.0.1:8000"

prj_cd = "LEA_IA17_097"
sam = "4009"
eff = "031"


root_url = "http://127.0.0.1:8000/api/fn122/"
url = f"{root_url}{prj_cd}/{sam}/{eff}/"
print("root url = ", root_url)
print("detail url = ", url)

# item list:
print("Checking our item list...")
response = requests.get(url)
print(response)
assert response.status_code == 200

# create a new FN122 item:

data = {
    "prj_cd": prj_cd,
    "sam": sam,
    "eff": eff,
    "effdst": 15.2,
    "grdep0": 5.6,
    "grdep1": None,
    "grtem0": 15,
    "grtem1": 9.5,
    "waterhaul": "0",
    "comment2": "A comment created by POST reuqest.",
}

print("creating new fn122 object...")
response = requests.post(root_url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 201


data = {
    "prj_cd": prj_cd,
    "sam": sam,
    "eff": eff,
    "effdst": 30.5,
    "grdep0": 5.3,
    "grdep1": 5.4,
    "grtem0": 11.9,
    "grtem1": 12.1,
    "waterhaul": "0",
    "comment2": "Updated with a PUT Request",
}

print("Update whole object with PUT request ...")
response = requests.put(url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 200


print("updating an existing  fn122 object with effdst=30.5.")
response = requests.patch(
    url, json={"effdst": 30.5, "comment2": "Updated via a PATCH request"}
)
print(response)
pprint(response.json())
assert response.status_code == 200

print("Deleting our new  fn122 object...")
response = requests.delete(url)
print(response)
assert response.status_code == 204
