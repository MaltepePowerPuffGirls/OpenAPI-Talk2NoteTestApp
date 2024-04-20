
import json
from pathlib import Path

class JsonManager:

    @classmethod
    def read_json(cls, path: Path) -> dict:
        
        with open(path, "r") as f:
            json_object = json.load(f)
        
        return json_object