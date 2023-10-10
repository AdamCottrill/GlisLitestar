from datetime import date, time
from enum import IntEnum, Enum
from typing import Optional

from pydantic import PositiveFloat, confloat, constr, conint, field_validator

from .FNBase import FNBase
from .utils import (
    string_to_float,
    string_to_int,
    strip_0,
    strip_date,
    yr_to_year,
    to_string,
    ProcessTypeEnum,
    PRJ_CD_REGEX,
)

xwind_regex = r"^000|\d{3}-\d{1,2}$"
xweather_regex = r"^[1-4]{2}$"


class PrecipEnum(str, Enum):
    none = "00"
    mist = "10"
    fog = "40"
    slight_drizzle = "51"
    heavy_drizzle = "55"
    light_rain = "61"
    heavy_rain = "65"
    light_snow = "71"
    heavy_snow = "75"
    light_rain_shower = "80"
    heavy_rain_shower = "85"
    thunder_storm = "95"


class VesselDirectionEnum(IntEnum):
    variable = 0
    northeast = 1
    east = 2
    southeast = 3
    south = 4
    southwest = 5
    west = 6
    northwest = 7
    north = 8
    not_definable = 9


class EffstEnum(str, Enum):
    valid = "1"
    potential = "5"
    invalid = "9"


class XslimeEnum(IntEnum):
    none = 0
    present = 1
    light = 2
    moderate = 3
    heavy = 4
    very_heavy = 5


class VegetationEnum(IntEnum):
    none = 1
    sparse = 2
    moderate = 3
    dense = 4


class BottomTypeEnum(str, Enum):
    boulder = "BO"
    bedrock_or_rock = "BR"
    clay = "CL"
    vetritus = "DE"
    gravel_pebble = "GP"
    marl = "MA"
    muck = "MU"
    rubble_cobble = "RC"
    sand = "SA"
    silt = "SI"


class CoverTypeEnum(str, Enum):
    boulder = "BO"
    combination = "CO"
    log_tree = "LT"
    macrophytes = "MA"
    no_cover = "NC"
    organic_debris = "OD"
    other = "OT"
    undercut_bank = "UB"


# TODO:
# BottomTypeChoice = Enum("BottomTypeChoice", bottom_type_choices)
# CoverTypeChoice = Enum("CoverTypeChoice", cover_type_choices)


