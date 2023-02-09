from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel
from dataBase.db import EnumField


class Companies(BaseModel):
    id = AutoField()
    name = CharField(unique=True)
    size = EnumField(
        choices=(
            "1-10 employees",
            "11-50 employees",
            "51-200 employees",
            "201-500 employees",
            "501-1, 000 employees",
            "1, 001-5, 000 employees",
            "5, 001-10, 000 employees",
        ),
        null=True,
    )  # USER-DEFINED
    # size = CharField(max_length=255, null=True)
    specialization = CharField(null=True)
    img_link = TextField()
    link = TextField()

    class Meta:
        table_name = "companies"
