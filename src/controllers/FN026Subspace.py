from litestar import Controller, get

from schemas import FN026Subspace
from utils import get_rows


class FN026SubspaceController(Controller):
    path = "api/fn026_subspace"

    @get("/")
    async def fn026Subspace(self) -> list[FN026Subspace]:

        sql = """SELECT [PRJ_CD],
         [SPACE],
         [SUBSPACE],
         [SUBSPACE_DES],
         [DD_LAT],
         [DD_LON],
         [SIDEP_LT],
         [SIDEP_GE],
         [GRDEP_LT],
         [GRDEP_GE],
         [SUBSPACE_WT]
        FROM FN026_Subspace;
        """

        data = await get_rows(sql)

        return data
