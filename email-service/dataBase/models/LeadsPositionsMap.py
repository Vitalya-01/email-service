from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel
from dataBase.models.Leads import Leads
from dataBase.models.Positions import Positions


class LeadsPositionsMap(BaseModel):
    lead_id = ForeignKeyField(column_name="lead_id", field="id", model=Leads)
    position_id = ForeignKeyField(
        column_name="position_id", field="id", model=Positions
    )

    class Meta:
        table_name = "leads_positions_map"
        primary_key = False
