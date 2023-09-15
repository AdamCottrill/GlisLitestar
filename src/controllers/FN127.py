from typing import Optional, Union
from litestar import Controller, delete, get, patch, post
from schemas import FN127, FN127Partial
from utils import (
    get_data,
    get_data_values,
    get_rows,
    read_sql_file,
    run_sql,
    update_clause,
)


class FN127Controller(Controller):
    path = "api/fn127"

    @get("/")
    async def fn127_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
        eff: Optional[str] = None,
        spc: Optional[str] = None,
        grp: Optional[str] = None,
        fish: Optional[str] = None,
        ageid: Optional[str] = None,
    ) -> list[FN127]:
        # filters and values
        names = ["prj_cd", "sam", "eff", "spc", "grp", "fish", "ageid"]
        values = [prj_cd, sam, eff, spc, grp, fish, ageid]

        sql = read_sql_file("controllers/sql/FN127/get_item_list.sql")

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{ageid:str}")
    async def fn127_detail(
        self, prj_cd: str, sam: str, eff: str, spc: str, grp: str, fish: str, ageid: str
    ) -> Union[FN127, None]:
        sql = read_sql_file("controllers/sql/FN126/get_item.sql")

        data = await get_rows(sql, [prj_cd, sam, eff, spc, grp, fish, ageid])

        return data

    @post(
        "/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{ageid:int}"
    )
    async def fn127_create(
        self,
        data: FN127,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
        fish: str,
        ageid: int,
    ) -> Union[FN127, None]:
        sql = read_sql_file("controllers/sql/FN127/create_item.sql")
        values = get_data_values(data)

        await run_sql(sql, values)

        return data

    @patch(
        "/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{ageid:int}"
    )
    async def fn127_patch(
        self,
        data: FN127Partial,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
        fish: str,
        ageid: int,
    ) -> Union[FN127, None]:
        keyfields = [prj_cd, sam, eff, spc, grp, fish, ageid]

        values = get_data_values(data)
        updates = update_clause(data)

        sql = f"""
        Update [FN127] set
        {updates}
        where
        [prj_cd]=? and
        [sam]=? and
        [eff]=? and
        [spc]=? and
        [grp]=? and
        [fish]=? and
        [ageid]=?
        """
        params = values + keyfields

        print(sql)
        print(params)

        await run_sql(sql, params)

        sql = read_sql_file("controllers/sql/FN127/get_item.sql")
        data = await get_rows(sql, keyfields)

        return data

    @delete(
        "/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{ageid:int}"
    )
    async def fn127_delete(
        self, prj_cd: str, sam: str, eff: str, spc: str, grp: str, fish: str, ageid: int
    ) -> None:
        sql = read_sql_file("controllers/sql/FN127/delete_item.sql")
        await run_sql(sql, [prj_cd, sam, eff, spc, grp, fish, ageid])

        return None


class FN127Controller(Controller):
    path = "api/fn127"

    @get("/")
    async def fn127_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
        eff: Optional[str] = None,
        spc: Optional[str] = None,
        grp: Optional[str] = None,
        fish: Optional[str] = None,
        ageid: Optional[str] = None,
    ) -> list[FN127]:
        # filters and values
        names = ["prj_cd", "sam", "eff", "spc", "grp", "fish", "ageid"]
        values = [prj_cd, sam, eff, spc, grp, fish, ageid]

        sql = read_sql_file("controllers/sql/FN127/get_item_list.sql")

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{ageid:str}")
    async def fn127_detail(
        self, prj_cd: str, sam: str, eff: str, spc: str, grp: str, fish: str, ageid: str
    ) -> Union[FN127, None]:
        sql = read_sql_file("controllers/sql/FN126/get_item.sql")

        data = await get_rows(sql, [prj_cd, sam, eff, spc, grp, fish, ageid])

        return data

    @post(
        "/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{ageid:int}"
    )
    async def fn127_create(
        self,
        data: FN127,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
        fish: str,
        ageid: int,
    ) -> Union[FN127, None]:
        sql = read_sql_file("controllers/sql/FN127/create_item.sql")
        values = get_data_values(data)

        await run_sql(sql, values)

        return data

    @patch(
        "/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{ageid:int}"
    )
    async def fn127_patch(
        self,
        data: FN127Partial,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
        fish: str,
        ageid: int,
    ) -> Union[FN127, None]:
        keyfields = [prj_cd, sam, eff, spc, grp, fish, ageid]
        values = get_data_values(data)
        updates = update_clause(data)

        sql = f"""
        Update [FN127] set
        {updates}
        where
        [prj_cd]=? and
        [sam]=? and
        [eff]=? and
        [spc]=? and
        [grp]=? and
        [fish]=? and
        [ageid]=?
        """
        params = values + keyfields
        await run_sql(sql, params)

        sql = read_sql_file("controllers/sql/FN127/get_item.sql")
        data = await get_rows(sql, keyfields)

        return data

    @delete(
        "/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{ageid:int}"
    )
    async def fn127_delete(
        self, prj_cd: str, sam: str, eff: str, spc: str, grp: str, fish: str, ageid: int
    ) -> None:
        sql = read_sql_file("controllers/sql/FN127/delete_item.sql")
        await run_sql(sql, [prj_cd, sam, eff, spc, grp, fish, ageid])

        return None
