import os
from pathlib import Path
import pdb

from typing import Union

import aioodbc


SRC_DB = os.path.abspath("../db/LEA_IA17_097_TEST.accdb")


def read_sql_file(sql_path: Path) -> str:
    """from Arjan Codes: Raw SQL, SQL Query Builder, or ORM?

    NOT NEEDED AFTER FishNetDataTable is fully adopted

    """
    return Path(sql_path).read_text()


async def get_rows(sql: str, args: list = None):
    constring = "DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={}"
    results = []
    async with aioodbc.connect(dsn=constring.format(SRC_DB)) as conn:
        async with conn.cursor() as cur:
            if args:
                await cur.execute(sql, args)
            else:
                await cur.execute(sql)
            colnames = [x[0].lower() for x in cur.description]
            rows = await cur.fetchall()

            for row in rows:
                results.append(dict(zip(colnames, row)))
    return results


async def run_sql(sql: str, values: list):
    """used for queries that don't return records - delete, post, put"""

    constring = "DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={}"
    async with aioodbc.connect(dsn=constring.format(SRC_DB)) as conn:
        async with conn.cursor() as cur:
            await cur.execute(sql, values)


async def get_data(sql: str, names, values):
    """build the where clause from the the values in names and values
    and tack it onto the sql statement before executing the sql
    statement.

    """
    if values.count(None) != len(values):
        where = args_to_where(names, values)
        sql = sql + where
        args = [val for val in values if val is not None]
        data = await get_rows(sql, args)
    else:
        data = await get_rows(sql)

    return data


def args_to_where(names: list[str], values: list[Union[str, int, None]]) -> str:
    """a little helper function to lake a list of filter names and
    assocaited values and return the where clause that can be added to
    out sql statement

    """

    args = [f"[{nm}]=?" for nm, val in zip(names, values) if val is not None]
    joined = " AND ".join(args)
    return f" WHERE {joined}"


def get_data_values(data):
    """Given a data class instance, return the its values as a list"""

    if hasattr(data, "dict"):
        # pydantic
        return [v for k, v in data.dict().items()]
    else:
        # msgspect
        return [v for k, v in data.__dict__.items()]


def update_clause(data):
    """Given a partial data class used for sql updates, build the
    update clause by returing the list of keys (field names) of the
    form [<key>]=? as a single comma separated list.

    NOT NEEDED AFTER FishNetDataTable is fully adopted

    """

    if hasattr(data, "dict"):
        # pydantic
        updates = ",".join(
            [f"[{k}]=?" for k, v in data.dict().items() if v is not None]
        )
    else:
        # msgspect
        updates = ",".join([f"[{k}]=?" for k, v in data.__dict__.items()])

    return updates
