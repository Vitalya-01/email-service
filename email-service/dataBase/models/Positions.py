from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel
from dataBase.models.Companies import Companies


class Positions(BaseModel):
    id = AutoField()
    company_id = ForeignKeyField(
        column_name="company_id", field="id", model=Companies, null=True
    )
    title = CharField()

    class Meta:
        table_name = "positions"
