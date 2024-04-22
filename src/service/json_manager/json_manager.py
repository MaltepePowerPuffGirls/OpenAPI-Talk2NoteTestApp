
import json
from pathlib import Path

from core.module.logger import AppLogger
from logging import Logger

class JsonManager:

    _logger: Logger = AppLogger(__name__)

    @classmethod
    def read_json(cls, path: Path) -> dict:
        try:
            with open(path, "r") as f:
                json_object = json.load(f)
            cls._logger.debug(f"Successfully read JSON from {path}")
            return json_object
        except FileNotFoundError:
            cls._logger.error(f"File not found: {path}")
            raise
        except json.JSONDecodeError as e:
            cls._logger.error(f"Error decoding JSON file {path}: {e}")
            raise