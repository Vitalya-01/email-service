from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel
from dataBase.models.Chains import Chains
from dataBase.models.Leads import Leads
from dataBase.db import EnumField


class ChainsLeadsMap(BaseModel):
    chain_id = ForeignKeyField(column_name="chain_id", field="id", model=Chains)
    lead_id = ForeignKeyField(column_name="lead_id", field="id", model=Leads)
    next_message_index = SmallIntegerField(constraints=[SQL("DEFAULT 0")])
    status = EnumField(
        choices=("IN_PROGRESS", "SUCCEEDED", "FAILED"), null=True
    )  # USER-DEFINED
    # status = CharField(max_length=255, null=True)
    connection_status = BooleanField(null=True)

    class Meta:
        table_name = "chains_leads_map"
        primary_key = False
