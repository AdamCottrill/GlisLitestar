from FnDbTable import FishNetDbTable

keyfields = ["PRJ_CD", "SAM", "EFF", "SPC", "GRP", "SIZ"]
data_flds = ["SIZCNT", "COMMENT4"]

FN124 = FishNetDbTable(table_name="FN124", keyfields=keyfields, data_fields=data_flds)
