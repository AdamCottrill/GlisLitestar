import requests
import sys
from pprint import pprint

domain = "http://127.0.0.1:8000"

prj_cd = "LEA_IA17_097"
sam = sys.argv[1]


root_url = "http://127.0.0.1:8000/api/fn121/"
url = f"{root_url}{prj_cd}/{sam}"
print("root url = ", root_url)
print("detail url = ", url)

# item list:
print("Checking our item list...")
response = requests.get(url)
print(response)
assert response.status_code == 200

# create a new FN121 item:

data = {
    "prj_cd": prj_cd,
    "sam": sam,
    "process_type": "2",
    "ssn": "02",
    "subspace": "887",
    "mode": "01",
    "effdt0": "2017-06-05",
    "efftm0": "12:10:00",
    "effdt1": "2017-06-06",
    "efftm1": "11:38:00",
    "effdur": 23.47,
    "effst": "1",
    "sitp": "1",
    "dd_lat0": 42.63267,
    "dd_lon0": -80.29183,
    "dd_lat1": 42.63167,
    "dd_lon1": -80.287,
    "grid5": "9999",
    "sitem0": 14.4,
    "sitem1": 14.4,
    "sidep0": 5.3,
    "sidep1": 5.3,
    "grdepmax": None,
    "grdepmid": 7.8,
    "grdepmin": 5.1,
    "secchi0": 5.3,
    "secchi1": 5.3,
    "slime": "1",
    "crew": "TEST",
    "comment1": "comment created by POST request.",
    "vessel": "EREXPLORER",
    "vessel_direction": "1",
    "vessel_speed": 1,
    "warp": 25,
    "bottom": "SI",
    "cover": "MA",
    "lead_angle": 45,
    "leaduse": 1,
    "distoff": 1,
    "vegetation": 1,
    "o2bot0": 7.4,
    "o2bot1": 7.2,
    "o2surf0": 12,
    "o2surf1": 10.6,
    "o2gr0": 7.6,
    "o2gr1": None,
    "airtem0": 10.6,
    "airtem1": 14.1,
    "wind0": "360-1",
    "wind1": "360-02",
    "precip0": "00",
    "precip1": "40",
    "cloud_pc0": 96,
    "cloud_pc1": 80,
    "waveht0": 1.3,
    "waveht1": 1.6,
    "xweather": "22",
}

print("creating new fn121 object...")
response = requests.post(root_url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 201


data = {
    "prj_cd": prj_cd,
    "sam": sam,
    "process_type": "2",
    "ssn": "02",
    "subspace": "939",
    "mode": "01",
    "effdt0": "2017-06-05",
    "efftm0": "10:48",
    "effdt1": "2017-06-06",
    "efftm1": "09:45",
    "effdur": 22.95,
    "effst": "1",
    "sitp": "2",
    "dd_lat0": 42.63083,
    "dd_lon0": -80.21383,
    "dd_lat1": 42.63333,
    "dd_lon1": -80.2175,
    "grid5": "1256",
    "sitem0": None,
    "sitem1": 14.3,
    "sidep0": 9.1,
    "sidep1": None,
    "grdepmax": 7.2,
    "grdepmid": 3.2,
    "grdepmin": 1.2,
    "secchi0": 6,
    "secchi1": None,
    "slime": None,
    "crew": None,
    "comment1": "comment created by PUT request.",
    "vessel": "EREXPLORER",
    "vessel_direction": None,
    "vessel_speed": None,
    "warp": None,
    "bottom": None,
    "cover": None,
    "lead_angle": None,
    "leaduse": None,
    "distoff": None,
    "vegetation": None,
    "o2bot0": None,
    "o2bot1": None,
    "o2surf0": None,
    "o2surf1": None,
    "o2gr0": 3.4,
    "o2gr1": 5.6,
    "airtem0": None,
    "airtem1": None,
    "wind0": None,
    "wind1": None,
    "precip0": None,
    "precip1": None,
    "cloud_pc0": None,
    "cloud_pc1": None,
    "waveht0": None,
    "waveht1": None,
    "xweather": None,
}

print("Update whole object with PUT request ...")
response = requests.put(url, json=data)
print(response)
pprint(response.json())
assert response.status_code == 200


# print("updating an existing  fn121 object")
# updates = {
#     "effdur": 18.92,
#     "effst": "1",
#     "sitp": "1",
#     "dd_lat0": 42.76333,
#     "dd_lon0": -80.2265,
#     "dd_lat1": 42.766,
#     "dd_lon1": -80.223,
# }
# response = requests.patch(url, json=updates)
# print(response)
# pprint(response.json())
# assert response.status_code == 200

print("Deleting our new  fn121 object...")
response = requests.delete(url)
print(response)
assert response.status_code == 204
