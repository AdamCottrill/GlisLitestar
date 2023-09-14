from litestar import Controller, get
from typing import Optional, Union
from schemas import FN012
from utils import get_data, get_rows


class FN012Controller(Controller):
    path = "api/fn012"

    @get("/")
    async def fn012_list(
        self,
        prj_cd: Optional[str] = None,
        spc: Optional[str] = None,
        grp: Optional[str] = None,
    ) -> list[FN012]:
        # filters and values
        names = ["prj_cd", "spc", "grp"]
        values = [prj_cd, spc, grp]

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
        FROM FN012
        """

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{spc:str}/{grp:str")
    async def fn012_detail(self, prj_cd: str, spc: str, grp: str) -> Union[FN012, None]:
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
        FROM FN012 where prj_cd=? and spc=? and grp=?
        """

        data = await get_rows(sql, [prj_cd, spc, grp])

        return data
