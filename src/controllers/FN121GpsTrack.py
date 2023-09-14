from litestar import Controller, get
from typing import Optional, Union
from schemas import FN121GpsTrack
from utils import get_data, get_rows


class FN121GpsTrackController(Controller):
    path = "api/fn121_gps_track"

    @get("/")
    async def fn121_gps_track_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
    ) -> list[FN121GpsTrack]:
        # filters and values
        names = ["prj_cd", "sam"]
        values = [prj_cd, sam]

        sql = """
        SELECT
         [PRJ_CD],
         [SAM],
         [TRACKID],
         [DD_LON],
         [DD_LAT],
         [Timestamp],
         [SIDEP]
        FROM [FN121_Gps_Tracks]
        """

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}")
    async def fn121_gps_track_detail(
        self, prj_cd: str, sam: str
    ) -> Union[FN121GpsTrack, None]:
        sql = """
        SELECT
         [PRJ_CD],
         [SAM],
         [TRACKID],
         [DD_LON],
         [DD_LAT],
         [Timestamp],
         [SIDEP]
        FROM [FN121_Gps_Tracks]
         where
        [prj_cd]=? and
        [sam]=?
        """

        data = await get_rows(sql, [prj_cd, sam])

        return data
