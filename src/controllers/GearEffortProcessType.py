from litestar import Controller, get
from typing import Optional
from schemas import GrEffProcType
from utils import get_data, get_rows


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

        sql = """SELECT [GR], [EFF], [PROCESS_TYPE], [EFFDST]
            FROM [Gear_Effort_Process_Types]
        """

        data = await get_data(sql, names, values)

        return data

    @get("{gear:str}/{eff:str}/{process_type:str}")
    async def gr_eff_proc_type_detail(
        self, gear: str, eff: str, process_type: str
    ) -> GrEffProcType:
        sql = """
            SELECT [GR], [EFF], [PROCESS_TYPE], [EFFDST]
            FROM [Gear_Effort_Process_Types]
            where [gr]= ? and  [eff] = ? and [Process_Type]=?
            """

        data = await get_rows(
            sql,
            [gear, eff, process_type],
        )

        return data
