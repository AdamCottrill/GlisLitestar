from pydantic import confloat, constr
from typing import Optional
from .FNBase import FNBase
from .utils import ProcessTypeEnum


class GrEffProcType(FNBase):
    """A validator the project-gear-process type table."""

    gr: constr(pattern="^([A-Z0-9]{2,5})$", max_length=5)
    eff: constr(pattern="^([A-Z0-9]{1,3})$")
    effdst: Optional[confloat(gt=0)] = None

    process_type: ProcessTypeEnum = ProcessTypeEnum.by_sample
