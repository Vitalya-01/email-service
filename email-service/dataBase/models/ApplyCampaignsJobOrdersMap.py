from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel
from dataBase.models.ApplyCampaigns import ApplyCampaigns
from dataBase.models.JobOrders import JobOrders


class ApplyCampaignsJobOrdersMap(BaseModel):
    apply_campaign_id = ForeignKeyField(
        column_name="apply_campaign_id", field="id", model=ApplyCampaigns
    )
    job_order_id = ForeignKeyField(
        column_name="job_order_id", field="id", model=JobOrders
    )

    class Meta:
        table_name = "apply_campaigns_job_orders_map"
        primary_key = False
