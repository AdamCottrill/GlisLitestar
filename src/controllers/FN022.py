from litestar import Controller, get
from typing import Optional
from schemas import FN022
from utils import get_rows, get_data


class FN022Controller(Controller):
    path = "api/fn022"

    @get("/")
    async def fn022_list(
        self,
        prj_cd: Optional[str] = None,
        ssn: Optional[str] = None,
    ) -> list[FN022]:
        names = ["prj_cd", "ssn"]
        values = [prj_cd, ssn]

        sql = """
        SELECT [PRJ_CD], [SSN], [SSN_DES], [SSN_DATE0], [SSN_DATE1]
        FROM FN022
        """

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{ssn:str}")
    async def fn022_detail(self, prj_cd: str, ssn: str) -> list[FN022]:
        sql = """
        SELECT [PRJ_CD], [SSN], [SSN_DES], [SSN_DATE0], [SSN_DATE1]
        FROM FN022 where [prj_cd] = ? and [ssn] = ?
        """
        data = await get_rows(sql, [prj_cd, ssn])

        return data
