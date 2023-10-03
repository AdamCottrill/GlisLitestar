from enum import Enum
from typing import Optional

from pydantic import constr, conint, field_validator
from .FNBase import FNBase
from .utils import PRJ_CD_REGEX, string_to_int, empty_to_none


from .choices import AGEST_CHOICES, AGEPREP1_CHOICES, AGEPREP2_CHOICES


class EdgeEnum(str, Enum):
    omega = "o"
    asterisk = "*"
    plus = "+"
    plus_plus = "++"
    regenerated = "R"
    omega_x = "ox"
    check_zone = "x"
    omega_slash = "o/"


class AgeFailEnum(str, Enum):
    no_structure = "91"
    regenerated_crystalized = "92"
    poorly_prepared = "93"
    contaminated_sample = "94"
    poor_structure = "95"


class FN127(FNBase):
    """Pydantic model for age estimates.

    Like FN125tags - this model should be updated when we refactor the
    FN127 model into separate fields.

    """

    prj_cd: constr(pattern=PRJ_CD_REGEX)
    sam: str
    eff: constr(pattern="^([A-Z0-9]{3})$")
    spc: constr(pattern="^([A-Z0-9]{3})$")
    grp: constr(pattern="^([A-Z0-9]{2})$")
    fish: constr(max_length=6, to_upper=True, pattern=r"^[0-9A-Z]{1,6}$")
    ageid: int
    preferred: bool
    agea: Optional[conint(ge=0)] = None
    agemt: Optional[constr(pattern="^([A-Z0-9]{5})$", max_length=5)] = None
    edge: Optional[EdgeEnum] = None
    conf: Optional[conint(ge=1, le=9)] = None
    nca: Optional[conint(ge=0)] = None

    agestrm: Optional[conint(ge=0)] = None
    agelake: Optional[conint(ge=0)] = None
    spawnchkcnt: Optional[conint(ge=0)] = None
    age_fail: Optional[AgeFailEnum] = None

    comment7: Optional[str] = None

    _string_to_int = field_validator("agea", "conf", "nca", mode="before")(
        string_to_int
    )

    _empty_to_none = field_validator("edge", "age_fail", mode="before")(empty_to_none)

    @field_validator("agemt")
    def check_agemt_structure(value, values):
        if value is not None:
            structure = value[0]
            if structure not in AGEST_CHOICES:
                msg = f"Unknown aging structure ({','.join(structure)}) found in agemt ({value})"
                raise ValueError(msg)
        return value

    @field_validator("agemt")
    def check_agemt_prep1(value, values):
        if value is not None:
            prep = value[1]
            if prep not in AGEPREP1_CHOICES:
                msg = f"Unknown aging prep1 method ({','.join(prep)}) found in agemt ({value})"
                raise ValueError(msg)
        return value

    @field_validator("agemt")
    def check_agemt_prep2(value, values):
        if value is not None:
            prep = value[2]
            if prep not in AGEPREP2_CHOICES:
                msg = f"Unknown aging prep2 method ({','.join(prep)}) found in agemt ({value})"
                raise ValueError(msg)
        return value
