from litestar import Controller, get
from typing import Optional
from schemas import StreamDimension
from utils import get_data, get_rows


class StreamDimensionController(Controller):
    path = "api/stream_dimensions"

    @get("/")
    async def stream_dimension_list(
        self,
        prj_cd: Optional[str] = None,
        subspace: Optional[str] = None,
        metres_up: Optional[str] = None,
        metres_across: Optional[str] = None,
    ) -> list[StreamDimension]:
        names = ["prj_cd", "subspace", "metres_up", "metres_across"]
        values = [prj_cd, subspace, metres_up, metres_across]

        sql = """
           SELECT [PRJ_CD],
            [SUBSPACE],
            [METRES_UP],
            [METRES_ACROSS],
            [WIDTH],
            [DEPTH],
            [VELOCITY],
            [COMMENT]
           FROM [Stream_Dimensions]
        """

        data = await get_data(sql, names, values)

        return data

    @get("{prj_cd:str}/{subspace:str}/{metres_up:str}/{metres_across:str}")
    async def stream_dimension_detail_detail(
        self, prj_cd: str, subspace: str, metres_up: str, metres_across: str
    ) -> StreamDimension:
        sql = """
        SELECT [PRJ_CD],
            [SUBSPACE],
            [METRES_UP],
            [METRES_ACROSS],
            [WIDTH],
            [DEPTH],
            [VELOCITY],
            [COMMENT]
           FROM [Stream_Dimensions]
            where [prj_cd]= ? and  [subspace] = ? and [metres_up]=? and [metres_across]=?
            """

        data = await get_rows(
            sql,
            [prj_cd, subspace, metres_up, metres_across],
        )

        return data
