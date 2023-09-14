from litestar import Controller, get
from typing import Optional, Union
from schemas import FN127
from utils import get_data, get_rows


class FN127Controller(Controller):
    path = "api/fn127"

    @get("/")
    async def fn127_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
        eff: Optional[str] = None,
        spc: Optional[str] = None,
        grp: Optional[str] = None,
        fish: Optional[str] = None,
        ageid: Optional[str] = None,
    ) -> list[FN127]:
        # filters and values
        names = ["prj_cd", "sam", "eff", "spc", "grp", "fish", "ageid"]
        values = [prj_cd, sam, eff, spc, grp, fish, ageid]

        sql = """
        SELECT
         [PRJ_CD],
         [SAM],
         [EFF],
         [SPC],
         [GRP],
         [FISH],
         [AGEID],
         [PREFERRED],
         [AGEA],
         [AGEMT],
         [EDGE],
         [CONF],
         [NCA],
         [AGESTRM],
         [AGELAKE],
         [SPAWNCHKCNT],
         [AGE_FAIL],
         [COMMENT7]
        FROM [FN127]
        """

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{ageid:str}")
    async def fn127_detail(
        self, prj_cd: str, sam: str, eff: str, spc: str, grp: str, fish: str, ageid: str
    ) -> Union[FN127, None]:
        sql = """
        SELECT
                 [PRJ_CD],
         [SAM],
         [EFF],
         [SPC],
         [GRP],
         [FISH],
         [AGEID],
         [PREFERRED],
         [AGEA],
         [AGEMT],
         [EDGE],
         [CONF],
         [NCA],
         [AGESTRM],
         [AGELAKE],
         [SPAWNCHKCNT],
         [AGE_FAIL],
         [COMMENT7]
        FROM [FN127] where
        [prj_cd]=? and
        [sam]=? and
        [eff]=? and
        [spc]=? and
        [grp]=? and
        [fish]=? and
        [ageid]=?
        """

        data = await get_rows(sql, [prj_cd, sam, eff, spc, grp, fish, ageid])

        return data
