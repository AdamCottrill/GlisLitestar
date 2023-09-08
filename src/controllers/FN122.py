from litestar import Controller, get

from schemas import FN122
from utils import get_rows


class FN122Controller(Controller):
    path = "api/fn122"

    @get("/")
    async def fn122(self) -> list[FN122]:
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
                FROM FN122;
        """

        data = await get_rows(sql)

        return data
