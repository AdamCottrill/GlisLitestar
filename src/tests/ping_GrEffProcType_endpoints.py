import requests
import sys
from pprint import pprint

domain = "http://127.0.0.1:8000"

gear = sys.argv[1]
eff = "091"
process_type = "1"

# the updated values
eff2 = "032"
process_type2 = "2"


root_url = "http://127.0.0.1:8000/api/gear_effort_proctype"

url = f"{root_url}/{gear}/{eff}/{process_type}"

print("root url = ", root_url)
print("detail url = ", url)

# item list:
print("Checking our item list...")
response = requests.get(url)
print(response)
assert response.status_code == 200

# create a new GEAR_EFF_PROCESS_TYPE item:


data = {"gr": gear, "process_type": process_type, "eff": eff, "effdst": 15.2}


print("creating new gear_eff_process_type object...")
response = requests.post(root_url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 201


data = {"gr": gear, "process_type": process_type2, "eff": eff2, "effdst": 45.2}

print("Update whole object with PUT request ...")
response = requests.put(url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 200


print("Deleting our new  gear_eff_process_type object...")
url = f"{root_url}/{gear}/{eff2}/{process_type2}"
response = requests.delete(url)
print(response)
assert response.status_code == 204
