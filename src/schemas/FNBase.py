from pydantic import BaseModel, ConfigDict, field_validator

prj_cd_regex = r"[A-Z]{3}\_[A-Z]{2}\d{2}\_[A-Z0-9]{3}"


class FNBase(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True, use_enum_values=True, extra="ignore"
    )

    @field_validator('*', mode='before')
    def empty_str_to_none(cls, v):
        if v == '':
            return None
        return v
