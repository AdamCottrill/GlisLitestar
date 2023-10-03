from litestar import Controller, get, post, patch, put, delete
from typing import Optional, Union
from schemas import FN125
from .FishnetTables import FN125 as FN125Table
from utils import (
    get_data,
    get_rows,
    run_sql,
    get_data_values,
)


class FN125Controller(Controller):
    path = "api/fn125"

    @get("/")
    async def fn125_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
        eff: Optional[str] = None,
        spc: Optional[str] = None,
        grp: Optional[str] = None,
        fish: Optional[str] = None,
    ) -> list[FN125]:
        # filters and values
        names = ["prj_cd", "sam", "eff", "spc", "grp", "fish"]
        values = [prj_cd, sam, eff, spc, grp, fish]

        sql = FN125Table.select(order_by_keys=False)
        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}")
    async def fn125_detail(
        self, prj_cd: str, sam: str, eff: str, spc: str, grp: str, fish: str
    ) -> Union[FN125, None]:

        sql = FN125Table.select_one()
        data = await get_rows(sql, [prj_cd, sam, eff, spc, grp, fish])

        return data

    @post("/")
    async def fn125_create(
        self,
        data: FN125,
    ) -> Union[FN125, None]:

        sql = FN125Table.create()
        values = get_data_values(data)

        await run_sql(sql, values)

        return data

    @put("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}")
    async def fn125_put(
        self,
        data: FN125,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
        fish: str,
    ) -> Union[FN125, None]:
        key_fields = [prj_cd, sam, eff, spc, grp, fish]
        values = get_data_values(data)

        sql = FN125Table.update_one(data.model_dump())

        params = values + key_fields
        await run_sql(sql, params)

        return data

    # @patch("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}")
    # async def fn125_patch(
    #     self,
    #     data: FN125Partial,
    #     prj_cd: str,
    #     sam: str,
    #     eff: str,
    #     spc: str,
    #     grp: str,
    #     fish: str,
    # ) -> Union[FN125, None]:
    #     key_fields = [prj_cd, sam, eff, spc, grp, fish]
    #     values = get_data_values(data)
    #     updates = update_clause(data)

    #     sql = f"""
    #     Update [FN125] set
    #     {updates}
    #     where
    #     [prj_cd]=? and
    #     [sam]=? and
    #     [eff]=? and
    #     [spc]=? and
    #     [grp]=? and
    #     [fish]=?
    #     """
    #     params = values + key_fields
    #     await run_sql(sql, params)

    #     sql = read_sql_file("controllers/sql/FN125/get_item.sql")
    #     data = await get_rows(sql, key_fields)

    #     return data

    @delete("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}")
    async def fn125_delete(
        self,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
        fish: str,
    ) -> None:
        sql = FN125Table.delete_one()
        await run_sql(sql, [prj_cd, sam, eff, spc, grp, fish])

        return None
