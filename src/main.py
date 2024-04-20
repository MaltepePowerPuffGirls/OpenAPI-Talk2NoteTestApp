
import config
from core.app import App
from service.openai_manager.openai_role import OpenAIRole

def run():

    app = App()
    
    role: OpenAIRole = app.roles["md-historian"]

    app.chat(role, {"prompt": "my beautiful text goes here"})

if __name__ == "__main__":
    run()