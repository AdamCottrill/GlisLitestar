from typing import Optional
from dataclasses import dataclass


@dataclass
class FN125Tag:
    prj_cd: str
    sam: str
    eff: str
    spc: str
    grp: str
    fish: str
    fish_tag_id: int
    tagid: str
    tagdoc: str
    tagstat: str
    cwtseq: int
    comment_tag: str


@dataclass
class FN125TagPartial:
    tagid: Optional[str] = None
    tagdoc: Optional[str] = None
    tagstat: Optional[str] = None
    cwtseq: Optional[int] = None
    comment_tag: Optional[str] = None
