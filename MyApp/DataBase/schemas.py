from peewee import *
from MyApp.DataBase import path
db = SqliteDatabase(path, timeout=10)

class TestMessages(Model):
    id_message = PrimaryKeyField()
    message = TextField()
    class Meta:
        database = db



