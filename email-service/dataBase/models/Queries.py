from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel


class Queries(BaseModel):
    id = AutoField()
    filters = JSONField(null=True)
    query = CharField()

    class Meta:
        table_name = "queries"
