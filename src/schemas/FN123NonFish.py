from typing import Optional

from pydantic import conint, constr, field_validator

from .FNBase import FNBase
from .utils import PRJ_CD_REGEX, string_to_int


class FN123NonFish(FNBase):
    """Pydantic model for Catch Counts of things that are not
    fish. (turtles and burds.).

    Catcnt if present must be more than 1.  If mortcnt is populated,
    it must be less than catcnt.

    """

    prj_cd: constr(pattern=PRJ_CD_REGEX)
    sam: str
    eff: constr(pattern="^([A-Z0-9]{3})$")
    taxon: constr(pattern="^([A-Z0-9]{4,20})$")

    catcnt: Optional[conint(ge=1)] = None
    mortcnt: Optional[conint(ge=0)] = None
    comment3: Optional[str] = None

    _string_to_int = field_validator("catcnt", "mortcnt", mode="before")(string_to_int)

    @field_validator("mortcnt")
    def check_catcnt_vs_mortcnt(cls, v, values):
        catcnt = values.data.get("catcnt")
        if catcnt is not None and v is not None:
            if catcnt < v:
                msg = f"MORTCNT ({v}) cannot be greater than CATCNT ({catcnt})"
                raise ValueError(msg)
        return v
