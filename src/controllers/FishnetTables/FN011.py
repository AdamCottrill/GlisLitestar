from FnDbTable import FishNetDbTable

keyfields = ["PRJ_CD"]
data_flds = [
    "YEAR",
    "PRJ_NM",
    "PRJ_LDR",
    "PRJ_DATE0",
    "PRJ_DATE1",
    "COMMENT0",
    "PROTOCOL",
    "LAKE",
]

FN011 = FishNetDbTable(table_name="FN011", keyfields=keyfields, data_fields=data_flds)
