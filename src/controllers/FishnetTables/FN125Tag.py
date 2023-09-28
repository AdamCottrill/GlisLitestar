from FnDbTable import FishNetDbTable

keyfields = ["PRJ_CD", "SAM", "EFF", "SPC", "GRP", "FISH", "FISH_TAG_ID"]
data_flds = ["TAGID", "TAGDOC", "TAGSTAT", "CWTSEQ", "COMMENT_TAG"]

FN125Tag = FishNetDbTable(
    table_name="FN125_Tags", keyfields=keyfields, data_fields=data_flds
)
