from pydantic import BaseModel, ConfigDict

prj_cd_regex = r"[A-Z]{3}\_[A-Z]{2}\d{2}\_[A-Z0-9]{3}"


class FNBase(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True, use_enum_values=True, extra="ignore"
    )
