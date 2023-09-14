from litestar import Controller, get
from typing import Optional, Union
from schemas import FN124
from utils import get_data, get_rows


class FN124Controller(Controller):
    path = "api/fn124"

    @get("/")
    async def fn124_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
        eff: Optional[str] = None,
        spc: Optional[str] = None,
        grp: Optional[str] = None,
        siz: Optional[str] = None,
    ) -> list[FN124]:
        # filters and values
        names = ["prj_cd", "sam", "eff", "spc", "grp", "siz"]
        values = [prj_cd, sam, eff, spc, grp, siz]

        sql = """
        SELECT
          [PRJ_CD],
          [SAM],
          [EFF],
          [SPC],
          [GRP],
          [SIZ],
          [SIZCNT],
          [COMMENT4]
        FROM [FN124]
        """

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{siz:str}")
    async def fn124_detail(
        self, prj_cd: str, sam: str, eff: str, spc: str, grp: str, siz: str
    ) -> Union[FN124, None]:
        sql = """
        SELECT
          [PRJ_CD],
          [SAM],
          [EFF],
          [SPC],
          [GRP],
          [SIZ],
          [SIZCNT],
          [COMMENT4]
        FROM [FN124]
         where
        [prj_cd]=? and
        [sam]=? and
        [eff]=? and
        [spc]=? and
        [grp]=? and
        [siz]=?
        """

        data = await get_rows(sql, [prj_cd, sam, eff, spc, grp, siz])

        return data
