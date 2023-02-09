from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel


class Proxies(BaseModel):
    id = AutoField()
    protocol = CharField(constraints=[SQL("DEFAULT 'http'::character varying")])
    host = CharField(unique=True)
    login = CharField(null=True)
    password = CharField(null=True)
    port = IntegerField()
    end_date = DateField(null=True)

    class Meta:
        table_name = "proxies"
