import json
from pathlib import Path


class ConfigManager:

    def __init__(self):
        self.config_path = Path("config/settings.json")

        with open(self.config_path, "r", encoding="utf-8") as file:
            self.settings = json.load(file)

    def get(self, key):
        return self.settings.get(key)