from litestar import Controller, get, post, put, delete
from typing import Optional, Union
from .FishnetTables import FN011 as FN011Table
from schemas import FN011
from utils import get_rows, get_data, run_sql


class FN011Controller(Controller):
    path = "api/fn011"

    @get("/")
    async def fn011_list(self, prj_cd: Optional[str] = None) -> list[FN011]:
        names = [
            "prj_cd",
        ]
        values = [
            prj_cd,
        ]

        sql = FN011Table.select(order_by_keys=False)
        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}")
    async def fn011_detail(self, prj_cd: str) -> FN011:
        sql = FN011Table.select_one()
        data = await get_rows(
            sql,
            [
                prj_cd,
            ],
        )
        return data

    @post("/")
    async def fn011_create(
        self,
        data: FN011,
    ) -> Optional[FN011]:
        sql = FN011Table.create()

        data_dict = data.model_dump()
        values = FN011Table.values(data_dict)

        await run_sql(sql, values)

        return data

    @put("/{prj_cd:str}")
    async def fn011_put(
        self,
        data: FN011,
        prj_cd: str,
    ) -> Optional[FN011]:
        key_fields = [
            prj_cd,
        ]

        sql = FN011Table.select_one()
        item = await get_rows(
            sql,
            [
                prj_cd,
            ],
        )

        data_dict = data.model_dump()
        values = FN011Table.values(data_dict)
        sql = FN011Table.update_one(data_dict)

        params = values + key_fields
        await run_sql(sql, params)

        return data

    @delete("/{prj_cd:str}")
    async def fn011_delete(
        self,
        prj_cd: str,
    ) -> None:
        sql = FN011Table.delete_one()
        await run_sql(
            sql,
            [
                prj_cd,
            ],
        )

        return None
