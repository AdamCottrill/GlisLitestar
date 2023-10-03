from enum import Enum, IntEnum
from typing import Optional

from pydantic import ConfigDict, confloat, conint, constr, field_validator


from .choices import AGEST_CHOICES, CLIP_CHOICES, TISSUE_CHOICES
from .FNBase import FNBase
from .utils import (
    PRJ_CD_REGEX,
    check_agest,
    check_ascii_sort,
    check_tissue,
    string_to_float,
    string_to_int,
    to_uppercase,
    val_to_string,
)

# strip out 0 from our choices - 0 is exclusive of all other choices
AGEST_REGEX = f"^(0|[{''.join([x for x in AGEST_CHOICES if x !='0'])}]+)$"
TISSUE_REGEX = f"^(0|[{''.join([x for x in TISSUE_CHOICES if x !='0'])}]+)$"


class FateEnum(str, Enum):
    killed = "K"
    released = "R"


class SexEnum(IntEnum):
    male = 1
    female = 2
    hermaphrodite = 3
    unknown = 9


class MatEnum(IntEnum):
    immature = 1
    mature = 2
    unknown = 9


class FdsamEnum(str, Enum):
    not_collected = "0"
    fn126_records = "1"
    external_database = "2"


# see the data dictionary for valid goncodes
gon_regex = r"^[1-4|9]$|^((99|([1-5]0)|(2[1-3]))[2-8A-E]?)$"


class FN125(FNBase):
    """Pydanic model for bioligical samples.

    most of the fieds in a biological sample are optional, but if they
    are provided, they are subject to constraints.

    """

    prj_cd: constr(pattern=PRJ_CD_REGEX)
    sam: str
    eff: constr(pattern="^([A-Z0-9]{3})$")
    spc: constr(pattern="^([A-Z0-9]{3})$")
    grp: constr(pattern="^([A-Z0-9]{2})$")

    fish: constr(max_length=6, to_upper=True, pattern=r"^[0-9A-Z]{1,6}$")
    rwt: Optional[confloat(gt=0)] = None
    eviswt: Optional[confloat(gt=0)] = None
    flen: Optional[conint(gt=0)] = None
    tlen: Optional[conint(gt=0)] = None
    girth: Optional[conint(gt=0)] = None
    sex: Optional[SexEnum]
    mat: Optional[MatEnum]
    gon: Optional[constr(pattern=gon_regex)]
    gonwt: Optional[confloat(gt=0)] = None
    clipc: Optional[str]
    clipa: Optional[str]
    nodc: Optional[str]
    noda: Optional[str]
    tissue: Optional[str]

    agest: Optional[constr(max_length=8)]
    tissue: Optional[constr(max_length=8)]

    fate: FateEnum = FateEnum.killed
    stom_contents_wt: Optional[confloat(ge=0)] = None
    fdsam: Optional[FdsamEnum]

    comment5: Optional[str]

    model_config = ConfigDict(validate_assignment=True)

    _val_to_string = field_validator("fish", mode="before")(val_to_string)

    _to_uppercase = field_validator(
        "fish", "agest", "tissue", "clipc", "clipa", mode="before"
    )(to_uppercase)

    _string_to_int = field_validator("tlen", "flen", "girth")(string_to_int)

    _string_to_float = field_validator("rwt", "eviswt", "gonwt", "stom_contents_wt")(
        string_to_float
    )

    # ascii-sort clips, node, agest and tissue
    _check_ascii_sort = field_validator("agest", "tissue", "clipc", "clipa")(
        check_ascii_sort
    )
    _check_agest = check_agest("agest", AGEST_CHOICES)
    _check_tissue = check_tissue("tissue", TISSUE_CHOICES)

    @field_validator("fate", mode="before")
    def set_fate(cls, fate):
        if fate:
            return fate
        else:
            return "K"

    @field_validator("tlen")
    def check_flen_vs_tlen(v, values):
        flen = values.data.get("flen")
        if flen is not None and v is not None:
            if flen > v:
                msg = f"TLEN ({v}) must be greater than or equal to FLEN ({flen})"
                raise ValueError(msg)
        return v

    @field_validator("tlen", "flen")
    def check_condition(v, values, **kwargs):
        """mininum of 0.1 for very, very, small smelt sampled in lake erie
        (lenght=41, rwt=0.1)"""
        rwt = values.data.get("rwt")
        if rwt is not None and v is not None:
            k = 100000 * rwt / (v**3)
            if k > 4.5:
                msg = f"FLEN/TLEN ({v}) is too short for the round weight (RWT={rwt}) (K={k:.3f})"
                raise ValueError(msg)
            if k < 0.1:
                msg = f"FLEN/TLEN ({v}) is too large for the round weight (RWT={rwt}) (K={k:.3f})"
                raise ValueError(msg)
        return v

    @field_validator("tissue")
    def check_tissue(value, values):
        if value is not None:
            unknown = [c for c in value if c not in TISSUE_CHOICES]
            if unknown:
                msg = f"Unknown tissue code ({','.join(unknown)}) found in TISSUE ({value})"
                raise ValueError(msg)
        return value

    @field_validator("clipc", "clipa")
    def check_clic_codes(value, values):
        if value is not None:
            unknown = [c for c in value if c not in CLIP_CHOICES]
            if unknown:
                msg = f"Unknown clip code ({','.join(unknown)}) found in clipa/clipc ({value})"
                raise ValueError(msg)
        return value

    @field_validator("eviswt")
    def check_eviswt_vs_rwt(v, values):
        rwt = values.data.get("rwt")
        if rwt is not None and v is not None:
            if v >= rwt:
                msg = f"EVISWT ({v}) must be less than RWT ({rwt})"
                raise ValueError(msg)
        return v
