import requests
from datetime import datetime
import sys
from pprint import pprint

domain = "http://127.0.0.1:8000"

prj_cd = sys.argv[1]

year = datetime.strptime(prj_cd[6:8], "%y").year


root_url = f"{domain}/api/fn011/"
url = f"{root_url}{prj_cd}/"
print("root url = ", root_url)
print("detail url = ", url)

# item list:
print("Checking our item list...")
response = requests.get(root_url)
print(response)
assert response.status_code == 200


# create a new FN011 item:
data = {
    "prj_cd": prj_cd,
    "lake": "HU",
    "protocol": "BSM",
    "prj_ldr": "Homer Simpson",
    "year": year,
    "prj_nm": "Fake Project",
    "prj_date0": f"{year}-08-03",
    "prj_date1": f"{year}-08-20",
    "comment0": "Created with a POST",
}

print("creating new fn011 object...")
response = requests.post(root_url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 201

data = {
    "prj_cd": prj_cd,
    "lake": "ER",
    "protocol": "FWIN",
    "prj_ldr": "Marge Simpson",
    "year": year,
    "prj_nm": "Updated Fake Project",
    "prj_date0": f"{year}-08-05",
    "prj_date1": f"{year}-08-25",
    "comment0": "Updated with a PUT",


}

print("Replace the whole object with PUT request ...")
response = requests.put(url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 200


print("Deleting our new  fn011 object...")
response = requests.delete(url)
print(response)
assert response.status_code == 204
