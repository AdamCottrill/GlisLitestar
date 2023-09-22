from dataclasses import dataclass
from typing import Union


@dataclass
class FishNetDbTable:
    table_name: str
    keyfields: list[str]
    data_fields: list[str]

    # def __init__(self: table_name:str, keyfields: list[str], fields: list[str]):
    #     self.table_name = table_name
    #     self.keyfields = keyfields
    #     self.fields = fields

    def __str__(self) -> str:
        return self.table_name

    @property
    def fields(self) -> list[str]:
        return self.keyfields + self.data_fields

    @property
    def __key_fields_list(self) -> str:
        return ",".join([f"[{fld}]" for fld in self.keyfields])

    @property
    def __fields_list(self) -> str:
        return ",".join([f"[{fld}]" for fld in self.fields])

    def __where_clause(self, fields: Union[list[str], None] = None) -> str:
        if fields:
            field_list = [f"[{fld}]=?" for fld in fields]
        else:
            field_list = [f"[{fld}]=?" for fld in self.keyfields]

        return " AND ".join(field_list)

    def __qmarks(self, values: list[str]) -> str:
        """Return a comma separated list question mark place holders -
        one question mark for each element in values list."""
        return ",".join(["?"] * len(values))

    def update_one(self, values: dict) -> str:
        # TODO - verify that the fields are in the model
        # how do we know if the value should be set to NULL or wasn't specified?
        updates = ",".join([f"[{k}]=?" for k, v in values.items() if v is not None])

        sql = f"""
        Update [{self.table_name}] set
        {updates}
        where
        {self.__where_clause()}
        """

        return sql

    def create(self) -> str:
        # insert into [FN126] (
        # <field list>
        # ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)

        sql = f"""INSERT INTO [{self.table_name}]
        ({self.__fields_list})
        VALUES ({self.__qmarks(self.fields)})"""

        return sql

    def select(
        self, filters: Union[list[str], None] = None, order_by_keys: bool = True
    ) -> str:
        # SELECT
        # <snip>
        # FROM [FN126] ... where ... order by {self.__key_fields_list()}

        sql = f"SELECT {self.__fields_list} FROM [{self.table_name}]"

        if filters:
            where_clause = self.__where_clause(fields=filters)
            sql = sql + f" WHERE {where_clause}"

        if order_by_keys:
            sql = sql + f" order by {self.__key_fields_list}"

        return sql

    def select_one(self) -> str:
        # SELECT
        # <snip>
        # FROM [FN126] where
        # [prj_cd]=? and
        # [sam]=? and
        # [eff]=?
        #
        sql = f"""SELECT {self.__fields_list} FROM [{self.table_name}]
        WHERE {self.__where_clause()};"""

        return sql

    def delete_one(self) -> str:
        # DELETE FROM [FN126] where
        # [prj_cd]=? and
        # [sam]=? and
        # [eff]=?
        #
        sql = f"""DELETE FROM [{self.table_name}]
        WHERE {self.__where_clause()};"""

        return sql
