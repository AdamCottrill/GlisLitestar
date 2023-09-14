from litestar import Controller, get

from schemas import FN028
from typing import Optional
from utils import get_rows, get_data


class FN028Controller(Controller):
    path = "api/fn028"

    @get("/")
    async def fn028_list(
        self,
        prj_cd: Optional[str] = None,
        mode: Optional[str] = None,
    ) -> list[FN028]:
        names = ["prj_cd", "mode"]
        values = [prj_cd, mode]

        sql = """SELECT [PRJ_CD],
             [MODE],
             [MODE_DES],
             [GR],
             [GRUSE],
             [ORIENT],
             [EFFDUR_GE],
             [EFFDUR_LT],
             [EFFTM0_GE],
             [EFFTM0_LT]
            FROM [FN028]

        """

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{mode:str}")
    async def fn028_detail(self, prj_cd: str, mode: str) -> list[FN028]:
        sql = """SELECT [PRJ_CD],
             [MODE],
             [MODE_DES],
             [GR],
             [GRUSE],
             [ORIENT],
             [EFFDUR_GE],
             [EFFDUR_LT],
             [EFFTM0_GE],
             [EFFTM0_LT]
            FROM [FN028]  where [prj_cd]=? and [mode]=?

        """

        data = await get_rows(sql, [prj_cd, mode])

        return data
