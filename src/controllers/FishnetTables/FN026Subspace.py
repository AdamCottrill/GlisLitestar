from FnDbTable import FishNetDbTable

keyfields = ["PRJ_CD", "SPACE", "SUBSPACE"]
data_flds = [
    "SUBSPACE_DES",
    "DD_LAT",
    "DD_LON",
    "SIDEP_LT",
    "SIDEP_GE",
    "GRDEP_LT",
    "GRDEP_GE",
    "SUBSPACE_WT",
]

FN026Subspace = FishNetDbTable(table_name="FN026_Subspace", keyfields=keyfields, data_fields=data_flds)
