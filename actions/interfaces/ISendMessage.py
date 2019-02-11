from abc import abstractmethod


class ISendMessage:
    """Shows if class can send request messages"""
    @abstractmethod
    def send_message(self, status: int, message: str):
        pass
