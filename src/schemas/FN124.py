from typing import Optional
from dataclasses import dataclass


@dataclass
class FN124:
    prj_cd: str
    sam: str
    eff: str
    spc: str
    grp: str
    siz: str
    sizcnt: int
    comment4: Optional[str] = None


@dataclass
class FN124Partial:
    sizcnt: Optional[int] = None
    comment4: Optional[str] = None
