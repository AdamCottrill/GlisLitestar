from litestar import Controller, get, post, delete, patch
from typing import Optional, Union
from schemas import FN126, FN126Partial
from utils import (
    get_data,
    get_rows,
    run_sql,
    read_sql_file,
    get_data_values,
    update_clause,
)


class FN126Controller(Controller):
    path = "api/fn126"

    @get("/")
    async def fn126_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
        eff: Optional[str] = None,
        spc: Optional[str] = None,
        grp: Optional[str] = None,
        fish: Optional[str] = None,
        food: Optional[str] = None,
    ) -> list[FN126]:
        # filters and values
        names = ["prj_cd", "sam", "eff", "spc", "grp", "fish", "food"]
        values = [prj_cd, sam, eff, spc, grp, fish, food]

        sql = read_sql_file("controllers/sql/FN126/get_item_list.sql")

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{food:int}")
    async def fn126_detail(
        self, prj_cd: str, sam: str, eff: str, spc: str, grp: str, fish: str, food: int
    ) -> Union[FN126, None]:
        sql = read_sql_file("controllers/sql/FN126/get_item.sql")
        data = await get_rows(sql, [prj_cd, sam, eff, spc, grp, fish, food])

        return data

    @post("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{food:int}")
    async def fn126_create(
        self,
        data: FN126,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
        fish: str,
        food: int,
    ) -> Union[FN126, None]:
        sql = read_sql_file("controllers/sql/FN126/create_item.sql")
        values = get_data_values(data)
        await run_sql(sql, values)

        return data

    @patch(
        "/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{food:int}"
    )
    async def fn126_patch(
        self,
        data: FN126Partial,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
        fish: str,
        food: int,
    ) -> Union[FN126, None]:
        keyfields = [prj_cd, sam, eff, spc, grp, fish, food]
        values = get_data_values(data)
        updates = update_clause(data)

        sql = f"""
        Update [FN126] set
        {updates}
        where
        [prj_cd]=? and
        [sam]=? and
        [eff]=? and
        [spc]=? and
        [grp]=? and
        [fish]=? and
        [food]=?
        """
        params = values + keyfields
        await run_sql(sql, params)

        sql = read_sql_file("controllers/sql/FN126/get_item.sql")
        data = await get_rows(sql, keyfields)

        return data

    @delete(
        "/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{food:int}"
    )
    async def fn126_delete(
        self, prj_cd: str, sam: str, eff: str, spc: str, grp: str, fish: str, food: int
    ) -> None:
        sql = read_sql_file("controllers/sql/FN126/delete_item.sql")
        await run_sql(sql, [prj_cd, sam, eff, spc, grp, fish, food])

        return None
