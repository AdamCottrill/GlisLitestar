#from typing import Optional
#from dataclasses import dataclass
#
#
#@dataclass
#class FN125Lamprey:
#    prj_cd: str
#    sam: str
#    eff: str
#    spc: str
#    grp: str
#    fish: str
#    lamid: int
#    xlam: Optional[str] = None
#    lamijc_type: Optional[str] = None
#    lamijc_size: Optional[int] = None
#    comment_lam: Optional[str] = None
#
#
#@dataclass
#class FN125LampreyPartial:
#    xlam: Optional[str] = None
#    lamijc_type: Optional[str] = None
#    lamijc_size: Optional[int] = None
#    comment_lam: Optional[str] = None


from enum import Enum
from typing import Optional

from pydantic import constr, conint, model_validator, field_validator
from .FNBase import FNBase
from .utils import empty_to_none, PRJ_CD_REGEX


class LamIjcEnum(str, Enum):
    NoWound = "0"
    A1 = "A1"
    A2 = "A2"
    A3 = "A3"
    A4 = "A4"
    B1 = "B1"
    B2 = "B2"
    B3 = "B3"
    B4 = "B4"


class FN125Lamprey(FNBase):
    """Pydantic model for Lamprey wounds.

    The lamijc_pattern is a 0 OR an A or a B follwed by a number between
    1 and 4 optionally followed by two digits between 10 and 50.

    """

    prj_cd: constr(pattern=PRJ_CD_REGEX)
    sam: str
    eff: constr(pattern="^([A-Z0-9]{3})$")
    spc: constr(pattern="^([A-Z0-9]{3})$")
    grp: constr(pattern="^([A-Z0-9]{2})$")
    fish: int
    lamid: int
    xlam: Optional[constr(pattern=r"^0|\d{4}$")]
    lamijc_type: Optional[LamIjcEnum]
    lamijc_size: Optional[conint(ge=10)]
    comment_lam: Optional[str]

    # need to have either xlam or lamijc should not have both.

    _empty_to_none = field_validator(
        "xlam",
        "lamijc_type",
        "lamijc_size",
        "comment_lam",
        mode="before",
    )(empty_to_none)

    @model_validator(mode="before")
    @classmethod
    def check_xlam_or_lamijc(cls, values):
        """Make sure there is either an xlam or lamicj value defined - but not both"""

        xlam = values.get("xlam")
        lamijc_type = values.get("lamijc_type")
        if lamijc_type is None and xlam is None:
            msg = f"No wounding information found in record."
            raise ValueError(msg)
        if lamijc_type and xlam:

            msg = f"Two different wound reporting mechanisms used."
            raise ValueError(msg)
        return values
