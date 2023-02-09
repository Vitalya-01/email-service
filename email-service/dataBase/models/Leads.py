from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel


class Leads(BaseModel):
    id = AutoField()
    first_name = CharField()
    last_name = CharField()
    avatar_link = TextField()
    profile_link = TextField(null=True)

    class Meta:
        table_name = "leads"
