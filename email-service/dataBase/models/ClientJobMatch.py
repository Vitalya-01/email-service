from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel
from dataBase.models.Clients import Clients
from dataBase.models.JobOrders import JobOrders


class ClientJobMatch(BaseModel):
    client_id = ForeignKeyField(
        column_name="client_id", field="id", model=Clients, null=False
    )
    job_order_id = ForeignKeyField(
        column_name="job_order_id", field="id", model=JobOrders, null=False
    )
    match = BooleanField(column_name="match", null=True)

    class Meta:
        indexes = (("client_id", "job_order_id"), True)
        table_name = "client_job_order_match"
        primary_key = False
