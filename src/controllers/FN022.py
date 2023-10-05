from litestar import Controller, get, post, put, delete
from typing import Optional, Union
from .FishnetTables import FN022 as FN022Table
from schemas import FN022
from utils import get_rows, get_data, get_data_values, run_sql


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

        sql = FN022Table.select(order_by_keys=False)
        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{ssn:str}")
    async def fn022_detail(self, prj_cd: str, ssn: str) -> list[FN022]:
        sql = FN022Table.select_one()
        data = await get_rows(sql, [prj_cd, ssn])

        return data

    @post("/")
    async def fn022_create(
        self,
        data: FN022,
    ) -> Union[FN022, None]:
        sql = FN022Table.create()

        values = get_data_values(data)

        await run_sql(sql, values)

        return data

    @put("/{prj_cd:str}/{ssn:str}")
    async def fn022_put(
        self,
        data: FN022,
        prj_cd: str,
        ssn: str,
    ) -> Union[FN022, None]:
        key_fields = [prj_cd, ssn]
        values = get_data_values(data)
        sql = FN022Table.update_one(data.model_dump())

        params = values + key_fields
        await run_sql(sql, params)

        return data

    @delete("/{prj_cd:str}/{ssn:str}")
    async def fn022_delete(
        self,
        prj_cd: str,
        ssn: str,
    ) -> None:
        sql = FN022Table.delete_one()
        await run_sql(sql, [prj_cd, ssn])

        return None
