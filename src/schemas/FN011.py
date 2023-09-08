from dataclasses import dataclass
from datetime import date, time


@dataclass
class FN011:
    prj_cd: str
    prj_nm: str
    prj_ldr: str
    prj_date0: date
    prj_date1: date
    comment0: str
    protocol: str
    lake: str
