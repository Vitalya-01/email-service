from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel
from dataBase.models.Actors import Actors


class SavedLeadLists(BaseModel):
    id = AutoField()
    actor_id = ForeignKeyField(column_name="actor_id", field="id", model=Actors)
    name = CharField()

    class Meta:
        table_name = "saved_lead_lists"
