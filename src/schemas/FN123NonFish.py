from typing import Optional
from dataclasses import dataclass


@dataclass
class FN123NonFish:
    prj_cd: str
    sam: str
    eff: str
    taxon: str
    catcnt: int
    mortcnt: Optional[int] = None
    comment3: Optional[str] = None


@dataclass
class FN123NonFishPartial:
    catcnt: Optional[int] = None
    mortcnt: Optional[int] = None
    comment3: Optional[str] = None
