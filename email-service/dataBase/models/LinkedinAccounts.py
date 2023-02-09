from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel


class LinkedinAccounts(BaseModel):
    id = AutoField()
    proxy_id = ForeignKeyField(
        column_name="proxy_id", field="id", model=Proxies, null=True
    )
    login = CharField()
    password = CharField()
    email = CharField()
    email_password = CharField()
    current_cookie = TextField(null=True)
    otp_key = CharField(null=True)
    invalid_cookies = BooleanField(constraints=[SQL("DEFAULT false")], null=True)
    busy = BooleanField(constraints=[SQL("DEFAULT false")])
    blocked = BooleanField(constraints=[SQL("DEFAULT false")])
    connections_per_day = IntegerField(constraints=[SQL("DEFAULT 0")])
    idle_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = "linkedin_accounts"
