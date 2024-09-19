from typing import Optional, List
from pydantic import field_validator
from datetime import datetime
from enum import Enum


PRJ_CD_REGEX = r"[A-Z0-9]{3}_[A-Z]{2}\d{2}_[A-Z0-9]{3}"


class ProcessTypeEnum(str, Enum):
    by_sample = "1"
    by_mesh_size = "2"
    by_panel_group = "3"
    by_panel = "4"
    other = "5"


def string_to_float(v) -> Optional[float]:
    """A validator that will convert floats passed in as strings to a
    python float."""

    if v is None:
        return v
    else:
        try:
            val = float(v)
        except ValueError:
            val = None
    return val


def string_to_int(v) -> Optional[int]:
    """A validator that will convert floats passed in as strings to a
    python integer"""

    if v is None:
        return v
    else:
        try:
            val = int(v)
        except ValueError:
            val = None
    return val


def to_string(v) -> Optional[str]:
    if v is None:
        return v
    else:
        try:
            val = str(v)
        except ValueError:
            val = None
    return val


def val_to_string(v) -> Optional[str]:
    """A validator that will convert integers passed in as strings to a
    python string."""

    if v is None:
        return v
    else:
        try:
            val = str(v)
        except ValueError:
            val = None
    return val


def empty_to_none(v: str) -> Optional[str]:
    if v == "":
        return None
    return v


def yr_to_year(yr):
    if int(yr) < 50:
        return f"20{yr}"
    else:
        return f"19{yr}"


def strip_0(val):
    """Lat lon can be null, but they cannot be 0."""
    if val == 0 or val == "0" or val == "":
        return None
    return val


def strip_date(value):
    """pyodbc treats times as datetimes. we need to strip the date off if
    it is there."""

    if value == "":
        return None
    if isinstance(value, datetime):
        return value.time()
    return value


def check_ascii_sort(value: str) -> Optional[str]:
    if value is not None:
        val = list(set(value))
        val.sort()
        val = "".join(val)
        if val != value:
            msg = f"Found non-unique or non-ascii sorted value '{value}' (it should be: {val})"
            raise ValueError(msg)
    return value


def check_agest_values(value: str, allowed: str) -> Optional[str]:
    if value is not None:
        if "0" in value and len(value) > 1:
            msg = f"Invalid AGEST. '0' cannot be used in combination with other structures."
            raise ValueError(msg)

        unknown = [c for c in value if c not in allowed]
        if unknown:
            msg = f"Unknown aging structures ({','.join(unknown)}) found in AGEST ({value})"
            raise ValueError(msg)
        return value



def check_agest(field_name: str, allowed: List[str]):
    return field_validator(field_name)(
        lambda v: check_agest_values(v, "".join(allowed))
    )


def check_tissue_values(value: str, allowed: str) -> Optional[str]:
    if value is not None:
        unknown = [c for c in value if c not in allowed]
        if unknown:
            msg = f"Unknown tissue type ({','.join(unknown)}) found in TISSUE ({value})"
            raise ValueError(msg)
        return value


def check_tissue(field_name: str, allowed: List[str]):
    return field_validator(field_name)(
        lambda v: check_tissue_values(v, "".join(allowed))
    )


def to_uppercase(value: str) -> str:
    if hasattr(value, "upper"):
        return value.upper()
    else:
        return value

def to_titlecase(value: str) -> str:
    if hasattr(value, "title"):
        return value.title().replace("'S ","'s ")
    else:
        return value


def not_specified(value: str) -> str:
    if value:
        return value.title()
    else:
        return "Not Specified"