class FN121(FNBase):
    """parser/field_validator for FN011 objects:

    + Valid project code.
    + Year must be consistent with project code
    + slug is lowercase prj_cd
    + effdt0 must be constistent with prj_cd
    + effdt1 must be constistent with prj_cd and occur on or after effdt0

    """

    prj_cd: constr(pattern=PRJ_CD_REGEX)
    sam: str
    process_type: ProcessTypeEnum = ProcessTypeEnum.by_sample

    ssn: constr(pattern="^([A-Z0-9]{2})$")
    subspace: constr(pattern="^([A-Z0-9]{2,6})$")
    mode: constr(pattern="^([A-Z0-9]{2})$")
    effdt0: Optional[date] = None
    efftm0: Optional[time] = None
    effdt1: Optional[date] = None
    efftm1: Optional[time] = None
    effdur: Optional[PositiveFloat] = None

    effst: Optional[EffstEnum] = None

    # stratum: Optional[str]
    # area: Optional[str]
    sitp: Optional[str] = None
    # site: Optional[str] = None

    dd_lat0: Optional[confloat(ge=41.6, le=49.2)] = None
    dd_lon0: Optional[confloat(ge=-89.6, le=-74.32)] = None

    dd_lat1: Optional[confloat(ge=41.6, le=49.2)] = None
    dd_lon1: Optional[confloat(ge=-89.6, le=-74.32)] = None

    grid5: constr(pattern="^([0-9]{4})$")

    sitem0: Optional[confloat(ge=-30, le=30)] = None
    sitem1: Optional[confloat(ge=-30, le=30)] = None

    sidep0: Optional[PositiveFloat] = None
    sidep1: Optional[PositiveFloat] = None
    # grdep: Union[None, PositiveFloat, EmptyStrToNone]
    grdepmin: Optional[confloat(ge=0)] = None
    grdepmax: Optional[PositiveFloat] = None
    grdepmid: Optional[PositiveFloat] = None

    secchi0: Optional[PositiveFloat] = None
    secchi1: Optional[PositiveFloat] = None
    slime: Optional[XslimeEnum] = None

    crew: Optional[str] = None

    comment1: Optional[str] = None

    # vessel fields TODO: vessel_id
    vessel: Optional[str] = None
    vessel_speed: Optional[confloat(ge=0, le=10)] = None
    vessel_direction: Optional[VesselDirectionEnum] = None
    warp: Optional[confloat(gt=0)] = None

    bottom: Optional[BottomTypeEnum] = None
    cover: Optional[CoverTypeEnum] = None

    vegetation: Optional[VegetationEnum] = None
    lead_angle: Optional[conint(ge=0, le=90)] = None
    leaduse: Optional[confloat(ge=0)] = None
    distoff: Optional[confloat(ge=0)] = None

    o2gr0: Optional[confloat(ge=0, le=15)] = None
    o2gr1: Optional[confloat(ge=0, le=15)] = None
    o2bot0: Optional[confloat(ge=0, le=15)] = None
    o2bot1: Optional[confloat(ge=0, le=15)] = None
    o2surf0: Optional[confloat(ge=0, le=15)] = None
    o2surf1: Optional[confloat(ge=0, le=15)] = None

    airtem0: Optional[confloat(ge=-30, le=45)] = None
    airtem1: Optional[confloat(ge=-30, le=45)] = None
    cloud_pc0: Optional[conint(ge=0, le=100)] = None
    cloud_pc1: Optional[conint(ge=0, le=100)] = None
    waveht0: Optional[confloat(ge=0, le=3.5)] = None
    waveht1: Optional[confloat(ge=0, le=3.5)] = None

    # precip enum
    precip0: Optional[PrecipEnum] = None
    precip1: Optional[PrecipEnum] = None

    # XWIND_REGEX
    wind0: Optional[constr(pattern=xwind_regex)] = None
    wind1: Optional[constr(pattern=xwind_regex)] = None

    # XWEATHER_REGEX
    xweather: Optional[constr(pattern=xweather_regex)] = None

    _string_to_float = field_validator(
        "dd_lat0",
        "dd_lon0",
        "dd_lat1",
        "dd_lon1",
        "sidep0",
        "sidep1",
        "effdur",
        "grdepmin",
        "grdepmid",
        "grdepmax",
        "secchi0",
        "secchi1",
        "sitem0",
        "sitem1",
        "vessel_speed",
        "warp",
        "lead_angle",
        "leaduse",
        "distoff",
        "o2gr0",
        "o2gr1",
        "o2bot0",
        "o2bot1",
        "o2surf0",
        "o2surf1",
        "airtem0",
        "airtem1",
        "cloud_pc0",
        "cloud_pc1",
        "waveht0",
        "waveht1",
        mode="before",
    )(string_to_float)

    _strip_0 = field_validator(
        "dd_lat0", "dd_lon0", "dd_lat1", "dd_lon1", mode="before"
    )(strip_0)

    _to_string = field_validator("effst", mode="before")(to_string)

    _strip_date = field_validator("efftm0", "efftm1", mode="before")(strip_date)

    _string_to_int = field_validator("vessel_direction", "vegetation", mode="before")(
        string_to_int
    )

    # _check_vessel = check_choices("vessel_id", VesselChoice, "Vessel")
    # _check_cover = check_choices("cover_id", CoverTypeChoice, "Cover")
    # _check_bottom = check_choices("bottom_id", BottomTypeChoice, "Bottom")

    @field_validator("effdt0", "effdt1")
    def date_matches_prj_cd(cls, v, values):
        if v:
            prj_cd_yr = yr_to_year(values.data.get("prj_cd", "")[6:8])
            date_yr = str(v.year)
            if prj_cd_yr != date_yr:
                err_msg = f"""Set or Lift Date ({v}) is not consistent with prj_cd ({prj_cd_yr})."""
                raise ValueError(err_msg)
        return v

    @field_validator("effdt1")
    def effdt0_before_effdt1(cls, v, values):
        effdt0 = values.data.get("effdt0")
        if v and effdt0:
            if effdt0 > v:
                raise ValueError(
                    f"Lift date (effdt1={v}) occurs before set date(effdt0={effdt0})."
                )
        return v

    @field_validator("grdepmax")
    def grdepmin_lte_grdepmax(cls, v, values):
        grdepmin = values.data.get("grdepmin")
        if v and grdepmin:
            if v < grdepmin:
                raise ValueError(
                    f"grdepmax ({v} m) must be greater than or equal to grdepmin ({grdepmin} m)."
                )
        return v

    @field_validator("grdepmid")
    def grdepmid_gte_grdepmin(cls, v, values):
        """contraint to ensure mid<=max removed"""
        grdepmin = values.data.get("grdepmin")
        if v and grdepmin:
            if v < grdepmin:
                raise ValueError(
                    f"grdepmid ({v} m) must be greater than or equal to grdepmin ({grdepmin} m)."
                )
        return v

    @field_validator("dd_lon0")
    def dd_lat0_and_dd_lon0(cls, v, values):
        dd_lat0 = values.data.get("dd_lat0")
        if v and dd_lat0:
            return v
        if v and dd_lat0 is None:
            raise ValueError(
                "dd_lat0 must be populated with a valid latitude if dd_lon0 is provided."
            )
        if v is None and dd_lat0:
            raise ValueError(
                "dd_lon0 must be populated with a valid longitude if dd_lat0 is provided."
            )
        return v

    @field_validator("dd_lon1")
    def dd_lat1_and_dd_lon1(cls, v, values):
        dd_lat0 = values.data.get("dd_lat1")
        if v and dd_lat0:
            return v
        if v and dd_lat0 is None:
            raise ValueError(
                "dd_lat1 must be populated with a valid latitude if dd_lon1 is provided."
            )
        if v is None and dd_lat0:
            raise ValueError(
                "dd_lon1 must be populated with a valid longitude if dd_lat1 is provided."
            )
        return v

    @field_validator("process_type", mode="before")
    def set_processs_type(processs_type):
        if processs_type:
            return processs_type
        else:
            return ProcessTypeEnum.by_sample

    @field_validator("wind0", "wind1")
    @classmethod
    def check_wind(cls, value, values):
        """wind must be 000 or a compound string"""

        if value == "000" or value is None:
            return value

        if value == "000-00":
            return "000"
        # split on the dash
        try:
            direction, speed = value.split("-")
            direction_int = int(direction)
            speed_int = int(speed)
        except:
            msg = f"{value} in not a valid wind speed and direction string."
            raise ValueError(msg)
        if direction_int < 1 or direction_int > 360:
            msg = "Direction must be an integer between 1 and 360."
            raise ValueError(msg)
        if speed_int < 1 or speed_int > 99:
            msg = "Speed must be an integer between 1 and 99."
            raise ValueError(msg)
        return value
