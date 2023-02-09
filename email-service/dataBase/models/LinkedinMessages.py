from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel
from dataBase.models.LinkedinDialogs import LinkedinDialogs


class LinkedinMessages(BaseModel):
    id = AutoField()
    dialog_id = ForeignKeyField(
        column_name="dialog_id", field="id", model=LinkedinDialogs
    )
    text = TextField()
    serial_number = SmallIntegerField()
    urn = TextField()

    class Meta:
        table_name = "linkedin_messages"
