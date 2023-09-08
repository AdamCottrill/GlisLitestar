from litestar import Controller, get
from typing import Optional

from schemas import FN123
from utils import get_rows, args_to_where


class FN123Controller(Controller):
    path = "api/fn123"

    @get("/")
    async def fn123(
        self,
        sam: Optional[str] = None,
        eff: Optional[str] = None,
        spc: Optional[str] = None,
        grp: Optional[str] = None,
    ) -> list[FN123]:
        """Add filters for SAM, EFF"""

        # filters and values
        names = ["sam", "eff", "spc", "grp"]
        values = [sam, eff, spc, grp]

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

        args = [val for val in values if val is not None]
        if args:
            where = args_to_where(names, values)
            sql = sql + where
            data = await get_rows(sql, args)
        else:
            data = await get_rows(sql)

        return data
