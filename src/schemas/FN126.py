from enum import Enum
from typing import Optional

from pydantic import PositiveInt, PositiveFloat, confloat, field_validator, constr
from .FNBase import FNBase
from .utils import (
    string_to_float,
    string_to_int,
    empty_to_none,
    PRJ_CD_REGEX,
    val_to_string,
)


class FdMesEnum(str, Enum):
    Length = "L"
    Volume = "V"
    Weight = "W"


class FN126(FNBase):
    """Pydantic model for diet data."""

    prj_cd: constr(pattern=PRJ_CD_REGEX)
    sam: str
    eff: constr(pattern="^([A-Z0-9]{1,3})$")
    spc: constr(pattern="^([A-Z0-9]{3})$")
    grp: constr(pattern="^([A-Z0-9]{2})$")
    fish: constr(max_length=6, to_upper=True, pattern=r"^[0-9A-Z]{1,6}$")
    food: int
    taxon: str
    fdcnt: Optional[confloat(ge=0)] = None
    fdmes: Optional[FdMesEnum]
    fdval: Optional[PositiveFloat]
    lifestage: Optional[PositiveInt]
    comment6: Optional[str]

    _val_to_str = field_validator("fish", mode="before")(val_to_string)
    _string_to_float = field_validator("fdval", mode="before")(string_to_float)
    _string_to_int = field_validator("lifestage", mode="before")(string_to_int)
    _empty_to_none = field_validator("fdmes", "fdcnt", mode="before")(empty_to_none)

    # fdmes and fdval should both be populated or both be null:
    @field_validator("fdval")
    def fdmes_and_fdval(cls, v, values):
        fdmes = values.data.get("fdmes")
        if v and fdmes:
            return v
        if v and fdmes is None:
            raise ValueError("fdmes must be populated if fdval is provided.")
        if v is None and fdmes:
            raise ValueError("fdval must be populated if fdmes is provided.")
