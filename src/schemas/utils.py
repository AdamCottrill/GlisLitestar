from typing import Optional


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


def empty_to_none(v: str) -> Optional[str]:
    if v == "":
        return None
    return v
