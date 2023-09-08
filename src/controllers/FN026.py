from litestar import Controller, get

from schemas import FN026
from utils import get_rows


class FN026Controller(Controller):
    path = "api/fn026"

    @get("/")
    async def fn026(self) -> list[FN026]:

        sql = """
        SELECT [PRJ_CD],
             [SPACE],
             [SPACE_DES],
             [DD_LAT],
             [DD_LON],
             [SIDEP_LT],
             [SIDEP_GE],
             [GRDEP_LT],
             [GRDEP_GE],
             [SPACE_WT]
            FROM FN026;
        """

        data = await get_rows(sql)

        return data
