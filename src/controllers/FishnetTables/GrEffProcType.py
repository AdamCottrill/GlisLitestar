from FnDbTable import FishNetDbTable

keyfields = ["GR", "EFF", "PROCESS_TYPE"]
data_flds = [
    "EFFDST",
]

GrEffProcType = FishNetDbTable(
    table_name="Gear_Effort_Process_Types", keyfields=keyfields, data_fields=data_flds
)
