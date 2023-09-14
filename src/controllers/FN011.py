from litestar import Controller, get

from typing import Optional

from schemas import FN011
from utils import get_rows, get_data


class FN011Controller(Controller):
    path = "api/fn011"

    @get("/")
    async def fn011_list(
        self, prj_cd: Optional[str] = None, year: Optional[str] = None
    ) -> list[FN011]:
        names = ["prj_cd", "year"]
        values = [prj_cd, year]

        sql = """SELECT [YEAR],
         [PRJ_CD],
         [PRJ_NM],
         [PRJ_LDR],
         [PRJ_DATE0],
         [PRJ_DATE1],
         [COMMENT0],
         [PROTOCOL],
         [LAKE]
         FROM FN011
         """

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}")
    async def fn011_detail(self, prj_cd: str) -> FN011:
        sql = """SELECT [YEAR],
         [PRJ_CD],
         [PRJ_NM],
         [PRJ_LDR],
         [PRJ_DATE0],
         [PRJ_DATE1],
         [COMMENT0],
         [PROTOCOL],
         [LAKE]
         FROM FN011 where prj_cd=?;
         """

        data = await get_rows(
            sql,
            [
                prj_cd,
            ],
        )

        return data
