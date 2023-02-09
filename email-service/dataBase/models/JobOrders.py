from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel
from dataBase.db import EnumField


class JobOrders(BaseModel):
    id = AutoField()
    company_id = ForeignKeyField(column_name="company_id", field="id", model=Companies)
    linkedin_job_id = BigIntegerField(unique=True)
    title = TextField()
    query_location = TextField(null=True)
    place = TextField(null=True)
    job_type = EnumField(
        choices=("On-site", "Remote", "Hybrid"), null=True
    )  # USER-DEFINED
    # job_type = CharField(max_length=255, null=True)
    description = TextField()
    description_html = TextField(null=True)
    apply_link = TextField(null=True)
    link = TextField(unique=True)
    lang = CharField(max_length=10, null=True)

    class Meta:
        table_name = "job_orders"
