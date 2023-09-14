from litestar import Controller, get
from typing import Optional, Union
from schemas import FN121Electrofishing
from utils import get_data, get_rows


class FN121ElectrofishingController(Controller):
    path = "api/fn121_electrofishing"

    @get("/")
    async def fn121_electrofishing_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
    ) -> list[FN121Electrofishing]:
        # filters and values
        names = ["prj_cd", "sam"]
        values = [prj_cd, sam]

        sql = """
        SELECT
         [PRJ_CD],
         [SAM],
         [SHOCK_SEC],
         [VOLTS_MIN],
         [VOLTS_MAX],
         [VOLTS_MEAN],
         [AMPS_MIN],
         [AMPS_MAX],
         [AMPS_MEAN],
         [POWER_MIN],
         [POWER_MAX],
         [POWER_MEAN],
         [CONDUCT],
         [TURBIDITY],
         [FREQ],
         [PULSE_DUR],
         [DUTY_CYCLE],
         [WAVEFORM],
         [ANODES],
         [NUM_NETTERS],
         [COMMENT_EFISH]
        FROM [FN121_Electrofishing]
        """

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}")
    async def fn121_electrofishing_detail(
        self, prj_cd: str, sam: str
    ) -> Union[FN121Electrofishing, None]:
        sql = """
        SELECT
         [PRJ_CD],
         [SAM],
         [SHOCK_SEC],
         [VOLTS_MIN],
         [VOLTS_MAX],
         [VOLTS_MEAN],
         [AMPS_MIN],
         [AMPS_MAX],
         [AMPS_MEAN],
         [POWER_MIN],
         [POWER_MAX],
         [POWER_MEAN],
         [CONDUCT],
         [TURBIDITY],
         [FREQ],
         [PULSE_DUR],
         [DUTY_CYCLE],
         [WAVEFORM],
         [ANODES],
         [NUM_NETTERS],
         [COMMENT_EFISH]
        FROM [FN121_Electrofishing]
         where
        [prj_cd]=? and
        [sam]=?
        """

        data = await get_rows(sql, [prj_cd, sam])

        return data
