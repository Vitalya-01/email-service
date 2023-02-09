from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel
from dataBase.models.LinkedinCampaigns import LinkedinCampaigns


class Chains(BaseModel):
    id = AutoField()
    campaign_id = ForeignKeyField(
        column_name="campaign_id", field="id", model=LinkedinCampaigns
    )

    class Meta:
        table_name = "chains"
