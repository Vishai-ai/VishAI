from app.desktop.application_manager import ApplicationManager
from app.automation.app_registry import AppRegistry


class DesktopService:
    """
    Handles all desktop-related commands.

    Responsible only for:
    - Finding the application
    - Opening the application
    """

    def __init__(self):

        self.registry = AppRegistry()

        self.apps = ApplicationManager()

    def execute(self, command: str):

        text = command.lower().strip()

        app = self.registry.search(text)

        if app is None:

            return False, "Application not found."

        return self.apps.open(app)