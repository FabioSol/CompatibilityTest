from MyApp.DataBase.schemas import TestMessages


class TestMessagesController:
    @staticmethod
    def new(message: str):
        return TestMessages.create(message=message)

    @staticmethod
    def get(id_message: int):
        return TestMessages.get(id_message=id_message)
