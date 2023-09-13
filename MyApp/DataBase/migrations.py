import os
from peewee import *
from MyApp.DataBase.schemas import TestMessages
from MyApp.DataBase.Controllers import TestMessagesController
from MyApp.DataBase import path

def create_db(path:str):
    db = SqliteDatabase(path)
    model_classes = [TestMessages]
    db.create_tables(model_classes)


if __name__ == '__main__':
    create_db(path)
    TestMessagesController.new("Successfully tested!")
