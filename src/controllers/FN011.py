from litestar import Controller, get

from schemas import FN011
from utils import get_rows


class FN011Controller(Controller):
    path = "api/fn011"

    @get("/")
    async def fn011(self) -> list[FN011]:
        sql = """SELECT [YEAR],
         [PRJ_CD],
         [PRJ_NM],
         [PRJ_LDR],
         [PRJ_DATE0],
         [PRJ_DATE1],
         [COMMENT0],
         [PROTOCOL],
         [LAKE]
         FROM FN011;
         """

        data = await get_rows(sql)

        return data
