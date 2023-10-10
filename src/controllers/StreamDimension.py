from litestar import Controller, get, post, put, delete
from typing import Optional, Union
from .FishnetTables import StreamDimension as StreamDimensionTable
from schemas import StreamDimension

from utils import get_data, get_rows, run_sql


class StreamDimensionController(Controller):
    path = "api/stream_dimensions"

    @get("/")
    async def stream_dimension_list(
        self,
        prj_cd: Optional[str] = None,
        subspace: Optional[str] = None,
        metres_up: Optional[str] = None,
        metres_across: Optional[str] = None,
    ) -> list[StreamDimension]:
        names = ["prj_cd", "subspace", "metres_up", "metres_across"]

        values = [prj_cd, subspace, metres_up, metres_across]
        sql = StreamDimensionTable.select(order_by_keys=False)

        data = await get_data(sql, names, values)

        return data

    @get("{prj_cd:str}/{subspace:str}/{metres_up:str}/{metres_across:str}")
    async def stream_dimension_detail_detail(
        self,
        prj_cd: str,
        subspace: str,
        metres_up: str,
        metres_across: Optional[str] = None,
    ) -> StreamDimension:
        sql = StreamDimensionTable.select_one()
        data = await get_rows(
            sql,
            [prj_cd, subspace, metres_up, metres_across],
        )

        return data

    @post("/")
    async def stream_dimenation_create(
        self,
        data: StreamDimension,
    ) -> Union[StreamDimension, None]:
        sql = StreamDimensionTable.create()

        data_dict = data.model_dump()
        values = StreamDimensionTable.values(data_dict)

        await run_sql(sql, values)

        return data

    @put("{prj_cd:str}/{subspace:str}/{metres_up:str}/{metres_across:str}")
    async def stream_dimenation_put(
        self,
        data: StreamDimension,
        prj_cd: str,
        subspace: str,
        metres_up: str,
        metres_across: Optional[str] = None,
    ) -> Union[StreamDimension, None]:
        key_fields = [prj_cd, subspace, metres_up, metres_across]
        data_dict = data.model_dump()
        values = StreamDimensionTable.values(data_dict)
        sql = StreamDimensionTable.update_one(data_dict)

        params = values + key_fields

        await run_sql(sql, params)

        return data

    @delete("{prj_cd:str}/{subspace:str}/{metres_up:str}/{metres_across:str}")
    async def stream_dimenation_delete(
        self,
        prj_cd: str,
        subspace: str,
        metres_up: str,
        metres_across: Optional[str] = None,
    ) -> None:
        sql = StreamDimensionTable.delete_one()

        await run_sql(sql, [prj_cd, subspace, metres_up, metres_across])
        return None
