import pytest
from pydantic import ValidationError

from src.schemas import FN124


@pytest.fixture()
def data():
    data = {
        "prj_cd": "LEA_IA17_097",
        "sam": "4009",
        "eff": "114",
        "spc": "081",
        "grp": "00",
        "siz": 50,
        "sizcnt": 4,
    }
    return data


def test_valid_data(data):
    """

    Arguments:
    - `data`:
    """

    item = FN124(**data)

    assert item.prj_cd == data["prj_cd"]
    assert item.sam == data["sam"]
    assert item.eff == data["eff"]
    assert item.spc == data["spc"]
    assert item.grp == data["grp"]
    assert item.siz == data["siz"]


required_fields = [
    ("prj_cd", "string"),
    ("sam", "string"),
    ("eff", "string"),
    ("spc", "string"),
    ("grp", "string"),
    ("siz", "integer"),
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
        FN124(**data)
    msg = f"Input should be a valid {data_type}"
    assert msg in str(excinfo.value)


error_list = [
    (
        "siz",
        -4,
        "Input should be greater than or equal to 10",
    ),
    (
        "siz",
        9,
        "Input should be greater than or equal to 10",
    ),
    (
        "sizcnt",
        -4,
        "Input should be greater than 0",
    ),
    (
        "sizcnt",
        0,
        "Input should be greater than 0",
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
        FN124(**data)

    assert msg in str(excinfo.value)
