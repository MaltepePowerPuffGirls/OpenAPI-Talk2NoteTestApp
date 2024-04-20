
from openai import OpenAI

from service.openai_manager.openai_proxy import OpenAPIProxy
from service.openai_manager.openai_role import OpenAIRole

from typing import Dict

class App:
    
    _instance = None
    
    model: str = "gpt-3.5-turbo"
    max_completion_tokens: int 
    max_prompt_tokens: int
    max_total_tokens: int
    response_format: str
    defaults: dict

    roles: Dict[str, OpenAIRole]

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.roles = {}

        return cls._instance
    
    def chat(self,
             role: OpenAIRole,
             content: dict) -> None:
        
        response = OpenAPIProxy.send_request(self.object(), 
                                             role.object(), 
                                             content)
    
        print("Response status code:", response.status_code)
        print("Response text:", response.text)

    def object(self):
        return {
            "model": self.model,
            "max_completion_tokens": self.max_completion_tokens,
            "max_prompt_tokens": self.max_prompt_tokens,
            "max_total_tokens": self.max_total_tokens,
            "response_format": self.response_format
        }

    def configure(self,
                  model: str,
                  max_completion_tokens: int, 
                  max_prompt_tokens: int,
                  max_total_tokens: int,
                  response_format: dict[str, str],
                  defaults: dict[str, any]):
        
        self.model = model
        self.max_completion_tokens = max_completion_tokens
        self.max_prompt_tokens = max_prompt_tokens
        self.max_total_tokens = max_total_tokens
        self.response_format = response_format
        self.defaults = defaults

    def generate_roles(self, roles: dict):

        for role_name, role_content in roles.items():
            def_copy = self.defaults.copy()
            def_copy.update(role_content)
            
            role = OpenAIRole(**def_copy)

            self.roles[role_name] = role