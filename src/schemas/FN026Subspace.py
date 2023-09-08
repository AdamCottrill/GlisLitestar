from dataclasses import dataclass


@dataclass
class FN026Subspace:
    prj_cd: str
    space: str
    subspace: str
    subspace_des: str
    dd_lat: float
    dd_lon: float
    sidep_lt: float
    sidep_ge: float
    grdep_lt: float
    grdep_ge: float
    subspace_wt: float
