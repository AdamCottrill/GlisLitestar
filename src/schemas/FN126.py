from enum import Enum
from typing import Optional

from pydantic import PositiveInt, PositiveFloat, confloat, field_validator, constr
from .FNBase import FNBase
from .utils import string_to_float, string_to_int, empty_to_none, PRJ_CD_REGEX


class FdMesEnum(str, Enum):
    Length = "L"
    Volume = "V"
    Weight = "W"


class FN126(FNBase):
    """Pydantic model for diet data."""

    prj_cd: constr(pattern=PRJ_CD_REGEX)
    sam: str
    eff: constr(pattern="^([A-Z0-9]{3})$")
    spc: constr(pattern="^([A-Z0-9]{3})$")
    grp: constr(pattern="^([A-Z0-9]{2})$")
    fish: str
    food: int
    taxon: str
    fdcnt: confloat(ge=0) = 0
    fdmes: Optional[FdMesEnum]
    fdval: Optional[PositiveFloat]
    lifestage: Optional[PositiveInt]
    comment6: Optional[str]

    _string_to_float = field_validator("fdval", mode="before")(string_to_float)
    _string_to_int = field_validator("lifestage", mode="before")(string_to_int)
    _empty_to_none = field_validator("fdmes", mode="before")(empty_to_none)
