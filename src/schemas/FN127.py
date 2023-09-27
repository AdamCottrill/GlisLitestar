# from dataclasses import dataclass
# from typing import Optional


# @dataclass
# class FN127:
#     prj_cd: str
#     sam: str
#     eff: str
#     spc: str
#     grp: str
#     fish: str
#     ageid: int
#     preferred: bool
#     agea: Optional[int] = None
#     agemt: Optional[str] = None
#     edge: Optional[str] = None
#     conf: Optional[int] = None
#     nca: Optional[int] = None
#     agestrm: Optional[int] = None
#     agelake: Optional[int] = None
#     spawnchkcnt: Optional[int] = None
#     age_fail: Optional[str] = None
#     comment7: Optional[str] = None


# @dataclass
# class FN127Partial:
#     preferred: Optional[bool] = None
#     agea: Optional[int] = None
#     agemt: Optional[str] = None
#     edge: Optional[str] = None
#     conf: Optional[int] = None
#     nca: Optional[int] = None
#     agestrm: Optional[int] = None
#     agelake: Optional[int] = None
#     spawnchkcnt: Optional[int] = None
#     age_fail: Optional[str] = None
#     comment7: Optional[str] = None


from enum import Enum
from typing import Optional

from pydantic import constr, conint, validator
from .FNBase import FNBase
from .utils import string_to_int, empty_to_none


AGEST_CHOICES = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "M",
    "T",
    "V",
    "X",
]
AGEPREP1_CHOICES = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "C", "K", "T"]
AGEPREP2_CHOICES = ["1", "2", "3", "4", "9"]


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

    prj_cd: str
    sam: str
    eff: str
    spc: str
    grp: str
    fish: str
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

    _string_to_int = validator("agea", "conf", "nca", allow_reuse=True, pre=True)(
        string_to_int
    )

    _empty_to_none = validator("edge", "age_fail", allow_reuse=True, pre=True)(
        empty_to_none
    )

    @validator("agemt", allow_reuse=True)
    @classmethod
    def check_agemt_structure(cls, value, values):
        if value is not None:
            structure = value[0]
            if structure not in AGEST_CHOICES:
                msg = f"Unknown aging structure ({','.join(structure)}) found in agemt ({value})"
                raise ValueError(msg)
        return value

    @validator("agemt", allow_reuse=True)
    @classmethod
    def check_agemt_prep1(cls, value, values):
        if value is not None:
            prep = value[1]
            if prep not in AGEPREP1_CHOICES:
                msg = f"Unknown aging prep1 method ({','.join(prep)}) found in agemt ({value})"
                raise ValueError(msg)
        return value

    @validator("agemt", allow_reuse=True)
    @classmethod
    def check_agemt_prep2(cls, value, values):
        if value is not None:
            prep = value[2]
            if prep not in AGEPREP2_CHOICES:
                msg = f"Unknown aging prep2 method ({','.join(prep)}) found in agemt ({value})"
                raise ValueError(msg)
        return value
