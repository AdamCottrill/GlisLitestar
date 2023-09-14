from dataclasses import dataclass


@dataclass
class GrEffProcType:
    gr: str
    eff: str
    process_type: str
    effdst: str
