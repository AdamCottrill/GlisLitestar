from litestar import Controller, get, post, put, delete

from .FishnetTables import FN028 as FN028Table
from schemas import FN028
from typing import Optional, Union
from utils import get_rows, get_data, run_sql


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
        sql = FN028Table.select(order_by_keys=False)
        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{mode:str}")
    async def fn028_detail(self, prj_cd: str, mode: str) -> list[FN028]:
        sql = FN028Table.select_one()
        data = await get_rows(sql, [prj_cd, mode])

        return data

    @post("/")
    async def fn028_create(
        self,
        data: FN028,
    ) -> Union[FN028, None]:
        sql = FN028Table.create()

        data_dict = data.model_dump()
        values = FN028Table.values(data_dict)

        await run_sql(sql, values)

        return data

    @put("/{prj_cd:str}/{mode:str}")
    async def fn028_put(
        self,
        data: FN028,
        prj_cd: str,
        mode: str,
    ) -> Union[FN028, None]:
        key_fields = [prj_cd, mode]

        data_dict = data.model_dump()
        values = FN028Table.values(data_dict)
        sql = FN028Table.update_one(data_dict)

        params = values + key_fields

        await run_sql(sql, params)

        return data

    @delete("/{prj_cd:str}/{mode:str}")
    async def fn028_delete(
        self,
        prj_cd: str,
        mode: str,
    ) -> None:
        sql = FN028Table.delete_one()
        await run_sql(sql, [prj_cd, mode])

        return None
