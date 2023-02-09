from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel
from dataBase.models.Proxies import Proxies
from dataBase.models.Actors import Actors


class Clients(BaseModel):
    id = AutoField()
    proxy_id = ForeignKeyField(
        column_name="proxy_id", field="id", model=Proxies, null=True
    )
    actor_id = ForeignKeyField(column_name="actor_id", field="id", model=Actors)
    first_name = CharField()
    last_name = CharField()
    linkedin_login = CharField()
    linkedin_password = CharField()
    email_login = CharField()
    email_password = CharField()
    query = CharField(null=True)
    current_cookie = TextField(null=True)

    class Meta:
        table_name = "clients"
