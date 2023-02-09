from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel
from dataBase.models.Leads import Leads
from dataBase.models.FollowUps import FollowUps


class FollowUpsLeadsMap(BaseModel):
    lead_id = ForeignKeyField(column_name="lead_id", field="id", model=Leads)
    follow_up_id = ForeignKeyField(
        column_name="follow_up_id", field="id", model=FollowUps
    )
    text = TextField()
    approved = BooleanField()
    send_datetime = DateTimeField(null=True)

    class Meta:
        table_name = "follow_ups_leads_map"
        primary_key = False
