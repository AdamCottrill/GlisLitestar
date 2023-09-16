from litestar import Controller, get, post, put, patch, delete
from typing import Optional, Union
from schemas import FN125Lamprey, FN125LampreyPartial
from utils import (
    get_data,
    get_rows,
    read_sql_file,
    get_data_values,
    run_sql,
    update_clause,
)


class FN125LampreyController(Controller):
    path = "api/fn125_lamprey"

    @get("/")
    async def fn125_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
        eff: Optional[str] = None,
        spc: Optional[str] = None,
        grp: Optional[str] = None,
        fish: Optional[str] = None,
        lamid: Optional[str] = None,
    ) -> list[FN125Lamprey]:
        # filters and values
        names = ["prj_cd", "sam", "eff", "spc", "grp", "fish", "lamid"]
        values = [prj_cd, sam, eff, spc, grp, fish, lamid]

        sql = read_sql_file("controllers/sql/FN125Lamprey/get_item_list.sql")

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{lamid:str}")
    async def fn125_detail(
        self, prj_cd: str, sam: str, eff: str, spc: str, grp: str, fish: str, lamid: str
    ) -> Union[FN125Lamprey, None]:
        sql = read_sql_file("controllers/sql/FN125Lamprey/get_item.sql")
        data = await get_rows(sql, [prj_cd, sam, eff, spc, grp, fish, lamid])

        return data

    @post("/")
    async def fn125Tag_create(
        self,
        data: FN125Lamprey,
    ) -> Union[FN125Lamprey, None]:
        sql = read_sql_file("controllers/sql/FN125Lamprey/create_item.sql")
        values = get_data_values(data)
        await run_sql(sql, values)

        return data

    @put("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{lamid:int}")
    async def fn125Tag_put(
        self,
        data: FN125Lamprey,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
        fish: str,
        lamid: int,
    ) -> Union[FN125Lamprey, None]:
        key_fields = [prj_cd, sam, eff, spc, grp, fish, lamid]
        values = get_data_values(data)
        updates = update_clause(data)

        sql = f"""
        Update [FN125_Lamprey] set
        {updates}
        where
        [prj_cd]=? and
        [sam]=? and
        [eff]=? and
        [spc]=? and
        [grp]=? and
        [fish]=? and
        [lamid]=?
        """
        params = values + key_fields
        await run_sql(sql, params)

        return data

    @patch(
        "/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{lamid:int}"
    )
    async def fn125Tag_patch(
        self,
        data: FN125LampreyPartial,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
        fish: str,
        lamid: int,
    ) -> Union[FN125Lamprey, None]:
        key_fields = [prj_cd, sam, eff, spc, grp, fish, lamid]
        values = get_data_values(data)
        updates = update_clause(data)

        sql = f"""
        Update [FN125_Lamprey] set
        {updates}
        where
        [prj_cd]=? and
        [sam]=? and
        [eff]=? and
        [spc]=? and
        [grp]=? and
        [fish]=? and
        [lamid]=?
        """
        params = values + key_fields
        await run_sql(sql, params)

        sql = read_sql_file("controllers/sql/FN125Lamprey/get_item.sql")
        data = await get_rows(sql, key_fields)

        return data

    @delete(
        "/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{lamid:int}"
    )
    async def fn125Tag_delete(
        self,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
        fish: str,
        lamid: int,
    ) -> None:
        sql = read_sql_file("controllers/sql/FN125Lamprey/delete_item.sql")
        await run_sql(sql, [prj_cd, sam, eff, spc, grp, fish, lamid])

        return None
