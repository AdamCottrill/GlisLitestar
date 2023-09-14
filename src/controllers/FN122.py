from litestar import Controller, get
from typing import Optional

from schemas import FN122
from utils import get_data, get_rows


class FN122Controller(Controller):
    path = "api/fn122"

    @get("/")
    async def fn122_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
        eff: Optional[str] = None,
    ) -> list[FN122]:
        """Add filters for SAM, EFF"""

        names = ["prj_cd", "sam", "eff"]
        values = [prj_cd, sam, eff]

        sql = """SELECT [PRJ_CD],
             [SAM],
             [EFF],
             [EFFDST],
             [GRDEP0],
             [GRDEP1],
             [GRTEM0],
             [GRTEM1],
             [WATERHAUL],
             [COMMENT2]
                FROM [FN122]
        """

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}/{eff:str}")
    async def fn122_detail(self, prj_cd: str, sam: str, eff: str) -> list[FN122]:
        """Add filters for SAM, EFF"""

        sql = """SELECT [PRJ_CD],
             [SAM],
             [EFF],
             [EFFDST],
             [GRDEP0],
             [GRDEP1],
             [GRTEM0],
             [GRTEM1],
             [WATERHAUL],
             [COMMENT2]
             FROM [FN122] where [prj_cd]=? and [sam]=? and [eff]=?
        """

        data = await get_rows(sql, [prj_cd, sam, eff])

        return data
