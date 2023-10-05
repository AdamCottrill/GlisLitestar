from datetime import date

from pydantic import field_validator, constr, ConfigDict

from .utils import not_specified, yr_to_year, PRJ_CD_REGEX
from .FNBase import FNBase


class FN022(FNBase):
    """Scrub our seasons.  Make sure that the dates are consistent with the
    project code, ssn_date0 occurs on or before ssn_date1

        TODO: ensure that seasons do not overlap within projects.
    """

    prj_cd: constr(pattern=PRJ_CD_REGEX)
    ssn: constr(pattern="^([A-Z0-9]{2})$", max_length=2)
    ssn_des: str
    ssn_date0: date
    ssn_date1: date

    model_config = ConfigDict(validate_assignment=True)

    _not_specified = field_validator("ssn_des", mode="before")(not_specified)

    @field_validator("ssn_date0")
    def ssn_date0_matches_prj_cd(cls, v, values):
        prj_cd_yr = yr_to_year(values.data.get("prj_cd", "")[6:8])
        date_yr = str(v.year)
        if prj_cd_yr != date_yr:
            err_msg = f"""Year of start date (ssn_date0={v}) is not consistent with prj_cd ({prj_cd_yr})."""
            raise ValueError(err_msg)
        return v

    @field_validator("ssn_date1")
    def ssn_date1_matches_prj_cd(cls, v, values):
        prj_cd_yr = yr_to_year(values.data.get("prj_cd", "")[6:8])
        date_yr = str(v.year)
        if prj_cd_yr != date_yr:
            err_msg = f"""Year of end date (ssn_date1={v}) is not consistent with prj_cd ({prj_cd_yr})."""
            raise ValueError(err_msg)
        return v

    @field_validator("ssn_date1")
    def ssn_date0_before_ssn_date1(cls, v, values):
        ssn_date0 = values.data.get("ssn_date0")
        if ssn_date0:
            if ssn_date0 > v:
                raise ValueError(
                    f"Season end date (ssn_date1={v}) occurs before start date(ssn_date0={ssn_date0})."
                )
        return v
