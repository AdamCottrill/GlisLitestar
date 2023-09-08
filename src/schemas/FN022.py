from dataclasses import dataclass
from datetime import date


@dataclass
class FN022:
    prj_cd: str
    ssn: str
    ssn_des: str
    ssn_date0: date
    ssn_date1: date
