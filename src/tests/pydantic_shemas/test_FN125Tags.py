"""=============================================================
 c:/Users/COTTRILLAD/1work/Python/pydantic_playground/tests/test_FN125Tag.py
 Created: 26 Aug 2021 16:43:50

 DESCRIPTION:

  A suite of unit tests to ensure that the Pydantic model for FN125Tag
  objects validate as expected.

  The script includes:

  1.  a dictionary that representes complete, valid data.

  2. a list of fields and associated modifications that should be
     automatically tranformed by Pydantic (e.g. trimming whitespaces
     and converting to title case)

  3. a list of required fields that are systematically omitted,

  4. and finally a list of changes to the dictionary of good data that
     invalidates it in a known way and verifies that pydantic raises
     the expected exception.

 A. Cottrill
=============================================================

"""


import pytest
from pydantic import ValidationError

from src.schemas import FN125Tag


@pytest.fixture()
def data():
    data = {
        "prj_cd": "LEA_IA17_097",
        "sam": "4009",
        "eff": "114",
        "spc": "081",
        "grp": "00",
        "fish": 1,
        "fish_tag_id": 1,
        "tagid": "123654A",
        "tagdoc": "25012",
        "tagstat": "A",
        "cwtseq": None,
        "comment_tag": "not a real tag",
    }
    return data


def test_valid_data(data):
    """

    Arguments:
    - `data`:
    """
    item = FN125Tag(**data)

    assert item.prj_cd == data["prj_cd"]
    assert item.sam == data["sam"]


required_fields = [
    ("prj_cd","string"),
    ("sam","string"),
    ("eff","string"),
    ("spc","string"),
    ("grp","string"),
    ("fish","integer"),
    ("fish_tag_id","integer"),
    ("tagdoc","string"),
    ("tagstat","string"),
]


@pytest.mark.parametrize("fld,data_type", required_fields)
def test_required_fields(data, fld, data_type):
    """Verify that the required fields without custome error message
    raise the default messge if they are not provided.


    Arguments:
    - `data`:

    """

    data[fld] = None
    with pytest.raises(ValidationError) as excinfo:
        FN125Tag(**data)
    msg = f"Input should be a valid {data_type}"
    assert msg in str(excinfo.value)


optional_fields = ["cwtseq", "comment_tag"]


@pytest.mark.parametrize("fld", optional_fields)
def test_optional_fields(data, fld):
    """Verify that the FN125Tag item is created without error if an optional field is omitted

    Arguments:
    - `data`:

    """
    data[fld] = None
    item = FN125Tag(**data)
    assert item.prj_cd == data["prj_cd"]
    assert item.sam == data["sam"]
    assert item.eff == data["eff"]
    assert item.spc == data["spc"]
    assert item.grp == data["grp"]
    assert item.fish == data["fish"]



mode_list = [
    # field, input, output
    ("cwtseq", "", None),
]


@pytest.mark.parametrize("fld,value_in,value_out", mode_list)
def test_valid_alternatives(data, fld, value_in, value_out):
    """When the pydanic model is created, it should transform some fo the
    fields.  GRP should be a two letter code made from uppercase
    letters or digits.  The pydantic model should convert any letters
    to uppercase automatically. Uppercase letters and any numbers
    should be returned unchanged.

    Arguments:
    - `data`:

    """
    data[fld] = value_in
    item = FN125Tag(**data)
    item_dict = item.model_dump()
    assert item_dict[fld] == value_out


error_list = [
    (
        "cwtseq",
        -4,
        "Input should be greater than 0",
    ),
    ("tagdoc", "X", "String should have at least 5 characters"),
    ("tagdoc", "1234567", "String should have at most 5 characters"),
    ("tagdoc", "1234*", "String should match pattern '^([A-Z0-9]{5})$'"),
    ("tagdoc", "Z1234", "Unknown tag_type code (Z) found in TAGDOC (Z1234)"),
    ("tagdoc", "0Z234", "Unknown tag_position code (Z) found in TAGDOC (0Z234)"),
    ("tagdoc", "01ZZ4", "Unknown tag_agency code (ZZ) found in TAGDOC (01ZZ4)"),
    ("tagdoc", "0123Z", "Unknown tag_colour code (Z) found in TAGDOC (0123Z)"),
]


