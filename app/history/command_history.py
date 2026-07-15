from datetime import datetime


class CommandHistory:
    """Stores executed commands."""

    def __init__(self):
        self.commands = []

    def add(self, command: str):

        self.commands.append({
            "time": datetime.now().strftime("%H:%M:%S"),
            "command": command,
        })

    def list(self):

        return self.commands

    def clear(self):

        self.commands.clear()