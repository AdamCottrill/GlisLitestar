"""=============================================================
 ~/fn_portal/tests/pydantic_schemas/test_GearProcessType.py
 Created: 02 Oct 2023 15:51:33

 DESCRIPTION:

  A suite of unit tests to ensure that the Pydantic model for
  Gear-ProcessType objects validate as expected.

  The script includes a dictionary that representes complete, valid
  data, it then includes a list of required fields that are
  systematically omitted, and finally a list of changes to the
  dictionary of good data that invalidates it in a known way and
  verifies that pydantic raises the expected exception.

 A. Cottrill
=============================================================

"""


import pytest
from pydantic import ValidationError


from src.schemas import GrEffProcType


@pytest.fixture()
def data():
    data = {"gr": "GL10", "process_type": "2", "eff": "032", "effdst": 15.2}
    return data


def test_valid_data(data):
    """

    Arguments:
    - `data`:
    """

    item = GrEffProcType(**data)

    # check attributes here:
    assert item.gr == data["gr"]
    assert item.eff == data["eff"]
    assert item.process_type == data["process_type"]
    assert item.effdst == data["effdst"]


required_fields = [("gr", "string"), ("eff", "string"), ("process_type", "string")]


@pytest.mark.parametrize("fld,data_type", required_fields)
def test_required_fields(data, fld, data_type):
    """Verify that the required fields without custome error message
    raise the default messge if they are not provided.

    Arguments:
    - `data`:

    """

    data[fld] = None

    with pytest.raises(ValidationError) as excinfo:
        GrEffProcType(**data)
    msg = f"Input should be a valid {data_type}"
    assert msg in str(excinfo.value)


error_list = [
    ("process_type", "X", "Input should be '1','2','3','4' or '5'"),
    (
        "effdst",
        -40.6,
        "Input should be greater than 0",
    ),
    (
        "gr",
        "GL*",
        "String should match pattern '^([A-Z0-9]{2,5})$'",
    ),
    (
        "gr",
        "FOOBAR",
        "String should have at most 5 characters",
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
        GrEffProcType(**data)

    assert msg in str(excinfo.value)
