from app.automation.automation_engine import AutomationEngine


class CommandExecutor:

    def __init__(self):
        self.automation = AutomationEngine()
        self.automation.initialize()

    def execute(self, command: str):

        text = command.lower().strip()

        # ---------------- Applications ----------------

        app_commands = {

            "notepad": self.automation.open_notepad,
            "calculator": self.automation.open_calculator,
            "calc": self.automation.open_calculator,
            "paint": self.automation.open_paint,
            "cmd": self.automation.open_cmd,
            "command prompt": self.automation.open_cmd,

        }

        trigger_words = [

            "open",
            "launch",
            "start",
            "run",
            "execute",
            "khol",
            "khol",
        ]

        for app, function in app_commands.items():

            if app in text:

                if any(word in text for word in trigger_words):

                    function()

                    return f"Opening {app.title()}..."

        return None