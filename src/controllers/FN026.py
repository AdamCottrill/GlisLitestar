from litestar import Controller, get

from schemas import FN026
from utils import get_rows


class FN026Controller(Controller):
    path = "api/fn026"

    @get("/")
    async def fn026_list(self) -> list[FN026]:
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

    @get("/{prj_cd:str}/{space:str}")
    async def fn026_detail(self, prj_cd: str, space: str) -> list[FN026]:
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
            FROM [FN026]
            WHERE [prj_cd]=? AND [space]=?
        """

        data = await get_rows(sql, [prj_cd, space])

        return data
