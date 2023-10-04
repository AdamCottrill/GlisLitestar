from typing import Optional

from pydantic import PositiveFloat, confloat, constr, field_validator, ConfigDict

from .FNBase import FNBase
from .utils import string_to_float, PRJ_CD_REGEX


class FN122(FNBase):
    """ """

    prj_cd: constr(pattern=PRJ_CD_REGEX)
    sam: str
    eff: constr(pattern="^([A-Z0-9]{1,3})$")

    effdst: Optional[PositiveFloat] = None
    grdep0: Optional[PositiveFloat] = None
    grdep1: Optional[PositiveFloat] = None
    grtem0: Optional[confloat(ge=-30, le=30)] = None
    grtem1: Optional[confloat(ge=-30, le=30)] = None

    waterhaul: bool = False
    comment2: Optional[str] = None

    model_config = ConfigDict(validate_assignment=True)

    @field_validator("waterhaul", mode="before")
    def set_waterhaul(cls, waterhaul):
        return waterhaul or False

    _string_to_float = field_validator(
        "effdst", "grdep0", "grdep1", "grtem0", "grtem1", mode="before"
    )(string_to_float)
