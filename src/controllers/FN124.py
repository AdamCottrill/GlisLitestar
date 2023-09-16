from litestar import Controller, get, post, put, patch, delete
from typing import Optional, Union
from schemas import FN124, FN124Partial
from utils import (
    get_data,
    get_rows,
    read_sql_file,
    get_data_values,
    run_sql,
    update_clause,
)


class FN124Controller(Controller):
    path = "api/fn124"

    @get("/")
    async def fn124_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
        eff: Optional[str] = None,
        spc: Optional[str] = None,
        grp: Optional[str] = None,
        siz: Optional[str] = None,
    ) -> list[FN124]:
        # filters and values
        names = ["prj_cd", "sam", "eff", "spc", "grp", "siz"]
        values = [prj_cd, sam, eff, spc, grp, siz]

        sql = read_sql_file("controllers/sql/FN124/get_item_list.sql")

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{siz:str}")
    async def fn124_detail(
        self, prj_cd: str, sam: str, eff: str, spc: str, grp: str, siz: str
    ) -> Union[FN124, None]:
        sql = read_sql_file("controllers/sql/FN124/get_item.sql")

        data = await get_rows(sql, [prj_cd, sam, eff, spc, grp, siz])

        return data

    @post("/")
    async def fn124_create(
        self,
        data: FN124,
    ) -> Union[FN124, None]:
        sql = read_sql_file("controllers/sql/FN124/create_item.sql")
        values = get_data_values(data)

        await run_sql(sql, values)

        return data

    @put("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{siz:str}")
    async def fn124_put(
        self,
        data: FN124,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
        siz: str,
    ) -> Union[FN124, None]:
        key_fields = [prj_cd, sam, eff, spc, grp, siz]
        values = get_data_values(data)
        updates = update_clause(data)

        sql = f"""
        Update [FN124] set
        {updates}
        where
        [prj_cd]=? and
        [sam]=? and
        [eff]=? and
        [spc]=? and
        [grp]=? and
        [siz]=?
        """
        params = values + key_fields
        await run_sql(sql, params)

        return data

    @patch("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{siz:str}")
    async def fn124_patch(
        self,
        data: FN124Partial,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
        siz: str,
    ) -> Union[FN124, None]:
        key_fields = [prj_cd, sam, eff, spc, grp, siz]
        values = get_data_values(data)
        updates = update_clause(data)

        sql = f"""
        Update [FN124] set
        {updates}
        where
        [prj_cd]=? and
        [sam]=? and
        [eff]=? and
        [spc]=? and
        [grp]=? and
        [siz]=?
        """
        params = values + key_fields
        await run_sql(sql, params)

        sql = read_sql_file("controllers/sql/FN124/get_item.sql")
        data = await get_rows(sql, key_fields)

        return data

    @delete("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{siz:str}")
    async def fn124_delete(
        self,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
        siz: str,
    ) -> None:
        sql = read_sql_file("controllers/sql/FN124/delete_item.sql")
        await run_sql(sql, [prj_cd, sam, eff, spc, grp, siz])

        return None
