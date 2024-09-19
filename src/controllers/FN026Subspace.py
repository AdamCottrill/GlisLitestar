from typing import Optional, Union

from litestar import Controller, delete, get, post, put
from schemas import FN026Subspace
from utils import get_data, get_rows, run_sql

from .FishnetTables import FN026Subspace as FN026SubspaceTable


class FN026SubspaceController(Controller):
    path = "api/fn026_subspace"

    @get("/")
    async def fn026Subspace_list(
        self,
        prj_cd: Optional[str] = None,
        space: Optional[str] = None,
        subspace: Optional[str] = None,
    ) -> list[FN026Subspace]:

        names = ["prj_cd", "space", "subspace"]
        values = [prj_cd, space, subspace]

        sql = FN026SubspaceTable.select(order_by_keys=False)
        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{space:str}/{subspace:str}")
    async def fn026Subspace_detail(
        self, prj_cd: str, space: str, subspace: str
    ) -> list[FN026Subspace]:

        sql = FN026SubspaceTable.select_one()
        data = await get_rows(sql, [prj_cd, space])

        return data

    @post("/")
    async def fn026Subspace_create(
        self,
        data: FN026Subspace,
    ) -> Optional[FN026Subspace]:
        sql = FN026SubspaceTable.create()

        data_dict = data.model_dump()
        values = FN026SubspaceTable.values(data_dict)

        await run_sql(sql, values)

        return data

    @put("/{prj_cd:str}/{space:str}/{subspace:str}")
    async def fn026Subspace_put(
        self, data: FN026Subspace, prj_cd: str, space: str, subspace: str
    ) -> Optional[FN026Subspace]:
        key_fields = [prj_cd, space, subspace]

        data_dict = data.model_dump()
        values = FN026SubspaceTable.values(data_dict)
        sql = FN026SubspaceTable.update_one(data_dict)

        params = values + key_fields
        await run_sql(sql, params)

        return data

    @delete("/{prj_cd:str}/{space:str}/{subspace:str}")
    async def fn026Subspace_delete(
        self, prj_cd: str, space: str, subspace: str
    ) -> None:
        sql = FN026SubspaceTable.delete_one()
        await run_sql(sql, [prj_cd, space, subspace])

        return None
