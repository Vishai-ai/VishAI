import json
from pathlib import Path

from app.core.base_engine import BaseEngine


class MemoryEngine(BaseEngine):
    """
    Long-term memory storage for VishAI.
    """

    def __init__(self):
        super().__init__("Memory")

        self.memory_file = Path("memory.json")

        self.data = {}

    def initialize(self):

        self.initialized = True

        if self.memory_file.exists():

            with open(self.memory_file, "r", encoding="utf-8") as f:

                self.data = json.load(f)

        else:

            self.data = {}

        return True

    def shutdown(self):

        with open(self.memory_file, "w", encoding="utf-8") as f:

            json.dump(self.data, f, indent=4)

        self.initialized = False

    def health(self):

        return {
            "engine": self.name,
            "initialized": self.initialized,
            "memories": len(self.data)
        }

    def remember(self, key, value):

        self.data[key] = value

    def recall(self, key):

        return self.data.get(key)

    def forget(self, key):

        if key in self.data:

            del self.data[key]