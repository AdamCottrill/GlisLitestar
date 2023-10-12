"""=============================================================
 ~/fn_portal/fn_portal/tests/pydantic_schemas/test_FN121GpsTrack.py
 Created: 27 May 2022 11:52:44

 DESCRIPTION:

  A suite of unit tests to ensure that the Pydantic model for FN121GpsTrack
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

from datetime import datetime
import pytest
from pydantic import ValidationError

from src.schemas import FN121GpsTrack


@pytest.fixture()
def data():
    data = {
        "prj_cd": "LHA_IA19_002",
        "sam": "1",
        "trackid": 1,
        "dd_lat": 45.5,
        "dd_lon": -81.5,
        "sidep": 12.0,
        "timestamp": datetime.now(),
        "comment": "test comment",
    }
    return data


def test_valid_data(data):
    """

    Arguments:
    - `data`:
    """

    item = FN121GpsTrack(**data)

    assert item.prj_cd == data["prj_cd"]
    assert item.sam == data["sam"]
    assert item.trackid == data["trackid"]


required_fields = [
    ("prj_cd", "string"),
    ("sam", "string"),
    ("trackid", "integer"),
    ("dd_lat", "number"),
    ("dd_lon", "number"),
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
        FN121GpsTrack(**data)
    msg = f"Input should be a valid {data_type}"
    assert msg in str(excinfo.value)


optional_fields = ["sidep", "timestamp", "comment"]


@pytest.mark.parametrize("fld", optional_fields)
def test_optional_fields(data, fld):
    """Verify that the FN121GpsTrack item is created without error if
    an optional field is omitted

    Arguments:
    - `data`:

    """
    data[fld] = None
    item = FN121GpsTrack(**data)

    assert item.prj_cd == data["prj_cd"]
    assert item.sam == data["sam"]
    assert item.trackid == data["trackid"]


alternative_values_list = [
    # field, input, output
    ("dd_lat", "45.1", 45.1),
    ("dd_lon", "-81.9", -81.9),
    ("sidep", "", None),
    ("sidep", "10.1", 10.1),
]


@pytest.mark.parametrize("fld,value_in,value_out", alternative_values_list)
def test_valid_alternatives(data, fld, value_in, value_out):
    """When the pydanic model is created, it should transform some fo the
    fields.  If the trapnet values are strings instead of numbers
    they should be converted to number. If they are empty strings,
    they should be None.

    Arguments:
    - `data`:

    """
    data[fld] = value_in
    item = FN121GpsTrack(**data)
    item_dict = item.dict()
    assert item_dict[fld] == value_out


error_list = [
    ("dd_lat", 40.0, "Input should be greater than or equal to 41.7"),
    (
        "dd_lat",
        50.1,
        "Input should be less than or equal to 49.2",
    ),
    ("dd_lon", -90.0, "Input should be greater than or equal to -89.6"),
    (
        "dd_lon",
        -75.1,
        "Input should be less than or equal to -76.4",
    ),
    ("trackid", -1, "Input should be greater than 0"),
    ("sidep", -1.0, "Input should be greater than or equal to 0"),
    ("sidep", 500.0, "Input should be less than or equal to 400"),
    # ("timestamp", "2020-10-16 12:34:16", "Input should be greater than or equal to 0"),
]


@pytest.mark.parametrize("fld,value,msg", error_list)
def test_invalid_data(data, fld, value, msg):
    """

    Arguments:
    - `data`:
    """

    data[fld] = value
    with pytest.raises(ValidationError) as excinfo:
        FN121GpsTrack(**data)

    assert msg in str(excinfo.value)
