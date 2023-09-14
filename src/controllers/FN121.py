from litestar import Controller, get
from typing import Optional
from schemas import FN121
from utils import get_data, get_rows


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

        sql = """SELECT [PRJ_CD],
             [SAM],
             [PROCESS_TYPE],
             [SSN],
             [SUBSPACE],
             [MODE],
             [EFFDT0],
             [EFFTM0],
             [EFFDT1],
             [EFFTM1],
             [EFFDUR],
             [EFFST],
             [SITP],
             [DD_LAT0],
             [DD_LON0],
             [DD_LAT1],
             [DD_LON1],
             [GRID5],
             [SITEM0],
             [SITEM1],
             [SIDEP0],
             [SIDEP1],
             [GRDEPMAX],
             [GRDEPMID],
             [GRDEPMIN],
             [SECCHI0],
             [SECCHI1],
             [SLIME],
             [CREW],
             [COMMENT1],
             [VESSEL],
             [VESSEL_DIRECTION],
             [VESSEL_SPEED],
             [WARP],
             [BOTTOM],
             [COVER],
             [LEAD_ANGLE],
             [LEADUSE],
             [DISTOFF],
             [VEGETATION],
             [O2BOT0],
             [O2BOT1],
             [O2SURF0],
             [O2SURF1],
             [O2GR0],
             [O2GR1],
             [AIRTEM0],
             [AIRTEM1],
             [WIND0],
             [WIND1],
             [PRECIP0],
             [PRECIP1],
             [CLOUD_PC0],
             [CLOUD_PC1],
             [WAVEHT0],
             [WAVEHT1],
             [XWEATHER]
            FROM [FN121]
            """

        data = await get_data(sql, names, values)

        return data

    @get("{prj_cd:str}/{sam:str}")
    async def fn121_detail(self, prj_cd: str, sam: str) -> FN121:
        sql = """SELECT [PRJ_CD],
             [SAM],
             [PROCESS_TYPE],
             [SSN],
             [SUBSPACE],
             [MODE],
             [EFFDT0],
             [EFFTM0],
             [EFFDT1],
             [EFFTM1],
             [EFFDUR],
             [EFFST],
             [SITP],
             [DD_LAT0],
             [DD_LON0],
             [DD_LAT1],
             [DD_LON1],
             [GRID5],
             [SITEM0],
             [SITEM1],
             [SIDEP0],
             [SIDEP1],
             [GRDEPMAX],
             [GRDEPMID],
             [GRDEPMIN],
             [SECCHI0],
             [SECCHI1],
             [SLIME],
             [CREW],
             [COMMENT1],
             [VESSEL],
             [VESSEL_DIRECTION],
             [VESSEL_SPEED],
             [WARP],
             [BOTTOM],
             [COVER],
             [LEAD_ANGLE],
             [LEADUSE],
             [DISTOFF],
             [VEGETATION],
             [O2BOT0],
             [O2BOT1],
             [O2SURF0],
             [O2SURF1],
             [O2GR0],
             [O2GR1],
             [AIRTEM0],
             [AIRTEM1],
             [WIND0],
             [WIND1],
             [PRECIP0],
             [PRECIP1],
             [CLOUD_PC0],
             [CLOUD_PC1],
             [WAVEHT0],
             [WAVEHT1],
             [XWEATHER]
            FROM [FN121]
            where [prj_cd]= ? & [sam] = ?
            """

        data = await get_rows(
            sql,
            [
                prj_cd,
                sam,
            ],
        )

        return data
