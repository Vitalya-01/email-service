from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel


class LinkedinInterlocutors(BaseModel):
    id = AutoField()
    first_name = CharField()
    last_name = CharField()
    avatar_link = TextField()
    linkedin_link = TextField()

    class Meta:
        table_name = "linkedin_interlocutors"
