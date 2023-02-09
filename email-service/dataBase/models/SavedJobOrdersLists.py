from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel
from dataBase.models.LinkedinAccounts import LinkedinAccounts


class SavedJobOrdersLists(BaseModel):
    id = AutoField()
    actor_id = ForeignKeyField(
        column_name="actor_id", field="id", model=LinkedinAccounts
    )
    name = CharField()

    class Meta:
        table_name = "saved_job_orders_lists"
