"""=============================================================
 c:/Users/COTTRILLAD/1work/Python/pydantic_playground/tests/test_FN028.py
 Created: 25 Aug 2021 15:23:07

 DESCRIPTION:

  A suite of unit tests to ensure that the Pydantic model for FN028
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
from datetime import time

from src.schemas import FN028


@pytest.fixture()
def data():
    data = {
        "prj_cd": "LHA_IA19_002",
        "mode": "A1",
        "mode_des": "the lake",
        "gr": "GL01",
        "orient": "1",
        "gruse": "2",
        "effdur_ge": 0.1,
        "effdur_lt": 1.0,
        "efftm0_ge": time(8, 0, 0),
        "efftm0_lt": time(16, 0, 0),
    }
    return data


def test_valid_data(data):
    """

    Arguments:
    - `data`:
    """

    item = FN028(**data)

    assert item.prj_cd == data["prj_cd"]
    assert item.mode == data["mode"].strip().title()
    assert item.mode_des == data["mode_des"].strip().title()


required_fields = [
    ("prj_cd", "Input should be a valid string"),
    ("mode", "Input should be a valid string"),
    ("gr", "Input should be a valid string"),
    ("orient", "Input should be '1','2','3','9','d' or 'u'"),
    ("gruse", "Input should be a valid integer"),
]


@pytest.mark.parametrize("fld,msg", required_fields)
def test_required_fields(data, fld, msg):
    """Verify that the required fields without custome error message
    raise the default messge if they are not provided.


    Arguments:
    - `data`:

    """

    data[fld] = None

    with pytest.raises(ValidationError) as excinfo:
        FN028(**data)
    assert msg in str(excinfo.value)


optional_fields = ["mode_des", "effdur_ge", "effdur_lt", "efftm0_ge", "efftm0_lt"]


@pytest.mark.parametrize("fld", optional_fields)
def test_optional_fields(data, fld):
    """Verify that the FN028 item is created without error if an optional field is omitted

    Arguments:
    - `data`:

    """

    data[fld] = None
    item = FN028(**data)
    assert item.prj_cd == data["prj_cd"]


mode_list = [
    # field, input, output
    (
        "mode_des",
        "Bottom Set Gill Nets Accross Contours",
        "Bottom Set Gill Nets Accross Contours",
    ),
    (
        "mode_des",
        "BOTTOM SET GILL NETS ACCROSS CONTOURS",
        "Bottom Set Gill Nets Accross Contours",
    ),
    (
        "mode_des",
        "bottom set gill nets accross contours",
        "Bottom Set Gill Nets Accross Contours",
    ),
    (
        "mode_des",
        None,
        "Not Specified",
    ),
]


@pytest.mark.parametrize("fld,value_in,value_out", mode_list)
def test_valid_alternatives(data, fld, value_in, value_out):
    """When the pydanic model is created, it should transform some fo the
    fields.  Mode should be a two letter code made from uppercase
    letters or digits.  The pydantic model should convert any letters
    to uppercase automatically. Uppercase letters and any numbers
    should be returned unchanged.  mode_des should be trimmed of any
    white mode and converted to upper case.

    Arguments:
    - `data`:

    """

    data[fld] = value_in
    item = FN028(**data)
    item_dict = item.model_dump()
    assert item_dict[fld] == value_out


error_list = [
    (
        "mode",
        "AA1",
        "String should have at most 2 characters",
    ),
    (
        "mode",
        "A*",
        "String should match pattern '^([A-Z0-9]{2})$'",
    ),
    ("effdur_ge", -3.14, "Input should be greater than 0"),
    ("effdur_lt", -3.14, "Input should be greater than 0"),
    ("effdur_ge", 0, "Input should be greater than 0"),
    ("effdur_lt", 0, "Input should be greater than 0"),
    (
        "efftm0_lt",
        time(6, 0, 0),
        "Latest set time (efftm0_lt=06:00:00) is earlier than earliest set time(efftm0_ge=08:00:00)",
    ),
    ("efftm0_ge", "foo", "Input should be in a valid time format"),
    ("efftm0_lt", "foo", "Input should be in a valid time format"),
    ("orient", 99, "Input should be '1','2','3','9','d' or 'u'"),
    ("gruse", 99, "Input should be 1,2,3,4,5,6,7 or 9"),
]


@pytest.mark.parametrize("fld,value,msg", error_list)
def test_invalid_data(data, fld, value, msg):
    """

    Arguments:
    - `data`:
    """

    data[fld] = value
    with pytest.raises(ValidationError) as excinfo:
        FN028(**data)
    assert msg in str(excinfo.value)
