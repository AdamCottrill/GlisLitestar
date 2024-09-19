from typing import Optional, Union

from litestar import Controller, delete, get, post, put
from schemas import FN125Tag
from .FishnetTables import FN125Tag as FN125TagTable
from utils import (
    get_data,
    get_rows,
    run_sql,
)


class FN125TagController(Controller):
    path = "api/fn125_tag"

    @get("/")
    async def fn125_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
        eff: Optional[str] = None,
        spc: Optional[str] = None,
        grp: Optional[str] = None,
        fish: Optional[str] = None,
        fish_tag_id: Optional[str] = None,
    ) -> list[FN125Tag]:
        # filters and values
        names = ["prj_cd", "sam", "eff", "spc", "grp", "fish", "fish_tag_id"]
        values = [prj_cd, sam, eff, spc, grp, fish, fish_tag_id]

        sql = FN125TagTable.select(order_by_keys=False)

        data = await get_data(sql, names, values)

        return data

    @get(
        "/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{fish_tag_id:int}"
    )
    async def fn125_detail(
        self,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
        fish: str,
        fish_tag_id: int,
    ) -> Union[FN125Tag, None]:
        sql = FN125TagTable.select_one()
        data = await get_rows(sql, [prj_cd, sam, eff, spc, grp, fish, fish_tag_id])

        return data

    @post("/")
    async def fn125Tag_create(
        self,
        data: FN125Tag,
    ) -> Union[FN125Tag, None]:
        sql = FN125TagTable.create()
        data_dict = data.model_dump()
        values = FN125TagTable.values(data_dict)
        await run_sql(sql, values)

        return data

    @put(
        "/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{fish_tag_id:int}"
    )
    async def fn125Tag_put(
        self,
        data: FN125Tag,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
        fish: str,
        fish_tag_id: int,
    ) -> Union[FN125Tag, None]:
        key_fields = [prj_cd, sam, eff, spc, grp, fish, fish_tag_id]

        data_dict = data.model_dump()
        values = FN125TagTable.values(data_dict)

        sql = FN125TagTable.update_one(data_dict)

        params = values + key_fields
        await run_sql(sql, params)

        return data

    # @patch(
    #     "/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{fish_tag_id:int}"
    # )
    # async def fn125Tag_patch(
    #     self,
    #     data: FN125TagPartial,
    #     prj_cd: str,
    #     sam: str,
    #     eff: str,
    #     spc: str,
    #     grp: str,
    #     fish: str,
    #     fish_tag_id: int,
    # ) -> Union[FN125Tag, None]:
    #     key_fields = [prj_cd, sam, eff, spc, grp, fish, fish_tag_id]
    #     values = get_data_values(data)
    #     updates = update_clause(data)

    #     sql = f"""
    #     Update [FN125_Tags] set
    #     {updates}
    #     where
    #     [prj_cd]=? and
    #     [sam]=? and
    #     [eff]=? and
    #     [spc]=? and
    #     [grp]=? and
    #     [fish]=? and
    #     [fish_tag_id]=?
    #     """
    #     params = values + key_fields
    #     await run_sql(sql, params)

    #     sql = read_sql_file("controllers/sql/FN125Tag/get_item.sql")
    #     data = await get_rows(sql, key_fields)

    #     return data

    @delete(
        "/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{fish_tag_id:int}"
    )
    async def fn125Tag_delete(
        self,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
        fish: str,
        fish_tag_id: int,
    ) -> None:
        sql = FN125TagTable.delete_one()
        await run_sql(sql, [prj_cd, sam, eff, spc, grp, fish, fish_tag_id])

        return None
