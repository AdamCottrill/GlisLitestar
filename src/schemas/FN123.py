from typing import Optional
from dataclasses import dataclass


@dataclass
class FN123:
    prj_cd: str
    sam: str
    eff: str
    spc: str
    grp: str
    catcnt: int
    biocnt: int
    catwt: Optional[float] = None
    subcnt: Optional[int] = None
    subwt: Optional[float] = None
    comment3: Optional[str] = None


@dataclass
class FN123Partial:
    catcnt: Optional[int] = None
    biocnt: Optional[int] = None
    catwt: Optional[float] = None
    subcnt: Optional[int] = None
    subwt: Optional[float] = None
    comment3: Optional[str] = None
