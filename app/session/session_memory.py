class SessionMemory:
    """Stores current conversation history."""

    def __init__(self):
        self.messages = []

    def add(self, role: str, message: str):
        self.messages.append({
            "role": role,
            "message": message
        })

    def history(self):
        return self.messages

    def clear(self):
        self.messages.clear()