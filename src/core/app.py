
from openai import OpenAI
from simple_term_menu import TerminalMenu

from typing import List

from service.openai_manager.openai_proxy import OpenAPIProxy
from service.openai_manager.openai_role import OpenAIRole

from core.module.logger import AppLogger
from logging import Logger

import core.cons as APP_C

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
    selected_role: OpenAI

    _logger: Logger = AppLogger(__name__)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.roles = {}

        return cls._instance
    
    def chat(self,
             role: OpenAIRole,
             content: dict) -> None:
        self._logger.debug("Sending request to OpenAPIProxy")
        response = OpenAPIProxy.send_request(self.object(), 
                                             role.object(), 
                                             content)

        self._logger.info(f"Response gathered with content: {content} - {role.role_name}")
        
        print()
        print("--------------------------------")
        print(" TEMPORARY DISPLAYER ".center(32, "-"))
        print("--------------------------------")
        print("Response status code:", response.status_code)
        print()
        print("Response text:", response.text)
        print("--------------------------------")
        print("--------------------------------")
        print()

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
        self._logger.info("Configuring the app")

        self.model = model
        self.max_completion_tokens = max_completion_tokens
        self.max_prompt_tokens = max_prompt_tokens
        self.max_total_tokens = max_total_tokens
        self.response_format = response_format
        self.defaults = defaults

    def generate_roles(self, roles: dict):
        self._logger.info("Generating roles")

        for role_name, role_content in roles.items():
            def_copy = self.defaults.copy()
            def_copy.update(role_content)
            
            role = OpenAIRole(**def_copy, role_name = role_name)

            self.roles[role_name] = role
            self._logger.info(f"Role generated: {role_name}")

    def init_menu(self):
        
        role_names = [role_name for role_name in self.roles.keys()]
        option_role_names = self.conv_role_names(role_names)
        options = [*option_role_names, "Quit"]

        main_menu = TerminalMenu(options, title="OpenAI Test Tool : Select an actor >")
        main_running = True

        while (main_running):
            option_index = main_menu.show()
            option_choice = options[option_index]

            if (option_choice == "Quit"):
                main_running = False
            else:
                self.selected_role = self.roles[role_names[option_index]]

            while (self.selected_role is not None):
                prompt = input(f" * prompt (role:{self.selected_role.role_name} / @back) : ")
                
                if prompt.lower() in ["exit", "back"]:
                    self.selected_role = None
                    continue

                self.chat(self.selected_role, {"prompt": prompt})

    @staticmethod
    def conv_role_names(role_names: List[str]) -> List[str]:
        return [f"[{index}] " + r_name.replace("-"," ").title() for index, r_name in enumerate(role_names, 1)]