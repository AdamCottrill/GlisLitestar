from dataclasses import dataclass
from datetime import time


@dataclass
class FN028:
    prj_cd: str
    mode: str
    mode_des: str
    gr: str
    gruse: str
    orient: str
    effdur_ge: str
    effdur_lt: str
    efftm0_ge: time
    efftm0_lt: time
