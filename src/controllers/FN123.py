from litestar import Controller, get, post, put, delete
from typing import Optional, Union
from .FishnetTables import FN123 as FN123Table
from schemas import FN123
from utils import (
    get_rows,
    get_data,
    get_data_values,
    run_sql,
)


class FN123Controller(Controller):
    path = "api/fn123"

    @get("/")
    async def fn123_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
        eff: Optional[str] = None,
        spc: Optional[str] = None,
        grp: Optional[str] = None,
    ) -> list[FN123]:
        """Add filters for SAM, EFF"""

        # filters and values
        names = ["prj_cd", "sam", "eff", "spc", "grp"]
        values = [prj_cd, sam, eff, spc, grp]
        sql = FN123Table.select(order_by_keys=False)

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}")
    async def fn123_detail(
        self,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
    ) -> FN123:
        sql = FN123Table.select_one()
        data = await get_rows(sql, [prj_cd, sam, eff, spc, grp])

        return data

    @post("/")
    async def fn123_create(
        self,
        data: FN123,
    ) -> Union[FN123, None]:
        values = get_data_values(data)
        sql = FN123Table.create()

        await run_sql(sql, values)

        return data

    @put("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}")
    async def fn123_put(
        self,
        data: FN123,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
    ) -> Union[FN123, None]:
        key_fields = [prj_cd, sam, eff, spc, grp]
        values = get_data_values(data)

        sql = FN123Table.update_one(data.model_dump())

        params = values + key_fields
        await run_sql(sql, params)

        return data

    # @patch("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}")
    # async def fn123_patch(
    #     self,
    #     data: FN123Partial,
    #     prj_cd: str,
    #     sam: str,
    #     eff: str,
    #     spc: str,
    #     grp: str,
    # ) -> Union[FN123, None]:
    #     key_fields = [prj_cd, sam, eff, spc, grp]
    #     values = get_data_values(data)
    #     updates = update_clause(data)

    #     sql = f"""
    #     Update [FN123] set
    #     {updates}
    #     where
    #     [prj_cd]=? and
    #     [sam]=? and
    #     [eff]=? and
    #     [spc]=? and
    #     [grp]=?
    #     """
    #     params = values + key_fields
    #     await run_sql(sql, params)

    #     sql = read_sql_file("controllers/sql/FN123/get_item.sql")
    #     data = await get_rows(sql, key_fields)

    #     return data

    @delete("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}")
    async def fn123_delete(
        self,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
    ) -> None:
        sql = FN123Table.delete_one()

        await run_sql(sql, [prj_cd, sam, eff, spc, grp])

        return None
