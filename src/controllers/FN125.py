from litestar import Controller, get
from typing import Optional, Union
from schemas import FN125
from utils import get_data, get_rows


class FN125Controller(Controller):
    path = "api/fn125"

    @get("/")
    async def fn125_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
        eff: Optional[str] = None,
        spc: Optional[str] = None,
        grp: Optional[str] = None,
        fish: Optional[str] = None,
    ) -> list[FN125]:
        # filters and values
        names = ["prj_cd", "sam", "eff", "spc", "grp", "fish"]
        values = [prj_cd, sam, eff, spc, grp, fish]

        sql = """
        SELECT
         [PRJ_CD],
         [SAM],
         [EFF],
         [SPC],
         [GRP],
         [FISH],
         [FLEN],
         [TLEN],
         [GIRTH],
         [RWT],
         [EVISWT],
         [SEX],
         [MAT],
         [GON],
         [GONWT],
         [CLIPC],
         [CLIPA],
         [NODC],
         [NODA],
         [TISSUE],
         [AGEST],
         [FATE],
         [FDSAM],
         [STOM_CONTENTS_WT],
         [COMMENT5]
        FROM [FN125]
        """

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}")
    async def fn125_detail(
        self, prj_cd: str, sam: str, eff: str, spc: str, grp: str, fish: str
    ) -> Union[FN125, None]:
        sql = """
        SELECT
         [PRJ_CD],
         [SAM],
         [EFF],
         [SPC],
         [GRP],
         [FISH],
         [FLEN],
         [TLEN],
         [GIRTH],
         [RWT],
         [EVISWT],
         [SEX],
         [MAT],
         [GON],
         [GONWT],
         [CLIPC],
         [CLIPA],
         [NODC],
         [NODA],
         [TISSUE],
         [AGEST],
         [FATE],
         [FDSAM],
         [STOM_CONTENTS_WT],
         [COMMENT5]
        FROM [FN125]
         where
        [prj_cd]=? and
        [sam]=? and
        [eff]=? and
        [spc]=? and
        [grp]=? and
        [fish]=?
        """

        data = await get_rows(sql, [prj_cd, sam, eff, spc, grp, fish])

        return data
