from typing import Optional
from dataclasses import dataclass


@dataclass
class FN125:
    prj_cd: str
    sam: str
    eff: str
    spc: str
    grp: str
    fish: str
    flen: Optional[int] = None
    tlen: Optional[int] = None
    girth: Optional[int] = None
    rwt: Optional[float] = None
    eviswt: Optional[int] = None
    sex: Optional[str] = None
    mat: Optional[str] = None
    gon: Optional[str] = None
    gonwt: Optional[float] = None
    clipc: Optional[str] = None
    clipa: Optional[str] = None
    nodc: Optional[str] = None
    noda: Optional[str] = None
    tissue: Optional[str] = None
    agest: Optional[str] = None
    fate: Optional[str] = None
    fdsam: Optional[str] = None
    stom_contents_wt: Optional[float] = None
    comment5: Optional[str] = None


@dataclass
class FN125Partial:
    flen: Optional[int] = None
    tlen: Optional[int] = None
    girth: Optional[int] = None
    rwt: Optional[float] = None
    eviswt: Optional[int] = None
    sex: Optional[str] = None
    mat: Optional[str] = None
    gon: Optional[str] = None
    gonwt: Optional[float] = None
    clipc: Optional[str] = None
    clipa: Optional[str] = None
    nodc: Optional[str] = None
    noda: Optional[str] = None
    tissue: Optional[str] = None
    agest: Optional[str] = None
    fate: Optional[str] = None
    fdsam: Optional[str] = None
    stom_contents_wt: Optional[float] = None
    comment5: Optional[str] = None
