"""=============================================================
 c:/Users/COTTRILLAD/1work/Python/pydantic_playground/tests/test_FN028.py
 Created: 25 Aug 2021 15:23:07

 DESCRIPTION:

  A suite of unit tests to ensure that the Pydantic model for FN121
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


from datetime import datetime, time

import pytest
from src.schemas import FN121
from pydantic import ValidationError


@pytest.fixture()
def data():
    data = {
        "prj_cd": "LEA_IA19_123",
        "sam": "12",
        "grid5": "1224",
        "ssn": "00",
        "subspace": "11",
        "mode": "B1",
        "effdt0": datetime(2019, 8, 2),
        "efftm0": time(8, 0, 0),
        "effdt1": datetime(2019, 8, 3),
        "efftm1": time(8, 0, 0),
        "effdur": 24.0,
        "effst": "1",
        "sitp": None,
        "site": "the dock",
        "dd_lat0": 45.5,
        "dd_lon0": -81.2,
        "dd_lat1": 45.6,
        "dd_lon1": -81.1,
        "sitem0": 18.1,
        "sitem1": 21.2,
        "sidep0": 10.2,
        "grdepmin": 8.2,
        "grdepmid": 10.1,
        "grdepmax": 11.6,
        "secchi0": 1.9,
        "secchi1": 3.5,
        "slime": None,
        "crew": "homer",
        "process_type": "2",
        "comment1": "not a real sample",
        "vessel": "tugboat",
        "vessel_speed": 4.0,
        "vessel_direction": 4,
        "warp": 11.0,
        # trapnet fields
        "cover": "BO",
        "bottom": "BO",
        "vegetation": 1,
        "lead_angle": 12,
        "leaduse": 12.5,
        "distoff": 11.0,
        # limnofields
        "o2gr0": 12.0,
        "o2gr1": 12.5,
        "o2bot0": 11.0,
        "o2bot1": 11.0,
        "o2surf0": 14.0,
        "o2surf1": 14.0,
    }
    return data


def test_valid_data(data):
    """

    Arguments:
    - `data`:
    """

    item = FN121(**data)

    assert item.prj_cd == data["prj_cd"]
    assert item.sam == data["sam"]
    assert item.ssn == data["ssn"]
    assert item.subspace == data["subspace"]
    assert item.mode == data["mode"]


required_fields = ["prj_cd", "sam", "grid5", "ssn", "subspace", "mode"]


required_fields = [
    ("prj_cd", "string"),
    ("sam", "string"),
    ("grid5", "string"),
    ("ssn", "string"),
    ("subspace", "string"),
    ("mode", "string"),
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
        FN121(**data)
    msg = f"Input should be a valid {data_type}"
    assert msg in str(excinfo.value)


optional_fields = [
    "effdt0",
    "efftm0",
    "effdt1",
    "efftm1",
    "effdur",
    "effst",
    "sitp",
    "site",
    "sitem0",
    "sitem1",
    "sidep0",
    "grdepmin",
    "grdepmid",
    "grdepmax",
    "secchi0",
    "secchi1",
    "slime",
    "crew",
    "process_type",
    "comment1",
    # trawl fields
    "vessel_speed",
    "vessel_direction",
    "warp",
    # trapnet fields
    # "cover_id",
    # "bottom_id",
    "vegetation",
    "lead_angle",
    "leaduse",
    "distoff",
    # limno fields
    "o2gr0",
    "o2gr1",
    "o2bot0",
    "o2bot1",
    "o2surf0",
    "o2surf1",
]


@pytest.mark.parametrize("fld", optional_fields)
def test_optional_fields(data, fld):
    """Verify that the FN121 item is created without error if an optional field is omitted

    Arguments:
    - `data`:

    """
    data[fld] = None
    item = FN121(**data)

    assert item.prj_cd == data["prj_cd"]
    assert item.sam == data["sam"]
    assert item.ssn == data["ssn"]
    assert item.subspace == data["subspace"]
    assert item.mode == data["mode"]


valid_alternatives_list = [
    # gear depth can be 0, or some small number 0.1
    ("grdepmin", 0),
    ("grdepmin", 0.1),
    # effst can be 1, 5(new) or 9:
    ("effst", "1"),
    ("effst", "5"),
    ("effst", "9"),
]


@pytest.mark.parametrize("fld,value", valid_alternatives_list)
def test_alternative_valid_data(data, fld, value):
    """THis test verifies that alternive values can be provide that will
    still be valid.  This test will be used to capture values taht have
    been submitted in real datasets.

    Arguments:
    - `data`:

    """
    data[fld] = value
    item = FN121(**data)
    item_dict = item.model_dump()
    assert item_dict[fld] == value


field_list = [
    # field, input, output
    ("effdur", "", None),
    ("sidep0", "", None),
    ("secchi0", "", None),
    ("secchi1", "", None),
    ("grdepmin", "", None),
    ("grdepmid", "", None),
    ("grdepmax", "", None),
    ("sitem0", "", None),
    ("sitem1", "", None),
    ("effst", "1", "1"),
    ("effst", "5", "5"),
    ("effst", "9", "9"),
    # trawl fields
    ("vessel_speed", "", None),
    ("vessel_speed", "8.1", 8.1),
    ("vessel_direction", "", None),
    ("warp", "", None),
    ("warp", "10.1", 10.1),
    # trapnet fields
    ("lead_angle", "", None),
    ("lead_angle", "11", 11),
    ("leaduse", "", None),
    ("leaduse", "10.1", 10.1),
    ("distoff", "", None),
    ("distoff", "10.1", 10.1),
    # limno fields
    ("o2gr0", "", None),
    ("o2gr0", "10.1", 10.1),
    ("o2gr1", "", None),
    ("o2gr1", "10.1", 10.1),
    ("o2bot0", "", None),
    ("o2bot0", "10.1", 10.1),
    ("o2bot1", "", None),
    ("o2bot1", "10.1", 10.1),
    ("o2surf0", "", None),
    ("o2surf0", "10.1", 10.1),
    ("o2surf1", "", None),
    ("o2surf1", "10.1", 10.1),
]


@pytest.mark.parametrize("fld,value_in,value_out", field_list)
def test_valid_alternatives(data, fld, value_in, value_out):
    """When the pydanic model is created, it should transform some
    optional fields.  For example fields that contain an empty string
    should be converted to None to eliminate empty strings in our
    master dataset.

    Arguments:
    - `data`:

    """
    data[fld] = value_in
    item = FN121(**data)
    item_dict = item.model_dump()
    assert item_dict[fld] == value_out


paired_field_list = [
    ("dd_lat0", "dd_lon0", "", None),
    ("dd_lat1", "dd_lon1", "", None),
    ("dd_lat0", "dd_lon0", "0", None),
    ("dd_lat1", "dd_lon1", "0", None),
]


@pytest.mark.parametrize("fld1,fld2,value_in,value_out", paired_field_list)
def test_paired_alternatives(data, fld1, fld2, value_in, value_out):
    """When the pydanic model is created, it should transform some
    optional fields.  Some fields must be transformed in pairs - lat
    and long are only valid if they are both populated, or both null.
    Arguments: - `data`:

    """
    data[fld1] = value_in
    data[fld2] = value_in
    item = FN121(**data)
    item_dict = item.model_dump()
    assert item_dict[fld1] == value_out
    assert item_dict[fld2] == value_out


error_list = [
    (
        "dd_lat0",
        None,
        "dd_lat0 must be populated with a valid latitude if dd_lon0 is provided",
    ),
    (
        "dd_lon0",
        None,
        "dd_lon0 must be populated with a valid longitude if dd_lat0 is provided",
    ),
    (
        "dd_lat1",
        None,
        "dd_lat1 must be populated with a valid latitude if dd_lon1 is provided",
    ),
    (
        "dd_lon1",
        None,
        "dd_lon1 must be populated with a valid longitude if dd_lat1 is provided",
    ),
    (
        "dd_lat0",
        "0",
        "dd_lat0 must be populated with a valid latitude if dd_lon0 is provided",
    ),
    (
        "dd_lon0",
        "0",
        "dd_lon0 must be populated with a valid longitude if dd_lat0 is provided",
    ),
    (
        "dd_lat1",
        "0",
        "dd_lat1 must be populated with a valid latitude if dd_lon1 is provided",
    ),
    (
        "dd_lon1",
        "0",
        "dd_lon1 must be populated with a valid longitude if dd_lat1 is provided",
    ),
    (
        "dd_lat0",
        40.6,
        "Input should be greater than or equal to 41.6",
    ),
    (
        "dd_lat0",
        49.5,
        "Input should be less than or equal to 49.2",
    ),
    (
        "dd_lat1",
        40.6,
        "Input should be greater than or equal to 41.6",
    ),
    (
        "dd_lat1",
        49.5,
        "Input should be less than or equal to 49.2",
    ),
    (
        "dd_lon0",
        -90.1,
        "Input should be greater than or equal to -89.6",
    ),
    (
        "dd_lon0",
        -72.0,
        "Input should be less than or equal to -74.32",
    ),
    (
        "dd_lon1",
        -90.1,
        "Input should be greater than or equal to -89.6",
    ),
    (
        "dd_lon1",
        -72.0,
        "Input should be less than or equal to -74.32",
    ),
    (
        "effdur",
        -1.0,
        "Input should be greater than 0",
    ),
    (
        "sidep0",
        -1.0,
        "Input should be greater than 0",
    ),
    (
        "secchi0",
        -1.0,
        "Input should be greater than 0",
    ),
    (
        "secchi1",
        -1.0,
        "Input should be greater than 0",
    ),
    (
        "grdepmin",
        -1.0,
        "Input should be greater than or equal to 0",
    ),
    (
        "grdepmid",
        1.0,
        "grdepmid (1.0 m) must be greater than or equal to grdepmin (8.2 m).",
    ),
    (
        "grdepmid",
        -1.0,
        "Input should be greater than 0",
    ),
    (
        "grdepmax",
        1.0,
        "grdepmax (1.0 m) must be greater than or equal to grdepmin (8.2 m).",
    ),
    (
        "grdepmax",
        -1.0,
        "Input should be greater than 0",
    ),
    (
        "effdt0",
        "foobar",
        "validation error for FN121\neffdt0\n  Input should be a valid date or datetime",
    ),
    (
        "effdt1",
        "foobar",
        "validation error for FN121\neffdt1\n  Input should be a valid date or datetime",
    ),
    (
        "efftm0",
        "foobar",
        "validation error for FN121\nefftm0\n  Input should be in a valid time format",
    ),
    (
        "efftm1",
        "foobar",
        "validation error for FN121\nefftm1\n  Input should be in a valid time format",
    ),
    (
        "effdt0",
        datetime(2018, 8, 3),
        "Set or Lift Date (2018-08-03) is not consistent with prj_cd (2019)",
    ),
    (
        "effdt1",
        datetime(2020, 8, 3),
        "Set or Lift Date (2020-08-03) is not consistent with prj_cd (2019)",
    ),
    (
        "effdt0",
        datetime(2019, 10, 3),
        "Lift date (effdt1=2019-08-03) occurs before set date(effdt0=2019-10-03)",
    ),
    ("slime", 99, "Input should be 0,1,2,3,4 or 5"),
    ("slime", 9, "Input should be 0,1,2,3,4 or 5"),
    ("slime", 6, "Input should be 0,1,2,3,4 or 5"),
    ("process_type", "9", "Input should be '1','2','3','4' or '5'"),
    ("effst", "99", "Input should be '1','5' or '9'"),
    (
        "sitem0",
        -31.1,
        "Input should be greater than or equal to -30",
    ),
    (
        "sitem1",
        -31.1,
        "Input should be greater than or equal to -30",
    ),
    (
        "sitem0",
        31.1,
        "Input should be less than or equal to 30",
    ),
    (
        "sitem1",
        31.1,
        "Input should be less than or equal to 30",
    ),
    ("vessel_speed", -1.0, "Input should be greater than or equal to 0"),
    (
        "vessel_speed",
        10.1,
        "Input should be less than or equal to 10",
    ),
    ("warp", -40.6, "Input should be greater than 0"),
    ("vessel_direction", 11, "Input should be 0,1,2,3,4,5,6,7,8 or 9"),
    ("lead_angle", -1, "Input should be greater than or equal to 0"),
    (
        "lead_angle",
        91,
        "Input should be less than or equal to 90",
    ),
    ("leaduse", -1.0, "Input should be greater than or equal to 0"),
    ("distoff", -40.6, "Input should be greater than or equal to 0"),
    ("vegetation", 0, "Input should be 1,2,3 or 4"),
    # (
    #     "bottom_id",
    #     "ZZ",
    #     "Error validating Bottom=''ZZ''. Valid Bottom values are: ['BO', 'BR', 'CL']",
    # ),
    # (
    #     "cover_id",
    #     "ZZ",
    #     "Error validating Cover=''ZZ''. Valid Cover values are: ['BO', 'CO', 'LT']",
    # ),
    ("o2gr0", -40.6, "Input should be greater than or equal to 0"),
    (
        "o2gr0",
        40.6,
        "Input should be less than or equal to 15",
    ),
    ("o2gr1", -40.6, "Input should be greater than or equal to 0"),
    (
        "o2gr1",
        40.6,
        "Input should be less than or equal to 15",
    ),
    ("o2bot0", -40.6, "Input should be greater than or equal to 0"),
    (
        "o2bot0",
        40.6,
        "Input should be less than or equal to 15",
    ),
    ("o2bot1", -40.6, "Input should be greater than or equal to 0"),
    (
        "o2bot1",
        40.6,
        "Input should be less than or equal to 15",
    ),
    ("o2surf0", -40.6, "Input should be greater than or equal to 0"),
    (
        "o2surf0",
        40.6,
        "Input should be less than or equal to 15",
    ),
    ("o2surf1", -40.6, "Input should be greater than or equal to 0"),
    (
        "o2surf1",
        40.6,
        "Input should be less than or equal to 15",
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
        FN121(**data)

    assert msg in str(excinfo.value)
