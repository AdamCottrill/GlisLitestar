from litestar import Controller, get, post, put, delete
from typing import Optional, Union
from schemas import FN121
from .FishnetTables import FN121 as FN121Table

from utils import (
    get_rows,
    get_data,
    run_sql,
)


class FN121Controller(Controller):
    path = "api/fn121"

    @get("/")
    async def fn121_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
        ssn: Optional[str] = None,
        subspace: Optional[str] = None,
        mode: Optional[str] = None,
    ) -> list[FN121]:
        # filters and values
        names = ["prj_cd", "sam", "ssn", "mode", "subspace"]
        values = [prj_cd, sam, ssn, mode, subspace]
        sql = FN121Table.select(order_by_keys=False)

        data = await get_data(sql, names, values)

        return data

    @get("{prj_cd:str}/{sam:str}")
    async def fn121_detail(self, prj_cd: str, sam: str) -> FN121:
        sql = FN121Table.select_one()

        data = await get_rows(
            sql,
            [
                prj_cd,
                sam,
            ],
        )

        return data

    @post("/")
    async def fn121_create(
        self,
        data: FN121,
    ) -> Union[FN121, None]:
        sql = FN121Table.create()

        data_dict = data.model_dump()
        values = FN121Table.values(data_dict)

        await run_sql(sql, values)

        return data

    @put("/{prj_cd:str}/{sam:str}")
    async def fn121_put(
        self,
        data: FN121,
        prj_cd: str,
        sam: str,
    ) -> Union[FN121, None]:
        key_fields = [prj_cd, sam]
        data_dict = data.model_dump()
        values = FN121Table.values(data_dict)
        sql = FN121Table.update_one(data_dict)
        params = values + key_fields
        await run_sql(sql, params)

        return data

    # @patch("/{prj_cd:str}/{sam:str}")
    # async def fn121_patch(
    #     self, data: FN121Partial, prj_cd: str, sam: str
    # ) -> Union[FN121, None]:
    #     key_fields = [prj_cd, sam]
    #     values = get_data_values(data)
    #     updates = update_clause(data)

    #     sql = f"""
    #     Update [FN121] set
    #     {updates}
    #     where
    #     [prj_cd]=? and
    #     [sam]=?
    #     """
    #     params = values + key_fields
    #     await run_sql(sql, params)

    #     sql = read_sql_file("controllers/sql/FN121/get_item.sql")
    #     data = await get_rows(sql, key_fields)

    #     return data

    @delete("/{prj_cd:str}/{sam:str}")
    async def fn121_delete(self, prj_cd: str, sam: str) -> None:
        sql = FN121Table.delete_one()
        await run_sql(sql, [prj_cd, sam])

        return None
