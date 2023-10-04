from typing import Optional

from pydantic import constr, conint, confloat, field_validator
from .FNBase import FNBase
from .utils import string_to_int, string_to_float, PRJ_CD_REGEX


class FN123(FNBase):
    """Pydantic model for FN123  - Catch Counts.

    slug, effort_id, and species_id are all required fields.  All
    other fields are currently optional. If catcnt is populated, it
    must be larger than both biocnt and subcnt.  If catwt is
    populated, it must be greater than subwt.

    """

    prj_cd: constr(pattern=PRJ_CD_REGEX)
    sam: str
    eff: constr(pattern="^([A-Z0-9]{1,3})$")
    spc: constr(pattern="^([A-Z0-9]{3})$")
    grp: constr(pattern="^([A-Z0-9]{2})$")

    catcnt: Optional[conint(ge=0)] = None
    biocnt: Optional[conint(ge=0)] = 0
    catwt: Optional[confloat(ge=0)] = None
    subcnt: Optional[conint(ge=0)] = None
    subwt: Optional[confloat(ge=0)] = None
    comment3: Optional[str] = None

    _string_to_float = field_validator("catwt", "subwt", mode="before")(string_to_float)

    _string_to_int = field_validator("catcnt", "subcnt", "biocnt", mode="before")(
        string_to_int
    )

    @field_validator("biocnt")
    def check_catcnt_vs_biocnt(cls, v, values):
        catcnt = values.data.get("catcnt")
        if catcnt is not None and v is not None:
            if catcnt < v:
                msg = f"BIOCNT ({v}) cannot be greater than CATCNT ({catcnt})"
                raise ValueError(msg)
        return v

    @field_validator("subcnt")
    def check_catcnt_vs_subcnt(cls, v, values):
        catcnt = values.data.get("catcnt")
        if catcnt is not None and v is not None:
            if catcnt < v:
                msg = f"SUBCNT ({v}) cannot be greater than CATCNT ({catcnt})"
                raise ValueError(msg)
        return v

    @field_validator("subwt")
    def check_catwt_vs_subwt(cls, v, values):
        catwt = values.data.get("catwt")
        if catwt is not None and v is not None:
            if catwt < v:
                msg = f"SUBWT ({v}) cannot be greater than CATWT ({catwt})"
                raise ValueError(msg)
        return v
