from dataclasses import dataclass


@dataclass
class FN026:
    prj_cd: str
    space: str
    space_des: str
    dd_lat: float
    dd_lon: float
    sidep_lt: float
    sidep_ge: float
    grdep_lt: float
    grdep_ge: float
    space_wt: float
