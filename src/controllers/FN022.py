from litestar import Controller, get

from schemas import FN022
from utils import get_rows


class FN022Controller(Controller):
    path = "api/fn022"

    @get("/")
    async def fn022(self) -> list[FN022]:
        sql = """
        SELECT [PRJ_CD], [SSN], [SSN_DES], [SSN_DATE0], [SSN_DATE1]
        FROM FN022;
        """
        data = await get_rows(sql)

        return data
