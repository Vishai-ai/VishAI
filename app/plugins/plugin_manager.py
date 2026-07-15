from app.plugins.memory_plugin import MemoryPlugin
from app.plugins.automation_plugin import AutomationPlugin


class PluginManager:
    """Loads and manages VishAI plugins."""

    def __init__(self, memory_manager, automation_manager):

        self.plugins = {
            "memory": MemoryPlugin(memory_manager),
            "automation": AutomationPlugin(automation_manager),
        }

    def get_plugin(self, name: str):
        return self.plugins.get(name)