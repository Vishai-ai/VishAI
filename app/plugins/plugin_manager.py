from app.plugins.memory_plugin import MemoryPlugin
from app.plugins.automation_plugin import AutomationPlugin


class PluginManager:
    """Loads and manages VishAI plugins."""

    def __init__(self):
        self.plugins = {
            "memory": MemoryPlugin(),
            "automation": AutomationPlugin(),
        }

    def get_plugin(self, name: str):
        return self.plugins.get(name)