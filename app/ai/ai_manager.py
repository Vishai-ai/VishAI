from app.ai.provider import AIProvider


class AIManager:
    """Controls which AI provider VishAI uses."""

    def __init__(self):
        self.provider = AIProvider.OLLAMA

    def current_provider(self):
        return self.provider.value

    def set_provider(self, provider: AIProvider):
        self.provider = provider