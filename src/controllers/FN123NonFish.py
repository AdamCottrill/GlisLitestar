from litestar import Controller, get, post, put, delete
from typing import Optional, Union
from .FishnetTables import FN123NonFish as FN123NonFishTable
from schemas import FN123NonFish

from utils import (
    get_rows,
    get_data,
    get_data_values,
    run_sql,
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

        sql = FN123NonFishTable.select(order_by_keys=False)
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
        sql = FN123NonFishTable.select_one()
        data = await get_rows(sql, [prj_cd, sam, eff, taxon])

        return data

    @post("/")
    async def fn123_nonfish_create(
        self,
        data: FN123NonFish,
    ) -> Union[FN123NonFish, None]:
        sql = FN123NonFishTable.create()
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

        sql = FN123NonFishTable.update_one(data.model_dump())

        params = values + key_fields
        await run_sql(sql, params)

        return data

    # @patch("/{prj_cd:str}/{sam:str}/{eff:str}/{taxon:str}")
    # async def fn123_nonfish_patch(
    #     self,
    #     data: FN123NonFishPartial,
    #     prj_cd: str,
    #     sam: str,
    #     eff: str,
    #     taxon: str,
    # ) -> Union[FN123NonFish, None]:
    #     key_fields = [prj_cd, sam, eff, taxon]
    #     values = get_data_values(data)
    #     updates = update_clause(data)

    #     sql = f"""
    #     Update [FN123_NonFish] set
    #     {updates}
    #     where
    #     [prj_cd]=? and
    #     [sam]=? and
    #     [eff]=? and
    #     [taxon]=?

    #     """
    #     params = values + key_fields
    #     await run_sql(sql, params)

    #     sql = read_sql_file("controllers/sql/FN123NonFish/get_item.sql")
    #     data = await get_rows(sql, key_fields)

    #     return data

    @delete("/{prj_cd:str}/{sam:str}/{eff:str}/{taxon:str}")
    async def fn123_nonfish_delete(
        self,
        prj_cd: str,
        sam: str,
        eff: str,
        taxon: str,
    ) -> None:
        sql = FN123NonFishTable.delete_one()
        await run_sql(sql, [prj_cd, sam, eff, taxon])

        return None
