from litestar import Controller, get, post, put, delete
from typing import Optional, Union
from .FishnetTables import GrEffProcType as GrEffProcTypeTable
from schemas import GrEffProcType

from utils import get_data, get_rows, run_sql


class GearEffProcTypeController(Controller):
    path = "api/gear_effort_proctype"

    @get("/")
    async def gr_eff_proc_type_list(
        self,
        gr: Optional[str] = None,
        eff: Optional[str] = None,
        process_type: Optional[str] = None,
    ) -> list[GrEffProcType]:
        names = ["gr", "eff", "process_type"]
        values = [gr, eff, process_type]

        sql = GrEffProcTypeTable.select(order_by_keys=False)

        data = await get_data(sql, names, values)

        return data

    @get("/{gear:str}/{eff:str}/{process_type:str}")
    async def gr_eff_proc_type_detail(
        self, gear: str, eff: str, process_type: str
    ) -> GrEffProcType:
        sql = GrEffProcTypeTable.select_one()
        data = await get_rows(
            sql,
            [gear, eff, process_type],
        )

        return data

    @post("/")
    async def gr_eff_proc_type_create(
        self,
        data: GrEffProcType,
    ) -> Union[GrEffProcType, None]:
        sql = GrEffProcTypeTable.create()

        data_dict = data.model_dump()
        values = GrEffProcTypeTable.values(data_dict)

        await run_sql(sql, values)

        return data

    @put("/{gear:str}/{eff:str}/{process_type:str}")
    async def gr_eff_proc_type_put(
        self, data: GrEffProcType, gear: str, eff: str, process_type: str
    ) -> Union[GrEffProcType, None]:
        key_fields = [gear, eff, process_type]

        data_dict = data.model_dump()
        values = GrEffProcTypeTable.values(data_dict)
        sql = GrEffProcTypeTable.update_one(data_dict)

        params = values + key_fields

        await run_sql(sql, params)

        return data

    @delete("/{gear:str}/{eff:str}/{process_type:str}")
    async def gr_eff_proc_type_delete(
        self, gear: str, eff: str, process_type: str
    ) -> None:
        key_fields = [gear, eff, process_type]
        sql = GrEffProcTypeTable.delete_one()
        await run_sql(sql, key_fields)

        return None
