from FnDbTable import FishNetDbTable

keyfields = ["PRJ_CD", "SAM", "EFF"]
data_flds = [
    "EFFDST",
    "GRDEP0",
    "GRDEP1",
    "GRTEM0",
    "GRTEM1",
    "WATERHAUL",
    "COMMENT2",
]


FN122 = FishNetDbTable(table_name="FN122", keyfields=keyfields, data_fields=data_flds)
