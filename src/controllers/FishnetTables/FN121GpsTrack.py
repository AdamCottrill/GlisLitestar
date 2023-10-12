from FnDbTable import FishNetDbTable

keyfields = ["PRJ_CD", "SAM", "TRACKID"]
data_flds = ["DD_LON", "DD_LAT", "Timestamp", "SIDEP"]

FN121GpsTrack = FishNetDbTable(
    table_name="FN121_Gps_Tracks", keyfields=keyfields, data_fields=data_flds
)
