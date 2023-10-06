from datetime import datetime, time
from enum import Enum, IntEnum
from typing import Optional

from pydantic import PositiveFloat, constr, field_validator, ConfigDict

from .FNBase import FNBase
from .utils import not_specified, string_to_float, int_to_string, PRJ_CD_REGEX

# orient_choices, gruse_choices

# GrUseEnum = Enum("GrUseEnum", gruse_choices)
# OrientEnum = Enum("OrientEnum", orient_choices)


class GrUseEnum(IntEnum):
    bottom = 1
    canned_gillnet = 2
    kyted_gillnet = 3
    midwater_trawl = 4
    surface_trawl = 5
    transect_sample = 6
    spot_point_sample = 7
    unknown = 9


class OrientEnum(Enum):
    perpendicular = "1"
    parallel = "2"
    other = "3"
    unknown = "9"
    downstream = "d"
    upstream = "u"


class FN028(FNBase):
    prj_cd: constr(pattern=PRJ_CD_REGEX)
    mode: constr(pattern="^([A-Z0-9]{2})$", max_length=2)
    mode_des: Optional[str] = "Not Specified"
    gr: constr(pattern="^([A-Z0-9]{2,5})$", max_length=5)

    gruse: GrUseEnum
    orient: OrientEnum
    effdur_ge: Optional[PositiveFloat] = None
    effdur_lt: Optional[PositiveFloat] = None

    efftm0_lt: Optional[time] = None
    efftm0_ge: Optional[time] = None

    model_config = ConfigDict(validate_assignment=True)

    _int_to_string = field_validator("gruse", mode="before")(int_to_string)
    _to_titlecase = field_validator("mode_des", mode="before")(not_specified)

    _string_to_float = field_validator("effdur_ge", "effdur_lt", mode="before")(
        string_to_float
    )

    @field_validator("efftm0_ge", "efftm0_lt", mode="before")
    def strip_date(cls, v):
        """pyodbc treats times as datetimes. we need to strip the date off if
        it is there."""
        if isinstance(v, datetime):
            return v.time()
        return v

    @field_validator("efftm0_ge")
    def efftm0_ge_greater_than_efftm0_lt(cls, v, values, **kwargs):
        tm0_lt = values.data.get("efftm0_lt")
        if v and tm0_lt:
            if v > tm0_lt:
                err_msg = f"Latest set time (efftm0_lt={tm0_lt}) is earlier than earliest set time(efftm0_ge={v})"
                raise ValueError(err_msg)
        return v
