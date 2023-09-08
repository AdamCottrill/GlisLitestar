from dataclasses import dataclass


@dataclass
class FN122:
    prj_cd: str
    sam: str
    eff: str
    effdst: float
    grdep0: float
    grdep1: float
    grtem0: float
    grtem1: float
    waterhaul: bool
    comment2: str
