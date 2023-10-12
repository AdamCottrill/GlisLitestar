from datetime import datetime
from typing import Optional

from pydantic import ConfigDict, confloat, conint, constr, field_validator

from .FNBase import FNBase
from .utils import PRJ_CD_REGEX, string_to_float, string_to_int


class FN121GpsTrack(FNBase):
    """A pydandic schema model to validate FN121GpsTrack objects.
    slug and sample_id are required, the other fields represent
    gps track points. They can be null, but must be
    constrained to plausible values.

    """

    prj_cd: constr(pattern=PRJ_CD_REGEX)
    sam: str
    trackid: conint(gt=0)

    dd_lat: confloat(ge=41.7, le=49.2)
    dd_lon: confloat(ge=-89.6, le=-76.4)
    sidep: Optional[confloat(ge=0, le=400)] = None
    timestamp: Optional[datetime] = None
    comment: Optional[str] = None

    model_config = ConfigDict(validate_assignment=True)

    _string_to_float = field_validator(
        "dd_lat",
        "dd_lon",
        "sidep",
        mode="before",
    )(string_to_float)

    _string_to_int = field_validator("trackid", mode="before")(string_to_int)
