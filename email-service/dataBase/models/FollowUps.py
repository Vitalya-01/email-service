from playhouse.postgres_ext import *
from dataBase.models.BaseModel import BaseModel
from dataBase.models.Chains import Chains


class FollowUps(BaseModel):
    id = AutoField()
    chain_id = ForeignKeyField(column_name="chain_id", field="id", model=Chains)
    text = TextField()
    number_in_chain_number = SmallIntegerField()
    time_delta = IntegerField(null=False)  # interval

    class Meta:
        table_name = "follow_ups"
