from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel
from dataBase.models.LinkedinAccounts import LinkedinAccounts


class CampaignsDrafts(BaseModel):
    id = AutoField()
    actor_id = ForeignKeyField(
        column_name="actor_id", field="id", model=LinkedinAccounts
    )
    name = CharField()
    data = JSONField()

    class Meta:
        table_name = "campaigns_drafts"
