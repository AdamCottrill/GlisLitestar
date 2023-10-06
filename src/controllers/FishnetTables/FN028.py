from FnDbTable import FishNetDbTable

keyfields = ["PRJ_CD", "MODE"]
data_flds = [
    "MODE_DES",
    "GR",
    "GRUSE",
    "ORIENT",
    "EFFDUR_GE",
    "EFFDUR_LT",
    "EFFTM0_GE",
    "EFFTM0_LT",
]

FN028 = FishNetDbTable(table_name="FN028", keyfields=keyfields, data_fields=data_flds)
