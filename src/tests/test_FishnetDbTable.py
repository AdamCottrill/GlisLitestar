from src.FnDbTable import FishNetDbTable

import pytest


def strip_string(target: str) -> str:
    """convert to uppercase and strip any spaces and carriage returns
    from a string.
    """
    return target.upper().replace(" ", "").replace("\n", "")


@pytest.fixture
def fishnet_table():
    keyfields = ["PRJ_CD", "SAM", "EFF"]
    data_flds = [
        "EFFDST",
        "GRDEP0",
        "GRDEP1",
        "GRTEM0",
        "GRTEM1",
        "WATERHAUL",
        "COMMENT2",
    ]

    fn122 = FishNetDbTable(
        table_name="FN122", keyfields=keyfields, data_fields=data_flds
    )

    return fn122


def test_fntable_str(fishnet_table):
    assert str(fishnet_table) == "FN122"


def test_fntable_table_name(fishnet_table):
    assert fishnet_table.table_name == "FN122"


def test_fntable_keyfields(fishnet_table):
    keyfields = fishnet_table.keyfields
    should_be = ["PRJ_CD", "SAM", "EFF"]
    assert should_be == keyfields


def test_fntable_fields(fishnet_table):
    should_be = [
        "PRJ_CD",
        "SAM",
        "EFF",
        "EFFDST",
        "GRDEP0",
        "GRDEP1",
        "GRTEM0",
        "GRTEM1",
        "WATERHAUL",
        "COMMENT2",
    ]

    assert fishnet_table.fields == should_be


def test_fntable_select(fishnet_table):
    sql = fishnet_table.select()
    should_be = """
    SELECT [PRJ_CD],
     [SAM],
     [EFF],
     [EFFDST],
     [GRDEP0],
     [GRDEP1],
     [GRTEM0],
     [GRTEM1],
     [WATERHAUL],
     [COMMENT2]
    FROM [FN122] ORDER BY [PRJ_CD], [SAM],[EFF]"""

    assert strip_string(sql) == strip_string(should_be)


def test_fntable_select_order_by_true(fishnet_table):
    sql = fishnet_table.select(order_by_keys=True)
    should_be = """
    SELECT [PRJ_CD],
     [SAM],
     [EFF],
     [EFFDST],
     [GRDEP0],
     [GRDEP1],
     [GRTEM0],
     [GRTEM1],
     [WATERHAUL],
     [COMMENT2]
    FROM [FN122] ORDER BY [PRJ_CD], [SAM],[EFF]
    """

    assert strip_string(sql) == strip_string(should_be)


def test_fntable_select_order_by_false(fishnet_table):
    sql = fishnet_table.select(order_by_keys=False)
    should_be = """
    SELECT [PRJ_CD],
     [SAM],
     [EFF],
     [EFFDST],
     [GRDEP0],
     [GRDEP1],
     [GRTEM0],
     [GRTEM1],
     [WATERHAUL],
     [COMMENT2]
    FROM [FN122]
    """

    assert strip_string(sql) == strip_string(should_be)


def test_fntable_select_w_filters(fishnet_table):
    criteria = ["EFF", "EFFDST"]
    sql = fishnet_table.select(criteria, False)

    should_be = """
    SELECT [PRJ_CD],
     [SAM],
     [EFF],
     [EFFDST],
     [GRDEP0],
     [GRDEP1],
     [GRTEM0],
     [GRTEM1],
     [WATERHAUL],
     [COMMENT2]
    FROM [FN122] WHERE [EFF]=? AND [EFFDST]=?
    """

    assert strip_string(sql) == strip_string(should_be)


def test_fntable_select_w_filters_order_by(fishnet_table):
    criteria = ["EFF", "EFFDST"]
    sql = fishnet_table.select(filters=criteria)

    should_be = """
    SELECT [PRJ_CD],
     [SAM],
     [EFF],
     [EFFDST],
     [GRDEP0],
     [GRDEP1],
     [GRTEM0],
     [GRTEM1],
     [WATERHAUL],
     [COMMENT2]
    FROM [FN122] WHERE [EFF]=? AND [EFFDST]=?
    ORDER BY [PRJ_CD], [SAM], [EFF]
    """

    assert strip_string(sql) == strip_string(should_be)


def test_fntable_select_one(fishnet_table):
    sql = fishnet_table.select_one()
    should_be = """
    SELECT [PRJ_CD],
     [SAM],
     [EFF],
     [EFFDST],
     [GRDEP0],
     [GRDEP1],
     [GRTEM0],
     [GRTEM1],
     [WATERHAUL],
     [COMMENT2]
    FROM [FN122] WHERE
    [PRJ_CD]=? AND
     [SAM]=? AND
     [EFF]=?;
    """

    assert strip_string(sql) == strip_string(should_be)


def test_fntable_delete_one(fishnet_table):
    sql = fishnet_table.delete_one()

    should_be = """
    DELETE
    FROM [FN122] WHERE
    [PRJ_CD]=? AND
     [SAM]=? AND
     [EFF]=?;
    """

    assert strip_string(sql) == strip_string(should_be)


def test_fntable_create(fishnet_table):
    sql = fishnet_table.create()
    should_be = """
    INSERT INTO [FN122] ([PRJ_CD],
     [SAM],
     [EFF],
     [EFFDST],
     [GRDEP0],
     [GRDEP1],
     [GRTEM0],
     [GRTEM1],
     [WATERHAUL],
     [COMMENT2]) VALUES  (?,?,?,?,?,?,?,?,?,?)
    """
    assert strip_string(sql) == strip_string(should_be)


def test_fntable_update(fishnet_table):
    updates = {"GRDEP0": 34, "COMMENT2": "An Update"}
    sql = fishnet_table.update_one(updates)

    should_be = """
    UPDATE [FN122] SET
     [GRDEP0] = ?,
     [COMMENT2] = ?
    WHERE
     [PRJ_CD]=? AND
     [SAM]=? AND
     [EFF]=?
    """
    assert strip_string(sql) == strip_string(should_be)


def test_values(fishnet_table):
    """the Fishnet table class has a values method that will accept a
    dictionary and return a list of values that are sorted in the same
    order as the fields in the FishnetTable class.
    """

    # jumbled dict to start
    data_dict = {
        "sam": "4009",
        "effdst": 75,
        "waterhaul": False,
        "eff": "114",
        "grdep1": 12.5,
        "grdep0": 12,
        "grtem0": 12.2,
        "grtem1": 13.1,
        "prj_cd": "LEA_IA17_097",
        "comment2": "best effort yet",
    }

    # original order
    init_order = [
        data_dict["sam"],
        data_dict["effdst"],
        data_dict["waterhaul"],
        data_dict["eff"],
    ]

    # the first 4 elements should be:
    should_be = [
        data_dict["prj_cd"],
        data_dict["sam"],
        data_dict["eff"],
        data_dict["effdst"],
    ]

    # sanity check make sure that the default order of the data dict is
    # based on creation order
    init_values = list(data_dict.values())[:4]
    assert init_values != should_be
    assert init_values == init_order

    observed = fishnet_table.values(data_dict)
    assert observed[:4] == should_be
