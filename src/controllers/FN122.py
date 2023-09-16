from litestar import Controller, get, post, put, patch, delete
from typing import Optional, Union

from schemas import FN122, FN122Partial

from utils import (
    get_rows,
    get_data,
    read_sql_file,
    get_data_values,
    run_sql,
    update_clause,
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

        sql = read_sql_file("controllers/sql/FN122/get_item_list.sql")

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}/{eff:str}")
    async def fn122_detail(self, prj_cd: str, sam: str, eff: str) -> list[FN122]:
        """Add filters for SAM, EFF"""

        sql = read_sql_file("controllers/sql/FN122/get_item.sql")

        data = await get_rows(sql, [prj_cd, sam, eff])

        return data

    @post("/")
    async def fn122_create(
        self,
        data: FN122,
    ) -> Union[FN122, None]:
        sql = read_sql_file("controllers/sql/FN122/create_item.sql")
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
        updates = update_clause(data)

        sql = f"""
        Update [FN122] set
        {updates}
        where
        [prj_cd]=? and
        [sam]=? and
        [eff]=?
        """
        params = values + key_fields
        await run_sql(sql, params)

        return data

    @patch("/{prj_cd:str}/{sam:str}/{eff:str}")
    async def fn122_patch(
        self, data: FN122Partial, prj_cd: str, sam: str, eff: str
    ) -> Union[FN122, None]:
        key_fields = [prj_cd, sam, eff]
        values = get_data_values(data)
        updates = update_clause(data)

        sql = f"""
        Update [FN122] set
        {updates}
        where
        [prj_cd]=? and
        [sam]=? and
        [eff]=?
        """
        params = values + key_fields
        await run_sql(sql, params)

        sql = read_sql_file("controllers/sql/FN122/get_item.sql")
        data = await get_rows(sql, key_fields)

        return data

    @delete("/{prj_cd:str}/{sam:str}/{eff:str}")
    async def fn122_delete(self, prj_cd: str, sam: str, eff: str) -> None:
        sql = read_sql_file("controllers/sql/FN122/delete_item.sql")
        await run_sql(sql, [prj_cd, sam, eff])

        return None
