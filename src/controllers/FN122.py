from litestar import Controller, get, post, put, delete
from typing import Optional, Union
from .FishnetTables import FN122 as FN122Table
from schemas import FN122

from utils import (
    get_rows,
    get_data,
    get_data_values,
    run_sql,
)


class FN122Controller(Controller):
    path = "api/fn122"

    @get("/")
    async def fn122_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
        eff: Optional[str] = None,
    ) -> list[FN122]:
        """Add filters for SAM, EFF"""

        names = ["prj_cd", "sam", "eff"]
        values = [prj_cd, sam, eff]
        sql = FN122Table.select(order_by_keys=False)
        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}/{eff:str}")
    async def fn122_detail(self, prj_cd: str, sam: str, eff: str) -> list[FN122]:
        """Add filters for SAM, EFF"""

        sql = FN122Table.select_one()
        data = await get_rows(sql, [prj_cd, sam, eff])

        return data

    @post("/")
    async def fn122_create(
        self,
        data: FN122,
    ) -> Union[FN122, None]:
        sql = FN122Table.create()

        values = get_data_values(data)

        await run_sql(sql, values)

        return data

    @put("/{prj_cd:str}/{sam:str}/{eff:str}")
    async def fn122_put(
        self,
        data: FN122,
        prj_cd: str,
        sam: str,
        eff: str,
    ) -> Union[FN122, None]:
        key_fields = [prj_cd, sam, eff]
        values = get_data_values(data)
        sql = FN122Table.update_one(data.model_dump())

        params = values + key_fields
        await run_sql(sql, params)

        return data

    # @patch("/{prj_cd:str}/{sam:str}/{eff:str}")
    # async def fn122_patch(
    #     self, data: FN122Partial, prj_cd: str, sam: str, eff: str
    # ) -> Union[FN122, None]:
    #     key_fields = [prj_cd, sam, eff]
    #     values = get_data_values(data)
    #     updates = update_clause(data)

    #     sql = f"""
    #     Update [FN122] set
    #     {updates}
    #     where
    #     [prj_cd]=? and
    #     [sam]=? and
    #     [eff]=?
    #     """
    #     params = values + key_fields
    #     await run_sql(sql, params)

    #     sql = read_sql_file("controllers/sql/FN122/get_item.sql")
    #     data = await get_rows(sql, key_fields)

    #     return data

    @delete("/{prj_cd:str}/{sam:str}/{eff:str}")
    async def fn122_delete(self, prj_cd: str, sam: str, eff: str) -> None:
        sql = FN122Table.delete_one()
        await run_sql(sql, [prj_cd, sam, eff])

        return None
