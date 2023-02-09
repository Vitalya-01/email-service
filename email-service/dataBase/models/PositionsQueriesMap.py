from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel
from dataBase.models.Positions import Positions
from dataBase.models.Queries import Queries


class PositionsQueriesMap(BaseModel):
    position_id = ForeignKeyField(
        column_name="position_id", field="id", model=Positions
    )
    query_id = ForeignKeyField(column_name="query_id", field="id", model=Queries)

    class Meta:
        table_name = "positions_queries_map"
        primary_key = False
