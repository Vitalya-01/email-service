from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel
from dataBase.models.Clients import Clients
from dataBase.models.LinkedinInterlocutors import LinkedinInterlocutors


class LinkedinDialogs(BaseModel):
    id = AutoField()
    client_id = ForeignKeyField(column_name="client_id", field="id", model=Clients)
    interlocutor = ForeignKeyField(
        column_name="interlocutor_id", field="id", model=LinkedinInterlocutors
    )

    class Meta:
        table_name = "linkedin_dialogs"
