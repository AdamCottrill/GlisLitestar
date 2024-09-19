from FnDbTable import FishNetDbTable

keyfields = ["PRJ_CD", "SPACE"]
data_flds = [
    "SPACE_DES",
    "DD_LAT",
    "DD_LON",
    "SIDEP_LT",
    "SIDEP_GE",
    "GRDEP_LT",
    "GRDEP_GE",
    "SPACE_WT",
]

FN026 = FishNetDbTable(table_name="FN026", keyfields=keyfields, data_fields=data_flds)
