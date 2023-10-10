from typing import Optional

from pydantic import confloat, conint, constr, field_validator

from .FNBase import FNBase
from .utils import PRJ_CD_REGEX, empty_to_none, string_to_float, string_to_int


class StreamDimension(FNBase):
    prj_cd: constr(pattern=PRJ_CD_REGEX)
    subspace: constr(pattern="^([A-Z0-9]{1,6})$")
    metres_up: conint(ge=0, le=1100)
    metres_across: Optional[confloat(ge=0, le=200)] = None
    width: Optional[confloat(ge=0, le=200)] = None
    depth: Optional[confloat(ge=0, le=10)] = None
    velocity: Optional[confloat(ge=0, le=5)] = None
    comment: Optional[constr(strip_whitespace=True)] = None

    _string_to_int = field_validator("metres_up", mode="before")(string_to_int)

    _empty_to_none = field_validator("comment", mode="before")(empty_to_none)

    class Config:
        validate_assignment = True

    _string_to_float = field_validator(
        "metres_across",
        "width",
        "depth",
        "velocity",
        mode="before",
    )(string_to_float)

    @field_validator("width")
    def check_width_vs_metres_across(cls, v, values):
        metres_across = values.data.get("metres_across")
        if v and metres_across:
            if v < metres_across:
                raise ValueError(
                    f"width ({v}) cannot be less than metres_across ({metres_across})"
                )
        return v
