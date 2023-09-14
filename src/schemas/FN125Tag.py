from dataclasses import dataclass


@dataclass
class FN125Tag:
    prj_cd: str
    sam: str
    eff: str
    spc: str
    grp: str
    fish: str
    fish_tag_id: str
    tagid: str
    tagdoc: str
    tagstat: str
    cwtseq: str
    comment_tag: str
