from litestar import Controller, get, post, patch, put, delete
from typing import Optional, Union
from schemas import FN125, FN125Partial
from utils import (
    get_data,
    get_rows,
    read_sql_file,
    run_sql,
    get_data_values,
    update_clause,
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

        sql = read_sql_file("controllers/sql/FN125/get_item_list.sql")

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}")
    async def fn125_detail(
        self, prj_cd: str, sam: str, eff: str, spc: str, grp: str, fish: str
    ) -> Union[FN125, None]:
        sql = read_sql_file("controllers/sql/FN125/get_item.sql")
        data = await get_rows(sql, [prj_cd, sam, eff, spc, grp, fish])

        return data

    @post("/")
    async def fn125_create(
        self,
        data: FN125,
    ) -> Union[FN125, None]:
        sql = read_sql_file("controllers/sql/FN125/create_item.sql")
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
        updates = update_clause(data)

        sql = f"""
        Update [FN125] set
        {updates}
        where
        [prj_cd]=? and
        [sam]=? and
        [eff]=? and
        [spc]=? and
        [grp]=? and
        [fish]=?
        """
        params = values + key_fields
        await run_sql(sql, params)

        return data

    @patch("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}")
    async def fn125_patch(
        self,
        data: FN125Partial,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
        fish: str,
    ) -> Union[FN125, None]:
        key_fields = [prj_cd, sam, eff, spc, grp, fish]
        values = get_data_values(data)
        updates = update_clause(data)

        sql = f"""
        Update [FN125] set
        {updates}
        where
        [prj_cd]=? and
        [sam]=? and
        [eff]=? and
        [spc]=? and
        [grp]=? and
        [fish]=?
        """
        params = values + key_fields
        await run_sql(sql, params)

        sql = read_sql_file("controllers/sql/FN125/get_item.sql")
        data = await get_rows(sql, key_fields)

        return data

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
        sql = read_sql_file("controllers/sql/FN125/delete_item.sql")
        await run_sql(sql, [prj_cd, sam, eff, spc, grp, fish])

        return None
