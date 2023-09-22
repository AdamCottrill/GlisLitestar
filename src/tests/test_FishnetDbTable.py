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
