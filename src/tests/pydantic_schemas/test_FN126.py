"""=============================================================
 c:/Users/COTTRILLAD/1work/Python/pydantic_playground/tests/test_FN126.py
 Created: 26 Aug 2021 16:43:50

 DESCRIPTION:

  A suite of unit tests to ensure that the Pydantic model for FN126
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

from src.schemas import FN126


@pytest.fixture()
def data():
    data = {
        "prj_cd": "LEA_IA17_097",
        "sam": "4009",
        "eff": "114",
        "spc": "081",
        "grp": "00",
        "fish": "1",
        "food": 1,
        "taxon": "7121",
        "fdcnt": 12,
        "fdmes": "L",
        "fdval": 100,
        "lifestage": None,
        "comment6": "A diet item.",
    }
    return data


def test_valid_data(data):
    """

    Arguments:
    - `data`:
    """

    item = FN126(**data)

    assert item.prj_cd == data["prj_cd"]
    assert item.sam == data["sam"]
    assert item.eff == data["eff"]
    assert item.spc == data["spc"]
    assert item.grp == data["grp"]
    assert item.fish == data["fish"]
    assert item.food == data["food"]


required_fields = [
        ("prj_cd","string"),
        ("sam","string"),
        ("eff","string"),
        ("spc","string"),
        ("grp","string"),
        ("fish","string"),
        ("food","integer"),
        ("taxon","string"),
]


@pytest.mark.parametrize("fld,data_type", required_fields)
def test_required_fields(data, data_type, fld):
    """Verify that the required fields without custome error message
    raise the default messge if they are not provided.


    Arguments:
    - `data`:

    """

    data[fld] = None

    with pytest.raises(ValidationError) as excinfo:
        FN126(**data)
    msg = f"Input should be a valid {data_type}"
    assert msg in str(excinfo.value)


optional_fields = ["fdcnt", "lifestage", "comment6"]


@pytest.mark.parametrize("fld", optional_fields)
def test_optional_fields(data, fld):
    """Verify that the FN126 item is created without error if an
    optional field is omitted

    Arguments:
    - `data`:

    """

    data[fld] = None
    item = FN126(**data)

    assert item.prj_cd == data["prj_cd"]
    assert item.sam == data["sam"]
    assert item.eff == data["eff"]
    assert item.spc == data["spc"]
    assert item.grp == data["grp"]
    assert item.fish == data["fish"]
    assert item.food == data["food"]



paired_field_list = [
    ("fdmes", "fdval", None, None),
]


@pytest.mark.parametrize("fld1,fld2,val1,val2", paired_field_list)
def test_paired_fields(data, fld1, fld2, val1, val2):
    """Fdmes and fdval are optional fields, but only if they are both
    null.  Otherwise, they are both required.  Arguments: - `data`:

    """
    data[fld1] = val1
    data[fld2] = val2
    item = FN126(**data)

    assert item.prj_cd == data["prj_cd"]
    assert item.sam == data["sam"]
    assert item.eff == data["eff"]
    assert item.spc == data["spc"]
    assert item.grp == data["grp"]
    assert item.fish == data["fish"]
    assert item.food == data["food"]



mode_list = [
    # field, input, output
    ("fdcnt", "", None),
    # ("fdval", "", None),
    ("lifestage", "", None),
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
    item = FN126(**data)
    item_dict = item.model_dump()
    assert item_dict[fld] == value_out


error_list = [
    (
        "fdcnt",
        -4,
        "Input should be greater than or equal to 0",
    ),
    (
        "lifestage",
        -4,
        "Input should be greater than 0",
    ),
    (
        "fdval",
        -4.0,
        "Input should be greater than 0",
    ),
    (
        "fdmes",
        "foo",
        "Input should be 'L','V' or 'W'",
    ),
    (
        "fdval",
        None,
        "fdval must be populated if fdmes is provided.",
    ),
    (
        "fdmes",
        None,
        "fdmes must be populated if fdval is provided.",
    ),
    (
        "fdval",
        "",
        "fdval must be populated if fdmes is provided.",
    ),
    (
        "fdmes",
        "",
        "fdmes must be populated if fdval is provided.",
    ),
    (
        "taxon",
        None,
        "Input should be a valid string",
    ),
]


@pytest.mark.parametrize("fld,value,msg", error_list)
def test_invalid_data(data, fld, value, msg):
    """

    Arguments:
    - `data`:
    """

    data[fld] = value
    with pytest.raises(ValidationError) as excinfo:
        FN126(**data)

    assert msg in str(excinfo.value)
