"""=============================================================
 c:/Users/COTTRILLAD/1work/Python/pydantic_playground/tests/test_FN123.py
 Created: 26 Aug 2021 16:43:50

 DESCRIPTION:

  A suite of unit tests to ensure that the Pydantic model for FN123
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

from src.schemas import FN123


@pytest.fixture()
def data():
    data = {
        "prj_cd": "LEA_IA17_097",
        "sam": "4009",
        "eff": "114",
        "spc": "081",
        "grp": "00",
        "catcnt": 12,
        "biocnt": 5,
        "catwt": 40.3,
        "subcnt": 3,
        "subwt": 5.6,
        "comment": "never seen so many.",
    }
    return data


def test_valid_data(data):
    """

    Arguments:
    - `data`:
    """

    item = FN123(**data)

    assert item.prj_cd == data["prj_cd"]
    assert item.sam == data["sam"]
    assert item.eff == data["eff"]
    assert item.spc == data["spc"]
    assert item.grp == data["grp"]


required_fields = [
    ("prj_cd", "string"),
    ("sam", "string"),
    ("eff", "string"),
    ("spc", "string"),
    ("grp", "string"),
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
        FN123(**data)
    msg = f"Input should be a valid {data_type}"
    assert msg in str(excinfo.value)


optional_fields = [
    "catcnt",
    "biocnt",
    "catwt",
    "subcnt",
    "subwt",
    "comment",
]


@pytest.mark.parametrize("fld", optional_fields)
def test_optional_fields(data, fld):
    """Verify that the FN123 item is created without error if an optional field is omitted

    Arguments:
    - `data`:

    """
    data[fld] = None
    item = FN123(**data)

    assert item.prj_cd == data["prj_cd"]
    assert item.sam == data["sam"]
    assert item.eff == data["eff"]
    assert item.spc == data["spc"]
    assert item.grp == data["grp"]


mode_list = [
    # field, input, output
    ("catcnt", "", None),
    ("biocnt", "", None),
    ("catwt", "", None),
    ("subcnt", "", None),
    ("subwt", "", None),
    ("grp", "12", "12"),
    ("grp", "AA", "AA"),
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
    item = FN123(**data)
    item_dict = item.model_dump()
    assert item_dict[fld] == value_out


error_list = [
    (
        "catcnt",
        -4,
        "Input should be greater than or equal to 0",
    ),
    (
        "biocnt",
        -4,
        "Input should be greater than or equal to 0",
    ),
    (
        "catwt",
        -31.6,
        "Input should be greater than or equal to 0",
    ),
    (
        "subwt",
        -31.6,
        "Input should be greater than or equal to 0",
    ),
    (
        "catwt",
        -31.6,
        "Input should be greater than or equal to 0",
    ),
    (
        "grp",
        "foo",
        "String should match pattern",
    ),
    (
        "grp",
        "1*",
        "String should match pattern",
    ),
    ("biocnt", 15, "BIOCNT (15) cannot be greater than CATCNT (12)"),
    ("subcnt", 15, "SUBCNT (15) cannot be greater than CATCNT (12)"),
    ("subwt", 50.2, "SUBWT (50.2) cannot be greater than CATWT (40.3)"),
]


@pytest.mark.parametrize("fld,value,msg", error_list)
def test_invalid_data(data, fld, value, msg):
    """

    Arguments:
    - `data`:
    """

    data[fld] = value
    with pytest.raises(ValidationError) as excinfo:
        FN123(**data)

    assert msg in str(excinfo.value)
