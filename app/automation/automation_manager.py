from app.automation.windows import WindowsAutomation
from app.automation.browser import BrowserAutomation
from app.automation.command_analyzer import CommandAnalyzer
from app.automation.app_registry import APP_REGISTRY
from app.core.logger import logger


class AutomationManager:
    """Central automation controller."""

    def __init__(self):
        self.windows = WindowsAutomation()
        self.browser = BrowserAutomation()
        self.analyzer = CommandAnalyzer()

        logger.info("Automation Manager Initialized")

    def execute(self, command: str):
        command_type, target = self.analyzer.analyze(command)

        if command_type == "app":

            executable = APP_REGISTRY.get(target)

            if executable:
                return self.windows.open_app(executable)

            return f"App '{target}' not found."

        elif command_type == "website":
            return self.browser.open_website(target)

        return "Unknown automation command."