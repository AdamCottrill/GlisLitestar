from litestar import Controller, get

from schemas import FN012
from utils import get_rows


class FN012Controller(Controller):
    path = "api/fn012"

    @get("/")
    async def fn012(self) -> list[FN012]:

        sql = """
        SELECT [PRJ_CD],
         [SPC],
         [SPC_NMCO],
         [GRP],
         [GRP_DES],
         [SIZSAM],
         [SIZATT],
         [SIZINT],
         [BIOSAM],
         [FDSAM],
         [SPCMRK],
         [TISSUE],
         [AGEST],
         [LAMSAM],
         [FLEN_MIN],
         [FLEN_MAX],
         [TLEN_MIN],
         [TLEN_MAX],
         [RWT_MIN],
         [RWT_MAX],
         [K_MIN_ERROR],
         [K_MIN_WARN],
         [K_MAX_ERROR],
         [K_MAX_WARN]
        FROM FN012;
        """

        data = await get_rows(sql)

        return data
