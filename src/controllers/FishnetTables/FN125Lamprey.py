from FnDbTable import FishNetDbTable

keyfields = ["PRJ_CD", "SAM", "EFF", "SPC", "GRP", "FISH", "LAMID"]
data_flds = ["XLAM", "LAMIJC_TYPE", "LAMIJC_SIZE", "COMMENT_LAM"]

FN125Lamprey = FishNetDbTable(
    table_name="FN125_Lamprey", keyfields=keyfields, data_fields=data_flds
)
