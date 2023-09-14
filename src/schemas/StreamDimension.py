from dataclasses import dataclass


@dataclass
class StreamDimension:
    prj_cd: str
    subspace: str
    metres_up: str
    metres_across: str
    width: str
    depth: str
    velocity: str
    comment: str
