from app.desktop.application_manager import ApplicationManager


class DesktopService:

    def __init__(self):

        self.apps = ApplicationManager()

    def execute(self, command: str):

        text = command.lower()

        triggers = [

            "open",

            "launch",

            "start",

            "run"

        ]

        if any(trigger in text for trigger in triggers):

            words = text.split()

            app = words[-1]

            return self.apps.open(app)

        return False, "Desktop command not recognized."