from litestar import Controller, get
from typing import Optional, Union
from schemas import FN126
from utils import get_data, get_rows


class FN126Controller(Controller):
    path = "api/fn126"

    @get("/")
    async def fn126_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
        eff: Optional[str] = None,
        spc: Optional[str] = None,
        grp: Optional[str] = None,
        fish: Optional[str] = None,
        food: Optional[str] = None,
    ) -> list[FN126]:
        # filters and values
        names = ["prj_cd", "sam", "eff", "spc", "grp", "fish", "food"]
        values = [prj_cd, sam, eff, spc, grp, fish, food]

        sql = """
        SELECT
         [PRJ_CD],
         [SAM],
         [EFF],
         [SPC],
         [GRP],
         [FISH],
         [FOOD],
         [TAXON],
         [FDCNT],
         [FDMES],
         [FDVAL],
         [LIFESTAGE],
         [COMMENT6]
        FROM [FN126]
        """

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{food:str}")
    async def fn126_detail(
        self, prj_cd: str, sam: str, eff: str, spc: str, grp: str, fish: str, food: str
    ) -> Union[FN126, None]:
        sql = """
        SELECT
         [PRJ_CD],
         [SAM],
         [EFF],
         [SPC],
         [GRP],
         [FISH],
         [FOOD],
         [TAXON],
         [FDCNT],
         [FDMES],
         [FDVAL],
         [LIFESTAGE],
         [COMMENT6]
        FROM [FN126] where
        [prj_cd]=? and
        [sam]=? and
        [eff]=? and
        [spc]=? and
        [grp]=? and
        [fish]=? and
        [food]=?
        """

        data = await get_rows(sql, [prj_cd, sam, eff, spc, grp, fish, food])

        return data
