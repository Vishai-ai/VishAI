from app.plugins.base_plugin import BasePlugin


class MemoryPlugin(BasePlugin):
    """Handles memory operations."""

    def __init__(self, memory_manager):
        self.memory = memory_manager

    def execute(self, command: str):
        return self.memory.get_user_name()