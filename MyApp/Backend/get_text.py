from MyApp.DataBase.Controllers import TestMessagesController

def get_text_from_db()->str:
    return TestMessagesController.get(1).message
