from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel
from dataBase.models.LinkedinAccounts import LinkedinAccounts


class Tokens(BaseModel):
    id = AutoField()
    actor_id = ForeignKeyField(
        column_name="actor_id", field="id", model=LinkedinAccounts
    )
    token = CharField()

    class Meta:
        table_name = "tokens"
