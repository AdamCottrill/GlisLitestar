from FnDbTable import FishNetDbTable

keyfields = ["PRJ_CD", "SSN"]
data_flds = ["SSN_DES", "SSN_DATE0", "SSN_DATE1"]


FN022 = FishNetDbTable(table_name="FN022", keyfields=keyfields, data_fields=data_flds)
