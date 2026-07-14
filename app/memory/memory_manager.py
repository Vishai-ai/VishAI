import json
from pathlib import Path

from app.core.logger import logger


class MemoryManager:

    def __init__(self):
        self.memory_file = Path("data/memory/memory.json")
        self.memory = {}

        self.load_memory()

    def load_memory(self):
        try:
            with open(self.memory_file, "r", encoding="utf-8") as file:
                self.memory = json.load(file)

            logger.info("Memory Loaded Successfully")

        except Exception as e:
            logger.error(f"Memory Load Failed: {e}")

    def save_memory(self):
        try:
            with open(self.memory_file, "w", encoding="utf-8") as file:
                json.dump(self.memory, file, indent=4)

            logger.info("Memory Saved Successfully")

        except Exception as e:
            logger.error(f"Memory Save Failed: {e}")

    def get_user_name(self):
        return self.memory["user"]["name"]

    def set_user_name(self, name):
        self.memory["user"]["name"] = name
        self.save_memory()

    def add_note(self, note):
        """Add a note to memory."""
        self.memory["notes"].append(note)
        self.save_memory()

    def get_notes(self):
        """Return all saved notes."""
        return self.memory["notes"]

    def set_fact(self, key: str, value: str):
        """Store a user fact."""

        if "facts" not in self.memory:
            self.memory["facts"] = {}

        self.memory["facts"][key] = value
        self.save_memory()

    def get_fact(self, key: str):
        """Retrieve a stored user fact."""

        if "facts" not in self.memory:
            return None

        return self.memory["facts"].get(key)