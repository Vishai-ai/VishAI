from app.desktop.desktop_service import DesktopService


class CommandExecutor:

    def __init__(self):

        self.desktop = DesktopService()

    def execute(self, command: str):

        text = command.lower().strip()

        trigger_words = [

            "open",

            "launch",

            "start",

            "run",

            "execute",

            "khol",

            "khol"

        ]

        if any(word in text for word in trigger_words):

            return self.desktop.execute(text)

        return False, "Unknown command."