@pytest.mark.parametrize("fld,value,msg", error_list)
def test_invalid_data(data,  fld, value, msg):
    """

    Arguments:
    - `data`:
    """

    data[fld] = value
    with pytest.raises(ValidationError) as excinfo:
        FN125Tag(**data)

    assert msg in str(excinfo.value)


# THere are some co-dependencies between fields - some combination are
# valid, other are not.  These tests check first to ensure that valid
# combination work, and then that invalid ones are caught and reported
# appropriately:

valid_combinations = [
    # tag stat can be N if tag is is empy and tagdoc starts with 6 or p
    {"tagstat": "N", "tagid": None, "tagdoc": "P1234"},
    {"tagstat": "N", "tagid": None, "tagdoc": "61234"},
]


@pytest.mark.parametrize("fld_values", valid_combinations)
def test_valid_field_combinations(data, fld_values):
    """

    Arguments:
    - `data`:
    """

    data.update(fld_values)
    item = FN125Tag(**data)

    assert item.prj_cd == data["prj_cd"]
    assert item.sam == data["sam"]
    assert item.eff == data["eff"]
    assert item.spc == data["spc"]
    assert item.grp == data["grp"]
    assert item.fish == data["fish"]

invalid_combinations = [
    # tag stat can only be "N" if tagid is is empty and tagdoc starts with 6 or p
    [
        {"tagstat": "N", "tagid": 1234, "tagdoc": "P1234"},
        "TAGSTAT cannot be 'N' if TAGID is populated (TAGID='1234')",
    ],
    [
        {"tagstat": "N", "tagid": None, "tagdoc": "21234"},
        "TAGSTAT='N' is only allowed if TAGTYPE is 6 (CWT) or P (PIT).",
    ],
    [
        {"tagstat": "A", "tagid": None, "tagdoc": "21234"},
        "TAGID cannot be empty if TAGSTAT='A' (tag applied).",
    ],
]


@pytest.mark.parametrize("fld_values,msg", invalid_combinations)
def test_invalid_combinations(data, fld_values, msg):
    """

    Arguments:
    - `data`:
    """
    data.update(fld_values)

    with pytest.raises(ValidationError) as excinfo:
        FN125Tag(**data)

    assert msg in str(excinfo.value)


valid_tagstats = [
    {"tagstat": "A", "tagid": 12345, "tagdoc": "99999"},
    {"tagstat": "A2", "tagid": 12345, "tagdoc": "99999"},
    {"tagstat": "C", "tagid": 12345, "tagdoc": "99999"},
    {"tagstat": "C139", "tagid": 12345, "tagdoc": "99999"},
    {"tagstat": "C011", "tagid": 12345, "tagdoc": "99999"},
    {"tagstat": "C499", "tagid": 12345, "tagdoc": "99999"},
]


@pytest.mark.parametrize("values", valid_tagstats)
def test_valid_tagstat(data, values):
    """The tagstat validator has been updated to use a regular
    expresstion rather than a enum to ensure that can adequately
    capture the disposition and condition codes that are sometimes
    collected.  This test ensures that valid alternatives are correcly
    treated as valid.
    Arguments:
    - `data`:
    """

    data.update(values)
    item = FN125Tag(**data)
    item_dict = item.model_dump()
    assert item_dict["tagstat"] == values["tagstat"]


invalid_tagstats = [
    "A1",
    "A0",
    "N1",
    "C811",
    "C899",
    "A111",
    "A019",
    "N111",
    "N019",
    "C81",
    "C0",
    "C2",
    "C299",
]


@pytest.mark.parametrize("tagstat", invalid_tagstats)
def test_invalid_tagstat(
    data,
    tagstat,
):
    """The tagstat validator has been updated to use a regular
    expresstion rather than a enum to ensure that can adequately
    capture the disposition and condition codes. This test ensures
    that invalid codes are flagged as invalid.
    Arguments:
    - `data`:
    """

    data["tagstat"] = tagstat
    with pytest.raises(ValidationError) as excinfo:
        FN125Tag(**data)

    msg = "String should match pattern '^(N|A2?|C([0134][1-49][1-49])?)$'"
    assert msg in str(excinfo.value)
