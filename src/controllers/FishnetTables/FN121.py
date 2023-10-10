from FnDbTable import FishNetDbTable

# GRDEP
# GRTEM

keyfields = ["PRJ_CD", "SAM"]
data_flds = [
    "PROCESS_TYPE",
    "SSN",
    "SUBSPACE",
    "MODE",
    "EFFDT0",
    "EFFTM0",
    "EFFDT1",
    "EFFTM1",
    "EFFDUR",
    "EFFST",
    "SITP",
    "DD_LAT0",
    "DD_LON0",
    "DD_LAT1",
    "DD_LON1",
    "GRID5",
    "SITEM0",
    "SITEM1",
    "SIDEP0",
    "SIDEP1",
    "GRDEPMIN",
    "GRDEPMAX",
    "GRDEPMID",
    "SECCHI0",
    "SECCHI1",
    "SLIME",
    "CREW",
    "COMMENT1",
    # trawl fields
    "VESSEL",
    "VESSEL_SPEED",
    "VESSEL_DIRECTION",
    "WARP",
    # trapnet fields
    "BOTTOM",
    "COVER",
    "VEGETATION",
    "LEAD_ANGLE",
    "LEADUSE",
    "DISTOFF",
    # limno fields
    "O2GR0",
    "O2GR1",
    "O2BOT0",
    "O2BOT1",
    "O2SURF0",
    "O2SURF1",
    # weather fields
    "AIRTEM0",
    "AIRTEM1",
    "CLOUD_PC0",
    "CLOUD_PC1",
    "WAVEHT0",
    "WAVEHT1",
    "PRECIP0",
    "PRECIP1",
    "WIND0",
    "WIND1",
    "XWEATHER",
]


FN121 = FishNetDbTable(table_name="FN121", keyfields=keyfields, data_fields=data_flds)
