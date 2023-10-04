from FnDbTable import FishNetDbTable

keyfields = ["PRJ_CD", "SAM", "EFF", "SPC", "GRP"]
data_flds = [
    "CATCNT",
    "BIOCNT",
    "CATWT",
    "SUBCNT",
    "SUBWT",
    "COMMENT3",
]


FN123 = FishNetDbTable(table_name="FN123", keyfields=keyfields, data_fields=data_flds)
