class ContextWindow:
    """Returns the latest conversation messages."""

    def __init__(self, max_messages=20):
        self.max_messages = max_messages

    def build(self, messages):
        return messages[-self.max_messages:]