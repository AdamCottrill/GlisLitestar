from pydantic import field_validator, constr, conint, PositiveInt, ConfigDict
from typing import Optional

from .FNBase import FNBase
from .utils import string_to_int, PRJ_CD_REGEX


class FN124(FNBase):
    """Pydanic model for length tallies."""

    prj_cd: constr(pattern=PRJ_CD_REGEX)
    sam: str
    eff: constr(pattern="^([A-Z0-9]{1,3})$")
    spc: constr(pattern="^([A-Z0-9]{3})$")
    grp: constr(pattern="^([A-Z0-9]{2})$")
    siz: conint(ge=10)
    sizcnt: PositiveInt
    comment4: Optional[str] = None

    model_config = ConfigDict(validate_assignment=True)

    _string_to_int = field_validator("siz", "sizcnt", mode="before")(string_to_int)
