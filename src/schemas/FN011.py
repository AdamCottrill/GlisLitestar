from datetime import date
from typing import Optional

from enum import Enum

from pydantic import field_validator, constr, ConfigDict

from .utils import to_titlecase, yr_to_year

from .FNBase import FNBase, prj_cd_regex


class LakeEnum(str, Enum):
    erie = "ER"
    huron = "HU"
    ontario = "ON"
    superior = "SU"
    st_clair = "SU"


class FN011(FNBase):
    """parser/validator for FN011 objects:

    + Valid project code.
    + Year must be consistent with project code
    + slug is lowercase prj_cd
    + prj_date0 must be constistent with prj_cd
    + prj_date1 must be constistent with prj_cd and occur on or after prj_date0

    """
    lake: LakeEnum = "HU"

    prj_cd: constr(pattern=prj_cd_regex, to_upper=True)
    year: int
    prj_nm: str
    prj_date0: date
    prj_date1: date
    comment0: Optional[str]
    protocol: str
    prj_ldr: str

    _prj_nm_titlecase = field_validator("prj_nm", )(to_titlecase)

    model_config = ConfigDict(validate_assignment=True)

    @field_validator("year")
    def check_year_with_prj_cd(cls, v, values):
        prj_cd = values.data.get("prj_cd")
        if prj_cd:
            prj_cd_yr = yr_to_year(prj_cd[6:8])
            if int(prj_cd_yr) != v:
                err_msg = (
                    f"{prj_cd}: Year ({v}) is not consistent with "
                    + f"prj_cd year ({prj_cd_yr})."
                )
                raise ValueError(err_msg)
        return v

    @field_validator("prj_date0")
    @classmethod
    def prj_date0_matches_prj_cd(cls, v, values):
        prj_cd = values.data.get("prj_cd")
        if prj_cd:
            prj_cd_yr = yr_to_year(prj_cd[6:8])
            date_yr = str(v.year)
            if prj_cd_yr != date_yr:
                err_msg = (
                    f"{prj_cd}: Year of start date (prj_date0={v}) is "
                    + f"not consistent with prj_cd ({prj_cd_yr})."
                )
                raise ValueError(err_msg)
        return v

    @field_validator("prj_date1")
    def prj_date0_before_prj_date1(cls, v, values):
        prj_date0 = values.data.get("prj_date0")
        if prj_date0:
            if prj_date0 > v:
                raise ValueError(
                    "Project end date (prj_date1) occurs before start date(prj_date0)."
                )
        return v

    @field_validator("prj_date1")
    @classmethod
    def prj_date1_matches_prj_cd(cls, v, values):
        prj_cd = values.data.get("prj_cd")
        if prj_cd:
            prj_cd_yr = yr_to_year(values.data.get("prj_cd", "")[6:8])
            date_yr = str(v.year)
            if prj_cd_yr != date_yr:
                err_msg = f"""{prj_cd}: Year of end date (prj_date1={v}) is not consistent with prj_cd ({prj_cd_yr})."""
                raise ValueError(err_msg)
        return v
