from app.plugins.base_plugin import BasePlugin


class AutomationPlugin(BasePlugin):
    """Handles automation operations."""

    def __init__(self, automation_manager):
        self.automation = automation_manager

    def execute(self, command: str):
        return self.automation.execute(command)