from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel
from dataBase.models.SavedLeadLists import SavedLeadLists
from dataBase.models.Leads import Leads


class SavedLeadListLeadsMap(BaseModel):
    saved_lead_list_id = ForeignKeyField(
        column_name="saved_lead_list_id", field="id", model=SavedLeadLists
    )
    lead_id = ForeignKeyField(column_name="lead_id", field="id", model=Leads)

    class Meta:
        table_name = "saved_lead_list_leads_map"
        primary_key = False
