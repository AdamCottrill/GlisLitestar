from litestar import Controller, get, post, put, delete
from typing import Optional, Union
from .FishnetTables import FN026 as FN026Table
from schemas import FN026
from utils import get_rows, get_data, run_sql

class FN026Controller(Controller):
    path = "api/fn026"


    @get("/")
    async def fn026_list(
        self,
        prj_cd: Optional[str] = None,
        space: Optional[str] = None,
    ) -> list[FN026]:
        names = ["prj_cd", "space"]
        values = [prj_cd, space]

        sql = FN026Table.select(order_by_keys=False)
        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{space:str}")
    async def fn026_detail(self, prj_cd: str, space: str) -> list[FN026]:
        sql = FN026Table.select_one()
        data = await get_rows(sql, [prj_cd, space])

        return data

    @post("/")
    async def fn026_create(
        self,
        data: FN026,
    ) -> Union[FN026, None]:

        sql = FN026Table.create()

        data_dict = data.model_dump()
        values = FN026Table.values(data_dict)

        await run_sql(sql, values)

        return data

    @put("/{prj_cd:str}/{space:str}")
    async def fn026_put(
        self,
        data: FN026,
        prj_cd: str,
        space: str,
    ) -> Union[FN026, None]:
        key_fields = [prj_cd, space]

        data_dict = data.model_dump()
        values = FN026Table.values(data_dict)
        sql = FN026Table.update_one(data_dict)

        params = values + key_fields
        await run_sql(sql, params)

        return data

    @delete("/{prj_cd:str}/{space:str}")
    async def fn026_delete(
        self,
        prj_cd: str,
        space: str,
    ) -> None:
        sql = FN026Table.delete_one()
        await run_sql(sql, [prj_cd, space])

        return None
