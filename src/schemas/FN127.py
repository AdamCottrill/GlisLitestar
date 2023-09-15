from dataclasses import dataclass
from typing import Optional


@dataclass
class FN127:
    prj_cd: str
    sam: str
    eff: str
    spc: str
    grp: str
    fish: str
    ageid: int
    preferred: bool
    agea: int
    agemt: str
    edge: str
    conf: int
    nca: int
    agestrm: int
    agelake: int
    spawnchkcnt: int
    age_fail: str
    comment7: str


@dataclass
class FN127Partial:
    preferred: Optional[bool] = None
    agea: Optional[int] = None
    agemt: Optional[str] = None
    edge: Optional[str] = None
    conf: Optional[int] = None
    nca: Optional[int] = None
    agestrm: Optional[int] = None
    agelake: Optional[int] = None
    spawnchkcnt: Optional[int] = None
    age_fail: Optional[str] = None
    comment7: Optional[str] = None
