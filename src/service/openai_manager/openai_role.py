
from typing import List

class OpenAIRole:

    def __init__(self,
                 actor: str,
                 method: str,
                 purpose: str,
                 temperature: str,
                 messages: List[str] = []) -> None:
        self.actor = actor
        self.method = method
        self.purpose = purpose
        self.temperature = temperature
        self.messages = messages

    def object(self) -> dict:
        obj_dict = {}
        for attr, value in self.__dict__.items():
            obj_dict[attr] = value
        return obj_dict