
from dotenv import load_dotenv
load_dotenv()

from service.json_manager.json_manager import JsonManager
from core.app import App
from pathlib import Path
import os

BASE_PATH = Path(os.getcwd()) / "src"
DATA_PATH = BASE_PATH / "data"
OPEN_AI_PATH = DATA_PATH / "note-taker.json"

json = JsonManager.read_json(OPEN_AI_PATH)

## APPLICATION PARAMETERS ##
MODEL = json.get("model")
MAX_COMPLETION_TOKENS = json.get("max_completion_tokens")
MAX_PROMPT_TOKENS = json.get("max_prompt_tokens")
MAX_TOTAL_TOKENS = json.get("max_total_tokens")
RESPONSE_FORMAT = json.get("response_format")
DEFAULTS = json.get("default")

App().configure(
    model = MODEL,
    max_completion_tokens = MAX_COMPLETION_TOKENS,
    max_prompt_tokens = MAX_PROMPT_TOKENS,
    max_total_tokens = MAX_TOTAL_TOKENS,
    response_format = RESPONSE_FORMAT,
    defaults = DEFAULTS
)

App().generate_roles(json.get("roles"))