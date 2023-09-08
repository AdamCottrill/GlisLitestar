from dataclasses import dataclass


@dataclass
class FN012:
    prj_cd: str
    spc: str
    spc_nmco: str
    grp: str
    grp_des: str
    sizsam: str
    sizatt: str
    sizint: int
    biosam: str
    fdsam: str
    spcmrk: str
    tissue: str
    agest: str
    lamsam: str
    flen_min: float
    flen_max: float
    tlen_min: float
    tlen_max: float
    rwt_min: float
    rwt_max: float
    k_min_error: float
    k_min_warn: float
    k_max_error: float
    k_max_warn: float
