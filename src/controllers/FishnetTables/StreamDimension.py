from FnDbTable import FishNetDbTable

keyfields = ["PRJ_CD", "SUBSPACE", "METRES_UP", "METRES_ACROSS"]
data_flds = ["WIDTH", "DEPTH", "VELOCITY", "COMMENT"]

StreamDimension = FishNetDbTable(
    table_name="Stream_Dimensions", keyfields=keyfields, data_fields=data_flds
)
