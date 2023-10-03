from FnDbTable import FishNetDbTable

keyfields = ["PRJ_CD", "SAM", "EFF", "SPC", "GRP", "FISH"]
data_flds = [
    "FLEN",
    "TLEN",
    "GIRTH",
    "RWT",
    "EVISWT",
    "SEX",
    "MAT",
    "GON",
    "GONWT",
    "CLIPC",
    "CLIPA",
    "NODC",
    "NODA",
    "TISSUE",
    "AGEST",
    "FATE",
    "FDSAM",
    "STOM_CONTENTS_WT",
    "COMMENT5",
]

FN125 = FishNetDbTable(table_name="FN125", keyfields=keyfields, data_fields=data_flds)
