from litestar import Controller, get
from typing import Optional, Union
from schemas import FN125Tag
from utils import get_data, get_rows


class FN125TagController(Controller):
    path = "api/fn125_tag"

    @get("/")
    async def fn125_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
        eff: Optional[str] = None,
        spc: Optional[str] = None,
        grp: Optional[str] = None,
        fish: Optional[str] = None,
        fish_tag_id: Optional[str] = None,
    ) -> list[FN125Tag]:
        # filters and values
        names = ["prj_cd", "sam", "eff", "spc", "grp", "fish", "fish_tag_id"]
        values = [prj_cd, sam, eff, spc, grp, fish, fish_tag_id]

        sql = """
        SELECT
         [PRJ_CD],
         [SAM],
         [EFF],
         [SPC],
         [GRP],
         [FISH],
         [FISH_TAG_ID],
         [TAGID],
         [TAGDOC],
         [TAGSTAT],
         [CWTSEQ],
         [COMMENT_TAG]
        FROM [FN125_Tags]
        """

        data = await get_data(sql, names, values)

        return data

    @get(
        "/{prj_cd:str}/{sam:str}/{eff:str}/{spc:str}/{grp:str}/{fish:str}/{fish_tag_id:str}"
    )
    async def fn125_detail(
        self,
        prj_cd: str,
        sam: str,
        eff: str,
        spc: str,
        grp: str,
        fish: str,
        fish_tag_id: str,
    ) -> Union[FN125Tag, None]:
        sql = """
        SELECT
                 [PRJ_CD],
         [SAM],
         [EFF],
         [SPC],
         [GRP],
         [FISH],
         [FISH_TAG_ID],
         [TAGID],
         [TAGDOC],
         [TAGSTAT],
         [CWTSEQ],
         [COMMENT_TAG]
        FROM [FN125_Tags]
         where
        [prj_cd]=? and
        [sam]=? and
        [eff]=? and
        [spc]=? and
        [grp]=? and
        [fish]=? and
        [fish_tag_id] = ?
        """

        data = await get_rows(sql, [prj_cd, sam, eff, spc, grp, fish, fish_tag_id])

        return data
