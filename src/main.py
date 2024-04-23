
import config
from core.app import App
from service.openai_manager.openai_role import OpenAIRole

def run():

    app = App()
    app.init_menu()

if __name__ == "__main__":
    run()