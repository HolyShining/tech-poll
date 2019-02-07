from abc import abstractmethod


class ISendMessage:

    @abstractmethod
    def send_message(self, status: int, message: str):
        pass
