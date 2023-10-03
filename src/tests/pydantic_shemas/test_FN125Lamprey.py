"""=============================================================
 c:/Users/COTTRILLAD/1work/Python/pydantic_playground/tests/test_FN125Lamprey.py
 Created: 26 Aug 2021 16:43:50

 DESCRIPTION:

  A suite of unit tests to ensure that the Pydantic model for FN125Lamprey
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

from src.schemas import FN125Lamprey


@pytest.fixture()
def data():
    data = {
        "prj_cd": "LEA_IA17_097",
        "sam": "4009",
        "eff": "114",
        "spc": "081",
        "grp": "00",
        "fish": "1",
        "lamid": 1,
        "xlam": None,
        "lamijc_type": "A1",
        "lamijc_size": 25,
        "comment_lam": "a single test wound",
    }
    return data


def test_valid_data(data):
    """

    Arguments:
    - `data`:
    """

    item = FN125Lamprey(**data)

    assert item.prj_cd == data["prj_cd"]
    assert item.sam == data["sam"]
    assert item.eff == data["eff"]
    assert item.spc == data["spc"]
    assert item.grp == data["grp"]
    assert item.fish == data["fish"]
    assert item.lamid == data["lamid"]


required_fields = [
    ("prj_cd", "string"),
    ("sam", "string"),
    ("eff", "string"),
    ("spc", "string"),
    ("grp", "string"),
    ("fish", "string"),
    ("lamid", "integer"),
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
        FN125Lamprey(**data)

    msg = f"Input should be a valid {data_type}"
    assert msg in str(excinfo.value)


optional_fields = [
    "xlam",
    "lamijc_size",
    "comment_lam",
]


@pytest.mark.parametrize("fld", optional_fields)
def test_optional_fields(data, fld):
    """Verify that the FN125Lamprey item is created without error if an
    optional field is omitted

    Arguments:
    - `data`:

    """
    data[fld] = None
    item = FN125Lamprey(**data)

    assert item.prj_cd == data["prj_cd"]
    assert item.sam == data["sam"]
    assert item.eff == data["eff"]
    assert item.spc == data["spc"]
    assert item.grp == data["grp"]
    assert item.fish == data["fish"]


valid_alternatives = [
    # field, input, output
    ("xlam", "", None),
    ("xlam", "0", "0"),
    ("xlam", "2011", "2011"),
    ("lamijc_size", "", None),
    ("comment_lam", "", None),
]


@pytest.mark.parametrize("fld,value_in,value_out", valid_alternatives)
def test_valid_alternatives(data, fld, value_in, value_out):
    """When the pydanic model is created, it should transform some of the
    fields.  If the field is xlam, make sure we delete the lamijc_type
    in the test so we don't trip the two-types error.

    Arguments:
    - `data`:

    """
    data[fld] = value_in
    if fld == "xlam":
        data["lamijc_type"] = None
    item = FN125Lamprey(**data)
    item_dict = item.dict()
    assert item_dict[fld] == value_out


error_list = [
    (
        "lamijc_size",
        -4,
        "Input should be greater than or equal to 10",
    ),
    (
        "lamijc_type",
        "4",
        "Input should be '0','A1','A2','A3','A4','B1','B2','B3' or 'B4'",
    ),
    (
        "xlam",
        "B535",
        r"String should match pattern '^0|\d{4}$'",
    ),
]


@pytest.mark.parametrize("fld,value,msg", error_list)
def test_invalid_data(data, fld, value, msg):
    """

    Arguments:
    - `data`:
    """

    data[fld] = value
    if fld == "xlam":
        data["lamijc_type"] = None
    with pytest.raises(ValidationError) as excinfo:
        FN125Lamprey(**data)

    assert msg in str(excinfo.value)
