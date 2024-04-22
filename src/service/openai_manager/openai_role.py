
from typing import List

class OpenAIRole:

    excluded_params = ["role_name"]

    def __init__(self,
                 role_name: str,
                 actor: str,
                 method: str,
                 purpose: str,
                 temperature: str,
                 messages: List[str] = []) -> None:
        self.role_name = role_name
        self.actor = actor
        self.method = method
        self.purpose = purpose
        self.temperature = temperature
        self.messages = messages

    def object(self) -> dict:
        obj_dict = {}
        for attr, value in self.__dict__.items():
            if attr in self.excluded_params:
                continue
            obj_dict[attr] = value
        return obj_dict