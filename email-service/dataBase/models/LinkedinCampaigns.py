from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel
from dataBase.models.Clients import Clients
from dataBase.db import EnumField


class LinkedinCampaigns(BaseModel):
    id = AutoField()
    client_id = ForeignKeyField(column_name="client_id", field="id", model=Clients)
    daily_followup_message_limit = SmallIntegerField()
    daily_invite_limit = SmallIntegerField()
    status = EnumField(
        choices=("ACTIVE", "PAUSED", "COMPLETED", "STOPPED"), null=True
    )  # USER-DEFINED
    # status = CharField(max_length=255, null=True)

    class Meta:
        table_name = "linkedin_campaigns"
