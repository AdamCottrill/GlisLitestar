"""=============================================================
 c:/Users/COTTRILLAD/1work/Python/pydantic_playground/tests/test_FN127.py
 Created: 26 Aug 2021 16:43:50

 DESCRIPTION:

  A suite of unit tests to ensure that the Pydantic model for FN127
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

from src.schemas import FN127


@pytest.fixture()
def data():
    data = {
        "prj_cd": "LEA_IA17_097",
        "sam": "4009",
        "eff": "114",
        "spc": "081",
        "grp": "00",
        "fish": "1",
        "ageid": 1,
        "preferred": True,
        "agea": 8,
        "agemt": "A2345",
        "edge": "++",
        "conf": 7,
        "nca": 7,
        "comment7": "test record",
    }
    return data


def test_valid_data(data):
    """

    Arguments:
    - `data`:
    """

    item = FN127(**data)

    assert item.prj_cd == data["prj_cd"]
    assert item.sam == data["sam"]
    assert item.eff == data["eff"]
    assert item.spc == data["spc"]
    assert item.grp == data["grp"]
    assert item.fish == data["fish"]
    assert item.ageid == data["ageid"]


required_fields = [
    ("prj_cd", "string"),
    ("sam", "string"),
    ("eff", "string"),
    ("spc", "string"),
    ("grp", "string"),
    ("fish", "string"),
    ("ageid", "integer"),
    ("preferred", "boolean"),
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
        FN127(**data)

    msg = f"Input should be a valid {data_type}"
    assert msg in str(excinfo.value)


optional_fields = ["agea", "agemt", "edge", "conf", "nca", "comment7"]


@pytest.mark.parametrize("fld", optional_fields)
def test_optional_fields(data, fld):
    """Verify that the FN127 item is created without error if an optional field is omitted

    Arguments:
    - `data`:

    """
    data[fld] = None
    item = FN127(**data)

    assert item.prj_cd == data["prj_cd"]
    assert item.sam == data["sam"]
    assert item.eff == data["eff"]
    assert item.spc == data["spc"]
    assert item.grp == data["grp"]
    assert item.fish == data["fish"]
    assert item.ageid == data["ageid"]



alternative_values = [
    # field, input, output
    ("agea", "", None),
    ("agea", "0", 0),
    ("agea", 0, 0),
    ("nca", "", None),
    ("nca", "0", 0),
    ("nca", 0, 0),
    ("conf", "", None),
]


@pytest.mark.parametrize("fld,value_in,value_out", alternative_values)
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
    item = FN127(**data)
    item_dict = item.model_dump()
    assert item_dict[fld] == value_out


error_list = [
    (
        "agea",
        -4,
        "Input should be greater than or equal to 0",
    ),
    (
        "nca",
        -4,
        "Input should be greater than or equal to 0",
    ),
    (
        "edge",
        "foo",
        "Input should be 'o','*','+','++','R','ox','x' or 'o/'"
    ),
    (
        "agemt",
        "foobar",
        "String should have at most 5 characters",
    ),
    (
        "agemt",
        "A",
        "String should match pattern '^([A-Z0-9]{5})$'",
    ),
    (
        "agemt",
        "A124*",
        "String should match pattern '^([A-Z0-9]{5})$'",
    ),
    ("agemt", "Z1111", "Unknown aging structure (Z) found in agemt (Z1111)"),
    ("agemt", "1Z111", "Unknown aging prep1 method (Z) found in agemt (1Z111)"),
    ("agemt", "11Z11", "Unknown aging prep2 method (Z) found in agemt (11Z11)"),
]


@pytest.mark.parametrize("fld,value,msg", error_list)
def test_invalid_data(data, fld, value, msg):
    """

    Arguments:
    - `data`:
    """

    data[fld] = value
    with pytest.raises(ValidationError) as excinfo:
        FN127(**data)

    assert msg in str(excinfo.value)
