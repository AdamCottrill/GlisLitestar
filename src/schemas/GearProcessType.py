from pydantic import validator

from .utils import ProcessTypeEnum

from .FNBase import FNBase


class GearProcessType(FNBase):
    """A validator the project-gear-process type table."""

    gear_id: int
    project_id: int
    slug: str
    process_type: ProcessTypeEnum = ProcessTypeEnum.by_sample
