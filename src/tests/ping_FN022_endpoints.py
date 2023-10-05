import requests
import sys
from pprint import pprint

domain = "http://127.0.0.1:8000"

prj_cd = "LEA_IA17_097"
ssn = sys.argv[1]


root_url = "http://127.0.0.1:8000/api/fn022/"
url = f"{root_url}{prj_cd}/{ssn}/"
print("root url = ", root_url)
print("detail url = ", url)

# item list:
print("Checking our item list...")
response = requests.get(url)
print(response)
assert response.status_code == 200

# create a new FN022 item:

data = {
    "prj_cd": prj_cd,
    "ssn": ssn,
    "ssn_date0": "2017-06-10",
    "ssn_date1": "2017-06-20",
    "ssn_des": "Created with a POST",
}

print("creating new fn022 object...")
response = requests.post(root_url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 201


data = {
    "prj_cd": prj_cd,
    "ssn": ssn,
    "ssn_date0": "2017-06-05",
    "ssn_date1": "2017-06-25",
    "ssn_des": "Updated with a PUT Request",
}

print("Update whole object with PUT request ...")
response = requests.put(url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 200


print("Deleting our new  fn022 object...")
response = requests.delete(url)
print(response)
assert response.status_code == 204
