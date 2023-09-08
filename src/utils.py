import os
from typing import Union
import aioodbc


SRC_DB = os.path.abspath("../db/LEA_IA17_097_TEST.accdb")


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


def args_to_where(names: list[str], values: list[Union[str, int, None]]) -> str:
    """a little helper function to lake a list of filter names and
    assocaited values and return the where clause that can be added to
    out sql statement

    """

    args = [f"[{nm}]=?" for nm, val in zip(names, values) if val is not None]
    joined = " AND ".join(args)
    return f" WHERE {joined}"
