from litestar import Controller, get
from typing import Optional

from schemas import FN123NonFish
from utils import get_rows, get_data


class FN123NonFishController(Controller):
    path = "api/fn123_nonfish"

    @get("/")
    async def fn123_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
        eff: Optional[str] = None,
        taxon: Optional[str] = None,
    ) -> list[FN123NonFish]:
        # filters and values
        names = ["prj_cd", "sam", "eff", "taxon"]
        values = [prj_cd, sam, eff, taxon]

        sql = """SELECT
            [PRJ_CD],
            [SAM],
            [EFF],
            [TAXON],
            [CATCNT],
            [MORTCNT],
            [COMMENT3]
        FROM [FN123_NonFish]"""

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}")
    async def fn123_detail(
        self,
        prj_cd: str,
        sam: str,
        eff: str,
        taxon: str,
    ) -> FN123NonFish:
        sql = """SELECT
            [PRJ_CD],
            [SAM],
            [EFF],
            [TAXON],
            [CATCNT],
            [MORTCNT],
            [COMMENT3]
        FROM [FN123_NonFish] where prj_cd=? and sam=? and eff=? and taxon=?"""

        data = await get_rows(sql, [prj_cd, sam, eff, taxon])

        return data
