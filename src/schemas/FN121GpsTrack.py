from dataclasses import dataclass
from datetime import datetime


@dataclass
class FN121GpsTrack:
    prj_cd: str
    sam: str
    trackid: str
    dd_lon: str
    dd_lat: str
    timestamp: datetime
    sidep: str
