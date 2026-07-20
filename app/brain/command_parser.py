from app.automation.app_registry import AppRegistry


class CommandParser:
    """
    Extracts actionable information from user commands.
    """

    def __init__(self):

        self.registry = AppRegistry()

    def parse(self, text: str):

        text = text.lower().strip()

        action = None

        for trigger in [

            "open",
            "launch",
            "start",
            "run",
            "execute"

        ]:

            if trigger in text:

                action = "open_app"
                break

        app = self.registry.search(text)

        return {

            "action": action,

            "target": app,

            "text": text

        }