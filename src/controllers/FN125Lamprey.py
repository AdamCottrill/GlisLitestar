from litestar import Controller, get
from typing import Optional, Union
from schemas import FN125Lamprey
from utils import get_data, get_rows


class FN125LampreyController(Controller):
    path = "api/fn125_lamprey"

    @get("/")
    async def fn125_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
        eff: Optional[str] = None,
        spc: Optional[str] = None,
        grp: Optional[str] = None,
        fish: Optional[str] = None,
        lamid: Optional[str] = None,
    ) -> list[FN125Lamprey]:
        # filters and values
        names = ["prj_cd", "sam", "eff", "spc", "grp", "fish", "lamid"]
        values = [prj_cd, sam, eff, spc, grp, fish, lamid]

        sql = """
        SELECT
          [PRJ_CD],
          [SAM],
          [EFF],
          [SPC],
          [GRP],
          [FISH],
          [LAMID],
          [XLAM],
          [LAMIJC_TYPE],
          [LAMIJC_SIZE],
          [COMMENT_LAM]
        FROM [FN125_Lamprey]
        """

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{lamid:str}")
    async def fn125_detail(
        self, prj_cd: str, sam: str, eff: str, spc: str, grp: str, fish: str, lamid: str
    ) -> Union[FN125Lamprey, None]:
        sql = """
        SELECT
          [PRJ_CD],
          [SAM],
          [EFF],
          [SPC],
          [GRP],
          [FISH],
          [LAMID],
          [XLAM],
          [LAMIJC_TYPE],
          [LAMIJC_SIZE],
          [COMMENT_LAM]
        FROM [FN125_Lamprey]
         where
        [prj_cd]=? and
        [sam]=? and
        [eff]=? and
        [spc]=? and
        [grp]=? and
        [fish]=? and
        [lamid] = ?
        """

        data = await get_rows(sql, [prj_cd, sam, eff, spc, grp, fish, lamid])

        return data
