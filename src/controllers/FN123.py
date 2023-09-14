from litestar import Controller, get
from typing import Optional

from schemas import FN123
from utils import get_rows, get_data


class FN123Controller(Controller):
    path = "api/fn123"

    @get("/")
    async def fn123_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
        eff: Optional[str] = None,
        spc: Optional[str] = None,
        grp: Optional[str] = None,
    ) -> list[FN123]:
        """Add filters for SAM, EFF"""

        # filters and values
        names = ["prj_cd", "sam", "eff", "spc", "grp"]
        values = [prj_cd, sam, eff, spc, grp]

        sql = """SELECT [PRJ_CD],
             [SAM],
             [EFF],
             [SPC],
             [GRP],
             [CATCNT],
             [BIOCNT],
             [CATWT],
             [SUBCNT],
             [SUBWT],
             [COMMENT3]
        FROM FN123"""

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}")
    async def fn123_detail(
        self,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
    ) -> FN123:
        sql = """SELECT [PRJ_CD],
             [SAM],
             [EFF],
             [SPC],
             [GRP],
             [CATCNT],
             [BIOCNT],
             [CATWT],
             [SUBCNT],
             [SUBWT],
             [COMMENT3]
        FROM FN123 where prj_cd=? and sam=? and eff=? and spc=? and grp=?"""

        data = await get_rows(sql, [prj_cd, sam, eff, spc, grp])

        return data
