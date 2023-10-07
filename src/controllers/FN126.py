from typing import Optional, Union

from litestar import Controller, delete, get, post, put
from schemas import FN126
from .FishnetTables import FN126 as FN126Table
from utils import (
    get_data,
    get_rows,
    run_sql,
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

        sql = FN126Table.select(order_by_keys=False)
        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{food:int}")
    async def fn126_detail(
        self, prj_cd: str, sam: str, eff: str, spc: str, grp: str, fish: str, food: int
    ) -> Union[FN126, None]:
        sql = FN126Table.select_one()
        data = await get_rows(sql, [prj_cd, sam, eff, spc, grp, fish, food])

        return data

    @post("/")
    async def fn126_create(
        self,
        data: FN126,
    ) -> Union[FN126, None]:
        sql = FN126Table.create()
        data_dict = data.model_dump()
        values = FN126Table.values(data_dict)

        await run_sql(sql, values)
        return data

    @put("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{food:int}")
    async def fn126_put(
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
        key_fields = [prj_cd, sam, eff, spc, grp, fish, food]

        data_dict = data.model_dump()
        values = FN126Table.values(data_dict)

        sql = FN126Table.update_one(data_dict)

        params = values + key_fields
        await run_sql(sql, params)

        return data

    @delete(
        "/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{food:int}"
    )
    async def fn126_delete(
        self, prj_cd: str, sam: str, eff: str, spc: str, grp: str, fish: str, food: int
    ) -> None:
        # sql = read_sql_file("controllers/sql/FN126/delete_item.sql")
        sql = FN126Table.delete_one()
        await run_sql(sql, [prj_cd, sam, eff, spc, grp, fish, food])

        return None
