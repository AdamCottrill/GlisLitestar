from typing import Optional
from dataclasses import dataclass


@dataclass
class FN122:
    prj_cd: str
    sam: str
    eff: str
    effdst: Optional[float] = None
    grdep0: Optional[float] = None
    grdep1: Optional[float] = None
    grtem0: Optional[float] = None
    grtem1: Optional[float] = None
    waterhaul: Optional[bool] = None
    comment2: Optional[str] = None


@dataclass
class FN122Partial:
    effdst: Optional[float] = None
    grdep0: Optional[float] = None
    grdep1: Optional[float] = None
    grtem0: Optional[float] = None
    grtem1: Optional[float] = None
    waterhaul: Optional[bool] = None
    comment2: Optional[str] = None
