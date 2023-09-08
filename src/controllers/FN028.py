from litestar import Controller, get

from schemas import FN028
from utils import get_rows


class FN028Controller(Controller):
    path = "api/fn028"

    @get("/")
    async def fn028(self) -> list[FN028]:

        sql = """SELECT [PRJ_CD],
             [MODE],
             [MODE_DES],
             [GR],
             [GRUSE],
             [ORIENT],
             [EFFDUR_GE],
             [EFFDUR_LT],
             [EFFTM0_GE],
             [EFFTM0_LT]
            FROM FN028;

        """

        data = await get_rows(sql)

        return data
