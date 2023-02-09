from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel
from dataBase.db import EnumField


class ApplyCampaigns(BaseModel):
    id = AutoField()
    client_id = ForeignKeyField(column_name="client_id", field="id", model=Clients)
    name = CharField()
    status = EnumField(
        choices=("ACTIVE", "PAUSED", "COMPLETED", "STOPPED"), null=True
    )  # USER-DEFINED
    # status = CharField(max_length=255, null=True)

    class Meta:
        table_name = "apply_campaigns"
