class ContextManager:
    """Stores short-term conversation context."""

    def __init__(self):
        self.last_command = None
        self.last_app = None

    def update(self, command: str, app: str = None):
        self.last_command = command

        if app:
            self.last_app = app

    def get_last_command(self):
        return self.last_command

    def get_last_app(self):
        return self.last_app