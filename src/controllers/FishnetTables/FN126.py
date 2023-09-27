from FnDbTable import FishNetDbTable

keyfields = ["PRJ_CD", "SAM", "EFF", "SPC", "GRP", "FISH", "FOOD"]
data_flds = ["TAXON", "FDCNT", "FDMES", "FDVAL", "LIFESTAGE", "COMMENT6"]

FN126 = FishNetDbTable(table_name="FN126", keyfields=keyfields, data_fields=data_flds)
