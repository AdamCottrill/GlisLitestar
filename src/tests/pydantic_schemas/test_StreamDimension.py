"""=============================================================
 ~/fn_portal/tests/pydantic_schemas/test_StreamDimension.py
 Created: 31 May 2023 15:11:21

 DESCRIPTION:

  A suite of unit tests to ensure that the Pydantic model for StreamDimension
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

from src.schemas import StreamDimension


@pytest.fixture()
def data():
    # metres_across and width are both null by default to prevent validation collisions.
    data = {
        "prj_cd": "LHA_IA19_002",
        "subspace": "AA1",
        "metres_up": 1,
        "metres_across": None,
        "width": None,
        "depth": 5,
        "velocity": 0.9,
        "comment": "a fake comment",
    }
    return data


def test_valid_data(data):
    """

    Arguments:
    - `data`:
    """

    item = StreamDimension(**data)

    assert item.prj_cd == data["prj_cd"]
    assert item.subspace == data["subspace"]
    assert item.metres_up == data["metres_up"]
    assert item.depth == data["depth"]
    assert item.velocity == data["velocity"]


required_fields = [
    ("prj_cd", "string"),
    ("subspace", "string"),
    ("metres_up", "integer"),
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
        StreamDimension(**data)

    msg = f"Input should be a valid {data_type}"
    assert msg in str(excinfo.value)


optional_fields = ["across", "width", "depth", "velocity", "comment"]


@pytest.mark.parametrize("fld", optional_fields)
def test_optional_fields(data, fld):
    """Verify that the StreamDimension item is created without error if an
    optional field is omitted

    Arguments:
    - `data`:

    """
    data[fld] = None
    item = StreamDimension(**data)

    assert item.prj_cd == data["prj_cd"]
    assert item.subspace == data["subspace"]
    assert item.metres_up == data["metres_up"]
    assert item.depth == data["depth"]
    assert item.velocity == data["velocity"]


subspace_list = [
    # field, input, output
    ("metres_up", "4", 4),
    ("metres_across", "0", 0),
    ("width", "0", 0),
    ("depth", "0", 0),
    ("velocity", "0", 0),
    ("metres_across", "1.1", 1.1),
    ("width", "1.1", 1.1),
    ("depth", "1.1", 1.1),
    ("velocity", "1.1", 1.1),
    ("metres_across", "", None),
    ("width", "", None),
    ("depth", "", None),
    ("velocity", "", None),
    ("comment", "", None),
]


@pytest.mark.parametrize("fld,value_in,value_out", subspace_list)
def test_valid_alternatives(data, fld, value_in, value_out):
    """When the pydanic model is created, it should transform some fo the
    fields -  from strings to floats and empty sstrings to None.

    Arguments:
    - `data`:

    """
    data[fld] = value_in
    item = StreamDimension(**data)
    item_dict = item.dict()
    assert item_dict[fld] == value_out


def test_width_more_than_metres_across(data):
    """A stream dimension should still be valid if metre_across is less than width.

    - `data`:

    """

    width = 2.4
    metres_across = 1.2
    data["width"] = width
    data["metres_across"] = metres_across
    item = StreamDimension(**data)
    item_dict = item.dict()
    assert item_dict["width"] == width
    assert item_dict["metres_across"] == metres_across


def test_width_less_than_metres_across(data):
    """A stream dimension should not be valid if metre_across is more than width.

    - `data`:

    """

    width = 1.2
    metres_across = 2.4
    data["width"] = width
    data["metres_across"] = metres_across

    msg = f"width ({width}) cannot be less than metres_across ({metres_across})"
    with pytest.raises(ValidationError) as excinfo:
        StreamDimension(**data)
    assert msg in str(excinfo.value)


error_list = [
    ("metres_up", -1, "Input should be greater than or equal to 0"),
    ("metres_up", 2000, "Input should be less than or equal to 1100"),
    ("metres_across", -1, "Input should be greater than or equal to 0"),
    ("metres_across", 201, "Input should be less than or equal to 200"),
    ("width", -1, "Input should be greater than or equal to 0"),
    ("width", 201, "Input should be less than or equal to 200"),
    ("depth", -1, "Input should be greater than or equal to 0"),
    ("depth", 11, "Input should be less than or equal to 10"),
    ("velocity", -1, "Input should be greater than or equal to 0"),
    ("velocity", 11, "Input should be less than or equal to 5"),
]


@pytest.mark.parametrize("fld,value,msg", error_list)
def test_invalid_data(data, fld, value, msg):
    """

    Arguments:
    - `data`:
    """

    data[fld] = value
    with pytest.raises(ValidationError) as excinfo:
        StreamDimension(**data)
    assert msg in str(excinfo.value)
