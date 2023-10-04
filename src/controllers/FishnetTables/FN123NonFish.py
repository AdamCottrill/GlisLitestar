from FnDbTable import FishNetDbTable

keyfields = ["PRJ_CD", "SAM", "EFF", "TAXON"]
data_flds = ["CATCNT", "MORTCNT", "COMMENT3"]


FN123NonFish = FishNetDbTable(
    table_name="FN123_NonFish", keyfields=keyfields, data_fields=data_flds
)
