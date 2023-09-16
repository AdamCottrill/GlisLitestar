from litestar import Controller, get, post, put, patch, delete
from typing import Optional, Union

from schemas import FN123NonFish, FN123NonFishPartial

from utils import (
    get_rows,
    get_data,
    read_sql_file,
    get_data_values,
    run_sql,
    update_clause,
)


class FN123NonFishController(Controller):
    path = "api/fn123_nonfish"

    @get("/")
    async def fn123_nonfish_list(
        self,
        prj_cd: Optional[str] = None,
        sam: Optional[str] = None,
        eff: Optional[str] = None,
        taxon: Optional[str] = None,
    ) -> list[FN123NonFish]:
        # filters and values
        names = ["prj_cd", "sam", "eff", "taxon"]
        values = [prj_cd, sam, eff, taxon]

        sql = read_sql_file("controllers/sql/FN123NonFish/get_item_list.sql")

        data = await get_data(sql, names, values)

        return data

    @get("/{prj_cd:str}/{sam:str}/{eff:str}/{taxon:str}")
    async def fn123_nonfish_detail(
        self,
        prj_cd: str,
        sam: str,
        eff: str,
        taxon: str,
    ) -> FN123NonFish:
        sql = read_sql_file("controllers/sql/FN123NonFish/get_item.sql")

        data = await get_rows(sql, [prj_cd, sam, eff, taxon])

        return data

    @post("/")
    async def fn123_nonfish_create(
        self,
        data: FN123NonFish,
    ) -> Union[FN123NonFish, None]:
        sql = read_sql_file("controllers/sql/FN123NonFish/create_item.sql")
        values = get_data_values(data)

        await run_sql(sql, values)

        return data

    @put("/{prj_cd:str}/{sam:str}/{eff:str}/{taxon:str}")
    async def fn123_nonfish_put(
        self,
        data: FN123NonFish,
        prj_cd: str,
        sam: str,
        eff: str,
        taxon: str,
    ) -> Union[FN123NonFish, None]:
        key_fields = [prj_cd, sam, eff, taxon]
        values = get_data_values(data)
        updates = update_clause(data)

        sql = f"""
        Update [FN123_NonFish] set
        {updates}
        where
        [prj_cd]=? and
        [sam]=? and
        [eff]=? and
        [taxon]=?
        """
        params = values + key_fields
        await run_sql(sql, params)

        return data

    @patch("/{prj_cd:str}/{sam:str}/{eff:str}/{taxon:str}")
    async def fn123_nonfish_patch(
        self,
        data: FN123NonFishPartial,
        prj_cd: str,
        sam: str,
        eff: str,
        taxon: str,
    ) -> Union[FN123NonFish, None]:
        key_fields = [prj_cd, sam, eff, taxon]
        values = get_data_values(data)
        updates = update_clause(data)

        sql = f"""
        Update [FN123_NonFish] set
        {updates}
        where
        [prj_cd]=? and
        [sam]=? and
        [eff]=? and
        [taxon]=?

        """
        params = values + key_fields
        await run_sql(sql, params)

        sql = read_sql_file("controllers/sql/FN123NonFish/get_item.sql")
        data = await get_rows(sql, key_fields)

        return data

    @delete("/{prj_cd:str}/{sam:str}/{eff:str}/{taxon:str}")
    async def fn123_nonfish_delete(
        self,
        prj_cd: str,
        sam: str,
        eff: str,
        taxon: str,
    ) -> None:
        sql = read_sql_file("controllers/sql/FN123NonFish/delete_item.sql")
        await run_sql(sql, [prj_cd, sam, eff, taxon])

        return None
