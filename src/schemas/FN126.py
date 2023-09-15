from typing import Optional
from dataclasses import dataclass


@dataclass
class FN126:
    prj_cd: str
    sam: str
    eff: str
    spc: str
    grp: str
    fish: str
    food: int
    taxon: str
    fdcnt: int
    fdmes: str
    fdval: float
    lifestage: str
    comment6: str


@dataclass
class FN126Partial:
    taxon: Optional[str] = None
    fdcnt: Optional[int] = None
    fdmes: Optional[str] = None
    fdval: Optional[float] = None
    lifestage: Optional[str] = None
    comment6: Optional[str] = None
