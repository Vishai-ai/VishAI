from app.memory.memory_manager import MemoryManager
from app.automation.automation_manager import AutomationManager
from app.plugins.plugin_manager import PluginManager
from app.brain.brain_engine import BrainEngine


class AppContainer:
    """Creates all VishAI services."""

    def __init__(self):

        # Core
        self.memory = MemoryManager()

        # Automation
        self.automation = AutomationManager()

        # Plugins
        self.plugins = PluginManager(
            memory_manager=self.memory,
            automation_manager=self.automation,
        )

        # Brain
        self.brain = BrainEngine(
            memory_manager=self.memory,
            plugin_manager=self.plugins,
)