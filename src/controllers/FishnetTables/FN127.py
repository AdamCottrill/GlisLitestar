from FnDbTable import FishNetDbTable

keyfields = ["PRJ_CD", "SAM", "EFF", "SPC", "GRP", "FISH", "AGEID"]
data_flds = [
    "PREFERRED",
    "AGEA",
    "AGEMT",
    "EDGE",
    "CONF",
    "NCA",
    "AGESTRM",
    "AGELAKE",
    "SPAWNCHKCNT",
    "AGE_FAIL",
    "COMMENT7",
]

FN127 = FishNetDbTable(table_name="FN127", keyfields=keyfields, data_fields=data_flds)
