from typing import Optional
from dataclasses import dataclass


@dataclass
class FN125Lamprey:
    prj_cd: str
    sam: str
    eff: str
    spc: str
    grp: str
    fish: str
    lamid: int
    xlam: Optional[str] = None
    lamijc_type: Optional[str] = None
    lamijc_size: Optional[int] = None
    comment_lam: Optional[str] = None


@dataclass
class FN125LampreyPartial:
    xlam: Optional[str] = None
    lamijc_type: Optional[str] = None
    lamijc_size: Optional[int] = None
    comment_lam: Optional[str] = None
