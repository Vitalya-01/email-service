from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel
from dataBase.models.JobOrders import JobOrders
from dataBase.models.SavedJobOrdersLists import SavedJobOrdersLists


class SavedJobOrdersListsJobOrdersMap(BaseModel):
    job_order_id = ForeignKeyField(
        column_name="job_order_id", field="id", model=JobOrders
    )
    saved_job_orders_list_id = ForeignKeyField(
        column_name="saved_job_orders_list_id", field="id", model=SavedJobOrdersLists
    )

    class Meta:
        table_name = "saved_job_orders_lists_job_orders_map"
        primary_key = False
