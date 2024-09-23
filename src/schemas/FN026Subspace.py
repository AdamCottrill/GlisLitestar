from typing import Optional

from pydantic import ConfigDict, PositiveFloat, confloat, constr, field_validator

from .FNBase import FNBase
from .utils import (
    PRJ_CD_REGEX,
    not_specified,
    string_to_float,
    strip_0,
    to_titlecase,
    to_uppercase,
    yr_to_year,
)


class FN026Subspace(FNBase):
    prj_cd: constr(pattern=PRJ_CD_REGEX)
    space: constr(pattern="^([A-Z0-9]{2})$", max_length=2, to_upper=True)
    subspace: constr(pattern="^([A-Z0-9]{1,6})$", max_length=6, to_upper=True)
    subspace_des: constr(strip_whitespace=True)
    grdep_ge: Optional[confloat(ge=0)] = None
    grdep_lt: Optional[PositiveFloat] = None
    sidep_ge: Optional[confloat(ge=0)] = None
    sidep_lt: Optional[PositiveFloat] = None

    subspace_wt: Optional[confloat(gt=0, le=1)] = None

    dd_lat: Optional[confloat(ge=41.6, le=49.2)] = None
    dd_lon: Optional[confloat(ge=-89.6, le=-74.32)] = None

    model_config = ConfigDict(validate_assignment=True)

    _to_titlecase = field_validator("subspace_des", mode="before")(to_titlecase)

    _to_uppercase = field_validator("space", "subspace", mode="before")(to_uppercase)

    _strip_0 = field_validator("dd_lat", "dd_lon", mode="before")(strip_0)

    _string_to_float = field_validator(
        "grdep_ge",
        "grdep_lt",
        "sidep_ge",
        "sidep_lt",
        "subspace_wt",
        mode="before",
    )(string_to_float)

    @field_validator("dd_lon")
    def dd_lat_and_dd_lon(cls, v, values):
        dd_lat = values.data.get("dd_lat")
        if v and dd_lat:
            return v
        if v and dd_lat is None:
            raise ValueError(
                "dd_lat must be populated with a valid latitude if dd_lon is provided."
            )
        if v is None and dd_lat:
            raise ValueError(
                "dd_lon must be populated with a valid longitude if dd_lat is provided."
            )
        return v
