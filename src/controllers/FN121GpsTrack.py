from litestar import Controller, get, post, put, delete
from typing import Optional, Union
from .FishnetTables import FN121GpsTrack as FN121GpsTrackTable
from schemas import FN121GpsTrack
from utils import get_data, get_rows, run_sql


class FN121GpsTrackController(Controller):
    path = "api/fn121_gps_tracks"

    @get("/")
    async def fn121_gps_track_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
    ) -> list[FN121GpsTrack]:
        # filters and values
        names = ["prj_cd", "sam"]
        values = [prj_cd, sam]

        sql = FN121GpsTrackTable.select(order_by_keys=False)

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}/{trackid:int}")
    async def fn121_gps_track_detail(
        self, prj_cd: str, sam: str, trackid: int
    ) -> Union[FN121GpsTrack, None]:
        sql = FN121GpsTrackTable.select_one()

        data = await get_rows(sql, [prj_cd, sam, trackid])

        return data

    @post("/")
    async def fn121_gps_track_create(
        self,
        data: FN121GpsTrack,
    ) -> Union[FN121GpsTrack, None]:
        sql = FN121GpsTrackTable.create()

        data_dict = data.model_dump()
        values = FN121GpsTrackTable.values(data_dict)

        await run_sql(sql, values)

        return data

    @put("/{prj_cd:str}/{sam:str}/{trackid:int}")
    async def fn121_gps_track_put(
        self, data: FN121GpsTrack, prj_cd: str, sam: str, trackid: int
    ) -> Union[FN121GpsTrack, None]:
        key_fields = [prj_cd, sam, trackid]

        data_dict = data.model_dump()
        values = FN121GpsTrackTable.values(data_dict)
        sql = FN121GpsTrackTable.update_one(data_dict)

        params = values + key_fields
        await run_sql(sql, params)

        return data

    @delete("/{prj_cd:str}/{sam:str}/{trackid:int}")
    async def fn121_gps_track_delete(self, prj_cd: str, sam: str, trackid: int) -> None:
        sql = FN121GpsTrackTable.delete_one()
        await run_sql(sql, [prj_cd, sam, trackid])

        return None
